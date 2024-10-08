# Results vs. 3.13.0b2

- fork: python
- ref: e256a7590a0149feadfe
- machine: windows-x86
- commit hash: e256a75
- commit date: 2024-09-24
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| float          | 52.4 ms                                                             | 62.8 ms: 1.20x slower                                                          |
| nbody          | 76.9 ms                                                             | 93.0 ms: 1.21x slower                                                          |
| Geometric mean | (ref)                                                               | 1.13x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| regex_dna      | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 109 ms: 1.09x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.35 us: 1.06x faster                                                          |
| pickle               | 8.07 us                                                             | 7.94 us: 1.02x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 67.5 ms: 1.05x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.68 ms: 1.12x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                         |
| xml_etree_generate   | 59.6 ms                                                             | 67.5 ms: 1.13x slower                                                          |
| xml_etree_process    | 42.1 ms                                                             | 49.4 ms: 1.17x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 180 us: 1.23x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 262 us: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.07x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.5 ms: 1.06x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.4 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 50.3 ms: 1.14x slower                                                          |
| mako            | 6.94 ms                                                             | 8.16 ms: 1.17x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 24.2 ms: 1.20x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.16x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 746 us: 13.04x faster                                                          |
| coverage                   | 307 ms                                                              | 53.2 ms: 5.78x faster                                                          |
| deepcopy                   | 280 us                                                              | 250 us: 1.12x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.35 us: 1.06x faster                                                          |
| async_tree_none            | 228 ms                                                              | 218 ms: 1.04x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 727 us: 1.04x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.6 us: 1.04x faster                                                          |
| deepcopy_reduce            | 2.59 us                                                             | 2.50 us: 1.03x faster                                                          |
| async_tree_io_tg           | 529 ms                                                              | 518 ms: 1.02x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.94 us: 1.02x faster                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 464 ms: 1.02x faster                                                           |
| gc_traversal               | 1.43 ms                                                             | 1.42 ms: 1.01x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.6 us: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| bench_mp_pool              | 69.4 ms                                                             | 69.9 ms: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.0 sec: 1.01x slower                                                         |
| sqlite_synth               | 1.96 us                                                             | 1.98 us: 1.01x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.90 ms: 1.01x slower                                                          |
| sympy_expand               | 375 ms                                                              | 381 ms: 1.02x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 455 ms: 1.02x slower                                                           |
| json_loads                 | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 107 ms: 1.02x slower                                                           |
| regex_dna                  | 118 ms                                                              | 121 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 216 ms: 1.02x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 57.2 ms: 1.02x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.5 ms: 1.02x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 3.00 us: 1.02x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.03x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| mdp                        | 1.60 sec                                                            | 1.66 sec: 1.03x slower                                                         |
| sympy_integrate            | 14.6 ms                                                             | 15.3 ms: 1.05x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 67.5 ms: 1.05x slower                                                          |
| json                       | 4.10 ms                                                             | 4.32 ms: 1.05x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 143 us: 1.06x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.5 ms: 1.06x slower                                                          |
| logging_simple             | 7.47 us                                                             | 7.93 us: 1.06x slower                                                          |
| go                         | 101 ms                                                              | 107 ms: 1.06x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.66 us: 1.06x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.06 ms: 1.07x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.4 ms: 1.07x slower                                                          |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                           |
| 2to3                       | 233 ms                                                              | 249 ms: 1.07x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 109 ms: 1.09x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.61 ms: 1.10x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 81.4 ms: 1.10x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.9 ms: 1.12x slower                                                          |
| django_template            | 30.1 ms                                                             | 33.6 ms: 1.12x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.68 ms: 1.12x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 44.6 ms: 1.12x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.85 sec: 1.12x slower                                                         |
| nqueens                    | 68.7 ms                                                             | 77.3 ms: 1.13x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 684 ms: 1.13x slower                                                           |
| pprint_pformat             | 1.24 sec                                                            | 1.40 sec: 1.13x slower                                                         |
| pycparser                  | 777 ms                                                              | 877 ms: 1.13x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 233 ms: 1.13x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.35 ms: 1.13x slower                                                          |
| chaos                      | 48.0 ms                                                             | 54.3 ms: 1.13x slower                                                          |
| async_generators           | 266 ms                                                              | 301 ms: 1.13x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 67.5 ms: 1.13x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 50.3 ms: 1.14x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.10 ms: 1.14x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 68.7 ms: 1.16x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.0 ms: 1.16x slower                                                          |
| pyflate                    | 308 ms                                                              | 362 ms: 1.17x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 49.4 ms: 1.17x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.16 ms: 1.17x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.1 us: 1.19x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.67 ms: 1.20x slower                                                          |
| float                      | 52.4 ms                                                             | 62.8 ms: 1.20x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 24.2 ms: 1.20x slower                                                          |
| scimark_fft                | 198 ms                                                              | 239 ms: 1.21x slower                                                           |
| nbody                      | 76.9 ms                                                             | 93.0 ms: 1.21x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.17 ms: 1.22x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 180 us: 1.23x slower                                                           |
| generators                 | 21.2 ms                                                             | 26.0 ms: 1.23x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 262 us: 1.23x slower                                                           |
| raytrace                   | 189 ms                                                              | 233 ms: 1.23x slower                                                           |
| fannkuch                   | 270 ms                                                              | 336 ms: 1.24x slower                                                           |
| richards_super             | 35.5 ms                                                             | 44.3 ms: 1.25x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 56.9 ms: 1.26x slower                                                          |
| richards                   | 31.2 ms                                                             | 39.4 ms: 1.26x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 74.6 ns: 1.29x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 105 ms: 1.29x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, pathlib, async_tree_memoization_tg, asyncio_tcp, tornado_http, async_tree_io, bench_thread_pool
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240924-3.14.0a0-e256a75/bm-20240924-pythonperf1_win32-x86-python-e256a7590a0149feadfe-3.14.0a0-e256a75.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown