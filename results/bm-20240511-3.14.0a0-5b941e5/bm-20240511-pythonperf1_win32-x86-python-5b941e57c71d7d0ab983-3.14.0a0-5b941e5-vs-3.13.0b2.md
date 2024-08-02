# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.05x faster
- HPT reliability: 59.96%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| chameleon      | 5.71 ms                                                             | 5.83 ms: 1.02x slower                                                          |
| html5lib       | 45.4 ms                                                             | 44.8 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 75.0 ms: 1.03x faster                                                          |
| float          | 52.4 ms                                                             | 52.0 ms: 1.01x faster                                                          |
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 97.3 ms: 1.03x faster                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list         | 3.57 us                                                             | 3.45 us: 1.03x faster                                                          |
| xml_etree_generate  | 59.6 ms                                                             | 58.1 ms: 1.03x faster                                                          |
| pickle              | 8.07 us                                                             | 7.92 us: 1.02x faster                                                          |
| json_loads          | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| tomli_loads         | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                         |
| xml_etree_process   | 42.1 ms                                                             | 41.7 ms: 1.01x faster                                                          |
| pickle_dict         | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| json_dumps          | 6.84 ms                                                             | 6.79 ms: 1.01x faster                                                          |
| pickle_pure_python  | 213 us                                                              | 212 us: 1.00x faster                                                           |
| xml_etree_iterparse | 64.2 ms                                                             | 63.9 ms: 1.00x faster                                                          |
| unpickle            | 9.79 us                                                             | 9.98 us: 1.02x slower                                                          |
| unpickle_list       | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| Geometric mean      | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.1 ms: 1.01x faster                                                          |
| python_startup_no_site | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.00x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako           | 6.94 ms                                                             | 6.85 ms: 1.01x faster                                                          |
| genshi_xml     | 44.3 ms                                                             | 45.1 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|--------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                   | 9.73 ms                                                             | 706 us: 13.79x faster                                                          |
| coverage                 | 307 ms                                                              | 48.7 ms: 6.30x faster                                                          |
| telco                    | 6.03 ms                                                             | 5.78 ms: 1.04x faster                                                          |
| pickle_list              | 3.57 us                                                             | 3.45 us: 1.03x faster                                                          |
| sympy_expand             | 375 ms                                                              | 364 ms: 1.03x faster                                                           |
| regex_compile            | 99.9 ms                                                             | 97.3 ms: 1.03x faster                                                          |
| xml_etree_generate       | 59.6 ms                                                             | 58.1 ms: 1.03x faster                                                          |
| nbody                    | 76.9 ms                                                             | 75.0 ms: 1.03x faster                                                          |
| raytrace                 | 189 ms                                                              | 184 ms: 1.02x faster                                                           |
| sympy_str                | 211 ms                                                              | 206 ms: 1.02x faster                                                           |
| typing_runtime_protocols | 136 us                                                              | 133 us: 1.02x faster                                                           |
| pickle                   | 8.07 us                                                             | 7.92 us: 1.02x faster                                                          |
| create_gc_cycles         | 756 us                                                              | 745 us: 1.02x faster                                                           |
| fannkuch                 | 270 ms                                                              | 266 ms: 1.01x faster                                                           |
| sympy_integrate          | 14.6 ms                                                             | 14.4 ms: 1.01x faster                                                          |
| chaos                    | 48.0 ms                                                             | 47.3 ms: 1.01x faster                                                          |
| deltablue                | 2.23 ms                                                             | 2.20 ms: 1.01x faster                                                          |
| mako                     | 6.94 ms                                                             | 6.85 ms: 1.01x faster                                                          |
| html5lib                 | 45.4 ms                                                             | 44.8 ms: 1.01x faster                                                          |
| json_loads               | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| pyflate                  | 308 ms                                                              | 304 ms: 1.01x faster                                                           |
| tomli_loads              | 1.65 sec                                                            | 1.63 sec: 1.01x faster                                                         |
| richards_super           | 35.5 ms                                                             | 35.1 ms: 1.01x faster                                                          |
| sqlite_synth             | 1.96 us                                                             | 1.94 us: 1.01x faster                                                          |
| xml_etree_process        | 42.1 ms                                                             | 41.7 ms: 1.01x faster                                                          |
| deepcopy                 | 280 us                                                              | 277 us: 1.01x faster                                                           |
| sympy_sum                | 105 ms                                                              | 104 ms: 1.01x faster                                                           |
| pickle_dict              | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| crypto_pyaes             | 55.8 ms                                                             | 55.4 ms: 1.01x faster                                                          |
| json_dumps               | 6.84 ms                                                             | 6.79 ms: 1.01x faster                                                          |
| nqueens                  | 68.7 ms                                                             | 68.2 ms: 1.01x faster                                                          |
| float                    | 52.4 ms                                                             | 52.0 ms: 1.01x faster                                                          |
| python_startup           | 22.2 ms                                                             | 22.1 ms: 1.01x faster                                                          |
| logging_format           | 8.13 us                                                             | 8.08 us: 1.01x faster                                                          |
| pickle_pure_python       | 213 us                                                              | 212 us: 1.00x faster                                                           |
| xml_etree_iterparse      | 64.2 ms                                                             | 63.9 ms: 1.00x faster                                                          |
| pprint_safe_repr         | 607 ms                                                              | 604 ms: 1.00x faster                                                           |
| comprehensions           | 11.9 us                                                             | 11.9 us: 1.00x slower                                                          |
| pidigits                 | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| logging_silent           | 57.9 ns                                                             | 58.2 ns: 1.01x slower                                                          |
| generators               | 21.2 ms                                                             | 21.3 ms: 1.01x slower                                                          |
| pycparser                | 777 ms                                                              | 782 ms: 1.01x slower                                                           |
| scimark_lu               | 59.4 ms                                                             | 59.9 ms: 1.01x slower                                                          |
| meteor_contest           | 74.1 ms                                                             | 74.8 ms: 1.01x slower                                                          |
| python_startup_no_site   | 18.2 ms                                                             | 18.4 ms: 1.01x slower                                                          |
| hexiom                   | 4.23 ms                                                             | 4.28 ms: 1.01x slower                                                          |
| json                     | 4.10 ms                                                             | 4.15 ms: 1.01x slower                                                          |
| bench_thread_pool        | 985 us                                                              | 1000 us: 1.01x slower                                                          |
| go                       | 101 ms                                                              | 102 ms: 1.02x slower                                                           |
| bench_mp_pool            | 69.4 ms                                                             | 70.6 ms: 1.02x slower                                                          |
| regex_dna                | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| genshi_xml               | 44.3 ms                                                             | 45.1 ms: 1.02x slower                                                          |
| unpickle                 | 9.79 us                                                             | 9.98 us: 1.02x slower                                                          |
| chameleon                | 5.71 ms                                                             | 5.83 ms: 1.02x slower                                                          |
| regex_effbot             | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| sqlglot_normalize        | 206 ms                                                              | 211 ms: 1.02x slower                                                           |
| unpickle_list            | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| mdp                      | 1.60 sec                                                            | 1.64 sec: 1.03x slower                                                         |
| regex_v8                 | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| deepcopy_reduce          | 2.59 us                                                             | 2.67 us: 1.03x slower                                                          |
| scimark_monte_carlo      | 45.2 ms                                                             | 46.9 ms: 1.04x slower                                                          |
| coroutines               | 15.5 ms                                                             | 16.1 ms: 1.04x slower                                                          |
| scimark_fft              | 198 ms                                                              | 206 ms: 1.04x slower                                                           |
| asyncio_tcp              | 662 ms                                                              | 694 ms: 1.05x slower                                                           |
| async_generators         | 266 ms                                                              | 279 ms: 1.05x slower                                                           |
| sqlglot_optimize         | 39.7 ms                                                             | 41.9 ms: 1.06x slower                                                          |
| pathlib                  | 83.9 ms                                                             | 88.5 ms: 1.06x slower                                                          |
| scimark_sor              | 81.0 ms                                                             | 86.2 ms: 1.06x slower                                                          |
| Geometric mean           | (ref)                                                               | 1.05x faster                                                                   |

Benchmark hidden because not significant (27): sqlglot_parse, logging_simple, async_tree_cpu_io_mixed, async_tree_none_tg, genshi_text, richards, spectral_norm, pprint_pformat, sqlglot_transpile, gc_traversal, flaskblogging, scimark_sparse_mat_mult, unpickle_pure_python, asyncio_tcp_ssl, docutils, deepcopy_memo, django_template, async_tree_io_tg, xml_etree_parse, async_tree_none, async_tree_memoization_tg, tornado_http, 2to3, async_tree_memoization, async_tree_cpu_io_mixed_tg, pylint, async_tree_io

# HPT report

- Reliability score: 59.96% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown