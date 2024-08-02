# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.04x faster
- HPT reliability: 89.69%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 256 ms: 1.10x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.93 sec: 1.07x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.8 ms: 1.05x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 503 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 269 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 540 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 56.7 ms: 1.36x faster                                                          |
| float          | 52.4 ms                                                             | 43.5 ms: 1.20x faster                                                          |
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                               | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 94.3 ms: 1.06x faster                                                          |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.8 ms: 1.02x faster                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 58.6 ms: 1.02x faster                                                          |
| pickle_pure_python   | 213 us                                                              | 214 us: 1.00x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 151 us: 1.02x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.05 ms: 1.03x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 44.5 ms: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| django_template | 30.1 ms                                                             | 33.2 ms: 1.11x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 52.7 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.04x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 751 us: 12.96x faster                                                          |
| coverage                   | 307 ms                                                              | 52.9 ms: 5.81x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 16.1 us: 1.46x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.9 ms: 1.42x faster                                                          |
| nbody                      | 76.9 ms                                                             | 56.7 ms: 1.36x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.43 ms: 1.28x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 46.3 ms: 1.21x faster                                                          |
| float                      | 52.4 ms                                                             | 43.5 ms: 1.20x faster                                                          |
| deepcopy                   | 280 us                                                              | 235 us: 1.19x faster                                                           |
| scimark_fft                | 198 ms                                                              | 168 ms: 1.18x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.44 ms: 1.18x faster                                                          |
| fannkuch                   | 270 ms                                                              | 233 ms: 1.16x faster                                                           |
| pyflate                    | 308 ms                                                              | 267 ms: 1.15x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.53 ms: 1.09x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.51 sec: 1.09x faster                                                         |
| pprint_safe_repr           | 607 ms                                                              | 570 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.17 sec: 1.06x faster                                                         |
| regex_compile              | 99.9 ms                                                             | 94.3 ms: 1.06x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.46 us: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 503 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 193 ms: 1.05x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 43.1 ms: 1.05x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 70.7 ms: 1.05x faster                                                          |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 269 ms: 1.02x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.8 ms: 1.02x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 58.6 ms: 1.02x faster                                                          |
| comprehensions             | 11.9 us                                                             | 11.7 us: 1.02x faster                                                          |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| pickle_pure_python         | 213 us                                                              | 214 us: 1.00x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 766 us: 1.01x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 58.7 ns: 1.01x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 215 ms: 1.02x slower                                                           |
| async_tree_io              | 530 ms                                                              | 540 ms: 1.02x slower                                                           |
| sympy_expand               | 375 ms                                                              | 383 ms: 1.02x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 151 us: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.22 ms: 1.03x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.36 us: 1.03x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.05 ms: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.74 us: 1.04x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| pathlib                    | 83.9 ms                                                             | 87.9 ms: 1.05x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.8 ms: 1.05x slower                                                          |
| json                       | 4.10 ms                                                             | 4.33 ms: 1.06x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 44.5 ms: 1.06x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.93 sec: 1.07x slower                                                         |
| nqueens                    | 68.7 ms                                                             | 73.5 ms: 1.07x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.07x slower                                                           |
| pycparser                  | 777 ms                                                              | 835 ms: 1.07x slower                                                           |
| richards                   | 31.2 ms                                                             | 33.6 ms: 1.08x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.9 ms: 1.09x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 75.4 ms: 1.09x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.3 ms: 1.09x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.62 ms: 1.09x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| richards_super             | 35.5 ms                                                             | 38.7 ms: 1.09x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.6 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 256 ms: 1.10x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.2 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 242 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 231 ms: 1.12x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| go                         | 101 ms                                                              | 114 ms: 1.13x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.9 ms: 1.14x slower                                                          |
| async_generators           | 266 ms                                                              | 314 ms: 1.18x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 18.4 ms: 1.19x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 52.7 ms: 1.19x slower                                                          |
| raytrace                   | 189 ms                                                              | 229 ms: 1.22x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.74 ms: 1.22x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 102 ms: 1.26x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.5 ms: 1.30x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 77.6 ms: 1.31x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (8): async_tree_memoization_tg, async_tree_cpu_io_mixed, sqlglot_parse, gc_traversal, asyncio_tcp_ssl, xml_etree_parse, bench_thread_pool, asyncio_tcp
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 89.69% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown