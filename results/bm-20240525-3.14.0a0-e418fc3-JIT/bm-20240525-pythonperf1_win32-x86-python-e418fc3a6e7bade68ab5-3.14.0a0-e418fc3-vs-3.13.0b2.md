# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: windows-x86
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.05x faster
- HPT reliability: 90.18%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| html5lib       | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                          |
| tornado_http   | 94.3 ms                                                             | 96.9 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 457 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_none, async_tree_none_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                          |
| float          | 52.4 ms                                                             | 41.8 ms: 1.25x faster                                                          |
| pidigits       | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 98.3 ms: 1.02x faster                                                          |
| regex_dna      | 118 ms                                                              | 118 ms: 1.00x faster                                                           |
| regex_v8       | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.41 sec: 1.17x faster                                                         |
| unpickle_pure_python | 147 us                                                              | 135 us: 1.09x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 55.7 ms: 1.07x faster                                                          |
| pickle_pure_python   | 213 us                                                              | 201 us: 1.06x faster                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.0 ms: 1.05x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 41.1 ms: 1.02x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.88 us: 1.02x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.76 ms: 1.01x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| xml_etree_parse      | 104 ms                                                              | 103 ms: 1.01x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): pickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.29 ms: 1.31x faster                                                          |
| genshi_text     | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                          |
| django_template | 30.1 ms                                                             | 32.3 ms: 1.07x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 51.3 ms: 1.16x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf1_win32-x86-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 710 us: 13.70x faster                                                          |
| coverage                   | 307 ms                                                              | 49.9 ms: 6.16x faster                                                          |
| nbody                      | 76.9 ms                                                             | 52.6 ms: 1.46x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.6 ms: 1.43x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.29 ms: 1.31x faster                                                          |
| float                      | 52.4 ms                                                             | 41.8 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.36 ms: 1.22x faster                                                          |
| fannkuch                   | 270 ms                                                              | 225 ms: 1.20x faster                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.41 sec: 1.17x faster                                                         |
| deepcopy_memo              | 23.5 us                                                             | 20.6 us: 1.14x faster                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 49.7 ms: 1.12x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 40.9 ms: 1.10x faster                                                          |
| telco                      | 6.03 ms                                                             | 5.51 ms: 1.09x faster                                                          |
| unpickle_pure_python       | 147 us                                                              | 135 us: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                              | 608 ms: 1.09x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.15 sec: 1.08x faster                                                         |
| pprint_safe_repr           | 607 ms                                                              | 562 ms: 1.08x faster                                                           |
| scimark_fft                | 198 ms                                                              | 185 ms: 1.07x faster                                                           |
| comprehensions             | 11.9 us                                                             | 11.1 us: 1.07x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 55.7 ms: 1.07x faster                                                          |
| sqlglot_parse              | 964 us                                                              | 908 us: 1.06x faster                                                           |
| pickle_pure_python         | 213 us                                                              | 201 us: 1.06x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.0 ms: 1.05x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.87 us: 1.05x faster                                                          |
| logging_format             | 8.13 us                                                             | 7.93 us: 1.03x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 41.1 ms: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                              | 195 ms: 1.02x faster                                                           |
| unpickle_list              | 2.93 us                                                             | 2.88 us: 1.02x faster                                                          |
| regex_compile              | 99.9 ms                                                             | 98.3 ms: 1.02x faster                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.17 ms: 1.02x faster                                                          |
| logging_simple             | 7.47 us                                                             | 7.35 us: 1.02x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 72.9 ms: 1.02x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.76 ms: 1.01x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.5 us: 1.01x faster                                                          |
| xml_etree_parse            | 104 ms                                                              | 103 ms: 1.01x faster                                                           |
| html5lib                   | 45.4 ms                                                             | 45.1 ms: 1.01x faster                                                          |
| regex_dna                  | 118 ms                                                              | 118 ms: 1.00x faster                                                           |
| sympy_str                  | 211 ms                                                              | 212 ms: 1.01x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.9 ms: 1.01x slower                                                          |
| sympy_expand               | 375 ms                                                              | 379 ms: 1.01x slower                                                           |
| richards_super             | 35.5 ms                                                             | 35.9 ms: 1.01x slower                                                          |
| create_gc_cycles           | 756 us                                                              | 765 us: 1.01x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 137 us: 1.01x slower                                                           |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 69.6 ms: 1.01x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.63 sec: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 457 ms: 1.02x slower                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.47 ms: 1.02x slower                                                          |
| richards                   | 31.2 ms                                                             | 31.9 ms: 1.02x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 96.9 ms: 1.03x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.21 ms: 1.03x slower                                                          |
| pathlib                    | 83.9 ms                                                             | 86.4 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| pycparser                  | 777 ms                                                              | 811 ms: 1.04x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 16.2 ms: 1.05x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.98 ms: 1.05x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 21.4 ms: 1.06x slower                                                          |
| 2to3                       | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| sympy_integrate            | 14.6 ms                                                             | 15.6 ms: 1.07x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 42.5 ms: 1.07x slower                                                          |
| chaos                      | 48.0 ms                                                             | 51.4 ms: 1.07x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.3 ms: 1.07x slower                                                          |
| chameleon                  | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 222 ms: 1.08x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.58 ms: 1.08x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 75.4 ms: 1.09x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.84 us: 1.10x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.4 ms: 1.11x slower                                                          |
| deepcopy                   | 280 us                                                              | 310 us: 1.11x slower                                                           |
| pylint                     | 217 ms                                                              | 241 ms: 1.11x slower                                                           |
| async_generators           | 266 ms                                                              | 296 ms: 1.12x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.8 ms: 1.12x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 90.3 ms: 1.12x slower                                                          |
| raytrace                   | 189 ms                                                              | 211 ms: 1.12x slower                                                           |
| go                         | 101 ms                                                              | 113 ms: 1.12x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.57 ms: 1.15x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 51.3 ms: 1.16x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 72.1 ms: 1.21x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                                   |

Benchmark hidden because not significant (14): logging_silent, async_tree_none, bench_thread_pool, asyncio_tcp_ssl, flaskblogging, async_tree_none_tg, pickle_list, async_tree_memoization, async_tree_io_tg, pickle, async_tree_cpu_io_mixed, async_tree_memoization_tg, pyflate, async_tree_io

# HPT report

- Reliability score: 90.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown