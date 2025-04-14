# Results vs. 3.13.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: windows-x86
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.000x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 258 ms: 1.03x slower                                                                   |
| docutils       | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                                 |
| html5lib       | 47.5 ms                                                         | 50.3 ms: 1.06x slower                                                                  |
| sphinx         | 719 ms                                                          | 754 ms: 1.05x slower                                                                   |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io              | 526 ms                                                          | 486 ms: 1.08x faster                                                                   |
| async_tree_memoization_tg  | 282 ms                                                          | 263 ms: 1.07x faster                                                                   |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.07x faster                                                                   |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                                   |
| asyncio_websockets         | 363 ms                                                          | 351 ms: 1.03x faster                                                                   |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.02x faster                                                                   |
| async_tree_io_tg           | 494 ms                                                          | 484 ms: 1.02x faster                                                                   |
| coroutines                 | 16.2 ms                                                         | 16.0 ms: 1.02x faster                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 464 ms: 1.02x slower                                                                   |
| async_generators           | 270 ms                                                          | 317 ms: 1.17x slower                                                                   |
| Geometric mean             | (ref)                                                           | 1.02x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 202 ms: 1.01x slower                                                                   |
| float          | 54.6 ms                                                         | 55.3 ms: 1.01x slower                                                                  |
| nbody          | 80.0 ms                                                         | 91.0 ms: 1.14x slower                                                                  |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                                  |
| regex_v8       | 16.8 ms                                                         | 15.5 ms: 1.09x faster                                                                  |
| regex_dna      | 114 ms                                                          | 120 ms: 1.06x slower                                                                   |
| regex_compile  | 101 ms                                                          | 111 ms: 1.10x slower                                                                   |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 107 ms: 1.01x faster                                                                   |
| tomli_loads          | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                                 |
| xml_etree_iterparse  | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                                  |
| xml_etree_generate   | 61.4 ms                                                         | 68.8 ms: 1.12x slower                                                                  |
| json_dumps           | 7.30 ms                                                         | 8.32 ms: 1.14x slower                                                                  |
| xml_etree_process    | 44.2 ms                                                         | 51.3 ms: 1.16x slower                                                                  |
| unpickle_pure_python | 160 us                                                          | 186 us: 1.16x slower                                                                   |
| pickle_pure_python   | 231 us                                                          | 287 us: 1.24x slower                                                                   |
| Geometric mean       | (ref)                                                           | 1.10x slower                                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                                  |
| python_startup_no_site | 19.7 ms                                                         | 21.5 ms: 1.10x slower                                                                  |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_text     | 21.5 ms                                                         | 23.1 ms: 1.08x slower                                                                  |
| mako            | 7.09 ms                                                         | 7.97 ms: 1.13x slower                                                                  |
| django_template | 29.8 ms                                                         | 34.1 ms: 1.14x slower                                                                  |
| Geometric mean  | (ref)                                                           | 1.09x slower                                                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250217-pythonperf1_win32-x86-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 786 us: 12.70x faster                                                                  |
| coverage                   | 324 ms                                                          | 51.5 ms: 6.29x faster                                                                  |
| pathlib                    | 82.9 ms                                                         | 34.1 ms: 2.43x faster                                                                  |
| deepcopy                   | 314 us                                                          | 244 us: 1.29x faster                                                                   |
| deepcopy_memo              | 25.4 us                                                         | 22.3 us: 1.14x faster                                                                  |
| regex_effbot               | 1.80 ms                                                         | 1.59 ms: 1.13x faster                                                                  |
| deepcopy_reduce            | 2.92 us                                                         | 2.63 us: 1.11x faster                                                                  |
| regex_v8                   | 16.8 ms                                                         | 15.5 ms: 1.09x faster                                                                  |
| async_tree_io              | 526 ms                                                          | 486 ms: 1.08x faster                                                                   |
| async_tree_memoization_tg  | 282 ms                                                          | 263 ms: 1.07x faster                                                                   |
| async_tree_none            | 245 ms                                                          | 228 ms: 1.07x faster                                                                   |
| async_tree_memoization     | 297 ms                                                          | 278 ms: 1.07x faster                                                                   |
| telco                      | 6.96 ms                                                         | 6.57 ms: 1.06x faster                                                                  |
| sqlite_synth               | 1.95 us                                                         | 1.89 us: 1.04x faster                                                                  |
| asyncio_websockets         | 363 ms                                                          | 351 ms: 1.03x faster                                                                   |
| async_tree_none_tg         | 214 ms                                                          | 209 ms: 1.02x faster                                                                   |
| async_tree_io_tg           | 494 ms                                                          | 484 ms: 1.02x faster                                                                   |
| coroutines                 | 16.2 ms                                                         | 16.0 ms: 1.02x faster                                                                  |
| python_startup             | 28.3 ms                                                         | 27.8 ms: 1.02x faster                                                                  |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 481 ms: 1.01x faster                                                                   |
| bench_mp_pool              | 90.6 ms                                                         | 90.0 ms: 1.01x faster                                                                  |
| xml_etree_parse            | 107 ms                                                          | 107 ms: 1.01x faster                                                                   |
| bpe_tokeniser              | 3.46 sec                                                        | 3.48 sec: 1.00x slower                                                                 |
| pidigits                   | 201 ms                                                          | 202 ms: 1.01x slower                                                                   |
| fannkuch                   | 299 ms                                                          | 301 ms: 1.01x slower                                                                   |
| float                      | 54.6 ms                                                         | 55.3 ms: 1.01x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 464 ms: 1.02x slower                                                                   |
| tomli_loads                | 1.71 sec                                                        | 1.75 sec: 1.02x slower                                                                 |
| 2to3                       | 250 ms                                                          | 258 ms: 1.03x slower                                                                   |
| pprint_safe_repr           | 648 ms                                                          | 669 ms: 1.03x slower                                                                   |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                                                  |
| sympy_sum                  | 106 ms                                                          | 110 ms: 1.04x slower                                                                   |
| mdp                        | 1.62 sec                                                        | 1.69 sec: 1.04x slower                                                                 |
| docutils                   | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                                 |
| pprint_pformat             | 1.33 sec                                                        | 1.39 sec: 1.04x slower                                                                 |
| json                       | 4.27 ms                                                         | 4.46 ms: 1.04x slower                                                                  |
| shortest_path              | 290 ms                                                          | 303 ms: 1.05x slower                                                                   |
| sympy_expand               | 373 ms                                                          | 391 ms: 1.05x slower                                                                   |
| sphinx                     | 719 ms                                                          | 754 ms: 1.05x slower                                                                   |
| sympy_str                  | 212 ms                                                          | 222 ms: 1.05x slower                                                                   |
| regex_dna                  | 114 ms                                                          | 120 ms: 1.06x slower                                                                   |
| html5lib                   | 47.5 ms                                                         | 50.3 ms: 1.06x slower                                                                  |
| bench_thread_pool          | 1.00 ms                                                         | 1.06 ms: 1.06x slower                                                                  |
| xml_etree_iterparse        | 62.6 ms                                                         | 66.6 ms: 1.06x slower                                                                  |
| pycparser                  | 872 ms                                                          | 930 ms: 1.07x slower                                                                   |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.04 ms: 1.07x slower                                                                  |
| dulwich_log                | 48.8 ms                                                         | 52.5 ms: 1.08x slower                                                                  |
| genshi_text                | 21.5 ms                                                         | 23.1 ms: 1.08x slower                                                                  |
| sympy_integrate            | 15.0 ms                                                         | 16.1 ms: 1.08x slower                                                                  |
| sqlglot_optimize           | 41.4 ms                                                         | 44.7 ms: 1.08x slower                                                                  |
| meteor_contest             | 74.6 ms                                                         | 80.6 ms: 1.08x slower                                                                  |
| spectral_norm              | 69.4 ms                                                         | 75.1 ms: 1.08x slower                                                                  |
| crypto_pyaes               | 56.9 ms                                                         | 61.7 ms: 1.08x slower                                                                  |
| sqlglot_normalize          | 216 ms                                                          | 235 ms: 1.09x slower                                                                   |
| logging_format             | 8.72 us                                                         | 9.55 us: 1.10x slower                                                                  |
| python_startup_no_site     | 19.7 ms                                                         | 21.5 ms: 1.10x slower                                                                  |
| regex_compile              | 101 ms                                                          | 111 ms: 1.10x slower                                                                   |
| typing_runtime_protocols   | 138 us                                                          | 151 us: 1.10x slower                                                                   |
| logging_simple             | 7.99 us                                                         | 8.82 us: 1.10x slower                                                                  |
| pyflate                    | 320 ms                                                          | 354 ms: 1.11x slower                                                                   |
| nqueens                    | 72.1 ms                                                         | 79.8 ms: 1.11x slower                                                                  |
| xml_etree_generate         | 61.4 ms                                                         | 68.8 ms: 1.12x slower                                                                  |
| comprehensions             | 12.5 us                                                         | 14.0 us: 1.12x slower                                                                  |
| mako                       | 7.09 ms                                                         | 7.97 ms: 1.13x slower                                                                  |
| scimark_fft                | 205 ms                                                          | 231 ms: 1.13x slower                                                                   |
| sqlglot_transpile          | 1.24 ms                                                         | 1.40 ms: 1.13x slower                                                                  |
| nbody                      | 80.0 ms                                                         | 91.0 ms: 1.14x slower                                                                  |
| json_dumps                 | 7.30 ms                                                         | 8.32 ms: 1.14x slower                                                                  |
| richards                   | 32.7 ms                                                         | 37.3 ms: 1.14x slower                                                                  |
| django_template            | 29.8 ms                                                         | 34.1 ms: 1.14x slower                                                                  |
| sqlglot_parse              | 1.00 ms                                                         | 1.15 ms: 1.15x slower                                                                  |
| scimark_lu                 | 60.2 ms                                                         | 69.6 ms: 1.15x slower                                                                  |
| xml_etree_process          | 44.2 ms                                                         | 51.3 ms: 1.16x slower                                                                  |
| unpickle_pure_python       | 160 us                                                          | 186 us: 1.16x slower                                                                   |
| richards_super             | 36.7 ms                                                         | 43.0 ms: 1.17x slower                                                                  |
| async_generators           | 270 ms                                                          | 317 ms: 1.17x slower                                                                   |
| chaos                      | 50.2 ms                                                         | 59.2 ms: 1.18x slower                                                                  |
| scimark_monte_carlo        | 47.7 ms                                                         | 56.9 ms: 1.19x slower                                                                  |
| scimark_sor                | 85.9 ms                                                         | 103 ms: 1.20x slower                                                                   |
| hexiom                     | 4.44 ms                                                         | 5.31 ms: 1.20x slower                                                                  |
| logging_silent             | 60.3 ns                                                         | 72.8 ns: 1.21x slower                                                                  |
| deltablue                  | 2.33 ms                                                         | 2.86 ms: 1.23x slower                                                                  |
| generators                 | 21.8 ms                                                         | 26.9 ms: 1.23x slower                                                                  |
| pickle_pure_python         | 231 us                                                          | 287 us: 1.24x slower                                                                   |
| many_optionals             | 436 us                                                          | 549 us: 1.26x slower                                                                   |
| raytrace                   | 201 ms                                                          | 254 ms: 1.26x slower                                                                   |
| subparsers                 | 14.8 ms                                                         | 22.2 ms: 1.50x slower                                                                  |
| Geometric mean             | (ref)                                                           | 1.00x slower                                                                           |

Benchmark hidden because not significant (7): create_gc_cycles, go, json_loads, pylint, k_core, genshi_xml, connected_components
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown