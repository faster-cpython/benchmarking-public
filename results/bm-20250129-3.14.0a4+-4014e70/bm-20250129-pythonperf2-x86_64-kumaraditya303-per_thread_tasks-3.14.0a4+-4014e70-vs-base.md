# Results vs. base

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: 4014e70
- commit date: 2025-01-29
- overall geometric mean: 1.001x slower
- HPT reliability: 57.26%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 282 ms                                                                       | 282 ms: 1.00x faster                                                             |
| docutils       | 2.89 sec                                                                     | 2.88 sec: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_generators           | 421 ms                                                                       | 413 ms: 1.02x faster                                                             |
| async_tree_none_tg         | 279 ms                                                                       | 277 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 504 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 518 ms                                                                       | 516 ms: 1.01x faster                                                             |
| async_tree_memoization_tg  | 336 ms                                                                       | 335 ms: 1.00x faster                                                             |
| coroutines                 | 20.7 ms                                                                      | 20.8 ms: 1.00x slower                                                            |
| asyncio_websockets         | 384 ms                                                                       | 388 ms: 1.01x slower                                                             |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (4): async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                       | 134 ms: 1.01x faster                                                             |
| regex_v8       | 25.2 ms                                                                      | 25.5 ms: 1.01x slower                                                            |
| regex_effbot   | 3.06 ms                                                                      | 3.17 ms: 1.04x slower                                                            |
| regex_dna      | 237 ms                                                                       | 249 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pickle_pure_python   | 328 us                                                                       | 322 us: 1.02x faster                                                             |
| xml_etree_process    | 59.5 ms                                                                      | 58.4 ms: 1.02x faster                                                            |
| xml_etree_generate   | 83.9 ms                                                                      | 82.9 ms: 1.01x faster                                                            |
| unpickle_pure_python | 209 us                                                                       | 207 us: 1.01x faster                                                             |
| tomli_loads          | 2.03 sec                                                                     | 2.05 sec: 1.01x slower                                                           |
| json_loads           | 37.5 us                                                                      | 37.8 us: 1.01x slower                                                            |
| xml_etree_iterparse  | 103 ms                                                                       | 106 ms: 1.02x slower                                                             |
| Geometric mean       | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|-----------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 23.6 ms                                                                      | 23.0 ms: 1.03x faster                                                            |
| django_template | 36.0 ms                                                                      | 36.8 ms: 1.02x slower                                                            |
| Geometric mean  | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20250125-pythonperf2-x86_64-python-e119526edface001ad7d-3.14.0a4+-e119526 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------------|:----------------------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pyflate                    | 452 ms                                                                       | 429 ms: 1.05x faster                                                             |
| telco                      | 8.12 ms                                                                      | 7.75 ms: 1.05x faster                                                            |
| genshi_text                | 23.6 ms                                                                      | 23.0 ms: 1.03x faster                                                            |
| thrift                     | 869 us                                                                       | 846 us: 1.03x faster                                                             |
| meteor_contest             | 127 ms                                                                       | 124 ms: 1.03x faster                                                             |
| async_generators           | 421 ms                                                                       | 413 ms: 1.02x faster                                                             |
| deepcopy_reduce            | 2.97 us                                                                      | 2.91 us: 1.02x faster                                                            |
| pickle_pure_python         | 328 us                                                                       | 322 us: 1.02x faster                                                             |
| xml_etree_process          | 59.5 ms                                                                      | 58.4 ms: 1.02x faster                                                            |
| comprehensions             | 17.8 us                                                                      | 17.5 us: 1.01x faster                                                            |
| chaos                      | 59.6 ms                                                                      | 58.7 ms: 1.01x faster                                                            |
| scimark_sor                | 114 ms                                                                       | 112 ms: 1.01x faster                                                             |
| scimark_fft                | 307 ms                                                                       | 303 ms: 1.01x faster                                                             |
| mdp                        | 2.48 sec                                                                     | 2.45 sec: 1.01x faster                                                           |
| nqueens                    | 89.0 ms                                                                      | 87.9 ms: 1.01x faster                                                            |
| subparsers                 | 22.8 ms                                                                      | 22.5 ms: 1.01x faster                                                            |
| xml_etree_generate         | 83.9 ms                                                                      | 82.9 ms: 1.01x faster                                                            |
| unpickle_pure_python       | 209 us                                                                       | 207 us: 1.01x faster                                                             |
| generators                 | 28.8 ms                                                                      | 28.6 ms: 1.01x faster                                                            |
| pprint_pformat             | 1.61 sec                                                                     | 1.59 sec: 1.01x faster                                                           |
| deepcopy                   | 283 us                                                                       | 280 us: 1.01x faster                                                             |
| pathlib                    | 15.7 ms                                                                      | 15.5 ms: 1.01x faster                                                            |
| async_tree_none_tg         | 279 ms                                                                       | 277 ms: 1.01x faster                                                             |
| sqlalchemy_imperative      | 17.6 ms                                                                      | 17.5 ms: 1.01x faster                                                            |
| sqlalchemy_declarative     | 143 ms                                                                       | 142 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed_tg | 507 ms                                                                       | 504 ms: 1.01x faster                                                             |
| async_tree_cpu_io_mixed    | 518 ms                                                                       | 516 ms: 1.01x faster                                                             |
| fannkuch                   | 370 ms                                                                       | 368 ms: 1.01x faster                                                             |
| regex_compile              | 135 ms                                                                       | 134 ms: 1.01x faster                                                             |
| docutils                   | 2.89 sec                                                                     | 2.88 sec: 1.00x faster                                                           |
| async_tree_memoization_tg  | 336 ms                                                                       | 335 ms: 1.00x faster                                                             |
| pprint_safe_repr           | 789 ms                                                                       | 786 ms: 1.00x faster                                                             |
| bpe_tokeniser              | 4.66 sec                                                                     | 4.64 sec: 1.00x faster                                                           |
| python_startup             | 16.0 ms                                                                      | 16.0 ms: 1.00x faster                                                            |
| 2to3                       | 282 ms                                                                       | 282 ms: 1.00x faster                                                             |
| coroutines                 | 20.7 ms                                                                      | 20.8 ms: 1.00x slower                                                            |
| connected_components       | 416 ms                                                                       | 417 ms: 1.00x slower                                                             |
| scimark_monte_carlo        | 64.7 ms                                                                      | 64.9 ms: 1.00x slower                                                            |
| sympy_integrate            | 23.1 ms                                                                      | 23.2 ms: 1.00x slower                                                            |
| sqlglot_normalize          | 114 ms                                                                       | 115 ms: 1.00x slower                                                             |
| sympy_str                  | 288 ms                                                                       | 290 ms: 1.00x slower                                                             |
| sqlglot_optimize           | 57.4 ms                                                                      | 57.7 ms: 1.00x slower                                                            |
| hexiom                     | 6.02 ms                                                                      | 6.06 ms: 1.01x slower                                                            |
| deepcopy_memo              | 29.4 us                                                                      | 29.5 us: 1.01x slower                                                            |
| logging_simple             | 6.05 us                                                                      | 6.09 us: 1.01x slower                                                            |
| tomli_loads                | 2.03 sec                                                                     | 2.05 sec: 1.01x slower                                                           |
| sympy_expand               | 491 ms                                                                       | 495 ms: 1.01x slower                                                             |
| asyncio_websockets         | 384 ms                                                                       | 388 ms: 1.01x slower                                                             |
| typing_runtime_protocols   | 171 us                                                                       | 172 us: 1.01x slower                                                             |
| sqlglot_transpile          | 1.71 ms                                                                      | 1.72 ms: 1.01x slower                                                            |
| json                       | 6.82 ms                                                                      | 6.88 ms: 1.01x slower                                                            |
| json_loads                 | 37.5 us                                                                      | 37.8 us: 1.01x slower                                                            |
| regex_v8                   | 25.2 ms                                                                      | 25.5 ms: 1.01x slower                                                            |
| spectral_norm              | 83.1 ms                                                                      | 84.0 ms: 1.01x slower                                                            |
| raytrace                   | 270 ms                                                                       | 273 ms: 1.01x slower                                                             |
| dulwich_log                | 65.9 ms                                                                      | 66.8 ms: 1.01x slower                                                            |
| logging_format             | 6.68 us                                                                      | 6.77 us: 1.01x slower                                                            |
| sqlglot_parse              | 1.32 ms                                                                      | 1.33 ms: 1.01x slower                                                            |
| richards_super             | 52.4 ms                                                                      | 53.1 ms: 1.01x slower                                                            |
| shortest_path              | 440 ms                                                                       | 447 ms: 1.02x slower                                                             |
| coverage                   | 76.5 ms                                                                      | 77.8 ms: 1.02x slower                                                            |
| go                         | 126 ms                                                                       | 129 ms: 1.02x slower                                                             |
| xml_etree_iterparse        | 103 ms                                                                       | 106 ms: 1.02x slower                                                             |
| django_template            | 36.0 ms                                                                      | 36.8 ms: 1.02x slower                                                            |
| deltablue                  | 3.27 ms                                                                      | 3.37 ms: 1.03x slower                                                            |
| richards                   | 46.3 ms                                                                      | 47.9 ms: 1.03x slower                                                            |
| create_gc_cycles           | 2.72 ms                                                                      | 2.81 ms: 1.03x slower                                                            |
| regex_effbot               | 3.06 ms                                                                      | 3.17 ms: 1.04x slower                                                            |
| gc_traversal               | 6.34 ms                                                                      | 6.58 ms: 1.04x slower                                                            |
| pycparser                  | 1.21 sec                                                                     | 1.26 sec: 1.04x slower                                                           |
| scimark_sparse_mat_mult    | 4.56 ms                                                                      | 4.80 ms: 1.05x slower                                                            |
| regex_dna                  | 237 ms                                                                       | 249 ms: 1.05x slower                                                             |
| Geometric mean             | (ref)                                                                        | 1.00x faster                                                                     |

Benchmark hidden because not significant (24): bench_mp_pool, nbody, bench_thread_pool, k_core, scimark_lu, sqlite_synth, logging_silent, crypto_pyaes, async_tree_none, many_optionals, async_tree_memoization, sympy_sum, json_dumps, genshi_xml, mako, python_startup_no_site, float, pidigits, sphinx, pylint, async_tree_io_tg, html5lib, async_tree_io, xml_etree_parse

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 57.26% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x