# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.08x faster
- HPT reliability: 94.17%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| docutils       | 1.82 sec                                                        | 2.02 sec: 1.11x slower                                                         |
| tornado_http   | 104 ms                                                          | 106 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x slower                                                                   |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 695 ms: 1.21x faster                                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 477 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 455 ms: 1.02x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.3 sec: 1.01x faster                                                         |
| async_tree_io              | 537 ms                                                          | 548 ms: 1.02x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 81.9 ms                                                         | 52.3 ms: 1.57x faster                                                          |
| float          | 57.8 ms                                                         | 43.0 ms: 1.34x faster                                                          |
| pidigits       | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 95.2 ms: 1.09x faster                                                          |
| regex_v8       | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| regex_dna      | 117 ms                                                          | 128 ms: 1.10x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 2.08 ms: 1.15x slower                                                          |
| Geometric mean | (ref)                                                           | 1.04x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pickle_pure_python   | 238 us                                                          | 213 us: 1.12x faster                                                           |
| tomli_loads          | 1.73 sec                                                        | 1.55 sec: 1.12x faster                                                         |
| unpickle_pure_python | 162 us                                                          | 146 us: 1.10x faster                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 57.7 ms: 1.08x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.09 ms: 1.04x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 63.0 ms: 1.03x faster                                                          |
| xml_etree_process    | 45.0 ms                                                         | 43.7 ms: 1.03x faster                                                          |
| json_loads           | 21.0 us                                                         | 20.9 us: 1.01x faster                                                          |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                           | 1.01x faster                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 7.31 ms                                                         | 5.49 ms: 1.33x faster                                                          |
| django_template | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                                          |
| genshi_text     | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| genshi_xml      | 49.5 ms                                                         | 53.3 ms: 1.08x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.03x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 766 us: 13.26x faster                                                          |
| coverage                   | 333 ms                                                          | 53.6 ms: 6.21x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 15.8 us: 1.66x faster                                                          |
| nbody                      | 81.9 ms                                                         | 52.3 ms: 1.57x faster                                                          |
| spectral_norm              | 71.3 ms                                                         | 47.7 ms: 1.49x faster                                                          |
| float                      | 57.8 ms                                                         | 43.0 ms: 1.34x faster                                                          |
| mako                       | 7.31 ms                                                         | 5.49 ms: 1.33x faster                                                          |
| fannkuch                   | 293 ms                                                          | 233 ms: 1.26x faster                                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 2.31 ms: 1.25x faster                                                          |
| scimark_fft                | 206 ms                                                          | 165 ms: 1.25x faster                                                           |
| pyflate                    | 326 ms                                                          | 261 ms: 1.25x faster                                                           |
| deepcopy                   | 307 us                                                          | 249 us: 1.23x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 695 ms: 1.21x faster                                                           |
| scimark_monte_carlo        | 50.3 ms                                                         | 41.6 ms: 1.21x faster                                                          |
| crypto_pyaes               | 58.2 ms                                                         | 48.3 ms: 1.20x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 250 ms: 1.15x faster                                                           |
| telco                      | 6.67 ms                                                         | 5.87 ms: 1.14x faster                                                          |
| deepcopy_reduce            | 2.85 us                                                         | 2.52 us: 1.13x faster                                                          |
| pickle_pure_python         | 238 us                                                          | 213 us: 1.12x faster                                                           |
| tomli_loads                | 1.73 sec                                                        | 1.55 sec: 1.12x faster                                                         |
| async_tree_none_tg         | 219 ms                                                          | 197 ms: 1.11x faster                                                           |
| unpickle_pure_python       | 162 us                                                          | 146 us: 1.10x faster                                                           |
| meteor_contest             | 77.0 ms                                                         | 70.1 ms: 1.10x faster                                                          |
| async_tree_memoization     | 302 ms                                                          | 277 ms: 1.09x faster                                                           |
| sqlglot_parse              | 1.05 ms                                                         | 965 us: 1.09x faster                                                           |
| async_tree_none            | 246 ms                                                          | 226 ms: 1.09x faster                                                           |
| regex_compile              | 103 ms                                                          | 95.2 ms: 1.09x faster                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 57.7 ms: 1.08x faster                                                          |
| comprehensions             | 12.7 us                                                         | 11.8 us: 1.08x faster                                                          |
| pycparser                  | 869 ms                                                          | 806 ms: 1.08x faster                                                           |
| pprint_safe_repr           | 644 ms                                                          | 599 ms: 1.08x faster                                                           |
| logging_silent             | 61.6 ns                                                         | 57.7 ns: 1.07x faster                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.23 ms: 1.05x faster                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.24 sec: 1.05x faster                                                         |
| json_dumps                 | 7.40 ms                                                         | 7.09 ms: 1.04x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 104 ms: 1.04x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 477 ms: 1.04x faster                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 63.0 ms: 1.03x faster                                                          |
| pidigits                   | 202 ms                                                          | 196 ms: 1.03x faster                                                           |
| xml_etree_process          | 45.0 ms                                                         | 43.7 ms: 1.03x faster                                                          |
| nqueens                    | 75.1 ms                                                         | 73.0 ms: 1.03x faster                                                          |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 455 ms: 1.02x faster                                                           |
| richards                   | 33.8 ms                                                         | 33.3 ms: 1.02x faster                                                          |
| python_startup             | 24.3 ms                                                         | 24.0 ms: 1.01x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.3 sec: 1.01x faster                                                         |
| go                         | 111 ms                                                          | 111 ms: 1.01x faster                                                           |
| json_loads                 | 21.0 us                                                         | 20.9 us: 1.01x faster                                                          |
| dulwich_log                | 49.7 ms                                                         | 50.2 ms: 1.01x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 15.9 ms: 1.02x slower                                                          |
| tornado_http               | 104 ms                                                          | 106 ms: 1.02x slower                                                           |
| 2to3                       | 253 ms                                                          | 258 ms: 1.02x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 4.73 ms: 1.02x slower                                                          |
| async_tree_io              | 537 ms                                                          | 548 ms: 1.02x slower                                                           |
| logging_format             | 8.57 us                                                         | 8.76 us: 1.02x slower                                                          |
| logging_simple             | 7.87 us                                                         | 8.06 us: 1.02x slower                                                          |
| mdp                        | 1.67 sec                                                        | 1.72 sec: 1.03x slower                                                         |
| richards_super             | 38.0 ms                                                         | 39.1 ms: 1.03x slower                                                          |
| chaos                      | 51.2 ms                                                         | 52.8 ms: 1.03x slower                                                          |
| sympy_str                  | 215 ms                                                          | 223 ms: 1.03x slower                                                           |
| sympy_sum                  | 108 ms                                                          | 112 ms: 1.04x slower                                                           |
| django_template            | 32.7 ms                                                         | 33.9 ms: 1.04x slower                                                          |
| bench_mp_pool              | 74.3 ms                                                         | 77.4 ms: 1.04x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 44.6 ms: 1.05x slower                                                          |
| scimark_sor                | 91.8 ms                                                         | 96.9 ms: 1.05x slower                                                          |
| genshi_text                | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| sympy_expand               | 375 ms                                                          | 401 ms: 1.07x slower                                                           |
| sympy_integrate            | 15.2 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| genshi_xml                 | 49.5 ms                                                         | 53.3 ms: 1.08x slower                                                          |
| sqlglot_normalize          | 220 ms                                                          | 239 ms: 1.09x slower                                                           |
| create_gc_cycles           | 713 us                                                          | 775 us: 1.09x slower                                                           |
| regex_dna                  | 117 ms                                                          | 128 ms: 1.10x slower                                                           |
| docutils                   | 1.82 sec                                                        | 2.02 sec: 1.11x slower                                                         |
| raytrace                   | 205 ms                                                          | 228 ms: 1.11x slower                                                           |
| pylint                     | 225 ms                                                          | 251 ms: 1.12x slower                                                           |
| deltablue                  | 2.41 ms                                                         | 2.75 ms: 1.14x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 2.08 ms: 1.15x slower                                                          |
| coroutines                 | 15.7 ms                                                         | 18.0 ms: 1.15x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 73.9 ms: 1.16x slower                                                          |
| async_generators           | 274 ms                                                          | 320 ms: 1.17x slower                                                           |
| typing_runtime_protocols   | 136 us                                                          | 161 us: 1.18x slower                                                           |
| generators                 | 22.1 ms                                                         | 28.5 ms: 1.29x slower                                                          |
| bench_thread_pool          | 1.02 ms                                                         | 3.09 ms: 3.02x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (6): html5lib, async_tree_io_tg, json, gc_traversal, python_startup_no_site, pathlib
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 94.17% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: unknown