# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.094x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 390 ms: 1.26x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                      |
| html5lib       | 65.1 ms                                                               | 71.6 ms: 1.10x slower                                                       |
| tornado_http   | 136 ms                                                                | 148 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.17x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                        |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 608 ms: 1.28x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 758 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.25x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| float          | 92.1 ms                                                               | 95.9 ms: 1.04x slower                                                       |
| nbody          | 105 ms                                                                | 117 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                       |
| regex_compile  | 137 ms                                                                | 177 ms: 1.29x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                        |
| xml_etree_process    | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                       |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                                       |
| tomli_loads          | 2.59 sec                                                              | 2.71 sec: 1.05x slower                                                      |
| pickle_pure_python   | 365 us                                                                | 394 us: 1.08x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.04x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                       |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                       |
| django_template | 40.7 ms                                                               | 53.3 ms: 1.31x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 84.8 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.24x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 544 ms: 1.36x faster                                                        |
| async_tree_none            | 624 ms                                                                | 469 ms: 1.33x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 448 ms: 1.29x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 608 ms: 1.28x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 39.6 us: 1.25x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.20x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 758 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                        |
| deepcopy                   | 446 us                                                                | 386 us: 1.15x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 21.6 ms: 1.14x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.12x faster                                                      |
| logging_format             | 8.34 us                                                               | 8.04 us: 1.04x faster                                                       |
| logging_simple             | 7.63 us                                                               | 7.42 us: 1.03x faster                                                       |
| deepcopy_reduce            | 4.10 us                                                               | 4.03 us: 1.02x faster                                                       |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| comprehensions             | 25.4 us                                                               | 25.5 us: 1.01x slower                                                       |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| asyncio_websockets         | 658 ms                                                                | 665 ms: 1.01x slower                                                        |
| json                       | 5.54 ms                                                               | 5.67 ms: 1.02x slower                                                       |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                        |
| thrift                     | 937 us                                                                | 965 us: 1.03x slower                                                        |
| mako                       | 12.9 ms                                                               | 13.3 ms: 1.03x slower                                                       |
| xml_etree_process          | 79.0 ms                                                               | 81.6 ms: 1.03x slower                                                       |
| mdp                        | 3.41 sec                                                              | 3.53 sec: 1.03x slower                                                      |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                                       |
| bench_thread_pool          | 1.31 ms                                                               | 1.36 ms: 1.04x slower                                                       |
| float                      | 92.1 ms                                                               | 95.9 ms: 1.04x slower                                                       |
| async_generators           | 491 ms                                                                | 513 ms: 1.04x slower                                                        |
| scimark_lu                 | 146 ms                                                                | 152 ms: 1.05x slower                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.71 sec: 1.05x slower                                                      |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 91.2 ms: 1.05x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.93 ms: 1.06x slower                                                       |
| scimark_sor                | 150 ms                                                                | 161 ms: 1.07x slower                                                        |
| pickle_pure_python         | 365 us                                                                | 394 us: 1.08x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 30.7 ms: 1.08x slower                                                       |
| tornado_http               | 136 ms                                                                | 148 ms: 1.09x slower                                                        |
| deltablue                  | 4.12 ms                                                               | 4.51 ms: 1.09x slower                                                       |
| scimark_fft                | 418 ms                                                                | 459 ms: 1.10x slower                                                        |
| html5lib                   | 65.1 ms                                                               | 71.6 ms: 1.10x slower                                                       |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.4 ms: 1.10x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 94.3 ms: 1.11x slower                                                       |
| nbody                      | 105 ms                                                                | 117 ms: 1.12x slower                                                        |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.12x slower                                                        |
| telco                      | 8.51 ms                                                               | 9.55 ms: 1.12x slower                                                       |
| coverage                   | 87.3 ms                                                               | 98.7 ms: 1.13x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                       |
| pyflate                    | 559 ms                                                                | 652 ms: 1.17x slower                                                        |
| logging_silent             | 127 ns                                                                | 149 ns: 1.17x slower                                                        |
| fannkuch                   | 443 ms                                                                | 522 ms: 1.18x slower                                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 187 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 215 us: 1.19x slower                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.75 ms: 1.19x slower                                                       |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.42 ms: 1.20x slower                                                       |
| go                         | 157 ms                                                                | 189 ms: 1.20x slower                                                        |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                                      |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.62 sec: 1.21x slower                                                      |
| spectral_norm              | 131 ms                                                                | 161 ms: 1.23x slower                                                        |
| genshi_text                | 27.4 ms                                                               | 34.0 ms: 1.24x slower                                                       |
| sqlglot_normalize          | 126 ms                                                                | 157 ms: 1.24x slower                                                        |
| chaos                      | 71.4 ms                                                               | 89.8 ms: 1.26x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 78.4 ms: 1.26x slower                                                       |
| 2to3                       | 308 ms                                                                | 390 ms: 1.26x slower                                                        |
| pylint                     | 355 ms                                                                | 450 ms: 1.27x slower                                                        |
| richards_super             | 58.5 ms                                                               | 74.4 ms: 1.27x slower                                                       |
| sympy_str                  | 280 ms                                                                | 359 ms: 1.28x slower                                                        |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.29x slower                                                       |
| regex_compile              | 137 ms                                                                | 177 ms: 1.29x slower                                                        |
| nqueens                    | 99.2 ms                                                               | 130 ms: 1.31x slower                                                        |
| django_template            | 40.7 ms                                                               | 53.3 ms: 1.31x slower                                                       |
| sympy_expand               | 454 ms                                                                | 597 ms: 1.32x slower                                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 82.0 ms: 1.34x slower                                                       |
| generators                 | 43.5 ms                                                               | 59.1 ms: 1.36x slower                                                       |
| sympy_integrate            | 21.6 ms                                                               | 29.6 ms: 1.37x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.26 sec: 1.37x slower                                                      |
| gc_traversal               | 4.40 ms                                                               | 6.12 ms: 1.39x slower                                                       |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                      |
| sympy_sum                  | 154 ms                                                                | 216 ms: 1.40x slower                                                        |
| genshi_xml                 | 60.6 ms                                                               | 84.8 ms: 1.40x slower                                                       |
| richards                   | 50.9 ms                                                               | 71.9 ms: 1.41x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 10.4 ms: 1.49x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.64 ms: 1.90x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 1.51 sec: 213.77x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x slower                                                                |

Benchmark hidden because not significant (5): xml_etree_parse, coroutines, xml_etree_iterparse, xml_etree_generate, raytrace
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.094x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.10x