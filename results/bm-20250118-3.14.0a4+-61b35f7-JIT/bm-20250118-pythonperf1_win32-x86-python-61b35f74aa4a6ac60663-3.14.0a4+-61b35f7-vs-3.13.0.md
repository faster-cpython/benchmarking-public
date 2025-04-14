# Results vs. 3.13.0

- fork: python
- ref: 61b35f74aa4a6ac60663
- machine: windows-x86
- commit hash: 61b35f7
- commit date: 2025-01-18
- overall geometric mean: 1.107x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 250 ms                                                          | 291 ms: 1.16x slower                                                            |
| docutils       | 1.78 sec                                                        | 2.15 sec: 1.21x slower                                                          |
| html5lib       | 47.5 ms                                                         | 54.7 ms: 1.15x slower                                                           |
| sphinx         | 719 ms                                                          | 868 ms: 1.21x slower                                                            |
| Geometric mean | (ref)                                                           | 1.18x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 282 ms                                                          | 261 ms: 1.08x faster                                                            |
| async_tree_io              | 526 ms                                                          | 508 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 208 ms: 1.03x faster                                                            |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 480 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 356 ms: 1.02x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 291 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 461 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 490 ms: 1.01x slower                                                            |
| async_generators           | 270 ms                                                          | 345 ms: 1.28x slower                                                            |
| coroutines                 | 16.2 ms                                                         | 21.8 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| float          | 54.6 ms                                                         | 56.8 ms: 1.04x slower                                                           |
| nbody          | 80.0 ms                                                         | 112 ms: 1.41x slower                                                            |
| Geometric mean | (ref)                                                           | 1.13x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| regex_dna      | 114 ms                                                          | 115 ms: 1.02x slower                                                            |
| regex_compile  | 101 ms                                                          | 132 ms: 1.30x slower                                                            |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                          | 110 ms: 1.02x slower                                                            |
| json_loads           | 21.6 us                                                         | 23.0 us: 1.06x slower                                                           |
| tomli_loads          | 1.71 sec                                                        | 1.89 sec: 1.10x slower                                                          |
| xml_etree_iterparse  | 62.6 ms                                                         | 69.7 ms: 1.11x slower                                                           |
| xml_etree_generate   | 61.4 ms                                                         | 77.0 ms: 1.25x slower                                                           |
| xml_etree_process    | 44.2 ms                                                         | 56.6 ms: 1.28x slower                                                           |
| json_dumps           | 7.30 ms                                                         | 9.55 ms: 1.31x slower                                                           |
| unpickle_pure_python | 160 us                                                          | 213 us: 1.33x slower                                                            |
| pickle_pure_python   | 231 us                                                          | 335 us: 1.45x slower                                                            |
| Geometric mean       | (ref)                                                           | 1.21x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                           |
| python_startup_no_site | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 7.09 ms                                                         | 7.39 ms: 1.04x slower                                                           |
| genshi_xml      | 50.1 ms                                                         | 61.8 ms: 1.23x slower                                                           |
| django_template | 29.8 ms                                                         | 40.2 ms: 1.35x slower                                                           |
| genshi_text     | 21.5 ms                                                         | 29.2 ms: 1.36x slower                                                           |
| Geometric mean  | (ref)                                                           | 1.24x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                     | 9.98 ms                                                         | 841 us: 11.87x faster                                                           |
| coverage                   | 324 ms                                                          | 54.3 ms: 5.96x faster                                                           |
| sqlglot_normalize          | 216 ms                                                          | 115 ms: 1.88x faster                                                            |
| regex_effbot               | 1.80 ms                                                         | 1.56 ms: 1.16x faster                                                           |
| async_tree_memoization_tg  | 282 ms                                                          | 261 ms: 1.08x faster                                                            |
| deepcopy                   | 314 us                                                          | 299 us: 1.05x faster                                                            |
| python_startup             | 28.3 ms                                                         | 27.2 ms: 1.04x faster                                                           |
| async_tree_io              | 526 ms                                                          | 508 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 214 ms                                                          | 208 ms: 1.03x faster                                                            |
| async_tree_none            | 245 ms                                                          | 238 ms: 1.03x faster                                                            |
| async_tree_io_tg           | 494 ms                                                          | 480 ms: 1.03x faster                                                            |
| asyncio_websockets         | 363 ms                                                          | 356 ms: 1.02x faster                                                            |
| async_tree_memoization     | 297 ms                                                          | 291 ms: 1.02x faster                                                            |
| sqlite_synth               | 1.95 us                                                         | 1.92 us: 1.02x faster                                                           |
| create_gc_cycles           | 1.06 ms                                                         | 1.04 ms: 1.01x faster                                                           |
| pidigits                   | 201 ms                                                          | 200 ms: 1.00x faster                                                            |
| deepcopy_memo              | 25.4 us                                                         | 25.5 us: 1.00x slower                                                           |
| async_tree_cpu_io_mixed_tg | 456 ms                                                          | 461 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 484 ms                                                          | 490 ms: 1.01x slower                                                            |
| regex_dna                  | 114 ms                                                          | 115 ms: 1.02x slower                                                            |
| xml_etree_parse            | 107 ms                                                          | 110 ms: 1.02x slower                                                            |
| python_startup_no_site     | 19.7 ms                                                         | 20.4 ms: 1.04x slower                                                           |
| gc_traversal               | 1.75 ms                                                         | 1.82 ms: 1.04x slower                                                           |
| float                      | 54.6 ms                                                         | 56.8 ms: 1.04x slower                                                           |
| mako                       | 7.09 ms                                                         | 7.39 ms: 1.04x slower                                                           |
| pathlib                    | 82.9 ms                                                         | 86.5 ms: 1.04x slower                                                           |
| k_core                     | 1.38 sec                                                        | 1.44 sec: 1.04x slower                                                          |
| deepcopy_reduce            | 2.92 us                                                         | 3.05 us: 1.05x slower                                                           |
| json_loads                 | 21.6 us                                                         | 23.0 us: 1.06x slower                                                           |
| json                       | 4.27 ms                                                         | 4.58 ms: 1.07x slower                                                           |
| bench_mp_pool              | 90.6 ms                                                         | 97.5 ms: 1.08x slower                                                           |
| telco                      | 6.96 ms                                                         | 7.57 ms: 1.09x slower                                                           |
| tomli_loads                | 1.71 sec                                                        | 1.89 sec: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.84 ms                                                         | 3.13 ms: 1.10x slower                                                           |
| connected_components       | 267 ms                                                          | 297 ms: 1.11x slower                                                            |
| xml_etree_iterparse        | 62.6 ms                                                         | 69.7 ms: 1.11x slower                                                           |
| bench_thread_pool          | 1.00 ms                                                         | 1.12 ms: 1.12x slower                                                           |
| shortest_path              | 290 ms                                                          | 327 ms: 1.13x slower                                                            |
| spectral_norm              | 69.4 ms                                                         | 78.3 ms: 1.13x slower                                                           |
| pycparser                  | 872 ms                                                          | 1.00 sec: 1.15x slower                                                          |
| pprint_pformat             | 1.33 sec                                                        | 1.53 sec: 1.15x slower                                                          |
| html5lib                   | 47.5 ms                                                         | 54.7 ms: 1.15x slower                                                           |
| 2to3                       | 250 ms                                                          | 291 ms: 1.16x slower                                                            |
| bpe_tokeniser              | 3.46 sec                                                        | 4.03 sec: 1.16x slower                                                          |
| dulwich_log                | 48.8 ms                                                         | 57.0 ms: 1.17x slower                                                           |
| pprint_safe_repr           | 648 ms                                                          | 759 ms: 1.17x slower                                                            |
| pylint                     | 227 ms                                                          | 269 ms: 1.19x slower                                                            |
| logging_format             | 8.72 us                                                         | 10.4 us: 1.19x slower                                                           |
| fannkuch                   | 299 ms                                                          | 359 ms: 1.20x slower                                                            |
| scimark_fft                | 205 ms                                                          | 247 ms: 1.21x slower                                                            |
| sphinx                     | 719 ms                                                          | 868 ms: 1.21x slower                                                            |
| docutils                   | 1.78 sec                                                        | 2.15 sec: 1.21x slower                                                          |
| sympy_expand               | 373 ms                                                          | 452 ms: 1.21x slower                                                            |
| logging_simple             | 7.99 us                                                         | 9.77 us: 1.22x slower                                                           |
| mdp                        | 1.62 sec                                                        | 1.99 sec: 1.22x slower                                                          |
| meteor_contest             | 74.6 ms                                                         | 91.7 ms: 1.23x slower                                                           |
| crypto_pyaes               | 56.9 ms                                                         | 70.1 ms: 1.23x slower                                                           |
| genshi_xml                 | 50.1 ms                                                         | 61.8 ms: 1.23x slower                                                           |
| sympy_str                  | 212 ms                                                          | 263 ms: 1.24x slower                                                            |
| pyflate                    | 320 ms                                                          | 399 ms: 1.25x slower                                                            |
| xml_etree_generate         | 61.4 ms                                                         | 77.0 ms: 1.25x slower                                                           |
| sympy_sum                  | 106 ms                                                          | 132 ms: 1.25x slower                                                            |
| typing_runtime_protocols   | 138 us                                                          | 174 us: 1.27x slower                                                            |
| scimark_sor                | 85.9 ms                                                         | 109 ms: 1.27x slower                                                            |
| sqlglot_parse              | 1.00 ms                                                         | 1.27 ms: 1.27x slower                                                           |
| go                         | 109 ms                                                          | 139 ms: 1.28x slower                                                            |
| async_generators           | 270 ms                                                          | 345 ms: 1.28x slower                                                            |
| sqlglot_transpile          | 1.24 ms                                                         | 1.58 ms: 1.28x slower                                                           |
| xml_etree_process          | 44.2 ms                                                         | 56.6 ms: 1.28x slower                                                           |
| sympy_integrate            | 15.0 ms                                                         | 19.4 ms: 1.29x slower                                                           |
| regex_compile              | 101 ms                                                          | 132 ms: 1.30x slower                                                            |
| json_dumps                 | 7.30 ms                                                         | 9.55 ms: 1.31x slower                                                           |
| unpickle_pure_python       | 160 us                                                          | 213 us: 1.33x slower                                                            |
| scimark_lu                 | 60.2 ms                                                         | 80.7 ms: 1.34x slower                                                           |
| sqlglot_optimize           | 41.4 ms                                                         | 55.6 ms: 1.34x slower                                                           |
| coroutines                 | 16.2 ms                                                         | 21.8 ms: 1.34x slower                                                           |
| django_template            | 29.8 ms                                                         | 40.2 ms: 1.35x slower                                                           |
| genshi_text                | 21.5 ms                                                         | 29.2 ms: 1.36x slower                                                           |
| chaos                      | 50.2 ms                                                         | 70.0 ms: 1.39x slower                                                           |
| scimark_monte_carlo        | 47.7 ms                                                         | 66.9 ms: 1.40x slower                                                           |
| nbody                      | 80.0 ms                                                         | 112 ms: 1.41x slower                                                            |
| richards_super             | 36.7 ms                                                         | 52.9 ms: 1.44x slower                                                           |
| richards                   | 32.7 ms                                                         | 47.2 ms: 1.44x slower                                                           |
| pickle_pure_python         | 231 us                                                          | 335 us: 1.45x slower                                                            |
| logging_silent             | 60.3 ns                                                         | 88.0 ns: 1.46x slower                                                           |
| deltablue                  | 2.33 ms                                                         | 3.41 ms: 1.46x slower                                                           |
| nqueens                    | 72.1 ms                                                         | 106 ms: 1.48x slower                                                            |
| many_optionals             | 436 us                                                          | 655 us: 1.50x slower                                                            |
| comprehensions             | 12.5 us                                                         | 19.1 us: 1.53x slower                                                           |
| subparsers                 | 14.8 ms                                                         | 22.7 ms: 1.54x slower                                                           |
| raytrace                   | 201 ms                                                          | 337 ms: 1.67x slower                                                            |
| hexiom                     | 4.44 ms                                                         | 7.57 ms: 1.71x slower                                                           |
| generators                 | 21.8 ms                                                         | 42.0 ms: 1.93x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.12x slower                                                                    |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (8) of results/bm-20250118-3.14.0a4+-61b35f7-JIT/bm-20250118-pythonperf1_win32-x86-python-61b35f74aa4a6ac60663-3.14.0a4+-61b35f7.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.107x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.14x
- 95% likely to have a slowdown of 1.13x
- 99% likely to have a slowdown of 1.10x

# Memory
- memory change: unknown