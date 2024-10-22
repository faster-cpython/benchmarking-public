# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.05x faster
- HPT reliability: 97.62%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.89 sec: 1.04x slower                                                         |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 244 ms: 1.18x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 722 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 481 ms: 1.03x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 500 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 469 ms: 1.01x slower                                                           |
| async_generators           | 274 ms                                                          | 281 ms: 1.03x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| float          | 57.8 ms                                                         | 58.2 ms: 1.01x slower                                                          |
| nbody          | 81.9 ms                                                         | 90.9 ms: 1.11x slower                                                          |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 104 ms: 1.01x slower                                                           |
| regex_dna      | 117 ms                                                          | 122 ms: 1.04x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_effbot   | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.2 us: 1.04x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 106 ms: 1.03x faster                                                           |
| pickle_pure_python   | 238 us                                                          | 239 us: 1.00x slower                                                           |
| json_dumps           | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.77 sec: 1.02x slower                                                         |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| xml_etree_process    | 45.0 ms                                                         | 46.9 ms: 1.04x slower                                                          |
| xml_etree_generate   | 62.6 ms                                                         | 65.5 ms: 1.05x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 170 us: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.02x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                          |
| python_startup         | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 47.3 ms: 1.05x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.5 ms: 1.04x faster                                                          |
| django_template | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| mako            | 7.31 ms                                                         | 8.06 ms: 1.10x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 770 us: 13.19x faster                                                          |
| coverage                   | 333 ms                                                          | 52.0 ms: 6.40x faster                                                          |
| deepcopy                   | 307 us                                                          | 242 us: 1.27x faster                                                           |
| deepcopy_memo              | 26.2 us                                                         | 20.9 us: 1.25x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 244 ms: 1.18x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 722 ms: 1.17x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.51 us: 1.14x faster                                                          |
| async_tree_none_tg         | 219 ms                                                          | 193 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 274 ms: 1.10x faster                                                           |
| async_tree_none            | 246 ms                                                          | 223 ms: 1.10x faster                                                           |
| telco                      | 6.67 ms                                                         | 6.24 ms: 1.07x faster                                                          |
| genshi_xml                 | 49.5 ms                                                         | 47.3 ms: 1.05x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 71.9 ms: 1.05x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 21.5 ms: 1.04x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.2 us: 1.04x faster                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 992 us: 1.03x faster                                                           |
| json                       | 4.27 ms                                                         | 4.15 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 197 ms: 1.03x faster                                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.4 ms: 1.03x faster                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.02 ms: 1.03x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 106 ms: 1.03x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 481 ms: 1.03x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 56.8 ms: 1.02x faster                                                          |
| async_tree_io_tg           | 509 ms                                                          | 500 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| python_startup             | 24.3 ms                                                         | 23.8 ms: 1.02x faster                                                          |
| 2to3                       | 253 ms                                                          | 249 ms: 1.02x faster                                                           |
| pathlib                    | 89.4 ms                                                         | 88.1 ms: 1.02x faster                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 73.4 ms: 1.01x faster                                                          |
| pycparser                  | 869 ms                                                          | 858 ms: 1.01x faster                                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.28 ms: 1.01x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.78 us: 1.01x faster                                                          |
| go                         | 111 ms                                                          | 110 ms: 1.01x faster                                                           |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                                          |
| pickle_pure_python         | 238 us                                                          | 239 us: 1.00x slower                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 50.6 ms: 1.01x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| float                      | 57.8 ms                                                         | 58.2 ms: 1.01x slower                                                          |
| dulwich_log                | 49.7 ms                                                         | 50.1 ms: 1.01x slower                                                          |
| regex_compile              | 103 ms                                                          | 104 ms: 1.01x slower                                                           |
| sympy_str                  | 215 ms                                                          | 217 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 469 ms: 1.01x slower                                                           |
| django_template            | 32.7 ms                                                         | 33.3 ms: 1.02x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.77 sec: 1.02x slower                                                         |
| sqlglot_normalize          | 220 ms                                                          | 225 ms: 1.02x slower                                                           |
| sqlglot_optimize           | 42.5 ms                                                         | 43.5 ms: 1.02x slower                                                          |
| async_generators           | 274 ms                                                          | 281 ms: 1.03x slower                                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.33 sec: 1.03x slower                                                         |
| sympy_expand               | 375 ms                                                          | 385 ms: 1.03x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.5 ms: 1.04x slower                                                          |
| docutils                   | 1.82 sec                                                        | 1.89 sec: 1.04x slower                                                         |
| xml_etree_process          | 45.0 ms                                                         | 46.9 ms: 1.04x slower                                                          |
| regex_dna                  | 117 ms                                                          | 122 ms: 1.04x slower                                                           |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| comprehensions             | 12.7 us                                                         | 13.3 us: 1.04x slower                                                          |
| pyflate                    | 326 ms                                                          | 341 ms: 1.05x slower                                                           |
| chaos                      | 51.2 ms                                                         | 53.6 ms: 1.05x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 65.5 ms: 1.05x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 748 us: 1.05x slower                                                           |
| richards_super             | 38.0 ms                                                         | 39.9 ms: 1.05x slower                                                          |
| unpickle_pure_python       | 162 us                                                          | 170 us: 1.06x slower                                                           |
| fannkuch                   | 293 ms                                                          | 311 ms: 1.06x slower                                                           |
| regex_effbot               | 1.81 ms                                                         | 1.92 ms: 1.06x slower                                                          |
| hexiom                     | 4.64 ms                                                         | 4.95 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.10 ms: 1.07x slower                                                          |
| scimark_fft                | 206 ms                                                          | 221 ms: 1.07x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 98.4 ms: 1.07x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.58 ms: 1.07x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 68.4 ms: 1.08x slower                                                          |
| raytrace                   | 205 ms                                                          | 222 ms: 1.08x slower                                                           |
| richards                   | 33.8 ms                                                         | 36.7 ms: 1.09x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 148 us: 1.09x slower                                                           |
| spectral_norm              | 71.3 ms                                                         | 78.1 ms: 1.10x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 17.3 ms: 1.10x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.06 ms: 1.10x slower                                                          |
| nbody                      | 81.9 ms                                                         | 90.9 ms: 1.11x slower                                                          |
| generators                 | 22.1 ms                                                         | 25.7 ms: 1.16x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 72.6 ns: 1.18x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.05x faster                                                                   |

Benchmark hidden because not significant (10): tornado_http, mdp, logging_format, sympy_integrate, pprint_safe_repr, html5lib, sympy_sum, async_tree_io, meteor_contest, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 97.62% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown