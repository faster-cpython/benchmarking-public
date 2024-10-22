# Results vs. 3.13.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.05x faster
- HPT reliability: 91.43%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| tornado_http   | 104 ms                                                          | 95.0 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp               | 842 ms                                                          | 651 ms: 1.29x faster                                                           |
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none           | 246 ms                                                          | 225 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 477 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                         |
| async_tree_io             | 537 ms                                                          | 546 ms: 1.02x slower                                                           |
| async_generators          | 274 ms                                                          | 285 ms: 1.04x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.2 ms: 1.10x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_io_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 58.9 ms: 1.02x slower                                                          |
| nbody          | 81.9 ms                                                         | 89.0 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| regex_dna      | 117 ms                                                          | 124 ms: 1.06x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_dumps           | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 105 ms: 1.03x faster                                                           |
| json_loads           | 21.0 us                                                         | 21.2 us: 1.01x slower                                                          |
| xml_etree_iterparse  | 65.1 ms                                                         | 66.0 ms: 1.01x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 167 us: 1.03x slower                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| pickle_pure_python   | 238 us                                                          | 250 us: 1.05x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 68.3 ms: 1.09x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 49.7 ms: 1.10x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                                          |
| python_startup_no_site | 19.9 ms                                                         | 18.9 ms: 1.05x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.3 ms: 1.07x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.9 ms: 1.02x faster                                                          |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| mako            | 7.31 ms                                                         | 7.95 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.00x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 778 us: 13.04x faster                                                          |
| coverage                  | 333 ms                                                          | 52.6 ms: 6.33x faster                                                          |
| asyncio_tcp               | 842 ms                                                          | 651 ms: 1.29x faster                                                           |
| deepcopy                  | 307 us                                                          | 241 us: 1.27x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 21.4 us: 1.23x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.47 us: 1.16x faster                                                          |
| async_tree_none_tg        | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| tornado_http              | 104 ms                                                          | 95.0 ms: 1.10x faster                                                          |
| async_tree_none           | 246 ms                                                          | 225 ms: 1.10x faster                                                           |
| pathlib                   | 89.4 ms                                                         | 82.2 ms: 1.09x faster                                                          |
| genshi_xml                | 49.5 ms                                                         | 46.3 ms: 1.07x faster                                                          |
| python_startup            | 24.3 ms                                                         | 22.9 ms: 1.06x faster                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 70.5 ms: 1.05x faster                                                          |
| pycparser                 | 869 ms                                                          | 824 ms: 1.05x faster                                                           |
| python_startup_no_site    | 19.9 ms                                                         | 18.9 ms: 1.05x faster                                                          |
| telco                     | 6.67 ms                                                         | 6.35 ms: 1.05x faster                                                          |
| json_dumps                | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 477 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 16.8 sec: 1.03x faster                                                         |
| xml_etree_parse           | 109 ms                                                          | 105 ms: 1.03x faster                                                           |
| bench_thread_pool         | 1.02 ms                                                         | 990 us: 1.03x faster                                                           |
| pidigits                  | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| nqueens                   | 75.1 ms                                                         | 73.1 ms: 1.03x faster                                                          |
| genshi_text               | 22.4 ms                                                         | 21.9 ms: 1.02x faster                                                          |
| logging_simple            | 7.87 us                                                         | 7.74 us: 1.02x faster                                                          |
| logging_format            | 8.57 us                                                         | 8.43 us: 1.02x faster                                                          |
| 2to3                      | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| pprint_safe_repr          | 644 ms                                                          | 634 ms: 1.02x faster                                                           |
| gc_traversal              | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| crypto_pyaes              | 58.2 ms                                                         | 57.7 ms: 1.01x faster                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.28 ms: 1.01x faster                                                          |
| mdp                       | 1.67 sec                                                        | 1.68 sec: 1.01x slower                                                         |
| sympy_integrate           | 15.2 ms                                                         | 15.3 ms: 1.01x slower                                                          |
| json_loads                | 21.0 us                                                         | 21.2 us: 1.01x slower                                                          |
| sympy_str                 | 215 ms                                                          | 218 ms: 1.01x slower                                                           |
| xml_etree_iterparse       | 65.1 ms                                                         | 66.0 ms: 1.01x slower                                                          |
| sqlglot_optimize          | 42.5 ms                                                         | 43.1 ms: 1.01x slower                                                          |
| sympy_expand              | 375 ms                                                          | 381 ms: 1.02x slower                                                           |
| django_template           | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| async_tree_io             | 537 ms                                                          | 546 ms: 1.02x slower                                                           |
| float                     | 57.8 ms                                                         | 58.9 ms: 1.02x slower                                                          |
| go                        | 111 ms                                                          | 114 ms: 1.02x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 16.0 ms: 1.02x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 226 ms: 1.03x slower                                                           |
| docutils                  | 1.82 sec                                                        | 1.87 sec: 1.03x slower                                                         |
| meteor_contest            | 77.0 ms                                                         | 79.1 ms: 1.03x slower                                                          |
| pyflate                   | 326 ms                                                          | 335 ms: 1.03x slower                                                           |
| json                      | 4.27 ms                                                         | 4.41 ms: 1.03x slower                                                          |
| unpickle_pure_python      | 162 us                                                          | 167 us: 1.03x slower                                                           |
| scimark_sor               | 91.8 ms                                                         | 95.0 ms: 1.03x slower                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.79 sec: 1.04x slower                                                         |
| async_generators          | 274 ms                                                          | 285 ms: 1.04x slower                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 52.4 ms: 1.04x slower                                                          |
| comprehensions            | 12.7 us                                                         | 13.3 us: 1.05x slower                                                          |
| raytrace                  | 205 ms                                                          | 215 ms: 1.05x slower                                                           |
| create_gc_cycles          | 713 us                                                          | 748 us: 1.05x slower                                                           |
| chaos                     | 51.2 ms                                                         | 53.8 ms: 1.05x slower                                                          |
| pickle_pure_python        | 238 us                                                          | 250 us: 1.05x slower                                                           |
| fannkuch                  | 293 ms                                                          | 309 ms: 1.06x slower                                                           |
| spectral_norm             | 71.3 ms                                                         | 75.3 ms: 1.06x slower                                                          |
| regex_dna                 | 117 ms                                                          | 124 ms: 1.06x slower                                                           |
| scimark_lu                | 63.5 ms                                                         | 67.2 ms: 1.06x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.09 ms: 1.06x slower                                                          |
| scimark_fft               | 206 ms                                                          | 220 ms: 1.07x slower                                                           |
| richards_super            | 38.0 ms                                                         | 40.7 ms: 1.07x slower                                                          |
| hexiom                    | 4.64 ms                                                         | 5.01 ms: 1.08x slower                                                          |
| deltablue                 | 2.41 ms                                                         | 2.61 ms: 1.09x slower                                                          |
| nbody                     | 81.9 ms                                                         | 89.0 ms: 1.09x slower                                                          |
| mako                      | 7.31 ms                                                         | 7.95 ms: 1.09x slower                                                          |
| richards                  | 33.8 ms                                                         | 36.8 ms: 1.09x slower                                                          |
| xml_etree_generate        | 62.6 ms                                                         | 68.3 ms: 1.09x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.2 ms: 1.10x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 49.7 ms: 1.10x slower                                                          |
| typing_runtime_protocols  | 136 us                                                          | 153 us: 1.12x slower                                                           |
| generators                | 22.1 ms                                                         | 26.6 ms: 1.21x slower                                                          |
| logging_silent            | 61.6 ns                                                         | 74.9 ns: 1.22x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (8): async_tree_io_tg, pylint, sqlglot_parse, sympy_sum, pprint_pformat, regex_compile, async_tree_cpu_io_mixed_tg, html5lib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 91.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown