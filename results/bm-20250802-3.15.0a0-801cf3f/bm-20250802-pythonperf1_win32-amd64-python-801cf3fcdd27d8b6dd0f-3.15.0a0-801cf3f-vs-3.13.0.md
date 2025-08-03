# Results vs. 3.13.0

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: windows-amd64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.238x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 39.5 ms: 1.20x faster                                                            |
| sphinx         | 719 ms                                                          | 651 ms: 1.10x faster                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 162 ms: 2.24x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 339 ms: 1.43x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 218 ms: 1.36x faster                                                             |
| async_tree_none            | 245 ms                                                          | 183 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 398 ms: 1.32x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 348 ms: 1.31x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 218 ms: 1.29x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 173 ms: 1.24x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 406 ms: 1.22x faster                                                             |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.34x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| nbody          | 80.0 ms                                                         | 65.3 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 81.0 ms: 1.25x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.64 ms: 1.10x faster                                                            |
| regex_dna      | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 134 us: 1.19x faster                                                             |
| xml_etree_parse      | 107 ms                                                          | 90.8 ms: 1.18x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.35 ms: 1.15x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 40.0 ms: 1.10x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 212 us: 1.09x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 58.0 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.1 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.2 ms: 1.42x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| django_template | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| mako            | 7.09 ms                                                         | 6.67 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.26x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 504 us: 19.80x faster                                                            |
| coverage                   | 324 ms                                                          | 51.3 ms: 6.32x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 33.0 ms: 2.51x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 162 ms: 2.24x faster                                                             |
| mdp                        | 1.62 sec                                                        | 824 ms: 1.97x faster                                                             |
| deepcopy                   | 314 us                                                          | 175 us: 1.79x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.91 us: 1.53x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.61 ms: 1.51x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 339 ms: 1.43x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 35.2 ms: 1.42x faster                                                            |
| go                         | 109 ms                                                          | 77.1 ms: 1.41x faster                                                            |
| json                       | 4.27 ms                                                         | 3.09 ms: 1.38x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.4 us: 1.38x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.38x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 218 ms: 1.36x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 102 us: 1.35x faster                                                             |
| async_tree_none            | 245 ms                                                          | 183 ms: 1.34x faster                                                             |
| async_tree_io              | 526 ms                                                          | 398 ms: 1.32x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 348 ms: 1.31x faster                                                             |
| sympy_expand               | 373 ms                                                          | 288 ms: 1.30x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 218 ms: 1.29x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.76 us: 1.29x faster                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.03 sec: 1.29x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 509 ms: 1.27x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.34 us: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| regex_compile              | 101 ms                                                          | 81.0 ms: 1.25x faster                                                            |
| sympy_str                  | 212 ms                                                          | 171 ms: 1.24x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 173 ms: 1.24x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.58 us: 1.24x faster                                                            |
| nbody                      | 80.0 ms                                                         | 65.3 ms: 1.22x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 406 ms: 1.22x faster                                                             |
| chaos                      | 50.2 ms                                                         | 41.3 ms: 1.22x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.6 ms: 1.21x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.42 sec: 1.21x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 39.5 ms: 1.20x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 134 us: 1.19x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.1 ms: 1.19x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.8 ms: 1.18x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 89.5 ms: 1.18x faster                                                            |
| pycparser                  | 872 ms                                                          | 739 ms: 1.18x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.96 sec: 1.17x faster                                                           |
| fannkuch                   | 299 ms                                                          | 256 ms: 1.17x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 49.2 ms: 1.16x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.8 us: 1.16x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 868 us: 1.15x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 6.35 ms: 1.15x faster                                                            |
| richards_super             | 36.7 ms                                                         | 32.1 ms: 1.14x faster                                                            |
| pylint                     | 227 ms                                                          | 199 ms: 1.14x faster                                                             |
| async_generators           | 270 ms                                                          | 237 ms: 1.14x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.9 ms: 1.14x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 63.5 ms: 1.13x faster                                                            |
| richards                   | 32.7 ms                                                         | 29.0 ms: 1.13x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                            |
| raytrace                   | 201 ms                                                          | 181 ms: 1.11x faster                                                             |
| scimark_fft                | 205 ms                                                          | 184 ms: 1.11x faster                                                             |
| pyflate                    | 320 ms                                                          | 289 ms: 1.11x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 40.0 ms: 1.10x faster                                                            |
| sphinx                     | 719 ms                                                          | 651 ms: 1.10x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.10x faster                                                           |
| 2to3                       | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 78.2 ms: 1.10x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.64 ms: 1.10x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 212 us: 1.09x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.60 ms: 1.09x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.67 ms: 1.06x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.19 ms: 1.06x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 58.0 ms: 1.06x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.2 ms: 1.03x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 67.2 ms: 1.03x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 58.6 ns: 1.03x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.27 ms: 1.03x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.1 ms: 1.06x slower                                                            |
| regex_dna                  | 114 ms                                                          | 121 ms: 1.06x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 96.9 ms: 1.07x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.10 ms: 1.20x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.68 sec: 1.22x slower                                                           |
| shortest_path              | 290 ms                                                          | 361 ms: 1.25x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.33 ms: 1.25x slower                                                            |
| connected_components       | 267 ms                                                          | 335 ms: 1.25x slower                                                             |
| many_optionals             | 436 us                                                          | 575 us: 1.32x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 31.1 ms: 2.11x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                     |

Benchmark hidden because not significant (1): scimark_lu
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-pythonperf1_win32-amd64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.238x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown