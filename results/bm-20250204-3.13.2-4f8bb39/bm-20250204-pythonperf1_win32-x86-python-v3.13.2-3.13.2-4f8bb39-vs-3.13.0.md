# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: windows-x86
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.009x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 254 ms: 1.01x slower                                            |
| docutils       | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                          |
| sphinx         | 719 ms                                                          | 729 ms: 1.01x slower                                            |
| tornado_http   | 94.1 ms                                                         | 112 ms: 1.19x slower                                            |
| Geometric mean | (ref)                                                           | 1.04x slower                                                    |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                            |
| coroutines                 | 16.2 ms                                                         | 16.0 ms: 1.02x faster                                           |
| async_tree_none            | 245 ms                                                          | 248 ms: 1.01x slower                                            |
| async_tree_io              | 526 ms                                                          | 533 ms: 1.01x slower                                            |
| async_tree_none_tg         | 214 ms                                                          | 221 ms: 1.03x slower                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 292 ms: 1.03x slower                                            |
| async_tree_io_tg           | 494 ms                                                          | 521 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 516 ms: 1.07x slower                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 506 ms: 1.11x slower                                            |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                    |

Benchmark hidden because not significant (2): async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 80.0 ms                                                         | 79.1 ms: 1.01x faster                                           |
| float          | 54.6 ms                                                         | 54.1 ms: 1.01x faster                                           |
| pidigits       | 201 ms                                                          | 203 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                           | 1.00x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                           |
| regex_compile  | 101 ms                                                          | 103 ms: 1.02x slower                                            |
| regex_dna      | 114 ms                                                          | 128 ms: 1.13x slower                                            |
| Geometric mean | (ref)                                                           | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| tomli_loads          | 1.71 sec                                                        | 1.65 sec: 1.04x faster                                          |
| unpickle_pure_python | 160 us                                                          | 158 us: 1.01x faster                                            |
| pickle_pure_python   | 231 us                                                          | 234 us: 1.01x slower                                            |
| xml_etree_process    | 44.2 ms                                                         | 45.0 ms: 1.02x slower                                           |
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.02x slower                                            |
| xml_etree_generate   | 61.4 ms                                                         | 62.9 ms: 1.03x slower                                           |
| xml_etree_iterparse  | 62.6 ms                                                         | 64.7 ms: 1.03x slower                                           |
| Geometric mean       | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (2): json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 29.8 ms: 1.05x slower                                           |
| python_startup_no_site | 19.7 ms                                                         | 21.3 ms: 1.09x slower                                           |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 48.1 ms: 1.04x faster                                           |
| genshi_text     | 21.5 ms                                                         | 20.9 ms: 1.03x faster                                           |
| django_template | 29.8 ms                                                         | 29.6 ms: 1.01x faster                                           |
| mako            | 7.09 ms                                                         | 7.38 ms: 1.04x slower                                           |
| Geometric mean  | (ref)                                                           | 1.01x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250204-pythonperf1_win32-x86-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pathlib                    | 82.9 ms                                                         | 67.2 ms: 1.23x faster                                           |
| regex_effbot               | 1.80 ms                                                         | 1.58 ms: 1.14x faster                                           |
| fannkuch                   | 299 ms                                                          | 284 ms: 1.05x faster                                            |
| thrift                     | 9.98 ms                                                         | 9.55 ms: 1.05x faster                                           |
| genshi_xml                 | 50.1 ms                                                         | 48.1 ms: 1.04x faster                                           |
| tomli_loads                | 1.71 sec                                                        | 1.65 sec: 1.04x faster                                          |
| deepcopy_memo              | 25.4 us                                                         | 24.6 us: 1.03x faster                                           |
| asyncio_websockets         | 363 ms                                                          | 352 ms: 1.03x faster                                            |
| genshi_text                | 21.5 ms                                                         | 20.9 ms: 1.03x faster                                           |
| pprint_pformat             | 1.33 sec                                                        | 1.29 sec: 1.03x faster                                          |
| pprint_safe_repr           | 648 ms                                                          | 631 ms: 1.03x faster                                            |
| deepcopy                   | 314 us                                                          | 306 us: 1.03x faster                                            |
| scimark_sor                | 85.9 ms                                                         | 84.0 ms: 1.02x faster                                           |
| gevent_hub                 | 0.77 ns                                                         | 0.75 ns: 1.02x faster                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 46.7 ms: 1.02x faster                                           |
| coverage                   | 324 ms                                                          | 318 ms: 1.02x faster                                            |
| coroutines                 | 16.2 ms                                                         | 16.0 ms: 1.02x faster                                           |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                           |
| unpickle_pure_python       | 160 us                                                          | 158 us: 1.01x faster                                            |
| nbody                      | 80.0 ms                                                         | 79.1 ms: 1.01x faster                                           |
| float                      | 54.6 ms                                                         | 54.1 ms: 1.01x faster                                           |
| mdp                        | 1.62 sec                                                        | 1.61 sec: 1.01x faster                                          |
| django_template            | 29.8 ms                                                         | 29.6 ms: 1.01x faster                                           |
| pycparser                  | 872 ms                                                          | 875 ms: 1.00x slower                                            |
| subparsers                 | 14.8 ms                                                         | 14.8 ms: 1.01x slower                                           |
| docutils                   | 1.78 sec                                                        | 1.79 sec: 1.01x slower                                          |
| djangocms                  | 2.55 ms                                                         | 2.57 ms: 1.01x slower                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.1 ms: 1.01x slower                                           |
| crypto_pyaes               | 56.9 ms                                                         | 57.4 ms: 1.01x slower                                           |
| sympy_str                  | 212 ms                                                          | 213 ms: 1.01x slower                                            |
| pickle_pure_python         | 231 us                                                          | 234 us: 1.01x slower                                            |
| sympy_expand               | 373 ms                                                          | 377 ms: 1.01x slower                                            |
| generators                 | 21.8 ms                                                         | 22.0 ms: 1.01x slower                                           |
| logging_format             | 8.72 us                                                         | 8.81 us: 1.01x slower                                           |
| scimark_fft                | 205 ms                                                          | 207 ms: 1.01x slower                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 3.50 sec: 1.01x slower                                          |
| sqlalchemy_declarative     | 94.9 ms                                                         | 96.1 ms: 1.01x slower                                           |
| async_tree_none            | 245 ms                                                          | 248 ms: 1.01x slower                                            |
| pidigits                   | 201 ms                                                          | 203 ms: 1.01x slower                                            |
| comprehensions             | 12.5 us                                                         | 12.7 us: 1.01x slower                                           |
| logging_simple             | 7.99 us                                                         | 8.09 us: 1.01x slower                                           |
| 2to3                       | 250 ms                                                          | 254 ms: 1.01x slower                                            |
| gc_traversal               | 1.75 ms                                                         | 1.77 ms: 1.01x slower                                           |
| sphinx                     | 719 ms                                                          | 729 ms: 1.01x slower                                            |
| async_tree_io              | 526 ms                                                          | 533 ms: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 2.88 ms: 1.02x slower                                           |
| sympy_sum                  | 106 ms                                                          | 107 ms: 1.02x slower                                            |
| bench_mp_pool              | 90.6 ms                                                         | 92.1 ms: 1.02x slower                                           |
| chaos                      | 50.2 ms                                                         | 51.1 ms: 1.02x slower                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.08 ms: 1.02x slower                                           |
| xml_etree_process          | 44.2 ms                                                         | 45.0 ms: 1.02x slower                                           |
| hexiom                     | 4.44 ms                                                         | 4.53 ms: 1.02x slower                                           |
| shortest_path              | 290 ms                                                          | 296 ms: 1.02x slower                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.02 ms: 1.02x slower                                           |
| k_core                     | 1.38 sec                                                        | 1.41 sec: 1.02x slower                                          |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.02x slower                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 42.4 ms: 1.02x slower                                           |
| many_optionals             | 436 us                                                          | 447 us: 1.02x slower                                            |
| regex_compile              | 101 ms                                                          | 103 ms: 1.02x slower                                            |
| xml_etree_generate         | 61.4 ms                                                         | 62.9 ms: 1.03x slower                                           |
| deltablue                  | 2.33 ms                                                         | 2.39 ms: 1.03x slower                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.27 ms: 1.03x slower                                           |
| richards_super             | 36.7 ms                                                         | 37.7 ms: 1.03x slower                                           |
| sqlalchemy_imperative      | 11.2 ms                                                         | 11.5 ms: 1.03x slower                                           |
| dulwich_log                | 48.8 ms                                                         | 50.1 ms: 1.03x slower                                           |
| sqlglot_normalize          | 216 ms                                                          | 222 ms: 1.03x slower                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.03 ms: 1.03x slower                                           |
| logging_silent             | 60.3 ns                                                         | 62.1 ns: 1.03x slower                                           |
| async_tree_none_tg         | 214 ms                                                          | 221 ms: 1.03x slower                                            |
| go                         | 109 ms                                                          | 112 ms: 1.03x slower                                            |
| async_tree_memoization_tg  | 282 ms                                                          | 292 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 64.7 ms: 1.03x slower                                           |
| raytrace                   | 201 ms                                                          | 208 ms: 1.04x slower                                            |
| richards                   | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                           |
| nqueens                    | 72.1 ms                                                         | 74.9 ms: 1.04x slower                                           |
| meteor_contest             | 74.6 ms                                                         | 77.6 ms: 1.04x slower                                           |
| json                       | 4.27 ms                                                         | 4.45 ms: 1.04x slower                                           |
| mako                       | 7.09 ms                                                         | 7.38 ms: 1.04x slower                                           |
| typing_runtime_protocols   | 138 us                                                          | 144 us: 1.04x slower                                            |
| python_startup             | 28.3 ms                                                         | 29.8 ms: 1.05x slower                                           |
| async_tree_io_tg           | 494 ms                                                          | 521 ms: 1.05x slower                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 516 ms: 1.07x slower                                            |
| python_startup_no_site     | 19.7 ms                                                         | 21.3 ms: 1.09x slower                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 506 ms: 1.11x slower                                            |
| regex_dna                  | 114 ms                                                          | 128 ms: 1.13x slower                                            |
| tornado_http               | 94.1 ms                                                         | 112 ms: 1.19x slower                                            |
| Geometric mean             | (ref)                                                           | 1.01x slower                                                    |

Benchmark hidden because not significant (14): regex_v8, connected_components, chameleon, telco, scimark_lu, json_dumps, spectral_norm, async_generators, deepcopy_reduce, json_loads, html5lib, pylint, async_tree_memoization, pyflate

- Geometric mean (including insignificant results): 1.009x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown