# Results vs. 3.13.0

- fork: python
- ref: 0ac40acec045c4ce780c
- machine: windows-x86
- commit hash: 0ac40ac
- commit date: 2024-12-14
- overall geometric mean: 1.042x faster
- HPT reliability: 58.52%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 240 ms: 1.04x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 45.3 ms: 1.05x faster                                                           |
| sphinx         | 719 ms                                                          | 734 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 227 ms: 1.25x faster                                                            |
| async_tree_none            | 245 ms                                                          | 199 ms: 1.23x faster                                                            |
| async_tree_io              | 526 ms                                                          | 433 ms: 1.21x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 246 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 415 ms: 1.19x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 182 ms: 1.18x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.01x slower                                                           |
| async_generators           | 270 ms                                                          | 287 ms: 1.06x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.00x slower                                                            |
| float          | 54.6 ms                                                         | 58.2 ms: 1.07x slower                                                           |
| nbody          | 80.0 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                           |
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                            |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.4 us: 1.06x faster                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.68 sec: 1.02x faster                                                          |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 167 us: 1.04x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.6 ms: 1.07x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 47.6 ms: 1.08x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 274 us: 1.19x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 8.69 ms: 1.19x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.2 ms: 1.11x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 20.7 ms: 1.04x faster                                                           |
| django_template | 29.8 ms                                                         | 31.6 ms: 1.06x slower                                                           |
| mako            | 7.09 ms                                                         | 7.61 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 767 us: 13.01x faster                                                           |
| coverage                   | 324 ms                                                          | 52.5 ms: 6.17x faster                                                           |
| deepcopy                   | 314 us                                                          | 229 us: 1.37x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 227 ms: 1.25x faster                                                            |
| async_tree_none            | 245 ms                                                          | 199 ms: 1.23x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.7 us: 1.23x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.40 us: 1.21x faster                                                           |
| async_tree_io              | 526 ms                                                          | 433 ms: 1.21x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 246 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 415 ms: 1.19x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 182 ms: 1.18x faster                                                            |
| go                         | 109 ms                                                          | 94.8 ms: 1.15x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 45.2 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 442 ms: 1.10x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.65 ms: 1.09x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.51 ms: 1.07x faster                                                           |
| json_loads                 | 21.6 us                                                         | 20.4 us: 1.06x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 45.3 ms: 1.05x faster                                                           |
| python_startup             | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                           |
| pylint                     | 227 ms                                                          | 217 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 437 ms: 1.04x faster                                                            |
| 2to3                       | 250 ms                                                          | 240 ms: 1.04x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 20.7 ms: 1.04x faster                                                           |
| pycparser                  | 872 ms                                                          | 840 ms: 1.04x faster                                                            |
| logging_simple             | 7.99 us                                                         | 7.71 us: 1.04x faster                                                           |
| connected_components       | 267 ms                                                          | 258 ms: 1.03x faster                                                            |
| logging_format             | 8.72 us                                                         | 8.46 us: 1.03x faster                                                           |
| json                       | 4.27 ms                                                         | 4.15 ms: 1.03x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 636 ms: 1.02x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.68 sec: 1.02x faster                                                          |
| spectral_norm              | 69.4 ms                                                         | 68.4 ms: 1.01x faster                                                           |
| fannkuch                   | 299 ms                                                          | 295 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.43 sec: 1.01x faster                                                          |
| shortest_path              | 290 ms                                                          | 288 ms: 1.01x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.94 us: 1.00x faster                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 41.3 ms: 1.00x faster                                                           |
| sympy_expand               | 373 ms                                                          | 374 ms: 1.00x slower                                                            |
| pidigits                   | 201 ms                                                          | 202 ms: 1.00x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 15.1 ms: 1.01x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.80 sec: 1.01x slower                                                          |
| typing_runtime_protocols   | 138 us                                                          | 139 us: 1.01x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.01x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.90 ms: 1.02x slower                                                           |
| sphinx                     | 719 ms                                                          | 734 ms: 1.02x slower                                                            |
| regex_compile              | 101 ms                                                          | 103 ms: 1.02x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 50.0 ms: 1.03x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 93.0 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.28 ms: 1.03x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 58.8 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.04 ms: 1.03x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 74.9 ms: 1.04x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 167 us: 1.04x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| async_generators           | 270 ms                                                          | 287 ms: 1.06x slower                                                            |
| django_template            | 29.8 ms                                                         | 31.6 ms: 1.06x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.6 ms: 1.07x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 79.6 ms: 1.07x slower                                                           |
| float                      | 54.6 ms                                                         | 58.2 ms: 1.07x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 4.74 ms: 1.07x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.4 us: 1.07x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.61 ms: 1.07x slower                                                           |
| nbody                      | 80.0 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| pyflate                    | 320 ms                                                          | 345 ms: 1.08x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 47.6 ms: 1.08x slower                                                           |
| chaos                      | 50.2 ms                                                         | 54.1 ms: 1.08x slower                                                           |
| generators                 | 21.8 ms                                                         | 23.7 ms: 1.09x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 52.1 ms: 1.09x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.57 ms: 1.10x slower                                                           |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| scimark_fft                | 205 ms                                                          | 227 ms: 1.11x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 95.1 ms: 1.11x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 67.6 ms: 1.12x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 70.2 ns: 1.16x slower                                                           |
| many_optionals             | 436 us                                                          | 511 us: 1.17x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 274 us: 1.19x slower                                                            |
| richards                   | 32.7 ms                                                         | 38.8 ms: 1.19x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.69 ms: 1.19x slower                                                           |
| raytrace                   | 201 ms                                                          | 241 ms: 1.20x slower                                                            |
| richards_super             | 36.7 ms                                                         | 43.9 ms: 1.20x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.4 ms: 1.38x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (9): regex_v8, k_core, bench_thread_pool, pathlib, create_gc_cycles, sqlglot_normalize, sympy_str, sympy_sum, pprint_pformat
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241214-3.14.0a2+-0ac40ac/bm-20241214-pythonperf1_win32-x86-python-0ac40acec045c4ce780c-3.14.0a2+-0ac40ac.json: mypy2

- Geometric mean (including insignificant results): 1.042x faster

# HPT report

- Reliability score: 58.52% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown