# Results vs. 3.13.0b2

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.01x faster
- HPT reliability: 93.36%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 244 ms: 1.05x slower                                                            |
| chameleon      | 5.71 ms                                                             | 5.95 ms: 1.04x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                          |
| html5lib       | 45.4 ms                                                             | 45.2 ms: 1.00x faster                                                           |
| tornado_http   | 94.3 ms                                                             | 97.4 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none           | 228 ms                                                              | 230 ms: 1.01x slower                                                            |
| async_tree_io_tg          | 529 ms                                                              | 538 ms: 1.02x slower                                                            |
| async_tree_cpu_io_mixed   | 471 ms                                                              | 479 ms: 1.02x slower                                                            |
| async_tree_memoization    | 275 ms                                                              | 281 ms: 1.02x slower                                                            |
| async_tree_memoization_tg | 254 ms                                                              | 260 ms: 1.03x slower                                                            |
| Geometric mean            | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 53.7 ms: 1.43x faster                                                           |
| float          | 52.4 ms                                                             | 41.3 ms: 1.27x faster                                                           |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                               | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 99.9 ms                                                             | 92.7 ms: 1.08x faster                                                           |
| regex_dna      | 118 ms                                                              | 117 ms: 1.01x faster                                                            |
| regex_effbot   | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.65 sec                                                            | 1.38 sec: 1.19x faster                                                          |
| unpickle_pure_python | 147 us                                                              | 136 us: 1.09x faster                                                            |
| pickle_pure_python   | 213 us                                                              | 198 us: 1.08x faster                                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 60.0 ms: 1.07x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 56.0 ms: 1.07x faster                                                           |
| xml_etree_process    | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                                           |
| json_dumps           | 6.84 ms                                                             | 6.69 ms: 1.02x faster                                                           |
| xml_etree_parse      | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| unpickle_list        | 2.93 us                                                             | 2.89 us: 1.01x faster                                                           |
| json_loads           | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| pickle               | 8.07 us                                                             | 8.21 us: 1.02x slower                                                           |
| pickle_list          | 3.57 us                                                             | 3.64 us: 1.02x slower                                                           |
| unpickle             | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 25.2 ms: 1.13x slower                                                           |
| python_startup_no_site | 18.2 ms                                                             | 21.3 ms: 1.17x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.15x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 6.94 ms                                                             | 5.31 ms: 1.31x faster                                                           |
| genshi_text     | 20.1 ms                                                             | 21.0 ms: 1.05x slower                                                           |
| django_template | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                           |
| genshi_xml      | 44.3 ms                                                             | 50.9 ms: 1.15x slower                                                           |
| Geometric mean  | (ref)                                                               | 1.00x faster                                                                    |

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|---------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                     | 76.9 ms                                                             | 53.7 ms: 1.43x faster                                                           |
| spectral_norm             | 68.0 ms                                                             | 47.9 ms: 1.42x faster                                                           |
| mako                      | 6.94 ms                                                             | 5.31 ms: 1.31x faster                                                           |
| float                     | 52.4 ms                                                             | 41.3 ms: 1.27x faster                                                           |
| fannkuch                  | 270 ms                                                              | 219 ms: 1.23x faster                                                            |
| scimark_sparse_mat_mult   | 2.87 ms                                                             | 2.38 ms: 1.21x faster                                                           |
| tomli_loads               | 1.65 sec                                                            | 1.38 sec: 1.19x faster                                                          |
| deepcopy_memo             | 23.5 us                                                             | 20.2 us: 1.17x faster                                                           |
| crypto_pyaes              | 55.8 ms                                                             | 49.2 ms: 1.13x faster                                                           |
| scimark_monte_carlo       | 45.2 ms                                                             | 39.9 ms: 1.13x faster                                                           |
| scimark_fft               | 198 ms                                                              | 176 ms: 1.13x faster                                                            |
| pprint_safe_repr          | 607 ms                                                              | 555 ms: 1.09x faster                                                            |
| sqlglot_parse             | 964 us                                                              | 887 us: 1.09x faster                                                            |
| unpickle_pure_python      | 147 us                                                              | 136 us: 1.09x faster                                                            |
| pprint_pformat            | 1.24 sec                                                            | 1.15 sec: 1.08x faster                                                          |
| pickle_pure_python        | 213 us                                                              | 198 us: 1.08x faster                                                            |
| regex_compile             | 99.9 ms                                                             | 92.7 ms: 1.08x faster                                                           |
| comprehensions            | 11.9 us                                                             | 11.1 us: 1.07x faster                                                           |
| xml_etree_iterparse       | 64.2 ms                                                             | 60.0 ms: 1.07x faster                                                           |
| xml_etree_generate        | 59.6 ms                                                             | 56.0 ms: 1.07x faster                                                           |
| logging_silent            | 57.9 ns                                                             | 54.6 ns: 1.06x faster                                                           |
| telco                     | 6.03 ms                                                             | 5.76 ms: 1.05x faster                                                           |
| sqlglot_transpile         | 1.19 ms                                                             | 1.14 ms: 1.04x faster                                                           |
| xml_etree_process         | 42.1 ms                                                             | 40.5 ms: 1.04x faster                                                           |
| meteor_contest            | 74.1 ms                                                             | 71.4 ms: 1.04x faster                                                           |
| richards                  | 31.2 ms                                                             | 30.5 ms: 1.02x faster                                                           |
| json_dumps                | 6.84 ms                                                             | 6.69 ms: 1.02x faster                                                           |
| sqlite_synth              | 1.96 us                                                             | 1.92 us: 1.02x faster                                                           |
| richards_super            | 35.5 ms                                                             | 34.7 ms: 1.02x faster                                                           |
| logging_format            | 8.13 us                                                             | 7.97 us: 1.02x faster                                                           |
| xml_etree_parse           | 104 ms                                                              | 102 ms: 1.02x faster                                                            |
| sympy_expand              | 375 ms                                                              | 370 ms: 1.01x faster                                                            |
| logging_simple            | 7.47 us                                                             | 7.36 us: 1.01x faster                                                           |
| unpickle_list             | 2.93 us                                                             | 2.89 us: 1.01x faster                                                           |
| pidigits                  | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| regex_dna                 | 118 ms                                                              | 117 ms: 1.01x faster                                                            |
| sympy_str                 | 211 ms                                                              | 209 ms: 1.01x faster                                                            |
| html5lib                  | 45.4 ms                                                             | 45.2 ms: 1.00x faster                                                           |
| json_loads                | 20.5 us                                                             | 20.7 us: 1.01x slower                                                           |
| asyncio_tcp_ssl           | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                          |
| async_tree_none           | 228 ms                                                              | 230 ms: 1.01x slower                                                            |
| async_tree_io_tg          | 529 ms                                                              | 538 ms: 1.02x slower                                                            |
| sympy_sum                 | 105 ms                                                              | 107 ms: 1.02x slower                                                            |
| mdp                       | 1.60 sec                                                            | 1.63 sec: 1.02x slower                                                          |
| async_tree_cpu_io_mixed   | 471 ms                                                              | 479 ms: 1.02x slower                                                            |
| pickle                    | 8.07 us                                                             | 8.21 us: 1.02x slower                                                           |
| async_tree_memoization    | 275 ms                                                              | 281 ms: 1.02x slower                                                            |
| coroutines                | 15.5 ms                                                             | 15.8 ms: 1.02x slower                                                           |
| pickle_list               | 3.57 us                                                             | 3.64 us: 1.02x slower                                                           |
| sqlglot_optimize          | 39.7 ms                                                             | 40.7 ms: 1.03x slower                                                           |
| async_tree_memoization_tg | 254 ms                                                              | 260 ms: 1.03x slower                                                            |
| sqlglot_normalize         | 206 ms                                                              | 211 ms: 1.03x slower                                                            |
| nqueens                   | 68.7 ms                                                             | 70.6 ms: 1.03x slower                                                           |
| deepcopy_reduce           | 2.59 us                                                             | 2.66 us: 1.03x slower                                                           |
| regex_effbot              | 1.88 ms                                                             | 1.94 ms: 1.03x slower                                                           |
| docutils                  | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                          |
| tornado_http              | 94.3 ms                                                             | 97.4 ms: 1.03x slower                                                           |
| typing_runtime_protocols  | 136 us                                                              | 140 us: 1.04x slower                                                            |
| pathlib                   | 83.9 ms                                                             | 86.9 ms: 1.04x slower                                                           |
| unpickle                  | 9.79 us                                                             | 10.2 us: 1.04x slower                                                           |
| json                      | 4.10 ms                                                             | 4.25 ms: 1.04x slower                                                           |
| chameleon                 | 5.71 ms                                                             | 5.95 ms: 1.04x slower                                                           |
| genshi_text               | 20.1 ms                                                             | 21.0 ms: 1.05x slower                                                           |
| chaos                     | 48.0 ms                                                             | 50.2 ms: 1.05x slower                                                           |
| 2to3                      | 233 ms                                                              | 244 ms: 1.05x slower                                                            |
| coverage                  | 307 ms                                                              | 325 ms: 1.06x slower                                                            |
| hexiom                    | 4.23 ms                                                             | 4.49 ms: 1.06x slower                                                           |
| sympy_integrate           | 14.6 ms                                                             | 15.6 ms: 1.06x slower                                                           |
| asyncio_tcp               | 662 ms                                                              | 705 ms: 1.07x slower                                                            |
| deepcopy                  | 280 us                                                              | 299 us: 1.07x slower                                                            |
| django_template           | 30.1 ms                                                             | 32.2 ms: 1.07x slower                                                           |
| go                        | 101 ms                                                              | 108 ms: 1.07x slower                                                            |
| thrift                    | 9.73 ms                                                             | 10.6 ms: 1.08x slower                                                           |
| bench_mp_pool             | 69.4 ms                                                             | 75.3 ms: 1.09x slower                                                           |
| scimark_sor               | 81.0 ms                                                             | 88.1 ms: 1.09x slower                                                           |
| pylint                    | 217 ms                                                              | 238 ms: 1.10x slower                                                            |
| generators                | 21.2 ms                                                             | 23.3 ms: 1.10x slower                                                           |
| raytrace                  | 189 ms                                                              | 208 ms: 1.10x slower                                                            |
| async_generators          | 266 ms                                                              | 297 ms: 1.12x slower                                                            |
| deltablue                 | 2.23 ms                                                             | 2.51 ms: 1.12x slower                                                           |
| python_startup            | 22.2 ms                                                             | 25.2 ms: 1.13x slower                                                           |
| genshi_xml                | 44.3 ms                                                             | 50.9 ms: 1.15x slower                                                           |
| python_startup_no_site    | 18.2 ms                                                             | 21.3 ms: 1.17x slower                                                           |
| scimark_lu                | 59.4 ms                                                             | 74.7 ms: 1.26x slower                                                           |
| Geometric mean            | (ref)                                                               | 1.01x faster                                                                    |

Benchmark hidden because not significant (11): pyflate, gc_traversal, create_gc_cycles, flaskblogging, pycparser, async_tree_io, regex_v8, pickle_dict, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_none_tg

# HPT report

- Reliability score: 93.36% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown