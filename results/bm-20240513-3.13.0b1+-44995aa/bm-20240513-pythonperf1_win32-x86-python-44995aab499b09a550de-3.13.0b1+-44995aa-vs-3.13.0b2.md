# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.01x slower
- HPT reliability: 88.90%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 236 ms: 1.01x slower                                                            |
| html5lib       | 45.4 ms                                                             | 44.9 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg, async_tree_io_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| nbody          | 76.9 ms                                                             | 76.2 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 101 ms: 1.01x slower                                                            |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                           |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| xml_etree_generate   | 59.6 ms                                                             | 58.5 ms: 1.02x faster                                                           |
| tomli_loads          | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.2 ms: 1.02x faster                                                           |
| xml_etree_process    | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                           |
| pickle_list          | 3.57 us                                                             | 3.52 us: 1.01x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.7 us: 1.00x faster                                                           |
| pickle               | 8.07 us                                                             | 8.12 us: 1.01x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 218 us: 1.02x slower                                                            |
| unpickle_pure_python | 147 us                                                              | 151 us: 1.03x slower                                                            |
| unpickle_list        | 2.93 us                                                             | 3.07 us: 1.05x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.6 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                             | 22.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 6.99 ms: 1.01x slower                                                           |
| genshi_text     | 20.1 ms                                                             | 20.3 ms: 1.01x slower                                                           |
| django_template | 30.1 ms                                                             | 31.0 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|--------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| raytrace                 | 189 ms                                                              | 182 ms: 1.03x faster                                                            |
| create_gc_cycles         | 756 us                                                              | 737 us: 1.03x faster                                                            |
| xml_etree_parse          | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| scimark_sparse_mat_mult  | 2.87 ms                                                             | 2.82 ms: 1.02x faster                                                           |
| fannkuch                 | 270 ms                                                              | 265 ms: 1.02x faster                                                            |
| xml_etree_generate       | 59.6 ms                                                             | 58.5 ms: 1.02x faster                                                           |
| async_generators         | 266 ms                                                              | 261 ms: 1.02x faster                                                            |
| tomli_loads              | 1.65 sec                                                            | 1.62 sec: 1.02x faster                                                          |
| crypto_pyaes             | 55.8 ms                                                             | 54.9 ms: 1.02x faster                                                           |
| sympy_str                | 211 ms                                                              | 208 ms: 1.02x faster                                                            |
| xml_etree_iterparse      | 64.2 ms                                                             | 63.2 ms: 1.02x faster                                                           |
| xml_etree_process        | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                           |
| comprehensions           | 11.9 us                                                             | 11.7 us: 1.01x faster                                                           |
| sympy_expand             | 375 ms                                                              | 370 ms: 1.01x faster                                                            |
| pickle_list              | 3.57 us                                                             | 3.52 us: 1.01x faster                                                           |
| html5lib                 | 45.4 ms                                                             | 44.9 ms: 1.01x faster                                                           |
| pidigits                 | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| meteor_contest           | 74.1 ms                                                             | 73.3 ms: 1.01x faster                                                           |
| nbody                    | 76.9 ms                                                             | 76.2 ms: 1.01x faster                                                           |
| deltablue                | 2.23 ms                                                             | 2.22 ms: 1.01x faster                                                           |
| python_startup           | 22.2 ms                                                             | 22.1 ms: 1.01x faster                                                           |
| pyflate                  | 308 ms                                                              | 307 ms: 1.01x faster                                                            |
| telco                    | 6.03 ms                                                             | 6.01 ms: 1.00x faster                                                           |
| pickle_dict              | 20.8 us                                                             | 20.7 us: 1.00x faster                                                           |
| pprint_pformat           | 1.24 sec                                                            | 1.24 sec: 1.00x slower                                                          |
| generators               | 21.2 ms                                                             | 21.2 ms: 1.00x slower                                                           |
| pprint_safe_repr         | 607 ms                                                              | 610 ms: 1.00x slower                                                            |
| pickle                   | 8.07 us                                                             | 8.12 us: 1.01x slower                                                           |
| mako                     | 6.94 ms                                                             | 6.99 ms: 1.01x slower                                                           |
| genshi_text              | 20.1 ms                                                             | 20.3 ms: 1.01x slower                                                           |
| nqueens                  | 68.7 ms                                                             | 69.2 ms: 1.01x slower                                                           |
| coverage                 | 307 ms                                                              | 310 ms: 1.01x slower                                                            |
| regex_effbot             | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                           |
| deepcopy                 | 280 us                                                              | 282 us: 1.01x slower                                                            |
| sqlglot_optimize         | 39.7 ms                                                             | 40.2 ms: 1.01x slower                                                           |
| gc_traversal             | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                           |
| regex_compile            | 99.9 ms                                                             | 101 ms: 1.01x slower                                                            |
| 2to3                     | 233 ms                                                              | 236 ms: 1.01x slower                                                            |
| regex_v8                 | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                           |
| richards                 | 31.2 ms                                                             | 31.7 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 206 ms                                                              | 209 ms: 1.02x slower                                                            |
| typing_runtime_protocols | 136 us                                                              | 138 us: 1.02x slower                                                            |
| regex_dna                | 118 ms                                                              | 120 ms: 1.02x slower                                                            |
| json                     | 4.10 ms                                                             | 4.17 ms: 1.02x slower                                                           |
| logging_format           | 8.13 us                                                             | 8.30 us: 1.02x slower                                                           |
| scimark_sor              | 81.0 ms                                                             | 82.6 ms: 1.02x slower                                                           |
| logging_simple           | 7.47 us                                                             | 7.63 us: 1.02x slower                                                           |
| pickle_pure_python       | 213 us                                                              | 218 us: 1.02x slower                                                            |
| chaos                    | 48.0 ms                                                             | 49.2 ms: 1.03x slower                                                           |
| bench_mp_pool            | 69.4 ms                                                             | 71.2 ms: 1.03x slower                                                           |
| pycparser                | 777 ms                                                              | 798 ms: 1.03x slower                                                            |
| unpickle_pure_python     | 147 us                                                              | 151 us: 1.03x slower                                                            |
| mdp                      | 1.60 sec                                                            | 1.65 sec: 1.03x slower                                                          |
| go                       | 101 ms                                                              | 104 ms: 1.03x slower                                                            |
| django_template          | 30.1 ms                                                             | 31.0 ms: 1.03x slower                                                           |
| coroutines               | 15.5 ms                                                             | 16.0 ms: 1.04x slower                                                           |
| thrift                   | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                                           |
| scimark_fft              | 198 ms                                                              | 207 ms: 1.04x slower                                                            |
| deepcopy_reduce          | 2.59 us                                                             | 2.70 us: 1.04x slower                                                           |
| hexiom                   | 4.23 ms                                                             | 4.43 ms: 1.05x slower                                                           |
| unpickle_list            | 2.93 us                                                             | 3.07 us: 1.05x slower                                                           |
| pathlib                  | 83.9 ms                                                             | 88.7 ms: 1.06x slower                                                           |
| unpickle                 | 9.79 us                                                             | 10.6 us: 1.08x slower                                                           |
| asyncio_tcp              | 662 ms                                                              | 734 ms: 1.11x slower                                                            |
| Geometric mean           | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (31): async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, sqlglot_parse, scimark_lu, async_tree_none, sympy_sum, sqlite_synth, flaskblogging, docutils, spectral_norm, async_tree_memoization_tg, float, async_tree_io_tg, chameleon, genshi_xml, asyncio_tcp_ssl, deepcopy_memo, sqlglot_transpile, async_tree_memoization, sympy_integrate, python_startup_no_site, bench_thread_pool, logging_silent, tornado_http, json_loads, async_tree_io, json_dumps, richards_super, scimark_monte_carlo, pylint

# HPT report

- Reliability score: 88.90% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown