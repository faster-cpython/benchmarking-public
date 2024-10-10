# Results vs. 3.13.0b2

- fork: mdboom
- ref: disable_interpreter_
- machine: windows-x86
- commit hash: 46655f3
- commit date: 2024-10-09
- overall geometric mean: 1.04x faster
- HPT reliability: 92.60%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 262 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 108 ms: 1.15x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 510 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 477 ms: 1.07x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_memoization_tg, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.9 ms: 1.45x faster                                                          |
| float          | 52.4 ms                                                             | 45.3 ms: 1.16x faster                                                          |
| pidigits       | 199 ms                                                              | 205 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                               | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 114 ms: 1.04x faster                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.84 ms: 1.03x faster                                                          |
| regex_compile  | 99.9 ms                                                             | 106 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_generate   | 59.6 ms                                                             | 54.1 ms: 1.10x faster                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| pickle_list          | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 40.6 ms: 1.04x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 63.4 ms: 1.01x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.79 ms: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| pickle_dict          | 20.8 us                                                             | 21.6 us: 1.04x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 109 ms: 1.05x slower                                                           |
| pickle               | 8.07 us                                                             | 8.46 us: 1.05x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 159 us: 1.08x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 250 us: 1.17x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.69 ms: 1.22x faster                                                          |
| django_template | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 23.4 ms: 1.17x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 54.6 ms: 1.23x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.06x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 756 us: 12.86x faster                                                          |
| coverage                   | 307 ms                                                              | 51.6 ms: 5.95x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 104 ms: 1.98x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 15.2 us: 1.55x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.9 ms: 1.45x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 50.9 ms: 1.33x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.69 ms: 1.22x faster                                                          |
| deepcopy                   | 280 us                                                              | 232 us: 1.20x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.41 ms: 1.19x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 47.8 ms: 1.17x faster                                                          |
| scimark_fft                | 198 ms                                                              | 170 ms: 1.16x faster                                                           |
| scimark_sor                | 81.0 ms                                                             | 69.6 ms: 1.16x faster                                                          |
| float                      | 52.4 ms                                                             | 45.3 ms: 1.16x faster                                                          |
| fannkuch                   | 270 ms                                                              | 239 ms: 1.13x faster                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 54.1 ms: 1.10x faster                                                          |
| deltablue                  | 2.23 ms                                                             | 2.03 ms: 1.10x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.39 us: 1.08x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.53 sec: 1.08x faster                                                         |
| pyflate                    | 308 ms                                                              | 288 ms: 1.07x faster                                                           |
| pprint_safe_repr           | 607 ms                                                              | 572 ms: 1.06x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.19 sec: 1.04x faster                                                         |
| async_tree_none            | 228 ms                                                              | 219 ms: 1.04x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.89 us: 1.04x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 510 ms: 1.04x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.44 us: 1.04x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 40.6 ms: 1.04x faster                                                          |
| regex_dna                  | 118 ms                                                              | 114 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 196 ms: 1.03x faster                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.84 ms: 1.03x faster                                                          |
| scimark_lu                 | 59.4 ms                                                             | 57.9 ms: 1.03x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 56.7 ns: 1.02x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 63.4 ms: 1.01x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.79 ms: 1.01x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.44 ms: 1.01x slower                                                          |
| json                       | 4.10 ms                                                             | 4.14 ms: 1.01x slower                                                          |
| comprehensions             | 11.9 us                                                             | 12.1 us: 1.02x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.02x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.36 us: 1.03x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.69 us: 1.03x slower                                                          |
| json_loads                 | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.4 sec: 1.03x slower                                                         |
| pidigits                   | 199 ms                                                              | 205 ms: 1.03x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 46.8 ms: 1.04x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 784 us: 1.04x slower                                                           |
| pickle_dict                | 20.8 us                                                             | 21.6 us: 1.04x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 109 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 494 ms: 1.05x slower                                                           |
| pickle                     | 8.07 us                                                             | 8.46 us: 1.05x slower                                                          |
| richards_super             | 35.5 ms                                                             | 37.4 ms: 1.05x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 88.4 ms: 1.05x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.02 ms: 1.06x slower                                                          |
| pycparser                  | 777 ms                                                              | 824 ms: 1.06x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| regex_compile              | 99.9 ms                                                             | 106 ms: 1.06x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 477 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| sympy_expand               | 375 ms                                                              | 403 ms: 1.07x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.6 us: 1.08x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 159 us: 1.08x slower                                                           |
| richards                   | 31.2 ms                                                             | 33.8 ms: 1.08x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.8 ms: 1.09x slower                                                          |
| sympy_str                  | 211 ms                                                              | 230 ms: 1.09x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 75.1 ms: 1.09x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 20.2 ms: 1.11x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 117 ms: 1.12x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 77.8 ms: 1.12x slower                                                          |
| 2to3                       | 233 ms                                                              | 262 ms: 1.12x slower                                                           |
| chaos                      | 48.0 ms                                                             | 53.9 ms: 1.12x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.34 ms: 1.13x slower                                                          |
| docutils                   | 1.81 sec                                                            | 2.05 sec: 1.13x slower                                                         |
| tornado_http               | 94.3 ms                                                             | 108 ms: 1.15x slower                                                           |
| generators                 | 21.2 ms                                                             | 24.4 ms: 1.15x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 23.4 ms: 1.17x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.1 ms: 1.17x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 250 us: 1.17x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 17.6 ms: 1.20x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.08 ms: 1.20x slower                                                          |
| asyncio_tcp                | 662 ms                                                              | 809 ms: 1.22x slower                                                           |
| async_generators           | 266 ms                                                              | 326 ms: 1.23x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 54.6 ms: 1.23x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 50.1 ms: 1.26x slower                                                          |
| pylint                     | 217 ms                                                              | 281 ms: 1.30x slower                                                           |
| raytrace                   | 189 ms                                                              | 253 ms: 1.34x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (9): async_tree_memoization_tg, async_tree_memoization, go, html5lib, unpickle_list, regex_v8, telco, meteor_contest, async_tree_io
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241009-3.14.0a0-46655f3-JIT/bm-20241009-pythonperf1_win32-x86-mdboom-disable_interpreter_-3.14.0a0-46655f3.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 92.60% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown