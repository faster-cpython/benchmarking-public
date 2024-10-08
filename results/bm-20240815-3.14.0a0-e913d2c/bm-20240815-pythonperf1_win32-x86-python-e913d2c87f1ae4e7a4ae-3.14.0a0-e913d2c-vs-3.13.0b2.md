# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-x86
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| html5lib       | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 513 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 552 ms: 1.04x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.00x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| float          | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                          |
| nbody          | 76.9 ms                                                             | 93.3 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| regex_effbot   | 1.88 ms                                                             | 1.93 ms: 1.02x slower                                                          |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 69.0 ms: 1.07x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.88 sec: 1.14x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 70.0 ms: 1.17x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 254 us: 1.19x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 178 us: 1.21x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 31.8 ms: 1.06x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 46.8 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.7 ms: 1.13x slower                                                          |
| mako            | 6.94 ms                                                             | 8.13 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.10x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 737 us: 13.20x faster                                                          |
| coverage                   | 307 ms                                                              | 53.0 ms: 5.80x faster                                                          |
| deepcopy                   | 280 us                                                              | 255 us: 1.10x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 513 ms: 1.03x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.8 us: 1.03x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.55 us: 1.02x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 746 us: 1.01x faster                                                           |
| json_loads                 | 20.5 us                                                             | 20.3 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 198 ms: 1.00x faster                                                           |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.2 sec: 1.02x slower                                                         |
| sympy_expand               | 375 ms                                                              | 382 ms: 1.02x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.93 ms: 1.02x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.20 ms: 1.03x slower                                                          |
| json                       | 4.10 ms                                                             | 4.22 ms: 1.03x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 57.6 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 462 ms: 1.03x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.04x slower                                                           |
| async_tree_io              | 530 ms                                                              | 552 ms: 1.04x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 87.3 ms: 1.04x slower                                                          |
| sympy_str                  | 211 ms                                                              | 220 ms: 1.04x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 72.7 ms: 1.05x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 110 ms: 1.05x slower                                                           |
| pprint_safe_repr           | 607 ms                                                              | 639 ms: 1.05x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.57 us: 1.05x slower                                                          |
| django_template            | 30.1 ms                                                             | 31.8 ms: 1.06x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 46.8 ms: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.95 us: 1.07x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.71 sec: 1.07x slower                                                         |
| html5lib                   | 45.4 ms                                                             | 48.6 ms: 1.07x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.94 sec: 1.07x slower                                                         |
| typing_runtime_protocols   | 136 us                                                              | 145 us: 1.07x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 107 ms: 1.07x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 15.7 ms: 1.07x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 69.0 ms: 1.07x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.0 ms: 1.08x slower                                                          |
| chaos                      | 48.0 ms                                                             | 52.0 ms: 1.08x slower                                                          |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.12 ms: 1.09x slower                                                          |
| 2to3                       | 233 ms                                                              | 254 ms: 1.09x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.36 sec: 1.10x slower                                                         |
| sqlglot_optimize           | 39.7 ms                                                             | 43.8 ms: 1.10x slower                                                          |
| pycparser                  | 777 ms                                                              | 858 ms: 1.10x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 733 ms: 1.11x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 230 ms: 1.11x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 82.9 ms: 1.12x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.70 ms: 1.13x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 22.7 ms: 1.13x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.09 ms: 1.13x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.13x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 17.6 ms: 1.14x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.88 sec: 1.14x slower                                                         |
| spectral_norm              | 68.0 ms                                                             | 78.2 ms: 1.15x slower                                                          |
| raytrace                   | 189 ms                                                              | 218 ms: 1.15x slower                                                           |
| async_generators           | 266 ms                                                              | 307 ms: 1.16x slower                                                           |
| scimark_fft                | 198 ms                                                              | 230 ms: 1.16x slower                                                           |
| comprehensions             | 11.9 us                                                             | 13.8 us: 1.17x slower                                                          |
| float                      | 52.4 ms                                                             | 61.2 ms: 1.17x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 69.4 ms: 1.17x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.13 ms: 1.17x slower                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 70.0 ms: 1.17x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 80.6 ms: 1.17x slower                                                          |
| go                         | 101 ms                                                              | 118 ms: 1.17x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 254 us: 1.19x slower                                                           |
| unpickle_pure_python       | 147 us                                                              | 178 us: 1.21x slower                                                           |
| nbody                      | 76.9 ms                                                             | 93.3 ms: 1.21x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 51.2 ms: 1.22x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.72 ms: 1.22x slower                                                          |
| pyflate                    | 308 ms                                                              | 379 ms: 1.23x slower                                                           |
| scimark_sor                | 81.0 ms                                                             | 99.6 ms: 1.23x slower                                                          |
| richards_super             | 35.5 ms                                                             | 43.6 ms: 1.23x slower                                                          |
| richards                   | 31.2 ms                                                             | 38.8 ms: 1.24x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.33 ms: 1.26x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 57.5 ms: 1.27x slower                                                          |
| fannkuch                   | 270 ms                                                              | 347 ms: 1.28x slower                                                           |
| generators                 | 21.2 ms                                                             | 27.2 ms: 1.29x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 77.1 ns: 1.33x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, gc_traversal, async_tree_memoization
Ignored benchmarks (8) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: unknown