# Results vs. 3.13.0b2

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: windows-x86
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.02x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                                         |
| html5lib       | 45.4 ms                                                             | 50.1 ms: 1.10x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 101 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 238 ms: 1.04x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 266 ms: 1.05x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 294 ms: 1.07x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 506 ms: 1.07x slower                                                           |
| async_tree_io              | 530 ms                                                              | 576 ms: 1.09x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 493 ms: 1.10x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 55.3 ms: 1.39x faster                                                          |
| float          | 52.4 ms                                                             | 44.5 ms: 1.18x faster                                                          |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.57 sec: 1.05x faster                                                         |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.7 ms: 1.02x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 223 us: 1.05x slower                                                           |
| json_dumps           | 6.84 ms                                                             | 7.26 ms: 1.06x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 63.9 ms: 1.07x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 159 us: 1.08x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 48.5 ms: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.4 ms: 1.05x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.36 ms: 1.29x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 24.0 ms: 1.19x slower                                                          |
| django_template | 30.1 ms                                                             | 36.0 ms: 1.20x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 57.0 ms: 1.29x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.09x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf1_win32-x86-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 808 us: 12.05x faster                                                          |
| coverage                   | 307 ms                                                              | 52.6 ms: 5.84x faster                                                          |
| sqlglot_normalize          | 206 ms                                                              | 101 ms: 2.04x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 16.3 us: 1.44x faster                                                          |
| nbody                      | 76.9 ms                                                             | 55.3 ms: 1.39x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 49.3 ms: 1.38x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.36 ms: 1.29x faster                                                          |
| scimark_fft                | 198 ms                                                              | 163 ms: 1.22x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.37 ms: 1.21x faster                                                          |
| float                      | 52.4 ms                                                             | 44.5 ms: 1.18x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 48.0 ms: 1.16x faster                                                          |
| fannkuch                   | 270 ms                                                              | 236 ms: 1.14x faster                                                           |
| deepcopy                   | 280 us                                                              | 254 us: 1.10x faster                                                           |
| pyflate                    | 308 ms                                                              | 284 ms: 1.09x faster                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 42.2 ms: 1.07x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.65 ms: 1.07x faster                                                          |
| asyncio_tcp                | 662 ms                                                              | 629 ms: 1.05x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.57 sec: 1.05x faster                                                         |
| comprehensions             | 11.9 us                                                             | 11.5 us: 1.03x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.7 ms: 1.02x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 594 ms: 1.02x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.22 sec: 1.02x faster                                                         |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| xml_etree_parse            | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_dna                  | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.64 us: 1.02x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 76.2 ms: 1.03x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.65 sec: 1.03x slower                                                         |
| json_loads                 | 20.5 us                                                             | 21.2 us: 1.03x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 59.9 ns: 1.03x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.24 ms: 1.04x slower                                                          |
| sympy_expand               | 375 ms                                                              | 391 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                          |
| async_tree_none            | 228 ms                                                              | 238 ms: 1.04x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 223 us: 1.05x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 266 ms: 1.05x slower                                                           |
| async_tree_none_tg         | 203 ms                                                              | 213 ms: 1.05x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.4 ms: 1.05x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.3 ms: 1.06x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 111 ms: 1.06x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 2.00 ms: 1.06x slower                                                          |
| sympy_str                  | 211 ms                                                              | 224 ms: 1.06x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.26 ms: 1.06x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 73.2 ms: 1.07x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 294 ms: 1.07x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 101 ms: 1.07x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 63.9 ms: 1.07x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 506 ms: 1.07x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 74.6 ms: 1.08x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 159 us: 1.08x slower                                                           |
| async_tree_io              | 530 ms                                                              | 576 ms: 1.09x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.86 us: 1.09x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 16.0 ms: 1.09x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 4.63 ms: 1.09x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.18 us: 1.09x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 493 ms: 1.10x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 50.1 ms: 1.10x slower                                                          |
| 2to3                       | 233 ms                                                              | 261 ms: 1.12x slower                                                           |
| chaos                      | 48.0 ms                                                             | 54.7 ms: 1.14x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 45.7 ms: 1.15x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 48.5 ms: 1.15x slower                                                          |
| richards                   | 31.2 ms                                                             | 36.0 ms: 1.15x slower                                                          |
| pycparser                  | 777 ms                                                              | 897 ms: 1.15x slower                                                           |
| pylint                     | 217 ms                                                              | 252 ms: 1.16x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 157 us: 1.16x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 24.0 ms: 1.19x slower                                                          |
| django_template            | 30.1 ms                                                             | 36.0 ms: 1.20x slower                                                          |
| go                         | 101 ms                                                              | 121 ms: 1.20x slower                                                           |
| richards_super             | 35.5 ms                                                             | 44.2 ms: 1.25x slower                                                          |
| async_generators           | 266 ms                                                              | 336 ms: 1.27x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 19.8 ms: 1.28x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 57.0 ms: 1.29x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.95 ms: 1.32x slower                                                          |
| raytrace                   | 189 ms                                                              | 252 ms: 1.34x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 111 ms: 1.37x slower                                                           |
| scimark_lu                 | 59.4 ms                                                             | 82.1 ms: 1.38x slower                                                          |
| generators                 | 21.2 ms                                                             | 29.9 ms: 1.41x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x faster                                                                   |

Benchmark hidden because not significant (8): create_gc_cycles, pathlib, regex_compile, gc_traversal, asyncio_tcp_ssl, sqlglot_parse, bench_thread_pool, async_tree_io_tg
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.51% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown