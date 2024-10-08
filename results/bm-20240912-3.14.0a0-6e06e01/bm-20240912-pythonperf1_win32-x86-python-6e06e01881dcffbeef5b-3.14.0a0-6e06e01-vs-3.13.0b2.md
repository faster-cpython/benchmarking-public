# Results vs. 3.13.0b2

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: windows-x86
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 248 ms: 1.07x slower                                                           |
| docutils       | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| html5lib       | 45.4 ms                                                             | 48.1 ms: 1.06x slower                                                          |
| tornado_http   | 94.3 ms                                                             | 95.1 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                               | 1.04x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| Geometric mean             | (ref)                                                               | 1.01x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_memoization_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| nbody          | 76.9 ms                                                             | 91.3 ms: 1.19x slower                                                          |
| float          | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| Geometric mean | (ref)                                                               | 1.12x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| regex_compile  | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                   |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.42 us: 1.04x faster                                                          |
| pickle               | 8.07 us                                                             | 7.77 us: 1.04x faster                                                          |
| pickle_dict          | 20.8 us                                                             | 20.3 us: 1.02x faster                                                          |
| unpickle_list        | 2.93 us                                                             | 2.96 us: 1.01x slower                                                          |
| json_loads           | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| xml_etree_parse      | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 66.8 ms: 1.04x slower                                                          |
| unpickle             | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.69 ms: 1.12x slower                                                          |
| xml_etree_generate   | 59.6 ms                                                             | 68.3 ms: 1.15x slower                                                          |
| tomli_loads          | 1.65 sec                                                            | 1.93 sec: 1.17x slower                                                         |
| xml_etree_process    | 42.1 ms                                                             | 50.7 ms: 1.20x slower                                                          |
| pickle_pure_python   | 213 us                                                              | 257 us: 1.21x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 181 us: 1.23x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| python_startup_no_site | 18.2 ms                                                             | 19.8 ms: 1.09x slower                                                          |
| Geometric mean         | (ref)                                                               | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 44.3 ms                                                             | 48.7 ms: 1.10x slower                                                          |
| genshi_text     | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| django_template | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                          |
| mako            | 6.94 ms                                                             | 7.99 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                               | 1.12x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 9.73 ms                                                             | 742 us: 13.11x faster                                                          |
| coverage                   | 307 ms                                                              | 52.7 ms: 5.83x faster                                                          |
| deepcopy                   | 280 us                                                              | 250 us: 1.12x faster                                                           |
| deepcopy_memo              | 23.5 us                                                             | 21.9 us: 1.07x faster                                                          |
| async_tree_none            | 228 ms                                                              | 217 ms: 1.05x faster                                                           |
| pickle_list                | 3.57 us                                                             | 3.42 us: 1.04x faster                                                          |
| pickle                     | 8.07 us                                                             | 7.77 us: 1.04x faster                                                          |
| create_gc_cycles           | 756 us                                                              | 733 us: 1.03x faster                                                           |
| async_tree_io_tg           | 529 ms                                                              | 515 ms: 1.03x faster                                                           |
| pickle_dict                | 20.8 us                                                             | 20.3 us: 1.02x faster                                                          |
| gc_traversal               | 1.43 ms                                                             | 1.41 ms: 1.02x faster                                                          |
| sqlite_synth               | 1.96 us                                                             | 1.93 us: 1.02x faster                                                          |
| async_tree_memoization     | 275 ms                                                              | 271 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 466 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                              | 197 ms: 1.01x faster                                                           |
| pathlib                    | 83.9 ms                                                             | 83.3 ms: 1.01x faster                                                          |
| tornado_http               | 94.3 ms                                                             | 95.1 ms: 1.01x slower                                                          |
| unpickle_list              | 2.93 us                                                             | 2.96 us: 1.01x slower                                                          |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.01x slower                                                         |
| json_loads                 | 20.5 us                                                             | 20.8 us: 1.01x slower                                                          |
| typing_runtime_protocols   | 136 us                                                              | 137 us: 1.01x slower                                                           |
| sympy_expand               | 375 ms                                                              | 383 ms: 1.02x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 107 ms: 1.02x slower                                                           |
| sympy_str                  | 211 ms                                                              | 216 ms: 1.02x slower                                                           |
| regex_v8                   | 15.7 ms                                                             | 16.1 ms: 1.02x slower                                                          |
| go                         | 101 ms                                                              | 103 ms: 1.03x slower                                                           |
| crypto_pyaes               | 55.8 ms                                                             | 57.3 ms: 1.03x slower                                                          |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 461 ms: 1.03x slower                                                           |
| bench_thread_pool          | 985 us                                                              | 1.02 ms: 1.03x slower                                                          |
| bench_mp_pool              | 69.4 ms                                                             | 71.5 ms: 1.03x slower                                                          |
| docutils                   | 1.81 sec                                                            | 1.87 sec: 1.03x slower                                                         |
| xml_etree_iterparse        | 64.2 ms                                                             | 66.8 ms: 1.04x slower                                                          |
| json                       | 4.10 ms                                                             | 4.28 ms: 1.04x slower                                                          |
| unpickle                   | 9.79 us                                                             | 10.3 us: 1.05x slower                                                          |
| telco                      | 6.03 ms                                                             | 6.37 ms: 1.06x slower                                                          |
| sympy_integrate            | 14.6 ms                                                             | 15.5 ms: 1.06x slower                                                          |
| html5lib                   | 45.4 ms                                                             | 48.1 ms: 1.06x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.70 sec: 1.06x slower                                                         |
| 2to3                       | 233 ms                                                              | 248 ms: 1.07x slower                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.07 ms: 1.07x slower                                                          |
| logging_format             | 8.13 us                                                             | 8.71 us: 1.07x slower                                                          |
| logging_simple             | 7.47 us                                                             | 8.00 us: 1.07x slower                                                          |
| pylint                     | 217 ms                                                              | 232 ms: 1.07x slower                                                           |
| python_startup             | 22.2 ms                                                             | 23.8 ms: 1.07x slower                                                          |
| meteor_contest             | 74.1 ms                                                             | 79.8 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 206 ms                                                              | 223 ms: 1.08x slower                                                           |
| regex_compile              | 99.9 ms                                                             | 108 ms: 1.08x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 43.0 ms: 1.08x slower                                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.8 ms: 1.09x slower                                                          |
| nqueens                    | 68.7 ms                                                             | 74.9 ms: 1.09x slower                                                          |
| sqlglot_parse              | 964 us                                                              | 1.05 ms: 1.09x slower                                                          |
| sqlglot_transpile          | 1.19 ms                                                             | 1.30 ms: 1.09x slower                                                          |
| pprint_safe_repr           | 607 ms                                                              | 665 ms: 1.10x slower                                                           |
| genshi_xml                 | 44.3 ms                                                             | 48.7 ms: 1.10x slower                                                          |
| spectral_norm              | 68.0 ms                                                             | 75.2 ms: 1.11x slower                                                          |
| genshi_text                | 20.1 ms                                                             | 22.3 ms: 1.11x slower                                                          |
| chaos                      | 48.0 ms                                                             | 53.4 ms: 1.11x slower                                                          |
| pprint_pformat             | 1.24 sec                                                            | 1.39 sec: 1.12x slower                                                         |
| django_template            | 30.1 ms                                                             | 33.7 ms: 1.12x slower                                                          |
| json_dumps                 | 6.84 ms                                                             | 7.69 ms: 1.12x slower                                                          |
| async_generators           | 266 ms                                                              | 300 ms: 1.13x slower                                                           |
| pycparser                  | 777 ms                                                              | 884 ms: 1.14x slower                                                           |
| pyflate                    | 308 ms                                                              | 352 ms: 1.14x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 68.3 ms: 1.15x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 68.1 ms: 1.15x slower                                                          |
| mako                       | 6.94 ms                                                             | 7.99 ms: 1.15x slower                                                          |
| coroutines                 | 15.5 ms                                                             | 18.0 ms: 1.16x slower                                                          |
| comprehensions             | 11.9 us                                                             | 13.8 us: 1.16x slower                                                          |
| fannkuch                   | 270 ms                                                              | 314 ms: 1.16x slower                                                           |
| tomli_loads                | 1.65 sec                                                            | 1.93 sec: 1.17x slower                                                         |
| scimark_fft                | 198 ms                                                              | 233 ms: 1.18x slower                                                           |
| nbody                      | 76.9 ms                                                             | 91.3 ms: 1.19x slower                                                          |
| float                      | 52.4 ms                                                             | 62.2 ms: 1.19x slower                                                          |
| deltablue                  | 2.23 ms                                                             | 2.68 ms: 1.20x slower                                                          |
| xml_etree_process          | 42.1 ms                                                             | 50.7 ms: 1.20x slower                                                          |
| hexiom                     | 4.23 ms                                                             | 5.10 ms: 1.21x slower                                                          |
| pickle_pure_python         | 213 us                                                              | 257 us: 1.21x slower                                                           |
| richards                   | 31.2 ms                                                             | 37.9 ms: 1.21x slower                                                          |
| scimark_sor                | 81.0 ms                                                             | 98.3 ms: 1.21x slower                                                          |
| scimark_monte_carlo        | 45.2 ms                                                             | 55.4 ms: 1.23x slower                                                          |
| richards_super             | 35.5 ms                                                             | 43.5 ms: 1.23x slower                                                          |
| unpickle_pure_python       | 147 us                                                              | 181 us: 1.23x slower                                                           |
| generators                 | 21.2 ms                                                             | 26.2 ms: 1.24x slower                                                          |
| raytrace                   | 189 ms                                                              | 236 ms: 1.25x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 74.5 ns: 1.29x slower                                                          |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                   |

Benchmark hidden because not significant (7): async_tree_none_tg, async_tree_memoization_tg, regex_effbot, regex_dna, deepcopy_reduce, async_tree_io, asyncio_tcp
Ignored benchmarks (2) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: chameleon, flaskblogging
Ignored benchmarks (2) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf1_win32-x86-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: unknown