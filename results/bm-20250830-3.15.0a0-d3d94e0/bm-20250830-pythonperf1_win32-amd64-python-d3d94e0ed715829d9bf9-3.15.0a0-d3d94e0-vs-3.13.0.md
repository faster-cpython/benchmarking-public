# Results vs. 3.13.0

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: windows-amd64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.261x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_io              | 526 ms                                                          | 384 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 391 ms: 1.26x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 171 ms: 1.25x faster                                                             |
| async_generators           | 270 ms                                                          | 226 ms: 1.19x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| float          | 54.6 ms                                                         | 44.4 ms: 1.23x faster                                                            |
| nbody          | 80.0 ms                                                         | 65.5 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| regex_compile  | 101 ms                                                          | 80.8 ms: 1.25x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.52 ms: 1.19x faster                                                            |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.45 ms: 1.34x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.8 ms: 1.22x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 140 us: 1.14x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 39.8 ms: 1.11x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 56.9 ms: 1.08x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 218 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.7 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| django_template | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.79 ms: 1.04x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 498 us: 20.04x faster                                                            |
| coverage                   | 324 ms                                                          | 49.7 ms: 6.52x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 29.8 ms: 2.78x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 159 ms: 2.28x faster                                                             |
| mdp                        | 1.62 sec                                                        | 815 ms: 1.99x faster                                                             |
| deepcopy                   | 314 us                                                          | 173 us: 1.81x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.16 ms: 1.67x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.59x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 326 ms: 1.48x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 33.9 ms: 1.48x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| json                       | 4.27 ms                                                         | 2.99 ms: 1.43x faster                                                            |
| async_tree_none            | 245 ms                                                          | 174 ms: 1.41x faster                                                             |
| go                         | 109 ms                                                          | 77.5 ms: 1.40x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.4 ms: 1.40x faster                                                            |
| pidigits                   | 201 ms                                                          | 145 ms: 1.39x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 332 ms: 1.37x faster                                                             |
| async_tree_io              | 526 ms                                                          | 384 ms: 1.37x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 208 ms: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.47 us: 1.35x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.45 ms: 1.34x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 105 us: 1.32x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.10 us: 1.31x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 19.5 us: 1.31x faster                                                            |
| sympy_expand               | 373 ms                                                          | 287 ms: 1.30x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.03 sec: 1.29x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 506 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 391 ms: 1.26x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 169 ms: 1.26x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 171 ms: 1.25x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| regex_compile              | 101 ms                                                          | 80.8 ms: 1.25x faster                                                            |
| float                      | 54.6 ms                                                         | 44.4 ms: 1.23x faster                                                            |
| pycparser                  | 872 ms                                                          | 711 ms: 1.23x faster                                                             |
| chaos                      | 50.2 ms                                                         | 41.0 ms: 1.23x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.8 ms: 1.22x faster                                                            |
| nbody                      | 80.0 ms                                                         | 65.5 ms: 1.22x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.41 sec: 1.22x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.60 us: 1.22x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.5 ms: 1.22x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.1 ms: 1.22x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.8 ms: 1.20x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.4 ms: 1.20x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 2.90 sec: 1.20x faster                                                           |
| async_generators           | 270 ms                                                          | 226 ms: 1.19x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.52 ms: 1.19x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 61.1 ms: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 856 us: 1.17x faster                                                             |
| richards_super             | 36.7 ms                                                         | 31.4 ms: 1.17x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.0 ms: 1.16x faster                                                            |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| richards                   | 32.7 ms                                                         | 28.4 ms: 1.15x faster                                                            |
| 2to3                       | 250 ms                                                          | 218 ms: 1.15x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 140 us: 1.14x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.2 ms: 1.14x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.1 ms: 1.14x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.0 us: 1.13x faster                                                            |
| sphinx                     | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                             |
| scimark_fft                | 205 ms                                                          | 181 ms: 1.13x faster                                                             |
| fannkuch                   | 299 ms                                                          | 267 ms: 1.12x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 39.8 ms: 1.11x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 78.0 ms: 1.10x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.62 sec: 1.10x faster                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.58 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 56.9 ms: 1.08x faster                                                            |
| pyflate                    | 320 ms                                                          | 298 ms: 1.07x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.14 ms: 1.07x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 64.8 ms: 1.07x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 218 us: 1.06x faster                                                             |
| logging_silent             | 60.3 ns                                                         | 57.3 ns: 1.05x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.23 ms: 1.05x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.79 ms: 1.04x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 58.4 ms: 1.03x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.6 ms: 1.03x faster                                                            |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 93.3 ms: 1.03x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.7 ms: 1.03x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.09 ms: 1.19x slower                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.29 ms: 1.22x slower                                                            |
| many_optionals             | 436 us                                                          | 543 us: 1.25x slower                                                             |
| connected_components       | 267 ms                                                          | 333 ms: 1.25x slower                                                             |
| k_core                     | 1.38 sec                                                        | 1.72 sec: 1.25x slower                                                           |
| shortest_path              | 290 ms                                                          | 364 ms: 1.26x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.2 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-pythonperf1_win32-amd64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.261x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown