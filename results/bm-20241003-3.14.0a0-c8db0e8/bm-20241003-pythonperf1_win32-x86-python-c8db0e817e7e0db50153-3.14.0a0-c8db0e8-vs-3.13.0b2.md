# Results vs. 3.13.0b2

- fork: python
- ref: c8db0e817e7e0db50153
- machine: windows-x86
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 46.2 ms: 1.02x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| Geometric mean | (ref)                                                               | 1.06x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                           |
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 491 ms: 1.04x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 475 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x slower                                                                   |

Benchmark hidden because not significant (4): async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| float          | 52.4 ms                                                             | 61.7 ms: 1.18x slower                                                          |
| nbody          | 76.9 ms                                                             | 91.6 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_dna      | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| regex_v8       | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 110 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.41 us: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| pickle               | 8.07 us                                                             | 8.18 us: 1.01x slower                                                          |
| unpickle_list        | 2.93 us                                                             | 3.00 us: 1.03x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 108 ms: 1.03x slower                                                           |
| json_loads           | 20.5 us                                                             | 21.3 us: 1.04x slower                                                          |
| xml_etree_iterparse  | 64.2 ms                                                             | 68.0 ms: 1.06x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.4 us: 1.07x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.54 ms: 1.10x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.92 sec: 1.16x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 50.7 ms: 1.21x slower                                                          |
| unpickle_pure_python | 147 us                                                              | 183 us: 1.24x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 268 us: 1.26x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.09x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.7 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.6 ms: 1.12x slower                                                          |
| django_template | 30.1 ms                                                             | 34.3 ms: 1.14x slower                                                          |
| mako            | 6.94 ms                                                             | 8.12 ms: 1.17x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.13x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 769 us: 12.65x faster                                                          |
| coverage                   | 307 ms                                                              | 53.6 ms: 5.73x faster                                                          |
| deepcopy                   | 280 us                                                              | 247 us: 1.13x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.41 us: 1.04x faster                                                          |
| async_tree_none            | 228 ms                                                              | 220 ms: 1.04x faster                                                           |
| create_gc_cycles           | 756 us                                                              | 732 us: 1.03x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 22.9 us: 1.03x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.7 us: 1.00x faster                                                          |
| pidigits                   | 199 ms                                                              | 200 ms: 1.01x slower                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.98 us: 1.01x slower                                                          |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| pickle                     | 8.07 us                                                             | 8.18 us: 1.01x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 46.2 ms: 1.02x slower                                                          |
| regex_effbot               | 1.88 ms                                                             | 1.92 ms: 1.02x slower                                                          |
| regex_dna                  | 118 ms                                                              | 120 ms: 1.02x slower                                                           |
| unpickle_list              | 2.93 us                                                             | 3.00 us: 1.03x slower                                                          |
| sympy_expand               | 375 ms                                                              | 385 ms: 1.03x slower                                                           |
| async_tree_io              | 530 ms                                                              | 545 ms: 1.03x slower                                                           |
| sympy_sum                  | 105 ms                                                              | 108 ms: 1.03x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.01 ms: 1.03x slower                                                          |
| regex_v8                   | 15.7 ms                                                             | 16.2 ms: 1.03x slower                                                          |
| xml_etree_parse            | 104 ms                                                              | 108 ms: 1.03x slower                                                           |
| sympy_str                  | 211 ms                                                              | 218 ms: 1.03x slower                                                           |
| pathlib                    | 83.9 ms                                                             | 86.5 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| json_loads                 | 20.5 us                                                             | 21.3 us: 1.04x slower                                                          |
| crypto_pyaes               | 55.8 ms                                                             | 57.8 ms: 1.04x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 491 ms: 1.04x slower                                                           |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 72.9 ms: 1.05x slower                                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 68.0 ms: 1.06x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 475 ms: 1.06x slower                                                           |
| unpickle                   | 9.79 us                                                             | 10.4 us: 1.07x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.7 ms: 1.07x slower                                                          |
| 2to3                       | 233 ms                                                              | 250 ms: 1.07x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.48 ms: 1.08x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 79.8 ms: 1.08x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.7 ms: 1.08x slower                                                          |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.11 ms: 1.08x slower                                                          |
| pylint                     | 217 ms                                                              | 236 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 148 us: 1.09x slower                                                           |
| go                         | 101 ms                                                              | 110 ms: 1.09x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 75.1 ms: 1.09x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.18 us: 1.09x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.92 us: 1.10x slower                                                          |
| genshi_xml                 | 44.3 ms                                                             | 48.7 ms: 1.10x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.54 ms: 1.10x slower                                                          |
| regex_compile              | 99.9 ms                                                             | 110 ms: 1.10x slower                                                           |
| mdp                        | 1.60 sec                                                            | 1.77 sec: 1.11x slower                                                         |
| pycparser                  | 777 ms                                                              | 861 ms: 1.11x slower                                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.32 ms: 1.11x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.07 ms: 1.11x slower                                                          |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.11x slower                                                           |
| pprint_safe_repr           | 607 ms                                                              | 680 ms: 1.12x slower                                                           |
| genshi_text                | 20.1 ms                                                             | 22.6 ms: 1.12x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.40 sec: 1.13x slower                                                         |
| async_generators           | 266 ms                                                              | 302 ms: 1.14x slower                                                           |
| django_template            | 30.1 ms                                                             | 34.3 ms: 1.14x slower                                                          |
| sqlglot_optimize           | 39.7 ms                                                             | 45.5 ms: 1.14x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 236 ms: 1.15x slower                                                           |
| spectral_norm              | 68.0 ms                                                             | 78.5 ms: 1.16x slower                                                          |
| fannkuch                   | 270 ms                                                              | 313 ms: 1.16x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 69.1 ms: 1.16x slower                                                          |
| tomli_loads                | 1.65 sec                                                            | 1.92 sec: 1.16x slower                                                         |
| scimark_lu                 | 59.4 ms                                                             | 69.2 ms: 1.17x slower                                                          |
| mako                       | 6.94 ms                                                             | 8.12 ms: 1.17x slower                                                          |
| chaos                      | 48.0 ms                                                             | 56.2 ms: 1.17x slower                                                          |
| scimark_fft                | 198 ms                                                              | 233 ms: 1.18x slower                                                           |
| float                      | 52.4 ms                                                             | 61.7 ms: 1.18x slower                                                          |
| comprehensions             | 11.9 us                                                             | 14.0 us: 1.18x slower                                                          |
| nbody                      | 76.9 ms                                                             | 91.6 ms: 1.19x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.5 ms: 1.20x slower                                                          |
| pyflate                    | 308 ms                                                              | 370 ms: 1.20x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 50.7 ms: 1.21x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 99.0 ms: 1.22x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.3 ms: 1.22x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.23 ms: 1.24x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 183 us: 1.24x slower                                                           |
| pickle_pure_python         | 213 us                                                              | 268 us: 1.26x slower                                                           |
| deltablue                  | 2.23 ms                                                             | 2.82 ms: 1.26x slower                                                          |
| generators                 | 21.2 ms                                                             | 26.7 ms: 1.26x slower                                                          |
| logging_silent             | 57.9 ns                                                             | 74.7 ns: 1.29x slower                                                          |
| richards_super             | 35.5 ms                                                             | 46.2 ms: 1.30x slower                                                          |
| richards                   | 31.2 ms                                                             | 41.4 ms: 1.32x slower                                                          |
| raytrace                   | 189 ms                                                              | 260 ms: 1.38x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.04x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_io_tg, gc_traversal, async_tree_none_tg, deepcopy_reduce, async_tree_memoization, asyncio_tcp, async_tree_memoization_tg
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf1_win32-x86-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x

# Memory
- memory change: unknown