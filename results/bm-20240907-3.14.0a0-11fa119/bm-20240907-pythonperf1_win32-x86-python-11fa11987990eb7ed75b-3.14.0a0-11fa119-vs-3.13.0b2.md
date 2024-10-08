# Results vs. 3.13.0b2

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: windows-x86
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 252 ms: 1.08x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 502 ms: 1.05x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 222 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 480 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| float          | 52.4 ms                                                             | 62.0 ms: 1.18x slower                                                          |
| nbody          | 76.9 ms                                                             | 94.3 ms: 1.23x slower                                                          |
| Geometric mean | (ref)                                                               | 1.14x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_dna      | 118 ms                                                              | 124 ms: 1.05x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 109 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.35 us: 1.06x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.4 us: 1.02x faster                                                          |
| pickle               | 8.07 us                                                             | 7.97 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| unpickle_list        | 2.93 us                                                             | 3.02 us: 1.03x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.0 ms: 1.06x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.62 ms: 1.11x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 66.7 ms: 1.12x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.89 sec: 1.15x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 49.5 ms: 1.18x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 255 us: 1.19x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 179 us: 1.22x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.4 ms: 1.11x slower                                                          |
| mako            | 6.94 ms                                                             | 8.27 ms: 1.19x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 719 us: 13.52x faster                                                          |
| coverage                   | 307 ms                                                              | 52.1 ms: 5.90x faster                                                          |
| deepcopy                   | 280 us                                                              | 242 us: 1.15x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.9 us: 1.07x faster                                                          |
| pickle_list                | 3.57 us                                                             | 3.35 us: 1.06x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 502 ms: 1.05x faster                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.47 us: 1.05x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 197 ms: 1.03x faster                                                           |
| async_tree_none            | 228 ms                                                              | 222 ms: 1.03x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 739 us: 1.02x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.4 us: 1.02x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.97 us: 1.01x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.94 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| sympy_expand               | 375 ms                                                              | 381 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 480 ms: 1.02x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| go                         | 101 ms                                                              | 103 ms: 1.02x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| sympy_str                  | 211 ms                                                              | 217 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| unpickle_list              | 2.93 us                                                             | 3.02 us: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 86.9 ms: 1.04x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 72.1 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 470 ms: 1.05x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 58.7 ms: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                          |
| regex_dna                  | 118 ms                                                              | 124 ms: 1.05x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.0 ms: 1.06x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 642 ms: 1.06x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.61 us: 1.06x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.32 sec: 1.06x slower                                                         |
| genshi_xml                 | 44.3 ms                                                             | 47.0 ms: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.94 us: 1.06x slower                                                          |
| pylint                     | 217 ms                                                              | 233 ms: 1.08x slower                                                           |
| django_template            | 30.1 ms                                                             | 32.4 ms: 1.08x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| 2to3                       | 233 ms                                                              | 252 ms: 1.08x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 109 ms: 1.09x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.75 sec: 1.09x slower                                                         |
| meteor_contest             | 74.1 ms                                                             | 81.4 ms: 1.10x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 43.9 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.19 ms: 1.11x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 22.4 ms: 1.11x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.62 ms: 1.11x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 76.5 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 866 ms: 1.11x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.33 ms: 1.12x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.08 ms: 1.12x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 76.0 ms: 1.12x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 66.7 ms: 1.12x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 106 ms: 1.12x slower                                                           |
| async_generators           | 266 ms                                                              | 298 ms: 1.12x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 152 us: 1.12x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 232 ms: 1.12x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| chaos                      | 48.0 ms                                                             | 54.1 ms: 1.13x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 757 ms: 1.14x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.90 ms: 1.14x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.89 sec: 1.15x slower                                                         |
| pyflate                    | 308 ms                                                              | 355 ms: 1.15x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.7 us: 1.16x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.5 ms: 1.18x slower                                                          |
| float                      | 52.4 ms                                                             | 62.0 ms: 1.18x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.4 ms: 1.19x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.27 ms: 1.19x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 255 us: 1.19x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.68 ms: 1.20x slower                                                          |
| raytrace                   | 189 ms                                                              | 229 ms: 1.21x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 179 us: 1.22x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 72.3 ms: 1.22x slower                                                          |
| nbody                      | 76.9 ms                                                             | 94.3 ms: 1.23x slower                                                          |
| richards_super             | 35.5 ms                                                             | 43.7 ms: 1.23x slower                                                          |
| richards                   | 31.2 ms                                                             | 38.8 ms: 1.24x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.25 ms: 1.24x slower                                                          |
| fannkuch                   | 270 ms                                                              | 336 ms: 1.24x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.8 ms: 1.26x slower                                                          |
| scimark_fft                | 198 ms                                                              | 253 ms: 1.28x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 103 ms: 1.28x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 75.2 ns: 1.30x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.6 ms: 1.31x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_memoization, json_loads, regex_effbot, async_tree_memoization_tg, async_tree_io, gc_traversal
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240907-3.14.0a0-11fa119/bm-20240907-pythonperf1_win32-x86-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown