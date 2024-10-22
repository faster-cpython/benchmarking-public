# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.02x faster
- HPT reliability: 99.81%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none           | 246 ms                                                          | 215 ms: 1.14x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 751 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 199 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| Geometric mean            | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 57.8 ms                                                         | 62.0 ms: 1.07x slower                                                          |
| nbody          | 81.9 ms                                                         | 95.8 ms: 1.17x slower                                                          |
| Geometric mean | (ref)                                                           | 1.08x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_dna      | 117 ms                                                          | 122 ms: 1.05x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                          |
| json_dumps           | 7.40 ms                                                         | 7.74 ms: 1.05x slower                                                          |
| pickle_pure_python   | 238 us                                                          | 254 us: 1.07x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| xml_etree_generate   | 62.6 ms                                                         | 68.4 ms: 1.09x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 179 us: 1.11x slower                                                           |
| xml_etree_process    | 45.0 ms                                                         | 51.0 ms: 1.13x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| python_startup         | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml     | 49.5 ms                                                         | 46.8 ms: 1.06x faster                                                          |
| genshi_text    | 22.4 ms                                                         | 21.8 ms: 1.03x faster                                                          |
| mako           | 7.31 ms                                                         | 8.41 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 727 us: 13.95x faster                                                          |
| coverage                  | 333 ms                                                          | 54.0 ms: 6.17x faster                                                          |
| deepcopy                  | 307 us                                                          | 246 us: 1.25x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 22.0 us: 1.19x faster                                                          |
| async_tree_none           | 246 ms                                                          | 215 ms: 1.14x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.51 us: 1.14x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 253 ms: 1.13x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 751 ms: 1.12x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 199 ms: 1.10x faster                                                           |
| go                        | 111 ms                                                          | 103 ms: 1.08x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 465 ms: 1.06x faster                                                           |
| genshi_xml                | 49.5 ms                                                         | 46.8 ms: 1.06x faster                                                          |
| html5lib                  | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 21.8 ms: 1.03x faster                                                          |
| pathlib                   | 89.4 ms                                                         | 86.9 ms: 1.03x faster                                                          |
| json_loads                | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 72.8 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| pycparser                 | 869 ms                                                          | 857 ms: 1.01x faster                                                           |
| xml_etree_parse           | 109 ms                                                          | 107 ms: 1.01x faster                                                           |
| gc_traversal              | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 19.7 ms: 1.01x faster                                                          |
| 2to3                      | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| sympy_sum                 | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| python_startup            | 24.3 ms                                                         | 24.1 ms: 1.01x faster                                                          |
| sympy_str                 | 215 ms                                                          | 216 ms: 1.01x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 75.9 ms: 1.01x slower                                                          |
| sympy_integrate           | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 223 ms: 1.01x slower                                                           |
| pprint_safe_repr          | 644 ms                                                          | 654 ms: 1.01x slower                                                           |
| mdp                       | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                         |
| async_tree_io_tg          | 509 ms                                                          | 518 ms: 1.02x slower                                                           |
| sympy_expand              | 375 ms                                                          | 381 ms: 1.02x slower                                                           |
| logging_simple            | 7.87 us                                                         | 8.02 us: 1.02x slower                                                          |
| sqlglot_parse             | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.32 ms: 1.02x slower                                                          |
| docutils                  | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| sqlglot_optimize          | 42.5 ms                                                         | 43.5 ms: 1.02x slower                                                          |
| logging_format            | 8.57 us                                                         | 8.78 us: 1.02x slower                                                          |
| pprint_pformat            | 1.30 sec                                                        | 1.33 sec: 1.03x slower                                                         |
| regex_compile             | 103 ms                                                          | 107 ms: 1.03x slower                                                           |
| meteor_contest            | 77.0 ms                                                         | 79.9 ms: 1.04x slower                                                          |
| pylint                    | 225 ms                                                          | 233 ms: 1.04x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| xml_etree_iterparse       | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                          |
| regex_dna                 | 117 ms                                                          | 122 ms: 1.05x slower                                                           |
| chaos                     | 51.2 ms                                                         | 53.5 ms: 1.05x slower                                                          |
| json_dumps                | 7.40 ms                                                         | 7.74 ms: 1.05x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 751 us: 1.05x slower                                                           |
| spectral_norm             | 71.3 ms                                                         | 75.6 ms: 1.06x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.5 us: 1.06x slower                                                          |
| telco                     | 6.67 ms                                                         | 7.08 ms: 1.06x slower                                                          |
| pickle_pure_python        | 238 us                                                          | 254 us: 1.07x slower                                                           |
| regex_effbot              | 1.81 ms                                                         | 1.94 ms: 1.07x slower                                                          |
| float                     | 57.8 ms                                                         | 62.0 ms: 1.07x slower                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.86 sec: 1.07x slower                                                         |
| typing_runtime_protocols  | 136 us                                                          | 148 us: 1.08x slower                                                           |
| xml_etree_generate        | 62.6 ms                                                         | 68.4 ms: 1.09x slower                                                          |
| pyflate                   | 326 ms                                                          | 358 ms: 1.10x slower                                                           |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.19 ms: 1.10x slower                                                          |
| unpickle_pure_python      | 162 us                                                          | 179 us: 1.11x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 70.6 ms: 1.11x slower                                                          |
| scimark_sor               | 91.8 ms                                                         | 102 ms: 1.11x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| async_generators          | 274 ms                                                          | 307 ms: 1.12x slower                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 56.6 ms: 1.13x slower                                                          |
| fannkuch                  | 293 ms                                                          | 332 ms: 1.13x slower                                                           |
| deltablue                 | 2.41 ms                                                         | 2.72 ms: 1.13x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 51.0 ms: 1.13x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.29 ms: 1.14x slower                                                          |
| scimark_fft               | 206 ms                                                          | 237 ms: 1.15x slower                                                           |
| raytrace                  | 205 ms                                                          | 236 ms: 1.15x slower                                                           |
| mako                      | 7.31 ms                                                         | 8.41 ms: 1.15x slower                                                          |
| richards                  | 33.8 ms                                                         | 39.0 ms: 1.15x slower                                                          |
| nbody                     | 81.9 ms                                                         | 95.8 ms: 1.17x slower                                                          |
| richards_super            | 38.0 ms                                                         | 44.8 ms: 1.18x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 74.5 ns: 1.21x slower                                                          |
| generators                | 22.1 ms                                                         | 27.9 ms: 1.26x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (9): bench_thread_pool, pidigits, crypto_pyaes, json, async_tree_cpu_io_mixed_tg, django_template, tornado_http, async_tree_io, dulwich_log
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.81% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown