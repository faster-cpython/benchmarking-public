# Results vs. 3.13.0b2

- fork: mdboom
- ref: remove_redundant_typ
- machine: windows-x86
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 95.6 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 476 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 62.7 ms: 1.20x slower                                                          |
| nbody          | 76.9 ms                                                             | 93.0 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.40 us: 1.05x faster                                                          |
| pickle               | 8.07 us                                                             | 7.91 us: 1.02x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.8 us: 1.00x slower                                                          |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| unpickle_list        | 2.93 us                                                             | 3.01 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.6 ms: 1.05x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.07x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                         |
| json_dumps           | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 49.9 ms: 1.19x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 177 us: 1.20x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 260 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.7 ms: 1.08x slower                                                          |
| django_template | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 8.09 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 779 us: 12.49x faster                                                          |
| coverage                   | 307 ms                                                              | 52.7 ms: 5.82x faster                                                          |
| deepcopy                   | 280 us                                                              | 245 us: 1.14x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.40 us: 1.05x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 22.5 us: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 728 us: 1.04x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.91 us: 1.02x faster                                                          |
| async_tree_memoization     | 275 ms                                                              | 270 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 520 ms: 1.02x faster                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| regex_dna                  | 118 ms                                                              | 117 ms: 1.01x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.8 us: 1.00x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| sqlite_synth               | 1.96 us                                                             | 1.98 us: 1.01x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 95.6 ms: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 57.1 ms: 1.02x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| unpickle_list              | 2.93 us                                                             | 3.01 us: 1.03x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 71.4 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                              | 387 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 487 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.24 ms: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 219 ms: 1.04x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.03 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.6 ms: 1.05x slower                                                          |
| go                         | 101 ms                                                              | 106 ms: 1.05x slower                                                           |
| logging_simple             | 7.47 us                                                             | 7.91 us: 1.06x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.62 us: 1.06x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 144 us: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 476 ms: 1.06x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.07x slower                                                          |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 251 ms: 1.08x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.09 ms: 1.08x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 47.7 ms: 1.08x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.73 sec: 1.08x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| pylint                     | 217 ms                                                              | 235 ms: 1.08x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 74.6 ms: 1.09x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 80.6 ms: 1.09x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.2 ms: 1.10x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.37 sec: 1.10x slower                                                         |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 862 ms: 1.11x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 75.5 ms: 1.11x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 676 ms: 1.11x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.4 ms: 1.12x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                         |
| sqlglot_normalize          | 206 ms                                                              | 231 ms: 1.12x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.12x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.79 ms: 1.13x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.09 ms: 1.13x slower                                                          |
| chaos                      | 48.0 ms                                                             | 54.7 ms: 1.14x slower                                                          |
| async_generators           | 266 ms                                                              | 303 ms: 1.14x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.7 us: 1.16x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| pyflate                    | 308 ms                                                              | 358 ms: 1.16x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.09 ms: 1.16x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 69.6 ms: 1.17x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.3 ms: 1.18x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.9 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 236 ms: 1.19x slower                                                           |
| float                      | 52.4 ms                                                             | 62.7 ms: 1.20x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 177 us: 1.20x slower                                                           |
| fannkuch                   | 270 ms                                                              | 326 ms: 1.21x slower                                                           |
| nbody                      | 76.9 ms                                                             | 93.0 ms: 1.21x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.13 ms: 1.21x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 260 us: 1.22x slower                                                           |
| generators                 | 21.2 ms                                                             | 25.8 ms: 1.22x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.76 ms: 1.24x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 101 ms: 1.25x slower                                                           |
| raytrace                   | 189 ms                                                              | 237 ms: 1.26x slower                                                           |
| richards_super             | 35.5 ms                                                             | 44.8 ms: 1.26x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 73.5 ns: 1.27x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.7 ms: 1.28x slower                                                          |
| richards                   | 31.2 ms                                                             | 40.5 ms: 1.30x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (8): asyncio_tcp, async_tree_memoization_tg, async_tree_none_tg, pathlib, html5lib, regex_effbot, deepcopy_reduce, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-pythonperf1_win32-x86-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown