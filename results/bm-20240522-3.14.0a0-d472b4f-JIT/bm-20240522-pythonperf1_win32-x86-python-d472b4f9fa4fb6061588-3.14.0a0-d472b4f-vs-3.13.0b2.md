# Results vs. 3.13.0b2

- fork: python
- ref: d472b4f9fa4fb6061588
- machine: windows-x86
- commit hash: d472b4f
- commit date: 2024-05-22
- overall geometric mean: 1.06x faster
- HPT reliability: 68.79%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| chameleon      | 5.71 ms                                                             | 6.12 ms: 1.07x slower                                                          |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 45.0 ms: 1.01x faster                                                          |
| tornado_http   | 94.3 ms                                                             | 96.8 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization    | 275 ms                                                              | 280 ms: 1.02x slower                                                           |
| async_tree_io_tg          | 529 ms                                                              | 539 ms: 1.02x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 261 ms: 1.03x slower                                                           |
| Geometric mean            | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (5): async_tree_none, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 52.1 ms: 1.47x faster                                                          |
| float          | 52.4 ms                                                             | 41.5 ms: 1.26x faster                                                          |
| pidigits       | 199 ms                                                              | 194 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                               | 1.24x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 96.8 ms: 1.03x faster                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| regex_effbot   | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.38 sec: 1.19x faster                                                         |
| pickle_pure_python   | 213 us                                                              | 196 us: 1.08x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 55.3 ms: 1.08x faster                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 60.0 ms: 1.07x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 138 us: 1.07x faster                                                           |
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                           |
| xml_etree_process    | 42.1 ms                                                             | 41.2 ms: 1.02x faster                                                          |
| json_dumps           | 6.84 ms                                                             | 6.74 ms: 1.01x faster                                                          |
| pickle_list          | 3.57 us                                                             | 3.53 us: 1.01x faster                                                          |
| json_loads           | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.06 us: 1.04x slower                                                          |
| pickle               | 8.07 us                                                             | 8.51 us: 1.05x slower                                                          |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.10x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.25 ms: 1.32x faster                                                          |
| django_template | 30.1 ms                                                             | 31.2 ms: 1.04x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 21.6 ms: 1.07x slower                                                          |
| genshi_xml      | 44.3 ms                                                             | 51.1 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.01x faster                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240522-pythonperf1_win32-x86-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f |
|---------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 9.73 ms                                                             | 705 us: 13.80x faster                                                          |
| coverage                  | 307 ms                                                              | 50.2 ms: 6.12x faster                                                          |
| nbody                     | 76.9 ms                                                             | 52.1 ms: 1.47x faster                                                          |
| spectral_norm             | 68.0 ms                                                             | 47.3 ms: 1.44x faster                                                          |
| mako                      | 6.94 ms                                                             | 5.25 ms: 1.32x faster                                                          |
| float                     | 52.4 ms                                                             | 41.5 ms: 1.26x faster                                                          |
| scimark_sparse_mat_mult   | 2.87 ms                                                             | 2.34 ms: 1.23x faster                                                          |
| fannkuch                  | 270 ms                                                              | 224 ms: 1.21x faster                                                           |
| tomli_loads               | 1.65 sec                                                            | 1.38 sec: 1.19x faster                                                         |
| scimark_fft               | 198 ms                                                              | 171 ms: 1.16x faster                                                           |
| crypto_pyaes              | 55.8 ms                                                             | 48.5 ms: 1.15x faster                                                          |
| deepcopy_memo             | 23.5 us                                                             | 20.5 us: 1.15x faster                                                          |
| telco                     | 6.03 ms                                                             | 5.45 ms: 1.11x faster                                                          |
| asyncio_tcp               | 662 ms                                                              | 599 ms: 1.11x faster                                                           |
| pprint_safe_repr          | 607 ms                                                              | 551 ms: 1.10x faster                                                           |
| pprint_pformat            | 1.24 sec                                                            | 1.14 sec: 1.09x faster                                                         |
| scimark_monte_carlo       | 45.2 ms                                                             | 41.6 ms: 1.09x faster                                                          |
| pickle_pure_python        | 213 us                                                              | 196 us: 1.08x faster                                                           |
| sqlglot_parse             | 964 us                                                              | 891 us: 1.08x faster                                                           |
| xml_etree_generate        | 59.6 ms                                                             | 55.3 ms: 1.08x faster                                                          |
| xml_etree_iterparse       | 64.2 ms                                                             | 60.0 ms: 1.07x faster                                                          |
| unpickle_pure_python      | 147 us                                                              | 138 us: 1.07x faster                                                           |
| logging_silent            | 57.9 ns                                                             | 54.8 ns: 1.06x faster                                                          |
| comprehensions            | 11.9 us                                                             | 11.2 us: 1.06x faster                                                          |
| pyflate                   | 308 ms                                                              | 292 ms: 1.05x faster                                                           |
| sqlite_synth              | 1.96 us                                                             | 1.88 us: 1.04x faster                                                          |
| sqlglot_transpile         | 1.19 ms                                                             | 1.15 ms: 1.04x faster                                                          |
| regex_compile             | 99.9 ms                                                             | 96.8 ms: 1.03x faster                                                          |
| meteor_contest            | 74.1 ms                                                             | 72.2 ms: 1.03x faster                                                          |
| pidigits                  | 199 ms                                                              | 194 ms: 1.02x faster                                                           |
| xml_etree_parse           | 104 ms                                                              | 102 ms: 1.02x faster                                                           |
| xml_etree_process         | 42.1 ms                                                             | 41.2 ms: 1.02x faster                                                          |
| json_dumps                | 6.84 ms                                                             | 6.74 ms: 1.01x faster                                                          |
| sympy_str                 | 211 ms                                                              | 209 ms: 1.01x faster                                                           |
| html5lib                  | 45.4 ms                                                             | 45.0 ms: 1.01x faster                                                          |
| richards                  | 31.2 ms                                                             | 30.9 ms: 1.01x faster                                                          |
| create_gc_cycles          | 756 us                                                              | 749 us: 1.01x faster                                                           |
| pickle_list               | 3.57 us                                                             | 3.53 us: 1.01x faster                                                          |
| logging_format            | 8.13 us                                                             | 8.09 us: 1.01x faster                                                          |
| logging_simple            | 7.47 us                                                             | 7.44 us: 1.00x faster                                                          |
| mdp                       | 1.60 sec                                                            | 1.60 sec: 1.00x faster                                                         |
| regex_dna                 | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| async_tree_memoization    | 275 ms                                                              | 280 ms: 1.02x slower                                                           |
| regex_v8                  | 15.7 ms                                                             | 16.0 ms: 1.02x slower                                                          |
| async_tree_io_tg          | 529 ms                                                              | 539 ms: 1.02x slower                                                           |
| pycparser                 | 777 ms                                                              | 794 ms: 1.02x slower                                                           |
| json_loads                | 20.5 us                                                             | 21.0 us: 1.02x slower                                                          |
| pathlib                   | 83.9 ms                                                             | 85.8 ms: 1.02x slower                                                          |
| gc_traversal              | 1.43 ms                                                             | 1.47 ms: 1.02x slower                                                          |
| tornado_http              | 94.3 ms                                                             | 96.8 ms: 1.03x slower                                                          |
| async_tree_memoization_tg | 254 ms                                                              | 261 ms: 1.03x slower                                                           |
| regex_effbot              | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                          |
| docutils                  | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| nqueens                   | 68.7 ms                                                             | 71.0 ms: 1.03x slower                                                          |
| django_template           | 30.1 ms                                                             | 31.2 ms: 1.04x slower                                                          |
| deepcopy_reduce           | 2.59 us                                                             | 2.69 us: 1.04x slower                                                          |
| unpickle                  | 9.79 us                                                             | 10.2 us: 1.04x slower                                                          |
| unpickle_list             | 2.93 us                                                             | 3.06 us: 1.04x slower                                                          |
| hexiom                    | 4.23 ms                                                             | 4.43 ms: 1.05x slower                                                          |
| pickle                    | 8.07 us                                                             | 8.51 us: 1.05x slower                                                          |
| sympy_integrate           | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| sqlglot_optimize          | 39.7 ms                                                             | 42.0 ms: 1.06x slower                                                          |
| 2to3                      | 233 ms                                                              | 248 ms: 1.06x slower                                                           |
| deepcopy                  | 280 us                                                              | 298 us: 1.06x slower                                                           |
| json                      | 4.10 ms                                                             | 4.37 ms: 1.07x slower                                                          |
| coroutines                | 15.5 ms                                                             | 16.5 ms: 1.07x slower                                                          |
| sqlglot_normalize         | 206 ms                                                              | 220 ms: 1.07x slower                                                           |
| chameleon                 | 5.71 ms                                                             | 6.12 ms: 1.07x slower                                                          |
| genshi_text               | 20.1 ms                                                             | 21.6 ms: 1.07x slower                                                          |
| bench_mp_pool             | 69.4 ms                                                             | 74.9 ms: 1.08x slower                                                          |
| chaos                     | 48.0 ms                                                             | 52.0 ms: 1.08x slower                                                          |
| typing_runtime_protocols  | 136 us                                                              | 147 us: 1.08x slower                                                           |
| python_startup            | 22.2 ms                                                             | 24.2 ms: 1.09x slower                                                          |
| async_generators          | 266 ms                                                              | 292 ms: 1.10x slower                                                           |
| pylint                    | 217 ms                                                              | 239 ms: 1.10x slower                                                           |
| raytrace                  | 189 ms                                                              | 208 ms: 1.10x slower                                                           |
| go                        | 101 ms                                                              | 111 ms: 1.10x slower                                                           |
| scimark_sor               | 81.0 ms                                                             | 89.5 ms: 1.11x slower                                                          |
| generators                | 21.2 ms                                                             | 23.6 ms: 1.12x slower                                                          |
| python_startup_no_site    | 18.2 ms                                                             | 20.4 ms: 1.12x slower                                                          |
| deltablue                 | 2.23 ms                                                             | 2.54 ms: 1.14x slower                                                          |
| genshi_xml                | 44.3 ms                                                             | 51.1 ms: 1.15x slower                                                          |
| scimark_lu                | 59.4 ms                                                             | 70.5 ms: 1.19x slower                                                          |
| Geometric mean            | (ref)                                                               | 1.06x faster                                                                   |

Benchmark hidden because not significant (12): richards_super, sympy_expand, flaskblogging, async_tree_none, pickle_dict, bench_thread_pool, sympy_sum, async_tree_cpu_io_mixed, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io

# HPT report

- Reliability score: 68.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown