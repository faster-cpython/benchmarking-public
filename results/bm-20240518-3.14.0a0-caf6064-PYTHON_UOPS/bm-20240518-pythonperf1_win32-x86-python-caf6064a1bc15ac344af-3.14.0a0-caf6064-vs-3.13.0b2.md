# Results vs. 3.13.0b2

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.62 ms: 1.16x slower                                                          |
| docutils       | 1.81 sec                                                            | 2.02 sec: 1.12x slower                                                         |
| html5lib       | 45.4 ms                                                             | 50.5 ms: 1.11x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 99.4 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 544 ms: 1.03x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.03x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 498 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 80.5 ms: 1.05x slower                                                          |
| float          | 52.4 ms                                                             | 56.6 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_dna      | 118 ms                                                              | 125 ms: 1.06x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 127 ms: 1.27x slower                                                           |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| pickle_list          | 3.57 us                                                             | 3.59 us: 1.01x slower                                                          |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.67 sec: 1.02x slower                                                         |
| json_dumps           | 6.84 ms                                                             | 7.00 ms: 1.02x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 61.5 ms: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.9 ms: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.05x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 44.6 ms: 1.06x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.11 us: 1.06x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 254 us: 1.19x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 181 us: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.05x slower                                                                   |

Benchmark hidden because not significant (2): xml_etree_parse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.7 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.0 ms: 1.09x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.1 ms: 1.10x slower                                                          |
| django_template | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| mako            | 6.94 ms                                                             | 7.84 ms: 1.13x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 727 us: 13.39x faster                                                          |
| coverage                   | 307 ms                                                              | 48.9 ms: 6.28x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 634 ms: 1.04x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.90 us: 1.03x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.59 us: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.67 sec: 1.02x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.02x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.00 ms: 1.02x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 18.7 ms: 1.02x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.34 us: 1.02x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 86.0 ms: 1.03x slower                                                          |
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 544 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 61.5 ms: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.71 us: 1.03x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 284 ms: 1.03x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 210 ms: 1.03x slower                                                           |
| async_tree_none            | 228 ms                                                              | 236 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 263 ms: 1.04x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 72.1 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.9 ms: 1.04x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.2 us: 1.05x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 468 ms: 1.05x slower                                                           |
| nbody                      | 76.9 ms                                                             | 80.5 ms: 1.05x slower                                                          |
| richards_super             | 35.5 ms                                                             | 37.3 ms: 1.05x slower                                                          |
| richards                   | 31.2 ms                                                             | 32.9 ms: 1.05x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 99.4 ms: 1.05x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 16.3 ms: 1.05x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 498 ms: 1.06x slower                                                           |
| regex_dna                  | 118 ms                                                              | 125 ms: 1.06x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 44.6 ms: 1.06x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.11 us: 1.06x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 59.3 ms: 1.06x slower                                                          |
| scimark_fft                | 198 ms                                                              | 212 ms: 1.07x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.46 ms: 1.07x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 651 ms: 1.07x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.34 sec: 1.08x slower                                                         |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.08x slower                                                          |
| float                      | 52.4 ms                                                             | 56.6 ms: 1.08x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 80.2 ms: 1.08x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.81 us: 1.08x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 48.0 ms: 1.09x slower                                                          |
| fannkuch                   | 270 ms                                                              | 294 ms: 1.09x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.30 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 149 us: 1.10x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.1 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 257 ms: 1.10x slower                                                           |
| json                       | 4.10 ms                                                             | 4.54 ms: 1.11x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 50.5 ms: 1.11x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.02 sec: 1.12x slower                                                         |
| django_template            | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.7 ms: 1.12x slower                                                          |
| deepcopy                   | 280 us                                                              | 314 us: 1.12x slower                                                           |
| sympy_expand               | 375 ms                                                              | 421 ms: 1.12x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 118 ms: 1.12x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.8 ms: 1.13x slower                                                          |
| mako                       | 6.94 ms                                                             | 7.84 ms: 1.13x slower                                                          |
| pylint                     | 217 ms                                                              | 245 ms: 1.13x slower                                                           |
| sympy_str                  | 211 ms                                                              | 239 ms: 1.13x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 233 ms: 1.13x slower                                                           |
| pycparser                  | 777 ms                                                              | 878 ms: 1.13x slower                                                           |
| raytrace                   | 189 ms                                                              | 214 ms: 1.13x slower                                                           |
| chaos                      | 48.0 ms                                                             | 54.3 ms: 1.13x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.26 ms: 1.14x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.7 ms: 1.14x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.1 ms: 1.15x slower                                                          |
| async_generators           | 266 ms                                                              | 306 ms: 1.15x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 78.4 ms: 1.15x slower                                                          |
| chameleon                  | 5.71 ms                                                             | 6.62 ms: 1.16x slower                                                          |
| go                         | 101 ms                                                              | 119 ms: 1.18x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 254 us: 1.19x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 97.7 ms: 1.21x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.5 us: 1.22x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.3 ms: 1.22x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 181 us: 1.23x slower                                                           |
| pyflate                    | 308 ms                                                              | 385 ms: 1.25x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 127 ms: 1.27x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 30.7 us: 1.31x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.96 ms: 1.32x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 80.1 ns: 1.38x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 83.0 ms: 1.40x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 6.23 ms: 1.47x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (7): python_startup, xml_etree_parse, pidigits, flaskblogging, create_gc_cycles, pickle, asyncio_tcp_ssl

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown