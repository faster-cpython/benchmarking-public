# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.096x faster
- HPT reliability: 97.05%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 234 ms: 1.07x faster                                                             |
| docutils       | 1.78 sec                                                        | 3.03 sec: 1.70x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.9 ms: 1.13x faster                                                            |
| sphinx         | 719 ms                                                          | 743 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                           | 1.10x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 155 ms: 2.35x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 342 ms: 1.45x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 150 ms: 1.43x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 198 ms: 1.42x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| async_tree_io              | 526 ms                                                          | 377 ms: 1.40x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 225 ms: 1.32x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.40x faster                                                                     |

Benchmark hidden because not significant (1): async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| float          | 54.6 ms                                                         | 47.7 ms: 1.15x faster                                                            |
| nbody          | 80.0 ms                                                         | 82.8 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.4 ms: 1.26x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.63 ms: 1.10x faster                                                            |
| regex_compile  | 101 ms                                                          | 99.5 ms: 1.02x faster                                                            |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|---------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads          | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| xml_etree_parse     | 107 ms                                                          | 92.1 ms: 1.17x faster                                                            |
| json_dumps          | 7.30 ms                                                         | 6.75 ms: 1.08x faster                                                            |
| xml_etree_iterparse | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                            |
| xml_etree_process   | 44.2 ms                                                         | 44.8 ms: 1.01x slower                                                            |
| pickle_pure_python  | 231 us                                                          | 240 us: 1.04x slower                                                             |
| xml_etree_generate  | 61.4 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| tomli_loads         | 1.71 sec                                                        | 2.75 sec: 1.61x slower                                                           |
| Geometric mean      | (ref)                                                           | 1.00x faster                                                                     |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 41.5 ms: 1.21x faster                                                            |
| django_template | 29.8 ms                                                         | 27.6 ms: 1.08x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 20.3 ms: 1.06x faster                                                            |
| mako            | 7.09 ms                                                         | 10.3 ms: 1.45x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 574 us: 17.39x faster                                                            |
| coverage                   | 324 ms                                                          | 67.7 ms: 4.79x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 32.8 ms: 2.53x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 155 ms: 2.35x faster                                                             |
| deepcopy                   | 314 us                                                          | 205 us: 1.53x faster                                                             |
| pidigits                   | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 342 ms: 1.45x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.21 ms: 1.44x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 150 ms: 1.43x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 198 ms: 1.42x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.42x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.39 us: 1.41x faster                                                            |
| async_tree_io              | 526 ms                                                          | 377 ms: 1.40x faster                                                             |
| json                       | 4.27 ms                                                         | 3.07 ms: 1.39x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| json_loads                 | 21.6 us                                                         | 15.8 us: 1.37x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.15 us: 1.36x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.25 ms: 1.33x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 225 ms: 1.32x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.24 sec: 1.31x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 13.4 ms: 1.26x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 41.5 ms: 1.21x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.1 us: 1.20x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.30 us: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 92.1 ms: 1.17x faster                                                            |
| go                         | 109 ms                                                          | 93.8 ms: 1.16x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 566 ms: 1.15x faster                                                             |
| float                      | 54.6 ms                                                         | 47.7 ms: 1.15x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 42.8 ms: 1.14x faster                                                            |
| sympy_expand               | 373 ms                                                          | 328 ms: 1.14x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 41.9 ms: 1.13x faster                                                            |
| logging_simple             | 7.99 us                                                         | 7.08 us: 1.13x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 80.3 ms: 1.13x faster                                                            |
| sympy_str                  | 212 ms                                                          | 192 ms: 1.11x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.63 ms: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.1 ms: 1.09x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.75 ms: 1.08x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.6 ms: 1.08x faster                                                            |
| pycparser                  | 872 ms                                                          | 811 ms: 1.07x faster                                                             |
| 2to3                       | 250 ms                                                          | 234 ms: 1.07x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 98.8 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 129 us: 1.07x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 20.3 ms: 1.06x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                            |
| pylint                     | 227 ms                                                          | 217 ms: 1.05x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.01 ms: 1.05x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.3 ms: 1.05x faster                                                            |
| comprehensions             | 12.5 us                                                         | 12.1 us: 1.03x faster                                                            |
| regex_compile              | 101 ms                                                          | 99.5 ms: 1.02x faster                                                            |
| pyflate                    | 320 ms                                                          | 316 ms: 1.01x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 57.6 ms: 1.01x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 44.8 ms: 1.01x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 87.8 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 306 ms: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                             |
| sphinx                     | 719 ms                                                          | 743 ms: 1.03x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 74.5 ms: 1.03x slower                                                            |
| richards                   | 32.7 ms                                                         | 33.8 ms: 1.04x slower                                                            |
| nbody                      | 80.0 ms                                                         | 82.8 ms: 1.04x slower                                                            |
| scimark_fft                | 205 ms                                                          | 213 ms: 1.04x slower                                                             |
| pickle_pure_python         | 231 us                                                          | 240 us: 1.04x slower                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 49.6 ms: 1.04x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 64.0 ms: 1.04x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.47 ms: 1.06x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.3 ms: 1.07x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.78 ms: 1.08x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 65.6 ms: 1.09x slower                                                            |
| generators                 | 21.8 ms                                                         | 23.7 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.09 ms: 1.09x slower                                                            |
| raytrace                   | 201 ms                                                          | 220 ms: 1.09x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 75.9 ms: 1.09x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 66.7 ns: 1.11x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.11 ms: 1.11x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 87.3 ms: 1.17x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.76 sec: 1.32x slower                                                           |
| mako                       | 7.09 ms                                                         | 10.3 ms: 1.45x slower                                                            |
| many_optionals             | 436 us                                                          | 654 us: 1.50x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 2.75 sec: 1.61x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.63 sec: 1.63x slower                                                           |
| docutils                   | 1.78 sec                                                        | 3.03 sec: 1.70x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.73 sec: 1.98x slower                                                           |
| shortest_path              | 290 ms                                                          | 659 ms: 2.27x slower                                                             |
| connected_components       | 267 ms                                                          | 630 ms: 2.36x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 36.1 ms: 2.45x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                     |

Benchmark hidden because not significant (2): async_generators, unpickle_pure_python
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f-NOGIL/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.096x faster

# HPT report

- Reliability score: 97.05% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown