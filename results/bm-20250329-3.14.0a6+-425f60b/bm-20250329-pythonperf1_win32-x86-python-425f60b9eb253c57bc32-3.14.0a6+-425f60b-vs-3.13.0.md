# Results vs. 3.13.0

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: windows-x86
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.013x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.88 sec: 1.06x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.6 ms: 1.02x slower                                                           |
| sphinx         | 719 ms                                                          | 774 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 200 ms: 1.81x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 258 ms: 1.15x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.14x faster                                                            |
| async_tree_io              | 526 ms                                                          | 470 ms: 1.12x faster                                                            |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 459 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 466 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 451 ms: 1.01x faster                                                            |
| async_generators           | 270 ms                                                          | 299 ms: 1.11x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 54.2 ms: 1.01x faster                                                           |
| nbody          | 80.0 ms                                                         | 85.9 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.1 ms: 1.11x faster                                                           |
| regex_dna      | 114 ms                                                          | 119 ms: 1.05x slower                                                            |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 21.8 us: 1.01x slower                                                           |
| xml_etree_parse      | 107 ms                                                          | 112 ms: 1.04x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.18 ms: 1.12x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 69.4 ms: 1.13x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 186 us: 1.16x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 271 us: 1.17x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 52.0 ms: 1.18x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 28.8 ms: 1.02x slower                                                           |
| python_startup_no_site | 19.7 ms                                                         | 22.7 ms: 1.15x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 23.0 ms: 1.07x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 53.8 ms: 1.07x slower                                                           |
| mako            | 7.09 ms                                                         | 8.37 ms: 1.18x slower                                                           |
| django_template | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.13x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coverage                   | 324 ms                                                          | 53.3 ms: 6.08x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 37.7 ms: 2.20x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 200 ms: 1.81x faster                                                            |
| mdp                        | 1.62 sec                                                        | 1.03 sec: 1.57x faster                                                          |
| deepcopy                   | 314 us                                                          | 248 us: 1.27x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 20.4 us: 1.24x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 258 ms: 1.15x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.57 ms: 1.15x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.14x faster                                                            |
| async_tree_io              | 526 ms                                                          | 470 ms: 1.12x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.1 ms: 1.11x faster                                                           |
| async_tree_none            | 245 ms                                                          | 221 ms: 1.11x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.65 us: 1.10x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 459 ms: 1.08x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 204 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 466 ms: 1.04x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 451 ms: 1.01x faster                                                            |
| float                      | 54.6 ms                                                         | 54.2 ms: 1.01x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.8 us: 1.01x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.07 ms: 1.02x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 659 ms: 1.02x slower                                                            |
| python_startup             | 28.3 ms                                                         | 28.8 ms: 1.02x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.36 sec: 1.02x slower                                                          |
| html5lib                   | 47.5 ms                                                         | 48.6 ms: 1.02x slower                                                           |
| go                         | 109 ms                                                          | 111 ms: 1.02x slower                                                            |
| connected_components       | 267 ms                                                          | 276 ms: 1.04x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 71.9 ms: 1.04x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 112 ms: 1.04x slower                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.05x slower                                                          |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.05x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 15.7 ms: 1.05x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 95.2 ms: 1.05x slower                                                           |
| pycparser                  | 872 ms                                                          | 917 ms: 1.05x slower                                                            |
| 2to3                       | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 112 ms: 1.06x slower                                                            |
| shortest_path              | 290 ms                                                          | 307 ms: 1.06x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.88 sec: 1.06x slower                                                          |
| fannkuch                   | 299 ms                                                          | 317 ms: 1.06x slower                                                            |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| sympy_str                  | 212 ms                                                          | 226 ms: 1.07x slower                                                            |
| genshi_text                | 21.5 ms                                                         | 23.0 ms: 1.07x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 53.8 ms: 1.07x slower                                                           |
| json                       | 4.27 ms                                                         | 4.59 ms: 1.07x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.72 sec: 1.07x slower                                                          |
| sympy_expand               | 373 ms                                                          | 401 ms: 1.07x slower                                                            |
| nbody                      | 80.0 ms                                                         | 85.9 ms: 1.07x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 52.4 ms: 1.08x slower                                                           |
| sphinx                     | 719 ms                                                          | 774 ms: 1.08x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.11 ms: 1.10x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.58 us: 1.10x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 52.7 ms: 1.10x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.85 us: 1.11x slower                                                           |
| async_generators           | 270 ms                                                          | 299 ms: 1.11x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 67.0 ns: 1.11x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 83.4 ms: 1.12x slower                                                           |
| chaos                      | 50.2 ms                                                         | 56.2 ms: 1.12x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.18 ms: 1.12x slower                                                           |
| scimark_fft                | 205 ms                                                          | 230 ms: 1.13x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 96.8 ms: 1.13x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 64.4 ms: 1.13x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 69.4 ms: 1.13x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 68.2 ms: 1.13x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.65 ms: 1.14x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 157 us: 1.14x slower                                                            |
| pyflate                    | 320 ms                                                          | 365 ms: 1.14x slower                                                            |
| comprehensions             | 12.5 us                                                         | 14.4 us: 1.15x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 22.7 ms: 1.15x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 83.1 ms: 1.15x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 186 us: 1.16x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 5.19 ms: 1.17x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 271 us: 1.17x slower                                                            |
| generators                 | 21.8 ms                                                         | 25.6 ms: 1.17x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 52.0 ms: 1.18x slower                                                           |
| mako                       | 7.09 ms                                                         | 8.37 ms: 1.18x slower                                                           |
| richards                   | 32.7 ms                                                         | 38.7 ms: 1.18x slower                                                           |
| richards_super             | 36.7 ms                                                         | 43.8 ms: 1.19x slower                                                           |
| raytrace                   | 201 ms                                                          | 240 ms: 1.19x slower                                                            |
| django_template            | 29.8 ms                                                         | 36.1 ms: 1.21x slower                                                           |
| many_optionals             | 436 us                                                          | 554 us: 1.27x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.30 ms: 1.29x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 22.4 ms: 1.52x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (4): pidigits, create_gc_cycles, pylint, coroutines
Ignored benchmarks (11) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250329-3.14.0a6+-425f60b/bm-20250329-pythonperf1_win32-x86-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown