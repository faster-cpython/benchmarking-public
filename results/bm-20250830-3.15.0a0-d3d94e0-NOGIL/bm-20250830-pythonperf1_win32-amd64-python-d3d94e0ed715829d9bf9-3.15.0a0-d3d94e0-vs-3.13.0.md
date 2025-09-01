# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.116x faster
- HPT reliability: 98.70%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.88 sec: 1.62x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.8 ms: 1.14x faster                                                            |
| sphinx         | 719 ms                                                          | 664 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 136 ms: 2.67x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 188 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 330 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 308 ms: 1.48x faster                                                             |
| async_tree_io              | 526 ms                                                          | 355 ms: 1.48x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 211 ms: 1.41x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.46x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| float          | 54.6 ms                                                         | 45.7 ms: 1.20x faster                                                            |
| nbody          | 80.0 ms                                                         | 80.8 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.63 ms: 1.11x faster                                                            |
| regex_compile  | 101 ms                                                          | 95.4 ms: 1.06x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 16.0 us: 1.35x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.95 ms: 1.23x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 62.1 ms: 1.01x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 163 us: 1.02x slower                                                             |
| xml_etree_process    | 44.2 ms                                                         | 45.5 ms: 1.03x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 239 us: 1.03x slower                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 63.8 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 2.36 sec: 1.37x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.01x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                            |
| django_template | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 19.9 ms: 1.08x faster                                                            |
| mako            | 7.09 ms                                                         | 10.1 ms: 1.43x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 567 us: 17.60x faster                                                            |
| coverage                   | 324 ms                                                          | 68.2 ms: 4.75x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.8 ms: 2.78x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 136 ms: 2.67x faster                                                             |
| deepcopy                   | 314 us                                                          | 205 us: 1.53x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 188 ms: 1.50x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 330 ms: 1.50x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 308 ms: 1.48x faster                                                             |
| async_tree_io              | 526 ms                                                          | 355 ms: 1.48x faster                                                             |
| pidigits                   | 201 ms                                                          | 136 ms: 1.48x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 147 ms: 1.46x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 334 ms: 1.45x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.13 sec: 1.44x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.37 us: 1.43x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.23 ms: 1.43x faster                                                            |
| async_tree_none            | 245 ms                                                          | 173 ms: 1.41x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 211 ms: 1.41x faster                                                             |
| json                       | 4.27 ms                                                         | 3.12 ms: 1.37x faster                                                            |
| json_loads                 | 21.6 us                                                         | 16.0 us: 1.35x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.19 us: 1.33x faster                                                            |
| telco                      | 6.96 ms                                                         | 5.27 ms: 1.32x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 40.7 ms: 1.23x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.10 us: 1.23x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.95 ms: 1.23x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.60 us: 1.21x faster                                                            |
| pycparser                  | 872 ms                                                          | 728 ms: 1.20x faster                                                             |
| float                      | 54.6 ms                                                         | 45.7 ms: 1.20x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.3 us: 1.19x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 41.6 ms: 1.17x faster                                                            |
| go                         | 109 ms                                                          | 93.5 ms: 1.16x faster                                                            |
| sympy_expand               | 373 ms                                                          | 324 ms: 1.15x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 79.2 ms: 1.14x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 41.8 ms: 1.14x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 571 ms: 1.14x faster                                                             |
| pylint                     | 227 ms                                                          | 202 ms: 1.12x faster                                                             |
| sympy_str                  | 212 ms                                                          | 190 ms: 1.12x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.63 ms: 1.11x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| 2to3                       | 250 ms                                                          | 228 ms: 1.10x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.9 ms: 1.09x faster                                                            |
| chaos                      | 50.2 ms                                                         | 46.0 ms: 1.09x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.5 ms: 1.08x faster                                                            |
| sphinx                     | 719 ms                                                          | 664 ms: 1.08x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 19.9 ms: 1.08x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 97.5 ms: 1.08x faster                                                            |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| regex_compile              | 101 ms                                                          | 95.4 ms: 1.06x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 131 us: 1.05x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 14.4 ms: 1.04x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.02 ms: 1.04x faster                                                            |
| pyflate                    | 320 ms                                                          | 311 ms: 1.03x faster                                                             |
| comprehensions             | 12.5 us                                                         | 12.2 us: 1.02x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 105 ms: 1.02x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 56.1 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 62.1 ms: 1.01x faster                                                            |
| nbody                      | 80.0 ms                                                         | 80.8 ms: 1.01x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 72.9 ms: 1.01x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 163 us: 1.02x slower                                                             |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| deltablue                  | 2.33 ms                                                         | 2.39 ms: 1.02x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 61.9 ns: 1.03x slower                                                            |
| richards                   | 32.7 ms                                                         | 33.6 ms: 1.03x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 45.5 ms: 1.03x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 239 us: 1.03x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 71.7 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 309 ms: 1.03x slower                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 63.8 ms: 1.04x slower                                                            |
| generators                 | 21.8 ms                                                         | 22.8 ms: 1.05x slower                                                            |
| raytrace                   | 201 ms                                                          | 211 ms: 1.05x slower                                                             |
| scimark_fft                | 205 ms                                                          | 215 ms: 1.05x slower                                                             |
| scimark_sor                | 85.9 ms                                                         | 90.5 ms: 1.05x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.0 ms: 1.07x slower                                                            |
| richards_super             | 36.7 ms                                                         | 39.5 ms: 1.08x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.08 ms: 1.08x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.80 ms: 1.08x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.13 ms: 1.10x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 66.7 ms: 1.11x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 86.7 ms: 1.16x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.70 sec: 1.28x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 2.36 sec: 1.37x slower                                                           |
| mako                       | 7.09 ms                                                         | 10.1 ms: 1.43x slower                                                            |
| many_optionals             | 436 us                                                          | 647 us: 1.48x slower                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 5.56 sec: 1.61x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.88 sec: 1.62x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.70 sec: 1.96x slower                                                           |
| shortest_path              | 290 ms                                                          | 653 ms: 2.25x slower                                                             |
| connected_components       | 267 ms                                                          | 616 ms: 2.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 35.2 ms: 2.38x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 98.70% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown