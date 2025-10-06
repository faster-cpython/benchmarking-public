# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.152x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.79 sec: 1.57x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| sphinx         | 719 ms                                                          | 666 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 141 ms: 2.56x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 324 ms: 1.53x faster                                                             |
| async_tree_io              | 526 ms                                                          | 347 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 187 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.49x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 145 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 251 ms: 1.08x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 137 ms: 1.47x faster                                                             |
| float          | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| nbody          | 80.0 ms                                                         | 78.6 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.7 ms: 1.33x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| regex_compile  | 101 ms                                                          | 91.3 ms: 1.11x faster                                                            |
| regex_dna      | 114 ms                                                          | 111 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.9 us: 1.36x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.11 ms: 1.20x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 90.6 ms: 1.19x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 149 us: 1.08x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 224 us: 1.03x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 61.9 ms: 1.01x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 44.6 ms: 1.01x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.29 sec: 1.33x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 38.3 ms: 1.31x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 18.6 ms: 1.15x faster                                                            |
| django_template | 29.8 ms                                                         | 26.2 ms: 1.14x faster                                                            |
| mako            | 7.09 ms                                                         | 9.70 ms: 1.37x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.06x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 572 us: 17.44x faster                                                            |
| coverage                   | 324 ms                                                          | 67.7 ms: 4.78x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.9 ms: 2.87x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 141 ms: 2.56x faster                                                             |
| deepcopy                   | 314 us                                                          | 184 us: 1.70x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.05 sec: 1.55x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 324 ms: 1.53x faster                                                             |
| async_tree_io              | 526 ms                                                          | 347 ms: 1.51x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 187 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 305 ms: 1.49x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 145 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 137 ms: 1.47x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.20 ms: 1.46x faster                                                            |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.06 us: 1.42x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.91 ms: 1.42x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.38 us: 1.41x faster                                                            |
| json                       | 4.27 ms                                                         | 3.04 ms: 1.40x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.5 us: 1.37x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.9 us: 1.36x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.7 ms: 1.33x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 38.3 ms: 1.31x faster                                                            |
| pycparser                  | 872 ms                                                          | 694 ms: 1.26x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.43 us: 1.24x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.05 us: 1.24x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 74.3 ms: 1.22x faster                                                            |
| go                         | 109 ms                                                          | 89.4 ms: 1.22x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 542 ms: 1.20x faster                                                             |
| sympy_expand               | 373 ms                                                          | 312 ms: 1.20x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.11 ms: 1.20x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.6 ms: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 46.2 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.8 ms: 1.17x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.7 ms: 1.17x faster                                                            |
| sympy_str                  | 212 ms                                                          | 182 ms: 1.16x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 18.6 ms: 1.15x faster                                                            |
| django_template            | 29.8 ms                                                         | 26.2 ms: 1.14x faster                                                            |
| 2to3                       | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 93.7 ms: 1.13x faster                                                            |
| regex_compile              | 101 ms                                                          | 91.3 ms: 1.11x faster                                                            |
| pylint                     | 227 ms                                                          | 205 ms: 1.11x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 13.7 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.0 ms: 1.09x faster                                                            |
| scimark_fft                | 205 ms                                                          | 188 ms: 1.09x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.5 us: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 666 ms: 1.08x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 149 us: 1.08x faster                                                             |
| async_generators           | 270 ms                                                          | 251 ms: 1.08x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 128 us: 1.07x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                            |
| pyflate                    | 320 ms                                                          | 304 ms: 1.05x faster                                                             |
| generators                 | 21.8 ms                                                         | 20.9 ms: 1.04x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.02 ms: 1.04x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 224 us: 1.03x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 58.9 ns: 1.02x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 55.7 ms: 1.02x faster                                                            |
| regex_dna                  | 114 ms                                                          | 111 ms: 1.02x faster                                                             |
| richards                   | 32.7 ms                                                         | 32.1 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| nbody                      | 80.0 ms                                                         | 78.6 ms: 1.02x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 84.8 ms: 1.01x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.46 ms: 1.00x slower                                                            |
| fannkuch                   | 299 ms                                                          | 301 ms: 1.01x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 61.9 ms: 1.01x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 44.6 ms: 1.01x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 61.5 ms: 1.02x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.03 ms: 1.02x slower                                                            |
| richards_super             | 36.7 ms                                                         | 37.6 ms: 1.02x slower                                                            |
| raytrace                   | 201 ms                                                          | 207 ms: 1.03x slower                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.96 ms: 1.04x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.0 ms: 1.05x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 73.6 ms: 1.06x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 87.7 ms: 1.18x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.60 sec: 1.21x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.29 sec: 1.33x slower                                                           |
| mako                       | 7.09 ms                                                         | 9.70 ms: 1.37x slower                                                            |
| many_optionals             | 436 us                                                          | 616 us: 1.41x slower                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 5.41 sec: 1.56x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.79 sec: 1.57x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.67 sec: 1.94x slower                                                           |
| shortest_path              | 290 ms                                                          | 653 ms: 2.25x slower                                                             |
| connected_components       | 267 ms                                                          | 617 ms: 2.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 35.0 ms: 2.37x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                     |

Benchmark hidden because not significant (2): nqueens, deltablue
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952-NOGIL/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.152x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: unknown