# Results vs. 3.13.0

- fork: python
- ref: 2f60b8f02fe7cb83dd58
- machine: windows-amd64
- commit hash: 2f60b8f
- commit date: 2025-11-01
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 216 ms: 1.16x faster                                                              |
| docutils       | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                            |
| html5lib       | 47.5 ms                                                         | 36.6 ms: 1.30x faster                                                             |
| sphinx         | 719 ms                                                          | 616 ms: 1.17x faster                                                              |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 149 ms: 2.43x faster                                                              |
| async_tree_memoization     | 297 ms                                                          | 195 ms: 1.52x faster                                                              |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 322 ms: 1.50x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 189 ms: 1.49x faster                                                              |
| async_tree_none            | 245 ms                                                          | 167 ms: 1.47x faster                                                              |
| async_tree_io              | 526 ms                                                          | 366 ms: 1.44x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 157 ms: 1.36x faster                                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 335 ms: 1.36x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 370 ms: 1.34x faster                                                              |
| async_generators           | 270 ms                                                          | 229 ms: 1.18x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.45x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 145 ms: 1.38x faster                                                              |
| float          | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                             |
| nbody          | 80.0 ms                                                         | 65.6 ms: 1.22x faster                                                             |
| Geometric mean | (ref)                                                           | 1.29x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 101 ms                                                          | 79.9 ms: 1.26x faster                                                             |
| regex_effbot   | 1.80 ms                                                         | 1.46 ms: 1.24x faster                                                             |
| regex_v8       | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                             |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                              |
| Geometric mean | (ref)                                                           | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 14.0 us: 1.55x faster                                                             |
| json_dumps           | 7.30 ms                                                         | 5.43 ms: 1.35x faster                                                             |
| tomli_loads          | 1.71 sec                                                        | 1.37 sec: 1.25x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 86.6 ms: 1.24x faster                                                             |
| unpickle_pure_python | 160 us                                                          | 134 us: 1.19x faster                                                              |
| xml_etree_process    | 44.2 ms                                                         | 38.6 ms: 1.15x faster                                                             |
| xml_etree_generate   | 61.4 ms                                                         | 55.3 ms: 1.11x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 210 us: 1.10x faster                                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                             |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                             |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.02x faster                                                             |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                             |
| genshi_text     | 21.5 ms                                                         | 15.5 ms: 1.38x faster                                                             |
| django_template | 29.8 ms                                                         | 23.4 ms: 1.27x faster                                                             |
| mako            | 7.09 ms                                                         | 6.72 ms: 1.05x faster                                                             |
| Geometric mean  | (ref)                                                           | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 494 us: 20.21x faster                                                             |
| coverage                   | 324 ms                                                          | 48.0 ms: 6.75x faster                                                             |
| pathlib                    | 82.9 ms                                                         | 28.3 ms: 2.93x faster                                                             |
| asyncio_websockets         | 363 ms                                                          | 149 ms: 2.43x faster                                                              |
| mdp                        | 1.62 sec                                                        | 812 ms: 2.00x faster                                                              |
| deepcopy                   | 314 us                                                          | 165 us: 1.91x faster                                                              |
| telco                      | 6.96 ms                                                         | 4.17 ms: 1.67x faster                                                             |
| deepcopy_reduce            | 2.92 us                                                         | 1.77 us: 1.65x faster                                                             |
| json_loads                 | 21.6 us                                                         | 14.0 us: 1.55x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 195 ms: 1.52x faster                                                              |
| json                       | 4.27 ms                                                         | 2.83 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 322 ms: 1.50x faster                                                              |
| async_tree_memoization_tg  | 282 ms                                                          | 189 ms: 1.49x faster                                                              |
| async_tree_none            | 245 ms                                                          | 167 ms: 1.47x faster                                                              |
| genshi_xml                 | 50.1 ms                                                         | 34.3 ms: 1.46x faster                                                             |
| async_tree_io              | 526 ms                                                          | 366 ms: 1.44x faster                                                              |
| deepcopy_memo              | 25.4 us                                                         | 17.8 us: 1.43x faster                                                             |
| go                         | 109 ms                                                          | 76.6 ms: 1.42x faster                                                             |
| genshi_text                | 21.5 ms                                                         | 15.5 ms: 1.38x faster                                                             |
| pidigits                   | 201 ms                                                          | 145 ms: 1.38x faster                                                              |
| async_tree_none_tg         | 214 ms                                                          | 157 ms: 1.36x faster                                                              |
| logging_format             | 8.72 us                                                         | 6.39 us: 1.36x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 335 ms: 1.36x faster                                                              |
| json_dumps                 | 7.30 ms                                                         | 5.43 ms: 1.35x faster                                                             |
| typing_runtime_protocols   | 138 us                                                          | 103 us: 1.34x faster                                                              |
| async_tree_io_tg           | 494 ms                                                          | 370 ms: 1.34x faster                                                              |
| logging_simple             | 7.99 us                                                         | 6.01 us: 1.33x faster                                                             |
| pprint_pformat             | 1.33 sec                                                        | 1.00 sec: 1.33x faster                                                            |
| sympy_expand               | 373 ms                                                          | 283 ms: 1.32x faster                                                              |
| pprint_safe_repr           | 648 ms                                                          | 497 ms: 1.30x faster                                                              |
| html5lib                   | 47.5 ms                                                         | 36.6 ms: 1.30x faster                                                             |
| pycparser                  | 872 ms                                                          | 684 ms: 1.27x faster                                                              |
| django_template            | 29.8 ms                                                         | 23.4 ms: 1.27x faster                                                             |
| sympy_str                  | 212 ms                                                          | 167 ms: 1.27x faster                                                              |
| regex_compile              | 101 ms                                                          | 79.9 ms: 1.26x faster                                                             |
| float                      | 54.6 ms                                                         | 43.3 ms: 1.26x faster                                                             |
| tomli_loads                | 1.71 sec                                                        | 1.37 sec: 1.25x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.57 us: 1.25x faster                                                             |
| xml_etree_parse            | 107 ms                                                          | 86.6 ms: 1.24x faster                                                             |
| dulwich_log                | 48.8 ms                                                         | 39.3 ms: 1.24x faster                                                             |
| sympy_sum                  | 106 ms                                                          | 85.3 ms: 1.24x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.46 ms: 1.24x faster                                                             |
| regex_v8                   | 16.8 ms                                                         | 13.7 ms: 1.23x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 12.2 ms: 1.23x faster                                                             |
| chaos                      | 50.2 ms                                                         | 41.1 ms: 1.22x faster                                                             |
| nbody                      | 80.0 ms                                                         | 65.6 ms: 1.22x faster                                                             |
| scimark_fft                | 205 ms                                                          | 169 ms: 1.21x faster                                                              |
| bench_thread_pool          | 1.00 ms                                                         | 833 us: 1.20x faster                                                              |
| unpickle_pure_python       | 160 us                                                          | 134 us: 1.19x faster                                                              |
| crypto_pyaes               | 56.9 ms                                                         | 47.9 ms: 1.19x faster                                                             |
| richards                   | 32.7 ms                                                         | 27.7 ms: 1.18x faster                                                             |
| async_generators           | 270 ms                                                          | 229 ms: 1.18x faster                                                              |
| richards_super             | 36.7 ms                                                         | 31.4 ms: 1.17x faster                                                             |
| sphinx                     | 719 ms                                                          | 616 ms: 1.17x faster                                                              |
| bpe_tokeniser              | 3.46 sec                                                        | 2.98 sec: 1.16x faster                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 41.0 ms: 1.16x faster                                                             |
| 2to3                       | 250 ms                                                          | 216 ms: 1.16x faster                                                              |
| pylint                     | 227 ms                                                          | 196 ms: 1.16x faster                                                              |
| coroutines                 | 16.2 ms                                                         | 14.1 ms: 1.15x faster                                                             |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.47 ms: 1.15x faster                                                             |
| xml_etree_process          | 44.2 ms                                                         | 38.6 ms: 1.15x faster                                                             |
| nqueens                    | 72.1 ms                                                         | 63.3 ms: 1.14x faster                                                             |
| generators                 | 21.8 ms                                                         | 19.2 ms: 1.14x faster                                                             |
| pyflate                    | 320 ms                                                          | 283 ms: 1.13x faster                                                              |
| raytrace                   | 201 ms                                                          | 178 ms: 1.13x faster                                                              |
| scimark_sor                | 85.9 ms                                                         | 76.6 ms: 1.12x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.3 ms: 1.12x faster                                                             |
| docutils                   | 1.78 sec                                                        | 1.59 sec: 1.12x faster                                                            |
| fannkuch                   | 299 ms                                                          | 267 ms: 1.12x faster                                                              |
| comprehensions             | 12.5 us                                                         | 11.2 us: 1.11x faster                                                             |
| xml_etree_generate         | 61.4 ms                                                         | 55.3 ms: 1.11x faster                                                             |
| pickle_pure_python         | 231 us                                                          | 210 us: 1.10x faster                                                              |
| logging_silent             | 60.3 ns                                                         | 55.2 ns: 1.09x faster                                                             |
| hexiom                     | 4.44 ms                                                         | 4.12 ms: 1.08x faster                                                             |
| scimark_lu                 | 60.2 ms                                                         | 56.2 ms: 1.07x faster                                                             |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.6 ms: 1.07x faster                                                             |
| spectral_norm              | 69.4 ms                                                         | 65.1 ms: 1.07x faster                                                             |
| mako                       | 7.09 ms                                                         | 6.72 ms: 1.05x faster                                                             |
| deltablue                  | 2.33 ms                                                         | 2.23 ms: 1.05x faster                                                             |
| meteor_contest             | 74.6 ms                                                         | 72.0 ms: 1.04x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 88.7 ms: 1.02x faster                                                             |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.02x faster                                                             |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                              |
| k_core                     | 1.38 sec                                                        | 1.56 sec: 1.13x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 2.05 ms: 1.17x slower                                                             |
| shortest_path              | 290 ms                                                          | 352 ms: 1.21x slower                                                              |
| create_gc_cycles           | 1.06 ms                                                         | 1.28 ms: 1.21x slower                                                             |
| connected_components       | 267 ms                                                          | 327 ms: 1.23x slower                                                              |
| many_optionals             | 436 us                                                          | 548 us: 1.26x slower                                                              |
| subparsers                 | 14.8 ms                                                         | 30.7 ms: 2.08x slower                                                             |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                      |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20251101-3.15.0a1+-2f60b8f/bm-20251101-pythonperf1_win32-amd64-python-2f60b8f02fe7cb83dd58-3.15.0a1+-2f60b8f.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.288x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown