# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: windows-x86
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.06x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.96 sec: 1.08x slower                                                         |
| html5lib       | 45.4 ms                                                             | 51.4 ms: 1.13x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 232 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 484 ms: 1.03x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 287 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.05x slower                                                           |
| async_tree_io              | 530 ms                                                              | 570 ms: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (3): async_tree_io_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| float          | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                          |
| nbody          | 76.9 ms                                                             | 102 ms: 1.32x slower                                                           |
| Geometric mean | (ref)                                                               | 1.16x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 2.05 ms: 1.09x slower                                                          |
| regex_dna      | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| regex_compile  | 99.9 ms                                                             | 111 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 65.8 ms: 1.10x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.71 ms: 1.13x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 49.1 ms: 1.17x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 174 us: 1.18x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 266 us: 1.25x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 50.4 ms: 1.14x slower                                                          |
| django_template | 30.1 ms                                                             | 34.9 ms: 1.16x slower                                                          |
| mako            | 6.94 ms                                                             | 8.31 ms: 1.20x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.4 ms: 1.21x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.18x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 751 us: 12.95x faster                                                          |
| coverage                   | 307 ms                                                              | 52.2 ms: 5.89x faster                                                          |
| deepcopy                   | 280 us                                                              | 264 us: 1.06x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 23.0 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 105 ms: 1.01x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                         |
| async_tree_none            | 228 ms                                                              | 232 ms: 1.02x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 484 ms: 1.03x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.66 us: 1.03x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.4 ms: 1.04x slower                                                          |
| async_tree_memoization     | 275 ms                                                              | 287 ms: 1.04x slower                                                           |
| sympy_expand               | 375 ms                                                              | 392 ms: 1.05x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 472 ms: 1.05x slower                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.7 ms: 1.06x slower                                                          |
| json                       | 4.10 ms                                                             | 4.34 ms: 1.06x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 89.3 ms: 1.06x slower                                                          |
| sympy_str                  | 211 ms                                                              | 225 ms: 1.07x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.7 ms: 1.07x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 74.2 ms: 1.07x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 112 ms: 1.07x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 59.8 ms: 1.07x slower                                                          |
| async_tree_io              | 530 ms                                                              | 570 ms: 1.08x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.6 ms: 1.08x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.96 sec: 1.08x slower                                                         |
| regex_effbot               | 1.88 ms                                                             | 2.05 ms: 1.09x slower                                                          |
| regex_dna                  | 118 ms                                                              | 129 ms: 1.09x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.60 ms: 1.10x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 16.1 ms: 1.10x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.76 sec: 1.10x slower                                                         |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.17 ms: 1.10x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 65.8 ms: 1.10x slower                                                          |
| pylint                     | 217 ms                                                              | 239 ms: 1.10x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.98 us: 1.10x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.27 us: 1.11x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 229 ms: 1.11x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 111 ms: 1.12x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.39 sec: 1.12x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 152 us: 1.12x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 44.6 ms: 1.12x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.71 ms: 1.13x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 685 ms: 1.13x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 107 ms: 1.13x slower                                                           |
| html5lib                   | 45.4 ms                                                             | 51.4 ms: 1.13x slower                                                          |
| 2to3                       | 233 ms                                                              | 264 ms: 1.13x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 83.9 ms: 1.13x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 50.4 ms: 1.14x slower                                                          |
| chaos                      | 48.0 ms                                                             | 54.7 ms: 1.14x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.7 ms: 1.14x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 78.0 ms: 1.15x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 79.0 ms: 1.15x slower                                                          |
| async_generators           | 266 ms                                                              | 306 ms: 1.15x slower                                                           |
| django_template            | 30.1 ms                                                             | 34.9 ms: 1.16x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.91 sec: 1.16x slower                                                         |
| sqlglot_transpile          | 1.19 ms                                                             | 1.38 ms: 1.16x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.12 ms: 1.16x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 49.1 ms: 1.17x slower                                                          |
| pyflate                    | 308 ms                                                              | 360 ms: 1.17x slower                                                           |
| float                      | 52.4 ms                                                             | 61.5 ms: 1.17x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 174 us: 1.18x slower                                                           |
| pycparser                  | 777 ms                                                              | 918 ms: 1.18x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 785 ms: 1.19x slower                                                           |
| scimark_fft                | 198 ms                                                              | 235 ms: 1.19x slower                                                           |
| comprehensions             | 11.9 us                                                             | 14.1 us: 1.19x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.31 ms: 1.20x slower                                                          |
| fannkuch                   | 270 ms                                                              | 325 ms: 1.20x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 24.4 ms: 1.21x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 72.4 ms: 1.22x slower                                                          |
| go                         | 101 ms                                                              | 124 ms: 1.23x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 101 ms: 1.24x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 266 us: 1.25x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.84 ms: 1.27x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.40 ms: 1.28x slower                                                          |
| raytrace                   | 189 ms                                                              | 241 ms: 1.28x slower                                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 58.2 ms: 1.29x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 75.3 ns: 1.30x slower                                                          |
| generators                 | 21.2 ms                                                             | 27.9 ms: 1.32x slower                                                          |
| nbody                      | 76.9 ms                                                             | 102 ms: 1.32x slower                                                           |
| richards_super             | 35.5 ms                                                             | 47.4 ms: 1.34x slower                                                          |
| richards                   | 31.2 ms                                                             | 43.7 ms: 1.40x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.06x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_io_tg, create_gc_cycles, async_tree_none_tg, gc_traversal, async_tree_memoization_tg
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf1_win32-x86-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.09x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: unknown