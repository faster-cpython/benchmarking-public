# Results vs. 3.13.0

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-x86
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.001x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 254 ms: 1.01x slower                                                      |
| docutils       | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                    |
| html5lib       | 47.5 ms                                                         | 46.9 ms: 1.01x faster                                                     |
| sphinx         | 719 ms                                                          | 756 ms: 1.05x slower                                                      |
| Geometric mean | (ref)                                                           | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 245 ms                                                          | 212 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 282 ms                                                          | 245 ms: 1.15x faster                                                      |
| async_tree_io              | 526 ms                                                          | 462 ms: 1.14x faster                                                      |
| async_tree_memoization     | 297 ms                                                          | 261 ms: 1.14x faster                                                      |
| async_tree_none_tg         | 214 ms                                                          | 194 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 494 ms                                                          | 451 ms: 1.10x faster                                                      |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 455 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 444 ms: 1.03x faster                                                      |
| asyncio_websockets         | 363 ms                                                          | 359 ms: 1.01x faster                                                      |
| coroutines                 | 16.2 ms                                                         | 16.9 ms: 1.04x slower                                                     |
| async_generators           | 270 ms                                                          | 303 ms: 1.12x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.01x slower                                                      |
| float          | 54.6 ms                                                         | 57.8 ms: 1.06x slower                                                     |
| nbody          | 80.0 ms                                                         | 87.3 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                           | 1.05x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                     |
| regex_compile  | 101 ms                                                          | 107 ms: 1.06x slower                                                      |
| regex_dna      | 114 ms                                                          | 123 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                           | 1.00x faster                                                              |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.66 sec: 1.04x faster                                                    |
| json_loads           | 21.6 us                                                         | 21.3 us: 1.02x faster                                                     |
| xml_etree_parse      | 107 ms                                                          | 108 ms: 1.01x slower                                                      |
| xml_etree_iterparse  | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                     |
| xml_etree_generate   | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                     |
| unpickle_pure_python | 160 us                                                          | 186 us: 1.16x slower                                                      |
| xml_etree_process    | 44.2 ms                                                         | 52.4 ms: 1.19x slower                                                     |
| pickle_pure_python   | 231 us                                                          | 286 us: 1.24x slower                                                      |
| json_dumps           | 7.30 ms                                                         | 9.41 ms: 1.29x slower                                                     |
| Geometric mean       | (ref)                                                           | 1.11x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                     |
| python_startup_no_site | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 46.4 ms: 1.08x faster                                                     |
| genshi_text     | 21.5 ms                                                         | 22.0 ms: 1.02x slower                                                     |
| mako            | 7.09 ms                                                         | 7.81 ms: 1.10x slower                                                     |
| django_template | 29.8 ms                                                         | 34.2 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                           | 1.05x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250123-pythonperf1_win32-x86-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 749 us: 13.32x faster                                                     |
| coverage                   | 324 ms                                                          | 53.8 ms: 6.02x faster                                                     |
| deepcopy                   | 314 us                                                          | 245 us: 1.28x faster                                                      |
| deepcopy_memo              | 25.4 us                                                         | 21.6 us: 1.18x faster                                                     |
| async_tree_none            | 245 ms                                                          | 212 ms: 1.16x faster                                                      |
| async_tree_memoization_tg  | 282 ms                                                          | 245 ms: 1.15x faster                                                      |
| async_tree_io              | 526 ms                                                          | 462 ms: 1.14x faster                                                      |
| async_tree_memoization     | 297 ms                                                          | 261 ms: 1.14x faster                                                      |
| regex_effbot               | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                     |
| deepcopy_reduce            | 2.92 us                                                         | 2.57 us: 1.13x faster                                                     |
| async_tree_none_tg         | 214 ms                                                          | 194 ms: 1.10x faster                                                      |
| async_tree_io_tg           | 494 ms                                                          | 451 ms: 1.10x faster                                                      |
| genshi_xml                 | 50.1 ms                                                         | 46.4 ms: 1.08x faster                                                     |
| go                         | 109 ms                                                          | 101 ms: 1.08x faster                                                      |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 455 ms: 1.06x faster                                                      |
| python_startup             | 28.3 ms                                                         | 26.8 ms: 1.06x faster                                                     |
| tomli_loads                | 1.71 sec                                                        | 1.66 sec: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 444 ms: 1.03x faster                                                      |
| connected_components       | 267 ms                                                          | 260 ms: 1.02x faster                                                      |
| json_loads                 | 21.6 us                                                         | 21.3 us: 1.02x faster                                                     |
| html5lib                   | 47.5 ms                                                         | 46.9 ms: 1.01x faster                                                     |
| shortest_path              | 290 ms                                                          | 286 ms: 1.01x faster                                                      |
| asyncio_websockets         | 363 ms                                                          | 359 ms: 1.01x faster                                                      |
| sqlite_synth               | 1.95 us                                                         | 1.94 us: 1.01x faster                                                     |
| pidigits                   | 201 ms                                                          | 202 ms: 1.01x slower                                                      |
| xml_etree_parse            | 107 ms                                                          | 108 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 3.46 sec                                                        | 3.50 sec: 1.01x slower                                                    |
| pprint_pformat             | 1.33 sec                                                        | 1.35 sec: 1.01x slower                                                    |
| 2to3                       | 250 ms                                                          | 254 ms: 1.01x slower                                                      |
| telco                      | 6.96 ms                                                         | 7.09 ms: 1.02x slower                                                     |
| python_startup_no_site     | 19.7 ms                                                         | 20.0 ms: 1.02x slower                                                     |
| bench_thread_pool          | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                     |
| gc_traversal               | 1.75 ms                                                         | 1.79 ms: 1.02x slower                                                     |
| genshi_text                | 21.5 ms                                                         | 22.0 ms: 1.02x slower                                                     |
| logging_format             | 8.72 us                                                         | 9.05 us: 1.04x slower                                                     |
| pathlib                    | 82.9 ms                                                         | 86.1 ms: 1.04x slower                                                     |
| coroutines                 | 16.2 ms                                                         | 16.9 ms: 1.04x slower                                                     |
| sympy_sum                  | 106 ms                                                          | 110 ms: 1.04x slower                                                      |
| spectral_norm              | 69.4 ms                                                         | 72.5 ms: 1.04x slower                                                     |
| docutils                   | 1.78 sec                                                        | 1.86 sec: 1.05x slower                                                    |
| bench_mp_pool              | 90.6 ms                                                         | 94.8 ms: 1.05x slower                                                     |
| sympy_str                  | 212 ms                                                          | 222 ms: 1.05x slower                                                      |
| sympy_expand               | 373 ms                                                          | 392 ms: 1.05x slower                                                      |
| sphinx                     | 719 ms                                                          | 756 ms: 1.05x slower                                                      |
| json                       | 4.27 ms                                                         | 4.50 ms: 1.05x slower                                                     |
| logging_simple             | 7.99 us                                                         | 8.42 us: 1.05x slower                                                     |
| regex_compile              | 101 ms                                                          | 107 ms: 1.06x slower                                                      |
| float                      | 54.6 ms                                                         | 57.8 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.01 ms: 1.06x slower                                                     |
| mdp                        | 1.62 sec                                                        | 1.72 sec: 1.06x slower                                                    |
| pyflate                    | 320 ms                                                          | 341 ms: 1.06x slower                                                      |
| sympy_integrate            | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                     |
| sqlglot_transpile          | 1.24 ms                                                         | 1.32 ms: 1.07x slower                                                     |
| sqlglot_parse              | 1.00 ms                                                         | 1.07 ms: 1.07x slower                                                     |
| dulwich_log                | 48.8 ms                                                         | 52.3 ms: 1.07x slower                                                     |
| sqlglot_optimize           | 41.4 ms                                                         | 44.5 ms: 1.07x slower                                                     |
| sqlglot_normalize          | 216 ms                                                          | 233 ms: 1.07x slower                                                      |
| xml_etree_iterparse        | 62.6 ms                                                         | 67.4 ms: 1.08x slower                                                     |
| regex_dna                  | 114 ms                                                          | 123 ms: 1.08x slower                                                      |
| nbody                      | 80.0 ms                                                         | 87.3 ms: 1.09x slower                                                     |
| crypto_pyaes               | 56.9 ms                                                         | 62.4 ms: 1.10x slower                                                     |
| mako                       | 7.09 ms                                                         | 7.81 ms: 1.10x slower                                                     |
| nqueens                    | 72.1 ms                                                         | 79.4 ms: 1.10x slower                                                     |
| meteor_contest             | 74.6 ms                                                         | 82.3 ms: 1.10x slower                                                     |
| scimark_fft                | 205 ms                                                          | 228 ms: 1.11x slower                                                      |
| async_generators           | 270 ms                                                          | 303 ms: 1.12x slower                                                      |
| xml_etree_generate         | 61.4 ms                                                         | 69.3 ms: 1.13x slower                                                     |
| django_template            | 29.8 ms                                                         | 34.2 ms: 1.15x slower                                                     |
| comprehensions             | 12.5 us                                                         | 14.4 us: 1.15x slower                                                     |
| typing_runtime_protocols   | 138 us                                                          | 159 us: 1.16x slower                                                      |
| deltablue                  | 2.33 ms                                                         | 2.71 ms: 1.16x slower                                                     |
| scimark_monte_carlo        | 47.7 ms                                                         | 55.3 ms: 1.16x slower                                                     |
| unpickle_pure_python       | 160 us                                                          | 186 us: 1.16x slower                                                      |
| chaos                      | 50.2 ms                                                         | 59.3 ms: 1.18x slower                                                     |
| hexiom                     | 4.44 ms                                                         | 5.25 ms: 1.18x slower                                                     |
| richards                   | 32.7 ms                                                         | 38.7 ms: 1.18x slower                                                     |
| richards_super             | 36.7 ms                                                         | 43.5 ms: 1.19x slower                                                     |
| xml_etree_process          | 44.2 ms                                                         | 52.4 ms: 1.19x slower                                                     |
| generators                 | 21.8 ms                                                         | 26.0 ms: 1.19x slower                                                     |
| scimark_sor                | 85.9 ms                                                         | 103 ms: 1.20x slower                                                      |
| logging_silent             | 60.3 ns                                                         | 74.5 ns: 1.23x slower                                                     |
| pickle_pure_python         | 231 us                                                          | 286 us: 1.24x slower                                                      |
| many_optionals             | 436 us                                                          | 540 us: 1.24x slower                                                      |
| scimark_lu                 | 60.2 ms                                                         | 74.9 ms: 1.24x slower                                                     |
| json_dumps                 | 7.30 ms                                                         | 9.41 ms: 1.29x slower                                                     |
| subparsers                 | 14.8 ms                                                         | 21.0 ms: 1.42x slower                                                     |
| raytrace                   | 201 ms                                                          | 293 ms: 1.45x slower                                                      |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                              |

Benchmark hidden because not significant (7): regex_v8, create_gc_cycles, pycparser, pylint, fannkuch, pprint_safe_repr, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown