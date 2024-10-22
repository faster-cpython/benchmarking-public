# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: windows-x86
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 253 ms: 1.11x faster                                            |
| chameleon      | 7.75 ms                                                         | 6.14 ms: 1.26x faster                                           |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                          |
| Geometric mean | (ref)                                                           | 1.11x faster                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                            |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 219 ms: 1.27x faster                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 287 ms: 1.22x faster                                            |
| async_tree_none            | 298 ms                                                          | 246 ms: 1.21x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 302 ms: 1.20x faster                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 81.9 ms: 1.55x faster                                           |
| float          | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                           | 1.27x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                            |
| regex_effbot   | 2.04 ms                                                         | 1.81 ms: 1.12x faster                                           |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                            |
| regex_v8       | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 162 us: 1.30x faster                                            |
| tomli_loads          | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                          |
| pickle_pure_python   | 286 us                                                          | 238 us: 1.20x faster                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                           |
| xml_etree_process    | 53.2 ms                                                         | 45.0 ms: 1.18x faster                                           |
| xml_etree_generate   | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                           |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                            |
| pickle_list          | 3.37 us                                                         | 3.40 us: 1.01x slower                                           |
| json_loads           | 20.4 us                                                         | 21.0 us: 1.03x slower                                           |
| unpickle_list        | 2.95 us                                                         | 3.09 us: 1.05x slower                                           |
| pickle               | 7.79 us                                                         | 8.42 us: 1.08x slower                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.09x slower                                           |
| pickle_dict          | 19.9 us                                                         | 21.7 us: 1.09x slower                                           |
| Geometric mean       | (ref)                                                           | 1.06x faster                                                    |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                           |
| python_startup         | 22.4 ms                                                         | 24.3 ms: 1.08x slower                                           |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.31 ms: 1.36x faster                                           |
| django_template | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                           |
| Geometric mean  | (ref)                                                           | 1.24x faster                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:---------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.1 ms: 1.74x faster                                           |
| logging_silent             | 101 ns                                                          | 61.6 ns: 1.64x faster                                           |
| nbody                      | 127 ms                                                          | 81.9 ms: 1.55x faster                                           |
| comprehensions             | 19.2 us                                                         | 12.7 us: 1.51x faster                                           |
| raytrace                   | 308 ms                                                          | 205 ms: 1.50x faster                                            |
| deltablue                  | 3.58 ms                                                         | 2.41 ms: 1.49x faster                                           |
| hexiom                     | 6.82 ms                                                         | 4.64 ms: 1.47x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 63.5 ms: 1.47x faster                                           |
| deepcopy_memo              | 38.4 us                                                         | 26.2 us: 1.47x faster                                           |
| spectral_norm              | 104 ms                                                          | 71.3 ms: 1.46x faster                                           |
| unpack_sequence            | 62.5 ns                                                         | 42.9 ns: 1.45x faster                                           |
| scimark_sor                | 130 ms                                                          | 91.8 ms: 1.41x faster                                           |
| mako                       | 9.96 ms                                                         | 7.31 ms: 1.36x faster                                           |
| chaos                      | 69.4 ms                                                         | 51.2 ms: 1.36x faster                                           |
| coroutines                 | 20.9 ms                                                         | 15.7 ms: 1.33x faster                                           |
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.90 ms: 1.33x faster                                           |
| float                      | 76.7 ms                                                         | 57.8 ms: 1.33x faster                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 50.3 ms: 1.32x faster                                           |
| scimark_fft                | 271 ms                                                          | 206 ms: 1.31x faster                                            |
| pyflate                    | 424 ms                                                          | 326 ms: 1.30x faster                                            |
| unpickle_pure_python       | 210 us                                                          | 162 us: 1.30x faster                                            |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                            |
| async_tree_none_tg         | 278 ms                                                          | 219 ms: 1.27x faster                                            |
| tomli_loads                | 2.20 sec                                                        | 1.73 sec: 1.27x faster                                          |
| chameleon                  | 7.75 ms                                                         | 6.14 ms: 1.26x faster                                           |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                            |
| nqueens                    | 93.7 ms                                                         | 75.1 ms: 1.25x faster                                           |
| logging_simple             | 9.75 us                                                         | 7.87 us: 1.24x faster                                           |
| go                         | 137 ms                                                          | 111 ms: 1.23x faster                                            |
| richards_super             | 46.5 ms                                                         | 38.0 ms: 1.22x faster                                           |
| richards                   | 41.3 ms                                                         | 33.8 ms: 1.22x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 287 ms: 1.22x faster                                            |
| logging_format             | 10.4 us                                                         | 8.57 us: 1.21x faster                                           |
| async_tree_none            | 298 ms                                                          | 246 ms: 1.21x faster                                            |
| fannkuch                   | 354 ms                                                          | 293 ms: 1.21x faster                                            |
| async_tree_memoization     | 364 ms                                                          | 302 ms: 1.20x faster                                            |
| pickle_pure_python         | 286 us                                                          | 238 us: 1.20x faster                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.1 ms: 1.19x faster                                           |
| crypto_pyaes               | 69.2 ms                                                         | 58.2 ms: 1.19x faster                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.19x faster                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.18x faster                                           |
| xml_etree_process          | 53.2 ms                                                         | 45.0 ms: 1.18x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 464 ms: 1.18x faster                                            |
| dulwich_log                | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                           |
| deepcopy                   | 360 us                                                          | 307 us: 1.17x faster                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.30 sec: 1.16x faster                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.2 ms: 1.16x faster                                           |
| xml_etree_generate         | 72.1 ms                                                         | 62.6 ms: 1.15x faster                                           |
| async_generators           | 313 ms                                                          | 274 ms: 1.14x faster                                            |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 42.5 ms: 1.14x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 494 ms: 1.14x faster                                            |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.85 us: 1.13x faster                                           |
| django_template            | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                           |
| meteor_contest             | 86.9 ms                                                         | 77.0 ms: 1.13x faster                                           |
| pycparser                  | 978 ms                                                          | 869 ms: 1.13x faster                                            |
| regex_effbot               | 2.04 ms                                                         | 1.81 ms: 1.12x faster                                           |
| pprint_safe_repr           | 721 ms                                                          | 644 ms: 1.12x faster                                            |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.11x faster                                            |
| 2to3                       | 280 ms                                                          | 253 ms: 1.11x faster                                            |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                          |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                           |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                            |
| sqlite_synth               | 2.07 us                                                         | 1.97 us: 1.05x faster                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                            |
| pathlib                    | 91.4 ms                                                         | 89.4 ms: 1.02x faster                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.4 sec: 1.02x faster                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.3 ms: 1.01x faster                                           |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                           |
| pickle_list                | 3.37 us                                                         | 3.40 us: 1.01x slower                                           |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                            |
| json_loads                 | 20.4 us                                                         | 21.0 us: 1.03x slower                                           |
| regex_v8                   | 15.0 ms                                                         | 15.6 ms: 1.04x slower                                           |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                           |
| unpickle_list              | 2.95 us                                                         | 3.09 us: 1.05x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 136 us: 1.08x slower                                            |
| pickle                     | 7.79 us                                                         | 8.42 us: 1.08x slower                                           |
| python_startup             | 22.4 ms                                                         | 24.3 ms: 1.08x slower                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.09x slower                                           |
| pickle_dict                | 19.9 us                                                         | 21.7 us: 1.09x slower                                           |
| create_gc_cycles           | 652 us                                                          | 713 us: 1.09x slower                                            |
| telco                      | 5.51 ms                                                         | 6.67 ms: 1.21x slower                                           |
| asyncio_tcp                | 662 ms                                                          | 842 ms: 1.27x slower                                            |
| sqlglot_normalize          | 100 ms                                                          | 220 ms: 2.19x slower                                            |
| coverage                   | 48.4 ms                                                         | 333 ms: 6.87x slower                                            |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                    |

Benchmark hidden because not significant (3): tornado_http, json_dumps, json
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1_win32-x86-python-v3.13.0-3.13.0-60403a5.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown