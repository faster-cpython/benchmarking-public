# Results vs. 3.13.0

- fork: python
- ref: 22a442181d5f1ac496da
- machine: windows-x86
- commit hash: 22a4421
- commit date: 2025-01-11
- overall geometric mean: 1.048x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.98 sec: 1.12x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 799 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| async_tree_io              | 526 ms                                                          | 485 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 457 ms: 1.08x faster                                                            |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 445 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                            |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 52.1 ms: 1.05x faster                                                           |
| nbody          | 80.0 ms                                                         | 100 ms: 1.25x slower                                                            |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| regex_dna      | 114 ms                                                          | 116 ms: 1.02x slower                                                            |
| regex_compile  | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.02x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.98 ms: 1.23x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 54.4 ms: 1.23x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 76.1 ms: 1.24x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 202 us: 1.26x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 298 us: 1.29x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.42 ms: 1.05x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 57.1 ms: 1.14x slower                                                           |
| django_template | 29.8 ms                                                         | 36.9 ms: 1.24x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 26.7 ms: 1.24x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.16x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 758 us: 13.16x faster                                                           |
| coverage                   | 324 ms                                                          | 53.0 ms: 6.11x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 107 ms: 2.03x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                            |
| deepcopy                   | 314 us                                                          | 280 us: 1.12x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| async_tree_io              | 526 ms                                                          | 485 ms: 1.08x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 457 ms: 1.08x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 23.8 us: 1.07x faster                                                           |
| float                      | 54.6 ms                                                         | 52.1 ms: 1.05x faster                                                           |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 445 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 473 ms: 1.02x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 88.7 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.87 us: 1.02x faster                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.94 us: 1.01x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.07 ms: 1.01x slower                                                           |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.02x slower                                                            |
| json                       | 4.27 ms                                                         | 4.36 ms: 1.02x slower                                                           |
| regex_dna                  | 114 ms                                                          | 116 ms: 1.02x slower                                                            |
| html5lib                   | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.77 sec: 1.03x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.42 sec: 1.03x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 72.6 ms: 1.05x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.42 ms: 1.05x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.83 ms: 1.05x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.31 ms: 1.05x slower                                                           |
| pylint                     | 227 ms                                                          | 238 ms: 1.05x slower                                                            |
| pathlib                    | 82.9 ms                                                         | 87.1 ms: 1.05x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.06 ms: 1.05x slower                                                           |
| 2to3                       | 250 ms                                                          | 264 ms: 1.06x slower                                                            |
| dulwich_log                | 48.8 ms                                                         | 51.5 ms: 1.06x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.23 us: 1.06x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.03 ms: 1.07x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.57 us: 1.07x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 115 ms: 1.09x slower                                                            |
| pycparser                  | 872 ms                                                          | 950 ms: 1.09x slower                                                            |
| connected_components       | 267 ms                                                          | 291 ms: 1.09x slower                                                            |
| sympy_expand               | 373 ms                                                          | 413 ms: 1.11x slower                                                            |
| shortest_path              | 290 ms                                                          | 321 ms: 1.11x slower                                                            |
| sphinx                     | 719 ms                                                          | 799 ms: 1.11x slower                                                            |
| sympy_str                  | 212 ms                                                          | 235 ms: 1.11x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.85 sec: 1.11x slower                                                          |
| docutils                   | 1.78 sec                                                        | 1.98 sec: 1.12x slower                                                          |
| regex_compile              | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.50 sec: 1.13x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 735 ms: 1.13x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 57.1 ms: 1.14x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.85 sec: 1.14x slower                                                          |
| fannkuch                   | 299 ms                                                          | 342 ms: 1.14x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 98.3 ms: 1.14x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.15 ms: 1.15x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.42 ms: 1.15x slower                                                           |
| go                         | 109 ms                                                          | 126 ms: 1.16x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 17.4 ms: 1.16x slower                                                           |
| scimark_fft                | 205 ms                                                          | 239 ms: 1.17x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 89.1 ms: 1.19x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 73.0 ms: 1.21x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 167 us: 1.21x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 50.6 ms: 1.22x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 69.8 ms: 1.23x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.98 ms: 1.23x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 54.4 ms: 1.23x slower                                                           |
| django_template            | 29.8 ms                                                         | 36.9 ms: 1.24x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 76.1 ms: 1.24x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 26.7 ms: 1.24x slower                                                           |
| pyflate                    | 320 ms                                                          | 400 ms: 1.25x slower                                                            |
| async_generators           | 270 ms                                                          | 338 ms: 1.25x slower                                                            |
| nbody                      | 80.0 ms                                                         | 100 ms: 1.25x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 202 us: 1.26x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 298 us: 1.29x slower                                                            |
| chaos                      | 50.2 ms                                                         | 65.0 ms: 1.29x slower                                                           |
| many_optionals             | 436 us                                                          | 565 us: 1.30x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 62.2 ms: 1.31x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 79.0 ns: 1.31x slower                                                           |
| richards                   | 32.7 ms                                                         | 43.1 ms: 1.32x slower                                                           |
| richards_super             | 36.7 ms                                                         | 48.4 ms: 1.32x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 95.6 ms: 1.33x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.18 ms: 1.36x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.4 ms: 1.45x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.2 us: 1.45x slower                                                           |
| raytrace                   | 201 ms                                                          | 305 ms: 1.52x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.11 ms: 1.60x slower                                                           |
| generators                 | 21.8 ms                                                         | 38.0 ms: 1.74x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250111-3.14.0a3+-22a4421-JIT/bm-20250111-pythonperf1_win32-x86-python-22a442181d5f1ac496da-3.14.0a3+-22a4421.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.048x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown