# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-x86
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.010x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 259 ms: 1.04x slower                                                                      |
| docutils       | 1.78 sec                                                        | 1.91 sec: 1.08x slower                                                                    |
| html5lib       | 47.5 ms                                                         | 45.8 ms: 1.04x faster                                                                     |
| sphinx         | 719 ms                                                          | 756 ms: 1.05x slower                                                                      |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                                      |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                                      |
| async_tree_io              | 526 ms                                                          | 466 ms: 1.13x faster                                                                      |
| async_tree_none_tg         | 214 ms                                                          | 194 ms: 1.11x faster                                                                      |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                                      |
| async_tree_memoization     | 297 ms                                                          | 273 ms: 1.09x faster                                                                      |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                                      |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 472 ms: 1.03x faster                                                                      |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 452 ms: 1.01x faster                                                                      |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.06x slower                                                                     |
| async_generators           | 270 ms                                                          | 294 ms: 1.09x slower                                                                      |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                                      |
| float          | 54.6 ms                                                         | 56.9 ms: 1.04x slower                                                                     |
| nbody          | 80.0 ms                                                         | 98.2 ms: 1.23x slower                                                                     |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                                     |
| regex_v8       | 16.8 ms                                                         | 15.5 ms: 1.08x faster                                                                     |
| regex_compile  | 101 ms                                                          | 110 ms: 1.09x slower                                                                      |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 20.7 us: 1.04x faster                                                                     |
| tomli_loads          | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                                    |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                                     |
| xml_etree_generate   | 61.4 ms                                                         | 71.9 ms: 1.17x slower                                                                     |
| xml_etree_process    | 44.2 ms                                                         | 53.5 ms: 1.21x slower                                                                     |
| json_dumps           | 7.30 ms                                                         | 9.00 ms: 1.23x slower                                                                     |
| unpickle_pure_python | 160 us                                                          | 206 us: 1.29x slower                                                                      |
| pickle_pure_python   | 231 us                                                          | 303 us: 1.31x slower                                                                      |
| Geometric mean       | (ref)                                                           | 1.13x slower                                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| python_startup | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                                     |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                              |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 51.5 ms: 1.03x slower                                                                     |
| mako            | 7.09 ms                                                         | 7.49 ms: 1.06x slower                                                                     |
| django_template | 29.8 ms                                                         | 33.9 ms: 1.14x slower                                                                     |
| genshi_text     | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                                     |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------:|:-----------------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 776 us: 12.85x faster                                                                     |
| coverage                   | 324 ms                                                          | 51.6 ms: 6.28x faster                                                                     |
| sqlglot_normalize          | 216 ms                                                          | 105 ms: 2.07x faster                                                                      |
| deepcopy                   | 314 us                                                          | 230 us: 1.36x faster                                                                      |
| deepcopy_memo              | 25.4 us                                                         | 21.0 us: 1.21x faster                                                                     |
| deepcopy_reduce            | 2.92 us                                                         | 2.44 us: 1.19x faster                                                                     |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                                                     |
| async_tree_memoization_tg  | 282 ms                                                          | 249 ms: 1.13x faster                                                                      |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.13x faster                                                                      |
| async_tree_io              | 526 ms                                                          | 466 ms: 1.13x faster                                                                      |
| async_tree_none_tg         | 214 ms                                                          | 194 ms: 1.11x faster                                                                      |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                                      |
| async_tree_memoization     | 297 ms                                                          | 273 ms: 1.09x faster                                                                      |
| python_startup             | 28.3 ms                                                         | 26.1 ms: 1.09x faster                                                                     |
| regex_v8                   | 16.8 ms                                                         | 15.5 ms: 1.08x faster                                                                     |
| go                         | 109 ms                                                          | 104 ms: 1.05x faster                                                                      |
| json_loads                 | 21.6 us                                                         | 20.7 us: 1.04x faster                                                                     |
| asyncio_websockets         | 363 ms                                                          | 348 ms: 1.04x faster                                                                      |
| bench_mp_pool              | 90.6 ms                                                         | 87.1 ms: 1.04x faster                                                                     |
| html5lib                   | 47.5 ms                                                         | 45.8 ms: 1.04x faster                                                                     |
| dulwich_log                | 48.8 ms                                                         | 47.0 ms: 1.04x faster                                                                     |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 472 ms: 1.03x faster                                                                      |
| sqlite_synth               | 1.95 us                                                         | 1.93 us: 1.01x faster                                                                     |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 452 ms: 1.01x faster                                                                      |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                                      |
| logging_format             | 8.72 us                                                         | 8.83 us: 1.01x slower                                                                     |
| pathlib                    | 82.9 ms                                                         | 84.2 ms: 1.02x slower                                                                     |
| bench_thread_pool          | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                                                     |
| telco                      | 6.96 ms                                                         | 7.12 ms: 1.02x slower                                                                     |
| genshi_xml                 | 50.1 ms                                                         | 51.5 ms: 1.03x slower                                                                     |
| gc_traversal               | 1.75 ms                                                         | 1.80 ms: 1.03x slower                                                                     |
| logging_simple             | 7.99 us                                                         | 8.22 us: 1.03x slower                                                                     |
| spectral_norm              | 69.4 ms                                                         | 71.9 ms: 1.04x slower                                                                     |
| 2to3                       | 250 ms                                                          | 259 ms: 1.04x slower                                                                      |
| sympy_expand               | 373 ms                                                          | 388 ms: 1.04x slower                                                                      |
| float                      | 54.6 ms                                                         | 56.9 ms: 1.04x slower                                                                     |
| tomli_loads                | 1.71 sec                                                        | 1.79 sec: 1.04x slower                                                                    |
| sympy_sum                  | 106 ms                                                          | 110 ms: 1.04x slower                                                                      |
| pycparser                  | 872 ms                                                          | 912 ms: 1.05x slower                                                                      |
| sphinx                     | 719 ms                                                          | 756 ms: 1.05x slower                                                                      |
| sympy_str                  | 212 ms                                                          | 223 ms: 1.05x slower                                                                      |
| mako                       | 7.09 ms                                                         | 7.49 ms: 1.06x slower                                                                     |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.4 ms: 1.06x slower                                                                     |
| connected_components       | 267 ms                                                          | 283 ms: 1.06x slower                                                                      |
| coroutines                 | 16.2 ms                                                         | 17.3 ms: 1.06x slower                                                                     |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.02 ms: 1.06x slower                                                                     |
| docutils                   | 1.78 sec                                                        | 1.91 sec: 1.08x slower                                                                    |
| shortest_path              | 290 ms                                                          | 312 ms: 1.08x slower                                                                      |
| mdp                        | 1.62 sec                                                        | 1.75 sec: 1.08x slower                                                                    |
| async_generators           | 270 ms                                                          | 294 ms: 1.09x slower                                                                      |
| regex_compile              | 101 ms                                                          | 110 ms: 1.09x slower                                                                      |
| pyflate                    | 320 ms                                                          | 350 ms: 1.09x slower                                                                      |
| sympy_integrate            | 15.0 ms                                                         | 16.5 ms: 1.10x slower                                                                     |
| bpe_tokeniser              | 3.46 sec                                                        | 3.87 sec: 1.12x slower                                                                    |
| pprint_safe_repr           | 648 ms                                                          | 736 ms: 1.14x slower                                                                      |
| scimark_sor                | 85.9 ms                                                         | 97.8 ms: 1.14x slower                                                                     |
| django_template            | 29.8 ms                                                         | 33.9 ms: 1.14x slower                                                                     |
| pprint_pformat             | 1.33 sec                                                        | 1.52 sec: 1.14x slower                                                                    |
| genshi_text                | 21.5 ms                                                         | 24.7 ms: 1.15x slower                                                                     |
| deltablue                  | 2.33 ms                                                         | 2.69 ms: 1.15x slower                                                                     |
| fannkuch                   | 299 ms                                                          | 346 ms: 1.16x slower                                                                      |
| scimark_lu                 | 60.2 ms                                                         | 70.1 ms: 1.16x slower                                                                     |
| sqlglot_transpile          | 1.24 ms                                                         | 1.45 ms: 1.17x slower                                                                     |
| sqlglot_parse              | 1.00 ms                                                         | 1.17 ms: 1.17x slower                                                                     |
| xml_etree_generate         | 61.4 ms                                                         | 71.9 ms: 1.17x slower                                                                     |
| meteor_contest             | 74.6 ms                                                         | 87.5 ms: 1.17x slower                                                                     |
| richards_super             | 36.7 ms                                                         | 43.6 ms: 1.19x slower                                                                     |
| scimark_fft                | 205 ms                                                          | 245 ms: 1.20x slower                                                                      |
| nqueens                    | 72.1 ms                                                         | 86.5 ms: 1.20x slower                                                                     |
| raytrace                   | 201 ms                                                          | 242 ms: 1.20x slower                                                                      |
| hexiom                     | 4.44 ms                                                         | 5.36 ms: 1.21x slower                                                                     |
| generators                 | 21.8 ms                                                         | 26.3 ms: 1.21x slower                                                                     |
| crypto_pyaes               | 56.9 ms                                                         | 68.9 ms: 1.21x slower                                                                     |
| xml_etree_process          | 44.2 ms                                                         | 53.5 ms: 1.21x slower                                                                     |
| richards                   | 32.7 ms                                                         | 39.6 ms: 1.21x slower                                                                     |
| typing_runtime_protocols   | 138 us                                                          | 167 us: 1.21x slower                                                                      |
| nbody                      | 80.0 ms                                                         | 98.2 ms: 1.23x slower                                                                     |
| json_dumps                 | 7.30 ms                                                         | 9.00 ms: 1.23x slower                                                                     |
| sqlglot_optimize           | 41.4 ms                                                         | 51.2 ms: 1.24x slower                                                                     |
| chaos                      | 50.2 ms                                                         | 62.6 ms: 1.25x slower                                                                     |
| logging_silent             | 60.3 ns                                                         | 75.6 ns: 1.25x slower                                                                     |
| scimark_monte_carlo        | 47.7 ms                                                         | 60.8 ms: 1.28x slower                                                                     |
| unpickle_pure_python       | 160 us                                                          | 206 us: 1.29x slower                                                                      |
| many_optionals             | 436 us                                                          | 563 us: 1.29x slower                                                                      |
| pickle_pure_python         | 231 us                                                          | 303 us: 1.31x slower                                                                      |
| comprehensions             | 12.5 us                                                         | 16.7 us: 1.34x slower                                                                     |
| subparsers                 | 14.8 ms                                                         | 21.5 ms: 1.45x slower                                                                     |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                                              |

Benchmark hidden because not significant (7): create_gc_cycles, python_startup_no_site, json, xml_etree_parse, regex_dna, pylint, k_core
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1_win32-x86-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: mypy2

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown