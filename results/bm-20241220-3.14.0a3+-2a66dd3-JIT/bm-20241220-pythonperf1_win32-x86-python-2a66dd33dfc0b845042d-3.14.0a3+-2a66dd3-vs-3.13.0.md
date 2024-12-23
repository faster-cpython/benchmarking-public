# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.052x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 265 ms: 1.06x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                          |
| html5lib       | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                           |
| sphinx         | 719 ms                                                          | 789 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 257 ms: 1.10x faster                                                            |
| async_tree_io              | 526 ms                                                          | 497 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 468 ms: 1.06x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 206 ms: 1.04x faster                                                            |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 355 ms: 1.02x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 290 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 447 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                           |
| async_generators           | 270 ms                                                          | 323 ms: 1.20x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| float          | 54.6 ms                                                         | 57.3 ms: 1.05x slower                                                           |
| nbody          | 80.0 ms                                                         | 96.3 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_compile  | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 21.1 us: 1.03x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| tomli_loads          | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 70.0 ms: 1.14x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 52.5 ms: 1.19x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 205 us: 1.28x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.55 ms: 1.31x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 303 us: 1.31x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.14x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 55.9 ms: 1.11x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 25.3 ms: 1.18x slower                                                           |
| django_template | 29.8 ms                                                         | 37.6 ms: 1.26x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.14x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 776 us: 12.86x faster                                                           |
| coverage                   | 324 ms                                                          | 52.7 ms: 6.15x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 108 ms: 2.00x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| deepcopy                   | 314 us                                                          | 282 us: 1.12x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 257 ms: 1.10x faster                                                            |
| python_startup             | 28.3 ms                                                         | 25.8 ms: 1.10x faster                                                           |
| async_tree_io              | 526 ms                                                          | 497 ms: 1.06x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 468 ms: 1.06x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 206 ms: 1.04x faster                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 87.3 ms: 1.04x faster                                                           |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 24.8 us: 1.03x faster                                                           |
| json_loads                 | 21.6 us                                                         | 21.1 us: 1.03x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 355 ms: 1.02x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 290 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 447 ms: 1.02x faster                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 19.4 ms: 1.01x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.90 us: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 108 ms: 1.01x slower                                                            |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                                            |
| pathlib                    | 82.9 ms                                                         | 83.8 ms: 1.01x slower                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.98 us: 1.01x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                          |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.02x slower                                                          |
| html5lib                   | 47.5 ms                                                         | 48.9 ms: 1.03x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.19 ms: 1.03x slower                                                           |
| pylint                     | 227 ms                                                          | 234 ms: 1.03x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.33 ms: 1.04x slower                                                           |
| json                       | 4.27 ms                                                         | 4.43 ms: 1.04x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| float                      | 54.6 ms                                                         | 57.3 ms: 1.05x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.17 us: 1.05x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 51.3 ms: 1.05x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 73.1 ms: 1.05x slower                                                           |
| 2to3                       | 250 ms                                                          | 265 ms: 1.06x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.07x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.53 us: 1.07x slower                                                           |
| connected_components       | 267 ms                                                          | 286 ms: 1.07x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.06 ms: 1.08x slower                                                           |
| shortest_path              | 290 ms                                                          | 315 ms: 1.09x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 116 ms: 1.10x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.95 sec: 1.10x slower                                                          |
| sphinx                     | 719 ms                                                          | 789 ms: 1.10x slower                                                            |
| pycparser                  | 872 ms                                                          | 958 ms: 1.10x slower                                                            |
| sympy_expand               | 373 ms                                                          | 411 ms: 1.10x slower                                                            |
| genshi_xml                 | 50.1 ms                                                         | 55.9 ms: 1.11x slower                                                           |
| sympy_str                  | 212 ms                                                          | 236 ms: 1.12x slower                                                            |
| fannkuch                   | 299 ms                                                          | 333 ms: 1.12x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.88 sec: 1.12x slower                                                          |
| regex_compile              | 101 ms                                                          | 114 ms: 1.13x slower                                                            |
| go                         | 109 ms                                                          | 123 ms: 1.13x slower                                                            |
| pprint_safe_repr           | 648 ms                                                          | 739 ms: 1.14x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 70.0 ms: 1.14x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.52 sec: 1.14x slower                                                          |
| scimark_fft                | 205 ms                                                          | 237 ms: 1.16x slower                                                            |
| pyflate                    | 320 ms                                                          | 372 ms: 1.16x slower                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.17 ms: 1.17x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 100 ms: 1.17x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.90 sec: 1.17x slower                                                          |
| sqlglot_transpile          | 1.24 ms                                                         | 1.45 ms: 1.17x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 25.3 ms: 1.18x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 17.7 ms: 1.18x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 88.7 ms: 1.19x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 52.5 ms: 1.19x slower                                                           |
| async_generators           | 270 ms                                                          | 323 ms: 1.20x slower                                                            |
| nbody                      | 80.0 ms                                                         | 96.3 ms: 1.20x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 68.8 ms: 1.21x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 74.3 ms: 1.23x slower                                                           |
| typing_runtime_protocols   | 138 us                                                          | 170 us: 1.23x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 51.3 ms: 1.24x slower                                                           |
| django_template            | 29.8 ms                                                         | 37.6 ms: 1.26x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 205 us: 1.28x slower                                                            |
| many_optionals             | 436 us                                                          | 568 us: 1.30x slower                                                            |
| chaos                      | 50.2 ms                                                         | 65.6 ms: 1.31x slower                                                           |
| richards_super             | 36.7 ms                                                         | 48.0 ms: 1.31x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.55 ms: 1.31x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 303 us: 1.31x slower                                                            |
| richards                   | 32.7 ms                                                         | 43.0 ms: 1.31x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 62.9 ms: 1.32x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 97.7 ms: 1.36x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.23 ms: 1.38x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 86.6 ns: 1.43x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.7 ms: 1.47x slower                                                           |
| comprehensions             | 12.5 us                                                         | 18.6 us: 1.49x slower                                                           |
| raytrace                   | 201 ms                                                          | 322 ms: 1.60x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.12 ms: 1.60x slower                                                           |
| generators                 | 21.8 ms                                                         | 36.5 ms: 1.68x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (3): regex_v8, create_gc_cycles, regex_dna
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3-JIT/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.052x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown