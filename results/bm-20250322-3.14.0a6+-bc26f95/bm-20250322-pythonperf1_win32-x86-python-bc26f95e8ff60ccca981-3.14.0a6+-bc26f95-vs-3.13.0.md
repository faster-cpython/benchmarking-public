# Results vs. 3.13.0

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: windows-x86
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.001x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 268 ms: 1.07x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.91 sec: 1.07x slower                                                          |
| html5lib       | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 771 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 199 ms: 1.82x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 238 ms: 1.18x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 255 ms: 1.16x faster                                                            |
| async_tree_io              | 526 ms                                                          | 464 ms: 1.13x faster                                                            |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 447 ms: 1.11x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 195 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 466 ms: 1.02x slower                                                            |
| async_generators           | 270 ms                                                          | 317 ms: 1.17x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 54.1 ms: 1.01x faster                                                           |
| nbody          | 80.0 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.1 ms: 1.11x faster                                                           |
| regex_dna      | 114 ms                                                          | 119 ms: 1.04x slower                                                            |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 68.0 ms: 1.09x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.33 ms: 1.14x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 187 us: 1.17x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 272 us: 1.18x slower                                                            |
| xml_etree_generate   | 61.4 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 53.2 ms: 1.20x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.9 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 53.9 ms: 1.07x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                           |
| mako            | 7.09 ms                                                         | 8.37 ms: 1.18x slower                                                           |
| django_template | 29.8 ms                                                         | 35.6 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 786 us: 12.70x faster                                                           |
| coverage                   | 324 ms                                                          | 53.2 ms: 6.08x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 37.3 ms: 2.22x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 199 ms: 1.82x faster                                                            |
| deepcopy                   | 314 us                                                          | 259 us: 1.21x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 238 ms: 1.18x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.6 us: 1.18x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 255 ms: 1.16x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.14x faster                                                           |
| async_tree_io              | 526 ms                                                          | 464 ms: 1.13x faster                                                            |
| async_tree_none            | 245 ms                                                          | 219 ms: 1.12x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.1 ms: 1.11x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 447 ms: 1.11x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 195 ms: 1.10x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.75 us: 1.06x faster                                                           |
| telco                      | 6.96 ms                                                         | 6.82 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                           |
| float                      | 54.6 ms                                                         | 54.1 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 486 ms: 1.01x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 16.5 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 466 ms: 1.02x slower                                                            |
| python_startup             | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.36 sec: 1.03x slower                                                          |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 49.1 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 670 ms: 1.03x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.04x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.05x slower                                                          |
| bench_mp_pool              | 90.6 ms                                                         | 95.7 ms: 1.06x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.68 sec: 1.06x slower                                                          |
| connected_components       | 267 ms                                                          | 283 ms: 1.06x slower                                                            |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 113 ms: 1.07x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 74.3 ms: 1.07x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 52.2 ms: 1.07x slower                                                           |
| 2to3                       | 250 ms                                                          | 268 ms: 1.07x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.91 sec: 1.07x slower                                                          |
| sphinx                     | 719 ms                                                          | 771 ms: 1.07x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 53.9 ms: 1.07x slower                                                           |
| nbody                      | 80.0 ms                                                         | 86.0 ms: 1.08x slower                                                           |
| sympy_str                  | 212 ms                                                          | 228 ms: 1.08x slower                                                            |
| json                       | 4.27 ms                                                         | 4.63 ms: 1.08x slower                                                           |
| shortest_path              | 290 ms                                                          | 314 ms: 1.08x slower                                                            |
| pycparser                  | 872 ms                                                          | 947 ms: 1.09x slower                                                            |
| sympy_expand               | 373 ms                                                          | 406 ms: 1.09x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 68.0 ms: 1.09x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 23.5 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 153 us: 1.11x slower                                                            |
| logging_simple             | 7.99 us                                                         | 8.88 us: 1.11x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 67.2 ns: 1.11x slower                                                           |
| pyflate                    | 320 ms                                                          | 358 ms: 1.12x slower                                                            |
| logging_format             | 8.72 us                                                         | 9.75 us: 1.12x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 67.7 ms: 1.12x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 96.7 ms: 1.13x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 84.9 ms: 1.14x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.3 ms: 1.14x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.33 ms: 1.14x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.24 ms: 1.14x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.08 ms: 1.14x slower                                                           |
| scimark_fft                | 205 ms                                                          | 235 ms: 1.15x slower                                                            |
| generators                 | 21.8 ms                                                         | 25.2 ms: 1.16x slower                                                           |
| comprehensions             | 12.5 us                                                         | 14.5 us: 1.16x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.88 sec: 1.16x slower                                                          |
| fannkuch                   | 299 ms                                                          | 347 ms: 1.16x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 22.9 ms: 1.17x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 187 us: 1.17x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.73 ms: 1.17x slower                                                           |
| async_generators           | 270 ms                                                          | 317 ms: 1.17x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 272 us: 1.18x slower                                                            |
| richards                   | 32.7 ms                                                         | 38.5 ms: 1.18x slower                                                           |
| richards_super             | 36.7 ms                                                         | 43.3 ms: 1.18x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.37 ms: 1.18x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| chaos                      | 50.2 ms                                                         | 59.7 ms: 1.19x slower                                                           |
| django_template            | 29.8 ms                                                         | 35.6 ms: 1.20x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 53.2 ms: 1.20x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 68.8 ms: 1.21x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 87.2 ms: 1.21x slower                                                           |
| raytrace                   | 201 ms                                                          | 253 ms: 1.25x slower                                                            |
| many_optionals             | 436 us                                                          | 562 us: 1.29x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.30 ms: 1.30x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 22.2 ms: 1.50x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (5): pidigits, json_loads, create_gc_cycles, pylint, go
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-pythonperf1_win32-x86-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown