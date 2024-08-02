# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 236 ms: 1.18x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.72 ms: 1.36x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.6 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 76.2 ms: 1.67x faster                                                           |
| float          | 76.7 ms                                                         | 52.4 ms: 1.46x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 151 us: 1.39x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 218 us: 1.31x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 41.4 ms: 1.28x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 58.5 ms: 1.23x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.11x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.87 ms: 1.08x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                           |
| pickle               | 7.79 us                                                         | 8.12 us: 1.04x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.07 us: 1.04x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.52 us: 1.05x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.6 us: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.2 ms: 1.05x faster                                                           |
| python_startup         | 22.4 ms                                                         | 22.1 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.99 ms: 1.42x faster                                                           |
| django_template | 36.9 ms                                                         | 31.0 ms: 1.19x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.30x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.2 ms: 1.81x faster                                                           |
| logging_silent             | 101 ns                                                          | 58.0 ns: 1.74x faster                                                           |
| raytrace                   | 308 ms                                                          | 182 ms: 1.69x faster                                                            |
| nbody                      | 127 ms                                                          | 76.2 ms: 1.67x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.7 us: 1.64x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.63x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.22 ms: 1.62x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 59.2 ms: 1.58x faster                                                           |
| scimark_sor                | 130 ms                                                          | 82.6 ms: 1.57x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.43 ms: 1.54x faster                                                           |
| spectral_norm              | 104 ms                                                          | 68.0 ms: 1.53x faster                                                           |
| float                      | 76.7 ms                                                         | 52.4 ms: 1.46x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.6 ms: 1.46x faster                                                           |
| mako                       | 9.96 ms                                                         | 6.99 ms: 1.42x faster                                                           |
| chaos                      | 69.4 ms                                                         | 49.2 ms: 1.41x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 151 us: 1.39x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                            |
| pyflate                    | 424 ms                                                          | 307 ms: 1.38x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.82 ms: 1.37x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                                          |
| chameleon                  | 7.75 ms                                                         | 5.72 ms: 1.36x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 69.2 ms: 1.35x faster                                                           |
| fannkuch                   | 354 ms                                                          | 265 ms: 1.33x faster                                                            |
| go                         | 137 ms                                                          | 104 ms: 1.33x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 276 ms: 1.32x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 218 us: 1.31x faster                                                            |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| richards                   | 41.3 ms                                                         | 31.7 ms: 1.30x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.0 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                            |
| richards_super             | 46.5 ms                                                         | 35.7 ms: 1.30x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 959 us: 1.30x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.28x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 41.4 ms: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                            |
| logging_simple             | 9.75 us                                                         | 7.63 us: 1.28x faster                                                           |
| deepcopy                   | 360 us                                                          | 282 us: 1.28x faster                                                            |
| regex_compile              | 129 ms                                                          | 101 ms: 1.28x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 54.9 ms: 1.26x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.30 us: 1.25x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 58.5 ms: 1.23x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.2 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| pycparser                  | 978 ms                                                          | 798 ms: 1.23x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 40.2 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 468 ms: 1.20x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.24 sec: 1.20x faster                                                          |
| async_generators           | 313 ms                                                          | 261 ms: 1.20x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 14.7 ms: 1.20x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.70 us: 1.19x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.0 ms: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 73.3 ms: 1.19x faster                                                           |
| 2to3                       | 280 ms                                                          | 236 ms: 1.18x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 610 ms: 1.18x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.65 sec: 1.16x faster                                                          |
| sympy_str                  | 240 ms                                                          | 208 ms: 1.15x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 987 us: 1.12x faster                                                            |
| tornado_http               | 105 ms                                                          | 94.6 ms: 1.11x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.11x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.10x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 6.87 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.08x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 71.2 ms: 1.06x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 18.2 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.7 ms: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| python_startup             | 22.4 ms                                                         | 22.1 ms: 1.01x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.6 us: 1.01x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.12 us: 1.04x slower                                                           |
| unpickle_list              | 2.95 us                                                         | 3.07 us: 1.04x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.52 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.6 us: 1.09x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.01 ms: 1.09x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 138 us: 1.09x slower                                                            |
| asyncio_tcp                | 662 ms                                                          | 734 ms: 1.11x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 737 us: 1.13x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 209 ms: 2.09x slower                                                            |
| coverage                   | 48.4 ms                                                         | 310 ms: 6.39x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (1): json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown