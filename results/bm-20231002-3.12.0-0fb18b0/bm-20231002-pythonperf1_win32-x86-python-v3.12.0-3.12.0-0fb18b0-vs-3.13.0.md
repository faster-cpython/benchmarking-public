# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: windows-x86
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.13x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 253 ms                                                          | 280 ms: 1.11x slower                                            |
| chameleon      | 6.14 ms                                                         | 7.75 ms: 1.26x slower                                           |
| docutils       | 1.82 sec                                                        | 1.98 sec: 1.09x slower                                          |
| Geometric mean | (ref)                                                           | 1.11x slower                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                            |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.7 sec: 1.02x slower                                          |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 564 ms: 1.14x slower                                            |
| async_generators           | 274 ms                                                          | 313 ms: 1.14x slower                                            |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 546 ms: 1.18x slower                                            |
| async_tree_memoization     | 302 ms                                                          | 364 ms: 1.20x slower                                            |
| async_tree_none            | 246 ms                                                          | 298 ms: 1.21x slower                                            |
| async_tree_memoization_tg  | 287 ms                                                          | 350 ms: 1.22x slower                                            |
| async_tree_none_tg         | 219 ms                                                          | 278 ms: 1.27x slower                                            |
| async_tree_io              | 537 ms                                                          | 693 ms: 1.29x slower                                            |
| async_tree_io_tg           | 509 ms                                                          | 677 ms: 1.33x slower                                            |
| coroutines                 | 15.7 ms                                                         | 20.9 ms: 1.33x slower                                           |
| Geometric mean             | (ref)                                                           | 1.17x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 202 ms                                                          | 199 ms: 1.01x faster                                            |
| float          | 57.8 ms                                                         | 76.7 ms: 1.33x slower                                           |
| nbody          | 81.9 ms                                                         | 127 ms: 1.55x slower                                            |
| Geometric mean | (ref)                                                           | 1.27x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                         | 15.0 ms: 1.04x faster                                           |
| regex_dna      | 117 ms                                                          | 127 ms: 1.09x slower                                            |
| regex_effbot   | 1.81 ms                                                         | 2.04 ms: 1.12x slower                                           |
| regex_compile  | 103 ms                                                          | 129 ms: 1.25x slower                                            |
| Geometric mean | (ref)                                                           | 1.10x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_dict          | 21.7 us                                                         | 19.9 us: 1.09x faster                                           |
| unpickle             | 10.5 us                                                         | 9.71 us: 1.09x faster                                           |
| pickle               | 8.42 us                                                         | 7.79 us: 1.08x faster                                           |
| unpickle_list        | 3.09 us                                                         | 2.95 us: 1.05x faster                                           |
| json_loads           | 21.0 us                                                         | 20.4 us: 1.03x faster                                           |
| pickle_list          | 3.40 us                                                         | 3.37 us: 1.01x faster                                           |
| xml_etree_parse      | 109 ms                                                          | 113 ms: 1.04x slower                                            |
| xml_etree_generate   | 62.6 ms                                                         | 72.1 ms: 1.15x slower                                           |
| xml_etree_process    | 45.0 ms                                                         | 53.2 ms: 1.18x slower                                           |
| xml_etree_iterparse  | 65.1 ms                                                         | 77.6 ms: 1.19x slower                                           |
| pickle_pure_python   | 238 us                                                          | 286 us: 1.20x slower                                            |
| tomli_loads          | 1.73 sec                                                        | 2.20 sec: 1.27x slower                                          |
| unpickle_pure_python | 162 us                                                          | 210 us: 1.30x slower                                            |
| Geometric mean       | (ref)                                                           | 1.06x slower                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 24.3 ms                                                         | 22.4 ms: 1.08x faster                                           |
| python_startup_no_site | 19.9 ms                                                         | 19.1 ms: 1.05x faster                                           |
| Geometric mean         | (ref)                                                           | 1.06x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                           |
| mako            | 7.31 ms                                                         | 9.96 ms: 1.36x slower                                           |
| Geometric mean  | (ref)                                                           | 1.24x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| coverage                   | 333 ms                                                          | 48.4 ms: 6.87x faster                                           |
| sqlglot_normalize          | 220 ms                                                          | 100 ms: 2.19x faster                                            |
| asyncio_tcp                | 842 ms                                                          | 662 ms: 1.27x faster                                            |
| telco                      | 6.67 ms                                                         | 5.51 ms: 1.21x faster                                           |
| create_gc_cycles           | 713 us                                                          | 652 us: 1.09x faster                                            |
| pickle_dict                | 21.7 us                                                         | 19.9 us: 1.09x faster                                           |
| unpickle                   | 10.5 us                                                         | 9.71 us: 1.09x faster                                           |
| python_startup             | 24.3 ms                                                         | 22.4 ms: 1.08x faster                                           |
| pickle                     | 8.42 us                                                         | 7.79 us: 1.08x faster                                           |
| typing_runtime_protocols   | 136 us                                                          | 126 us: 1.08x faster                                            |
| unpickle_list              | 3.09 us                                                         | 2.95 us: 1.05x faster                                           |
| python_startup_no_site     | 19.9 ms                                                         | 19.1 ms: 1.05x faster                                           |
| regex_v8                   | 15.6 ms                                                         | 15.0 ms: 1.04x faster                                           |
| json_loads                 | 21.0 us                                                         | 20.4 us: 1.03x faster                                           |
| pidigits                   | 202 ms                                                          | 199 ms: 1.01x faster                                            |
| pickle_list                | 3.40 us                                                         | 3.37 us: 1.01x faster                                           |
| gc_traversal               | 1.45 ms                                                         | 1.44 ms: 1.01x faster                                           |
| bench_mp_pool              | 74.3 ms                                                         | 75.4 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 17.4 sec                                                        | 17.7 sec: 1.02x slower                                          |
| pathlib                    | 89.4 ms                                                         | 91.4 ms: 1.02x slower                                           |
| xml_etree_parse            | 109 ms                                                          | 113 ms: 1.04x slower                                            |
| sqlite_synth               | 1.97 us                                                         | 2.07 us: 1.05x slower                                           |
| sympy_expand               | 375 ms                                                          | 398 ms: 1.06x slower                                            |
| bench_thread_pool          | 1.02 ms                                                         | 1.10 ms: 1.08x slower                                           |
| regex_dna                  | 117 ms                                                          | 127 ms: 1.09x slower                                            |
| docutils                   | 1.82 sec                                                        | 1.98 sec: 1.09x slower                                          |
| 2to3                       | 253 ms                                                          | 280 ms: 1.11x slower                                            |
| sympy_str                  | 215 ms                                                          | 240 ms: 1.11x slower                                            |
| pprint_safe_repr           | 644 ms                                                          | 721 ms: 1.12x slower                                            |
| regex_effbot               | 1.81 ms                                                         | 2.04 ms: 1.12x slower                                           |
| pycparser                  | 869 ms                                                          | 978 ms: 1.13x slower                                            |
| meteor_contest             | 77.0 ms                                                         | 86.9 ms: 1.13x slower                                           |
| django_template            | 32.7 ms                                                         | 36.9 ms: 1.13x slower                                           |
| deepcopy_reduce            | 2.85 us                                                         | 3.23 us: 1.13x slower                                           |
| sympy_sum                  | 108 ms                                                          | 123 ms: 1.14x slower                                            |
| async_tree_cpu_io_mixed    | 494 ms                                                          | 564 ms: 1.14x slower                                            |
| sqlglot_optimize           | 42.5 ms                                                         | 48.5 ms: 1.14x slower                                           |
| mdp                        | 1.67 sec                                                        | 1.91 sec: 1.14x slower                                          |
| async_generators           | 274 ms                                                          | 313 ms: 1.14x slower                                            |
| xml_etree_generate         | 62.6 ms                                                         | 72.1 ms: 1.15x slower                                           |
| sympy_integrate            | 15.2 ms                                                         | 17.5 ms: 1.16x slower                                           |
| pprint_pformat             | 1.30 sec                                                        | 1.50 sec: 1.16x slower                                          |
| deepcopy                   | 307 us                                                          | 360 us: 1.17x slower                                            |
| dulwich_log                | 49.7 ms                                                         | 58.5 ms: 1.18x slower                                           |
| async_tree_cpu_io_mixed_tg | 464 ms                                                          | 546 ms: 1.18x slower                                            |
| xml_etree_process          | 45.0 ms                                                         | 53.2 ms: 1.18x slower                                           |
| sqlglot_transpile          | 1.29 ms                                                         | 1.53 ms: 1.18x slower                                           |
| sqlglot_parse              | 1.05 ms                                                         | 1.25 ms: 1.19x slower                                           |
| crypto_pyaes               | 58.2 ms                                                         | 69.2 ms: 1.19x slower                                           |
| xml_etree_iterparse        | 65.1 ms                                                         | 77.6 ms: 1.19x slower                                           |
| pickle_pure_python         | 238 us                                                          | 286 us: 1.20x slower                                            |
| async_tree_memoization     | 302 ms                                                          | 364 ms: 1.20x slower                                            |
| fannkuch                   | 293 ms                                                          | 354 ms: 1.21x slower                                            |
| async_tree_none            | 246 ms                                                          | 298 ms: 1.21x slower                                            |
| logging_format             | 8.57 us                                                         | 10.4 us: 1.21x slower                                           |
| async_tree_memoization_tg  | 287 ms                                                          | 350 ms: 1.22x slower                                            |
| richards                   | 33.8 ms                                                         | 41.3 ms: 1.22x slower                                           |
| richards_super             | 38.0 ms                                                         | 46.5 ms: 1.22x slower                                           |
| go                         | 111 ms                                                          | 137 ms: 1.23x slower                                            |
| logging_simple             | 7.87 us                                                         | 9.75 us: 1.24x slower                                           |
| nqueens                    | 75.1 ms                                                         | 93.7 ms: 1.25x slower                                           |
| regex_compile              | 103 ms                                                          | 129 ms: 1.25x slower                                            |
| chameleon                  | 6.14 ms                                                         | 7.75 ms: 1.26x slower                                           |
| tomli_loads                | 1.73 sec                                                        | 2.20 sec: 1.27x slower                                          |
| async_tree_none_tg         | 219 ms                                                          | 278 ms: 1.27x slower                                            |
| async_tree_io              | 537 ms                                                          | 693 ms: 1.29x slower                                            |
| unpickle_pure_python       | 162 us                                                          | 210 us: 1.30x slower                                            |
| pyflate                    | 326 ms                                                          | 424 ms: 1.30x slower                                            |
| scimark_fft                | 206 ms                                                          | 271 ms: 1.31x slower                                            |
| scimark_monte_carlo        | 50.3 ms                                                         | 66.4 ms: 1.32x slower                                           |
| float                      | 57.8 ms                                                         | 76.7 ms: 1.33x slower                                           |
| scimark_sparse_mat_mult    | 2.90 ms                                                         | 3.86 ms: 1.33x slower                                           |
| async_tree_io_tg           | 509 ms                                                          | 677 ms: 1.33x slower                                            |
| coroutines                 | 15.7 ms                                                         | 20.9 ms: 1.33x slower                                           |
| chaos                      | 51.2 ms                                                         | 69.4 ms: 1.36x slower                                           |
| mako                       | 7.31 ms                                                         | 9.96 ms: 1.36x slower                                           |
| scimark_sor                | 91.8 ms                                                         | 130 ms: 1.41x slower                                            |
| unpack_sequence            | 42.9 ns                                                         | 62.5 ns: 1.45x slower                                           |
| spectral_norm              | 71.3 ms                                                         | 104 ms: 1.46x slower                                            |
| deepcopy_memo              | 26.2 us                                                         | 38.4 us: 1.47x slower                                           |
| scimark_lu                 | 63.5 ms                                                         | 93.2 ms: 1.47x slower                                           |
| hexiom                     | 4.64 ms                                                         | 6.82 ms: 1.47x slower                                           |
| deltablue                  | 2.41 ms                                                         | 3.58 ms: 1.49x slower                                           |
| raytrace                   | 205 ms                                                          | 308 ms: 1.50x slower                                            |
| comprehensions             | 12.7 us                                                         | 19.2 us: 1.51x slower                                           |
| nbody                      | 81.9 ms                                                         | 127 ms: 1.55x slower                                            |
| logging_silent             | 61.6 ns                                                         | 101 ns: 1.64x slower                                            |
| generators                 | 22.1 ms                                                         | 38.5 ms: 1.74x slower                                           |
| Geometric mean             | (ref)                                                           | 1.13x slower                                                    |

Benchmark hidden because not significant (3): json, json_dumps, tornado_http
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.15x
- 95% likely to have a slowdown of 1.14x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: unknown