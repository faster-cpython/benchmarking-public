# Results vs. 3.13.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: windows-amd64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.301x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 338 ms: 1.35x slower                                                             |
| docutils       | 1.78 sec                                                        | 4.13 sec: 2.32x slower                                                           |
| html5lib       | 47.5 ms                                                         | 63.6 ms: 1.34x slower                                                            |
| sphinx         | 719 ms                                                          | 1.27 sec: 1.77x slower                                                           |
| Geometric mean | (ref)                                                           | 1.65x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                             |
| async_tree_io              | 526 ms                                                          | 574 ms: 1.09x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 309 ms: 1.09x slower                                                             |
| async_tree_none            | 245 ms                                                          | 272 ms: 1.11x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 553 ms: 1.12x slower                                                             |
| async_tree_memoization     | 297 ms                                                          | 337 ms: 1.14x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 246 ms: 1.15x slower                                                             |
| async_generators           | 270 ms                                                          | 408 ms: 1.51x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 32.5 ms: 2.00x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 140 ms: 1.44x faster                                                             |
| float          | 54.6 ms                                                         | 96.6 ms: 1.77x slower                                                            |
| nbody          | 80.0 ms                                                         | 181 ms: 2.26x slower                                                             |
| Geometric mean | (ref)                                                           | 1.41x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_dna      | 114 ms                                                          | 113 ms: 1.01x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.83 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 160 ms: 1.58x slower                                                             |
| Geometric mean | (ref)                                                           | 1.12x slower                                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.1 us: 1.02x slower                                                            |
| xml_etree_parse      | 107 ms                                                          | 111 ms: 1.03x slower                                                             |
| json_dumps           | 7.30 ms                                                         | 9.50 ms: 1.30x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 92.3 ms: 1.48x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 79.8 ms: 1.81x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 453 us: 1.96x slower                                                             |
| unpickle_pure_python | 160 us                                                          | 360 us: 2.25x slower                                                             |
| tomli_loads          | 1.71 sec                                                        | 5.09 sec: 2.97x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.64x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 66.2 ms: 1.32x slower                                                            |
| django_template | 29.8 ms                                                         | 45.8 ms: 1.54x slower                                                            |
| genshi_text     | 21.5 ms                                                         | 33.3 ms: 1.55x slower                                                            |
| mako            | 7.09 ms                                                         | 16.8 ms: 2.37x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.65x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 842 us: 11.85x faster                                                            |
| coverage                   | 324 ms                                                          | 84.7 ms: 3.83x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 145 ms: 2.50x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 35.5 ms: 2.34x faster                                                            |
| pidigits                   | 201 ms                                                          | 140 ms: 1.44x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.70 us: 1.15x faster                                                            |
| json                       | 4.27 ms                                                         | 4.17 ms: 1.03x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 88.5 ms: 1.02x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 453 ms: 1.01x faster                                                             |
| regex_dna                  | 114 ms                                                          | 113 ms: 1.01x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.83 ms: 1.01x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                            |
| json_loads                 | 21.6 us                                                         | 22.1 us: 1.02x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 111 ms: 1.03x slower                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.10 ms: 1.04x slower                                                            |
| deepcopy                   | 314 us                                                          | 334 us: 1.06x slower                                                             |
| async_tree_io              | 526 ms                                                          | 574 ms: 1.09x slower                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 309 ms: 1.09x slower                                                             |
| async_tree_none            | 245 ms                                                          | 272 ms: 1.11x slower                                                             |
| async_tree_io_tg           | 494 ms                                                          | 553 ms: 1.12x slower                                                             |
| async_tree_memoization     | 297 ms                                                          | 337 ms: 1.14x slower                                                             |
| async_tree_none_tg         | 214 ms                                                          | 246 ms: 1.15x slower                                                             |
| dulwich_log                | 48.8 ms                                                         | 56.0 ms: 1.15x slower                                                            |
| telco                      | 6.96 ms                                                         | 8.03 ms: 1.15x slower                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 3.48 us: 1.19x slower                                                            |
| pylint                     | 227 ms                                                          | 279 ms: 1.23x slower                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 1.25 ms: 1.25x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 9.50 ms: 1.30x slower                                                            |
| sympy_expand               | 373 ms                                                          | 493 ms: 1.32x slower                                                             |
| genshi_xml                 | 50.1 ms                                                         | 66.2 ms: 1.32x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 63.6 ms: 1.34x slower                                                            |
| logging_format             | 8.72 us                                                         | 11.7 us: 1.34x slower                                                            |
| 2to3                       | 250 ms                                                          | 338 ms: 1.35x slower                                                             |
| sympy_sum                  | 106 ms                                                          | 144 ms: 1.36x slower                                                             |
| sympy_str                  | 212 ms                                                          | 293 ms: 1.39x slower                                                             |
| logging_simple             | 7.99 us                                                         | 11.1 us: 1.39x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 21.0 ms: 1.40x slower                                                            |
| mdp                        | 1.62 sec                                                        | 2.31 sec: 1.42x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 201 us: 1.46x slower                                                             |
| many_optionals             | 436 us                                                          | 638 us: 1.46x slower                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 92.3 ms: 1.48x slower                                                            |
| async_generators           | 270 ms                                                          | 408 ms: 1.51x slower                                                             |
| django_template            | 29.8 ms                                                         | 45.8 ms: 1.54x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 33.3 ms: 1.55x slower                                                            |
| regex_compile              | 101 ms                                                          | 160 ms: 1.58x slower                                                             |
| meteor_contest             | 74.6 ms                                                         | 120 ms: 1.61x slower                                                             |
| deepcopy_memo              | 25.4 us                                                         | 43.3 us: 1.70x slower                                                            |
| go                         | 109 ms                                                          | 190 ms: 1.75x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 107 ms: 1.75x slower                                                             |
| sphinx                     | 719 ms                                                          | 1.27 sec: 1.77x slower                                                           |
| float                      | 54.6 ms                                                         | 96.6 ms: 1.77x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 128 ms: 1.78x slower                                                             |
| xml_etree_process          | 44.2 ms                                                         | 79.8 ms: 1.81x slower                                                            |
| generators                 | 21.8 ms                                                         | 39.4 ms: 1.81x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 27.5 ms: 1.86x slower                                                            |
| chaos                      | 50.2 ms                                                         | 95.9 ms: 1.91x slower                                                            |
| pycparser                  | 872 ms                                                          | 1.71 sec: 1.96x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 453 us: 1.96x slower                                                             |
| pyflate                    | 320 ms                                                          | 631 ms: 1.97x slower                                                             |
| fannkuch                   | 299 ms                                                          | 593 ms: 1.99x slower                                                             |
| raytrace                   | 201 ms                                                          | 403 ms: 2.00x slower                                                             |
| coroutines                 | 16.2 ms                                                         | 32.5 ms: 2.00x slower                                                            |
| scimark_fft                | 205 ms                                                          | 416 ms: 2.03x slower                                                             |
| comprehensions             | 12.5 us                                                         | 26.2 us: 2.10x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 120 ms: 2.10x slower                                                             |
| richards                   | 32.7 ms                                                         | 69.8 ms: 2.14x slower                                                            |
| richards_super             | 36.7 ms                                                         | 79.3 ms: 2.16x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 190 ms: 2.21x slower                                                             |
| k_core                     | 1.38 sec                                                        | 3.08 sec: 2.24x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 360 us: 2.25x slower                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 107 ms: 2.25x slower                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 6.40 ms: 2.25x slower                                                            |
| nbody                      | 80.0 ms                                                         | 181 ms: 2.26x slower                                                             |
| pprint_safe_repr           | 648 ms                                                          | 1.49 sec: 2.29x slower                                                           |
| docutils                   | 1.78 sec                                                        | 4.13 sec: 2.32x slower                                                           |
| mako                       | 7.09 ms                                                         | 16.8 ms: 2.37x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 10.7 ms: 2.41x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 8.38 sec: 2.42x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 170 ms: 2.45x slower                                                             |
| shortest_path              | 290 ms                                                          | 722 ms: 2.49x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 5.83 ms: 2.50x slower                                                            |
| connected_components       | 267 ms                                                          | 680 ms: 2.55x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 168 ms: 2.78x slower                                                             |
| tomli_loads                | 1.71 sec                                                        | 5.09 sec: 2.97x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 4.23 sec: 3.18x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 574 ns: 9.51x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.46x slower                                                                     |

Benchmark hidden because not significant (2): regex_v8, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf1_win32-amd64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.301x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: unknown