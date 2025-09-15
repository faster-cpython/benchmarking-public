# Results vs. 3.13.0

- fork: python
- ref: 7168e98c80d28ab71f39
- machine: windows-amd64
- commit hash: 7168e98
- commit date: 2025-09-13
- overall geometric mean: 1.119x faster
- HPT reliability: 99.03%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.84 sec: 1.60x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                            |
| sphinx         | 719 ms                                                          | 669 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                             |
| async_tree_io              | 526 ms                                                          | 356 ms: 1.48x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 339 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 335 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 319 ms: 1.43x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 199 ms: 1.42x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 153 ms: 1.40x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 216 ms: 1.37x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                            |
| async_generators           | 270 ms                                                          | 265 ms: 1.02x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.43x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| float          | 54.6 ms                                                         | 46.3 ms: 1.18x faster                                                            |
| nbody          | 80.0 ms                                                         | 81.4 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.19x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.3 ms: 1.27x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                            |
| regex_compile  | 101 ms                                                          | 94.7 ms: 1.07x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.0 us: 1.35x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.11 ms: 1.19x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 92.9 ms: 1.16x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 157 us: 1.02x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 44.8 ms: 1.01x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 238 us: 1.03x slower                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 64.1 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.41 sec: 1.40x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.08x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 41.0 ms: 1.22x faster                                                            |
| django_template | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 20.1 ms: 1.07x faster                                                            |
| mako            | 7.09 ms                                                         | 9.98 ms: 1.41x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 568 us: 17.57x faster                                                            |
| coverage                   | 324 ms                                                          | 67.6 ms: 4.79x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.0 ms: 2.86x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 143 ms: 2.54x faster                                                             |
| deepcopy                   | 314 us                                                          | 190 us: 1.65x faster                                                             |
| async_tree_io              | 526 ms                                                          | 356 ms: 1.48x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 339 ms: 1.46x faster                                                             |
| pidigits                   | 201 ms                                                          | 138 ms: 1.45x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.80 ms: 1.45x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.35 us: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 335 ms: 1.44x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 319 ms: 1.43x faster                                                             |
| async_tree_none            | 245 ms                                                          | 172 ms: 1.42x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 2.05 us: 1.42x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 199 ms: 1.42x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.16 sec: 1.40x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 153 ms: 1.40x faster                                                             |
| json                       | 4.27 ms                                                         | 3.09 ms: 1.38x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.27 ms: 1.38x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 216 ms: 1.37x faster                                                             |
| json_loads                 | 21.6 us                                                         | 16.0 us: 1.35x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.5 us: 1.30x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.3 ms: 1.27x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 41.0 ms: 1.22x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.22 us: 1.21x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 75.1 ms: 1.21x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.11 ms: 1.19x faster                                                            |
| go                         | 109 ms                                                          | 91.4 ms: 1.19x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.72 us: 1.19x faster                                                            |
| float                      | 54.6 ms                                                         | 46.3 ms: 1.18x faster                                                            |
| sympy_expand               | 373 ms                                                          | 319 ms: 1.17x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 92.9 ms: 1.16x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.3 ms: 1.15x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 565 ms: 1.15x faster                                                             |
| pycparser                  | 872 ms                                                          | 761 ms: 1.15x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 42.9 ms: 1.14x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.59 ms: 1.14x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.3 ms: 1.14x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.2 ms: 1.12x faster                                                            |
| sympy_str                  | 212 ms                                                          | 189 ms: 1.12x faster                                                             |
| 2to3                       | 250 ms                                                          | 227 ms: 1.10x faster                                                             |
| django_template            | 29.8 ms                                                         | 27.3 ms: 1.09x faster                                                            |
| pylint                     | 227 ms                                                          | 208 ms: 1.09x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 97.0 ms: 1.09x faster                                                            |
| sphinx                     | 719 ms                                                          | 669 ms: 1.08x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 20.1 ms: 1.07x faster                                                            |
| regex_compile              | 101 ms                                                          | 94.7 ms: 1.07x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 14.1 ms: 1.06x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 59.6 ms: 1.05x faster                                                            |
| chaos                      | 50.2 ms                                                         | 47.8 ms: 1.05x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 132 us: 1.05x faster                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.01 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 18.9 ms: 1.04x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 157 us: 1.02x faster                                                             |
| async_generators           | 270 ms                                                          | 265 ms: 1.02x faster                                                             |
| pyflate                    | 320 ms                                                          | 316 ms: 1.01x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 70.1 ms: 1.01x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 57.6 ms: 1.01x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 87.1 ms: 1.01x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 44.8 ms: 1.01x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 73.2 ms: 1.02x slower                                                            |
| richards                   | 32.7 ms                                                         | 33.2 ms: 1.02x slower                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| nbody                      | 80.0 ms                                                         | 81.4 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.5 ns: 1.02x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 238 us: 1.03x slower                                                             |
| fannkuch                   | 299 ms                                                          | 309 ms: 1.03x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 2.42 ms: 1.04x slower                                                            |
| scimark_fft                | 205 ms                                                          | 212 ms: 1.04x slower                                                             |
| generators                 | 21.8 ms                                                         | 22.7 ms: 1.04x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 64.1 ms: 1.04x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.65 ms: 1.05x slower                                                            |
| raytrace                   | 201 ms                                                          | 214 ms: 1.06x slower                                                             |
| richards_super             | 36.7 ms                                                         | 39.1 ms: 1.07x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 50.9 ms: 1.07x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 65.4 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.09 ms: 1.09x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.12 ms: 1.11x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 88.2 ms: 1.18x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.73 sec: 1.31x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.41 sec: 1.40x slower                                                           |
| mako                       | 7.09 ms                                                         | 9.98 ms: 1.41x slower                                                            |
| many_optionals             | 436 us                                                          | 627 us: 1.44x slower                                                             |
| docutils                   | 1.78 sec                                                        | 2.84 sec: 1.60x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.54 sec: 1.60x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.70 sec: 1.96x slower                                                           |
| shortest_path              | 290 ms                                                          | 670 ms: 2.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 34.8 ms: 2.36x slower                                                            |
| connected_components       | 267 ms                                                          | 631 ms: 2.37x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                     |

Benchmark hidden because not significant (1): comprehensions
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250913-3.15.0a0-7168e98-NOGIL/bm-20250913-pythonperf1_win32-amd64-python-7168e98c80d28ab71f39-3.15.0a0-7168e98.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.119x faster

# HPT report

- Reliability score: 99.03% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown