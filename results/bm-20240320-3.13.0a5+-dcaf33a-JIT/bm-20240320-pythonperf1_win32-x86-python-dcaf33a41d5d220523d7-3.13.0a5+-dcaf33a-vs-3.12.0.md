# Results vs. 3.12.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: windows-x86
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.07x slower
- HPT reliability: 99.15%
- HPT 99th percentile: 1.00x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 266 ms: 1.05x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.84 ms: 1.33x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.45 sec: 1.24x slower                                                          |
| tornado_http   | 105 ms                                                          | 97.2 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 564 ms                                                          | 1.57 sec: 2.78x slower                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 1.61 sec: 2.95x slower                                                          |
| async_tree_none            | 298 ms                                                          | 1.20 sec: 4.03x slower                                                          |
| async_tree_memoization     | 364 ms                                                          | 1.47 sec: 4.03x slower                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 1.47 sec: 4.21x slower                                                          |
| async_tree_none_tg         | 278 ms                                                          | 1.24 sec: 4.46x slower                                                          |
| async_tree_io              | 693 ms                                                          | 4.63 sec: 6.68x slower                                                          |
| async_tree_io_tg           | 677 ms                                                          | 4.73 sec: 6.98x slower                                                          |
| Geometric mean             | (ref)                                                           | 4.30x slower                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 100 ms: 1.27x faster                                                            |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| float          | 76.7 ms                                                         | 82.2 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.18x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                           |
| regex_dna      | 127 ms                                                          | 124 ms: 1.02x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 286 us                                                          | 215 us: 1.33x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.72 sec: 1.28x faster                                                          |
| unpickle_pure_python | 210 us                                                          | 174 us: 1.21x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.93 ms: 1.07x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.1 us: 1.01x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 20.0 us: 1.00x slower                                                           |
| pickle               | 7.79 us                                                         | 8.00 us: 1.03x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.46 us: 1.03x slower                                                           |
| unpickle_list        | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| xml_etree_parse      | 113 ms                                                          | 133 ms: 1.18x slower                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 93.8 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                           |
| python_startup_no_site | 19.1 ms                                                         | 24.2 ms: 1.27x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.23x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.15 ms: 1.39x faster                                                           |
| django_template | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.29x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 22.4 ms: 1.72x faster                                                           |
| logging_silent             | 101 ns                                                          | 60.6 ns: 1.67x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 25.2 us: 1.52x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.6 ms: 1.45x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 43.1 ns: 1.45x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.40x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.15 ms: 1.39x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.67 ms: 1.34x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 215 us: 1.33x faster                                                            |
| comprehensions             | 19.2 us                                                         | 14.4 us: 1.33x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.84 ms: 1.33x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.3 ms: 1.31x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.29x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 98.8 us: 1.28x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.72 sec: 1.28x faster                                                          |
| nbody                      | 127 ms                                                          | 100 ms: 1.27x faster                                                            |
| deepcopy                   | 360 us                                                          | 289 us: 1.25x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.13 ms: 1.23x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 174 us: 1.21x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 1.03 ms: 1.21x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.19x faster                                                           |
| django_template            | 36.9 ms                                                         | 31.1 ms: 1.19x faster                                                           |
| regex_compile              | 129 ms                                                          | 110 ms: 1.18x faster                                                            |
| raytrace                   | 308 ms                                                          | 264 ms: 1.17x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| logging_simple             | 9.75 us                                                         | 8.38 us: 1.16x faster                                                           |
| richards                   | 41.3 ms                                                         | 35.7 ms: 1.16x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.02 us: 1.15x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.14x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.98 ms: 1.14x faster                                                           |
| chaos                      | 69.4 ms                                                         | 60.9 ms: 1.14x faster                                                           |
| sympy_str                  | 240 ms                                                          | 211 ms: 1.14x faster                                                            |
| richards_super             | 46.5 ms                                                         | 40.9 ms: 1.13x faster                                                           |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.13x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.27 ms: 1.13x faster                                                           |
| pyflate                    | 424 ms                                                          | 376 ms: 1.13x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 61.5 ms: 1.12x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 83.3 ms: 1.12x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 47.6 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.74 sec: 1.10x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| go                         | 137 ms                                                          | 126 ms: 1.09x faster                                                            |
| tornado_http               | 105 ms                                                          | 97.2 ms: 1.08x faster                                                           |
| fannkuch                   | 354 ms                                                          | 329 ms: 1.07x faster                                                            |
| sympy_expand               | 398 ms                                                          | 371 ms: 1.07x faster                                                            |
| json_dumps                 | 7.40 ms                                                         | 6.93 ms: 1.07x faster                                                           |
| sqlite_synth               | 2.07 us                                                         | 1.95 us: 1.06x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 86.3 ms: 1.06x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 45.8 ms: 1.06x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 629 ms: 1.05x faster                                                            |
| 2to3                       | 280 ms                                                          | 266 ms: 1.05x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.95 ms: 1.05x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 69.1 ms: 1.04x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 83.4 ms: 1.04x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 90.2 ms: 1.04x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 64.6 ms: 1.03x faster                                                           |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.02x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.46 sec: 1.02x faster                                                          |
| json_loads                 | 20.4 us                                                         | 20.1 us: 1.01x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 715 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.0 us: 1.00x slower                                                           |
| pycparser                  | 978 ms                                                          | 989 ms: 1.01x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 664 us: 1.02x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.00 us: 1.03x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.46 us: 1.03x slower                                                           |
| async_generators           | 313 ms                                                          | 322 ms: 1.03x slower                                                            |
| unpickle_list              | 2.95 us                                                         | 3.04 us: 1.03x slower                                                           |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.07x slower                                                           |
| float                      | 76.7 ms                                                         | 82.2 ms: 1.07x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.5 us: 1.08x slower                                                           |
| xml_etree_parse            | 113 ms                                                          | 133 ms: 1.18x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.53 ms: 1.19x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.6 ms: 1.19x slower                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 93.8 ms: 1.21x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.45 sec: 1.24x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 24.2 ms: 1.27x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 221 ms: 2.20x slower                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 1.57 sec: 2.78x slower                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 1.61 sec: 2.95x slower                                                          |
| async_tree_none            | 298 ms                                                          | 1.20 sec: 4.03x slower                                                          |
| async_tree_memoization     | 364 ms                                                          | 1.47 sec: 4.03x slower                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 1.47 sec: 4.21x slower                                                          |
| async_tree_none_tg         | 278 ms                                                          | 1.24 sec: 4.46x slower                                                          |
| async_tree_io              | 693 ms                                                          | 4.63 sec: 6.68x slower                                                          |
| async_tree_io_tg           | 677 ms                                                          | 4.73 sec: 6.98x slower                                                          |
| coverage                   | 48.4 ms                                                         | 508 ms: 10.48x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240320-3.13.0a5+-dcaf33a-JIT/bm-20240320-pythonperf1_win32-x86-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 99.15% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: unknown