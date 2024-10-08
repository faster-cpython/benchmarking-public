# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 45.8 ms: 1.01x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 213 ms: 1.07x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                           |
| float          | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| nbody          | 76.9 ms                                                             | 94.3 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 118 ms: 1.00x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.8 ms: 1.07x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.39 ms: 1.08x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 67.5 ms: 1.13x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 49.9 ms: 1.19x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 263 us: 1.23x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 183 us: 1.24x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.1 ms: 1.04x slower                                                          |
| django_template | 30.1 ms                                                             | 31.9 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.0 ms: 1.10x slower                                                          |
| mako            | 6.94 ms                                                             | 8.24 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 719 us: 13.53x faster                                                          |
| coverage                   | 307 ms                                                              | 53.6 ms: 5.73x faster                                                          |
| deepcopy                   | 280 us                                                              | 242 us: 1.16x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.42 us: 1.07x faster                                                          |
| async_tree_none            | 228 ms                                                              | 213 ms: 1.07x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.2 us: 1.06x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 744 us: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 118 ms: 1.00x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 45.8 ms: 1.01x slower                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.45 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 56.7 ms: 1.02x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| sympy_str                  | 211 ms                                                              | 215 ms: 1.02x slower                                                           |
| sympy_expand               | 375 ms                                                              | 383 ms: 1.02x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 460 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| go                         | 101 ms                                                              | 104 ms: 1.04x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.03 ms: 1.04x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 46.1 ms: 1.04x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.04x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.4 ms: 1.04x slower                                                          |
| json                       | 4.10 ms                                                             | 4.30 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 143 us: 1.05x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 73.2 ms: 1.05x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 642 ms: 1.06x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.61 us: 1.06x slower                                                          |
| django_template            | 30.1 ms                                                             | 31.9 ms: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.94 us: 1.06x slower                                                          |
| 2to3                       | 233 ms                                                              | 248 ms: 1.07x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.33 sec: 1.07x slower                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.8 ms: 1.07x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.08x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.72 sec: 1.08x slower                                                         |
| pylint                     | 217 ms                                                              | 234 ms: 1.08x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.39 ms: 1.08x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 722 ms: 1.09x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.14 ms: 1.09x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 225 ms: 1.09x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.0 ms: 1.10x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 75.3 ms: 1.10x slower                                                          |
| async_generators           | 266 ms                                                              | 292 ms: 1.10x slower                                                           |
| chaos                      | 48.0 ms                                                             | 52.8 ms: 1.10x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.1 ms: 1.10x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.8 ms: 1.10x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.10x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.69 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 862 ms: 1.11x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.84 sec: 1.12x slower                                                         |
| meteor_contest             | 74.1 ms                                                             | 82.8 ms: 1.12x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.4 ms: 1.12x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 67.5 ms: 1.13x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 77.6 ms: 1.14x slower                                                          |
| pyflate                    | 308 ms                                                              | 354 ms: 1.15x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.7 us: 1.15x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 68.7 ms: 1.16x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.9 ms: 1.19x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.24 ms: 1.19x slower                                                          |
| float                      | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 237 ms: 1.20x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.71 ms: 1.21x slower                                                          |
| raytrace                   | 189 ms                                                              | 229 ms: 1.21x slower                                                           |
| nbody                      | 76.9 ms                                                             | 94.3 ms: 1.23x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.20 ms: 1.23x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 263 us: 1.23x slower                                                           |
| richards_super             | 35.5 ms                                                             | 43.9 ms: 1.24x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 183 us: 1.24x slower                                                           |
| fannkuch                   | 270 ms                                                              | 336 ms: 1.25x slower                                                           |
| richards                   | 31.2 ms                                                             | 39.4 ms: 1.26x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 73.1 ns: 1.26x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.8 ms: 1.27x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.4 ms: 1.27x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 103 ms: 1.27x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_memoization_tg, async_tree_none_tg, async_tree_memoization, async_tree_io
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown