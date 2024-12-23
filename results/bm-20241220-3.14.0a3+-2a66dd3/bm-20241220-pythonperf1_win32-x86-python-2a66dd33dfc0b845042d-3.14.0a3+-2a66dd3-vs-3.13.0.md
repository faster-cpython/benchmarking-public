# Results vs. 3.13.0

- fork: python
- ref: 2a66dd33dfc0b845042d
- machine: windows-x86
- commit hash: 2a66dd3
- commit date: 2024-12-20
- overall geometric mean: 1.032x faster
- HPT reliability: 86.70%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 246 ms: 1.02x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 44.1 ms: 1.08x faster                                                           |
| sphinx         | 719 ms                                                          | 732 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 232 ms: 1.22x faster                                                            |
| async_tree_none            | 245 ms                                                          | 203 ms: 1.21x faster                                                            |
| async_tree_io              | 526 ms                                                          | 443 ms: 1.19x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 253 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 185 ms: 1.16x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 426 ms: 1.16x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 449 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                           |
| async_generators           | 270 ms                                                          | 291 ms: 1.08x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 84.2 ms: 1.05x slower                                                           |
| float          | 54.6 ms                                                         | 59.0 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.64 ms: 1.10x faster                                                           |
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                                            |
| regex_dna      | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.64 sec: 1.04x faster                                                          |
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 174 us: 1.09x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 48.6 ms: 1.10x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.9 ms: 1.11x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 268 us: 1.16x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.08 ms: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.6 ms: 1.10x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 21.3 ms: 1.01x faster                                                           |
| django_template | 29.8 ms                                                         | 31.5 ms: 1.06x slower                                                           |
| mako            | 7.09 ms                                                         | 7.74 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 742 us: 13.45x faster                                                           |
| coverage                   | 324 ms                                                          | 51.1 ms: 6.33x faster                                                           |
| deepcopy                   | 314 us                                                          | 227 us: 1.38x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 232 ms: 1.22x faster                                                            |
| async_tree_none            | 245 ms                                                          | 203 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.45 us: 1.19x faster                                                           |
| async_tree_io              | 526 ms                                                          | 443 ms: 1.19x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 253 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 185 ms: 1.16x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 426 ms: 1.16x faster                                                            |
| go                         | 109 ms                                                          | 97.0 ms: 1.12x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 22.8 us: 1.12x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 45.6 ms: 1.10x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.64 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 449 ms: 1.08x faster                                                            |
| html5lib                   | 47.5 ms                                                         | 44.1 ms: 1.08x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| pycparser                  | 872 ms                                                          | 830 ms: 1.05x faster                                                            |
| pylint                     | 227 ms                                                          | 216 ms: 1.05x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                            |
| tomli_loads                | 1.71 sec                                                        | 1.64 sec: 1.04x faster                                                          |
| connected_components       | 267 ms                                                          | 256 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 439 ms: 1.04x faster                                                            |
| telco                      | 6.96 ms                                                         | 6.71 ms: 1.04x faster                                                           |
| logging_simple             | 7.99 us                                                         | 7.71 us: 1.04x faster                                                           |
| logging_format             | 8.72 us                                                         | 8.49 us: 1.03x faster                                                           |
| shortest_path              | 290 ms                                                          | 284 ms: 1.02x faster                                                            |
| 2to3                       | 250 ms                                                          | 246 ms: 1.02x faster                                                            |
| json                       | 4.27 ms                                                         | 4.20 ms: 1.02x faster                                                           |
| k_core                     | 1.38 sec                                                        | 1.35 sec: 1.02x faster                                                          |
| genshi_text                | 21.5 ms                                                         | 21.3 ms: 1.01x faster                                                           |
| xml_etree_parse            | 107 ms                                                          | 107 ms: 1.01x faster                                                            |
| pprint_safe_repr           | 648 ms                                                          | 646 ms: 1.00x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 82.5 ms: 1.00x faster                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.32 sec: 1.00x faster                                                          |
| fannkuch                   | 299 ms                                                          | 300 ms: 1.01x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| create_gc_cycles           | 1.06 ms                                                         | 1.07 ms: 1.01x slower                                                           |
| sympy_expand               | 373 ms                                                          | 380 ms: 1.02x slower                                                            |
| sphinx                     | 719 ms                                                          | 732 ms: 1.02x slower                                                            |
| regex_compile              | 101 ms                                                          | 103 ms: 1.02x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 70.7 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 216 ms                                                          | 221 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 141 us: 1.02x slower                                                            |
| sympy_str                  | 212 ms                                                          | 217 ms: 1.02x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 92.6 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 42.4 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.54 sec: 1.02x slower                                                          |
| python_startup_no_site     | 19.7 ms                                                         | 20.2 ms: 1.03x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.4 ms: 1.03x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.28 ms: 1.03x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 50.4 ms: 1.03x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.83 ms: 1.04x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.70 sec: 1.05x slower                                                          |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| nbody                      | 80.0 ms                                                         | 84.2 ms: 1.05x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.1 ms: 1.05x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 60.2 ms: 1.06x slower                                                           |
| django_template            | 29.8 ms                                                         | 31.5 ms: 1.06x slower                                                           |
| pyflate                    | 320 ms                                                          | 339 ms: 1.06x slower                                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.02 ms: 1.06x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 80.3 ms: 1.08x slower                                                           |
| async_generators           | 270 ms                                                          | 291 ms: 1.08x slower                                                            |
| float                      | 54.6 ms                                                         | 59.0 ms: 1.08x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 174 us: 1.09x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 78.6 ms: 1.09x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.74 ms: 1.09x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 48.6 ms: 1.10x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.58 ms: 1.10x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.9 ms: 1.11x slower                                                           |
| regex_dna                  | 114 ms                                                          | 126 ms: 1.11x slower                                                            |
| scimark_fft                | 205 ms                                                          | 228 ms: 1.11x slower                                                            |
| chaos                      | 50.2 ms                                                         | 56.2 ms: 1.12x slower                                                           |
| generators                 | 21.8 ms                                                         | 24.4 ms: 1.12x slower                                                           |
| comprehensions             | 12.5 us                                                         | 14.2 us: 1.13x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.03 ms: 1.13x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.3 ms: 1.14x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.4 ms: 1.14x slower                                                           |
| logging_silent             | 60.3 ns                                                         | 69.3 ns: 1.15x slower                                                           |
| richards_super             | 36.7 ms                                                         | 42.5 ms: 1.16x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 268 us: 1.16x slower                                                            |
| many_optionals             | 436 us                                                          | 508 us: 1.17x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 100 ms: 1.17x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 70.9 ms: 1.18x slower                                                           |
| raytrace                   | 201 ms                                                          | 245 ms: 1.22x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 9.08 ms: 1.24x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.2 ms: 1.37x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (5): regex_v8, sqlite_synth, pidigits, sympy_sum, bench_thread_pool
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241220-3.14.0a3+-2a66dd3/bm-20241220-pythonperf1_win32-x86-python-2a66dd33dfc0b845042d-3.14.0a3+-2a66dd3.json: mypy2

- Geometric mean (including insignificant results): 1.032x faster

# HPT report

- Reliability score: 86.70% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown