# Results vs. 3.13.0

- fork: python
- ref: 6fcac09401e336b25833
- machine: windows-amd64
- commit hash: 6fcac09
- commit date: 2025-08-23
- overall geometric mean: 1.135x faster
- HPT reliability: 99.67%
- HPT 99th percentile: 1.01x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| docutils       | 1.78 sec                                                        | 2.77 sec: 1.56x slower                                                           |
| html5lib       | 47.5 ms                                                         | 41.1 ms: 1.16x faster                                                            |
| sphinx         | 719 ms                                                          | 662 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 137 ms: 2.64x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 324 ms: 1.52x faster                                                             |
| async_tree_memoization_tg  | 282 ms                                                          | 187 ms: 1.51x faster                                                             |
| async_tree_io              | 526 ms                                                          | 349 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 306 ms: 1.49x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 144 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| Geometric mean             | (ref)                                                           | 1.47x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| float          | 54.6 ms                                                         | 45.5 ms: 1.20x faster                                                            |
| nbody          | 80.0 ms                                                         | 81.3 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 12.8 ms: 1.32x faster                                                            |
| regex_effbot   | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| regex_compile  | 101 ms                                                          | 93.8 ms: 1.08x faster                                                            |
| regex_dna      | 114 ms                                                          | 111 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                           | 1.15x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 15.7 us: 1.37x faster                                                            |
| json_dumps           | 7.30 ms                                                         | 5.90 ms: 1.24x faster                                                            |
| xml_etree_parse      | 107 ms                                                          | 90.5 ms: 1.19x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 58.3 ms: 1.07x faster                                                            |
| unpickle_pure_python | 160 us                                                          | 156 us: 1.03x faster                                                             |
| pickle_pure_python   | 231 us                                                          | 233 us: 1.01x slower                                                             |
| tomli_loads          | 1.71 sec                                                        | 2.60 sec: 1.52x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| python_startup_no_site | 19.7 ms                                                         | 19.0 ms: 1.03x faster                                                            |
| Geometric mean         | (ref)                                                           | 1.07x faster                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 38.7 ms: 1.29x faster                                                            |
| genshi_text     | 21.5 ms                                                         | 18.9 ms: 1.14x faster                                                            |
| django_template | 29.8 ms                                                         | 27.1 ms: 1.10x faster                                                            |
| mako            | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 572 us: 17.46x faster                                                            |
| coverage                   | 324 ms                                                          | 66.8 ms: 4.85x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 30.2 ms: 2.75x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 137 ms: 2.64x faster                                                             |
| deepcopy                   | 314 us                                                          | 200 us: 1.57x faster                                                             |
| async_tree_io_tg           | 494 ms                                                          | 324 ms: 1.52x faster                                                             |
| mdp                        | 1.62 sec                                                        | 1.07 sec: 1.51x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 187 ms: 1.51x faster                                                             |
| async_tree_io              | 526 ms                                                          | 349 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 306 ms: 1.49x faster                                                             |
| gc_traversal               | 1.75 ms                                                         | 1.17 ms: 1.49x faster                                                            |
| pidigits                   | 201 ms                                                          | 135 ms: 1.49x faster                                                             |
| async_tree_none_tg         | 214 ms                                                          | 144 ms: 1.48x faster                                                             |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 328 ms: 1.48x faster                                                             |
| sqlite_synth               | 1.95 us                                                         | 1.33 us: 1.47x faster                                                            |
| async_tree_none            | 245 ms                                                          | 170 ms: 1.44x faster                                                             |
| telco                      | 6.96 ms                                                         | 4.84 ms: 1.44x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 209 ms: 1.42x faster                                                             |
| json                       | 4.27 ms                                                         | 3.07 ms: 1.39x faster                                                            |
| json_loads                 | 21.6 us                                                         | 15.7 us: 1.37x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.12 us: 1.37x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 12.8 ms: 1.32x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 38.7 ms: 1.29x faster                                                            |
| json_dumps                 | 7.30 ms                                                         | 5.90 ms: 1.24x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.7 us: 1.23x faster                                                            |
| logging_format             | 8.72 us                                                         | 7.16 us: 1.22x faster                                                            |
| pycparser                  | 872 ms                                                          | 721 ms: 1.21x faster                                                             |
| regex_effbot               | 1.80 ms                                                         | 1.49 ms: 1.21x faster                                                            |
| logging_simple             | 7.99 us                                                         | 6.63 us: 1.20x faster                                                            |
| float                      | 54.6 ms                                                         | 45.5 ms: 1.20x faster                                                            |
| dulwich_log                | 48.8 ms                                                         | 40.8 ms: 1.20x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 90.5 ms: 1.19x faster                                                            |
| go                         | 109 ms                                                          | 92.1 ms: 1.18x faster                                                            |
| sympy_expand               | 373 ms                                                          | 318 ms: 1.17x faster                                                             |
| bench_mp_pool              | 90.6 ms                                                         | 77.8 ms: 1.16x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 558 ms: 1.16x faster                                                             |
| html5lib                   | 47.5 ms                                                         | 41.1 ms: 1.16x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 18.9 ms: 1.14x faster                                                            |
| sympy_str                  | 212 ms                                                          | 187 ms: 1.13x faster                                                             |
| pylint                     | 227 ms                                                          | 201 ms: 1.13x faster                                                             |
| 2to3                       | 250 ms                                                          | 222 ms: 1.13x faster                                                             |
| python_startup             | 28.3 ms                                                         | 25.5 ms: 1.11x faster                                                            |
| django_template            | 29.8 ms                                                         | 27.1 ms: 1.10x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 14.8 ms: 1.10x faster                                                            |
| sympy_sum                  | 106 ms                                                          | 96.2 ms: 1.10x faster                                                            |
| sphinx                     | 719 ms                                                          | 662 ms: 1.09x faster                                                             |
| chaos                      | 50.2 ms                                                         | 46.3 ms: 1.08x faster                                                            |
| regex_compile              | 101 ms                                                          | 93.8 ms: 1.08x faster                                                            |
| typing_runtime_protocols   | 138 us                                                          | 128 us: 1.08x faster                                                             |
| sympy_integrate            | 15.0 ms                                                         | 14.0 ms: 1.07x faster                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 58.3 ms: 1.07x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 994 us: 1.07x faster                                                             |
| async_generators           | 270 ms                                                          | 254 ms: 1.06x faster                                                             |
| comprehensions             | 12.5 us                                                         | 11.9 us: 1.05x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.0 ms: 1.03x faster                                                            |
| unpickle_pure_python       | 160 us                                                          | 156 us: 1.03x faster                                                             |
| regex_dna                  | 114 ms                                                          | 111 ms: 1.02x faster                                                             |
| pyflate                    | 320 ms                                                          | 314 ms: 1.02x faster                                                             |
| crypto_pyaes               | 56.9 ms                                                         | 56.2 ms: 1.01x faster                                                            |
| pickle_pure_python         | 231 us                                                          | 233 us: 1.01x slower                                                             |
| nqueens                    | 72.1 ms                                                         | 73.1 ms: 1.01x slower                                                            |
| nbody                      | 80.0 ms                                                         | 81.3 ms: 1.02x slower                                                            |
| fannkuch                   | 299 ms                                                          | 304 ms: 1.02x slower                                                             |
| scimark_sor                | 85.9 ms                                                         | 88.0 ms: 1.02x slower                                                            |
| scimark_fft                | 205 ms                                                          | 210 ms: 1.03x slower                                                             |
| logging_silent             | 60.3 ns                                                         | 61.9 ns: 1.03x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 4.59 ms: 1.03x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 2.43 ms: 1.04x slower                                                            |
| raytrace                   | 201 ms                                                          | 211 ms: 1.05x slower                                                             |
| spectral_norm              | 69.4 ms                                                         | 73.5 ms: 1.06x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 51.6 ms: 1.08x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 65.2 ms: 1.08x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.09 ms: 1.09x slower                                                            |
| richards                   | 32.7 ms                                                         | 35.9 ms: 1.10x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.10 ms: 1.10x slower                                                            |
| richards_super             | 36.7 ms                                                         | 41.1 ms: 1.12x slower                                                            |
| generators                 | 21.8 ms                                                         | 24.9 ms: 1.14x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 85.7 ms: 1.15x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.61 sec: 1.21x slower                                                           |
| many_optionals             | 436 us                                                          | 617 us: 1.41x slower                                                             |
| mako                       | 7.09 ms                                                         | 10.1 ms: 1.42x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 2.60 sec: 1.52x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 5.37 sec: 1.55x slower                                                           |
| docutils                   | 1.78 sec                                                        | 2.77 sec: 1.56x slower                                                           |
| k_core                     | 1.38 sec                                                        | 2.60 sec: 1.89x slower                                                           |
| shortest_path              | 290 ms                                                          | 629 ms: 2.17x slower                                                             |
| connected_components       | 267 ms                                                          | 580 ms: 2.17x slower                                                             |
| subparsers                 | 14.8 ms                                                         | 34.4 ms: 2.33x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                     |

Benchmark hidden because not significant (2): xml_etree_generate, xml_etree_process
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250823-3.15.0a0-6fcac09-NOGIL/bm-20250823-pythonperf1_win32-amd64-python-6fcac09401e336b25833-3.15.0a0-6fcac09.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.135x faster

# HPT report

- Reliability score: 99.67% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: unknown