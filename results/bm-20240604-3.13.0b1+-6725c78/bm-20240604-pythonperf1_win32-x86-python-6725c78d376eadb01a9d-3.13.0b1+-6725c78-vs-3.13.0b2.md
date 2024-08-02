# Results vs. 3.13.0b2

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.01x slower
- HPT reliability: 95.03%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| chameleon      | 5.71 ms                                                             | 5.85 ms: 1.02x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                          |
| html5lib       | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 471 ms                                                              | 466 ms: 1.01x faster                                                            |
| Geometric mean          | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_none_tg, async_tree_io, async_tree_none, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 73.9 ms: 1.04x faster                                                           |
| float          | 52.4 ms                                                             | 52.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.97 ms: 1.05x slower                                                           |
| regex_dna      | 118 ms                                                              | 127 ms: 1.07x slower                                                            |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_list        | 2.93 us                                                             | 2.87 us: 1.02x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.4 us: 1.02x faster                                                           |
| tomli_loads          | 1.65 sec                                                            | 1.62 sec: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.01x faster                                                            |
| pickle               | 8.07 us                                                             | 8.01 us: 1.01x faster                                                           |
| unpickle_pure_python | 147 us                                                              | 146 us: 1.01x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 64.6 ms: 1.01x slower                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 60.1 ms: 1.01x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 42.4 ms: 1.01x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 6.94 ms: 1.01x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 219 us: 1.03x slower                                                            |
| json_loads           | 20.5 us                                                             | 21.1 us: 1.03x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.0 ms: 1.03x slower                                                           |
| python_startup_no_site | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 19.2 ms: 1.05x faster                                                           |
| django_template | 30.1 ms                                                             | 30.6 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|--------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text              | 20.1 ms                                                             | 19.2 ms: 1.05x faster                                                           |
| nbody                    | 76.9 ms                                                             | 73.9 ms: 1.04x faster                                                           |
| sqlglot_parse            | 964 us                                                              | 934 us: 1.03x faster                                                            |
| spectral_norm            | 68.0 ms                                                             | 66.3 ms: 1.02x faster                                                           |
| sympy_expand             | 375 ms                                                              | 367 ms: 1.02x faster                                                            |
| unpickle_list            | 2.93 us                                                             | 2.87 us: 1.02x faster                                                           |
| sqlglot_transpile        | 1.19 ms                                                             | 1.17 ms: 1.02x faster                                                           |
| bench_thread_pool        | 985 us                                                              | 969 us: 1.02x faster                                                            |
| pickle_dict              | 20.8 us                                                             | 20.4 us: 1.02x faster                                                           |
| fannkuch                 | 270 ms                                                              | 266 ms: 1.02x faster                                                            |
| richards_super           | 35.5 ms                                                             | 34.9 ms: 1.02x faster                                                           |
| tomli_loads              | 1.65 sec                                                            | 1.62 sec: 1.01x faster                                                          |
| create_gc_cycles         | 756 us                                                              | 745 us: 1.01x faster                                                            |
| docutils                 | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                          |
| async_tree_cpu_io_mixed  | 471 ms                                                              | 466 ms: 1.01x faster                                                            |
| coverage                 | 307 ms                                                              | 304 ms: 1.01x faster                                                            |
| sympy_str                | 211 ms                                                              | 209 ms: 1.01x faster                                                            |
| xml_etree_parse          | 104 ms                                                              | 103 ms: 1.01x faster                                                            |
| pickle                   | 8.07 us                                                             | 8.01 us: 1.01x faster                                                           |
| html5lib                 | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                           |
| pathlib                  | 83.9 ms                                                             | 83.3 ms: 1.01x faster                                                           |
| unpickle_pure_python     | 147 us                                                              | 146 us: 1.01x faster                                                            |
| deepcopy_memo            | 23.5 us                                                             | 23.4 us: 1.01x faster                                                           |
| pyflate                  | 308 ms                                                              | 307 ms: 1.00x faster                                                            |
| scimark_sor              | 81.0 ms                                                             | 80.6 ms: 1.00x faster                                                           |
| logging_silent           | 57.9 ns                                                             | 58.2 ns: 1.01x slower                                                           |
| float                    | 52.4 ms                                                             | 52.6 ms: 1.01x slower                                                           |
| sqlglot_normalize        | 206 ms                                                              | 207 ms: 1.01x slower                                                            |
| crypto_pyaes             | 55.8 ms                                                             | 56.1 ms: 1.01x slower                                                           |
| xml_etree_iterparse      | 64.2 ms                                                             | 64.6 ms: 1.01x slower                                                           |
| thrift                   | 9.73 ms                                                             | 9.80 ms: 1.01x slower                                                           |
| generators               | 21.2 ms                                                             | 21.3 ms: 1.01x slower                                                           |
| pprint_safe_repr         | 607 ms                                                              | 611 ms: 1.01x slower                                                            |
| pprint_pformat           | 1.24 sec                                                            | 1.25 sec: 1.01x slower                                                          |
| xml_etree_generate       | 59.6 ms                                                             | 60.1 ms: 1.01x slower                                                           |
| xml_etree_process        | 42.1 ms                                                             | 42.4 ms: 1.01x slower                                                           |
| sympy_integrate          | 14.6 ms                                                             | 14.8 ms: 1.01x slower                                                           |
| meteor_contest           | 74.1 ms                                                             | 74.7 ms: 1.01x slower                                                           |
| nqueens                  | 68.7 ms                                                             | 69.3 ms: 1.01x slower                                                           |
| deepcopy                 | 280 us                                                              | 282 us: 1.01x slower                                                            |
| go                       | 101 ms                                                              | 102 ms: 1.01x slower                                                            |
| scimark_lu               | 59.4 ms                                                             | 60.0 ms: 1.01x slower                                                           |
| sqlglot_optimize         | 39.7 ms                                                             | 40.2 ms: 1.01x slower                                                           |
| pycparser                | 777 ms                                                              | 786 ms: 1.01x slower                                                            |
| logging_format           | 8.13 us                                                             | 8.23 us: 1.01x slower                                                           |
| deepcopy_reduce          | 2.59 us                                                             | 2.63 us: 1.01x slower                                                           |
| json_dumps               | 6.84 ms                                                             | 6.94 ms: 1.01x slower                                                           |
| comprehensions           | 11.9 us                                                             | 12.0 us: 1.02x slower                                                           |
| hexiom                   | 4.23 ms                                                             | 4.30 ms: 1.02x slower                                                           |
| sqlite_synth             | 1.96 us                                                             | 2.00 us: 1.02x slower                                                           |
| django_template          | 30.1 ms                                                             | 30.6 ms: 1.02x slower                                                           |
| async_generators         | 266 ms                                                              | 271 ms: 1.02x slower                                                            |
| logging_simple           | 7.47 us                                                             | 7.61 us: 1.02x slower                                                           |
| telco                    | 6.03 ms                                                             | 6.15 ms: 1.02x slower                                                           |
| typing_runtime_protocols | 136 us                                                              | 139 us: 1.02x slower                                                            |
| pickle_list              | 3.57 us                                                             | 3.65 us: 1.02x slower                                                           |
| chameleon                | 5.71 ms                                                             | 5.85 ms: 1.02x slower                                                           |
| pickle_pure_python       | 213 us                                                              | 219 us: 1.03x slower                                                            |
| json_loads               | 20.5 us                                                             | 21.1 us: 1.03x slower                                                           |
| python_startup           | 22.2 ms                                                             | 23.0 ms: 1.03x slower                                                           |
| asyncio_tcp              | 662 ms                                                              | 686 ms: 1.04x slower                                                            |
| unpickle                 | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| python_startup_no_site   | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                           |
| scimark_fft              | 198 ms                                                              | 207 ms: 1.04x slower                                                            |
| mdp                      | 1.60 sec                                                            | 1.67 sec: 1.04x slower                                                          |
| regex_effbot             | 1.88 ms                                                             | 1.97 ms: 1.05x slower                                                           |
| json                     | 4.10 ms                                                             | 4.36 ms: 1.06x slower                                                           |
| regex_dna                | 118 ms                                                              | 127 ms: 1.07x slower                                                            |
| Geometric mean           | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (27): scimark_sparse_mat_mult, gc_traversal, async_tree_cpu_io_mixed_tg, scimark_monte_carlo, coroutines, richards, asyncio_tcp_ssl, deltablue, tornado_http, async_tree_io_tg, async_tree_none_tg, chaos, 2to3, regex_compile, pidigits, flaskblogging, sympy_sum, bench_mp_pool, async_tree_io, regex_v8, pylint, genshi_xml, mako, raytrace, async_tree_none, async_tree_memoization_tg, async_tree_memoization

# HPT report

- Reliability score: 95.03% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown