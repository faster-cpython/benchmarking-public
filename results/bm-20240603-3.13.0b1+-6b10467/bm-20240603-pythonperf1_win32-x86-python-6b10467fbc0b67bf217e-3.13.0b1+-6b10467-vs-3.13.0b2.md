# Results vs. 3.13.0b2

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: windows-x86
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x faster
- HPT reliability: 87.20%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 230 ms: 1.01x faster                                                            |
| html5lib       | 45.4 ms                                                             | 43.9 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 224 ms: 1.02x faster                                                            |
| async_tree_io_tg           | 529 ms                                                              | 525 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| nbody          | 76.9 ms                                                             | 75.9 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 52.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 97.2 ms: 1.03x faster                                                           |
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|---------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads         | 1.65 sec                                                            | 1.58 sec: 1.04x faster                                                          |
| unpickle_list       | 2.93 us                                                             | 2.88 us: 1.02x faster                                                           |
| xml_etree_parse     | 104 ms                                                              | 103 ms: 1.02x faster                                                            |
| pickle              | 8.07 us                                                             | 7.95 us: 1.02x faster                                                           |
| xml_etree_iterparse | 64.2 ms                                                             | 63.4 ms: 1.01x faster                                                           |
| xml_etree_process   | 42.1 ms                                                             | 41.6 ms: 1.01x faster                                                           |
| xml_etree_generate  | 59.6 ms                                                             | 59.1 ms: 1.01x faster                                                           |
| pickle_list         | 3.57 us                                                             | 3.54 us: 1.01x faster                                                           |
| pickle_dict         | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| json_loads          | 20.5 us                                                             | 20.8 us: 1.01x slower                                                           |
| unpickle            | 9.79 us                                                             | 10.1 us: 1.03x slower                                                           |
| pickle_pure_python  | 213 us                                                              | 221 us: 1.04x slower                                                            |
| Geometric mean      | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): json_dumps, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 22.2 ms                                                             | 22.4 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 18.9 ms: 1.07x faster                                                           |
| genshi_xml      | 44.3 ms                                                             | 42.8 ms: 1.03x faster                                                           |
| django_template | 30.1 ms                                                             | 29.1 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240603-pythonperf1_win32-x86-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text                | 20.1 ms                                                             | 18.9 ms: 1.07x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.75 ms: 1.05x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.58 sec: 1.04x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 583 ms: 1.04x faster                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.19 sec: 1.04x faster                                                          |
| html5lib                   | 45.4 ms                                                             | 43.9 ms: 1.03x faster                                                           |
| sympy_expand               | 375 ms                                                              | 363 ms: 1.03x faster                                                            |
| genshi_xml                 | 44.3 ms                                                             | 42.8 ms: 1.03x faster                                                           |
| django_template            | 30.1 ms                                                             | 29.1 ms: 1.03x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 97.2 ms: 1.03x faster                                                           |
| logging_format             | 8.13 us                                                             | 7.93 us: 1.03x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 940 us: 1.03x faster                                                            |
| logging_simple             | 7.47 us                                                             | 7.31 us: 1.02x faster                                                           |
| sympy_str                  | 211 ms                                                              | 207 ms: 1.02x faster                                                            |
| spectral_norm              | 68.0 ms                                                             | 66.6 ms: 1.02x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.93 us: 1.02x faster                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.17 ms: 1.02x faster                                                           |
| chaos                      | 48.0 ms                                                             | 47.1 ms: 1.02x faster                                                           |
| unpickle_list              | 2.93 us                                                             | 2.88 us: 1.02x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 103 ms: 1.02x faster                                                            |
| async_tree_none            | 228 ms                                                              | 224 ms: 1.02x faster                                                            |
| raytrace                   | 189 ms                                                              | 186 ms: 1.02x faster                                                            |
| pickle                     | 8.07 us                                                             | 7.95 us: 1.02x faster                                                           |
| sympy_sum                  | 105 ms                                                              | 104 ms: 1.02x faster                                                            |
| 2to3                       | 233 ms                                                              | 230 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.4 ms: 1.01x faster                                                           |
| nbody                      | 76.9 ms                                                             | 75.9 ms: 1.01x faster                                                           |
| sympy_integrate            | 14.6 ms                                                             | 14.5 ms: 1.01x faster                                                           |
| richards_super             | 35.5 ms                                                             | 35.0 ms: 1.01x faster                                                           |
| xml_etree_process          | 42.1 ms                                                             | 41.6 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 83.1 ms: 1.01x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 59.1 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 525 ms: 1.01x faster                                                            |
| pickle_list                | 3.57 us                                                             | 3.54 us: 1.01x faster                                                           |
| nqueens                    | 68.7 ms                                                             | 68.1 ms: 1.01x faster                                                           |
| richards                   | 31.2 ms                                                             | 31.0 ms: 1.01x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                           |
| deltablue                  | 2.23 ms                                                             | 2.22 ms: 1.01x faster                                                           |
| deepcopy                   | 280 us                                                              | 278 us: 1.00x faster                                                            |
| bench_mp_pool              | 69.4 ms                                                             | 69.1 ms: 1.00x faster                                                           |
| coverage                   | 307 ms                                                              | 308 ms: 1.00x slower                                                            |
| meteor_contest             | 74.1 ms                                                             | 74.4 ms: 1.00x slower                                                           |
| thrift                     | 9.73 ms                                                             | 9.80 ms: 1.01x slower                                                           |
| float                      | 52.4 ms                                                             | 52.8 ms: 1.01x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.4 ms: 1.01x slower                                                           |
| go                         | 101 ms                                                              | 102 ms: 1.01x slower                                                            |
| generators                 | 21.2 ms                                                             | 21.4 ms: 1.01x slower                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| deepcopy_memo              | 23.5 us                                                             | 23.8 us: 1.01x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 209 ms: 1.01x slower                                                            |
| async_generators           | 266 ms                                                              | 269 ms: 1.01x slower                                                            |
| fannkuch                   | 270 ms                                                              | 274 ms: 1.02x slower                                                            |
| mdp                        | 1.60 sec                                                            | 1.63 sec: 1.02x slower                                                          |
| comprehensions             | 11.9 us                                                             | 12.1 us: 1.02x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.1 us: 1.03x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.66 us: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 486 ms: 1.03x slower                                                            |
| hexiom                     | 4.23 ms                                                             | 4.38 ms: 1.03x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 84.1 ms: 1.04x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.98 ms: 1.04x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 221 us: 1.04x slower                                                            |
| scimark_lu                 | 59.4 ms                                                             | 61.7 ms: 1.04x slower                                                           |
| scimark_fft                | 198 ms                                                              | 207 ms: 1.05x slower                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 47.5 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (28): async_tree_none_tg, async_tree_memoization, typing_runtime_protocols, crypto_pyaes, regex_effbot, bench_thread_pool, chameleon, async_tree_io, pycparser, tornado_http, async_tree_memoization_tg, docutils, create_gc_cycles, asyncio_tcp_ssl, sqlglot_optimize, json_dumps, flaskblogging, unpickle_pure_python, mako, pyflate, pylint, json, coroutines, regex_v8, python_startup_no_site, gc_traversal, logging_silent, asyncio_tcp

# HPT report

- Reliability score: 87.20% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown