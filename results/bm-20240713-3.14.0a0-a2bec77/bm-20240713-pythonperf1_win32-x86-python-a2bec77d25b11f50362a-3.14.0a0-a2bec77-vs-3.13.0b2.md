# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 95.0 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 506 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 225 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 477 ms: 1.01x slower                                                           |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 466 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 58.9 ms: 1.12x slower                                                          |
| nbody          | 76.9 ms                                                             | 89.0 ms: 1.16x slower                                                          |
| Geometric mean | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 103 ms: 1.04x slower                                                           |
| regex_dna      | 118 ms                                                              | 124 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.0 ms: 1.03x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.14 ms: 1.04x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                         |
| unpickle_pure_python | 147 us                                                              | 167 us: 1.13x slower                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 68.3 ms: 1.15x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 250 us: 1.18x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 49.7 ms: 1.18x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.3 ms: 1.05x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                                          |
| django_template | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 7.95 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 778 us: 12.50x faster                                                          |
| coverage                   | 307 ms                                                              | 52.6 ms: 5.84x faster                                                          |
| deepcopy                   | 280 us                                                              | 241 us: 1.16x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.4 us: 1.10x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.47 us: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 506 ms: 1.05x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 246 ms: 1.03x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 82.2 ms: 1.02x faster                                                          |
| async_tree_none            | 228 ms                                                              | 225 ms: 1.01x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 748 us: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| tornado_http               | 94.3 ms                                                             | 95.0 ms: 1.01x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 477 ms: 1.01x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.01x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 70.5 ms: 1.02x slower                                                          |
| sympy_expand               | 375 ms                                                              | 381 ms: 1.02x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.0 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| async_tree_io              | 530 ms                                                              | 546 ms: 1.03x slower                                                           |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 57.7 ms: 1.03x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 103 ms: 1.04x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.43 us: 1.04x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.74 us: 1.04x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 18.9 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 466 ms: 1.04x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.14 ms: 1.04x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.30 sec: 1.04x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.3 ms: 1.04x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 634 ms: 1.05x slower                                                           |
| regex_dna                  | 118 ms                                                              | 124 ms: 1.05x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 46.3 ms: 1.05x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| telco                      | 6.03 ms                                                             | 6.35 ms: 1.05x slower                                                          |
| pycparser                  | 777 ms                                                              | 824 ms: 1.06x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 73.1 ms: 1.06x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 79.1 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| async_generators           | 266 ms                                                              | 285 ms: 1.07x slower                                                           |
| json                       | 4.10 ms                                                             | 4.41 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.09 ms: 1.08x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.28 ms: 1.08x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.1 ms: 1.08x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.79 sec: 1.09x slower                                                         |
| pyflate                    | 308 ms                                                              | 335 ms: 1.09x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 226 ms: 1.10x slower                                                           |
| django_template            | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.3 ms: 1.11x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.2 ms: 1.11x slower                                                          |
| scimark_fft                | 198 ms                                                              | 220 ms: 1.11x slower                                                           |
| chaos                      | 48.0 ms                                                             | 53.8 ms: 1.12x slower                                                          |
| float                      | 52.4 ms                                                             | 58.9 ms: 1.12x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.3 us: 1.12x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                           |
| go                         | 101 ms                                                              | 114 ms: 1.13x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 67.2 ms: 1.13x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 167 us: 1.13x slower                                                           |
| raytrace                   | 189 ms                                                              | 215 ms: 1.14x slower                                                           |
| mako                       | 6.94 ms                                                             | 7.95 ms: 1.15x slower                                                          |
| fannkuch                   | 270 ms                                                              | 309 ms: 1.15x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 68.3 ms: 1.15x slower                                                          |
| richards_super             | 35.5 ms                                                             | 40.7 ms: 1.15x slower                                                          |
| nbody                      | 76.9 ms                                                             | 89.0 ms: 1.16x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 52.4 ms: 1.16x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.61 ms: 1.17x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 95.0 ms: 1.17x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 250 us: 1.18x slower                                                           |
| richards                   | 31.2 ms                                                             | 36.8 ms: 1.18x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.7 ms: 1.18x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.01 ms: 1.18x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.6 ms: 1.26x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 74.9 ns: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_memoization, asyncio_tcp_ssl, gc_traversal, bench_thread_pool, pylint
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown