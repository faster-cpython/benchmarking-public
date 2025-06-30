# Results vs. 3.13.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.279x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 220 ms: 1.14x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| sphinx         | 719 ms                                                          | 633 ms: 1.13x faster                                                             |
| Geometric mean | (ref)                                                           | 1.16x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 208 ms: 1.43x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| async_tree_io              | 526 ms                                                          | 397 ms: 1.32x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 170 ms: 1.26x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.38x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| nbody          | 80.0 ms                                                         | 63.0 ms: 1.27x faster                                                            |
| float          | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.4 ms: 1.27x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                            |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.38 sec: 1.25x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 89.2 ms: 1.20x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 135 us: 1.19x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 6.19 ms: 1.18x faster                                                            |
| xml_etree_process    | 44.2 ms                                                         | 39.1 ms: 1.13x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 208 us: 1.11x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 56.1 ms: 1.09x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.3 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.17x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| django_template | 29.8 ms                                                         | 24.3 ms: 1.23x faster                                                            |
| mako            | 7.09 ms                                                         | 6.55 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 494 us: 20.19x faster                                                            |
| coverage                   | 324 ms                                                          | 47.6 ms: 6.80x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 31.7 ms: 2.62x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 158 ms: 2.30x faster                                                             |
| mdp                        | 1.62 sec                                                        | 801 ms: 2.03x faster                                                             |
| deepcopy                   | 314 us                                                          | 168 us: 1.86x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.84 us: 1.58x faster                                                            |
| telco                      | 6.96 ms                                                         | 4.60 ms: 1.51x faster                                                            |
| json_loads                 | 21.6 us                                                         | 14.3 us: 1.51x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.47x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 17.6 us: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| go                         | 109 ms                                                          | 75.5 ms: 1.44x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 208 ms: 1.43x faster                                                             |
| json                       | 4.27 ms                                                         | 3.03 ms: 1.41x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 101 us: 1.36x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.49 us: 1.34x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 340 ms: 1.34x faster                                                             |
| logging_simple             | 7.99 us                                                         | 5.99 us: 1.33x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| async_tree_io              | 526 ms                                                          | 397 ms: 1.32x faster                                                             |
| pprint_safe_repr           | 648 ms                                                          | 490 ms: 1.32x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.01 sec: 1.32x faster                                                           |
| sympy_expand               | 373 ms                                                          | 287 ms: 1.30x faster                                                             |
| regex_compile              | 101 ms                                                          | 79.4 ms: 1.27x faster                                                            |
| nbody                      | 80.0 ms                                                         | 63.0 ms: 1.27x faster                                                            |
| float                      | 54.6 ms                                                         | 43.1 ms: 1.27x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 170 ms: 1.26x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.3 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 393 ms: 1.26x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 38.0 ms: 1.25x faster                                                            |
| sympy_str                  | 212 ms                                                          | 170 ms: 1.25x faster                                                             |
| pycparser                  | 872 ms                                                          | 699 ms: 1.25x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.38 sec: 1.25x faster                                                           |
| chaos                      | 50.2 ms                                                         | 40.6 ms: 1.24x faster                                                            |
| django_template            | 29.8 ms                                                         | 24.3 ms: 1.23x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.59 us: 1.23x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 87.3 ms: 1.21x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.0 ms: 1.21x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.4 ms: 1.21x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 89.2 ms: 1.20x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.50 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.9 ms: 1.19x faster                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 47.8 ms: 1.19x faster                                                            |
| nqueens                    | 72.1 ms                                                         | 60.5 ms: 1.19x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 40.1 ms: 1.19x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 843 us: 1.19x faster                                                             |
| unpickle_pure_python       | 160 us                                                          | 135 us: 1.19x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.92 sec: 1.19x faster                                                           |
| json_dumps                 | 7.30 ms                                                         | 6.19 ms: 1.18x faster                                                            |
| fannkuch                   | 299 ms                                                          | 255 ms: 1.17x faster                                                             |
| async_generators           | 270 ms                                                          | 230 ms: 1.17x faster                                                             |
| scimark_fft                | 205 ms                                                          | 176 ms: 1.16x faster                                                             |
| scimark_sor                | 85.9 ms                                                         | 74.0 ms: 1.16x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.9 us: 1.15x faster                                                            |
| pylint                     | 227 ms                                                          | 198 ms: 1.15x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.49 ms: 1.14x faster                                                            |
| 2to3                       | 250 ms                                                          | 220 ms: 1.14x faster                                                             |
| sphinx                     | 719 ms                                                          | 633 ms: 1.13x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 39.1 ms: 1.13x faster                                                            |
| pyflate                    | 320 ms                                                          | 285 ms: 1.12x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.4 ms: 1.12x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.4 ms: 1.12x faster                                                            |
| raytrace                   | 201 ms                                                          | 180 ms: 1.12x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 208 us: 1.11x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.60 sec: 1.11x faster                                                           |
| python_startup             | 28.3 ms                                                         | 25.7 ms: 1.10x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.03 ms: 1.10x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 56.1 ms: 1.09x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.15 ms: 1.09x faster                                                            |
| mako                       | 7.09 ms                                                         | 6.55 ms: 1.08x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 64.7 ms: 1.07x faster                                                            |
| scimark_lu                 | 60.2 ms                                                         | 56.6 ms: 1.06x faster                                                            |
| meteor_contest             | 74.6 ms                                                         | 71.8 ms: 1.04x faster                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 95.7 ms: 1.06x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.3 ms: 1.06x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 16.9 ms: 1.15x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                            |
| shortest_path              | 290 ms                                                          | 364 ms: 1.26x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.33 ms: 1.26x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.73 sec: 1.26x slower                                                           |
| connected_components       | 267 ms                                                          | 337 ms: 1.26x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                     |

Benchmark hidden because not significant (2): python_startup_no_site, many_optionals
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250630-3.15.0a0-75f4059/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.279x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown