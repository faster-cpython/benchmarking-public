# Results vs. 3.13.0

- fork: Yhg1s
- ref: 3.13_revert_incremen
- machine: windows-x86
- commit hash: 8504cc0
- commit date: 2024-09-30
- overall geometric mean: 1.04x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 243 ms: 1.04x faster                                                            |
| chameleon      | 6.14 ms                                                         | 5.73 ms: 1.07x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.79 sec: 1.01x faster                                                          |
| html5lib       | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 751 ms: 1.12x faster                                                            |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                            |
| async_tree_io              | 537 ms                                                          | 515 ms: 1.04x faster                                                            |
| async_tree_io_tg           | 509 ms                                                          | 490 ms: 1.04x faster                                                            |
| async_tree_none            | 246 ms                                                          | 238 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 480 ms: 1.03x faster                                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 280 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 219 ms                                                          | 214 ms: 1.02x faster                                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                            |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                    |

Benchmark hidden because not significant (2): coroutines, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 75.5 ms: 1.08x faster                                                           |
| float          | 57.8 ms                                                         | 54.8 ms: 1.05x faster                                                           |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 100 ms: 1.03x faster                                                            |
| regex_v8       | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                           |
| regex_dna      | 117 ms                                                          | 119 ms: 1.02x slower                                                            |
| regex_effbot   | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 162 us                                                          | 150 us: 1.07x faster                                                            |
| pickle_dict          | 21.7 us                                                         | 20.3 us: 1.07x faster                                                           |
| pickle_pure_python   | 238 us                                                          | 225 us: 1.06x faster                                                            |
| pickle               | 8.42 us                                                         | 7.98 us: 1.05x faster                                                           |
| unpickle_list        | 3.09 us                                                         | 2.94 us: 1.05x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 62.0 ms: 1.05x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 60.1 ms: 1.04x faster                                                           |
| xml_etree_parse      | 109 ms                                                          | 106 ms: 1.03x faster                                                            |
| xml_etree_process    | 45.0 ms                                                         | 43.9 ms: 1.03x faster                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.69 sec: 1.02x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (3): json_loads, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 44.4 ms: 1.12x faster                                                           |
| genshi_text     | 22.4 ms                                                         | 20.3 ms: 1.11x faster                                                           |
| django_template | 32.7 ms                                                         | 30.1 ms: 1.08x faster                                                           |
| mako            | 7.31 ms                                                         | 6.90 ms: 1.06x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.09x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240930-pythonperf1_win32-x86-Yhg1s-3.13_revert_incremen-3.13.0rc2+-8504cc0 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 751 ms: 1.12x faster                                                            |
| genshi_xml                 | 49.5 ms                                                         | 44.4 ms: 1.12x faster                                                           |
| genshi_text                | 22.4 ms                                                         | 20.3 ms: 1.11x faster                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 962 us: 1.09x faster                                                            |
| pprint_safe_repr           | 644 ms                                                          | 591 ms: 1.09x faster                                                            |
| nqueens                    | 75.1 ms                                                         | 69.0 ms: 1.09x faster                                                           |
| scimark_sor                | 91.8 ms                                                         | 84.6 ms: 1.09x faster                                                           |
| django_template            | 32.7 ms                                                         | 30.1 ms: 1.08x faster                                                           |
| raytrace                   | 205 ms                                                          | 189 ms: 1.08x faster                                                            |
| nbody                      | 81.9 ms                                                         | 75.5 ms: 1.08x faster                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.19 ms: 1.08x faster                                                           |
| chaos                      | 51.2 ms                                                         | 47.3 ms: 1.08x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 46.6 ms: 1.08x faster                                                           |
| deltablue                  | 2.41 ms                                                         | 2.23 ms: 1.08x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 150 us: 1.07x faster                                                            |
| chameleon                  | 6.14 ms                                                         | 5.73 ms: 1.07x faster                                                           |
| deepcopy                   | 307 us                                                          | 287 us: 1.07x faster                                                            |
| pprint_pformat             | 1.30 sec                                                        | 1.21 sec: 1.07x faster                                                          |
| pickle_dict                | 21.7 us                                                         | 20.3 us: 1.07x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.67 us: 1.07x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 24.7 us: 1.06x faster                                                           |
| hexiom                     | 4.64 ms                                                         | 4.38 ms: 1.06x faster                                                           |
| mako                       | 7.31 ms                                                         | 6.90 ms: 1.06x faster                                                           |
| fannkuch                   | 293 ms                                                          | 277 ms: 1.06x faster                                                            |
| pickle_pure_python         | 238 us                                                          | 225 us: 1.06x faster                                                            |
| html5lib                   | 48.3 ms                                                         | 45.7 ms: 1.06x faster                                                           |
| logging_silent             | 61.6 ns                                                         | 58.4 ns: 1.05x faster                                                           |
| pickle                     | 8.42 us                                                         | 7.98 us: 1.05x faster                                                           |
| float                      | 57.8 ms                                                         | 54.8 ms: 1.05x faster                                                           |
| unpickle_list              | 3.09 us                                                         | 2.94 us: 1.05x faster                                                           |
| sqlglot_normalize          | 220 ms                                                          | 209 ms: 1.05x faster                                                            |
| xml_etree_iterparse        | 65.1 ms                                                         | 62.0 ms: 1.05x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.06 ms: 1.05x faster                                                           |
| go                         | 111 ms                                                          | 106 ms: 1.05x faster                                                            |
| richards                   | 33.8 ms                                                         | 32.3 ms: 1.05x faster                                                           |
| comprehensions             | 12.7 us                                                         | 12.2 us: 1.04x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 290 ms: 1.04x faster                                                            |
| crypto_pyaes               | 58.2 ms                                                         | 55.8 ms: 1.04x faster                                                           |
| pycparser                  | 869 ms                                                          | 834 ms: 1.04x faster                                                            |
| async_tree_io              | 537 ms                                                          | 515 ms: 1.04x faster                                                            |
| xml_etree_generate         | 62.6 ms                                                         | 60.1 ms: 1.04x faster                                                           |
| scimark_lu                 | 63.5 ms                                                         | 61.0 ms: 1.04x faster                                                           |
| 2to3                       | 253 ms                                                          | 243 ms: 1.04x faster                                                            |
| richards_super             | 38.0 ms                                                         | 36.5 ms: 1.04x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 490 ms: 1.04x faster                                                            |
| coverage                   | 333 ms                                                          | 320 ms: 1.04x faster                                                            |
| logging_simple             | 7.87 us                                                         | 7.58 us: 1.04x faster                                                           |
| bench_thread_pool          | 1.02 ms                                                         | 983 us: 1.04x faster                                                            |
| logging_format             | 8.57 us                                                         | 8.26 us: 1.04x faster                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 41.0 ms: 1.04x faster                                                           |
| spectral_norm              | 71.3 ms                                                         | 68.8 ms: 1.04x faster                                                           |
| generators                 | 22.1 ms                                                         | 21.4 ms: 1.03x faster                                                           |
| regex_compile              | 103 ms                                                          | 100 ms: 1.03x faster                                                            |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                            |
| async_tree_none            | 246 ms                                                          | 238 ms: 1.03x faster                                                            |
| create_gc_cycles           | 713 us                                                          | 691 us: 1.03x faster                                                            |
| scimark_fft                | 206 ms                                                          | 200 ms: 1.03x faster                                                            |
| meteor_contest             | 77.0 ms                                                         | 74.8 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 480 ms: 1.03x faster                                                            |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.82 ms: 1.03x faster                                                           |
| xml_etree_parse            | 109 ms                                                          | 106 ms: 1.03x faster                                                            |
| xml_etree_process          | 45.0 ms                                                         | 43.9 ms: 1.03x faster                                                           |
| mdp                        | 1.67 sec                                                        | 1.63 sec: 1.03x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 280 ms: 1.03x faster                                                            |
| async_tree_none_tg         | 219 ms                                                          | 214 ms: 1.02x faster                                                            |
| tomli_loads                | 1.73 sec                                                        | 1.69 sec: 1.02x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 454 ms: 1.02x faster                                                            |
| sympy_sum                  | 108 ms                                                          | 106 ms: 1.02x faster                                                            |
| sympy_integrate            | 15.2 ms                                                         | 14.9 ms: 1.02x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.55 ms: 1.02x faster                                                           |
| docutils                   | 1.82 sec                                                        | 1.79 sec: 1.01x faster                                                          |
| sympy_str                  | 215 ms                                                          | 212 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.01x faster                                                          |
| dulwich_log                | 49.7 ms                                                         | 49.1 ms: 1.01x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 88.6 ms: 1.01x faster                                                           |
| thrift                     | 10.1 ms                                                         | 10.1 ms: 1.01x faster                                                           |
| python_startup             | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                           |
| regex_v8                   | 15.6 ms                                                         | 15.8 ms: 1.01x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 138 us: 1.02x slower                                                            |
| regex_dna                  | 117 ms                                                          | 119 ms: 1.02x slower                                                            |
| regex_effbot               | 1.81 ms                                                         | 1.91 ms: 1.06x slower                                                           |
| unpack_sequence            | 42.9 ns                                                         | 49.4 ns: 1.15x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                    |

Benchmark hidden because not significant (15): pylint, json, gc_traversal, tornado_http, bench_mp_pool, json_loads, python_startup_no_site, pickle_list, sympy_expand, flaskblogging, unpickle, pyflate, coroutines, async_generators, sqlite_synth

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: unknown