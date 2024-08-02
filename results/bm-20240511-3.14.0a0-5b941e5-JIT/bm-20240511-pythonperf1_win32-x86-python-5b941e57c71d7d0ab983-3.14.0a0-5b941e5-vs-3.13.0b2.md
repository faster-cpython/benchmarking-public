# Results vs. 3.13.0b2

- fork: python
- ref: 5b941e57c71d7d0ab983
- machine: windows-x86
- commit hash: 5b941e5
- commit date: 2024-05-11
- overall geometric mean: 1.05x faster
- HPT reliability: 93.07%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| tornado_http   | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 533 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| async_tree_memoization_tg  | 254 ms                                                              | 260 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_none, async_tree_io, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 55.2 ms: 1.39x faster                                                          |
| float          | 52.4 ms                                                             | 41.1 ms: 1.27x faster                                                          |
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                               | 1.21x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 92.2 ms: 1.08x faster                                                          |
| regex_v8       | 15.7 ms                                                             | 15.6 ms: 1.01x faster                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 55.3 ms: 1.08x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 137 us: 1.07x faster                                                           |
| unpickle_list        | 2.93 us                                                             | 2.73 us: 1.07x faster                                                          |
| pickle_pure_python   | 213 us                                                              | 202 us: 1.06x faster                                                           |
| json_dumps           | 6.84 ms                                                             | 6.53 ms: 1.05x faster                                                          |
| xml_etree_process    | 42.1 ms                                                             | 40.2 ms: 1.05x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| pickle               | 8.07 us                                                             | 8.19 us: 1.01x slower                                                          |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.03x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): pickle_list, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.11x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.31 ms: 1.31x faster                                                          |
| django_template | 30.1 ms                                                             | 32.0 ms: 1.06x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.2 ms: 1.10x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 52.3 ms: 1.18x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240511-pythonperf1_win32-x86-python-5b941e57c71d7d0ab983-3.14.0a0-5b941e5 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 734 us: 13.26x faster                                                          |
| coverage                   | 307 ms                                                              | 51.2 ms: 6.00x faster                                                          |
| spectral_norm              | 68.0 ms                                                             | 47.2 ms: 1.44x faster                                                          |
| nbody                      | 76.9 ms                                                             | 55.2 ms: 1.39x faster                                                          |
| mako                       | 6.94 ms                                                             | 5.31 ms: 1.31x faster                                                          |
| float                      | 52.4 ms                                                             | 41.1 ms: 1.27x faster                                                          |
| fannkuch                   | 270 ms                                                              | 220 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.34 ms: 1.23x faster                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.39 sec: 1.18x faster                                                         |
| scimark_fft                | 198 ms                                                              | 168 ms: 1.18x faster                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 47.9 ms: 1.17x faster                                                          |
| deepcopy_memo              | 23.5 us                                                             | 20.8 us: 1.13x faster                                                          |
| comprehensions             | 11.9 us                                                             | 10.8 us: 1.10x faster                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 41.2 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 607 ms                                                              | 560 ms: 1.08x faster                                                           |
| regex_compile              | 99.9 ms                                                             | 92.2 ms: 1.08x faster                                                          |
| xml_etree_generate         | 59.6 ms                                                             | 55.3 ms: 1.08x faster                                                          |
| unpickle_pure_python       | 147 us                                                              | 137 us: 1.07x faster                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.16 sec: 1.07x faster                                                         |
| unpickle_list              | 2.93 us                                                             | 2.73 us: 1.07x faster                                                          |
| sqlglot_parse              | 964 us                                                              | 903 us: 1.07x faster                                                           |
| logging_silent             | 57.9 ns                                                             | 54.7 ns: 1.06x faster                                                          |
| pickle_pure_python         | 213 us                                                              | 202 us: 1.06x faster                                                           |
| telco                      | 6.03 ms                                                             | 5.72 ms: 1.05x faster                                                          |
| json_dumps                 | 6.84 ms                                                             | 6.53 ms: 1.05x faster                                                          |
| xml_etree_process          | 42.1 ms                                                             | 40.2 ms: 1.05x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.88 us: 1.04x faster                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 61.8 ms: 1.04x faster                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.16 ms: 1.02x faster                                                          |
| sympy_str                  | 211 ms                                                              | 208 ms: 1.02x faster                                                           |
| sympy_expand               | 375 ms                                                              | 369 ms: 1.02x faster                                                           |
| logging_format             | 8.13 us                                                             | 8.03 us: 1.01x faster                                                          |
| logging_simple             | 7.47 us                                                             | 7.37 us: 1.01x faster                                                          |
| meteor_contest             | 74.1 ms                                                             | 73.3 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| regex_v8                   | 15.7 ms                                                             | 15.6 ms: 1.01x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| pycparser                  | 777 ms                                                              | 781 ms: 1.01x slower                                                           |
| richards_super             | 35.5 ms                                                             | 35.7 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 529 ms                                                              | 533 ms: 1.01x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 69.2 ms: 1.01x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.63 sec: 1.01x slower                                                         |
| pickle                     | 8.07 us                                                             | 8.19 us: 1.01x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 479 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.03x slower                                                          |
| async_tree_memoization_tg  | 254 ms                                                              | 260 ms: 1.03x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 97.0 ms: 1.03x slower                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.67 us: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 463 ms: 1.03x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 140 us: 1.04x slower                                                           |
| docutils                   | 1.81 sec                                                            | 1.88 sec: 1.04x slower                                                         |
| pathlib                    | 83.9 ms                                                             | 87.9 ms: 1.05x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 41.7 ms: 1.05x slower                                                          |
| go                         | 101 ms                                                              | 106 ms: 1.05x slower                                                           |
| regex_effbot               | 1.88 ms                                                             | 1.99 ms: 1.05x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| json                       | 4.10 ms                                                             | 4.34 ms: 1.06x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.06x slower                                                          |
| django_template            | 30.1 ms                                                             | 32.0 ms: 1.06x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 16.5 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 220 ms: 1.07x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.53 ms: 1.07x slower                                                          |
| async_generators           | 266 ms                                                              | 285 ms: 1.07x slower                                                           |
| asyncio_tcp                | 662 ms                                                              | 711 ms: 1.07x slower                                                           |
| chaos                      | 48.0 ms                                                             | 51.5 ms: 1.07x slower                                                          |
| chameleon                  | 5.71 ms                                                             | 6.16 ms: 1.08x slower                                                          |
| deepcopy                   | 280 us                                                              | 302 us: 1.08x slower                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 75.1 ms: 1.08x slower                                                          |
| generators                 | 21.2 ms                                                             | 23.2 ms: 1.10x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.4 ms: 1.10x slower                                                          |
| raytrace                   | 189 ms                                                              | 208 ms: 1.10x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.2 ms: 1.10x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 89.6 ms: 1.11x slower                                                          |
| pylint                     | 217 ms                                                              | 240 ms: 1.11x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 20.5 ms: 1.13x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.53 ms: 1.13x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 52.3 ms: 1.18x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 76.0 ms: 1.28x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.05x faster                                                                   |

Benchmark hidden because not significant (15): pickle_list, create_gc_cycles, pyflate, regex_dna, async_tree_none, flaskblogging, richards, html5lib, xml_etree_parse, bench_thread_pool, gc_traversal, asyncio_tcp_ssl, async_tree_io, async_tree_memoization, async_tree_none_tg

# HPT report

- Reliability score: 93.07% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown