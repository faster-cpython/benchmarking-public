# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 202 ms: 1.02x slower                                                           |
| float          | 52.4 ms                                                             | 62.0 ms: 1.18x slower                                                          |
| nbody          | 76.9 ms                                                             | 95.8 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_dna      | 118 ms                                                              | 122 ms: 1.03x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.9 ms: 1.06x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.86 sec: 1.13x slower                                                         |
| json_dumps           | 6.84 ms                                                             | 7.74 ms: 1.13x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 68.4 ms: 1.15x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 254 us: 1.19x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 51.0 ms: 1.21x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 179 us: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.8 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.8 ms: 1.08x slower                                                          |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| mako            | 6.94 ms                                                             | 8.41 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 727 us: 13.38x faster                                                          |
| coverage                   | 307 ms                                                              | 54.0 ms: 5.69x faster                                                          |
| deepcopy                   | 280 us                                                              | 246 us: 1.14x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.0 us: 1.07x faster                                                          |
| async_tree_none            | 228 ms                                                              | 215 ms: 1.06x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.51 us: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| sympy_expand               | 375 ms                                                              | 381 ms: 1.02x slower                                                           |
| pidigits                   | 199 ms                                                              | 202 ms: 1.02x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| go                         | 101 ms                                                              | 103 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 216 ms: 1.02x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.02x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_dna                  | 118 ms                                                              | 122 ms: 1.03x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 86.9 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 465 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.27 ms: 1.04x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 58.2 ms: 1.04x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.3 ms: 1.05x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 72.8 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.9 ms: 1.06x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 46.8 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| logging_simple             | 7.47 us                                                             | 8.02 us: 1.07x slower                                                          |
| pylint                     | 217 ms                                                              | 233 ms: 1.07x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                         |
| 2to3                       | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| pprint_safe_repr           | 607 ms                                                              | 654 ms: 1.08x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 79.9 ms: 1.08x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.78 us: 1.08x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.8 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 223 ms: 1.08x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                           |
| django_template            | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.5 ms: 1.09x slower                                                          |
| pycparser                  | 777 ms                                                              | 857 ms: 1.10x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 75.9 ms: 1.11x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.19 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.6 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.5 ms: 1.12x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.86 sec: 1.13x slower                                                         |
| coroutines                 | 15.5 ms                                                             | 17.5 ms: 1.13x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.74 ms: 1.13x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 751 ms: 1.13x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.5 us: 1.14x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 68.4 ms: 1.15x slower                                                          |
| async_generators           | 266 ms                                                              | 307 ms: 1.16x slower                                                           |
| pyflate                    | 308 ms                                                              | 358 ms: 1.16x slower                                                           |
| telco                      | 6.03 ms                                                             | 7.08 ms: 1.17x slower                                                          |
| float                      | 52.4 ms                                                             | 62.0 ms: 1.18x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 70.6 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 237 ms: 1.19x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 254 us: 1.19x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.41 ms: 1.21x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 51.0 ms: 1.21x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 179 us: 1.21x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.72 ms: 1.22x slower                                                          |
| fannkuch                   | 270 ms                                                              | 332 ms: 1.23x slower                                                           |
| nbody                      | 76.9 ms                                                             | 95.8 ms: 1.25x slower                                                          |
| richards                   | 31.2 ms                                                             | 39.0 ms: 1.25x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.29 ms: 1.25x slower                                                          |
| raytrace                   | 189 ms                                                              | 236 ms: 1.25x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.6 ms: 1.25x slower                                                          |
| richards_super             | 35.5 ms                                                             | 44.8 ms: 1.26x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 102 ms: 1.26x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 74.5 ns: 1.29x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.9 ms: 1.32x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none_tg, create_gc_cycles, async_tree_memoization_tg, async_tree_memoization, gc_traversal, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown