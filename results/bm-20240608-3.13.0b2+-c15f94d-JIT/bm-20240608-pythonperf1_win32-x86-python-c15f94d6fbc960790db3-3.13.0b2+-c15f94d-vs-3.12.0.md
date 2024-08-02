# Results vs. 3.12.0

- fork: python
- ref: c15f94d6fbc960790db3
- machine: windows-x86
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                          |
| tornado_http   | 105 ms                                                          | 97.1 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.14x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 535 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 53.4 ms: 2.38x faster                                                           |
| float          | 76.7 ms                                                         | 41.9 ms: 1.83x faster                                                           |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 92.1 ms: 1.40x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                           |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.40 sec: 1.57x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 134 us: 1.57x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 198 us: 1.45x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 40.9 ms: 1.30x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 55.6 ms: 1.30x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.54 ms: 1.13x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.80 us: 1.05x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.58 us: 1.06x slower                                                           |
| pickle               | 7.79 us                                                         | 8.32 us: 1.07x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.16x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.9 ms: 1.10x slower                                                           |
| python_startup         | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.10x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                           |
| django_template | 36.9 ms                                                         | 30.8 ms: 1.20x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.49x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 53.4 ms: 2.38x faster                                                           |
| spectral_norm              | 104 ms                                                          | 47.5 ms: 2.19x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 20.1 us: 1.91x faster                                                           |
| logging_silent             | 101 ns                                                          | 54.2 ns: 1.86x faster                                                           |
| mako                       | 9.96 ms                                                         | 5.34 ms: 1.86x faster                                                           |
| float                      | 76.7 ms                                                         | 41.9 ms: 1.83x faster                                                           |
| comprehensions             | 19.2 us                                                         | 10.8 us: 1.77x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 39.6 ms: 1.68x faster                                                           |
| scimark_fft                | 271 ms                                                          | 165 ms: 1.65x faster                                                            |
| fannkuch                   | 354 ms                                                          | 216 ms: 1.64x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.39 ms: 1.62x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.9 ms: 1.61x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.40 sec: 1.57x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 134 us: 1.57x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 4.49 ms: 1.52x faster                                                           |
| raytrace                   | 308 ms                                                          | 204 ms: 1.51x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 47.1 ms: 1.47x faster                                                           |
| scimark_sor                | 130 ms                                                          | 88.6 ms: 1.47x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 198 us: 1.45x faster                                                            |
| deltablue                  | 3.58 ms                                                         | 2.51 ms: 1.43x faster                                                           |
| regex_compile              | 129 ms                                                          | 92.1 ms: 1.40x faster                                                           |
| pyflate                    | 424 ms                                                          | 303 ms: 1.40x faster                                                            |
| chaos                      | 69.4 ms                                                         | 50.1 ms: 1.39x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 904 us: 1.38x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 68.9 ms: 1.36x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 259 ms: 1.35x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 206 ms: 1.35x faster                                                            |
| richards                   | 41.3 ms                                                         | 30.9 ms: 1.34x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.6 ms: 1.34x faster                                                           |
| richards_super             | 46.5 ms                                                         | 34.8 ms: 1.33x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.32 us: 1.33x faster                                                           |
| async_tree_none            | 298 ms                                                          | 227 ms: 1.31x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.17 ms: 1.31x faster                                                           |
| logging_format             | 10.4 us                                                         | 7.94 us: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.30x faster                                                            |
| xml_etree_process          | 53.2 ms                                                         | 40.9 ms: 1.30x faster                                                           |
| go                         | 137 ms                                                          | 106 ms: 1.30x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 55.6 ms: 1.30x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 72.4 ms: 1.29x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 60.4 ms: 1.29x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.17 sec: 1.28x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 566 ms: 1.27x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 287 ms: 1.27x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 535 ms: 1.27x faster                                                            |
| pycparser                  | 978 ms                                                          | 781 ms: 1.25x faster                                                            |
| deepcopy                   | 360 us                                                          | 294 us: 1.22x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 452 ms: 1.21x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 469 ms: 1.20x faster                                                            |
| django_template            | 36.9 ms                                                         | 30.8 ms: 1.20x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.70 us: 1.19x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 73.0 ms: 1.19x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.62 sec: 1.18x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 41.4 ms: 1.17x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                            |
| sympy_str                  | 240 ms                                                          | 210 ms: 1.14x faster                                                            |
| 2to3                       | 280 ms                                                          | 246 ms: 1.14x faster                                                            |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.54 ms: 1.13x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 989 us: 1.12x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.87 us: 1.11x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.10x faster                                                            |
| pathlib                    | 91.4 ms                                                         | 84.0 ms: 1.09x faster                                                           |
| tornado_http               | 105 ms                                                          | 97.1 ms: 1.08x faster                                                           |
| async_generators           | 313 ms                                                          | 295 ms: 1.06x faster                                                            |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                            |
| asyncio_tcp                | 662 ms                                                          | 625 ms: 1.06x faster                                                            |
| docutils                   | 1.98 sec                                                        | 1.88 sec: 1.06x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| unpickle_list              | 2.95 us                                                         | 2.80 us: 1.05x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                           |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                            |
| json                       | 4.15 ms                                                         | 4.07 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                            |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 76.7 ms: 1.02x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.63 ms: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.58 us: 1.06x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.32 us: 1.07x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 20.9 ms: 1.10x slower                                                           |
| python_startup             | 22.4 ms                                                         | 24.8 ms: 1.11x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 141 us: 1.11x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 218 ms: 2.17x slower                                                            |
| coverage                   | 48.4 ms                                                         | 331 ms: 6.83x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): gc_traversal
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240608-3.13.0b2+-c15f94d-JIT/bm-20240608-pythonperf1_win32-x86-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown