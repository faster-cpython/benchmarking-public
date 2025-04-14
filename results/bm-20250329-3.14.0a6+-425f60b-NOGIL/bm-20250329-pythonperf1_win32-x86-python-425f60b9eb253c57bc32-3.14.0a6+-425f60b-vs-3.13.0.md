# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.107x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.11x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 278 ms: 1.11x slower                                                            |
| docutils       | 1.78 sec                                                        | 3.16 sec: 1.77x slower                                                          |
| html5lib       | 47.5 ms                                                         | 52.2 ms: 1.10x slower                                                           |
| sphinx         | 719 ms                                                          | 970 ms: 1.35x slower                                                            |
| Geometric mean | (ref)                                                           | 1.31x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.19x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 236 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 416 ms: 1.19x faster                                                            |
| async_tree_io              | 526 ms                                                          | 445 ms: 1.18x faster                                                            |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 265 ms: 1.12x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 428 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 459 ms: 1.05x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                           |
| async_generators           | 270 ms                                                          | 313 ms: 1.16x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.15x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 187 ms: 1.07x faster                                                            |
| float          | 54.6 ms                                                         | 62.5 ms: 1.15x slower                                                           |
| nbody          | 80.0 ms                                                         | 133 ms: 1.66x slower                                                            |
| Geometric mean | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_dna      | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| regex_compile  | 101 ms                                                          | 127 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| json_loads           | 21.6 us                                                         | 25.6 us: 1.18x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 73.3 ms: 1.19x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.81 ms: 1.21x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 54.8 ms: 1.24x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 301 us: 1.30x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 210 us: 1.31x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 3.64 sec: 2.12x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.26x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.8 ms: 1.05x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 23.8 ms: 1.21x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 59.6 ms: 1.19x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 27.2 ms: 1.27x slower                                                           |
| django_template | 29.8 ms                                                         | 38.8 ms: 1.30x slower                                                           |
| mako            | 7.09 ms                                                         | 11.7 ms: 1.65x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.34x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 793 us: 12.58x faster                                                           |
| coverage                   | 324 ms                                                          | 74.0 ms: 4.38x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 37.8 ms: 2.19x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 166 ms: 2.19x faster                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.07 ms: 1.63x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 13.5 ms: 1.25x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 872 us: 1.21x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.61 us: 1.21x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 236 ms: 1.20x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 416 ms: 1.19x faster                                                            |
| async_tree_io              | 526 ms                                                          | 445 ms: 1.18x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| async_tree_none            | 245 ms                                                          | 215 ms: 1.14x faster                                                            |
| deepcopy                   | 314 us                                                          | 280 us: 1.12x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 265 ms: 1.12x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 82.2 ms: 1.10x faster                                                           |
| pidigits                   | 201 ms                                                          | 187 ms: 1.07x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.52 sec: 1.07x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 428 ms: 1.06x faster                                                            |
| regex_dna                  | 114 ms                                                          | 107 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 459 ms: 1.05x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 3.02 us: 1.04x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.8 ms: 1.05x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                           |
| deepcopy_memo              | 25.4 us                                                         | 27.0 us: 1.06x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.44 ms: 1.07x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.0 ms: 1.07x slower                                                           |
| pylint                     | 227 ms                                                          | 249 ms: 1.10x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 52.2 ms: 1.10x slower                                                           |
| 2to3                       | 250 ms                                                          | 278 ms: 1.11x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 54.3 ms: 1.11x slower                                                           |
| json                       | 4.27 ms                                                         | 4.85 ms: 1.14x slower                                                           |
| float                      | 54.6 ms                                                         | 62.5 ms: 1.15x slower                                                           |
| logging_format             | 8.72 us                                                         | 10.0 us: 1.15x slower                                                           |
| sympy_expand               | 373 ms                                                          | 431 ms: 1.15x slower                                                            |
| async_generators           | 270 ms                                                          | 313 ms: 1.16x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.31 us: 1.17x slower                                                           |
| sympy_str                  | 212 ms                                                          | 250 ms: 1.18x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 125 ms: 1.18x slower                                                            |
| json_loads                 | 21.6 us                                                         | 25.6 us: 1.18x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 59.6 ms: 1.19x slower                                                           |
| generators                 | 21.8 ms                                                         | 25.9 ms: 1.19x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 73.3 ms: 1.19x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.81 ms: 1.21x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 18.1 ms: 1.21x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 23.8 ms: 1.21x slower                                                           |
| go                         | 109 ms                                                          | 133 ms: 1.23x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 54.8 ms: 1.24x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 90.0 ms: 1.25x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 86.9 ms: 1.25x slower                                                           |
| regex_compile              | 101 ms                                                          | 127 ms: 1.25x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 108 ms: 1.26x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 27.2 ms: 1.27x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.29 ms: 1.29x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 96.3 ms: 1.29x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 301 us: 1.30x slower                                                            |
| pyflate                    | 320 ms                                                          | 417 ms: 1.30x slower                                                            |
| fannkuch                   | 299 ms                                                          | 389 ms: 1.30x slower                                                            |
| django_template            | 29.8 ms                                                         | 38.8 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 180 us: 1.31x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 210 us: 1.31x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 74.7 ms: 1.31x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 857 ms: 1.32x slower                                                            |
| chaos                      | 50.2 ms                                                         | 66.4 ms: 1.32x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.11 ms: 1.33x slower                                                           |
| comprehensions             | 12.5 us                                                         | 16.8 us: 1.34x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 80.9 ns: 1.34x slower                                                           |
| sphinx                     | 719 ms                                                          | 970 ms: 1.35x slower                                                            |
| pycparser                  | 872 ms                                                          | 1.18 sec: 1.36x slower                                                          |
| hexiom                     | 4.44 ms                                                         | 6.07 ms: 1.37x slower                                                           |
| many_optionals             | 436 us                                                          | 601 us: 1.38x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 83.4 ms: 1.39x slower                                                           |
| raytrace                   | 201 ms                                                          | 280 ms: 1.39x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.98 ms: 1.40x slower                                                           |
| scimark_fft                | 205 ms                                                          | 288 ms: 1.41x slower                                                            |
| richards_super             | 36.7 ms                                                         | 52.7 ms: 1.44x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 69.1 ms: 1.45x slower                                                           |
| richards                   | 32.7 ms                                                         | 47.9 ms: 1.47x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 23.3 ms: 1.58x slower                                                           |
| mako                       | 7.09 ms                                                         | 11.7 ms: 1.65x slower                                                           |
| nbody                      | 80.0 ms                                                         | 133 ms: 1.66x slower                                                            |
| docutils                   | 1.78 sec                                                        | 3.16 sec: 1.77x slower                                                          |
| bpe_tokeniser              | 3.46 sec                                                        | 6.45 sec: 1.86x slower                                                          |
| pprint_pformat             | 1.33 sec                                                        | 2.49 sec: 1.87x slower                                                          |
| k_core                     | 1.38 sec                                                        | 2.62 sec: 1.90x slower                                                          |
| tomli_loads                | 1.71 sec                                                        | 3.64 sec: 2.12x slower                                                          |
| shortest_path              | 290 ms                                                          | 651 ms: 2.25x slower                                                            |
| connected_components       | 267 ms                                                          | 619 ms: 2.32x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x slower                                                                    |
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.107x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.11x

# Memory
- memory change: unknown