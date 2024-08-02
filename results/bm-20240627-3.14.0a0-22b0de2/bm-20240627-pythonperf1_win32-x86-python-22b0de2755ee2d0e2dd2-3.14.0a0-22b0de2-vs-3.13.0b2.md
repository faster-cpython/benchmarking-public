# Results vs. 3.13.0b2

- fork: python
- ref: 22b0de2755ee2d0e2dd2
- machine: windows-x86
- commit hash: 22b0de2
- commit date: 2024-06-27
- overall geometric mean: 1.08x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.96 sec: 1.08x slower                                                         |
| html5lib       | 45.4 ms                                                             | 49.9 ms: 1.10x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 97.6 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 262 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 491 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.06x slower                                                           |
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                           |
| async_tree_io              | 530 ms                                                              | 579 ms: 1.09x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| float          | 52.4 ms                                                             | 64.8 ms: 1.24x slower                                                          |
| nbody          | 76.9 ms                                                             | 103 ms: 1.34x slower                                                           |
| Geometric mean | (ref)                                                               | 1.18x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 115 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 69.7 ms: 1.09x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.82 ms: 1.14x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 70.2 ms: 1.18x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 2.01 sec: 1.22x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 51.6 ms: 1.23x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 189 us: 1.29x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 278 us: 1.30x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.16x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 34.4 ms: 1.14x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 54.6 ms: 1.23x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.9 ms: 1.24x slower                                                          |
| mako            | 6.94 ms                                                             | 8.76 ms: 1.26x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.22x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240627-pythonperf1_win32-x86-python-22b0de2755ee2d0e2dd2-3.14.0a0-22b0de2 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 810 us: 12.01x faster                                                          |
| coverage                   | 307 ms                                                              | 52.1 ms: 5.90x faster                                                          |
| deepcopy                   | 280 us                                                              | 271 us: 1.03x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 739 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 71.0 ms: 1.02x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| async_tree_none_tg         | 203 ms                                                              | 208 ms: 1.03x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 262 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 97.6 ms: 1.03x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 491 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.06x slower                                                           |
| async_tree_none            | 228 ms                                                              | 241 ms: 1.06x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 25.1 us: 1.07x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.76 us: 1.07x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 295 ms: 1.07x slower                                                           |
| json                       | 4.10 ms                                                             | 4.40 ms: 1.07x slower                                                          |
| pylint                     | 217 ms                                                              | 234 ms: 1.08x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.96 sec: 1.08x slower                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 69.7 ms: 1.09x slower                                                          |
| async_tree_io              | 530 ms                                                              | 579 ms: 1.09x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.75 sec: 1.09x slower                                                         |
| html5lib                   | 45.4 ms                                                             | 49.9 ms: 1.10x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 116 ms: 1.10x slower                                                           |
| sympy_expand               | 375 ms                                                              | 413 ms: 1.10x slower                                                           |
| sympy_str                  | 211 ms                                                              | 233 ms: 1.10x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 16.2 ms: 1.11x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 82.4 ms: 1.11x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.79 ms: 1.13x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 77.5 ms: 1.13x slower                                                          |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 63.7 ms: 1.14x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.42 sec: 1.14x slower                                                         |
| django_template            | 30.1 ms                                                             | 34.4 ms: 1.14x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 694 ms: 1.14x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.82 ms: 1.14x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 155 us: 1.15x slower                                                           |
| pycparser                  | 777 ms                                                              | 892 ms: 1.15x slower                                                           |
| logging_format             | 8.13 us                                                             | 9.33 us: 1.15x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 115 ms: 1.15x slower                                                           |
| logging_simple             | 7.47 us                                                             | 8.62 us: 1.15x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.1 ms: 1.17x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 79.6 ms: 1.17x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 70.2 ms: 1.18x slower                                                          |
| async_generators           | 266 ms                                                              | 314 ms: 1.18x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 47.3 ms: 1.19x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 246 ms: 1.19x slower                                                           |
| tomli_loads                | 1.65 sec                                                            | 2.01 sec: 1.22x slower                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.45 ms: 1.22x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 51.6 ms: 1.23x slower                                                          |
| pyflate                    | 308 ms                                                              | 378 ms: 1.23x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 54.6 ms: 1.23x slower                                                          |
| float                      | 52.4 ms                                                             | 64.8 ms: 1.24x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 24.9 ms: 1.24x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.8 us: 1.25x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.21 ms: 1.25x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.61 ms: 1.26x slower                                                          |
| go                         | 101 ms                                                              | 127 ms: 1.26x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.76 ms: 1.26x slower                                                          |
| chaos                      | 48.0 ms                                                             | 60.7 ms: 1.27x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 75.5 ms: 1.27x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.43 ms: 1.28x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 189 us: 1.29x slower                                                           |
| fannkuch                   | 270 ms                                                              | 347 ms: 1.29x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.88 ms: 1.29x slower                                                          |
| richards_super             | 35.5 ms                                                             | 45.8 ms: 1.29x slower                                                          |
| scimark_fft                | 198 ms                                                              | 257 ms: 1.30x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 278 us: 1.30x slower                                                           |
| raytrace                   | 189 ms                                                              | 247 ms: 1.31x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 106 ms: 1.31x slower                                                           |
| richards                   | 31.2 ms                                                             | 41.2 ms: 1.32x slower                                                          |
| nbody                      | 76.9 ms                                                             | 103 ms: 1.34x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 77.7 ns: 1.34x slower                                                          |
| generators                 | 21.2 ms                                                             | 28.5 ms: 1.35x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 60.9 ms: 1.35x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.08x slower                                                                   |

Benchmark hidden because not significant (5): asyncio_tcp_ssl, pathlib, bench_thread_pool, async_tree_io_tg, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.10x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown