# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.03x faster
- HPT reliability: 99.66%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| docutils       | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| html5lib       | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| Geometric mean | (ref)                                                           | 1.00x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 217 ms: 1.13x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 745 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 460 ms: 1.07x faster                                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                           |
| async_tree_io_tg           | 509 ms                                                          | 516 ms: 1.01x slower                                                           |
| async_generators           | 274 ms                                                          | 299 ms: 1.09x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 201 ms: 1.01x faster                                                           |
| float          | 57.8 ms                                                         | 60.8 ms: 1.05x slower                                                          |
| nbody          | 81.9 ms                                                         | 96.8 ms: 1.18x slower                                                          |
| Geometric mean | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 103 ms                                                          | 107 ms: 1.04x slower                                                           |
| regex_v8       | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| regex_dna      | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| regex_effbot   | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| xml_etree_parse      | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                          |
| unpickle_pure_python | 162 us                                                          | 171 us: 1.06x slower                                                           |
| pickle_pure_python   | 238 us                                                          | 254 us: 1.07x slower                                                           |
| xml_etree_generate   | 62.6 ms                                                         | 67.9 ms: 1.08x slower                                                          |
| tomli_loads          | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| xml_etree_process    | 45.0 ms                                                         | 49.3 ms: 1.09x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.04x slower                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| genshi_xml      | 49.5 ms                                                         | 46.5 ms: 1.06x faster                                                          |
| genshi_text     | 22.4 ms                                                         | 21.6 ms: 1.04x faster                                                          |
| django_template | 32.7 ms                                                         | 32.3 ms: 1.01x faster                                                          |
| mako            | 7.31 ms                                                         | 8.38 ms: 1.15x slower                                                          |
| Geometric mean  | (ref)                                                           | 1.01x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| thrift                     | 10.1 ms                                                         | 735 us: 13.80x faster                                                          |
| coverage                   | 333 ms                                                          | 51.5 ms: 6.46x faster                                                          |
| deepcopy                   | 307 us                                                          | 247 us: 1.24x faster                                                           |
| deepcopy_reduce            | 2.85 us                                                         | 2.43 us: 1.17x faster                                                          |
| deepcopy_memo              | 26.2 us                                                         | 22.5 us: 1.17x faster                                                          |
| async_tree_memoization_tg  | 287 ms                                                          | 249 ms: 1.15x faster                                                           |
| async_tree_none            | 246 ms                                                          | 217 ms: 1.13x faster                                                           |
| asyncio_tcp                | 842 ms                                                          | 745 ms: 1.13x faster                                                           |
| async_tree_memoization     | 302 ms                                                          | 273 ms: 1.11x faster                                                           |
| async_tree_none_tg         | 219 ms                                                          | 198 ms: 1.10x faster                                                           |
| go                         | 111 ms                                                          | 102 ms: 1.09x faster                                                           |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 460 ms: 1.07x faster                                                           |
| genshi_xml                 | 49.5 ms                                                         | 46.5 ms: 1.06x faster                                                          |
| genshi_text                | 22.4 ms                                                         | 21.6 ms: 1.04x faster                                                          |
| html5lib                   | 48.3 ms                                                         | 46.5 ms: 1.04x faster                                                          |
| json_loads                 | 21.0 us                                                         | 20.4 us: 1.03x faster                                                          |
| gc_traversal               | 1.45 ms                                                         | 1.42 ms: 1.02x faster                                                          |
| pathlib                    | 89.4 ms                                                         | 87.8 ms: 1.02x faster                                                          |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.1 sec: 1.02x faster                                                         |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 456 ms: 1.02x faster                                                           |
| django_template            | 32.7 ms                                                         | 32.3 ms: 1.01x faster                                                          |
| xml_etree_parse            | 109 ms                                                          | 108 ms: 1.01x faster                                                           |
| sympy_sum                  | 108 ms                                                          | 107 ms: 1.01x faster                                                           |
| pidigits                   | 202 ms                                                          | 201 ms: 1.01x faster                                                           |
| 2to3                       | 253 ms                                                          | 251 ms: 1.01x faster                                                           |
| crypto_pyaes               | 58.2 ms                                                         | 57.8 ms: 1.01x faster                                                          |
| logging_simple             | 7.87 us                                                         | 7.92 us: 1.01x slower                                                          |
| sqlglot_optimize           | 42.5 ms                                                         | 42.8 ms: 1.01x slower                                                          |
| sympy_str                  | 215 ms                                                          | 217 ms: 1.01x slower                                                           |
| bench_mp_pool              | 74.3 ms                                                         | 74.9 ms: 1.01x slower                                                          |
| pycparser                  | 869 ms                                                          | 878 ms: 1.01x slower                                                           |
| sympy_expand               | 375 ms                                                          | 379 ms: 1.01x slower                                                           |
| pprint_safe_repr           | 644 ms                                                          | 651 ms: 1.01x slower                                                           |
| nqueens                    | 75.1 ms                                                         | 76.1 ms: 1.01x slower                                                          |
| async_tree_io_tg           | 509 ms                                                          | 516 ms: 1.01x slower                                                           |
| sqlglot_normalize          | 220 ms                                                          | 223 ms: 1.02x slower                                                           |
| mdp                        | 1.67 sec                                                        | 1.70 sec: 1.02x slower                                                         |
| docutils                   | 1.82 sec                                                        | 1.86 sec: 1.02x slower                                                         |
| sympy_integrate            | 15.2 ms                                                         | 15.5 ms: 1.02x slower                                                          |
| sqlglot_parse              | 1.05 ms                                                         | 1.08 ms: 1.03x slower                                                          |
| sqlglot_transpile          | 1.29 ms                                                         | 1.33 ms: 1.03x slower                                                          |
| pprint_pformat             | 1.30 sec                                                        | 1.34 sec: 1.03x slower                                                         |
| telco                      | 6.67 ms                                                         | 6.92 ms: 1.04x slower                                                          |
| regex_compile              | 103 ms                                                          | 107 ms: 1.04x slower                                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 67.9 ms: 1.04x slower                                                          |
| regex_v8                   | 15.6 ms                                                         | 16.3 ms: 1.04x slower                                                          |
| pylint                     | 225 ms                                                          | 235 ms: 1.04x slower                                                           |
| float                      | 57.8 ms                                                         | 60.8 ms: 1.05x slower                                                          |
| create_gc_cycles           | 713 us                                                          | 751 us: 1.05x slower                                                           |
| regex_dna                  | 117 ms                                                          | 123 ms: 1.06x slower                                                           |
| unpickle_pure_python       | 162 us                                                          | 171 us: 1.06x slower                                                           |
| comprehensions             | 12.7 us                                                         | 13.5 us: 1.06x slower                                                          |
| spectral_norm              | 71.3 ms                                                         | 75.8 ms: 1.06x slower                                                          |
| regex_effbot               | 1.81 ms                                                         | 1.93 ms: 1.07x slower                                                          |
| chaos                      | 51.2 ms                                                         | 54.6 ms: 1.07x slower                                                          |
| meteor_contest             | 77.0 ms                                                         | 82.2 ms: 1.07x slower                                                          |
| pickle_pure_python         | 238 us                                                          | 254 us: 1.07x slower                                                           |
| scimark_sor                | 91.8 ms                                                         | 98.5 ms: 1.07x slower                                                          |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.12 ms: 1.07x slower                                                          |
| xml_etree_generate         | 62.6 ms                                                         | 67.9 ms: 1.08x slower                                                          |
| tomli_loads                | 1.73 sec                                                        | 1.89 sec: 1.09x slower                                                         |
| scimark_monte_carlo        | 50.3 ms                                                         | 55.0 ms: 1.09x slower                                                          |
| async_generators           | 274 ms                                                          | 299 ms: 1.09x slower                                                           |
| pyflate                    | 326 ms                                                          | 357 ms: 1.09x slower                                                           |
| xml_etree_process          | 45.0 ms                                                         | 49.3 ms: 1.09x slower                                                          |
| deltablue                  | 2.41 ms                                                         | 2.64 ms: 1.10x slower                                                          |
| scimark_lu                 | 63.5 ms                                                         | 70.2 ms: 1.11x slower                                                          |
| typing_runtime_protocols   | 136 us                                                          | 151 us: 1.11x slower                                                           |
| coroutines                 | 15.7 ms                                                         | 17.5 ms: 1.12x slower                                                          |
| fannkuch                   | 293 ms                                                          | 328 ms: 1.12x slower                                                           |
| hexiom                     | 4.64 ms                                                         | 5.27 ms: 1.14x slower                                                          |
| richards                   | 33.8 ms                                                         | 38.5 ms: 1.14x slower                                                          |
| richards_super             | 38.0 ms                                                         | 43.3 ms: 1.14x slower                                                          |
| mako                       | 7.31 ms                                                         | 8.38 ms: 1.15x slower                                                          |
| raytrace                   | 205 ms                                                          | 236 ms: 1.15x slower                                                           |
| scimark_fft                | 206 ms                                                          | 241 ms: 1.17x slower                                                           |
| nbody                      | 81.9 ms                                                         | 96.8 ms: 1.18x slower                                                          |
| logging_silent             | 61.6 ns                                                         | 74.7 ns: 1.21x slower                                                          |
| generators                 | 22.1 ms                                                         | 27.7 ms: 1.25x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.03x faster                                                                   |

Benchmark hidden because not significant (9): json, python_startup, logging_format, dulwich_log, async_tree_io, json_dumps, python_startup_no_site, bench_thread_pool, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: chameleon, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.66% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown