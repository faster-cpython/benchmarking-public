# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-aarch64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.123x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 401 ms: 1.30x slower                                                        |
| docutils       | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                      |
| html5lib       | 65.1 ms                                                               | 73.0 ms: 1.12x slower                                                       |
| tornado_http   | 136 ms                                                                | 152 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.20x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                                        |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 450 ms: 1.28x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 606 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 768 ms: 1.19x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                      |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.12x faster                                                      |
| Geometric mean             | (ref)                                                                 | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| float          | 92.1 ms                                                               | 98.7 ms: 1.07x slower                                                       |
| nbody          | 105 ms                                                                | 132 ms: 1.26x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| regex_effbot   | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                       |
| regex_v8       | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                       |
| regex_compile  | 137 ms                                                                | 183 ms: 1.34x slower                                                        |
| Geometric mean | (ref)                                                                 | 1.11x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 189 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 150 ms                                                                | 151 ms: 1.01x slower                                                        |
| json_loads           | 30.7 us                                                               | 31.8 us: 1.04x slower                                                       |
| xml_etree_generate   | 112 ms                                                                | 117 ms: 1.05x slower                                                        |
| unpickle_pure_python | 260 us                                                                | 275 us: 1.06x slower                                                        |
| xml_etree_process    | 79.0 ms                                                               | 86.3 ms: 1.09x slower                                                       |
| pickle_pure_python   | 365 us                                                                | 411 us: 1.13x slower                                                        |
| tomli_loads          | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                      |
| json_dumps           | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                                 | 1.07x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                       |
| python_startup         | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                       |
| Geometric mean         | (ref)                                                                 | 1.16x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                       |
| genshi_text     | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                       |
| django_template | 40.7 ms                                                               | 55.3 ms: 1.36x slower                                                       |
| genshi_xml      | 60.6 ms                                                               | 86.4 ms: 1.43x slower                                                       |
| Geometric mean  | (ref)                                                                 | 1.29x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 740 ms                                                                | 542 ms: 1.37x faster                                                        |
| async_tree_none            | 624 ms                                                                | 473 ms: 1.32x faster                                                        |
| async_tree_none_tg         | 577 ms                                                                | 450 ms: 1.28x faster                                                        |
| async_tree_memoization     | 777 ms                                                                | 606 ms: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 742 ms: 1.19x faster                                                        |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 768 ms: 1.19x faster                                                        |
| async_tree_io              | 1.41 sec                                                              | 1.20 sec: 1.18x faster                                                      |
| deepcopy_memo              | 49.6 us                                                               | 42.3 us: 1.17x faster                                                       |
| deepcopy                   | 446 us                                                                | 392 us: 1.14x faster                                                        |
| pathlib                    | 24.5 ms                                                               | 21.9 ms: 1.12x faster                                                       |
| async_tree_io_tg           | 1.40 sec                                                              | 1.26 sec: 1.12x faster                                                      |
| xml_etree_parse            | 195 ms                                                                | 189 ms: 1.03x faster                                                        |
| regex_dna                  | 254 ms                                                                | 251 ms: 1.01x faster                                                        |
| coroutines                 | 29.0 ms                                                               | 28.6 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 150 ms                                                                | 151 ms: 1.01x slower                                                        |
| pidigits                   | 233 ms                                                                | 234 ms: 1.01x slower                                                        |
| asyncio_websockets         | 658 ms                                                                | 664 ms: 1.01x slower                                                        |
| deepcopy_reduce            | 4.10 us                                                               | 4.19 us: 1.02x slower                                                       |
| async_generators           | 491 ms                                                                | 505 ms: 1.03x slower                                                        |
| json                       | 5.54 ms                                                               | 5.72 ms: 1.03x slower                                                       |
| thrift                     | 937 us                                                                | 971 us: 1.04x slower                                                        |
| json_loads                 | 30.7 us                                                               | 31.8 us: 1.04x slower                                                       |
| mdp                        | 3.41 sec                                                              | 3.55 sec: 1.04x slower                                                      |
| raytrace                   | 353 ms                                                                | 368 ms: 1.04x slower                                                        |
| bench_thread_pool          | 1.31 ms                                                               | 1.37 ms: 1.05x slower                                                       |
| xml_etree_generate         | 112 ms                                                                | 117 ms: 1.05x slower                                                        |
| python_startup_no_site     | 8.37 ms                                                               | 8.78 ms: 1.05x slower                                                       |
| unpickle_pure_python       | 260 us                                                                | 275 us: 1.06x slower                                                        |
| regex_effbot               | 4.64 ms                                                               | 4.94 ms: 1.06x slower                                                       |
| float                      | 92.1 ms                                                               | 98.7 ms: 1.07x slower                                                       |
| comprehensions             | 25.4 us                                                               | 27.3 us: 1.07x slower                                                       |
| scimark_lu                 | 146 ms                                                                | 158 ms: 1.09x slower                                                        |
| regex_v8                   | 28.3 ms                                                               | 30.9 ms: 1.09x slower                                                       |
| xml_etree_process          | 79.0 ms                                                               | 86.3 ms: 1.09x slower                                                       |
| mako                       | 12.9 ms                                                               | 14.2 ms: 1.10x slower                                                       |
| scimark_sor                | 150 ms                                                                | 166 ms: 1.11x slower                                                        |
| tornado_http               | 136 ms                                                                | 152 ms: 1.12x slower                                                        |
| html5lib                   | 65.1 ms                                                               | 73.0 ms: 1.12x slower                                                       |
| pickle_pure_python         | 365 us                                                                | 411 us: 1.13x slower                                                        |
| tomli_loads                | 2.59 sec                                                              | 2.93 sec: 1.13x slower                                                      |
| coverage                   | 87.3 ms                                                               | 98.8 ms: 1.13x slower                                                       |
| crypto_pyaes               | 86.6 ms                                                               | 99.1 ms: 1.14x slower                                                       |
| scimark_fft                | 418 ms                                                                | 481 ms: 1.15x slower                                                        |
| sqlalchemy_imperative      | 16.7 ms                                                               | 19.2 ms: 1.15x slower                                                       |
| json_dumps                 | 12.3 ms                                                               | 14.2 ms: 1.16x slower                                                       |
| deltablue                  | 4.12 ms                                                               | 4.83 ms: 1.17x slower                                                       |
| telco                      | 8.51 ms                                                               | 10.0 ms: 1.18x slower                                                       |
| meteor_contest             | 112 ms                                                                | 133 ms: 1.19x slower                                                        |
| scimark_monte_carlo        | 85.1 ms                                                               | 101 ms: 1.19x slower                                                        |
| logging_silent             | 127 ns                                                                | 153 ns: 1.21x slower                                                        |
| typing_runtime_protocols   | 181 us                                                                | 221 us: 1.23x slower                                                        |
| sqlalchemy_declarative     | 157 ms                                                                | 193 ms: 1.23x slower                                                        |
| fannkuch                   | 443 ms                                                                | 547 ms: 1.23x slower                                                        |
| pylint                     | 355 ms                                                                | 438 ms: 1.24x slower                                                        |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 7.70 ms: 1.24x slower                                                       |
| sqlglot_parse              | 1.46 ms                                                               | 1.82 ms: 1.25x slower                                                       |
| docutils                   | 2.98 sec                                                              | 3.74 sec: 1.25x slower                                                      |
| pycparser                  | 1.26 sec                                                              | 1.58 sec: 1.26x slower                                                      |
| nbody                      | 105 ms                                                                | 132 ms: 1.26x slower                                                        |
| generators                 | 43.5 ms                                                               | 55.2 ms: 1.27x slower                                                       |
| sqlglot_transpile          | 1.83 ms                                                               | 2.33 ms: 1.28x slower                                                       |
| spectral_norm              | 131 ms                                                                | 167 ms: 1.28x slower                                                        |
| python_startup             | 11.4 ms                                                               | 14.6 ms: 1.28x slower                                                       |
| genshi_text                | 27.4 ms                                                               | 35.2 ms: 1.28x slower                                                       |
| go                         | 157 ms                                                                | 203 ms: 1.29x slower                                                        |
| pyflate                    | 559 ms                                                                | 725 ms: 1.30x slower                                                        |
| sqlglot_normalize          | 126 ms                                                                | 163 ms: 1.30x slower                                                        |
| 2to3                       | 308 ms                                                                | 401 ms: 1.30x slower                                                        |
| dulwich_log                | 62.0 ms                                                               | 81.7 ms: 1.32x slower                                                       |
| sympy_str                  | 280 ms                                                                | 370 ms: 1.32x slower                                                        |
| sympy_expand               | 454 ms                                                                | 603 ms: 1.33x slower                                                        |
| regex_compile              | 137 ms                                                                | 183 ms: 1.34x slower                                                        |
| chaos                      | 71.4 ms                                                               | 95.6 ms: 1.34x slower                                                       |
| django_template            | 40.7 ms                                                               | 55.3 ms: 1.36x slower                                                       |
| richards_super             | 58.5 ms                                                               | 80.8 ms: 1.38x slower                                                       |
| nqueens                    | 99.2 ms                                                               | 139 ms: 1.40x slower                                                        |
| sympy_integrate            | 21.6 ms                                                               | 30.3 ms: 1.40x slower                                                       |
| gc_traversal               | 4.40 ms                                                               | 6.16 ms: 1.40x slower                                                       |
| sqlglot_optimize           | 61.3 ms                                                               | 86.1 ms: 1.40x slower                                                       |
| genshi_xml                 | 60.6 ms                                                               | 86.4 ms: 1.43x slower                                                       |
| sympy_sum                  | 154 ms                                                                | 222 ms: 1.44x slower                                                        |
| pprint_safe_repr           | 916 ms                                                                | 1.37 sec: 1.50x slower                                                      |
| pprint_pformat             | 1.88 sec                                                              | 2.85 sec: 1.52x slower                                                      |
| richards                   | 50.9 ms                                                               | 79.8 ms: 1.57x slower                                                       |
| hexiom                     | 6.98 ms                                                               | 11.5 ms: 1.65x slower                                                       |
| create_gc_cycles           | 1.92 ms                                                               | 3.67 ms: 1.91x slower                                                       |
| bench_mp_pool              | 7.05 ms                                                               | 2.46 sec: 348.67x slower                                                    |
| Geometric mean             | (ref)                                                                 | 1.22x slower                                                                |

Benchmark hidden because not significant (2): logging_simple, logging_format
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (2) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-arminc-aarch64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.123x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.12x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.11x