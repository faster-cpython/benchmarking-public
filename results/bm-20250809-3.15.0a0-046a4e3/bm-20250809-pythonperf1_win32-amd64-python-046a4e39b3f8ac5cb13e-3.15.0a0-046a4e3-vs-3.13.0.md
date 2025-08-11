# Results vs. 3.13.0

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: windows-amd64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.259x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| html5lib       | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| sphinx         | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 177 ms: 1.39x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 337 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 390 ms: 1.27x faster                                                             |
| async_generators           | 270 ms                                                          | 224 ms: 1.21x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.39x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| float          | 54.6 ms                                                         | 44.0 ms: 1.24x faster                                                            |
| nbody          | 80.0 ms                                                         | 65.8 ms: 1.22x faster                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| regex_compile  | 101 ms                                                          | 81.3 ms: 1.24x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.48 ms: 1.21x faster                                                            |
| regex_dna      | 114 ms                                                          | 119 ms: 1.04x slower                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.1 us: 1.54x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 88.9 ms: 1.21x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                           |
| unpickle_pure_python | 160 us                                                          | 135 us: 1.19x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 40.2 ms: 1.10x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 214 us: 1.08x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 57.9 ms: 1.06x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.4 ms: 1.03x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| django_template | 29.8 ms                                                         | 24.3 ms: 1.22x faster                                                            |
| mako            | 7.09 ms                                                         | 6.66 ms: 1.06x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.27x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 502 us: 19.86x faster                                                            |
| coverage                   | 324 ms                                                          | 49.6 ms: 6.54x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 31.9 ms: 2.60x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 157 ms: 2.31x faster                                                             |
| mdp                        | 1.62 sec                                                        | 794 ms: 2.05x faster                                                             |
| deepcopy                   | 314 us                                                          | 168 us: 1.87x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.80 us: 1.62x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.1 us: 1.54x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.72 ms: 1.48x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 204 ms: 1.45x faster                                                             |
| json                       | 4.27 ms                                                         | 2.97 ms: 1.44x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 35.0 ms: 1.43x faster                                                            |
| go                         | 109 ms                                                          | 76.7 ms: 1.42x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.2 us: 1.40x faster                                                            |
| async_tree_none            | 245 ms                                                          | 177 ms: 1.39x faster                                                             |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.7 ms: 1.37x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.36 ms: 1.36x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 337 ms: 1.35x faster                                                             |
| async_tree_io              | 526 ms                                                          | 389 ms: 1.35x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 210 ms: 1.35x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.52 us: 1.34x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.03 us: 1.33x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 104 us: 1.32x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 497 ms: 1.30x faster                                                             |
| sympy_expand               | 373 ms                                                          | 287 ms: 1.30x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.02 sec: 1.30x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 390 ms: 1.27x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 37.6 ms: 1.26x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| regex_compile              | 101 ms                                                          | 81.3 ms: 1.24x faster                                                            |
| float                      | 54.6 ms                                                         | 44.0 ms: 1.24x faster                                                            |
| pycparser                  | 872 ms                                                          | 702 ms: 1.24x faster                                                             |
| chaos                      | 50.2 ms                                                         | 40.6 ms: 1.24x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 39.4 ms: 1.24x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.3 ms: 1.22x faster                                                            |
| nbody                      | 80.0 ms                                                         | 65.8 ms: 1.22x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 46.9 ms: 1.21x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.48 ms: 1.21x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.61 us: 1.21x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.3 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 88.9 ms: 1.21x faster                                                            |
| async_generators           | 270 ms                                                          | 224 ms: 1.21x faster                                                             |
| richards                   | 32.7 ms                                                         | 27.2 ms: 1.20x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.44 sec: 1.19x faster                                                           |
| sympy_integrate            | 15.0 ms                                                         | 12.6 ms: 1.19x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 135 us: 1.19x faster                                                             |
| bench_thread_pool          | 1.00 ms                                                         | 848 us: 1.18x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.93 sec: 1.18x faster                                                           |
| richards_super             | 36.7 ms                                                         | 31.1 ms: 1.18x faster                                                            |
| pylint                     | 227 ms                                                          | 197 ms: 1.15x faster                                                             |
| 2to3                       | 250 ms                                                          | 219 ms: 1.14x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 63.1 ms: 1.14x faster                                                            |
| comprehensions             | 12.5 us                                                         | 11.0 us: 1.14x faster                                                            |
| fannkuch                   | 299 ms                                                          | 262 ms: 1.14x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.1 ms: 1.14x faster                                                            |
| sphinx                     | 719 ms                                                          | 636 ms: 1.13x faster                                                             |
| scimark_monte_carlo        | 47.7 ms                                                         | 42.4 ms: 1.12x faster                                                            |
| docutils                   | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                           |
| coroutines                 | 16.2 ms                                                         | 14.7 ms: 1.10x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 40.2 ms: 1.10x faster                                                            |
| scimark_fft                | 205 ms                                                          | 187 ms: 1.10x faster                                                             |
| raytrace                   | 201 ms                                                          | 184 ms: 1.09x faster                                                             |
| pyflate                    | 320 ms                                                          | 293 ms: 1.09x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 78.9 ms: 1.09x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 63.9 ms: 1.09x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.11 ms: 1.08x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 214 us: 1.08x faster                                                             |
| python_startup             | 28.3 ms                                                         | 26.6 ms: 1.06x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.66 ms: 1.06x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 57.9 ms: 1.06x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.21 ms: 1.05x faster                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.69 ms: 1.05x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 58.0 ns: 1.04x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 72.6 ms: 1.03x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 59.3 ms: 1.02x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.4 ms: 1.03x slower                                                            |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.04x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 94.5 ms: 1.04x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.15 ms: 1.23x slower                                                            |
| connected_components       | 267 ms                                                          | 329 ms: 1.23x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.31 ms: 1.23x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.70 sec: 1.24x slower                                                           |
| many_optionals             | 436 us                                                          | 546 us: 1.25x slower                                                             |
| shortest_path              | 290 ms                                                          | 379 ms: 1.31x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 29.3 ms: 1.98x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250809-3.15.0a0-046a4e3/bm-20250809-pythonperf1_win32-amd64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.259x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown