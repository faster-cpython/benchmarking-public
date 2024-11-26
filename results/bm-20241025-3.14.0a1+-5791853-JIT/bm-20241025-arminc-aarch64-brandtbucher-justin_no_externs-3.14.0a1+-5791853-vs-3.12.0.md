# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.090x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 385 ms: 1.25x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.66 sec: 1.23x slower                                                      |
| html5lib       | 65.1 ms                                                               | 71.5 ms: 1.10x slower                                                       |
| tornado_http   | 136 ms                                                                | 148 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 535 ms: 1.38x faster                                                        |
| async_tree_none            | 624 ms                                                                | 465 ms: 1.34x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 595 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 442 ms: 1.30x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 738 ms: 1.20x faster                                                        |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| float          | 92.1 ms                                                               | 96.2 ms: 1.04x slower                                                       |
| nbody          | 105 ms                                                                | 119 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.06x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                       |
| regex_compile  | 137 ms                                                                | 176 ms: 1.28x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.10x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 186 ms: 1.05x faster                                                        |
| xml_etree_iterparse  | 150 ms                                                                | 148 ms: 1.01x faster                                                        |
| xml_etree_generate   | 112 ms                                                                | 111 ms: 1.01x faster                                                        |
| xml_etree_process    | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                       |
| unpickle_pure_python | 260 us                                                                | 268 us: 1.03x slower                                                        |
| tomli_loads          | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                      |
| json_loads           | 30.7 us                                                               | 31.7 us: 1.03x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 387 us: 1.06x slower                                                        |
| json_dumps           | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.03x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                       |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                       |
| django_template | 40.7 ms                                                               | 52.3 ms: 1.29x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 84.5 ms: 1.40x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.24x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 535 ms: 1.38x faster                                                        |
| async_tree_none            | 624 ms                                                                | 465 ms: 1.34x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 595 ms: 1.31x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 442 ms: 1.30x faster                                                        |
| deepcopy_memo              | 49.6 us                                                               | 39.0 us: 1.27x faster                                                       |
| async_tree_io              | 1.41 sec                                                              | 1.17 sec: 1.21x faster                                                      |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 761 ms: 1.20x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 738 ms: 1.20x faster                                                        |
| deepcopy                   | 446 us                                                                | 378 us: 1.18x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 21.3 ms: 1.15x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.25 sec: 1.13x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 186 ms: 1.05x faster                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 4.01 us: 1.02x faster                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 148 ms: 1.01x faster                                                        |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| xml_etree_generate         | 112 ms                                                                | 111 ms: 1.01x faster                                                        |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                        |
| pidigits                   | 233 ms                                                                | 235 ms: 1.01x slower                                                        |
| mdp                        | 3.41 sec                                                              | 3.49 sec: 1.02x slower                                                      |
| xml_etree_process          | 79.0 ms                                                               | 80.9 ms: 1.02x slower                                                       |
| thrift                     | 937 us                                                                | 963 us: 1.03x slower                                                        |
| unpickle_pure_python       | 260 us                                                                | 268 us: 1.03x slower                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.67 sec: 1.03x slower                                                      |
| json_loads                 | 30.7 us                                                               | 31.7 us: 1.03x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 151 ms: 1.03x slower                                                        |
| async_generators           | 491 ms                                                                | 510 ms: 1.04x slower                                                        |
| float                      | 92.1 ms                                                               | 96.2 ms: 1.04x slower                                                       |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                       |
| python_startup_no_site     | 8.37 ms                                                               | 8.77 ms: 1.05x slower                                                       |
| mako                       | 12.9 ms                                                               | 13.7 ms: 1.06x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 387 us: 1.06x slower                                                        |
| crypto_pyaes               | 86.6 ms                                                               | 92.0 ms: 1.06x slower                                                       |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                       |
| scimark_monte_carlo        | 85.1 ms                                                               | 90.7 ms: 1.07x slower                                                       |
| scimark_fft                | 418 ms                                                                | 450 ms: 1.08x slower                                                        |
| deltablue                  | 4.12 ms                                                               | 4.45 ms: 1.08x slower                                                       |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                       |
| tornado_http               | 136 ms                                                                | 148 ms: 1.09x slower                                                        |
| scimark_sor                | 150 ms                                                                | 164 ms: 1.09x slower                                                        |
| html5lib                   | 65.1 ms                                                               | 71.5 ms: 1.10x slower                                                       |
| meteor_contest             | 112 ms                                                                | 125 ms: 1.11x slower                                                        |
| coverage                   | 87.3 ms                                                               | 98.5 ms: 1.13x slower                                                       |
| telco                      | 8.51 ms                                                               | 9.67 ms: 1.14x slower                                                       |
| nbody                      | 105 ms                                                                | 119 ms: 1.14x slower                                                        |
| json_dumps                 | 12.3 ms                                                               | 14.0 ms: 1.14x slower                                                       |
| sqlalchemy_imperative      | 16.7 ms                                                               | 19.2 ms: 1.15x slower                                                       |
| fannkuch                   | 443 ms                                                                | 510 ms: 1.15x slower                                                        |
| pyflate                    | 559 ms                                                                | 645 ms: 1.15x slower                                                        |
| logging_silent             | 127 ns                                                                | 147 ns: 1.16x slower                                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.20 ms: 1.16x slower                                                       |
| go                         | 157 ms                                                                | 185 ms: 1.18x slower                                                        |
| sqlglot_parse              | 1.46 ms                                                               | 1.73 ms: 1.18x slower                                                       |
| sqlalchemy_declarative     | 157 ms                                                                | 188 ms: 1.20x slower                                                        |
| spectral_norm              | 131 ms                                                                | 156 ms: 1.20x slower                                                        |
| pycparser                  | 1.26 sec                                                              | 1.51 sec: 1.20x slower                                                      |
| sqlglot_transpile          | 1.83 ms                                                               | 2.21 ms: 1.21x slower                                                       |
| typing_runtime_protocols   | 181 us                                                                | 219 us: 1.21x slower                                                        |
| docutils                   | 2.98 sec                                                              | 3.66 sec: 1.23x slower                                                      |
| richards_super             | 58.5 ms                                                               | 71.8 ms: 1.23x slower                                                       |
| pylint                     | 355 ms                                                                | 437 ms: 1.23x slower                                                        |
| chaos                      | 71.4 ms                                                               | 88.3 ms: 1.24x slower                                                       |
| sqlglot_normalize          | 126 ms                                                                | 156 ms: 1.24x slower                                                        |
| 2to3                       | 308 ms                                                                | 385 ms: 1.25x slower                                                        |
| genshi_text                | 27.4 ms                                                               | 34.6 ms: 1.26x slower                                                       |
| dulwich_log                | 62.0 ms                                                               | 78.8 ms: 1.27x slower                                                       |
| regex_compile              | 137 ms                                                                | 176 ms: 1.28x slower                                                        |
| sympy_str                  | 280 ms                                                                | 358 ms: 1.28x slower                                                        |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                       |
| django_template            | 40.7 ms                                                               | 52.3 ms: 1.29x slower                                                       |
| sympy_expand               | 454 ms                                                                | 590 ms: 1.30x slower                                                        |
| sqlglot_optimize           | 61.3 ms                                                               | 81.4 ms: 1.33x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 132 ms: 1.33x slower                                                        |
| generators                 | 43.5 ms                                                               | 58.3 ms: 1.34x slower                                                       |
| richards                   | 50.9 ms                                                               | 68.5 ms: 1.34x slower                                                       |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.35x slower                                                      |
| sympy_integrate            | 21.6 ms                                                               | 29.3 ms: 1.36x slower                                                       |
| pprint_pformat             | 1.88 sec                                                              | 2.61 sec: 1.38x slower                                                      |
| genshi_xml                 | 60.6 ms                                                               | 84.5 ms: 1.40x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 216 ms: 1.40x slower                                                        |
| gc_traversal               | 4.40 ms                                                               | 6.26 ms: 1.42x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 10.5 ms: 1.51x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.65 ms: 1.90x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 1.27 sec: 180.52x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.17x slower                                                                |

Benchmark hidden because not significant (6): logging_simple, coroutines, logging_format, raytrace, comprehensions, json
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.090x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.11x