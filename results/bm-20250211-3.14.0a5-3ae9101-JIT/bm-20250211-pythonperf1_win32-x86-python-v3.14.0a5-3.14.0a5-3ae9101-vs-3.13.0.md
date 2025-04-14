# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a5
- machine: windows-x86
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.042x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 269 ms: 1.08x slower                                                |
| docutils       | 1.78 sec                                                        | 2.03 sec: 1.14x slower                                              |
| html5lib       | 47.5 ms                                                         | 49.0 ms: 1.03x slower                                               |
| sphinx         | 719 ms                                                          | 774 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                           | 1.08x slower                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 489 ms: 1.08x faster                                                |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                |
| async_tree_memoization_tg  | 282 ms                                                          | 273 ms: 1.03x faster                                                |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                |
| coroutines                 | 16.2 ms                                                         | 15.8 ms: 1.02x faster                                               |
| async_tree_none_tg         | 214 ms                                                          | 217 ms: 1.01x slower                                                |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 506 ms: 1.05x slower                                                |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 494 ms: 1.08x slower                                                |
| async_generators           | 270 ms                                                          | 334 ms: 1.24x slower                                                |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                        |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 54.6 ms                                                         | 53.9 ms: 1.01x faster                                               |
| pidigits       | 201 ms                                                          | 201 ms: 1.00x slower                                                |
| nbody          | 80.0 ms                                                         | 110 ms: 1.38x slower                                                |
| Geometric mean | (ref)                                                           | 1.11x slower                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                               |
| regex_v8       | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                               |
| regex_dna      | 114 ms                                                          | 119 ms: 1.04x slower                                                |
| regex_compile  | 101 ms                                                          | 119 ms: 1.18x slower                                                |
| Geometric mean | (ref)                                                           | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 22.8 us: 1.05x slower                                               |
| tomli_loads          | 1.71 sec                                                        | 1.85 sec: 1.08x slower                                              |
| xml_etree_iterparse  | 62.6 ms                                                         | 68.8 ms: 1.10x slower                                               |
| xml_etree_generate   | 61.4 ms                                                         | 75.0 ms: 1.22x slower                                               |
| json_dumps           | 7.30 ms                                                         | 9.18 ms: 1.26x slower                                               |
| xml_etree_process    | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                               |
| pickle_pure_python   | 231 us                                                          | 327 us: 1.41x slower                                                |
| unpickle_pure_python | 160 us                                                          | 227 us: 1.42x slower                                                |
| Geometric mean       | (ref)                                                           | 1.19x slower                                                        |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                         | 21.6 ms: 1.10x slower                                               |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                        |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.91 ms: 1.12x slower                                               |
| genshi_text     | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                               |
| django_template | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                               |
| Geometric mean  | (ref)                                                           | 1.12x slower                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250211-pythonperf1_win32-x86-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 768 us: 12.99x faster                                               |
| coverage                   | 324 ms                                                          | 55.9 ms: 5.80x faster                                               |
| pathlib                    | 82.9 ms                                                         | 35.0 ms: 2.37x faster                                               |
| sqlglot_normalize          | 216 ms                                                          | 108 ms: 2.01x faster                                                |
| deepcopy                   | 314 us                                                          | 258 us: 1.22x faster                                                |
| deepcopy_memo              | 25.4 us                                                         | 21.3 us: 1.20x faster                                               |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                               |
| regex_v8                   | 16.8 ms                                                         | 15.6 ms: 1.08x faster                                               |
| async_tree_io              | 526 ms                                                          | 489 ms: 1.08x faster                                                |
| deepcopy_reduce            | 2.92 us                                                         | 2.74 us: 1.07x faster                                               |
| spectral_norm              | 69.4 ms                                                         | 65.5 ms: 1.06x faster                                               |
| async_tree_none            | 245 ms                                                          | 233 ms: 1.05x faster                                                |
| async_tree_memoization     | 297 ms                                                          | 285 ms: 1.04x faster                                                |
| sqlite_synth               | 1.95 us                                                         | 1.88 us: 1.04x faster                                               |
| async_tree_memoization_tg  | 282 ms                                                          | 273 ms: 1.03x faster                                                |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                                |
| coroutines                 | 16.2 ms                                                         | 15.8 ms: 1.02x faster                                               |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.02x faster                                               |
| float                      | 54.6 ms                                                         | 53.9 ms: 1.01x faster                                               |
| bench_mp_pool              | 90.6 ms                                                         | 89.8 ms: 1.01x faster                                               |
| pidigits                   | 201 ms                                                          | 201 ms: 1.00x slower                                                |
| async_tree_none_tg         | 214 ms                                                          | 217 ms: 1.01x slower                                                |
| html5lib                   | 47.5 ms                                                         | 49.0 ms: 1.03x slower                                               |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                               |
| k_core                     | 1.38 sec                                                        | 1.43 sec: 1.04x slower                                              |
| regex_dna                  | 114 ms                                                          | 119 ms: 1.04x slower                                                |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 506 ms: 1.05x slower                                                |
| logging_simple             | 7.99 us                                                         | 8.39 us: 1.05x slower                                               |
| json_loads                 | 21.6 us                                                         | 22.8 us: 1.05x slower                                               |
| logging_format             | 8.72 us                                                         | 9.24 us: 1.06x slower                                               |
| generators                 | 21.8 ms                                                         | 23.3 ms: 1.07x slower                                               |
| go                         | 109 ms                                                          | 117 ms: 1.07x slower                                                |
| 2to3                       | 250 ms                                                          | 269 ms: 1.08x slower                                                |
| sphinx                     | 719 ms                                                          | 774 ms: 1.08x slower                                                |
| tomli_loads                | 1.71 sec                                                        | 1.85 sec: 1.08x slower                                              |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 494 ms: 1.08x slower                                                |
| dulwich_log                | 48.8 ms                                                         | 52.8 ms: 1.08x slower                                               |
| telco                      | 6.96 ms                                                         | 7.55 ms: 1.08x slower                                               |
| pyflate                    | 320 ms                                                          | 348 ms: 1.09x slower                                                |
| json                       | 4.27 ms                                                         | 4.68 ms: 1.10x slower                                               |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.12 ms: 1.10x slower                                               |
| python_startup_no_site     | 19.7 ms                                                         | 21.6 ms: 1.10x slower                                               |
| xml_etree_iterparse        | 62.6 ms                                                         | 68.8 ms: 1.10x slower                                               |
| sympy_sum                  | 106 ms                                                          | 117 ms: 1.10x slower                                                |
| scimark_monte_carlo        | 47.7 ms                                                         | 52.8 ms: 1.11x slower                                               |
| mako                       | 7.09 ms                                                         | 7.91 ms: 1.12x slower                                               |
| pycparser                  | 872 ms                                                          | 974 ms: 1.12x slower                                                |
| connected_components       | 267 ms                                                          | 300 ms: 1.12x slower                                                |
| sympy_str                  | 212 ms                                                          | 238 ms: 1.12x slower                                                |
| genshi_text                | 21.5 ms                                                         | 24.3 ms: 1.13x slower                                               |
| sympy_expand               | 373 ms                                                          | 422 ms: 1.13x slower                                                |
| scimark_lu                 | 60.2 ms                                                         | 68.6 ms: 1.14x slower                                               |
| docutils                   | 1.78 sec                                                        | 2.03 sec: 1.14x slower                                              |
| mdp                        | 1.62 sec                                                        | 1.87 sec: 1.15x slower                                              |
| sympy_integrate            | 15.0 ms                                                         | 17.2 ms: 1.15x slower                                               |
| bpe_tokeniser              | 3.46 sec                                                        | 4.00 sec: 1.16x slower                                              |
| shortest_path              | 290 ms                                                          | 336 ms: 1.16x slower                                                |
| regex_compile              | 101 ms                                                          | 119 ms: 1.18x slower                                                |
| logging_silent             | 60.3 ns                                                         | 72.0 ns: 1.19x slower                                               |
| pprint_safe_repr           | 648 ms                                                          | 776 ms: 1.20x slower                                                |
| scimark_sor                | 85.9 ms                                                         | 103 ms: 1.20x slower                                                |
| pprint_pformat             | 1.33 sec                                                        | 1.60 sec: 1.20x slower                                              |
| sqlglot_transpile          | 1.24 ms                                                         | 1.49 ms: 1.21x slower                                               |
| sqlglot_parse              | 1.00 ms                                                         | 1.21 ms: 1.21x slower                                               |
| chaos                      | 50.2 ms                                                         | 61.3 ms: 1.22x slower                                               |
| xml_etree_generate         | 61.4 ms                                                         | 75.0 ms: 1.22x slower                                               |
| django_template            | 29.8 ms                                                         | 36.8 ms: 1.24x slower                                               |
| async_generators           | 270 ms                                                          | 334 ms: 1.24x slower                                                |
| deltablue                  | 2.33 ms                                                         | 2.89 ms: 1.24x slower                                               |
| typing_runtime_protocols   | 138 us                                                          | 171 us: 1.25x slower                                                |
| meteor_contest             | 74.6 ms                                                         | 93.2 ms: 1.25x slower                                               |
| sqlglot_optimize           | 41.4 ms                                                         | 51.8 ms: 1.25x slower                                               |
| scimark_fft                | 205 ms                                                          | 257 ms: 1.26x slower                                                |
| json_dumps                 | 7.30 ms                                                         | 9.18 ms: 1.26x slower                                               |
| richards                   | 32.7 ms                                                         | 41.3 ms: 1.26x slower                                               |
| xml_etree_process          | 44.2 ms                                                         | 55.9 ms: 1.27x slower                                               |
| fannkuch                   | 299 ms                                                          | 380 ms: 1.27x slower                                                |
| richards_super             | 36.7 ms                                                         | 47.0 ms: 1.28x slower                                               |
| many_optionals             | 436 us                                                          | 576 us: 1.32x slower                                                |
| raytrace                   | 201 ms                                                          | 268 ms: 1.33x slower                                                |
| comprehensions             | 12.5 us                                                         | 16.9 us: 1.35x slower                                               |
| bench_thread_pool          | 1.00 ms                                                         | 1.35 ms: 1.35x slower                                               |
| crypto_pyaes               | 56.9 ms                                                         | 76.8 ms: 1.35x slower                                               |
| nbody                      | 80.0 ms                                                         | 110 ms: 1.38x slower                                                |
| hexiom                     | 4.44 ms                                                         | 6.27 ms: 1.41x slower                                               |
| pickle_pure_python         | 231 us                                                          | 327 us: 1.41x slower                                                |
| unpickle_pure_python       | 160 us                                                          | 227 us: 1.42x slower                                                |
| nqueens                    | 72.1 ms                                                         | 104 ms: 1.44x slower                                                |
| subparsers                 | 14.8 ms                                                         | 22.6 ms: 1.53x slower                                               |
| Geometric mean             | (ref)                                                           | 1.05x slower                                                        |

Benchmark hidden because not significant (5): async_tree_io_tg, python_startup, xml_etree_parse, genshi_xml, pylint
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.042x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.08x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown