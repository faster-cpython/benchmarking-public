# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 97.93%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.02 sec: 1.11x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.9 ms: 1.05x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 507 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 477 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 548 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.3 ms: 1.47x faster                                                          |
| float          | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                          |
| pidigits       | 199 ms                                                              | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 95.2 ms: 1.05x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 128 ms: 1.09x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 2.08 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.55 sec: 1.06x faster                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 57.7 ms: 1.03x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.0 ms: 1.02x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 146 us: 1.01x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.09 ms: 1.04x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 43.7 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.49 ms: 1.27x faster                                                          |
| django_template | 30.1 ms                                                             | 33.9 ms: 1.13x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.0 ms: 1.19x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.3 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 766 us: 12.71x faster                                                          |
| coverage                   | 307 ms                                                              | 53.6 ms: 5.73x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.8 us: 1.49x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.3 ms: 1.47x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.7 ms: 1.42x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.49 ms: 1.27x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.31 ms: 1.24x faster                                                          |
| float                      | 52.4 ms                                                             | 43.0 ms: 1.22x faster                                                          |
| scimark_fft                | 198 ms                                                              | 165 ms: 1.20x faster                                                           |
| pyflate                    | 308 ms                                                              | 261 ms: 1.18x faster                                                           |
| fannkuch                   | 270 ms                                                              | 233 ms: 1.16x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 48.3 ms: 1.16x faster                                                          |
| deepcopy                   | 280 us                                                              | 249 us: 1.12x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.6 ms: 1.09x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.55 sec: 1.06x faster                                                         |
| meteor_contest             | 74.1 ms                                                             | 70.1 ms: 1.06x faster                                                          |
| regex_compile              | 99.9 ms                                                             | 95.2 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 507 ms: 1.04x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 57.7 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.52 us: 1.03x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.87 ms: 1.03x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.0 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 196 ms: 1.02x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 599 ms: 1.01x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.8 us: 1.01x faster                                                          |
| unpickle_pure_python       | 147 us                                                              | 146 us: 1.01x faster                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 477 ms: 1.01x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.3 sec: 1.02x slower                                                         |
| create_gc_cycles           | 756 us                                                              | 775 us: 1.03x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.23 ms: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                              | 548 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.09 ms: 1.04x slower                                                          |
| pycparser                  | 777 ms                                                              | 806 ms: 1.04x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 43.7 ms: 1.04x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 695 ms: 1.05x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 47.9 ms: 1.05x slower                                                          |
| sympy_str                  | 211 ms                                                              | 223 ms: 1.05x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 112 ms: 1.06x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 73.0 ms: 1.06x slower                                                          |
| richards                   | 31.2 ms                                                             | 33.3 ms: 1.07x slower                                                          |
| sympy_expand               | 375 ms                                                              | 401 ms: 1.07x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.08x slower                                                         |
| logging_format             | 8.13 us                                                             | 8.76 us: 1.08x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.06 us: 1.08x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 90.7 ms: 1.08x slower                                                          |
| regex_dna                  | 118 ms                                                              | 128 ms: 1.09x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.8 ms: 1.10x slower                                                          |
| go                         | 101 ms                                                              | 111 ms: 1.10x slower                                                           |
| richards_super             | 35.5 ms                                                             | 39.1 ms: 1.10x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 2.08 ms: 1.11x slower                                                          |
| 2to3                       | 233 ms                                                              | 258 ms: 1.11x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.3 ms: 1.11x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.02 sec: 1.11x slower                                                         |
| bench_mp_pool              | 69.4 ms                                                             | 77.4 ms: 1.12x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.73 ms: 1.12x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.6 ms: 1.12x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.13x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.9 ms: 1.13x slower                                                          |
| pylint                     | 217 ms                                                              | 251 ms: 1.16x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 239 ms: 1.16x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 18.0 ms: 1.17x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 161 us: 1.19x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 24.0 ms: 1.19x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 96.9 ms: 1.20x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 53.3 ms: 1.21x slower                                                          |
| async_generators           | 266 ms                                                              | 320 ms: 1.21x slower                                                           |
| raytrace                   | 189 ms                                                              | 228 ms: 1.21x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.75 ms: 1.23x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 73.9 ms: 1.24x slower                                                          |
| generators                 | 21.2 ms                                                             | 28.5 ms: 1.35x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 3.09 ms: 3.13x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_none, logging_silent, pickle_pure_python, pprint_pformat, xml_etree_parse, sqlglot_parse, async_tree_memoization
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: dulwich_log

# HPT report

- Reliability score: 97.93% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown