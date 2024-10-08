# Results vs. base

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.00x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 289 ms                                                                      | 286 ms: 1.01x faster                                                         |
| docutils       | 2.97 sec                                                                    | 2.95 sec: 1.01x faster                                                       |
| html5lib       | 73.4 ms                                                                     | 73.8 ms: 1.01x slower                                                        |
| tornado_http   | 119 ms                                                                      | 118 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 382 ms                                                                      | 380 ms: 1.01x faster                                                         |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                 |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 90.9 ms                                                                     | 86.7 ms: 1.05x faster                                                        |
| pidigits       | 253 ms                                                                      | 254 ms: 1.01x slower                                                         |
| float          | 79.9 ms                                                                     | 81.8 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.3 ms                                                                     | 25.1 ms: 1.05x faster                                                        |
| regex_dna      | 241 ms                                                                      | 240 ms: 1.00x faster                                                         |
| regex_compile  | 140 ms                                                                      | 140 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                                      | 212 us: 1.05x faster                                                         |
| json_dumps           | 11.0 ms                                                                     | 10.7 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 105 ms                                                                      | 102 ms: 1.03x faster                                                         |
| xml_etree_parse      | 143 ms                                                                      | 140 ms: 1.02x faster                                                         |
| xml_etree_generate   | 84.5 ms                                                                     | 83.0 ms: 1.02x faster                                                        |
| xml_etree_process    | 59.8 ms                                                                     | 58.9 ms: 1.02x faster                                                        |
| tomli_loads          | 2.43 sec                                                                    | 2.45 sec: 1.01x slower                                                       |
| pickle_pure_python   | 313 us                                                                      | 320 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                                       | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.5 ms                                                                     | 13.3 ms: 1.01x faster                                                        |
| python_startup_no_site | 9.11 ms                                                                     | 9.01 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 56.0 ms                                                                     | 54.6 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------------|:---------------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python      | 224 us                                                                      | 212 us: 1.05x faster                                                         |
| nbody                     | 90.9 ms                                                                     | 86.7 ms: 1.05x faster                                                        |
| regex_v8                  | 26.3 ms                                                                     | 25.1 ms: 1.05x faster                                                        |
| telco                     | 8.27 ms                                                                     | 7.94 ms: 1.04x faster                                                        |
| json_dumps                | 11.0 ms                                                                     | 10.7 ms: 1.03x faster                                                        |
| xml_etree_iterparse       | 105 ms                                                                      | 102 ms: 1.03x faster                                                         |
| scimark_sor               | 110 ms                                                                      | 107 ms: 1.03x faster                                                         |
| genshi_xml                | 56.0 ms                                                                     | 54.6 ms: 1.03x faster                                                        |
| thrift                    | 900 us                                                                      | 878 us: 1.03x faster                                                         |
| scimark_fft               | 303 ms                                                                      | 296 ms: 1.02x faster                                                         |
| xml_etree_parse           | 143 ms                                                                      | 140 ms: 1.02x faster                                                         |
| sympy_sum                 | 156 ms                                                                      | 153 ms: 1.02x faster                                                         |
| dulwich_log               | 68.2 ms                                                                     | 66.7 ms: 1.02x faster                                                        |
| raytrace                  | 272 ms                                                                      | 267 ms: 1.02x faster                                                         |
| xml_etree_generate        | 84.5 ms                                                                     | 83.0 ms: 1.02x faster                                                        |
| logging_format            | 6.96 us                                                                     | 6.84 us: 1.02x faster                                                        |
| xml_etree_process         | 59.8 ms                                                                     | 58.9 ms: 1.02x faster                                                        |
| pprint_safe_repr          | 817 ms                                                                      | 805 ms: 1.01x faster                                                         |
| fannkuch                  | 365 ms                                                                      | 360 ms: 1.01x faster                                                         |
| pprint_pformat            | 1.67 sec                                                                    | 1.64 sec: 1.01x faster                                                       |
| python_startup            | 13.5 ms                                                                     | 13.3 ms: 1.01x faster                                                        |
| bpe_tokeniser             | 4.93 sec                                                                    | 4.87 sec: 1.01x faster                                                       |
| python_startup_no_site    | 9.11 ms                                                                     | 9.01 ms: 1.01x faster                                                        |
| chaos                     | 61.4 ms                                                                     | 60.8 ms: 1.01x faster                                                        |
| generators                | 33.9 ms                                                                     | 33.5 ms: 1.01x faster                                                        |
| sympy_expand              | 505 ms                                                                      | 500 ms: 1.01x faster                                                         |
| tornado_http              | 119 ms                                                                      | 118 ms: 1.01x faster                                                         |
| 2to3                      | 289 ms                                                                      | 286 ms: 1.01x faster                                                         |
| pycparser                 | 1.25 sec                                                                    | 1.24 sec: 1.01x faster                                                       |
| deepcopy_reduce           | 2.89 us                                                                     | 2.87 us: 1.01x faster                                                        |
| scimark_lu                | 96.1 ms                                                                     | 95.4 ms: 1.01x faster                                                        |
| asyncio_websockets        | 390 ms                                                                      | 388 ms: 1.01x faster                                                         |
| sqlglot_normalize         | 119 ms                                                                      | 118 ms: 1.01x faster                                                         |
| docutils                  | 2.97 sec                                                                    | 2.95 sec: 1.01x faster                                                       |
| async_generators          | 362 ms                                                                      | 360 ms: 1.01x faster                                                         |
| sympy_integrate           | 23.2 ms                                                                     | 23.1 ms: 1.01x faster                                                        |
| async_tree_memoization_tg | 382 ms                                                                      | 380 ms: 1.01x faster                                                         |
| sympy_str                 | 294 ms                                                                      | 292 ms: 1.00x faster                                                         |
| deepcopy                  | 283 us                                                                      | 282 us: 1.00x faster                                                         |
| regex_dna                 | 241 ms                                                                      | 240 ms: 1.00x faster                                                         |
| regex_compile             | 140 ms                                                                      | 140 ms: 1.00x faster                                                         |
| mdp                       | 2.50 sec                                                                    | 2.51 sec: 1.00x slower                                                       |
| asyncio_tcp               | 373 ms                                                                      | 374 ms: 1.00x slower                                                         |
| pidigits                  | 253 ms                                                                      | 254 ms: 1.01x slower                                                         |
| html5lib                  | 73.4 ms                                                                     | 73.8 ms: 1.01x slower                                                        |
| meteor_contest            | 124 ms                                                                      | 125 ms: 1.01x slower                                                         |
| json                      | 5.38 ms                                                                     | 5.42 ms: 1.01x slower                                                        |
| hexiom                    | 6.21 ms                                                                     | 6.26 ms: 1.01x slower                                                        |
| tomli_loads               | 2.43 sec                                                                    | 2.45 sec: 1.01x slower                                                       |
| comprehensions            | 17.0 us                                                                     | 17.1 us: 1.01x slower                                                        |
| deltablue                 | 3.41 ms                                                                     | 3.46 ms: 1.01x slower                                                        |
| pyflate                   | 468 ms                                                                      | 476 ms: 1.02x slower                                                         |
| nqueens                   | 88.2 ms                                                                     | 89.8 ms: 1.02x slower                                                        |
| logging_silent            | 97.8 ns                                                                     | 99.6 ns: 1.02x slower                                                        |
| scimark_sparse_mat_mult   | 4.04 ms                                                                     | 4.11 ms: 1.02x slower                                                        |
| pickle_pure_python        | 313 us                                                                      | 320 us: 1.02x slower                                                         |
| scimark_monte_carlo       | 65.0 ms                                                                     | 66.6 ms: 1.02x slower                                                        |
| float                     | 79.9 ms                                                                     | 81.8 ms: 1.02x slower                                                        |
| richards_super            | 57.9 ms                                                                     | 59.6 ms: 1.03x slower                                                        |
| coverage                  | 80.6 ms                                                                     | 83.2 ms: 1.03x slower                                                        |
| coroutines                | 21.1 ms                                                                     | 21.9 ms: 1.04x slower                                                        |
| go                        | 156 ms                                                                      | 164 ms: 1.05x slower                                                         |
| Geometric mean            | (ref)                                                                       | 1.00x faster                                                                 |

Benchmark hidden because not significant (28): bench_thread_pool, async_tree_cpu_io_mixed_tg, pylint, async_tree_none, async_tree_none_tg, typing_runtime_protocols, async_tree_cpu_io_mixed, create_gc_cycles, spectral_norm, asyncio_tcp_ssl, gc_traversal, sqlglot_optimize, deepcopy_memo, genshi_text, sqlglot_transpile, async_tree_io, django_template, async_tree_memoization, logging_simple, json_loads, pathlib, crypto_pyaes, regex_effbot, sqlglot_parse, mako, async_tree_io_tg, richards, bench_mp_pool

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x