# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: windows-x86
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.04x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.90 sec: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.00x slower                                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 732 ms: 1.15x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| async_tree_none           | 246 ms                                                          | 224 ms: 1.10x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| async_tree_io_tg          | 509 ms                                                          | 502 ms: 1.01x faster                                                           |
| async_generators          | 274 ms                                                          | 290 ms: 1.06x slower                                                           |
| coroutines                | 15.7 ms                                                         | 17.2 ms: 1.10x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| float          | 57.8 ms                                                         | 60.5 ms: 1.05x slower                                                          |
| nbody          | 81.9 ms                                                         | 91.4 ms: 1.12x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 105 ms: 1.01x slower                                                           |
| regex_dna      | 117 ms                                                          | 121 ms: 1.04x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.98 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_parse      | 109 ms                                                          | 106 ms: 1.03x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.5 us: 1.02x faster                                                          |
| pickle_pure_python   | 238 us                                                          | 241 us: 1.01x slower                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 168 us: 1.04x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.84 sec: 1.06x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 48.2 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 48.6 ms: 1.02x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| django_template | 32.7 ms                                                         | 33.8 ms: 1.04x slower                                                          |
| mako            | 7.31 ms                                                         | 7.94 ms: 1.09x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240720-pythonperf1_win32-x86-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|---------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                    | 10.1 ms                                                         | 754 us: 13.47x faster                                                          |
| coverage                  | 333 ms                                                          | 54.3 ms: 6.14x faster                                                          |
| deepcopy                  | 307 us                                                          | 247 us: 1.24x faster                                                           |
| deepcopy_memo             | 26.2 us                                                         | 21.4 us: 1.22x faster                                                          |
| async_tree_memoization_tg | 287 ms                                                          | 246 ms: 1.17x faster                                                           |
| asyncio_tcp               | 842 ms                                                          | 732 ms: 1.15x faster                                                           |
| async_tree_none_tg        | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| deepcopy_reduce           | 2.85 us                                                         | 2.56 us: 1.11x faster                                                          |
| async_tree_none           | 246 ms                                                          | 224 ms: 1.10x faster                                                           |
| async_tree_memoization    | 302 ms                                                          | 276 ms: 1.10x faster                                                           |
| telco                     | 6.67 ms                                                         | 6.15 ms: 1.08x faster                                                          |
| async_tree_cpu_io_mixed   | 494 ms                                                          | 479 ms: 1.03x faster                                                           |
| xml_etree_parse           | 109 ms                                                          | 106 ms: 1.03x faster                                                           |
| json_dumps                | 7.40 ms                                                         | 7.21 ms: 1.03x faster                                                          |
| bench_thread_pool         | 1.02 ms                                                         | 996 us: 1.02x faster                                                           |
| asyncio_tcp_ssl           | 17.4 sec                                                        | 17.0 sec: 1.02x faster                                                         |
| json_loads                | 21.0 us                                                         | 20.5 us: 1.02x faster                                                          |
| pycparser                 | 869 ms                                                          | 852 ms: 1.02x faster                                                           |
| pidigits                  | 202 ms                                                          | 198 ms: 1.02x faster                                                           |
| genshi_xml                | 49.5 ms                                                         | 48.6 ms: 1.02x faster                                                          |
| async_tree_io_tg          | 509 ms                                                          | 502 ms: 1.01x faster                                                           |
| pathlib                   | 89.4 ms                                                         | 88.2 ms: 1.01x faster                                                          |
| gc_traversal              | 1.45 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| 2to3                      | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| genshi_text               | 22.4 ms                                                         | 22.3 ms: 1.01x faster                                                          |
| pickle_pure_python        | 238 us                                                          | 241 us: 1.01x slower                                                           |
| meteor_contest            | 77.0 ms                                                         | 77.9 ms: 1.01x slower                                                          |
| regex_compile             | 103 ms                                                          | 105 ms: 1.01x slower                                                           |
| crypto_pyaes              | 58.2 ms                                                         | 58.9 ms: 1.01x slower                                                          |
| python_startup_no_site    | 19.9 ms                                                         | 20.3 ms: 1.02x slower                                                          |
| go                        | 111 ms                                                          | 113 ms: 1.02x slower                                                           |
| sympy_str                 | 215 ms                                                          | 219 ms: 1.02x slower                                                           |
| sympy_integrate           | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| bench_mp_pool             | 74.3 ms                                                         | 75.9 ms: 1.02x slower                                                          |
| sympy_sum                 | 108 ms                                                          | 110 ms: 1.02x slower                                                           |
| pprint_pformat            | 1.30 sec                                                        | 1.33 sec: 1.02x slower                                                         |
| sqlglot_parse             | 1.05 ms                                                         | 1.07 ms: 1.02x slower                                                          |
| sqlglot_transpile         | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| chaos                     | 51.2 ms                                                         | 52.9 ms: 1.03x slower                                                          |
| django_template           | 32.7 ms                                                         | 33.8 ms: 1.04x slower                                                          |
| mdp                       | 1.67 sec                                                        | 1.73 sec: 1.04x slower                                                         |
| xml_etree_iterparse       | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| sympy_expand              | 375 ms                                                          | 388 ms: 1.04x slower                                                           |
| regex_dna                 | 117 ms                                                          | 121 ms: 1.04x slower                                                           |
| pyflate                   | 326 ms                                                          | 338 ms: 1.04x slower                                                           |
| unpickle_pure_python      | 162 us                                                          | 168 us: 1.04x slower                                                           |
| regex_v8                  | 15.6 ms                                                         | 16.2 ms: 1.04x slower                                                          |
| sqlglot_normalize         | 220 ms                                                          | 229 ms: 1.04x slower                                                           |
| sqlglot_optimize          | 42.5 ms                                                         | 44.3 ms: 1.04x slower                                                          |
| docutils                  | 1.82 sec                                                        | 1.90 sec: 1.04x slower                                                         |
| float                     | 57.8 ms                                                         | 60.5 ms: 1.05x slower                                                          |
| xml_etree_generate        | 62.6 ms                                                         | 65.6 ms: 1.05x slower                                                          |
| create_gc_cycles          | 713 us                                                          | 748 us: 1.05x slower                                                           |
| scimark_monte_carlo       | 50.3 ms                                                         | 52.9 ms: 1.05x slower                                                          |
| raytrace                  | 205 ms                                                          | 216 ms: 1.05x slower                                                           |
| nqueens                   | 75.1 ms                                                         | 79.5 ms: 1.06x slower                                                          |
| scimark_sor               | 91.8 ms                                                         | 97.2 ms: 1.06x slower                                                          |
| async_generators          | 274 ms                                                          | 290 ms: 1.06x slower                                                           |
| comprehensions            | 12.7 us                                                         | 13.5 us: 1.06x slower                                                          |
| tomli_loads               | 1.73 sec                                                        | 1.84 sec: 1.06x slower                                                         |
| typing_runtime_protocols  | 136 us                                                          | 145 us: 1.07x slower                                                           |
| hexiom                    | 4.64 ms                                                         | 4.94 ms: 1.07x slower                                                          |
| xml_etree_process         | 45.0 ms                                                         | 48.2 ms: 1.07x slower                                                          |
| scimark_lu                | 63.5 ms                                                         | 68.5 ms: 1.08x slower                                                          |
| mako                      | 7.31 ms                                                         | 7.94 ms: 1.09x slower                                                          |
| deltablue                 | 2.41 ms                                                         | 2.62 ms: 1.09x slower                                                          |
| regex_effbot              | 1.81 ms                                                         | 1.98 ms: 1.09x slower                                                          |
| richards                  | 33.8 ms                                                         | 36.9 ms: 1.09x slower                                                          |
| coroutines                | 15.7 ms                                                         | 17.2 ms: 1.10x slower                                                          |
| scimark_sparse_mat_mult   | 2.90 ms                                                         | 3.20 ms: 1.10x slower                                                          |
| scimark_fft               | 206 ms                                                          | 228 ms: 1.10x slower                                                           |
| spectral_norm             | 71.3 ms                                                         | 78.8 ms: 1.11x slower                                                          |
| richards_super            | 38.0 ms                                                         | 42.0 ms: 1.11x slower                                                          |
| nbody                     | 81.9 ms                                                         | 91.4 ms: 1.12x slower                                                          |
| fannkuch                  | 293 ms                                                          | 328 ms: 1.12x slower                                                           |
| logging_silent            | 61.6 ns                                                         | 71.0 ns: 1.15x slower                                                          |
| generators                | 22.1 ms                                                         | 26.1 ms: 1.18x slower                                                          |
| Geometric mean            | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (10): tornado_http, html5lib, logging_format, python_startup, logging_simple, async_tree_cpu_io_mixed_tg, pprint_safe_repr, json, async_tree_io, pylint
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, dulwich_log, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown