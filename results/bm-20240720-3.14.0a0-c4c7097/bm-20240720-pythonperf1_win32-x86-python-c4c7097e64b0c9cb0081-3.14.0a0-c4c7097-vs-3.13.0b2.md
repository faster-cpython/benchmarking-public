# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.9 ms: 1.06x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 103 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 502 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 224 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 541 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 52.4 ms                                                             | 60.5 ms: 1.16x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.4 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                               | 1.11x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 105 ms: 1.05x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.5 ms: 1.05x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.21 ms: 1.05x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 65.6 ms: 1.10x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 241 us: 1.13x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 168 us: 1.14x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 48.2 ms: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| django_template | 30.1 ms                                                             | 33.8 ms: 1.13x slower                                                          |
| mako            | 6.94 ms                                                             | 7.94 ms: 1.14x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 754 us: 12.91x faster                                                          |
| coverage                   | 307 ms                                                              | 54.3 ms: 5.66x faster                                                          |
| deepcopy                   | 280 us                                                              | 247 us: 1.13x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.4 us: 1.10x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 502 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 224 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.56 us: 1.01x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 748 us: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.15 ms: 1.02x slower                                                          |
| async_tree_io              | 530 ms                                                              | 541 ms: 1.02x slower                                                           |
| regex_dna                  | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.04x slower                                                           |
| sympy_expand               | 375 ms                                                              | 388 ms: 1.04x slower                                                           |
| sympy_str                  | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                          |
| pylint                     | 217 ms                                                              | 227 ms: 1.05x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.90 sec: 1.05x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 105 ms: 1.05x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.53 us: 1.05x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 110 ms: 1.05x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.5 ms: 1.05x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 88.2 ms: 1.05x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 77.9 ms: 1.05x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.86 us: 1.05x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.21 ms: 1.05x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.9 ms: 1.05x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.9 ms: 1.06x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 645 ms: 1.06x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| 2to3                       | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                         |
| python_startup             | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| async_generators           | 266 ms                                                              | 290 ms: 1.09x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 75.9 ms: 1.09x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 103 ms: 1.10x slower                                                           |
| pyflate                    | 308 ms                                                              | 338 ms: 1.10x slower                                                           |
| pycparser                  | 777 ms                                                              | 852 ms: 1.10x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 48.6 ms: 1.10x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 65.6 ms: 1.10x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.9 ms: 1.10x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 732 ms: 1.11x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.2 ms: 1.11x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.3 ms: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 229 ms: 1.11x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.20 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.3 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.8 ms: 1.13x slower                                                          |
| go                         | 101 ms                                                              | 113 ms: 1.13x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 241 us: 1.13x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 168 us: 1.14x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.5 us: 1.14x slower                                                          |
| mako                       | 6.94 ms                                                             | 7.94 ms: 1.14x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 48.2 ms: 1.15x slower                                                          |
| raytrace                   | 189 ms                                                              | 216 ms: 1.15x slower                                                           |
| scimark_fft                | 198 ms                                                              | 228 ms: 1.15x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 68.5 ms: 1.15x slower                                                          |
| float                      | 52.4 ms                                                             | 60.5 ms: 1.16x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.5 ms: 1.16x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 78.8 ms: 1.16x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.94 ms: 1.17x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 52.9 ms: 1.17x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.62 ms: 1.17x slower                                                          |
| richards                   | 31.2 ms                                                             | 36.9 ms: 1.18x slower                                                          |
| richards_super             | 35.5 ms                                                             | 42.0 ms: 1.18x slower                                                          |
| nbody                      | 76.9 ms                                                             | 91.4 ms: 1.19x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 97.2 ms: 1.20x slower                                                          |
| fannkuch                   | 270 ms                                                              | 328 ms: 1.21x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 71.0 ns: 1.23x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.1 ms: 1.23x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (5): pidigits, json_loads, gc_traversal, async_tree_memoization, bench_thread_pool
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown