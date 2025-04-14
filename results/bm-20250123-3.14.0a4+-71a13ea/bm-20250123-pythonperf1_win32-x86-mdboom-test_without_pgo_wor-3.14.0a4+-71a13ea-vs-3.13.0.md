# Results vs. 3.13.0

- fork: mdboom
- ref: test_without_pgo_wor
- machine: windows-x86
- commit hash: 71a13ea
- commit date: 2025-01-23
- overall geometric mean: 1.001x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 256 ms: 1.02x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                          |
| sphinx         | 719 ms                                                          | 754 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 212 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 244 ms: 1.16x faster                                                            |
| async_tree_io              | 526 ms                                                          | 459 ms: 1.15x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 261 ms: 1.13x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 192 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 461 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 450 ms: 1.01x faster                                                            |
| coroutines                 | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                                           |
| async_generators           | 270 ms                                                          | 311 ms: 1.15x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| float          | 54.6 ms                                                         | 57.8 ms: 1.06x slower                                                           |
| nbody          | 80.0 ms                                                         | 89.4 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| regex_dna      | 114 ms                                                          | 113 ms: 1.01x faster                                                            |
| regex_compile  | 101 ms                                                          | 106 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.69 sec: 1.02x faster                                                          |
| json_loads           | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.9 ms: 1.07x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 185 us: 1.15x slower                                                            |
| xml_etree_process    | 44.2 ms                                                         | 52.4 ms: 1.18x slower                                                           |
| pickle_pure_python   | 231 us                                                          | 281 us: 1.22x slower                                                            |
| json_dumps           | 7.30 ms                                                         | 9.25 ms: 1.27x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 48.7 ms: 1.03x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 22.1 ms: 1.03x slower                                                           |
| mako            | 7.09 ms                                                         | 7.68 ms: 1.08x slower                                                           |
| django_template | 29.8 ms                                                         | 33.7 ms: 1.13x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-test_without_pgo_wor-3.14.0a4+-71a13ea |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 770 us: 12.96x faster                                                           |
| coverage                   | 324 ms                                                          | 53.1 ms: 6.10x faster                                                           |
| deepcopy                   | 314 us                                                          | 250 us: 1.26x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.55 ms: 1.16x faster                                                           |
| deepcopy_memo              | 25.4 us                                                         | 21.9 us: 1.16x faster                                                           |
| async_tree_none            | 245 ms                                                          | 212 ms: 1.16x faster                                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 244 ms: 1.16x faster                                                            |
| async_tree_io              | 526 ms                                                          | 459 ms: 1.15x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 261 ms: 1.13x faster                                                            |
| deepcopy_reduce            | 2.92 us                                                         | 2.61 us: 1.12x faster                                                           |
| async_tree_none_tg         | 214 ms                                                          | 192 ms: 1.11x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                            |
| go                         | 109 ms                                                          | 101 ms: 1.07x faster                                                            |
| python_startup             | 28.3 ms                                                         | 26.7 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 461 ms: 1.05x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                            |
| connected_components       | 267 ms                                                          | 258 ms: 1.03x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 48.7 ms: 1.03x faster                                                           |
| sqlite_synth               | 1.95 us                                                         | 1.91 us: 1.02x faster                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.69 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 450 ms: 1.01x faster                                                            |
| create_gc_cycles           | 1.06 ms                                                         | 1.05 ms: 1.01x faster                                                           |
| pycparser                  | 872 ms                                                          | 864 ms: 1.01x faster                                                            |
| regex_dna                  | 114 ms                                                          | 113 ms: 1.01x faster                                                            |
| pidigits                   | 201 ms                                                          | 200 ms: 1.01x faster                                                            |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.45 sec: 1.00x faster                                                          |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.78 ms: 1.02x slower                                                           |
| fannkuch                   | 299 ms                                                          | 305 ms: 1.02x slower                                                            |
| 2to3                       | 250 ms                                                          | 256 ms: 1.02x slower                                                            |
| telco                      | 6.96 ms                                                         | 7.13 ms: 1.02x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 22.1 ms: 1.03x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.03 ms: 1.03x slower                                                           |
| python_startup_no_site     | 19.7 ms                                                         | 20.3 ms: 1.03x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 672 ms: 1.04x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 72.0 ms: 1.04x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.05 us: 1.04x slower                                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.38 sec: 1.04x slower                                                          |
| docutils                   | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                          |
| pathlib                    | 82.9 ms                                                         | 86.7 ms: 1.05x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.37 us: 1.05x slower                                                           |
| sphinx                     | 719 ms                                                          | 754 ms: 1.05x slower                                                            |
| bench_mp_pool              | 90.6 ms                                                         | 95.1 ms: 1.05x slower                                                           |
| regex_compile              | 101 ms                                                          | 106 ms: 1.05x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 111 ms: 1.05x slower                                                            |
| mdp                        | 1.62 sec                                                        | 1.71 sec: 1.05x slower                                                          |
| float                      | 54.6 ms                                                         | 57.8 ms: 1.06x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.01 ms: 1.06x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                           |
| sympy_str                  | 212 ms                                                          | 226 ms: 1.07x slower                                                            |
| pyflate                    | 320 ms                                                          | 341 ms: 1.07x slower                                                            |
| scimark_fft                | 205 ms                                                          | 219 ms: 1.07x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.9 ms: 1.07x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.32 ms: 1.07x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 52.2 ms: 1.07x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.08 ms: 1.07x slower                                                           |
| sympy_expand               | 373 ms                                                          | 402 ms: 1.08x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 44.9 ms: 1.08x slower                                                           |
| sqlglot_normalize          | 216 ms                                                          | 235 ms: 1.08x slower                                                            |
| mako                       | 7.09 ms                                                         | 7.68 ms: 1.08x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 17.6 ms: 1.09x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 62.0 ms: 1.09x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.1 ms: 1.09x slower                                                           |
| meteor_contest             | 74.6 ms                                                         | 82.0 ms: 1.10x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 79.5 ms: 1.10x slower                                                           |
| nbody                      | 80.0 ms                                                         | 89.4 ms: 1.12x slower                                                           |
| chaos                      | 50.2 ms                                                         | 56.4 ms: 1.12x slower                                                           |
| django_template            | 29.8 ms                                                         | 33.7 ms: 1.13x slower                                                           |
| json                       | 4.27 ms                                                         | 4.86 ms: 1.14x slower                                                           |
| async_generators           | 270 ms                                                          | 311 ms: 1.15x slower                                                            |
| unpickle_pure_python       | 160 us                                                          | 185 us: 1.15x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 160 us: 1.16x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 5.18 ms: 1.17x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 56.2 ms: 1.18x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.75 ms: 1.18x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 52.4 ms: 1.18x slower                                                           |
| comprehensions             | 12.5 us                                                         | 14.9 us: 1.19x slower                                                           |
| generators                 | 21.8 ms                                                         | 26.1 ms: 1.20x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 104 ms: 1.21x slower                                                            |
| pickle_pure_python         | 231 us                                                          | 281 us: 1.22x slower                                                            |
| richards                   | 32.7 ms                                                         | 39.9 ms: 1.22x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 74.6 ms: 1.24x slower                                                           |
| richards_super             | 36.7 ms                                                         | 45.5 ms: 1.24x slower                                                           |
| many_optionals             | 436 us                                                          | 548 us: 1.26x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 76.4 ns: 1.27x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 9.25 ms: 1.27x slower                                                           |
| raytrace                   | 201 ms                                                          | 281 ms: 1.39x slower                                                            |
| subparsers                 | 14.8 ms                                                         | 21.2 ms: 1.44x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                                    |

Benchmark hidden because not significant (5): regex_v8, pylint, html5lib, k_core, shortest_path
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown