# Results vs. 3.13.0b2

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: windows-x86
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 44.1 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 510 ms: 1.04x faster                                                           |
| async_tree_none_tg         | 203 ms                                                              | 198 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 457 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.9 ms: 1.20x slower                                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle               | 8.07 us                                                             | 7.99 us: 1.01x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 21.0 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.9 ms: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.10 us: 1.06x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.62 ms: 1.11x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 68.2 ms: 1.14x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.89 sec: 1.14x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 49.8 ms: 1.18x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 262 us: 1.23x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 181 us: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                   |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.8 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 46.9 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.2 ms: 1.10x slower                                                          |
| mako            | 6.94 ms                                                             | 8.18 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.11x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 737 us: 13.20x faster                                                          |
| coverage                   | 307 ms                                                              | 54.7 ms: 5.61x faster                                                          |
| deepcopy                   | 280 us                                                              | 246 us: 1.14x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.3 us: 1.06x faster                                                          |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 510 ms: 1.04x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 731 us: 1.03x faster                                                           |
| html5lib                   | 45.4 ms                                                             | 44.1 ms: 1.03x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.39 ms: 1.03x faster                                                          |
| async_tree_none_tg         | 203 ms                                                              | 198 ms: 1.03x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 81.8 ms: 1.02x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.54 us: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.99 us: 1.01x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 69.9 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| pickle_dict                | 20.8 us                                                             | 21.0 us: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 457 ms: 1.02x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.02x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.86 sec: 1.03x slower                                                         |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.3 ms: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                              | 388 ms: 1.03x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.04x slower                                                          |
| go                         | 101 ms                                                              | 104 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 58.1 ms: 1.04x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.9 ms: 1.04x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.4 ms: 1.05x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.37 ms: 1.06x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.10 us: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| genshi_xml                 | 44.3 ms                                                             | 46.9 ms: 1.06x slower                                                          |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.08 ms: 1.07x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.04 us: 1.08x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.77 us: 1.08x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| django_template            | 30.1 ms                                                             | 32.6 ms: 1.08x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 659 ms: 1.09x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 43.2 ms: 1.09x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.8 ms: 1.09x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.35 sec: 1.09x slower                                                         |
| nqueens                    | 68.7 ms                                                             | 74.9 ms: 1.09x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 226 ms: 1.09x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.2 ms: 1.10x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 81.9 ms: 1.11x slower                                                          |
| pycparser                  | 777 ms                                                              | 864 ms: 1.11x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.62 ms: 1.11x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 76.1 ms: 1.12x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.7 ms: 1.12x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.08 ms: 1.13x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.13x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 68.2 ms: 1.14x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.89 sec: 1.14x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 68.1 ms: 1.15x slower                                                          |
| async_generators           | 266 ms                                                              | 305 ms: 1.15x slower                                                           |
| pyflate                    | 308 ms                                                              | 360 ms: 1.17x slower                                                           |
| mako                       | 6.94 ms                                                             | 8.18 ms: 1.18x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.0 us: 1.18x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.8 ms: 1.18x slower                                                          |
| float                      | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| scimark_fft                | 198 ms                                                              | 236 ms: 1.19x slower                                                           |
| nbody                      | 76.9 ms                                                             | 91.9 ms: 1.20x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.7 ms: 1.21x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.15 ms: 1.22x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.72 ms: 1.22x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 262 us: 1.23x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 181 us: 1.23x slower                                                           |
| generators                 | 21.2 ms                                                             | 26.2 ms: 1.24x slower                                                          |
| raytrace                   | 189 ms                                                              | 235 ms: 1.25x slower                                                           |
| fannkuch                   | 270 ms                                                              | 338 ms: 1.25x slower                                                           |
| richards_super             | 35.5 ms                                                             | 45.0 ms: 1.27x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.5 ms: 1.27x slower                                                          |
| richards                   | 31.2 ms                                                             | 39.8 ms: 1.28x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 104 ms: 1.28x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 75.0 ns: 1.30x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_memoization_tg, async_tree_io, json_loads, tornado_http, asyncio_tcp, pickle_list
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-pythonperf1_win32-x86-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown