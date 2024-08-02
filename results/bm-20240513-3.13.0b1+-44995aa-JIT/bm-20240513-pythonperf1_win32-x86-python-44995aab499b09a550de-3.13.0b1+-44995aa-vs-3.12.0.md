# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 244 ms: 1.15x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.95 ms: 1.30x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                          |
| tornado_http   | 105 ms                                                          | 97.4 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                            |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.7 ms: 2.37x faster                                                           |
| float          | 76.7 ms                                                         | 41.3 ms: 1.86x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.65x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 92.7 ms: 1.39x faster                                                           |
| regex_dna      | 127 ms                                                          | 117 ms: 1.09x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.38 sec: 1.59x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 136 us: 1.55x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 198 us: 1.45x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 40.5 ms: 1.32x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.0 ms: 1.29x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 56.0 ms: 1.29x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.69 ms: 1.11x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 102 ms: 1.10x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.89 us: 1.02x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle               | 7.79 us                                                         | 8.21 us: 1.05x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.64 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                                           |
| python_startup         | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.12x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                           |
| django_template | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.47x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 53.7 ms: 2.37x faster                                                           |
| spectral_norm              | 104 ms                                                          | 47.9 ms: 2.17x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 20.2 us: 1.90x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.31 ms: 1.88x faster                                                           |
| float                      | 76.7 ms                                                         | 41.3 ms: 1.86x faster                                                           |
| logging_silent             | 101 ns                                                          | 54.6 ns: 1.85x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.1 us: 1.73x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.9 ms: 1.67x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.3 ms: 1.66x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.38 ms: 1.62x faster                                                           |
| fannkuch                   | 354 ms                                                          | 219 ms: 1.61x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.38 sec: 1.59x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 136 us: 1.55x faster                                                            |
| scimark_fft                | 271 ms                                                          | 176 ms: 1.54x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.49 ms: 1.52x faster                                                           |
| raytrace                   | 308 ms                                                          | 208 ms: 1.48x faster                                                            |
| scimark_sor                | 130 ms                                                          | 88.1 ms: 1.47x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 198 us: 1.45x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.51 ms: 1.43x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 887 us: 1.41x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 49.2 ms: 1.41x faster                                                           |
| regex_compile              | 129 ms                                                          | 92.7 ms: 1.39x faster                                                           |
| pyflate                    | 424 ms                                                          | 305 ms: 1.39x faster                                                            |
| chaos                      | 69.4 ms                                                         | 50.2 ms: 1.38x faster                                                           |
| richards                   | 41.3 ms                                                         | 30.5 ms: 1.35x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.14 ms: 1.34x faster                                                           |
| richards_super             | 46.5 ms                                                         | 34.7 ms: 1.34x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 70.6 ms: 1.33x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.36 us: 1.32x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.8 ms: 1.32x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 40.5 ms: 1.32x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.15 sec: 1.31x faster                                                          |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.31x faster                                                            |
| logging_format             | 10.4 us                                                         | 7.97 us: 1.30x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.95 ms: 1.30x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 555 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 281 ms: 1.30x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.0 ms: 1.29x faster                                                           |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 56.0 ms: 1.29x faster                                                           |
| go                         | 137 ms                                                          | 108 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                            |
| pycparser                  | 978 ms                                                          | 778 ms: 1.26x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 74.7 ms: 1.25x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 71.4 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 450 ms: 1.21x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.66 us: 1.21x faster                                                           |
| deepcopy                   | 360 us                                                          | 299 us: 1.20x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 40.7 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 479 ms: 1.18x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.63 sec: 1.17x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.2 ms: 1.15x faster                                                           |
| sympy_str                  | 240 ms                                                          | 209 ms: 1.15x faster                                                            |
| 2to3                       | 280 ms                                                          | 244 ms: 1.15x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.6 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 990 us: 1.11x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.69 ms: 1.11x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 102 ms: 1.10x faster                                                            |
| regex_dna                  | 127 ms                                                          | 117 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| tornado_http               | 105 ms                                                          | 97.4 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.08x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                          |
| async_generators           | 313 ms                                                          | 297 ms: 1.06x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 86.9 ms: 1.05x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.94 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.04x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.89 us: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                           |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.76 ms: 1.05x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.21 us: 1.05x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 705 ms: 1.07x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.64 us: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 140 us: 1.11x slower                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 21.3 ms: 1.12x slower                                                           |
| python_startup             | 22.4 ms                                                         | 25.2 ms: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 755 us: 1.16x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 211 ms: 2.11x slower                                                            |
| coverage                   | 48.4 ms                                                         | 325 ms: 6.70x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa-JIT/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown