# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: justin_likely
- machine: windows-x86
- commit hash: bad9944
- commit date: 2024-10-18
- overall geometric mean: 1.00x slower
- HPT reliability: 99.39%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 266 ms: 1.14x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.0 ms: 1.01x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 109 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| async_tree_io              | 530 ms                                                              | 510 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 547 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 59.6 ms: 1.29x faster                                                          |
| float          | 52.4 ms                                                             | 45.7 ms: 1.15x faster                                                          |
| Geometric mean | (ref)                                                               | 1.14x faster                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.76 ms: 1.07x faster                                                          |
| regex_dna      | 118 ms                                                              | 118 ms: 1.00x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 56.1 ms: 1.06x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.81 us: 1.04x faster                                                          |
| pickle_list          | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 21.2 us: 1.02x slower                                                          |
| pickle               | 8.07 us                                                             | 8.39 us: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 110 ms: 1.06x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 164 us: 1.12x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 251 us: 1.18x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 8.74 ms: 1.28x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): json_loads, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| python_startup         | 22.2 ms                                                             | 26.9 ms: 1.21x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.16x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.78 ms: 1.20x faster                                                          |
| django_template | 30.1 ms                                                             | 33.1 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.7 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 790 us: 12.31x faster                                                          |
| coverage                   | 307 ms                                                              | 52.7 ms: 5.83x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.7 us: 1.41x faster                                                          |
| nbody                      | 76.9 ms                                                             | 59.6 ms: 1.29x faster                                                          |
| deepcopy                   | 280 us                                                              | 231 us: 1.21x faster                                                           |
| mako                       | 6.94 ms                                                             | 5.78 ms: 1.20x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 57.8 ms: 1.18x faster                                                          |
| scimark_sor                | 81.0 ms                                                             | 69.2 ms: 1.17x faster                                                          |
| float                      | 52.4 ms                                                             | 45.7 ms: 1.15x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.6 ms: 1.14x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.55 ms: 1.13x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 50.3 ms: 1.11x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.38 us: 1.09x faster                                                          |
| scimark_fft                | 198 ms                                                              | 184 ms: 1.08x faster                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.76 ms: 1.07x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 56.1 ms: 1.06x faster                                                          |
| fannkuch                   | 270 ms                                                              | 254 ms: 1.06x faster                                                           |
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 577 ms: 1.05x faster                                                           |
| go                         | 101 ms                                                              | 96.0 ms: 1.05x faster                                                          |
| unpickle_list              | 2.93 us                                                             | 2.81 us: 1.04x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 55.7 ns: 1.04x faster                                                          |
| async_tree_io              | 530 ms                                                              | 510 ms: 1.04x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.20 sec: 1.03x faster                                                         |
| meteor_contest             | 74.1 ms                                                             | 72.1 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| regex_dna                  | 118 ms                                                              | 118 ms: 1.00x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 59.9 ms: 1.01x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.10 ms: 1.01x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.24 us: 1.01x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.0 ms: 1.01x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.62 us: 1.02x slower                                                          |
| pickle_dict                | 20.8 us                                                             | 21.2 us: 1.02x slower                                                          |
| pyflate                    | 308 ms                                                              | 317 ms: 1.03x slower                                                           |
| async_tree_io_tg           | 529 ms                                                              | 547 ms: 1.03x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.5 sec: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                           |
| pickle                     | 8.07 us                                                             | 8.39 us: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                              | 392 ms: 1.04x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 142 us: 1.05x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 110 ms: 1.06x slower                                                           |
| pycparser                  | 777 ms                                                              | 824 ms: 1.06x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 89.1 ms: 1.06x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.07x slower                                                           |
| sympy_str                  | 211 ms                                                              | 226 ms: 1.07x slower                                                           |
| sqlglot_parse              | 964 us                                                              | 1.04 ms: 1.07x slower                                                          |
| comprehensions             | 11.9 us                                                             | 12.8 us: 1.08x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.75 sec: 1.09x slower                                                         |
| django_template            | 30.1 ms                                                             | 33.1 ms: 1.10x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 76.0 ms: 1.11x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 117 ms: 1.11x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 164 us: 1.12x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.13x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                         |
| genshi_text                | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| 2to3                       | 233 ms                                                              | 266 ms: 1.14x slower                                                           |
| generators                 | 21.2 ms                                                             | 24.3 ms: 1.15x slower                                                          |
| chaos                      | 48.0 ms                                                             | 55.3 ms: 1.15x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.58 ms: 1.16x slower                                                          |
| json                       | 4.10 ms                                                             | 4.74 ms: 1.16x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 109 ms: 1.16x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 251 us: 1.18x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 244 ms: 1.18x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 17.4 ms: 1.19x slower                                                          |
| python_startup             | 22.2 ms                                                             | 26.9 ms: 1.21x slower                                                          |
| async_generators           | 266 ms                                                              | 322 ms: 1.21x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 53.7 ms: 1.21x slower                                                          |
| richards                   | 31.2 ms                                                             | 38.8 ms: 1.24x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 50.3 ms: 1.27x slower                                                          |
| richards_super             | 35.5 ms                                                             | 45.2 ms: 1.27x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.83 ms: 1.28x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 8.74 ms: 1.28x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.42 ms: 1.28x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 866 ms: 1.31x slower                                                           |
| pylint                     | 217 ms                                                              | 284 ms: 1.31x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 94.1 ms: 1.36x slower                                                          |
| raytrace                   | 189 ms                                                              | 272 ms: 1.44x slower                                                           |
| create_gc_cycles           | 756 us                                                              | 1.20 ms: 1.58x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, regex_v8, json_loads, xml_etree_iterparse, sqlite_synth, pidigits, xml_etree_process, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (3) of results/bm-20241018-3.14.0a1+-bad9944-JIT/bm-20241018-pythonperf1_win32-x86-brandtbucher-justin_likely-3.14.0a1+-bad9944.json: dulwich_log, sphinx, unpack_sequence

# HPT report

- Reliability score: 99.39% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown