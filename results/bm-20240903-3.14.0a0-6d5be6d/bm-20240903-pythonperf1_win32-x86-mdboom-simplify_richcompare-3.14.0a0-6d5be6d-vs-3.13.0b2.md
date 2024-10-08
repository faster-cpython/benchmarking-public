# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.1 ms: 1.01x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.05x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 216 ms: 1.06x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 247 ms: 1.03x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 198 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 272 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 202 ms: 1.02x slower                                                           |
| float          | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                          |
| nbody          | 76.9 ms                                                             | 96.0 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.46 ms: 1.09x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.86 sec: 1.13x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 251 us: 1.18x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 50.0 ms: 1.19x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 179 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.1 ms: 1.04x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                                          |
| django_template | 30.1 ms                                                             | 32.9 ms: 1.09x slower                                                          |
| mako            | 6.94 ms                                                             | 8.20 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 741 us: 13.14x faster                                                          |
| coverage                   | 307 ms                                                              | 51.8 ms: 5.93x faster                                                          |
| deepcopy                   | 280 us                                                              | 238 us: 1.17x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.0 us: 1.07x faster                                                          |
| async_tree_none            | 228 ms                                                              | 216 ms: 1.06x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.46 us: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 509 ms: 1.04x faster                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 247 ms: 1.03x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 198 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 465 ms: 1.01x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 272 ms: 1.01x faster                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| html5lib                   | 45.4 ms                                                             | 46.1 ms: 1.01x slower                                                          |
| pidigits                   | 199 ms                                                              | 202 ms: 1.02x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| regex_dna                  | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                         |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| sympy_expand               | 375 ms                                                              | 384 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 216 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.1 us: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.03x slower                                                          |
| go                         | 101 ms                                                              | 104 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 86.9 ms: 1.04x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 46.1 ms: 1.04x slower                                                          |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 73.2 ms: 1.06x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| pprint_safe_repr           | 607 ms                                                              | 643 ms: 1.06x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.92 us: 1.06x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.65 us: 1.06x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 59.5 ms: 1.07x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.32 sec: 1.07x slower                                                         |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 42.9 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 716 ms: 1.08x slower                                                           |
| pylint                     | 217 ms                                                              | 235 ms: 1.08x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 223 ms: 1.08x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.9 ms: 1.09x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.46 ms: 1.09x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.9 ms: 1.09x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.15 ms: 1.10x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 149 us: 1.10x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.11x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 82.0 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| async_generators           | 266 ms                                                              | 297 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.77 ms: 1.12x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.86 sec: 1.13x slower                                                         |
| chaos                      | 48.0 ms                                                             | 54.1 ms: 1.13x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 67.3 ms: 1.13x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 76.9 ms: 1.13x slower                                                          |
| pycparser                  | 777 ms                                                              | 888 ms: 1.14x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.6 us: 1.15x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.8 ms: 1.15x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.3 ms: 1.16x slower                                                          |
| pyflate                    | 308 ms                                                              | 358 ms: 1.16x slower                                                           |
| float                      | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 251 us: 1.18x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 70.0 ms: 1.18x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.20 ms: 1.18x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 50.0 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 237 ms: 1.20x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 179 us: 1.22x slower                                                           |
| raytrace                   | 189 ms                                                              | 231 ms: 1.22x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.75 ms: 1.23x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.4 ms: 1.25x slower                                                          |
| nbody                      | 76.9 ms                                                             | 96.0 ms: 1.25x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 102 ms: 1.26x slower                                                           |
| fannkuch                   | 270 ms                                                              | 342 ms: 1.26x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 5.36 ms: 1.27x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 74.8 ns: 1.29x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.6 ms: 1.31x slower                                                          |
| richards_super             | 35.5 ms                                                             | 46.9 ms: 1.32x slower                                                          |
| richards                   | 31.2 ms                                                             | 41.9 ms: 1.34x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): create_gc_cycles, async_tree_io, gc_traversal
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: unknown