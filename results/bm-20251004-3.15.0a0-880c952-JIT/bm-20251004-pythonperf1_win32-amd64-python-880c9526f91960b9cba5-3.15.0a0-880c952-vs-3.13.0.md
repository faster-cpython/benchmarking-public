# Results vs. 3.13.0

- fork: python
- ref: 880c9526f91960b9cba5
- machine: windows-amd64
- commit hash: 880c952
- commit date: 2025-10-04
- overall geometric mean: 1.327x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 213 ms: 1.18x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.1 ms: 1.28x faster                                                            |
| sphinx         | 719 ms                                                          | 625 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 168 ms: 2.15x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.49x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 336 ms: 1.44x faster                                                             |
| async_tree_io              | 526 ms                                                          | 382 ms: 1.38x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 376 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 164 ms: 1.31x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 240 ms: 1.13x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.6 ms: 1.49x faster                                                            |
| pidigits       | 201 ms                                                          | 148 ms: 1.36x faster                                                             |
| float          | 54.6 ms                                                         | 43.0 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 76.4 ms: 1.32x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.08 sec: 1.59x faster                                                           |
| json_loads           | 21.6 us                                                         | 13.9 us: 1.56x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.53x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 34.5 ms: 1.28x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 48.8 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.6 ms: 1.24x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 201 us: 1.15x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 60.3 ms: 1.04x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| mako            | 7.09 ms                                                         | 5.33 ms: 1.33x faster                                                            |
| django_template | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 502 us: 19.88x faster                                                            |
| coverage                   | 324 ms                                                          | 48.3 ms: 6.71x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.4 ms: 2.82x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 168 ms: 2.15x faster                                                             |
| mdp                        | 1.62 sec                                                        | 784 ms: 2.07x faster                                                             |
| deepcopy                   | 314 us                                                          | 162 us: 1.93x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.90 ms: 1.78x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.76 us: 1.66x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 835 ms: 1.59x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 409 ms: 1.59x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.08 sec: 1.59x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 16.1 us: 1.57x faster                                                            |
| json_loads                 | 21.6 us                                                         | 13.9 us: 1.56x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.53x faster                                                             |
| scimark_fft                | 205 ms                                                          | 136 ms: 1.51x faster                                                             |
| nbody                      | 80.0 ms                                                         | 53.6 ms: 1.49x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.49x faster                                                             |
| json                       | 4.27 ms                                                         | 2.88 ms: 1.49x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| go                         | 109 ms                                                          | 75.2 ms: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 336 ms: 1.44x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.47 sec: 1.40x faster                                                           |
| genshi_text                | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| logging_simple             | 7.99 us                                                         | 5.73 us: 1.39x faster                                                            |
| logging_format             | 8.72 us                                                         | 6.29 us: 1.39x faster                                                            |
| fannkuch                   | 299 ms                                                          | 217 ms: 1.38x faster                                                             |
| async_tree_io              | 526 ms                                                          | 382 ms: 1.38x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| pidigits                   | 201 ms                                                          | 148 ms: 1.36x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.38 ms: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.34x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 341 ms: 1.34x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.33 ms: 1.33x faster                                                            |
| regex_compile              | 101 ms                                                          | 76.4 ms: 1.32x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 376 ms: 1.32x faster                                                             |
| sympy_expand               | 373 ms                                                          | 285 ms: 1.31x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 164 ms: 1.31x faster                                                             |
| pyflate                    | 320 ms                                                          | 246 ms: 1.30x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 44.1 ms: 1.29x faster                                                            |
| pycparser                  | 872 ms                                                          | 676 ms: 1.29x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 34.5 ms: 1.28x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 37.1 ms: 1.28x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 38.2 ms: 1.28x faster                                                            |
| sympy_str                  | 212 ms                                                          | 166 ms: 1.28x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.53 us: 1.28x faster                                                            |
| float                      | 54.6 ms                                                         | 43.0 ms: 1.27x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.23 ms: 1.27x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 48.8 ms: 1.26x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 83.9 ms: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.0 ms: 1.26x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.6 ms: 1.24x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 818 us: 1.22x faster                                                             |
| django_template            | 29.8 ms                                                         | 24.4 ms: 1.22x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.3 ms: 1.21x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.0 ms: 1.21x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 59.7 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.5 ms: 1.20x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.20x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.9 ms: 1.20x faster                                                            |
| 2to3                       | 250 ms                                                          | 213 ms: 1.18x faster                                                             |
| pylint                     | 227 ms                                                          | 193 ms: 1.17x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| raytrace                   | 201 ms                                                          | 174 ms: 1.16x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 201 us: 1.15x faster                                                             |
| sphinx                     | 719 ms                                                          | 625 ms: 1.15x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 240 ms: 1.13x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 77.5 ms: 1.11x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.03 ms: 1.10x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.0 ms: 1.07x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 60.3 ms: 1.04x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.3 ms: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.5 ms: 1.03x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 88.5 ms: 1.02x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.30 ms: 1.01x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.58 sec: 1.15x slower                                                           |
| connected_components       | 267 ms                                                          | 314 ms: 1.18x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.06 ms: 1.18x slower                                                            |
| shortest_path              | 290 ms                                                          | 347 ms: 1.20x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| many_optionals             | 436 us                                                          | 569 us: 1.30x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 30.6 ms: 2.07x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                     |

Benchmark hidden because not significant (1): regex_dna
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251004-3.15.0a0-880c952-JIT/bm-20251004-pythonperf1_win32-amd64-python-880c9526f91960b9cba5-3.15.0a0-880c952.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.327x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: unknown