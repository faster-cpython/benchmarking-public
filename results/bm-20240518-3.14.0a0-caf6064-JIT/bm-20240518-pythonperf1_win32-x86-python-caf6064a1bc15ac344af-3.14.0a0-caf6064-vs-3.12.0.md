# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: windows-x86
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 247 ms: 1.13x faster                                                           |
| chameleon      | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                                          |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.8 ms: 1.10x faster                                                          |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                           |
| async_tree_none            | 298 ms                                                          | 229 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.3 ms: 2.38x faster                                                          |
| float          | 76.7 ms                                                         | 40.6 ms: 1.89x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.66x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 90.7 ms: 1.42x faster                                                          |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 135 us: 1.55x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 199 us: 1.43x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 39.9 ms: 1.33x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 54.9 ms: 1.31x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.88 us: 1.02x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| pickle               | 7.79 us                                                         | 8.16 us: 1.05x slower                                                          |
| pickle_dict          | 19.9 us                                                         | 20.9 us: 1.05x slower                                                          |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| pickle_list          | 3.37 us                                                         | 3.62 us: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.08x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.30 ms: 1.88x faster                                                          |
| django_template | 36.9 ms                                                         | 30.9 ms: 1.20x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.50x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 53.3 ms: 2.38x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.5 ms: 2.19x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 20.3 us: 1.89x faster                                                          |
| float                      | 76.7 ms                                                         | 40.6 ms: 1.89x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.30 ms: 1.88x faster                                                          |
| logging_silent             | 101 ns                                                          | 53.9 ns: 1.87x faster                                                          |
| comprehensions             | 19.2 us                                                         | 11.2 us: 1.71x faster                                                          |
| generators                 | 38.5 ms                                                         | 22.6 ms: 1.70x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.32 ms: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 167 ms: 1.62x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.5 ms: 1.60x faster                                                          |
| fannkuch                   | 354 ms                                                          | 224 ms: 1.58x faster                                                           |
| raytrace                   | 308 ms                                                          | 198 ms: 1.55x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 135 us: 1.55x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.42 sec: 1.55x faster                                                         |
| hexiom                     | 6.82 ms                                                         | 4.43 ms: 1.54x faster                                                          |
| pyflate                    | 424 ms                                                          | 292 ms: 1.45x faster                                                           |
| scimark_sor                | 130 ms                                                          | 89.7 ms: 1.45x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 199 us: 1.43x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.51 ms: 1.43x faster                                                          |
| regex_compile              | 129 ms                                                          | 90.7 ms: 1.42x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 49.2 ms: 1.41x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 895 us: 1.39x faster                                                           |
| richards                   | 41.3 ms                                                         | 30.3 ms: 1.36x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 68.8 ms: 1.36x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 260 ms: 1.35x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 207 ms: 1.34x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 39.9 ms: 1.33x faster                                                          |
| richards_super             | 46.5 ms                                                         | 34.9 ms: 1.33x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.15 ms: 1.33x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.8 ms: 1.32x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 54.9 ms: 1.31x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.43 us: 1.31x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.31x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.98 us: 1.30x faster                                                          |
| async_tree_none            | 298 ms                                                          | 229 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 16.2 ms: 1.29x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                                         |
| chameleon                  | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                                          |
| go                         | 137 ms                                                          | 107 ms: 1.29x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 567 ms: 1.27x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.4 ms: 1.27x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 537 ms: 1.26x faster                                                           |
| pycparser                  | 978 ms                                                          | 805 ms: 1.21x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 71.9 ms: 1.21x faster                                                          |
| deepcopy                   | 360 us                                                          | 300 us: 1.20x faster                                                           |
| django_template            | 36.9 ms                                                         | 30.9 ms: 1.20x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.73 us: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 465 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 482 ms: 1.17x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.64 sec: 1.17x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 41.8 ms: 1.16x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 106 ms: 1.16x faster                                                           |
| sympy_str                  | 240 ms                                                          | 207 ms: 1.16x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                                          |
| 2to3                       | 280 ms                                                          | 247 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 986 us: 1.12x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.89 us: 1.10x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.8 ms: 1.10x faster                                                          |
| asyncio_tcp                | 662 ms                                                          | 611 ms: 1.08x faster                                                           |
| sympy_expand               | 398 ms                                                          | 370 ms: 1.08x faster                                                           |
| async_generators           | 313 ms                                                          | 293 ms: 1.07x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 85.8 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                         |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.99 ms: 1.02x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.88 us: 1.02x faster                                                          |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 74.4 ms: 1.01x faster                                                          |
| telco                      | 5.51 ms                                                         | 5.47 ms: 1.01x faster                                                          |
| coverage                   | 48.4 ms                                                         | 49.6 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                          |
| pickle                     | 7.79 us                                                         | 8.16 us: 1.05x slower                                                          |
| pickle_dict                | 19.9 us                                                         | 20.9 us: 1.05x slower                                                          |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.39 ms: 1.06x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.4 ms: 1.07x slower                                                          |
| pickle_list                | 3.37 us                                                         | 3.62 us: 1.07x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 754 us: 1.16x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 218 ms: 2.17x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.24x faster                                                                   |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064-JIT/bm-20240518-pythonperf1_win32-x86-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown