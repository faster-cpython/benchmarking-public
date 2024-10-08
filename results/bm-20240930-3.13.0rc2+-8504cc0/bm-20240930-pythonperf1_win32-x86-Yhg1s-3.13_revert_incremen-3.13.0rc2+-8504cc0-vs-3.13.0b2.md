# Results vs. 3.13.0b2

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-x86
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.02x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 243 ms: 1.04x slower                                                            |
| docutils       | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                          |
| tornado_http   | 94.3 ms                                                             | 104 ms: 1.10x slower                                                            |
| Geometric mean | (ref)                                                               | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): chameleon, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 529 ms                                                              | 490 ms: 1.08x faster                                                            |
| async_tree_io              | 530 ms                                                              | 515 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 480 ms: 1.02x slower                                                            |
| async_tree_none            | 228 ms                                                              | 238 ms: 1.05x slower                                                            |
| async_tree_memoization     | 275 ms                                                              | 290 ms: 1.05x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 214 ms: 1.05x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 280 ms: 1.10x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 76.9 ms                                                             | 75.5 ms: 1.02x faster                                                           |
| pidigits       | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| float          | 52.4 ms                                                             | 54.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| regex_effbot   | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.39 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 64.2 ms                                                             | 62.0 ms: 1.03x faster                                                           |
| pickle_dict          | 20.8 us                                                             | 20.3 us: 1.02x faster                                                           |
| pickle               | 8.07 us                                                             | 7.98 us: 1.01x faster                                                           |
| xml_etree_generate   | 59.6 ms                                                             | 60.1 ms: 1.01x slower                                                           |
| xml_etree_parse      | 104 ms                                                              | 106 ms: 1.01x slower                                                            |
| json_loads           | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| unpickle_pure_python | 147 us                                                              | 150 us: 1.02x slower                                                            |
| tomli_loads          | 1.65 sec                                                            | 1.69 sec: 1.03x slower                                                          |
| json_dumps           | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                           |
| xml_etree_process    | 42.1 ms                                                             | 43.9 ms: 1.04x slower                                                           |
| pickle_pure_python   | 213 us                                                              | 225 us: 1.06x slower                                                            |
| unpickle             | 9.79 us                                                             | 10.5 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                               | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                           |
| python_startup_no_site | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                           |
| Geometric mean         | (ref)                                                               | 1.09x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 6.94 ms                                                             | 6.90 ms: 1.01x faster                                                           |
| genshi_text    | 20.1 ms                                                             | 20.3 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                               | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:-------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| create_gc_cycles           | 756 us                                                              | 691 us: 1.09x faster                                                            |
| async_tree_io_tg           | 529 ms                                                              | 490 ms: 1.08x faster                                                            |
| pickle_list                | 3.57 us                                                             | 3.39 us: 1.05x faster                                                           |
| xml_etree_iterparse        | 64.2 ms                                                             | 62.0 ms: 1.03x faster                                                           |
| async_tree_io              | 530 ms                                                              | 515 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 607 ms                                                              | 591 ms: 1.03x faster                                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.21 sec: 1.02x faster                                                          |
| pickle_dict                | 20.8 us                                                             | 20.3 us: 1.02x faster                                                           |
| nbody                      | 76.9 ms                                                             | 75.5 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 2.82 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                              | 196 ms: 1.01x faster                                                            |
| chaos                      | 48.0 ms                                                             | 47.3 ms: 1.01x faster                                                           |
| pickle                     | 8.07 us                                                             | 7.98 us: 1.01x faster                                                           |
| docutils                   | 1.81 sec                                                            | 1.79 sec: 1.01x faster                                                          |
| mako                       | 6.94 ms                                                             | 6.90 ms: 1.01x faster                                                           |
| sqlite_synth               | 1.96 us                                                             | 1.97 us: 1.00x slower                                                           |
| nqueens                    | 68.7 ms                                                             | 69.0 ms: 1.00x slower                                                           |
| sympy_str                  | 211 ms                                                              | 212 ms: 1.01x slower                                                            |
| sympy_sum                  | 105 ms                                                              | 106 ms: 1.01x slower                                                            |
| genshi_text                | 20.1 ms                                                             | 20.3 ms: 1.01x slower                                                           |
| xml_etree_generate         | 59.6 ms                                                             | 60.1 ms: 1.01x slower                                                           |
| logging_silent             | 57.9 ns                                                             | 58.4 ns: 1.01x slower                                                           |
| meteor_contest             | 74.1 ms                                                             | 74.8 ms: 1.01x slower                                                           |
| generators                 | 21.2 ms                                                             | 21.4 ms: 1.01x slower                                                           |
| scimark_fft                | 198 ms                                                              | 200 ms: 1.01x slower                                                            |
| regex_dna                  | 118 ms                                                              | 119 ms: 1.01x slower                                                            |
| spectral_norm              | 68.0 ms                                                             | 68.8 ms: 1.01x slower                                                           |
| coroutines                 | 15.5 ms                                                             | 15.7 ms: 1.01x slower                                                           |
| xml_etree_parse            | 104 ms                                                              | 106 ms: 1.01x slower                                                            |
| regex_effbot               | 1.88 ms                                                             | 1.91 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 454 ms: 1.01x slower                                                            |
| sympy_integrate            | 14.6 ms                                                             | 14.9 ms: 1.02x slower                                                           |
| logging_format             | 8.13 us                                                             | 8.26 us: 1.02x slower                                                           |
| sqlglot_normalize          | 206 ms                                                              | 209 ms: 1.02x slower                                                            |
| logging_simple             | 7.47 us                                                             | 7.58 us: 1.02x slower                                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.1 sec: 1.02x slower                                                          |
| mdp                        | 1.60 sec                                                            | 1.63 sec: 1.02x slower                                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 480 ms: 1.02x slower                                                            |
| json_loads                 | 20.5 us                                                             | 20.9 us: 1.02x slower                                                           |
| typing_runtime_protocols   | 136 us                                                              | 138 us: 1.02x slower                                                            |
| unpickle_pure_python       | 147 us                                                              | 150 us: 1.02x slower                                                            |
| fannkuch                   | 270 ms                                                              | 277 ms: 1.03x slower                                                            |
| deepcopy                   | 280 us                                                              | 287 us: 1.03x slower                                                            |
| tomli_loads                | 1.65 sec                                                            | 1.69 sec: 1.03x slower                                                          |
| scimark_lu                 | 59.4 ms                                                             | 61.0 ms: 1.03x slower                                                           |
| comprehensions             | 11.9 us                                                             | 12.2 us: 1.03x slower                                                           |
| richards_super             | 35.5 ms                                                             | 36.5 ms: 1.03x slower                                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 41.0 ms: 1.03x slower                                                           |
| async_generators           | 266 ms                                                              | 274 ms: 1.03x slower                                                            |
| scimark_monte_carlo        | 45.2 ms                                                             | 46.6 ms: 1.03x slower                                                           |
| json_dumps                 | 6.84 ms                                                             | 7.06 ms: 1.03x slower                                                           |
| deepcopy_reduce            | 2.59 us                                                             | 2.67 us: 1.03x slower                                                           |
| json                       | 4.10 ms                                                             | 4.23 ms: 1.03x slower                                                           |
| hexiom                     | 4.23 ms                                                             | 4.38 ms: 1.03x slower                                                           |
| richards                   | 31.2 ms                                                             | 32.3 ms: 1.04x slower                                                           |
| thrift                     | 9.73 ms                                                             | 10.1 ms: 1.04x slower                                                           |
| xml_etree_process          | 42.1 ms                                                             | 43.9 ms: 1.04x slower                                                           |
| coverage                   | 307 ms                                                              | 320 ms: 1.04x slower                                                            |
| 2to3                       | 233 ms                                                              | 243 ms: 1.04x slower                                                            |
| scimark_sor                | 81.0 ms                                                             | 84.6 ms: 1.04x slower                                                           |
| async_tree_none            | 228 ms                                                              | 238 ms: 1.05x slower                                                            |
| float                      | 52.4 ms                                                             | 54.8 ms: 1.05x slower                                                           |
| deepcopy_memo              | 23.5 us                                                             | 24.7 us: 1.05x slower                                                           |
| async_tree_memoization     | 275 ms                                                              | 290 ms: 1.05x slower                                                            |
| async_tree_none_tg         | 203 ms                                                              | 214 ms: 1.05x slower                                                            |
| pickle_pure_python         | 213 us                                                              | 225 us: 1.06x slower                                                            |
| pathlib                    | 83.9 ms                                                             | 88.6 ms: 1.06x slower                                                           |
| pyflate                    | 308 ms                                                              | 326 ms: 1.06x slower                                                            |
| go                         | 101 ms                                                              | 106 ms: 1.06x slower                                                            |
| bench_mp_pool              | 69.4 ms                                                             | 74.1 ms: 1.07x slower                                                           |
| pycparser                  | 777 ms                                                              | 834 ms: 1.07x slower                                                            |
| unpickle                   | 9.79 us                                                             | 10.5 us: 1.08x slower                                                           |
| python_startup             | 22.2 ms                                                             | 24.1 ms: 1.08x slower                                                           |
| telco                      | 6.03 ms                                                             | 6.55 ms: 1.09x slower                                                           |
| python_startup_no_site     | 18.2 ms                                                             | 19.9 ms: 1.09x slower                                                           |
| tornado_http               | 94.3 ms                                                             | 104 ms: 1.10x slower                                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 280 ms: 1.10x slower                                                            |
| asyncio_tcp                | 662 ms                                                              | 751 ms: 1.14x slower                                                            |
| Geometric mean             | (ref)                                                               | 1.02x slower                                                                    |

Benchmark hidden because not significant (17): bench_thread_pool, deltablue, sqlglot_parse, sympy_expand, crypto_pyaes, regex_compile, flaskblogging, sqlglot_transpile, django_template, regex_v8, chameleon, genshi_xml, raytrace, unpickle_list, html5lib, gc_traversal, pylint
Ignored benchmarks (2) of results/bm-20240930-3.13.0rc2+-8504cc0/bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0.json: dulwich_log, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown