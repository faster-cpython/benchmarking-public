# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 217 ms: 1.15x faster                                                              |
| docutils       | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                            |
| html5lib       | 47.5 ms                                                         | 37.2 ms: 1.28x faster                                                             |
| sphinx         | 719 ms                                                          | 624 ms: 1.15x faster                                                              |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 198 ms: 1.50x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                              |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.37x faster                                                              |
| async_tree_io              | 526 ms                                                          | 387 ms: 1.36x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 164 ms: 1.31x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 380 ms: 1.30x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                             |
| async_generators           | 270 ms                                                          | 239 ms: 1.13x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.41x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 54.2 ms: 1.48x faster                                                             |
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                              |
| float          | 54.6 ms                                                         | 41.0 ms: 1.33x faster                                                             |
| Geometric mean | (ref)                                                           | 1.39x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 76.8 ms: 1.32x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                             |
| regex_v8       | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                             |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                            |
| json_loads           | 21.6 us                                                         | 14.0 us: 1.54x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 106 us: 1.51x faster                                                              |
| json_dumps           | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 49.5 ms: 1.24x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 88.0 ms: 1.22x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 196 us: 1.18x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.1 ms: 1.01x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.31x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 18.8 ms: 1.05x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                             |
| mako            | 7.09 ms                                                         | 5.28 ms: 1.34x faster                                                             |
| django_template | 29.8 ms                                                         | 23.7 ms: 1.26x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 498 us: 20.05x faster                                                             |
| coverage                   | 324 ms                                                          | 50.3 ms: 6.44x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 29.1 ms: 2.85x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                              |
| mdp                        | 1.62 sec                                                        | 785 ms: 2.07x faster                                                              |
| deepcopy                   | 314 us                                                          | 166 us: 1.89x faster                                                              |
| telco                      | 6.96 ms                                                         | 3.86 ms: 1.80x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.83 us: 1.60x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.09 sec: 1.57x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 856 ms: 1.55x faster                                                              |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.54x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 423 ms: 1.53x faster                                                              |
| unpickle_pure_python       | 160 us                                                          | 106 us: 1.51x faster                                                              |
| json                       | 4.27 ms                                                         | 2.83 ms: 1.51x faster                                                             |
| scimark_fft                | 205 ms                                                          | 136 ms: 1.50x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 198 ms: 1.50x faster                                                              |
| deepcopy_memo              | 25.4 us                                                         | 17.1 us: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                              |
| nbody                      | 80.0 ms                                                         | 54.2 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                              |
| go                         | 109 ms                                                          | 75.8 ms: 1.43x faster                                                             |
| fannkuch                   | 299 ms                                                          | 208 ms: 1.43x faster                                                              |
| genshi_xml                 | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.47 sec: 1.40x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.37x faster                                                              |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                              |
| json_dumps                 | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                             |
| async_tree_io              | 526 ms                                                          | 387 ms: 1.36x faster                                                              |
| logging_format             | 8.72 us                                                         | 6.44 us: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                              |
| mako                       | 7.09 ms                                                         | 5.28 ms: 1.34x faster                                                             |
| float                      | 54.6 ms                                                         | 41.0 ms: 1.33x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.00 us: 1.33x faster                                                             |
| regex_compile              | 101 ms                                                          | 76.8 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 164 ms: 1.31x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 380 ms: 1.30x faster                                                              |
| sympy_expand               | 373 ms                                                          | 288 ms: 1.30x faster                                                              |
| pyflate                    | 320 ms                                                          | 247 ms: 1.30x faster                                                              |
| pycparser                  | 872 ms                                                          | 680 ms: 1.28x faster                                                              |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.22 ms: 1.28x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.2 ms: 1.28x faster                                                             |
| sympy_str                  | 212 ms                                                          | 166 ms: 1.27x faster                                                              |
| crypto_pyaes               | 56.9 ms                                                         | 44.9 ms: 1.27x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 38.7 ms: 1.26x faster                                                             |
| django_template            | 29.8 ms                                                         | 23.7 ms: 1.26x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 84.7 ms: 1.25x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 49.5 ms: 1.24x faster                                                             |
| chaos                      | 50.2 ms                                                         | 40.9 ms: 1.23x faster                                                             |
| richards                   | 32.7 ms                                                         | 26.7 ms: 1.22x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 59.0 ms: 1.22x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 88.0 ms: 1.22x faster                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 831 us: 1.21x faster                                                              |
| sympy_integrate            | 15.0 ms                                                         | 12.5 ms: 1.20x faster                                                             |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                             |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.19x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 196 us: 1.18x faster                                                              |
| pylint                     | 227 ms                                                          | 193 ms: 1.17x faster                                                              |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.9 ms: 1.17x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                             |
| raytrace                   | 201 ms                                                          | 174 ms: 1.16x faster                                                              |
| 2to3                       | 250 ms                                                          | 217 ms: 1.15x faster                                                              |
| sphinx                     | 719 ms                                                          | 624 ms: 1.15x faster                                                              |
| generators                 | 21.8 ms                                                         | 19.1 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                             |
| async_generators           | 270 ms                                                          | 239 ms: 1.13x faster                                                              |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 77.8 ms: 1.10x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.03 ms: 1.10x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 64.3 ms: 1.08x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 70.6 ms: 1.06x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 18.8 ms: 1.05x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 89.0 ms: 1.02x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.1 ms: 1.01x slower                                                             |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                              |
| k_core                     | 1.38 sec                                                        | 1.60 sec: 1.16x slower                                                            |
| connected_components       | 267 ms                                                          | 315 ms: 1.18x slower                                                              |
| gc_traversal               | 1.75 ms                                                         | 2.08 ms: 1.19x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.26 ms: 1.19x slower                                                             |
| shortest_path              | 290 ms                                                          | 348 ms: 1.20x slower                                                              |
| many_optionals             | 436 us                                                          | 575 us: 1.32x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 31.6 ms: 2.14x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                      |

Benchmark hidden because not significant (1): scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-JIT/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown