# Results vs. 3.13.0

- fork: python
- ref: 3663b2ad54c9e15775a6
- machine: windows-amd64
- commit hash: 3663b2a
- commit date: 2025-08-16
- overall geometric mean: 1.137x faster
- HPT reliability: 99.64%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 223 ms: 1.12x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.75 sec: 1.55x slower                                                           |
| html5lib       | 47.5 ms                                                         | 40.9 ms: 1.16x faster                                                            |
| sphinx         | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.60x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 325 ms: 1.52x faster                                                             |
| async_tree_io              | 526 ms                                                          | 347 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 307 ms: 1.48x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 190 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.1 ms: 1.07x faster                                                            |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| float          | 54.6 ms                                                         | 46.1 ms: 1.18x faster                                                            |
| nbody          | 80.0 ms                                                         | 82.1 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| regex_compile  | 101 ms                                                          | 93.0 ms: 1.09x faster                                                            |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.1 us: 1.35x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.81 ms: 1.26x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 89.7 ms: 1.20x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 60.3 ms: 1.04x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 157 us: 1.02x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 44.4 ms: 1.00x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 62.4 ms: 1.02x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 240 us: 1.04x slower                                                             |
| tomli_loads          | 1.71 sec                                                        | 2.53 sec: 1.47x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.5 ms: 1.24x faster                                                            |
| django_template | 29.8 ms                                                         | 26.7 ms: 1.11x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.6 ms: 1.10x faster                                                            |
| mako            | 7.09 ms                                                         | 9.93 ms: 1.40x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.02x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 562 us: 17.75x faster                                                            |
| coverage                   | 324 ms                                                          | 66.3 ms: 4.88x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.6 ms: 2.90x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 140 ms: 2.60x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.03 sec: 1.58x faster                                                           |
| deepcopy                   | 314 us                                                          | 206 us: 1.53x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 325 ms: 1.52x faster                                                             |
| async_tree_io              | 526 ms                                                          | 347 ms: 1.51x faster                                                             |
| pidigits                   | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 307 ms: 1.48x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 190 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 329 ms: 1.47x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.34 us: 1.46x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_none            | 245 ms                                                          | 169 ms: 1.45x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.22 ms: 1.44x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.88 ms: 1.43x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| json                       | 4.27 ms                                                         | 3.12 ms: 1.37x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.13 us: 1.37x faster                                                            |
| json_loads                 | 21.6 us                                                         | 16.1 us: 1.35x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.2 ms: 1.27x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.81 ms: 1.26x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 40.5 ms: 1.24x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.16 us: 1.22x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.0 us: 1.21x faster                                                            |
| pycparser                  | 872 ms                                                          | 720 ms: 1.21x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 89.7 ms: 1.20x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.68 us: 1.20x faster                                                            |
| go                         | 109 ms                                                          | 91.2 ms: 1.19x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.0 ms: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 46.1 ms: 1.18x faster                                                            |
| sympy_expand               | 373 ms                                                          | 316 ms: 1.18x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 77.7 ms: 1.17x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 40.9 ms: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 565 ms: 1.15x faster                                                             |
| sympy_str                  | 212 ms                                                          | 185 ms: 1.14x faster                                                             |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| 2to3                       | 250 ms                                                          | 223 ms: 1.12x faster                                                             |
| django_template            | 29.8 ms                                                         | 26.7 ms: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| chaos                      | 50.2 ms                                                         | 45.5 ms: 1.10x faster                                                            |
| sphinx                     | 719 ms                                                          | 653 ms: 1.10x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 95.9 ms: 1.10x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 19.6 ms: 1.10x faster                                                            |
| regex_compile              | 101 ms                                                          | 93.0 ms: 1.09x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 13.9 ms: 1.08x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.1 ms: 1.07x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 129 us: 1.07x faster                                                             |
| async_generators           | 270 ms                                                          | 255 ms: 1.06x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.0 us: 1.04x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 60.3 ms: 1.04x faster                                                            |
| pyflate                    | 320 ms                                                          | 311 ms: 1.03x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 157 us: 1.02x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 44.4 ms: 1.00x slower                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 61.3 ns: 1.02x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 62.4 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 306 ms: 1.02x slower                                                             |
| raytrace                   | 201 ms                                                          | 206 ms: 1.02x slower                                                             |
| hexiom                     | 4.44 ms                                                         | 4.56 ms: 1.03x slower                                                            |
| nbody                      | 80.0 ms                                                         | 82.1 ms: 1.03x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 74.3 ms: 1.03x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 88.7 ms: 1.03x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 240 us: 1.04x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 72.3 ms: 1.04x slower                                                            |
| scimark_fft                | 205 ms                                                          | 214 ms: 1.05x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 2.45 ms: 1.05x slower                                                            |
| richards                   | 32.7 ms                                                         | 34.3 ms: 1.05x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.6 ms: 1.06x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.04 ms: 1.07x slower                                                            |
| generators                 | 21.8 ms                                                         | 23.4 ms: 1.07x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.08 ms: 1.08x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 65.5 ms: 1.09x slower                                                            |
| richards_super             | 36.7 ms                                                         | 40.0 ms: 1.09x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.47 sec: 1.11x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 85.8 ms: 1.15x slower                                                            |
| many_optionals             | 436 us                                                          | 606 us: 1.39x slower                                                             |
| mako                       | 7.09 ms                                                         | 9.93 ms: 1.40x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.53 sec: 1.47x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.25 sec: 1.52x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.75 sec: 1.55x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.60 sec: 1.89x slower                                                           |
| connected_components       | 267 ms                                                          | 545 ms: 2.05x slower                                                             |
| shortest_path              | 290 ms                                                          | 608 ms: 2.10x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 33.8 ms: 2.29x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (1): crypto_pyaes
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250816-3.15.0a0-3663b2a-NOGIL/bm-20250816-pythonperf1_win32-amd64-python-3663b2ad54c9e15775a6-3.15.0a0-3663b2a.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.137x faster

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown