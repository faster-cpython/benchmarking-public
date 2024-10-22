# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.1 ms: 1.05x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 716 ms: 1.18x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| async_tree_none           | 246 ms                                                          | 216 ms: 1.14x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 198 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_generators          | 274 ms                                                          | 297 ms: 1.08x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (3): async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                          |
| nbody          | 81.9 ms                                                         | 96.0 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 117 ms                                                          | 121 ms: 1.04x slower                                                           |
| regex_compile  | 103 ms                                                          | 107 ms: 1.04x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 251 us: 1.05x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 50.0 ms: 1.11x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.05x slower                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 49.5 ms                                                         | 46.1 ms: 1.08x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 21.9 ms: 1.03x faster                                                          |
| mako           | 7.31 ms                                                         | 8.20 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 741 us: 13.70x faster                                                          |
| coverage                  | 333 ms                                                          | 51.8 ms: 6.43x faster                                                          |
| deepcopy                  | 307 us                                                          | 238 us: 1.29x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 22.0 us: 1.19x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 716 ms: 1.18x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 247 ms: 1.16x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.46 us: 1.16x faster                                                          |
| async_tree_none           | 246 ms                                                          | 216 ms: 1.14x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 272 ms: 1.11x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 198 ms: 1.11x faster                                                           |
| genshi_xml                | 49.5 ms                                                         | 46.1 ms: 1.08x faster                                                          |
| go                        | 111 ms                                                          | 104 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| html5lib                  | 48.3 ms                                                         | 46.1 ms: 1.05x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 86.9 ms: 1.03x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 21.9 ms: 1.03x faster                                                          |
| python_startup            | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| xml_etree_parse           | 109 ms                                                          | 107 ms: 1.02x faster                                                           |
| 2to3                      | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| bench_mp_pool             | 74.3 ms                                                         | 73.2 ms: 1.01x faster                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| dulwich_log               | 49.7 ms                                                         | 49.2 ms: 1.01x faster                                                          |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| gc_traversal              | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| sympy_str                 | 215 ms                                                          | 216 ms: 1.01x slower                                                           |
| logging_simple            | 7.87 us                                                         | 7.92 us: 1.01x slower                                                          |
| json_dumps                | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 42.9 ms: 1.01x slower                                                          |
| logging_format            | 8.57 us                                                         | 8.65 us: 1.01x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 223 ms: 1.01x slower                                                           |
| mdp                       | 1.67 sec                                                        | 1.70 sec: 1.01x slower                                                         |
| telco                     | 6.67 ms                                                         | 6.77 ms: 1.02x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| docutils                  | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| pycparser                 | 869 ms                                                          | 888 ms: 1.02x slower                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.32 sec: 1.02x slower                                                         |
| crypto_pyaes              | 58.2 ms                                                         | 59.5 ms: 1.02x slower                                                          |
| sqlglot_parse             | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                          |
| sympy_expand              | 375 ms                                                          | 384 ms: 1.03x slower                                                           |
| sqlglot_transpile         | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| regex_dna                 | 117 ms                                                          | 121 ms: 1.04x slower                                                           |
| regex_compile             | 103 ms                                                          | 107 ms: 1.04x slower                                                           |
| xml_etree_iterparse       | 65.1 ms                                                         | 67.7 ms: 1.04x slower                                                          |
| pylint                    | 225 ms                                                          | 235 ms: 1.05x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 16.4 ms: 1.05x slower                                                          |
| pickle_pure_python        | 238 us                                                          | 251 us: 1.05x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 79.3 ms: 1.06x slower                                                          |
| chaos                     | 51.2 ms                                                         | 54.1 ms: 1.06x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 754 us: 1.06x slower                                                           |
| meteor_contest            | 77.0 ms                                                         | 82.0 ms: 1.06x slower                                                          |
| float                     | 57.8 ms                                                         | 61.5 ms: 1.06x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.6 us: 1.07x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| xml_etree_generate        | 62.6 ms                                                         | 67.3 ms: 1.08x slower                                                          |
| spectral_norm             | 71.3 ms                                                         | 76.9 ms: 1.08x slower                                                          |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.15 ms: 1.08x slower                                                          |
| async_generators          | 274 ms                                                          | 297 ms: 1.08x slower                                                           |
| typing_runtime_protocols  | 136 us                                                          | 149 us: 1.09x slower                                                           |
| pyflate                   | 326 ms                                                          | 358 ms: 1.10x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 70.0 ms: 1.10x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 50.0 ms: 1.11x slower                                                          |
| scimark_sor               | 91.8 ms                                                         | 102 ms: 1.11x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 179 us: 1.11x slower                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 56.4 ms: 1.12x slower                                                          |
| mako                      | 7.31 ms                                                         | 8.20 ms: 1.12x slower                                                          |
| raytrace                  | 205 ms                                                          | 231 ms: 1.12x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.8 ms: 1.13x slower                                                          |
| deltablue                 | 2.41 ms                                                         | 2.75 ms: 1.14x slower                                                          |
| scimark_fft               | 206 ms                                                          | 237 ms: 1.15x slower                                                           |
| hexiom                    | 4.64 ms                                                         | 5.36 ms: 1.16x slower                                                          |
| fannkuch                  | 293 ms                                                          | 342 ms: 1.17x slower                                                           |
| nbody                     | 81.9 ms                                                         | 96.0 ms: 1.17x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 74.8 ns: 1.21x slower                                                          |
| richards_super            | 38.0 ms                                                         | 46.9 ms: 1.24x slower                                                          |
| richards                  | 33.8 ms                                                         | 41.9 ms: 1.24x slower                                                          |
| generators                | 22.1 ms                                                         | 27.6 ms: 1.25x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (10): async_tree_io, bench_thread_pool, async_tree_cpu_io_mixed_tg, async_tree_io_tg, pprint_safe_repr, pidigits, tornado_http, json, json_loads, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.83% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown