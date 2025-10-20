# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.161x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 217 ms: 1.16x faster                                                              |
| docutils       | 1.78 sec                                                        | 2.80 sec: 1.58x slower                                                            |
| html5lib       | 47.5 ms                                                         | 40.5 ms: 1.17x faster                                                             |
| sphinx         | 719 ms                                                          | 638 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.60x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 318 ms: 1.56x faster                                                              |
| async_tree_io              | 526 ms                                                          | 339 ms: 1.55x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 184 ms: 1.53x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 142 ms: 1.51x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 306 ms: 1.49x faster                                                              |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 335 ms: 1.45x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 13.6 ms: 1.19x faster                                                             |
| async_generators           | 270 ms                                                          | 256 ms: 1.05x faster                                                              |
| Geometric mean             | (ref)                                                           | 1.49x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.47x faster                                                              |
| float          | 54.6 ms                                                         | 45.1 ms: 1.21x faster                                                             |
| nbody          | 80.0 ms                                                         | 76.8 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                           | 1.23x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                             |
| regex_compile  | 101 ms                                                          | 90.1 ms: 1.12x faster                                                             |
| regex_dna      | 114 ms                                                          | 112 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.34x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 6.16 ms: 1.19x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 92.7 ms: 1.16x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 150 us: 1.07x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.7 ms: 1.07x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 222 us: 1.04x faster                                                              |
| xml_etree_process    | 44.2 ms                                                         | 43.3 ms: 1.02x faster                                                             |
| tomli_loads          | 1.71 sec                                                        | 2.24 sec: 1.31x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 37.7 ms: 1.33x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 18.3 ms: 1.18x faster                                                             |
| django_template | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                             |
| mako            | 7.09 ms                                                         | 9.74 ms: 1.38x slower                                                             |
| Geometric mean  | (ref)                                                           | 1.07x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 575 us: 17.35x faster                                                             |
| coverage                   | 324 ms                                                          | 67.2 ms: 4.82x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 28.7 ms: 2.89x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.60x faster                                                              |
| deepcopy                   | 314 us                                                          | 185 us: 1.70x faster                                                              |
| mdp                        | 1.62 sec                                                        | 1.02 sec: 1.59x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 318 ms: 1.56x faster                                                              |
| async_tree_io              | 526 ms                                                          | 339 ms: 1.55x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 184 ms: 1.53x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 142 ms: 1.51x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 306 ms: 1.49x faster                                                              |
| deepcopy_reduce            | 2.92 us                                                         | 1.97 us: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.47x faster                                                              |
| sqlite_synth               | 1.95 us                                                         | 1.34 us: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 335 ms: 1.45x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 206 ms: 1.44x faster                                                              |
| gc_traversal               | 1.75 ms                                                         | 1.25 ms: 1.40x faster                                                             |
| telco                      | 6.96 ms                                                         | 5.07 ms: 1.37x faster                                                             |
| json                       | 4.27 ms                                                         | 3.14 ms: 1.36x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 18.7 us: 1.36x faster                                                             |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.34x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 37.7 ms: 1.33x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 12.8 ms: 1.31x faster                                                             |
| pycparser                  | 872 ms                                                          | 691 ms: 1.26x faster                                                              |
| logging_simple             | 7.99 us                                                         | 6.44 us: 1.24x faster                                                             |
| go                         | 109 ms                                                          | 87.9 ms: 1.24x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 73.9 ms: 1.23x faster                                                             |
| sympy_expand               | 373 ms                                                          | 307 ms: 1.22x faster                                                              |
| float                      | 54.6 ms                                                         | 45.1 ms: 1.21x faster                                                             |
| logging_format             | 8.72 us                                                         | 7.21 us: 1.21x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 543 ms: 1.19x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 13.6 ms: 1.19x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.16 ms: 1.19x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 41.3 ms: 1.18x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.53 ms: 1.18x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 18.3 ms: 1.18x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 40.5 ms: 1.17x faster                                                             |
| sympy_str                  | 212 ms                                                          | 183 ms: 1.16x faster                                                              |
| xml_etree_parse            | 107 ms                                                          | 92.7 ms: 1.16x faster                                                             |
| 2to3                       | 250 ms                                                          | 217 ms: 1.16x faster                                                              |
| django_template            | 29.8 ms                                                         | 25.8 ms: 1.15x faster                                                             |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                              |
| chaos                      | 50.2 ms                                                         | 44.4 ms: 1.13x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 93.4 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 638 ms: 1.13x faster                                                              |
| regex_compile              | 101 ms                                                          | 90.1 ms: 1.12x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 13.6 ms: 1.10x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.4 us: 1.10x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 126 us: 1.10x faster                                                              |
| scimark_fft                | 205 ms                                                          | 188 ms: 1.09x faster                                                              |
| generators                 | 21.8 ms                                                         | 20.3 ms: 1.07x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 150 us: 1.07x faster                                                              |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.7 ms: 1.07x faster                                                             |
| async_generators           | 270 ms                                                          | 256 ms: 1.05x faster                                                              |
| pyflate                    | 320 ms                                                          | 304 ms: 1.05x faster                                                              |
| scimark_sor                | 85.9 ms                                                         | 82.0 ms: 1.05x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.01 ms: 1.04x faster                                                             |
| richards                   | 32.7 ms                                                         | 31.4 ms: 1.04x faster                                                             |
| nbody                      | 80.0 ms                                                         | 76.8 ms: 1.04x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 222 us: 1.04x faster                                                              |
| crypto_pyaes               | 56.9 ms                                                         | 55.1 ms: 1.03x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 43.3 ms: 1.02x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 70.9 ms: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.01x faster                                                              |
| spectral_norm              | 69.4 ms                                                         | 68.8 ms: 1.01x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.42 ms: 1.00x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 48.0 ms: 1.01x slower                                                             |
| raytrace                   | 201 ms                                                          | 204 ms: 1.01x slower                                                              |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.90 ms: 1.02x slower                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 63.2 ms: 1.05x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 85.2 ms: 1.14x slower                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.63 sec: 1.23x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.24 sec: 1.31x slower                                                            |
| mako                       | 7.09 ms                                                         | 9.74 ms: 1.38x slower                                                             |
| many_optionals             | 436 us                                                          | 620 us: 1.42x slower                                                              |
| bpe_tokeniser              | 3.46 sec                                                        | 5.39 sec: 1.56x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.80 sec: 1.58x slower                                                            |
| k_core                     | 1.38 sec                                                        | 2.67 sec: 1.94x slower                                                            |
| shortest_path              | 290 ms                                                          | 652 ms: 2.25x slower                                                              |
| connected_components       | 267 ms                                                          | 617 ms: 2.31x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 35.0 ms: 2.37x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                      |

Benchmark hidden because not significant (5): deltablue, richards_super, xml_etree_generate, fannkuch, logging_silent
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0-NOGIL/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.161x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: unknown