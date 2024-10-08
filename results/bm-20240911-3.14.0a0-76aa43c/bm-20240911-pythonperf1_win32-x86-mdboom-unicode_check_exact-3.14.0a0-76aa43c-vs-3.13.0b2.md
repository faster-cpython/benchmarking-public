# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicode_check_exact
- machine: windows-x86
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 250 ms: 1.07x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                        |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 95.8 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 516 ms: 1.03x faster                                                          |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                  |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 201 ms: 1.01x slower                                                          |
| float          | 52.4 ms                                                             | 61.4 ms: 1.17x slower                                                         |
| nbody          | 76.9 ms                                                             | 91.6 ms: 1.19x slower                                                         |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 116 ms: 1.01x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                         |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.50 us: 1.02x faster                                                         |
| pickle_dict          | 20.8 us                                                             | 20.5 us: 1.01x faster                                                         |
| pickle               | 8.07 us                                                             | 7.96 us: 1.01x faster                                                         |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                         |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.03x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.08 us: 1.05x slower                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                         |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                         |
| json_dumps           | 6.84 ms                                                             | 7.41 ms: 1.08x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 66.8 ms: 1.12x slower                                                         |
| tomli_loads          | 1.65 sec                                                            | 1.90 sec: 1.15x slower                                                        |
| xml_etree_process    | 42.1 ms                                                             | 48.6 ms: 1.15x slower                                                         |
| pickle_pure_python   | 213 us                                                              | 256 us: 1.20x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 178 us: 1.21x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.5 ms: 1.06x slower                                                         |
| python_startup_no_site | 18.2 ms                                                             | 19.4 ms: 1.06x slower                                                         |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.9 ms: 1.06x slower                                                         |
| django_template | 30.1 ms                                                             | 32.5 ms: 1.08x slower                                                         |
| genshi_text     | 20.1 ms                                                             | 21.8 ms: 1.09x slower                                                         |
| mako            | 6.94 ms                                                             | 7.98 ms: 1.15x slower                                                         |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 753 us: 12.91x faster                                                         |
| coverage                   | 307 ms                                                              | 51.9 ms: 5.92x faster                                                         |
| deepcopy                   | 280 us                                                              | 244 us: 1.15x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 22.2 us: 1.06x faster                                                         |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 734 us: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 516 ms: 1.03x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.50 us: 1.02x faster                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.54 us: 1.02x faster                                                         |
| pathlib                    | 83.9 ms                                                             | 82.5 ms: 1.02x faster                                                         |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                         |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.5 us: 1.01x faster                                                         |
| regex_dna                  | 118 ms                                                              | 116 ms: 1.01x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.96 us: 1.01x faster                                                         |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                         |
| sympy_expand               | 375 ms                                                              | 377 ms: 1.00x slower                                                          |
| sympy_str                  | 211 ms                                                              | 213 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                        |
| bench_mp_pool              | 69.4 ms                                                             | 70.1 ms: 1.01x slower                                                         |
| pidigits                   | 199 ms                                                              | 201 ms: 1.01x slower                                                          |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.01x slower                                                          |
| json                       | 4.10 ms                                                             | 4.16 ms: 1.02x slower                                                         |
| tornado_http               | 94.3 ms                                                             | 95.8 ms: 1.02x slower                                                         |
| crypto_pyaes               | 55.8 ms                                                             | 57.0 ms: 1.02x slower                                                         |
| go                         | 101 ms                                                              | 103 ms: 1.02x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                         |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.03x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.1 ms: 1.03x slower                                                         |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 142 us: 1.05x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.34 ms: 1.05x slower                                                         |
| unpickle_list              | 2.93 us                                                             | 3.08 us: 1.05x slower                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.8 ms: 1.06x slower                                                         |
| python_startup             | 22.2 ms                                                             | 23.5 ms: 1.06x slower                                                         |
| genshi_xml                 | 44.3 ms                                                             | 46.9 ms: 1.06x slower                                                         |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 19.4 ms: 1.06x slower                                                         |
| logging_format             | 8.13 us                                                             | 8.66 us: 1.06x slower                                                         |
| logging_simple             | 7.47 us                                                             | 7.99 us: 1.07x slower                                                         |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 42.5 ms: 1.07x slower                                                         |
| sqlglot_normalize          | 206 ms                                                              | 221 ms: 1.07x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 250 ms: 1.07x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 73.8 ms: 1.08x slower                                                         |
| meteor_contest             | 74.1 ms                                                             | 79.8 ms: 1.08x slower                                                         |
| django_template            | 30.1 ms                                                             | 32.5 ms: 1.08x slower                                                         |
| json_dumps                 | 6.84 ms                                                             | 7.41 ms: 1.08x slower                                                         |
| genshi_text                | 20.1 ms                                                             | 21.8 ms: 1.09x slower                                                         |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.13 ms: 1.09x slower                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.30 ms: 1.09x slower                                                         |
| pprint_safe_repr           | 607 ms                                                              | 662 ms: 1.09x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                                         |
| mdp                        | 1.60 sec                                                            | 1.75 sec: 1.09x slower                                                        |
| pprint_pformat             | 1.24 sec                                                            | 1.36 sec: 1.10x slower                                                        |
| pycparser                  | 777 ms                                                              | 865 ms: 1.11x slower                                                          |
| async_generators           | 266 ms                                                              | 297 ms: 1.12x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 66.8 ms: 1.12x slower                                                         |
| chaos                      | 48.0 ms                                                             | 53.9 ms: 1.12x slower                                                         |
| spectral_norm              | 68.0 ms                                                             | 77.7 ms: 1.14x slower                                                         |
| comprehensions             | 11.9 us                                                             | 13.6 us: 1.15x slower                                                         |
| mako                       | 6.94 ms                                                             | 7.98 ms: 1.15x slower                                                         |
| tomli_loads                | 1.65 sec                                                            | 1.90 sec: 1.15x slower                                                        |
| pyflate                    | 308 ms                                                              | 356 ms: 1.15x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 48.6 ms: 1.15x slower                                                         |
| float                      | 52.4 ms                                                             | 61.4 ms: 1.17x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 70.5 ms: 1.19x slower                                                         |
| fannkuch                   | 270 ms                                                              | 322 ms: 1.19x slower                                                          |
| nbody                      | 76.9 ms                                                             | 91.6 ms: 1.19x slower                                                         |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.19x slower                                                         |
| pickle_pure_python         | 213 us                                                              | 256 us: 1.20x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.10 ms: 1.21x slower                                                         |
| deltablue                  | 2.23 ms                                                             | 2.70 ms: 1.21x slower                                                         |
| unpickle_pure_python       | 147 us                                                              | 178 us: 1.21x slower                                                          |
| raytrace                   | 189 ms                                                              | 234 ms: 1.24x slower                                                          |
| scimark_fft                | 198 ms                                                              | 246 ms: 1.24x slower                                                          |
| richards                   | 31.2 ms                                                             | 38.8 ms: 1.24x slower                                                         |
| scimark_sor                | 81.0 ms                                                             | 101 ms: 1.24x slower                                                          |
| richards_super             | 35.5 ms                                                             | 44.3 ms: 1.25x slower                                                         |
| generators                 | 21.2 ms                                                             | 26.6 ms: 1.26x slower                                                         |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.6 ms: 1.27x slower                                                         |
| logging_silent             | 57.9 ns                                                             | 74.8 ns: 1.29x slower                                                         |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                  |

Benchmark hidden because not significant (6): asyncio_tcp, async_tree_none_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, regex_effbot, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-pythonperf1_win32-x86-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: unknown