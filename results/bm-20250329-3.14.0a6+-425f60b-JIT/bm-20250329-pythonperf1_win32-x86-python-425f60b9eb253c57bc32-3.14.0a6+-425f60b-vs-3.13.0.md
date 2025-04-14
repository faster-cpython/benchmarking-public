# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.075x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 283 ms: 1.13x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.99 sec: 1.12x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.2 ms: 1.02x slower                                                           |
| sphinx         | 719 ms                                                          | 796 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 205 ms: 1.77x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 257 ms: 1.10x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 271 ms: 1.09x faster                                                            |
| async_tree_io              | 526 ms                                                          | 494 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 232 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.04x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 211 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 515 ms: 1.06x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.09x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 501 ms: 1.10x slower                                                            |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.01x slower                                                            |
| float          | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| nbody          | 80.0 ms                                                         | 112 ms: 1.41x slower                                                            |
| Geometric mean | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                           |
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                           |
| regex_compile  | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.87 sec: 1.09x slower                                                          |
| json_dumps           | 7.30 ms                                                         | 8.35 ms: 1.14x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 56.3 ms: 1.27x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 326 us: 1.41x slower                                                            |
| unpickle_pure_python | 160 us                                                          | 239 us: 1.49x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.18x slower                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.9 ms: 1.16x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 54.3 ms: 1.08x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 23.6 ms: 1.10x slower                                                           |
| mako            | 7.09 ms                                                         | 8.18 ms: 1.16x slower                                                           |
| django_template | 29.8 ms                                                         | 35.7 ms: 1.20x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coverage                   | 324 ms                                                          | 55.0 ms: 5.89x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 37.5 ms: 2.21x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 205 ms: 1.77x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.13 sec: 1.44x faster                                                          |
| deepcopy                   | 314 us                                                          | 254 us: 1.24x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 14.5 ms: 1.16x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.62 us: 1.11x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 257 ms: 1.10x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 271 ms: 1.09x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 23.3 us: 1.09x faster                                                           |
| async_tree_io              | 526 ms                                                          | 494 ms: 1.06x faster                                                            |
| async_tree_none            | 245 ms                                                          | 232 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 473 ms: 1.04x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.03x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 211 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                          | 202 ms: 1.01x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 48.2 ms: 1.02x slower                                                           |
| python_startup             | 28.3 ms                                                         | 29.0 ms: 1.03x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.03x slower                                                            |
| pylint                     | 227 ms                                                          | 235 ms: 1.04x slower                                                            |
| go                         | 109 ms                                                          | 114 ms: 1.05x slower                                                            |
| float                      | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 95.6 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 515 ms: 1.06x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.87 ms: 1.07x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 114 ms: 1.08x slower                                                            |
| k_core                     | 1.38 sec                                                        | 1.49 sec: 1.08x slower                                                          |
| genshi_xml                 | 50.1 ms                                                         | 54.3 ms: 1.08x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.45 us: 1.08x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 53.0 ms: 1.09x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 68.1 ms: 1.09x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.87 sec: 1.09x slower                                                          |
| json                       | 4.27 ms                                                         | 4.66 ms: 1.09x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.8 ms: 1.09x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.76 us: 1.10x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 23.6 ms: 1.10x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 501 ms: 1.10x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.14 ms: 1.10x slower                                                           |
| sphinx                     | 719 ms                                                          | 796 ms: 1.11x slower                                                            |
| telco                      | 6.96 ms                                                         | 7.75 ms: 1.11x slower                                                           |
| sympy_str                  | 212 ms                                                          | 236 ms: 1.11x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 16.7 ms: 1.12x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.99 sec: 1.12x slower                                                          |
| sympy_expand               | 373 ms                                                          | 421 ms: 1.13x slower                                                            |
| 2to3                       | 250 ms                                                          | 283 ms: 1.13x slower                                                            |
| regex_compile              | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 78.6 ms: 1.13x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.35 ms: 1.14x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.7 ms: 1.15x slower                                                           |
| pycparser                  | 872 ms                                                          | 1.01 sec: 1.15x slower                                                          |
| mako                       | 7.09 ms                                                         | 8.18 ms: 1.16x slower                                                           |
| shortest_path              | 290 ms                                                          | 337 ms: 1.16x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 22.9 ms: 1.16x slower                                                           |
| connected_components       | 267 ms                                                          | 311 ms: 1.17x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 101 ms: 1.17x slower                                                            |
| pyflate                    | 320 ms                                                          | 377 ms: 1.18x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 72.6 ms: 1.18x slower                                                           |
| chaos                      | 50.2 ms                                                         | 59.5 ms: 1.19x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 4.13 sec: 1.19x slower                                                          |
| django_template            | 29.8 ms                                                         | 35.7 ms: 1.20x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.61 sec: 1.21x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 786 ms: 1.21x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 92.2 ms: 1.24x slower                                                           |
| generators                 | 21.8 ms                                                         | 27.0 ms: 1.24x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 75.3 ns: 1.25x slower                                                           |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| fannkuch                   | 299 ms                                                          | 376 ms: 1.26x slower                                                            |
| raytrace                   | 201 ms                                                          | 255 ms: 1.27x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 56.3 ms: 1.27x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 76.8 ms: 1.27x slower                                                           |
| many_optionals             | 436 us                                                          | 563 us: 1.29x slower                                                            |
| richards_super             | 36.7 ms                                                         | 47.5 ms: 1.29x slower                                                           |
| richards                   | 32.7 ms                                                         | 42.3 ms: 1.30x slower                                                           |
| scimark_fft                | 205 ms                                                          | 265 ms: 1.30x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 93.6 ms: 1.30x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 180 us: 1.31x slower                                                            |
| deltablue                  | 2.33 ms                                                         | 3.10 ms: 1.33x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.34 ms: 1.34x slower                                                           |
| nbody                      | 80.0 ms                                                         | 112 ms: 1.41x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 326 us: 1.41x slower                                                            |
| crypto_pyaes               | 56.9 ms                                                         | 83.3 ms: 1.46x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.6 us: 1.48x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 239 us: 1.49x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 22.1 ms: 1.50x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 6.75 ms: 1.52x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.08x slower                                                                    |

Benchmark hidden because not significant (3): regex_dna, json_loads, create_gc_cycles
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b-JIT/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.075x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown