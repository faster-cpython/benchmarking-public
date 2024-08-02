# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: windows-x86
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.00x faster
- HPT reliability: 57.94%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| html5lib       | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 52.4 ms                                                             | 53.1 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 99.0 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| regex_dna      | 118 ms                                                              | 122 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|---------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list       | 2.93 us                                                             | 2.73 us: 1.07x faster                                                           |
| xml_etree_parse     | 104 ms                                                              | 101 ms: 1.03x faster                                                            |
| tomli_loads         | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                          |
| xml_etree_iterparse | 64.2 ms                                                             | 63.1 ms: 1.02x faster                                                           |
| xml_etree_generate  | 59.6 ms                                                             | 58.6 ms: 1.02x faster                                                           |
| xml_etree_process   | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                           |
| pickle_dict         | 20.8 us                                                             | 20.4 us: 1.02x faster                                                           |
| pickle              | 8.07 us                                                             | 7.99 us: 1.01x faster                                                           |
| json_loads          | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| pickle_pure_python  | 213 us                                                              | 215 us: 1.01x slower                                                            |
| pickle_list         | 3.57 us                                                             | 3.63 us: 1.02x slower                                                           |
| json_dumps          | 6.84 ms                                                             | 6.99 ms: 1.02x slower                                                           |
| unpickle            | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| Geometric mean      | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                           |
| python_startup         | 22.2 ms                                                             | 22.8 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 20.1 ms                                                             | 19.5 ms: 1.03x faster                                                           |
| genshi_xml     | 44.3 ms                                                             | 43.5 ms: 1.02x faster                                                           |
| mako           | 6.94 ms                                                             | 6.83 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf1_win32-x86-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list            | 2.93 us                                                             | 2.73 us: 1.07x faster                                                           |
| pprint_safe_repr         | 607 ms                                                              | 576 ms: 1.05x faster                                                            |
| pprint_pformat           | 1.24 sec                                                            | 1.18 sec: 1.05x faster                                                          |
| xml_etree_parse          | 104 ms                                                              | 101 ms: 1.03x faster                                                            |
| typing_runtime_protocols | 136 us                                                              | 131 us: 1.03x faster                                                            |
| sqlglot_parse            | 964 us                                                              | 934 us: 1.03x faster                                                            |
| sympy_expand             | 375 ms                                                              | 364 ms: 1.03x faster                                                            |
| genshi_text              | 20.1 ms                                                             | 19.5 ms: 1.03x faster                                                           |
| spectral_norm            | 68.0 ms                                                             | 66.0 ms: 1.03x faster                                                           |
| nqueens                  | 68.7 ms                                                             | 66.7 ms: 1.03x faster                                                           |
| tomli_loads              | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                          |
| sympy_str                | 211 ms                                                              | 207 ms: 1.02x faster                                                            |
| deltablue                | 2.23 ms                                                             | 2.19 ms: 1.02x faster                                                           |
| xml_etree_iterparse      | 64.2 ms                                                             | 63.1 ms: 1.02x faster                                                           |
| xml_etree_generate       | 59.6 ms                                                             | 58.6 ms: 1.02x faster                                                           |
| xml_etree_process        | 42.1 ms                                                             | 41.4 ms: 1.02x faster                                                           |
| genshi_xml               | 44.3 ms                                                             | 43.5 ms: 1.02x faster                                                           |
| deepcopy_reduce          | 2.59 us                                                             | 2.55 us: 1.02x faster                                                           |
| sqlglot_transpile        | 1.19 ms                                                             | 1.17 ms: 1.02x faster                                                           |
| html5lib                 | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                           |
| mako                     | 6.94 ms                                                             | 6.83 ms: 1.02x faster                                                           |
| pickle_dict              | 20.8 us                                                             | 20.4 us: 1.02x faster                                                           |
| richards_super           | 35.5 ms                                                             | 35.0 ms: 1.01x faster                                                           |
| sympy_sum                | 105 ms                                                              | 104 ms: 1.01x faster                                                            |
| sympy_integrate          | 14.6 ms                                                             | 14.5 ms: 1.01x faster                                                           |
| sqlite_synth             | 1.96 us                                                             | 1.94 us: 1.01x faster                                                           |
| telco                    | 6.03 ms                                                             | 5.96 ms: 1.01x faster                                                           |
| pickle                   | 8.07 us                                                             | 7.99 us: 1.01x faster                                                           |
| coroutines               | 15.5 ms                                                             | 15.3 ms: 1.01x faster                                                           |
| deepcopy                 | 280 us                                                              | 277 us: 1.01x faster                                                            |
| logging_format           | 8.13 us                                                             | 8.05 us: 1.01x faster                                                           |
| create_gc_cycles         | 756 us                                                              | 748 us: 1.01x faster                                                            |
| regex_compile            | 99.9 ms                                                             | 99.0 ms: 1.01x faster                                                           |
| richards                 | 31.2 ms                                                             | 31.0 ms: 1.01x faster                                                           |
| pathlib                  | 83.9 ms                                                             | 83.3 ms: 1.01x faster                                                           |
| comprehensions           | 11.9 us                                                             | 11.8 us: 1.01x faster                                                           |
| meteor_contest           | 74.1 ms                                                             | 73.7 ms: 1.00x faster                                                           |
| generators               | 21.2 ms                                                             | 21.3 ms: 1.00x slower                                                           |
| pyflate                  | 308 ms                                                              | 310 ms: 1.00x slower                                                            |
| json_loads               | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| scimark_sor              | 81.0 ms                                                             | 81.7 ms: 1.01x slower                                                           |
| pickle_pure_python       | 213 us                                                              | 215 us: 1.01x slower                                                            |
| regex_v8                 | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                           |
| scimark_fft              | 198 ms                                                              | 201 ms: 1.01x slower                                                            |
| go                       | 101 ms                                                              | 102 ms: 1.01x slower                                                            |
| float                    | 52.4 ms                                                             | 53.1 ms: 1.01x slower                                                           |
| json                     | 4.10 ms                                                             | 4.16 ms: 1.01x slower                                                           |
| regex_effbot             | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| thrift                   | 9.73 ms                                                             | 9.88 ms: 1.02x slower                                                           |
| pickle_list              | 3.57 us                                                             | 3.63 us: 1.02x slower                                                           |
| json_dumps               | 6.84 ms                                                             | 6.99 ms: 1.02x slower                                                           |
| python_startup_no_site   | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                           |
| mdp                      | 1.60 sec                                                            | 1.64 sec: 1.03x slower                                                          |
| sqlglot_normalize        | 206 ms                                                              | 211 ms: 1.03x slower                                                            |
| python_startup           | 22.2 ms                                                             | 22.8 ms: 1.03x slower                                                           |
| async_generators         | 266 ms                                                              | 273 ms: 1.03x slower                                                            |
| sqlglot_optimize         | 39.7 ms                                                             | 40.8 ms: 1.03x slower                                                           |
| hexiom                   | 4.23 ms                                                             | 4.35 ms: 1.03x slower                                                           |
| deepcopy_memo            | 23.5 us                                                             | 24.2 us: 1.03x slower                                                           |
| regex_dna                | 118 ms                                                              | 122 ms: 1.03x slower                                                            |
| chaos                    | 48.0 ms                                                             | 49.5 ms: 1.03x slower                                                           |
| unpickle                 | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| fannkuch                 | 270 ms                                                              | 281 ms: 1.04x slower                                                            |
| scimark_monte_carlo      | 45.2 ms                                                             | 47.1 ms: 1.04x slower                                                           |
| Geometric mean           | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (31): scimark_sparse_mat_mult, tornado_http, async_tree_memoization, async_tree_none, asyncio_tcp_ssl, pycparser, async_tree_cpu_io_mixed_tg, coverage, bench_thread_pool, docutils, flaskblogging, logging_silent, 2to3, logging_simple, pylint, unpickle_pure_python, pidigits, crypto_pyaes, scimark_lu, gc_traversal, django_template, chameleon, raytrace, async_tree_cpu_io_mixed, bench_mp_pool, nbody, async_tree_memoization_tg, async_tree_io_tg, async_tree_io, async_tree_none_tg, asyncio_tcp

# HPT report

- Reliability score: 57.94% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown