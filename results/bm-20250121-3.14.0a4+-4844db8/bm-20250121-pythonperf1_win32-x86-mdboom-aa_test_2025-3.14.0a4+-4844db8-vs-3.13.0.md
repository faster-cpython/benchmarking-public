# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025
- machine: windows-x86
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.003x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 256 ms: 1.02x slower                                                    |
| docutils       | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                  |
| html5lib       | 47.5 ms                                                         | 48.5 ms: 1.02x slower                                                   |
| sphinx         | 719 ms                                                          | 757 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                           | 1.04x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 463 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                    |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                    |
| async_tree_memoization     | 297 ms                                                          | 267 ms: 1.11x faster                                                    |
| async_tree_io_tg           | 494 ms                                                          | 452 ms: 1.09x faster                                                    |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 456 ms: 1.06x faster                                                    |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 440 ms: 1.04x faster                                                    |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.06x slower                                                   |
| async_generators           | 270 ms                                                          | 300 ms: 1.11x slower                                                    |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.00x slower                                                    |
| float          | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                   |
| nbody          | 80.0 ms                                                         | 90.0 ms: 1.13x slower                                                   |
| Geometric mean | (ref)                                                           | 1.05x slower                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                   |
| regex_v8       | 16.8 ms                                                         | 15.5 ms: 1.09x faster                                                   |
| regex_dna      | 114 ms                                                          | 117 ms: 1.03x slower                                                    |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                           | 1.03x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 21.4 us: 1.01x faster                                                   |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                    |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                   |
| xml_etree_generate   | 61.4 ms                                                         | 67.9 ms: 1.10x slower                                                   |
| xml_etree_process    | 44.2 ms                                                         | 50.9 ms: 1.15x slower                                                   |
| unpickle_pure_python | 160 us                                                          | 185 us: 1.16x slower                                                    |
| pickle_pure_python   | 231 us                                                          | 286 us: 1.24x slower                                                    |
| json_dumps           | 7.30 ms                                                         | 9.40 ms: 1.29x slower                                                   |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                            |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                   |
| python_startup_no_site | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 46.2 ms: 1.09x faster                                                   |
| mako            | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                   |
| django_template | 29.8 ms                                                         | 33.4 ms: 1.12x slower                                                   |
| Geometric mean  | (ref)                                                           | 1.03x slower                                                            |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250121-pythonperf1_win32-x86-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 762 us: 13.09x faster                                                   |
| coverage                   | 324 ms                                                          | 54.4 ms: 5.96x faster                                                   |
| deepcopy                   | 314 us                                                          | 235 us: 1.34x faster                                                    |
| deepcopy_memo              | 25.4 us                                                         | 21.5 us: 1.18x faster                                                   |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                   |
| async_tree_io              | 526 ms                                                          | 463 ms: 1.14x faster                                                    |
| deepcopy_reduce            | 2.92 us                                                         | 2.57 us: 1.14x faster                                                   |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                    |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                    |
| async_tree_memoization     | 297 ms                                                          | 267 ms: 1.11x faster                                                    |
| go                         | 109 ms                                                          | 98.5 ms: 1.10x faster                                                   |
| async_tree_io_tg           | 494 ms                                                          | 452 ms: 1.09x faster                                                    |
| regex_v8                   | 16.8 ms                                                         | 15.5 ms: 1.09x faster                                                   |
| genshi_xml                 | 50.1 ms                                                         | 46.2 ms: 1.09x faster                                                   |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 456 ms: 1.06x faster                                                    |
| python_startup             | 28.3 ms                                                         | 27.0 ms: 1.05x faster                                                   |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 440 ms: 1.04x faster                                                    |
| connected_components       | 267 ms                                                          | 258 ms: 1.03x faster                                                    |
| telco                      | 6.96 ms                                                         | 6.84 ms: 1.02x faster                                                   |
| json_loads                 | 21.6 us                                                         | 21.4 us: 1.01x faster                                                   |
| sqlite_synth               | 1.95 us                                                         | 1.94 us: 1.01x faster                                                   |
| pidigits                   | 201 ms                                                          | 202 ms: 1.00x slower                                                    |
| fannkuch                   | 299 ms                                                          | 300 ms: 1.01x slower                                                    |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                    |
| logging_format             | 8.72 us                                                         | 8.85 us: 1.02x slower                                                   |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                   |
| html5lib                   | 47.5 ms                                                         | 48.5 ms: 1.02x slower                                                   |
| python_startup_no_site     | 19.7 ms                                                         | 20.1 ms: 1.02x slower                                                   |
| 2to3                       | 250 ms                                                          | 256 ms: 1.02x slower                                                    |
| bpe_tokeniser              | 3.46 sec                                                        | 3.55 sec: 1.02x slower                                                  |
| pprint_pformat             | 1.33 sec                                                        | 1.36 sec: 1.03x slower                                                  |
| regex_dna                  | 114 ms                                                          | 117 ms: 1.03x slower                                                    |
| logging_simple             | 7.99 us                                                         | 8.23 us: 1.03x slower                                                   |
| float                      | 54.6 ms                                                         | 56.5 ms: 1.03x slower                                                   |
| spectral_norm              | 69.4 ms                                                         | 72.0 ms: 1.04x slower                                                   |
| bench_thread_pool          | 1.00 ms                                                         | 1.04 ms: 1.04x slower                                                   |
| sqlglot_normalize          | 216 ms                                                          | 225 ms: 1.04x slower                                                    |
| bench_mp_pool              | 90.6 ms                                                         | 94.7 ms: 1.05x slower                                                   |
| docutils                   | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                  |
| sqlglot_optimize           | 41.4 ms                                                         | 43.5 ms: 1.05x slower                                                   |
| sphinx                     | 719 ms                                                          | 757 ms: 1.05x slower                                                    |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                  |
| sympy_sum                  | 106 ms                                                          | 112 ms: 1.06x slower                                                    |
| pathlib                    | 82.9 ms                                                         | 87.8 ms: 1.06x slower                                                   |
| sympy_str                  | 212 ms                                                          | 224 ms: 1.06x slower                                                    |
| sympy_integrate            | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                   |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                    |
| pyflate                    | 320 ms                                                          | 340 ms: 1.06x slower                                                    |
| sympy_expand               | 373 ms                                                          | 397 ms: 1.06x slower                                                    |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.06x slower                                                   |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.8 ms: 1.07x slower                                                   |
| sqlglot_transpile          | 1.24 ms                                                         | 1.33 ms: 1.07x slower                                                   |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.06 ms: 1.08x slower                                                   |
| dulwich_log                | 48.8 ms                                                         | 52.6 ms: 1.08x slower                                                   |
| sqlglot_parse              | 1.00 ms                                                         | 1.08 ms: 1.08x slower                                                   |
| mako                       | 7.09 ms                                                         | 7.69 ms: 1.09x slower                                                   |
| json                       | 4.27 ms                                                         | 4.65 ms: 1.09x slower                                                   |
| nqueens                    | 72.1 ms                                                         | 78.6 ms: 1.09x slower                                                   |
| meteor_contest             | 74.6 ms                                                         | 81.7 ms: 1.09x slower                                                   |
| xml_etree_generate         | 61.4 ms                                                         | 67.9 ms: 1.10x slower                                                   |
| crypto_pyaes               | 56.9 ms                                                         | 63.0 ms: 1.11x slower                                                   |
| async_generators           | 270 ms                                                          | 300 ms: 1.11x slower                                                    |
| scimark_fft                | 205 ms                                                          | 228 ms: 1.11x slower                                                    |
| django_template            | 29.8 ms                                                         | 33.4 ms: 1.12x slower                                                   |
| nbody                      | 80.0 ms                                                         | 90.0 ms: 1.13x slower                                                   |
| chaos                      | 50.2 ms                                                         | 56.6 ms: 1.13x slower                                                   |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.1 ms: 1.14x slower                                                   |
| typing_runtime_protocols   | 138 us                                                          | 157 us: 1.14x slower                                                    |
| xml_etree_process          | 44.2 ms                                                         | 50.9 ms: 1.15x slower                                                   |
| unpickle_pure_python       | 160 us                                                          | 185 us: 1.16x slower                                                    |
| deltablue                  | 2.33 ms                                                         | 2.70 ms: 1.16x slower                                                   |
| scimark_sor                | 85.9 ms                                                         | 99.7 ms: 1.16x slower                                                   |
| richards                   | 32.7 ms                                                         | 38.0 ms: 1.16x slower                                                   |
| comprehensions             | 12.5 us                                                         | 14.6 us: 1.17x slower                                                   |
| hexiom                     | 4.44 ms                                                         | 5.21 ms: 1.17x slower                                                   |
| generators                 | 21.8 ms                                                         | 25.7 ms: 1.18x slower                                                   |
| richards_super             | 36.7 ms                                                         | 43.6 ms: 1.19x slower                                                   |
| logging_silent             | 60.3 ns                                                         | 74.6 ns: 1.24x slower                                                   |
| pickle_pure_python         | 231 us                                                          | 286 us: 1.24x slower                                                    |
| scimark_lu                 | 60.2 ms                                                         | 75.2 ms: 1.25x slower                                                   |
| many_optionals             | 436 us                                                          | 545 us: 1.25x slower                                                    |
| json_dumps                 | 7.30 ms                                                         | 9.40 ms: 1.29x slower                                                   |
| raytrace                   | 201 ms                                                          | 280 ms: 1.39x slower                                                    |
| subparsers                 | 14.8 ms                                                         | 21.4 ms: 1.45x slower                                                   |
| Geometric mean             | (ref)                                                           | 1.00x faster                                                            |

Benchmark hidden because not significant (8): pycparser, pylint, shortest_path, tomli_loads, genshi_text, pprint_safe_repr, create_gc_cycles, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown