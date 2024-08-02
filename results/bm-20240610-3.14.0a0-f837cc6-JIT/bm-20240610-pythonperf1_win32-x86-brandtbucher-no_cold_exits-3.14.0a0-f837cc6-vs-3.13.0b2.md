# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: no_cold_exits
- machine: windows-x86
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.07x faster
- HPT reliability: 62.11%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 244 ms: 1.05x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                        |
| html5lib       | 45.4 ms                                                             | 45.9 ms: 1.01x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                  |

Benchmark hidden because not significant (5): async_tree_io, async_tree_none, async_tree_io_tg, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                         |
| float          | 52.4 ms                                                             | 41.6 ms: 1.26x faster                                                         |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                          |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 96.3 ms: 1.04x faster                                                         |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                         |
| regex_dna      | 118 ms                                                              | 124 ms: 1.05x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                         |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                        |
| xml_etree_generate   | 59.6 ms                                                             | 54.5 ms: 1.09x faster                                                         |
| unpickle_pure_python | 147 us                                                              | 135 us: 1.09x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.76 us: 1.06x faster                                                         |
| pickle_pure_python   | 213 us                                                              | 201 us: 1.06x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.1 ms: 1.05x faster                                                         |
| xml_etree_parse      | 104 ms                                                              | 99.5 ms: 1.05x faster                                                         |
| xml_etree_process    | 42.1 ms                                                             | 40.2 ms: 1.05x faster                                                         |
| json_dumps           | 6.84 ms                                                             | 6.66 ms: 1.03x faster                                                         |
| pickle_dict          | 20.8 us                                                             | 20.9 us: 1.00x slower                                                         |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                         |
| pickle               | 8.07 us                                                             | 8.24 us: 1.02x slower                                                         |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                         |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 18.5 ms: 1.02x slower                                                         |
| python_startup         | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                         |
| Geometric mean         | (ref)                                                               | 1.02x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-----------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.33 ms: 1.30x faster                                                         |
| genshi_text     | 20.1 ms                                                             | 21.0 ms: 1.05x slower                                                         |
| django_template | 30.1 ms                                                             | 31.7 ms: 1.06x slower                                                         |
| genshi_xml      | 44.3 ms                                                             | 50.7 ms: 1.15x slower                                                         |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240610-pythonperf1_win32-x86-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------------|:-------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 712 us: 13.66x faster                                                         |
| coverage                   | 307 ms                                                              | 48.6 ms: 6.32x faster                                                         |
| nbody                      | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                         |
| spectral_norm              | 68.0 ms                                                             | 47.9 ms: 1.42x faster                                                         |
| mako                       | 6.94 ms                                                             | 5.33 ms: 1.30x faster                                                         |
| fannkuch                   | 270 ms                                                              | 211 ms: 1.28x faster                                                          |
| float                      | 52.4 ms                                                             | 41.6 ms: 1.26x faster                                                         |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.34 ms: 1.23x faster                                                         |
| scimark_fft                | 198 ms                                                              | 163 ms: 1.21x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                        |
| deepcopy_memo              | 23.5 us                                                             | 20.0 us: 1.18x faster                                                         |
| telco                      | 6.03 ms                                                             | 5.23 ms: 1.15x faster                                                         |
| crypto_pyaes               | 55.8 ms                                                             | 48.5 ms: 1.15x faster                                                         |
| pyflate                    | 308 ms                                                              | 270 ms: 1.14x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 39.9 ms: 1.13x faster                                                         |
| pprint_safe_repr           | 607 ms                                                              | 550 ms: 1.10x faster                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.13 sec: 1.10x faster                                                        |
| xml_etree_generate         | 59.6 ms                                                             | 54.5 ms: 1.09x faster                                                         |
| unpickle_pure_python       | 147 us                                                              | 135 us: 1.09x faster                                                          |
| sqlglot_parse              | 964 us                                                              | 899 us: 1.07x faster                                                          |
| richards                   | 31.2 ms                                                             | 29.2 ms: 1.07x faster                                                         |
| richards_super             | 35.5 ms                                                             | 33.3 ms: 1.07x faster                                                         |
| unpickle_list              | 2.93 us                                                             | 2.76 us: 1.06x faster                                                         |
| pickle_pure_python         | 213 us                                                              | 201 us: 1.06x faster                                                          |
| logging_silent             | 57.9 ns                                                             | 54.8 ns: 1.06x faster                                                         |
| asyncio_tcp                | 662 ms                                                              | 626 ms: 1.06x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.1 ms: 1.05x faster                                                         |
| xml_etree_parse            | 104 ms                                                              | 99.5 ms: 1.05x faster                                                         |
| comprehensions             | 11.9 us                                                             | 11.3 us: 1.05x faster                                                         |
| xml_etree_process          | 42.1 ms                                                             | 40.2 ms: 1.05x faster                                                         |
| logging_format             | 8.13 us                                                             | 7.82 us: 1.04x faster                                                         |
| regex_compile              | 99.9 ms                                                             | 96.3 ms: 1.04x faster                                                         |
| logging_simple             | 7.47 us                                                             | 7.21 us: 1.04x faster                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.16 ms: 1.03x faster                                                         |
| json_dumps                 | 6.84 ms                                                             | 6.66 ms: 1.03x faster                                                         |
| meteor_contest             | 74.1 ms                                                             | 72.3 ms: 1.02x faster                                                         |
| sqlite_synth               | 1.96 us                                                             | 1.92 us: 1.02x faster                                                         |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                          |
| nqueens                    | 68.7 ms                                                             | 67.4 ms: 1.02x faster                                                         |
| pathlib                    | 83.9 ms                                                             | 82.7 ms: 1.01x faster                                                         |
| mdp                        | 1.60 sec                                                            | 1.59 sec: 1.01x faster                                                        |
| sympy_expand               | 375 ms                                                              | 374 ms: 1.00x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.9 us: 1.00x slower                                                         |
| json_loads                 | 20.5 us                                                             | 20.7 us: 1.01x slower                                                         |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                         |
| html5lib                   | 45.4 ms                                                             | 45.9 ms: 1.01x slower                                                         |
| gc_traversal               | 1.43 ms                                                             | 1.46 ms: 1.02x slower                                                         |
| python_startup_no_site     | 18.2 ms                                                             | 18.5 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                          |
| pickle                     | 8.07 us                                                             | 8.24 us: 1.02x slower                                                         |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.02x slower                                                          |
| pycparser                  | 777 ms                                                              | 795 ms: 1.02x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 261 ms: 1.03x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                         |
| python_startup             | 22.2 ms                                                             | 22.9 ms: 1.03x slower                                                         |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                        |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 464 ms: 1.04x slower                                                          |
| 2to3                       | 233 ms                                                              | 244 ms: 1.05x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.0 ms: 1.05x slower                                                         |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                         |
| sqlglot_optimize           | 39.7 ms                                                             | 41.7 ms: 1.05x slower                                                         |
| json                       | 4.10 ms                                                             | 4.30 ms: 1.05x slower                                                         |
| bench_mp_pool              | 69.4 ms                                                             | 73.0 ms: 1.05x slower                                                         |
| hexiom                     | 4.23 ms                                                             | 4.45 ms: 1.05x slower                                                         |
| regex_dna                  | 118 ms                                                              | 124 ms: 1.05x slower                                                          |
| django_template            | 30.1 ms                                                             | 31.7 ms: 1.06x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.06x slower                                                         |
| deepcopy_reduce            | 2.59 us                                                             | 2.74 us: 1.06x slower                                                         |
| sqlglot_normalize          | 206 ms                                                              | 219 ms: 1.06x slower                                                          |
| chaos                      | 48.0 ms                                                             | 51.3 ms: 1.07x slower                                                         |
| deepcopy                   | 280 us                                                              | 300 us: 1.07x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 146 us: 1.07x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 87.6 ms: 1.08x slower                                                         |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                          |
| go                         | 101 ms                                                              | 111 ms: 1.10x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.5 ms: 1.11x slower                                                         |
| deltablue                  | 2.23 ms                                                             | 2.51 ms: 1.12x slower                                                         |
| raytrace                   | 189 ms                                                              | 213 ms: 1.13x slower                                                          |
| async_generators           | 266 ms                                                              | 301 ms: 1.13x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 50.7 ms: 1.15x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 71.1 ms: 1.20x slower                                                         |
| Geometric mean             | (ref)                                                               | 1.07x faster                                                                  |

Benchmark hidden because not significant (11): bench_thread_pool, async_tree_io, asyncio_tcp_ssl, create_gc_cycles, sympy_str, async_tree_none, pickle_list, coroutines, async_tree_io_tg, async_tree_memoization, async_tree_none_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging

# HPT report

- Reliability score: 62.11% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown