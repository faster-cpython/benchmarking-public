# Results vs. 3.13.0

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: windows-x86
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.014x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.01x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 253 ms: 1.01x slower                                                            |
| docutils       | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                          |
| sphinx         | 719 ms                                                          | 748 ms: 1.04x slower                                                            |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 259 ms: 1.15x faster                                                            |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.14x faster                                                            |
| async_tree_io              | 526 ms                                                          | 463 ms: 1.14x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 351 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 468 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 454 ms: 1.01x faster                                                            |
| async_generators           | 270 ms                                                          | 306 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 199 ms: 1.01x faster                                                            |
| float          | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| nbody          | 80.0 ms                                                         | 89.3 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| regex_v8       | 16.8 ms                                                         | 15.2 ms: 1.10x faster                                                           |
| regex_dna      | 114 ms                                                          | 112 ms: 1.02x faster                                                            |
| regex_compile  | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads           | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.73 sec: 1.01x slower                                                          |
| xml_etree_parse      | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| xml_etree_iterparse  | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 67.0 ms: 1.09x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 48.7 ms: 1.10x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 8.19 ms: 1.12x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 187 us: 1.17x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 277 us: 1.20x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.08x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.7 ms                                                         | 21.7 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 50.1 ms                                                         | 48.6 ms: 1.03x faster                                                           |
| genshi_text     | 21.5 ms                                                         | 22.9 ms: 1.06x slower                                                           |
| mako            | 7.09 ms                                                         | 7.73 ms: 1.09x slower                                                           |
| django_template | 29.8 ms                                                         | 35.4 ms: 1.19x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 776 us: 12.85x faster                                                           |
| coverage                   | 324 ms                                                          | 52.1 ms: 6.22x faster                                                           |
| pathlib                    | 82.9 ms                                                         | 34.3 ms: 2.41x faster                                                           |
| deepcopy                   | 314 us                                                          | 241 us: 1.30x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 21.6 us: 1.18x faster                                                           |
| deepcopy_reduce            | 2.92 us                                                         | 2.49 us: 1.17x faster                                                           |
| regex_effbot               | 1.80 ms                                                         | 1.54 ms: 1.17x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 245 ms: 1.15x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 259 ms: 1.15x faster                                                            |
| async_tree_none            | 245 ms                                                          | 216 ms: 1.14x faster                                                            |
| async_tree_io              | 526 ms                                                          | 463 ms: 1.14x faster                                                            |
| regex_v8                   | 16.8 ms                                                         | 15.2 ms: 1.10x faster                                                           |
| async_tree_io_tg           | 494 ms                                                          | 453 ms: 1.09x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 197 ms: 1.09x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.84 us: 1.06x faster                                                           |
| asyncio_websockets         | 363 ms                                                          | 351 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 468 ms: 1.03x faster                                                            |
| genshi_xml                 | 50.1 ms                                                         | 48.6 ms: 1.03x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.03 ms: 1.03x faster                                                           |
| regex_dna                  | 114 ms                                                          | 112 ms: 1.02x faster                                                            |
| pidigits                   | 201 ms                                                          | 199 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 454 ms: 1.01x faster                                                            |
| json_loads                 | 21.6 us                                                         | 21.5 us: 1.00x faster                                                           |
| bpe_tokeniser              | 3.46 sec                                                        | 3.47 sec: 1.00x slower                                                          |
| tomli_loads                | 1.71 sec                                                        | 1.73 sec: 1.01x slower                                                          |
| 2to3                       | 250 ms                                                          | 253 ms: 1.01x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 109 ms: 1.01x slower                                                            |
| sympy_sum                  | 106 ms                                                          | 107 ms: 1.01x slower                                                            |
| sympy_expand               | 373 ms                                                          | 379 ms: 1.01x slower                                                            |
| sympy_str                  | 212 ms                                                          | 217 ms: 1.02x slower                                                            |
| shortest_path              | 290 ms                                                          | 297 ms: 1.02x slower                                                            |
| sqlglot_normalize          | 216 ms                                                          | 222 ms: 1.03x slower                                                            |
| pprint_pformat             | 1.33 sec                                                        | 1.36 sec: 1.03x slower                                                          |
| pprint_safe_repr           | 648 ms                                                          | 667 ms: 1.03x slower                                                            |
| pycparser                  | 872 ms                                                          | 897 ms: 1.03x slower                                                            |
| fannkuch                   | 299 ms                                                          | 310 ms: 1.04x slower                                                            |
| gc_traversal               | 1.75 ms                                                         | 1.81 ms: 1.04x slower                                                           |
| json                       | 4.27 ms                                                         | 4.43 ms: 1.04x slower                                                           |
| docutils                   | 1.78 sec                                                        | 1.85 sec: 1.04x slower                                                          |
| sphinx                     | 719 ms                                                          | 748 ms: 1.04x slower                                                            |
| sqlglot_optimize           | 41.4 ms                                                         | 43.3 ms: 1.04x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                                           |
| logging_simple             | 7.99 us                                                         | 8.36 us: 1.05x slower                                                           |
| xml_etree_iterparse        | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                           |
| logging_format             | 8.72 us                                                         | 9.16 us: 1.05x slower                                                           |
| float                      | 54.6 ms                                                         | 57.5 ms: 1.05x slower                                                           |
| spectral_norm              | 69.4 ms                                                         | 73.2 ms: 1.05x slower                                                           |
| dulwich_log                | 48.8 ms                                                         | 51.8 ms: 1.06x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 22.9 ms: 1.06x slower                                                           |
| regex_compile              | 101 ms                                                          | 108 ms: 1.07x slower                                                            |
| nqueens                    | 72.1 ms                                                         | 77.6 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.07 ms: 1.08x slower                                                           |
| comprehensions             | 12.5 us                                                         | 13.6 us: 1.08x slower                                                           |
| xml_etree_generate         | 61.4 ms                                                         | 67.0 ms: 1.09x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.73 ms: 1.09x slower                                                           |
| pyflate                    | 320 ms                                                          | 352 ms: 1.10x slower                                                            |
| meteor_contest             | 74.6 ms                                                         | 82.1 ms: 1.10x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 48.7 ms: 1.10x slower                                                           |
| scimark_fft                | 205 ms                                                          | 226 ms: 1.11x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 21.7 ms: 1.11x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.80 sec: 1.11x slower                                                          |
| typing_runtime_protocols   | 138 us                                                          | 153 us: 1.11x slower                                                            |
| nbody                      | 80.0 ms                                                         | 89.3 ms: 1.12x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 63.9 ms: 1.12x slower                                                           |
| json_dumps                 | 7.30 ms                                                         | 8.19 ms: 1.12x slower                                                           |
| chaos                      | 50.2 ms                                                         | 56.5 ms: 1.13x slower                                                           |
| async_generators           | 270 ms                                                          | 306 ms: 1.14x slower                                                            |
| scimark_monte_carlo        | 47.7 ms                                                         | 54.5 ms: 1.14x slower                                                           |
| richards                   | 32.7 ms                                                         | 37.7 ms: 1.15x slower                                                           |
| sqlglot_transpile          | 1.24 ms                                                         | 1.43 ms: 1.15x slower                                                           |
| scimark_lu                 | 60.2 ms                                                         | 69.5 ms: 1.15x slower                                                           |
| sqlglot_parse              | 1.00 ms                                                         | 1.16 ms: 1.16x slower                                                           |
| scimark_sor                | 85.9 ms                                                         | 99.7 ms: 1.16x slower                                                           |
| hexiom                     | 4.44 ms                                                         | 5.15 ms: 1.16x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 187 us: 1.17x slower                                                            |
| richards_super             | 36.7 ms                                                         | 43.4 ms: 1.18x slower                                                           |
| django_template            | 29.8 ms                                                         | 35.4 ms: 1.19x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 277 us: 1.20x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 72.4 ns: 1.20x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 2.83 ms: 1.21x slower                                                           |
| generators                 | 21.8 ms                                                         | 26.8 ms: 1.23x slower                                                           |
| many_optionals             | 436 us                                                          | 549 us: 1.26x slower                                                            |
| raytrace                   | 201 ms                                                          | 257 ms: 1.27x slower                                                            |
| bench_thread_pool          | 1.00 ms                                                         | 1.31 ms: 1.31x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 21.8 ms: 1.48x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.01x faster                                                                    |

Benchmark hidden because not significant (9): connected_components, k_core, pylint, python_startup, telco, bench_mp_pool, go, html5lib, coroutines
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-pythonperf1_win32-x86-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: unknown