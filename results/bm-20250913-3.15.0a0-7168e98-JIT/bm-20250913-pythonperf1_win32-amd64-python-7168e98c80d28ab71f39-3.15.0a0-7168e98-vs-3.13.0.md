# Results vs. 3.13.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 623 ms: 1.15x faster                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 198 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| async_tree_io              | 526 ms                                                          | 380 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 375 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 163 ms: 1.32x faster                                                             |
| async_generators           | 270 ms                                                          | 242 ms: 1.11x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 15.3 ms: 1.06x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 53.1 ms: 1.51x faster                                                            |
| pidigits       | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| float          | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| Geometric mean | (ref)                                                           | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 76.9 ms: 1.31x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.3 ms: 1.27x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.17x faster                                                            |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.08 sec: 1.59x faster                                                           |
| json_loads           | 21.6 us                                                         | 13.7 us: 1.58x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 103 us: 1.56x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.35 ms: 1.36x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 34.6 ms: 1.28x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 84.5 ms: 1.27x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 196 us: 1.18x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 61.5 ms: 1.02x faster                                                            |
| Geometric mean       | (ref)                                                           | 1.32x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 24.8 ms: 1.14x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.8 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| mako            | 7.09 ms                                                         | 5.27 ms: 1.34x faster                                                            |
| django_template | 29.8 ms                                                         | 24.7 ms: 1.21x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 498 us: 20.03x faster                                                            |
| coverage                   | 324 ms                                                          | 49.5 ms: 6.54x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 28.6 ms: 2.90x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| mdp                        | 1.62 sec                                                        | 789 ms: 2.06x faster                                                             |
| deepcopy                   | 314 us                                                          | 163 us: 1.93x faster                                                             |
| telco                      | 6.96 ms                                                         | 3.74 ms: 1.86x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.76 us: 1.65x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.08 sec: 1.59x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 841 ms: 1.58x faster                                                             |
| json_loads                 | 21.6 us                                                         | 13.7 us: 1.58x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 412 ms: 1.57x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 103 us: 1.56x faster                                                             |
| deepcopy_memo              | 25.4 us                                                         | 16.4 us: 1.54x faster                                                            |
| nbody                      | 80.0 ms                                                         | 53.1 ms: 1.51x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 198 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 327 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| json                       | 4.27 ms                                                         | 2.90 ms: 1.48x faster                                                            |
| richards                   | 32.7 ms                                                         | 22.2 ms: 1.48x faster                                                            |
| go                         | 109 ms                                                          | 74.7 ms: 1.46x faster                                                            |
| async_tree_none            | 245 ms                                                          | 168 ms: 1.46x faster                                                             |
| fannkuch                   | 299 ms                                                          | 209 ms: 1.43x faster                                                             |
| richards_super             | 36.7 ms                                                         | 26.2 ms: 1.40x faster                                                            |
| scimark_fft                | 205 ms                                                          | 146 ms: 1.40x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.39x faster                                                            |
| async_tree_io              | 526 ms                                                          | 380 ms: 1.38x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.50 sec: 1.38x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| json_dumps                 | 7.30 ms                                                         | 5.35 ms: 1.36x faster                                                            |
| logging_format             | 8.72 us                                                         | 6.43 us: 1.36x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 209 ms: 1.35x faster                                                             |
| pidigits                   | 201 ms                                                          | 149 ms: 1.35x faster                                                             |
| mako                       | 7.09 ms                                                         | 5.27 ms: 1.34x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 103 us: 1.34x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.01 us: 1.33x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 375 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 163 ms: 1.32x faster                                                             |
| regex_compile              | 101 ms                                                          | 76.9 ms: 1.31x faster                                                            |
| sympy_expand               | 373 ms                                                          | 289 ms: 1.29x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.51 us: 1.29x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 34.6 ms: 1.28x faster                                                            |
| sympy_str                  | 212 ms                                                          | 166 ms: 1.28x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 44.7 ms: 1.27x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 84.5 ms: 1.27x faster                                                            |
| pycparser                  | 872 ms                                                          | 687 ms: 1.27x faster                                                             |
| pyflate                    | 320 ms                                                          | 253 ms: 1.27x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.3 ms: 1.27x faster                                                            |
| chaos                      | 50.2 ms                                                         | 39.7 ms: 1.27x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 38.8 ms: 1.26x faster                                                            |
| float                      | 54.6 ms                                                         | 43.5 ms: 1.25x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.28 ms: 1.25x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 38.5 ms: 1.24x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 85.2 ms: 1.24x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 50.8 ms: 1.21x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.7 ms: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 60.6 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 843 us: 1.19x faster                                                             |
| raytrace                   | 201 ms                                                          | 170 ms: 1.19x faster                                                             |
| comprehensions             | 12.5 us                                                         | 10.6 us: 1.18x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 196 us: 1.18x faster                                                             |
| pylint                     | 227 ms                                                          | 193 ms: 1.17x faster                                                             |
| 2to3                       | 250 ms                                                          | 214 ms: 1.17x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.17x faster                                                            |
| sphinx                     | 719 ms                                                          | 623 ms: 1.15x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.1 ms: 1.14x faster                                                            |
| python_startup             | 28.3 ms                                                         | 24.8 ms: 1.14x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 75.8 ms: 1.13x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 53.4 ns: 1.13x faster                                                            |
| async_generators           | 270 ms                                                          | 242 ms: 1.11x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.61 sec: 1.11x faster                                                           |
| hexiom                     | 4.44 ms                                                         | 4.07 ms: 1.09x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.15 ms: 1.08x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 15.3 ms: 1.06x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 66.0 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.8 ms: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.8 ms: 1.04x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 87.9 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.1 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 61.5 ms: 1.02x faster                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.59 sec: 1.15x slower                                                           |
| connected_components       | 267 ms                                                          | 318 ms: 1.19x slower                                                             |
| gc_traversal               | 1.75 ms                                                         | 2.09 ms: 1.20x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.27 ms: 1.20x slower                                                            |
| shortest_path              | 290 ms                                                          | 351 ms: 1.21x slower                                                             |
| many_optionals             | 436 us                                                          | 560 us: 1.28x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.5 ms: 2.00x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250913-3.15.0a0-7168e98-JIT/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: unknown