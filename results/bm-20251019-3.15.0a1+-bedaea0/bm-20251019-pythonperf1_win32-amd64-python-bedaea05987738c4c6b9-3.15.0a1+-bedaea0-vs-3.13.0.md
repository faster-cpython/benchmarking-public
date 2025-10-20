# Results vs. 3.13.0

- fork: python
- ref: bedaea05987738c4c6b9
- machine: windows-amd64
- commit hash: bedaea0
- commit date: 2025-10-19
- overall geometric mean: 1.258x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                              |
| docutils       | 1.78 sec                                                        | 1.63 sec: 1.09x faster                                                            |
| html5lib       | 47.5 ms                                                         | 39.0 ms: 1.22x faster                                                             |
| sphinx         | 719 ms                                                          | 637 ms: 1.13x faster                                                              |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 146 ms: 2.49x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                              |
| async_tree_none            | 245 ms                                                          | 177 ms: 1.38x faster                                                              |
| async_tree_io              | 526 ms                                                          | 382 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.37x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                              |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.40x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 148 ms: 1.36x faster                                                              |
| float          | 54.6 ms                                                         | 44.8 ms: 1.22x faster                                                             |
| nbody          | 80.0 ms                                                         | 67.9 ms: 1.18x faster                                                             |
| Geometric mean | (ref)                                                           | 1.25x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                             |
| regex_compile  | 101 ms                                                          | 81.0 ms: 1.25x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                             |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.5 us: 1.49x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.53 ms: 1.32x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 87.5 ms: 1.23x faster                                                             |
| tomli_loads          | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 138 us: 1.16x faster                                                              |
| xml_etree_process    | 44.2 ms                                                         | 39.3 ms: 1.13x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 57.1 ms: 1.08x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 218 us: 1.06x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.1 ms: 1.04x slower                                                             |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 15.9 ms: 1.36x faster                                                             |
| django_template | 29.8 ms                                                         | 25.2 ms: 1.18x faster                                                             |
| mako            | 7.09 ms                                                         | 6.61 ms: 1.07x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 501 us: 19.92x faster                                                             |
| coverage                   | 324 ms                                                          | 49.4 ms: 6.56x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 29.4 ms: 2.82x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 146 ms: 2.49x faster                                                              |
| mdp                        | 1.62 sec                                                        | 823 ms: 1.97x faster                                                              |
| deepcopy                   | 314 us                                                          | 168 us: 1.87x faster                                                              |
| telco                      | 6.96 ms                                                         | 4.26 ms: 1.63x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.81 us: 1.61x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.5 us: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                              |
| deepcopy_memo              | 25.4 us                                                         | 17.3 us: 1.47x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 203 ms: 1.46x faster                                                              |
| json                       | 4.27 ms                                                         | 2.98 ms: 1.44x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                             |
| async_tree_none            | 245 ms                                                          | 177 ms: 1.38x faster                                                              |
| go                         | 109 ms                                                          | 78.8 ms: 1.38x faster                                                             |
| async_tree_io              | 526 ms                                                          | 382 ms: 1.38x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 334 ms: 1.37x faster                                                              |
| pidigits                   | 201 ms                                                          | 148 ms: 1.36x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                              |
| genshi_text                | 21.5 ms                                                         | 15.9 ms: 1.36x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 103 us: 1.33x faster                                                              |
| logging_format             | 8.72 us                                                         | 6.57 us: 1.33x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.53 ms: 1.32x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 493 ms: 1.32x faster                                                              |
| logging_simple             | 7.99 us                                                         | 6.08 us: 1.31x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.01 sec: 1.31x faster                                                            |
| sympy_expand               | 373 ms                                                          | 289 ms: 1.29x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 383 ms: 1.29x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 166 ms: 1.29x faster                                                              |
| sympy_str                  | 212 ms                                                          | 169 ms: 1.25x faster                                                              |
| regex_v8                   | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                             |
| regex_compile              | 101 ms                                                          | 81.0 ms: 1.25x faster                                                             |
| pycparser                  | 872 ms                                                          | 702 ms: 1.24x faster                                                              |
| sqlite_synth               | 1.95 us                                                         | 1.59 us: 1.23x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 87.5 ms: 1.23x faster                                                             |
| float                      | 54.6 ms                                                         | 44.8 ms: 1.22x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 39.0 ms: 1.22x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 40.3 ms: 1.21x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.5 ms: 1.21x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                             |
| chaos                      | 50.2 ms                                                         | 41.7 ms: 1.20x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.5 ms: 1.20x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 48.0 ms: 1.19x faster                                                             |
| django_template            | 29.8 ms                                                         | 25.2 ms: 1.18x faster                                                             |
| nbody                      | 80.0 ms                                                         | 67.9 ms: 1.18x faster                                                             |
| scimark_fft                | 205 ms                                                          | 175 ms: 1.17x faster                                                              |
| richards                   | 32.7 ms                                                         | 28.1 ms: 1.16x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 138 us: 1.16x faster                                                              |
| bench_thread_pool          | 1.00 ms                                                         | 863 us: 1.16x faster                                                              |
| richards_super             | 36.7 ms                                                         | 31.7 ms: 1.16x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 3.00 sec: 1.16x faster                                                            |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                              |
| nqueens                    | 72.1 ms                                                         | 63.3 ms: 1.14x faster                                                             |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                              |
| pylint                     | 227 ms                                                          | 200 ms: 1.14x faster                                                              |
| scimark_monte_carlo        | 47.7 ms                                                         | 42.2 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 637 ms: 1.13x faster                                                              |
| xml_etree_process          | 44.2 ms                                                         | 39.3 ms: 1.13x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.2 us: 1.12x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.6 ms: 1.11x faster                                                             |
| fannkuch                   | 299 ms                                                          | 269 ms: 1.11x faster                                                              |
| pyflate                    | 320 ms                                                          | 289 ms: 1.11x faster                                                              |
| scimark_sor                | 85.9 ms                                                         | 78.0 ms: 1.10x faster                                                             |
| raytrace                   | 201 ms                                                          | 183 ms: 1.10x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.60 ms: 1.09x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.63 sec: 1.09x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.08x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 57.1 ms: 1.08x faster                                                             |
| mako                       | 7.09 ms                                                         | 6.61 ms: 1.07x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 218 us: 1.06x faster                                                              |
| hexiom                     | 4.44 ms                                                         | 4.23 ms: 1.05x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.22 ms: 1.05x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 57.7 ns: 1.04x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.03x faster                                                             |
| scimark_lu                 | 60.2 ms                                                         | 59.0 ms: 1.02x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 73.4 ms: 1.02x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 69.6 ms: 1.00x slower                                                             |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                              |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.1 ms: 1.04x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.11 ms: 1.21x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.28 ms: 1.21x slower                                                             |
| connected_components       | 267 ms                                                          | 330 ms: 1.24x slower                                                              |
| k_core                     | 1.38 sec                                                        | 1.71 sec: 1.24x slower                                                            |
| shortest_path              | 290 ms                                                          | 360 ms: 1.24x slower                                                              |
| many_optionals             | 436 us                                                          | 562 us: 1.29x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 31.5 ms: 2.13x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                      |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251019-3.15.0a1+-bedaea0/bm-20251019-pythonperf1_win32-amd64-python-bedaea05987738c4c6b9-3.15.0a1+-bedaea0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.258x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown