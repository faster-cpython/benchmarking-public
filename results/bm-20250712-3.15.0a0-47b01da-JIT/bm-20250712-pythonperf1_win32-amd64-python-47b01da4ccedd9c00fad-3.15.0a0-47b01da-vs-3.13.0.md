# Results vs. 3.13.0

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: windows-amd64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.311x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 641 ms: 1.12x faster                                                             |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                             |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_io              | 526 ms                                                          | 388 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 337 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 390 ms: 1.27x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 54.6 ms: 1.46x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.2 ms: 1.28x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.63 ms: 1.10x faster                                                            |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 107 us: 1.50x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.5 ms: 1.24x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 50.5 ms: 1.22x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.23 ms: 1.17x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 201 us: 1.15x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.3 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| mako            | 7.09 ms                                                         | 5.38 ms: 1.32x faster                                                            |
| django_template | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 490 us: 20.35x faster                                                            |
| coverage                   | 324 ms                                                          | 49.7 ms: 6.51x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.0 ms: 2.76x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                             |
| mdp                        | 1.62 sec                                                        | 800 ms: 2.03x faster                                                             |
| deepcopy                   | 314 us                                                          | 171 us: 1.83x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.80 us: 1.62x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.33 ms: 1.61x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.13 sec: 1.52x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 107 us: 1.50x faster                                                             |
| async_tree_none            | 245 ms                                                          | 165 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 200 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.2 ms: 1.47x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 330 ms: 1.47x faster                                                             |
| nbody                      | 80.0 ms                                                         | 54.6 ms: 1.46x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 912 ms: 1.46x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 447 ms: 1.45x faster                                                             |
| go                         | 109 ms                                                          | 76.4 ms: 1.42x faster                                                            |
| json                       | 4.27 ms                                                         | 3.02 ms: 1.42x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.1 us: 1.41x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| fannkuch                   | 299 ms                                                          | 213 ms: 1.40x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| scimark_fft                | 205 ms                                                          | 149 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_io              | 526 ms                                                          | 388 ms: 1.35x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 337 ms: 1.35x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.58 sec: 1.34x faster                                                           |
| logging_format             | 8.72 us                                                         | 6.54 us: 1.33x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.38 ms: 1.32x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.09 us: 1.31x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 167 ms: 1.28x faster                                                             |
| regex_compile              | 101 ms                                                          | 79.2 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 390 ms: 1.27x faster                                                             |
| sympy_expand               | 373 ms                                                          | 295 ms: 1.27x faster                                                             |
| pyflate                    | 320 ms                                                          | 253 ms: 1.27x faster                                                             |
| float                      | 54.6 ms                                                         | 43.4 ms: 1.26x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.55 us: 1.26x faster                                                            |
| chaos                      | 50.2 ms                                                         | 40.0 ms: 1.26x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 45.4 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 696 ms: 1.25x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 35.3 ms: 1.25x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 57.7 ms: 1.25x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.1 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.28 ms: 1.25x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 86.5 ms: 1.24x faster                                                            |
| sympy_str                  | 212 ms                                                          | 173 ms: 1.22x faster                                                             |
| richards                   | 32.7 ms                                                         | 26.9 ms: 1.22x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 50.5 ms: 1.22x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.2 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.3 ms: 1.21x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.4 ms: 1.21x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.0 ms: 1.20x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 39.9 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 845 us: 1.19x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.7 ms: 1.18x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.6 us: 1.18x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.23 ms: 1.17x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 74.5 ms: 1.15x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 201 us: 1.15x faster                                                             |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 641 ms: 1.12x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 62.0 ms: 1.12x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.4 ms: 1.11x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.63 ms: 1.10x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.14 ms: 1.09x faster                                                            |
| async_generators           | 270 ms                                                          | 248 ms: 1.09x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.11 ms: 1.08x faster                                                            |
| generators                 | 21.8 ms                                                         | 20.2 ms: 1.08x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 56.1 ns: 1.07x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.66 sec: 1.07x faster                                                           |
| meteor_contest             | 74.6 ms                                                         | 70.5 ms: 1.06x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.8 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.3 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.3 ms: 1.02x faster                                                            |
| many_optionals             | 436 us                                                          | 451 us: 1.03x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 94.7 ms: 1.05x slower                                                            |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 17.1 ms: 1.16x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.60 sec: 1.17x slower                                                           |
| connected_components       | 267 ms                                                          | 322 ms: 1.21x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.13 ms: 1.22x slower                                                            |
| shortest_path              | 290 ms                                                          | 353 ms: 1.22x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.32 ms: 1.24x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-pythonperf1_win32-amd64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.311x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown