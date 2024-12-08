# Results vs. 3.13.0

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-x86
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.034x faster
- HPT reliability: 86.53%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 247 ms: 1.01x faster                                                            |
| docutils       | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| html5lib       | 47.5 ms                                                         | 44.7 ms: 1.06x faster                                                           |
| sphinx         | 719 ms                                                          | 727 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 201 ms: 1.22x faster                                                            |
| async_tree_io              | 526 ms                                                          | 432 ms: 1.22x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 237 ms: 1.19x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 250 ms: 1.19x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 421 ms: 1.17x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 187 ms: 1.14x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 449 ms: 1.08x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 443 ms: 1.03x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                           |
| async_generators           | 270 ms                                                          | 296 ms: 1.10x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.01x slower                                                            |
| nbody          | 80.0 ms                                                         | 86.7 ms: 1.08x slower                                                           |
| float          | 54.6 ms                                                         | 60.8 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.3 ms: 1.10x faster                                                           |
| regex_dna      | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| regex_compile  | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.3 us: 1.07x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 104 ms: 1.03x faster                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.80 sec: 1.05x slower                                                          |
| unpickle_pure_python | 160 us                                                          | 170 us: 1.06x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 48.3 ms: 1.09x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.3 ms: 1.10x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.57 ms: 1.17x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 274 us: 1.19x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 45.7 ms: 1.10x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 21.0 ms: 1.02x faster                                                           |
| mako            | 7.09 ms                                                         | 7.50 ms: 1.06x slower                                                           |
| django_template | 29.8 ms                                                         | 32.5 ms: 1.09x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241207-pythonperf1_win32-x86-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 736 us: 13.55x faster                                                           |
| coverage                   | 324 ms                                                          | 52.9 ms: 6.12x faster                                                           |
| deepcopy                   | 314 us                                                          | 230 us: 1.36x faster                                                            |
| async_tree_none            | 245 ms                                                          | 201 ms: 1.22x faster                                                            |
| async_tree_io              | 526 ms                                                          | 432 ms: 1.22x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.45 us: 1.19x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 237 ms: 1.19x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.4 us: 1.19x faster                                                           |
| async_tree_memoization     | 297 ms                                                          | 250 ms: 1.19x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 421 ms: 1.17x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 187 ms: 1.14x faster                                                            |
| go                         | 109 ms                                                          | 98.3 ms: 1.11x faster                                                           |
| regex_v8                   | 16.8 ms                                                         | 15.3 ms: 1.10x faster                                                           |
| genshi_xml                 | 50.1 ms                                                         | 45.7 ms: 1.10x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 972 us: 1.09x faster                                                            |
| pylint                     | 227 ms                                                          | 210 ms: 1.08x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 449 ms: 1.08x faster                                                            |
| telco                      | 6.96 ms                                                         | 6.51 ms: 1.07x faster                                                           |
| pycparser                  | 872 ms                                                          | 816 ms: 1.07x faster                                                            |
| json_loads                 | 21.6 us                                                         | 20.3 us: 1.07x faster                                                           |
| html5lib                   | 47.5 ms                                                         | 44.7 ms: 1.06x faster                                                           |
| python_startup             | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 349 ms: 1.04x faster                                                            |
| k_core                     | 1.38 sec                                                        | 1.33 sec: 1.04x faster                                                          |
| logging_format             | 8.72 us                                                         | 8.44 us: 1.03x faster                                                           |
| connected_components       | 267 ms                                                          | 259 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 443 ms: 1.03x faster                                                            |
| xml_etree_parse            | 107 ms                                                          | 104 ms: 1.03x faster                                                            |
| logging_simple             | 7.99 us                                                         | 7.78 us: 1.03x faster                                                           |
| pprint_safe_repr           | 648 ms                                                          | 634 ms: 1.02x faster                                                            |
| genshi_text                | 21.5 ms                                                         | 21.0 ms: 1.02x faster                                                           |
| json                       | 4.27 ms                                                         | 4.18 ms: 1.02x faster                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 983 us: 1.02x faster                                                            |
| pathlib                    | 82.9 ms                                                         | 81.6 ms: 1.02x faster                                                           |
| 2to3                       | 250 ms                                                          | 247 ms: 1.01x faster                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.43 sec: 1.01x faster                                                          |
| shortest_path              | 290 ms                                                          | 289 ms: 1.00x faster                                                            |
| sqlglot_normalize          | 216 ms                                                          | 218 ms: 1.01x slower                                                            |
| pidigits                   | 201 ms                                                          | 202 ms: 1.01x slower                                                            |
| docutils                   | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                                          |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.01x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 107 ms: 1.01x slower                                                            |
| sympy_expand               | 373 ms                                                          | 377 ms: 1.01x slower                                                            |
| sphinx                     | 719 ms                                                          | 727 ms: 1.01x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 139 us: 1.01x slower                                                            |
| sympy_str                  | 212 ms                                                          | 215 ms: 1.01x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 92.1 ms: 1.02x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 42.3 ms: 1.02x slower                                                           |
| fannkuch                   | 299 ms                                                          | 305 ms: 1.02x slower                                                            |
| sympy_integrate            | 15.0 ms                                                         | 15.4 ms: 1.03x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 50.5 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.9 ms: 1.04x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 59.2 ms: 1.04x slower                                                           |
| regex_compile              | 101 ms                                                          | 105 ms: 1.04x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.69 sec: 1.04x slower                                                          |
| coroutines                 | 16.2 ms                                                         | 17.0 ms: 1.05x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.80 sec: 1.05x slower                                                          |
| spectral_norm              | 69.4 ms                                                         | 72.9 ms: 1.05x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.30 ms: 1.05x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.06 ms: 1.06x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.50 ms: 1.06x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 170 us: 1.06x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 80.6 ms: 1.08x slower                                                           |
| nbody                      | 80.0 ms                                                         | 86.7 ms: 1.08x slower                                                           |
| django_template            | 29.8 ms                                                         | 32.5 ms: 1.09x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 65.7 ms: 1.09x slower                                                           |
| pyflate                    | 320 ms                                                          | 349 ms: 1.09x slower                                                            |
| xml_etree_process          | 44.2 ms                                                         | 48.3 ms: 1.09x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.3 ms: 1.10x slower                                                           |
| async_generators           | 270 ms                                                          | 296 ms: 1.10x slower                                                            |
| chaos                      | 50.2 ms                                                         | 55.2 ms: 1.10x slower                                                           |
| generators                 | 21.8 ms                                                         | 23.9 ms: 1.10x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 79.4 ms: 1.10x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.9 us: 1.11x slower                                                           |
| float                      | 54.6 ms                                                         | 60.8 ms: 1.11x slower                                                           |
| scimark_fft                | 205 ms                                                          | 229 ms: 1.12x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 5.01 ms: 1.13x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.65 ms: 1.14x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.23 ms: 1.14x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.9 ms: 1.16x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 55.7 ms: 1.17x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.57 ms: 1.17x slower                                                           |
| richards_super             | 36.7 ms                                                         | 43.4 ms: 1.18x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 274 us: 1.19x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 102 ms: 1.19x slower                                                            |
| raytrace                   | 201 ms                                                          | 239 ms: 1.19x slower                                                            |
| many_optionals             | 436 us                                                          | 525 us: 1.20x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 73.1 ns: 1.21x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 20.8 ms: 1.41x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): sqlite_synth, pprint_pformat
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.034x faster

# HPT report

- Reliability score: 86.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown