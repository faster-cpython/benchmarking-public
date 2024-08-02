# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.04x faster
- HPT reliability: 89.45%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| html5lib       | 45.4 ms                                                             | 45.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (4): 2to3, chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg        | 529 ms                                                              | 534 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed | 471 ms                                                              | 476 ms: 1.01x slower                                                           |
| Geometric mean          | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_io, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 76.4 ms: 1.01x faster                                                          |
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 116 ms: 1.02x faster                                                           |
| regex_compile  | 99.9 ms                                                             | 98.9 ms: 1.01x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.8 ms: 1.01x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.9 us: 1.01x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 148 us: 1.01x slower                                                           |
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| pickle               | 8.07 us                                                             | 8.15 us: 1.01x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 2.97 us: 1.01x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 6.95 ms: 1.02x slower                                                          |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| pickle_list          | 3.57 us                                                             | 3.63 us: 1.02x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 42.9 ms: 1.02x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 221 us: 1.04x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                          |
| python_startup         | 22.2 ms                                                             | 22.8 ms: 1.03x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 19.1 ms: 1.05x faster                                                          |
| django_template | 30.1 ms                                                             | 30.4 ms: 1.01x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                   | 9.73 ms                                                             | 682 us: 14.27x faster                                                          |
| coverage                 | 307 ms                                                              | 48.4 ms: 6.35x faster                                                          |
| genshi_text              | 20.1 ms                                                             | 19.1 ms: 1.05x faster                                                          |
| sympy_expand             | 375 ms                                                              | 361 ms: 1.04x faster                                                           |
| richards_super           | 35.5 ms                                                             | 34.2 ms: 1.04x faster                                                          |
| nqueens                  | 68.7 ms                                                             | 66.5 ms: 1.03x faster                                                          |
| chaos                    | 48.0 ms                                                             | 46.7 ms: 1.03x faster                                                          |
| spectral_norm            | 68.0 ms                                                             | 66.2 ms: 1.03x faster                                                          |
| tomli_loads              | 1.65 sec                                                            | 1.60 sec: 1.03x faster                                                         |
| crypto_pyaes             | 55.8 ms                                                             | 54.4 ms: 1.03x faster                                                          |
| sympy_str                | 211 ms                                                              | 206 ms: 1.03x faster                                                           |
| scimark_sparse_mat_mult  | 2.87 ms                                                             | 2.80 ms: 1.02x faster                                                          |
| richards                 | 31.2 ms                                                             | 30.5 ms: 1.02x faster                                                          |
| typing_runtime_protocols | 136 us                                                              | 133 us: 1.02x faster                                                           |
| scimark_lu               | 59.4 ms                                                             | 58.3 ms: 1.02x faster                                                          |
| regex_dna                | 118 ms                                                              | 116 ms: 1.02x faster                                                           |
| raytrace                 | 189 ms                                                              | 185 ms: 1.02x faster                                                           |
| sympy_sum                | 105 ms                                                              | 104 ms: 1.01x faster                                                           |
| sqlglot_normalize        | 206 ms                                                              | 204 ms: 1.01x faster                                                           |
| html5lib                 | 45.4 ms                                                             | 45.0 ms: 1.01x faster                                                          |
| regex_compile            | 99.9 ms                                                             | 98.9 ms: 1.01x faster                                                          |
| sqlite_synth             | 1.96 us                                                             | 1.94 us: 1.01x faster                                                          |
| nbody                    | 76.9 ms                                                             | 76.4 ms: 1.01x faster                                                          |
| xml_etree_iterparse      | 64.2 ms                                                             | 63.8 ms: 1.01x faster                                                          |
| sympy_integrate          | 14.6 ms                                                             | 14.6 ms: 1.00x faster                                                          |
| fannkuch                 | 270 ms                                                              | 269 ms: 1.00x faster                                                           |
| sqlglot_optimize         | 39.7 ms                                                             | 39.6 ms: 1.00x faster                                                          |
| pidigits                 | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| meteor_contest           | 74.1 ms                                                             | 74.4 ms: 1.00x slower                                                          |
| pickle_dict              | 20.8 us                                                             | 20.9 us: 1.01x slower                                                          |
| comprehensions           | 11.9 us                                                             | 11.9 us: 1.01x slower                                                          |
| pprint_pformat           | 1.24 sec                                                            | 1.25 sec: 1.01x slower                                                         |
| logging_format           | 8.13 us                                                             | 8.19 us: 1.01x slower                                                          |
| xml_etree_generate       | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                          |
| async_tree_io_tg         | 529 ms                                                              | 534 ms: 1.01x slower                                                           |
| unpickle_pure_python     | 147 us                                                              | 148 us: 1.01x slower                                                           |
| xml_etree_parse          | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| regex_v8                 | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| pickle                   | 8.07 us                                                             | 8.15 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed  | 471 ms                                                              | 476 ms: 1.01x slower                                                           |
| pyflate                  | 308 ms                                                              | 311 ms: 1.01x slower                                                           |
| django_template          | 30.1 ms                                                             | 30.4 ms: 1.01x slower                                                          |
| deltablue                | 2.23 ms                                                             | 2.26 ms: 1.01x slower                                                          |
| deepcopy                 | 280 us                                                              | 283 us: 1.01x slower                                                           |
| pycparser                | 777 ms                                                              | 788 ms: 1.01x slower                                                           |
| unpickle_list            | 2.93 us                                                             | 2.97 us: 1.01x slower                                                          |
| generators               | 21.2 ms                                                             | 21.5 ms: 1.02x slower                                                          |
| json_dumps               | 6.84 ms                                                             | 6.95 ms: 1.02x slower                                                          |
| json_loads               | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| pickle_list              | 3.57 us                                                             | 3.63 us: 1.02x slower                                                          |
| mdp                      | 1.60 sec                                                            | 1.63 sec: 1.02x slower                                                         |
| xml_etree_process        | 42.1 ms                                                             | 42.9 ms: 1.02x slower                                                          |
| python_startup_no_site   | 18.2 ms                                                             | 18.6 ms: 1.02x slower                                                          |
| async_generators         | 266 ms                                                              | 271 ms: 1.02x slower                                                           |
| hexiom                   | 4.23 ms                                                             | 4.33 ms: 1.02x slower                                                          |
| coroutines               | 15.5 ms                                                             | 15.9 ms: 1.02x slower                                                          |
| scimark_monte_carlo      | 45.2 ms                                                             | 46.3 ms: 1.03x slower                                                          |
| bench_mp_pool            | 69.4 ms                                                             | 71.2 ms: 1.03x slower                                                          |
| deepcopy_reduce          | 2.59 us                                                             | 2.66 us: 1.03x slower                                                          |
| scimark_fft              | 198 ms                                                              | 203 ms: 1.03x slower                                                           |
| python_startup           | 22.2 ms                                                             | 22.8 ms: 1.03x slower                                                          |
| telco                    | 6.03 ms                                                             | 6.20 ms: 1.03x slower                                                          |
| go                       | 101 ms                                                              | 104 ms: 1.04x slower                                                           |
| pickle_pure_python       | 213 us                                                              | 221 us: 1.04x slower                                                           |
| json                     | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                          |
| pathlib                  | 83.9 ms                                                             | 87.5 ms: 1.04x slower                                                          |
| scimark_sor              | 81.0 ms                                                             | 85.0 ms: 1.05x slower                                                          |
| unpickle                 | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| Geometric mean           | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (27): bench_thread_pool, create_gc_cycles, async_tree_io, async_tree_none, logging_silent, genshi_xml, flaskblogging, mako, asyncio_tcp_ssl, sqlglot_transpile, logging_simple, docutils, chameleon, pprint_safe_repr, deepcopy_memo, 2to3, sqlglot_parse, async_tree_memoization, regex_effbot, pylint, float, tornado_http, gc_traversal, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, asyncio_tcp

# HPT report

- Reliability score: 89.45% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown