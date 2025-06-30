# Results vs. 3.13.0

- fork: python
- ref: 75f40595e555e7d016cf
- machine: windows-amd64
- commit hash: 75f4059
- commit date: 2025-06-30
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 1.67 sec: 1.06x faster                                                           |
| html5lib       | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| sphinx         | 719 ms                                                          | 646 ms: 1.11x faster                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.45x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 207 ms: 1.43x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| async_tree_io              | 526 ms                                                          | 397 ms: 1.33x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 346 ms: 1.32x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 253 ms: 1.07x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 56.8 ms: 1.41x faster                                                            |
| pidigits       | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| float          | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                            |
| Geometric mean | (ref)                                                           | 1.33x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 78.1 ms: 1.29x faster                                                            |
| regex_v8       | 16.8 ms                                                         | 14.2 ms: 1.18x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| regex_dna      | 114 ms                                                          | 122 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                           | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| json_loads           | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 109 us: 1.47x faster                                                             |
| xml_etree_process    | 44.2 ms                                                         | 35.5 ms: 1.25x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 87.6 ms: 1.23x faster                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 51.8 ms: 1.19x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 6.25 ms: 1.17x faster                                                            |
| pickle_pure_python   | 231 us                                                          | 204 us: 1.13x faster                                                             |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.0 ms: 1.02x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.25x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| mako            | 7.09 ms                                                         | 5.47 ms: 1.29x faster                                                            |
| django_template | 29.8 ms                                                         | 23.9 ms: 1.25x faster                                                            |
| Geometric mean  | (ref)                                                           | 1.35x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 488 us: 20.46x faster                                                            |
| coverage                   | 324 ms                                                          | 50.4 ms: 6.43x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 31.9 ms: 2.60x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 160 ms: 2.26x faster                                                             |
| mdp                        | 1.62 sec                                                        | 824 ms: 1.97x faster                                                             |
| deepcopy                   | 314 us                                                          | 172 us: 1.83x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.25 ms: 1.64x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 1.87 us: 1.56x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.14 sec: 1.50x faster                                                           |
| json_loads                 | 21.6 us                                                         | 14.6 us: 1.48x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 109 us: 1.47x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 333 ms: 1.45x faster                                                             |
| genshi_xml                 | 50.1 ms                                                         | 34.7 ms: 1.45x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 207 ms: 1.43x faster                                                             |
| go                         | 109 ms                                                          | 77.0 ms: 1.41x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 18.1 us: 1.41x faster                                                            |
| nbody                      | 80.0 ms                                                         | 56.8 ms: 1.41x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 15.3 ms: 1.40x faster                                                            |
| json                       | 4.27 ms                                                         | 3.05 ms: 1.40x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 465 ms: 1.39x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 959 ms: 1.39x faster                                                             |
| pidigits                   | 201 ms                                                          | 146 ms: 1.37x faster                                                             |
| scimark_fft                | 205 ms                                                          | 153 ms: 1.34x faster                                                             |
| bpe_tokeniser              | 3.46 sec                                                        | 2.59 sec: 1.33x faster                                                           |
| typing_runtime_protocols   | 138 us                                                          | 103 us: 1.33x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 212 ms: 1.33x faster                                                             |
| fannkuch                   | 299 ms                                                          | 225 ms: 1.33x faster                                                             |
| async_tree_io              | 526 ms                                                          | 397 ms: 1.33x faster                                                             |
| logging_format             | 8.72 us                                                         | 6.59 us: 1.32x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 346 ms: 1.32x faster                                                             |
| logging_simple             | 7.99 us                                                         | 6.13 us: 1.30x faster                                                            |
| mako                       | 7.09 ms                                                         | 5.47 ms: 1.29x faster                                                            |
| regex_compile              | 101 ms                                                          | 78.1 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 388 ms: 1.28x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 168 ms: 1.28x faster                                                             |
| sympy_expand               | 373 ms                                                          | 298 ms: 1.25x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.56 us: 1.25x faster                                                            |
| django_template            | 29.8 ms                                                         | 23.9 ms: 1.25x faster                                                            |
| xml_etree_process          | 44.2 ms                                                         | 35.5 ms: 1.25x faster                                                            |
| pycparser                  | 872 ms                                                          | 703 ms: 1.24x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.29 ms: 1.24x faster                                                            |
| pyflate                    | 320 ms                                                          | 259 ms: 1.24x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 46.2 ms: 1.23x faster                                                            |
| sympy_str                  | 212 ms                                                          | 172 ms: 1.23x faster                                                             |
| float                      | 54.6 ms                                                         | 44.5 ms: 1.23x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 38.7 ms: 1.23x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 87.6 ms: 1.23x faster                                                            |
| richards                   | 32.7 ms                                                         | 27.1 ms: 1.21x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.4 ms: 1.21x faster                                                            |
| chaos                      | 50.2 ms                                                         | 41.7 ms: 1.21x faster                                                            |
| richards_super             | 36.7 ms                                                         | 30.6 ms: 1.20x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 88.3 ms: 1.20x faster                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 51.8 ms: 1.19x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.2 ms: 1.18x faster                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 850 us: 1.18x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 61.7 ms: 1.17x faster                                                            |
| sympy_integrate            | 15.0 ms                                                         | 12.8 ms: 1.17x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 6.25 ms: 1.17x faster                                                            |
| comprehensions             | 12.5 us                                                         | 10.7 us: 1.16x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.1 ms: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                            |
| raytrace                   | 201 ms                                                          | 177 ms: 1.14x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 204 us: 1.13x faster                                                             |
| 2to3                       | 250 ms                                                          | 221 ms: 1.13x faster                                                             |
| pylint                     | 227 ms                                                          | 201 ms: 1.13x faster                                                             |
| sphinx                     | 719 ms                                                          | 646 ms: 1.11x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.6 ms: 1.10x faster                                                            |
| logging_silent             | 60.3 ns                                                         | 54.9 ns: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| generators                 | 21.8 ms                                                         | 19.9 ms: 1.09x faster                                                            |
| scimark_sor                | 85.9 ms                                                         | 80.2 ms: 1.07x faster                                                            |
| hexiom                     | 4.44 ms                                                         | 4.16 ms: 1.07x faster                                                            |
| async_generators           | 270 ms                                                          | 253 ms: 1.07x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.67 sec: 1.06x faster                                                           |
| meteor_contest             | 74.6 ms                                                         | 70.7 ms: 1.06x faster                                                            |
| deltablue                  | 2.33 ms                                                         | 2.23 ms: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.2 ms: 1.02x faster                                                            |
| spectral_norm              | 69.4 ms                                                         | 68.7 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.0 ms: 1.02x slower                                                            |
| many_optionals             | 436 us                                                          | 447 us: 1.02x slower                                                             |
| scimark_lu                 | 60.2 ms                                                         | 62.8 ms: 1.04x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 95.3 ms: 1.05x slower                                                            |
| regex_dna                  | 114 ms                                                          | 122 ms: 1.07x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 16.9 ms: 1.15x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.64 sec: 1.19x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 2.14 ms: 1.22x slower                                                            |
| connected_components       | 267 ms                                                          | 327 ms: 1.23x slower                                                             |
| shortest_path              | 290 ms                                                          | 360 ms: 1.24x slower                                                             |
| create_gc_cycles           | 1.06 ms                                                         | 1.33 ms: 1.26x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                     |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250630-3.15.0a0-75f4059-JIT/bm-20250630-pythonperf1_win32-amd64-python-75f40595e555e7d016cf-3.15.0a0-75f4059.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown