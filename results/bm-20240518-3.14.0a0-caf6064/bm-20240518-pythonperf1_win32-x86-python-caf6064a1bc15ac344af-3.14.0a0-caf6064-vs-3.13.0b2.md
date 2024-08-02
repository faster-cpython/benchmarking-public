# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.04x faster
- HPT reliability: 74.08%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 235 ms: 1.01x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.80 sec: 1.00x faster                                                         |
| html5lib       | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 496 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 475 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_none_tg, async_tree_none, async_tree_io, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 53.5 ms: 1.02x slower                                                          |
| nbody          | 76.9 ms                                                             | 78.9 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 97.6 ms: 1.02x faster                                                          |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.02x faster                                                           |
| pickle_list          | 3.57 us                                                             | 3.51 us: 1.02x faster                                                          |
| pickle               | 8.07 us                                                             | 7.97 us: 1.01x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.5 ms: 1.01x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.64 sec: 1.01x faster                                                         |
| pickle_dict          | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 42.5 ms: 1.01x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 150 us: 1.02x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.04 ms: 1.03x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.03 us: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 223 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.0 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_text     | 20.1 ms                                                             | 19.3 ms: 1.04x faster                                                          |
| django_template | 30.1 ms                                                             | 29.4 ms: 1.02x faster                                                          |
| mako            | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 709 us: 13.72x faster                                                          |
| coverage                   | 307 ms                                                              | 50.9 ms: 6.04x faster                                                          |
| genshi_text                | 20.1 ms                                                             | 19.3 ms: 1.04x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 732 us: 1.03x faster                                                           |
| sympy_str                  | 211 ms                                                              | 205 ms: 1.03x faster                                                           |
| sympy_expand               | 375 ms                                                              | 365 ms: 1.03x faster                                                           |
| raytrace                   | 189 ms                                                              | 183 ms: 1.03x faster                                                           |
| chaos                      | 48.0 ms                                                             | 46.6 ms: 1.03x faster                                                          |
| regex_compile              | 99.9 ms                                                             | 97.6 ms: 1.02x faster                                                          |
| django_template            | 30.1 ms                                                             | 29.4 ms: 1.02x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 54.6 ms: 1.02x faster                                                          |
| typing_runtime_protocols   | 136 us                                                              | 133 us: 1.02x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 103 ms: 1.02x faster                                                           |
| html5lib                   | 45.4 ms                                                             | 44.7 ms: 1.02x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.51 us: 1.02x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.93 us: 1.02x faster                                                          |
| bench_thread_pool          | 985 us                                                              | 969 us: 1.02x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.22 sec: 1.02x faster                                                         |
| pprint_safe_repr           | 607 ms                                                              | 599 ms: 1.01x faster                                                           |
| sympy_sum                  | 105 ms                                                              | 104 ms: 1.01x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.97 us: 1.01x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.5 ms: 1.01x faster                                                          |
| sqlglot_parse              | 964 us                                                              | 954 us: 1.01x faster                                                           |
| sqlglot_normalize          | 206 ms                                                              | 204 ms: 1.01x faster                                                           |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.64 sec: 1.01x faster                                                         |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.8 us: 1.01x faster                                                          |
| deltablue                  | 2.23 ms                                                             | 2.22 ms: 1.00x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| docutils                   | 1.81 sec                                                            | 1.80 sec: 1.00x faster                                                         |
| sqlglot_optimize           | 39.7 ms                                                             | 39.6 ms: 1.00x faster                                                          |
| mdp                        | 1.60 sec                                                            | 1.61 sec: 1.00x slower                                                         |
| xml_etree_generate         | 59.6 ms                                                             | 60.0 ms: 1.01x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 68.4 ms: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| pyflate                    | 308 ms                                                              | 310 ms: 1.01x slower                                                           |
| richards                   | 31.2 ms                                                             | 31.5 ms: 1.01x slower                                                          |
| 2to3                       | 233 ms                                                              | 235 ms: 1.01x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 42.5 ms: 1.01x slower                                                          |
| json                       | 4.10 ms                                                             | 4.16 ms: 1.02x slower                                                          |
| go                         | 101 ms                                                              | 102 ms: 1.02x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 75.3 ms: 1.02x slower                                                          |
| python_startup             | 22.2 ms                                                             | 22.6 ms: 1.02x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 150 us: 1.02x slower                                                           |
| float                      | 52.4 ms                                                             | 53.5 ms: 1.02x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.31 us: 1.02x slower                                                          |
| pycparser                  | 777 ms                                                              | 795 ms: 1.02x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 85.8 ms: 1.02x slower                                                          |
| generators                 | 21.2 ms                                                             | 21.7 ms: 1.02x slower                                                          |
| mako                       | 6.94 ms                                                             | 7.12 ms: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.66 us: 1.03x slower                                                          |
| nbody                      | 76.9 ms                                                             | 78.9 ms: 1.03x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 61.0 ms: 1.03x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.95 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.66 us: 1.03x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.04 ms: 1.03x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.03 us: 1.04x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.38 ms: 1.04x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 71.9 ms: 1.04x slower                                                          |
| async_generators           | 266 ms                                                              | 276 ms: 1.04x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.28 ms: 1.04x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 16.1 ms: 1.04x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| scimark_fft                | 198 ms                                                              | 207 ms: 1.04x slower                                                           |
| deepcopy                   | 280 us                                                              | 292 us: 1.05x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.0 ms: 1.05x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 223 us: 1.05x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 24.6 us: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 496 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 475 ms: 1.06x slower                                                           |
| fannkuch                   | 270 ms                                                              | 288 ms: 1.07x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 48.3 ms: 1.07x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 91.4 ms: 1.13x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (21): asyncio_tcp, sympy_integrate, async_tree_io_tg, chameleon, tornado_http, gc_traversal, richards_super, nqueens, json_loads, asyncio_tcp_ssl, flaskblogging, async_tree_none_tg, logging_silent, sqlglot_transpile, async_tree_none, regex_v8, pylint, genshi_xml, async_tree_io, async_tree_memoization, async_tree_memoization_tg

# HPT report

- Reliability score: 74.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown