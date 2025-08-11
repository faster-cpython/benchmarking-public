# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.292x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 224 ms: 1.12x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.6 ms: 1.23x faster                                                            |
| sphinx         | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 205 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 211 ms: 1.34x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 251 ms: 1.07x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 54.9 ms: 1.46x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| regex_dna      | 114 ms                                                          | 119 ms: 1.05x slower                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.45 ms: 1.34x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 35.7 ms: 1.24x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 88.0 ms: 1.22x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 51.2 ms: 1.20x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 204 us: 1.13x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 63.2 ms: 1.01x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.29x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.5 ms: 1.07x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| mako            | 7.09 ms                                                         | 5.28 ms: 1.34x faster                                                            |
| django_template | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 489 us: 20.40x faster                                                            |
| coverage                   | 324 ms                                                          | 51.1 ms: 6.34x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 32.2 ms: 2.58x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 807 ms: 2.01x faster                                                             |
| deepcopy                   | 314 us                                                          | 174 us: 1.81x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.24 ms: 1.64x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.58x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.10 sec: 1.56x faster                                                           |
| unpickle_pure_python       | 160 us                                                          | 105 us: 1.52x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 442 ms: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 907 ms: 1.46x faster                                                             |
| nbody                      | 80.0 ms                                                         | 54.9 ms: 1.46x faster                                                            |
| fannkuch                   | 299 ms                                                          | 206 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 205 ms: 1.45x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| go                         | 109 ms                                                          | 75.6 ms: 1.44x faster                                                            |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.3 us: 1.39x faster                                                            |
| scimark_fft                | 205 ms                                                          | 148 ms: 1.38x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| json                       | 4.27 ms                                                         | 3.10 ms: 1.38x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.55 sec: 1.36x faster                                                           |
| mako                       | 7.09 ms                                                         | 5.28 ms: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.45 ms: 1.34x faster                                                            |
| async_tree_io              | 526 ms                                                          | 393 ms: 1.34x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 211 ms: 1.34x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.52 us: 1.34x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.04 us: 1.32x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.31x faster                                                             |
| sympy_expand               | 373 ms                                                          | 290 ms: 1.29x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 385 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| regex_compile              | 101 ms                                                          | 78.9 ms: 1.28x faster                                                            |
| pycparser                  | 872 ms                                                          | 690 ms: 1.26x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.25 ms: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 169 ms: 1.25x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.7 ms: 1.24x faster                                                            |
| richards                   | 32.7 ms                                                         | 26.4 ms: 1.24x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.6 ms: 1.23x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.2 ms: 1.23x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 46.4 ms: 1.23x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.0 ms: 1.22x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 88.0 ms: 1.22x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.2 ms: 1.22x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.0 ms: 1.21x faster                                                            |
| pyflate                    | 320 ms                                                          | 265 ms: 1.21x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 51.2 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.9 ms: 1.19x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.0 ms: 1.19x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.5 us: 1.19x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.7 ms: 1.18x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 61.3 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 864 us: 1.16x faster                                                             |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 204 us: 1.13x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 75.8 ms: 1.13x faster                                                            |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| 2to3                       | 250 ms                                                          | 224 ms: 1.12x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.7 ms: 1.11x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.10 ms: 1.08x faster                                                            |
| async_generators           | 270 ms                                                          | 251 ms: 1.07x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.5 ms: 1.07x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 65.5 ms: 1.06x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.4 ms: 1.03x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.26 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.0 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 63.2 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.9 ns: 1.03x slower                                                            |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.05x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 96.2 ms: 1.06x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.62 sec: 1.18x slower                                                           |
| connected_components       | 267 ms                                                          | 323 ms: 1.21x slower                                                             |
| shortest_path              | 290 ms                                                          | 355 ms: 1.23x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.32 ms: 1.25x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.21 ms: 1.26x slower                                                            |
| many_optionals             | 436 us                                                          | 570 us: 1.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.8 ms: 2.02x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.292x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown