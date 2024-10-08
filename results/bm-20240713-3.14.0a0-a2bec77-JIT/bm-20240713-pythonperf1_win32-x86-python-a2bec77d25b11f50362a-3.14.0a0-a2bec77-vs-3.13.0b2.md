# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.04x faster
- HPT reliability: 86.76%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 253 ms: 1.09x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.93 sec: 1.06x slower                                                         |
| html5lib       | 45.4 ms                                                             | 47.0 ms: 1.03x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 97.5 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 54.7 ms: 1.41x faster                                                          |
| float          | 52.4 ms                                                             | 43.9 ms: 1.19x faster                                                          |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.19x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 95.3 ms: 1.05x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_dna      | 118 ms                                                              | 123 ms: 1.05x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads         | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| xml_etree_iterparse | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| pickle_pure_python  | 213 us                                                              | 209 us: 1.02x faster                                                           |
| xml_etree_parse     | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| json_loads          | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| xml_etree_generate  | 59.6 ms                                                             | 61.4 ms: 1.03x slower                                                          |
| json_dumps          | 6.84 ms                                                             | 7.15 ms: 1.05x slower                                                          |
| xml_etree_process   | 42.1 ms                                                             | 46.5 ms: 1.11x slower                                                          |
| Geometric mean      | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.44 ms: 1.28x faster                                                          |
| django_template | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 23.5 ms: 1.17x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 53.6 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.05x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 760 us: 12.81x faster                                                          |
| coverage                   | 307 ms                                                              | 52.0 ms: 5.91x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 15.3 us: 1.54x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.2 ms: 1.44x faster                                                          |
| nbody                      | 76.9 ms                                                             | 54.7 ms: 1.41x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.44 ms: 1.28x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.38 ms: 1.21x faster                                                          |
| scimark_fft                | 198 ms                                                              | 166 ms: 1.19x faster                                                           |
| float                      | 52.4 ms                                                             | 43.9 ms: 1.19x faster                                                          |
| deepcopy                   | 280 us                                                              | 237 us: 1.18x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 48.0 ms: 1.16x faster                                                          |
| fannkuch                   | 270 ms                                                              | 236 ms: 1.14x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.31 ms: 1.14x faster                                                          |
| pyflate                    | 308 ms                                                              | 277 ms: 1.11x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.41 us: 1.07x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 565 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 42.3 ms: 1.07x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.07x faster                                                         |
| async_tree_io_tg           | 529 ms                                                              | 501 ms: 1.06x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 95.3 ms: 1.05x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.9 ms: 1.04x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.03x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.5 us: 1.03x faster                                                          |
| pathlib                    | 83.9 ms                                                             | 82.0 ms: 1.02x faster                                                          |
| pickle_pure_python         | 213 us                                                              | 209 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| sqlglot_parse              | 964 us                                                              | 956 us: 1.01x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 104 ms: 1.01x faster                                                           |
| logging_silent             | 57.9 ns                                                             | 58.4 ns: 1.01x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.21 us: 1.01x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.56 us: 1.01x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 75.1 ms: 1.01x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 458 ms: 1.02x slower                                                           |
| json                       | 4.10 ms                                                             | 4.20 ms: 1.03x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.22 ms: 1.03x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 61.4 ms: 1.03x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 97.5 ms: 1.03x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 47.0 ms: 1.03x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.1 ms: 1.04x slower                                                          |
| sympy_str                  | 211 ms                                                              | 220 ms: 1.04x slower                                                           |
| regex_dna                  | 118 ms                                                              | 123 ms: 1.05x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.15 ms: 1.05x slower                                                          |
| sympy_expand               | 375 ms                                                              | 393 ms: 1.05x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.68 sec: 1.05x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 111 ms: 1.06x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 73.7 ms: 1.06x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.93 sec: 1.06x slower                                                         |
| nqueens                    | 68.7 ms                                                             | 73.3 ms: 1.07x slower                                                          |
| richards                   | 31.2 ms                                                             | 33.7 ms: 1.08x slower                                                          |
| 2to3                       | 233 ms                                                              | 253 ms: 1.09x slower                                                           |
| pycparser                  | 777 ms                                                              | 845 ms: 1.09x slower                                                           |
| chaos                      | 48.0 ms                                                             | 52.3 ms: 1.09x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                                          |
| richards_super             | 35.5 ms                                                             | 39.1 ms: 1.10x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.3 ms: 1.11x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 46.5 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 241 ms: 1.11x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.70 ms: 1.11x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.4 ms: 1.12x slower                                                          |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 153 us: 1.13x slower                                                           |
| async_generators           | 266 ms                                                              | 307 ms: 1.16x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 18.0 ms: 1.16x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.5 ms: 1.17x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 241 ms: 1.17x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.69 ms: 1.21x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 53.6 ms: 1.21x slower                                                          |
| raytrace                   | 189 ms                                                              | 229 ms: 1.21x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 104 ms: 1.29x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.6 ms: 1.30x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 82.6 ms: 1.39x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (10): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, bench_thread_pool, unpickle_pure_python, create_gc_cycles, asyncio_tcp_ssl, gc_traversal, asyncio_tcp, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 86.76% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown