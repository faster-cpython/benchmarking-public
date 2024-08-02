# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.18x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 233 ms: 1.20x faster                                                            |
| chameleon      | 7.75 ms                                                         | 5.85 ms: 1.32x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| tornado_http   | 105 ms                                                          | 94.2 ms: 1.12x faster                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 73.9 ms: 1.72x faster                                                           |
| float          | 76.7 ms                                                         | 52.6 ms: 1.46x faster                                                           |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                           | 1.36x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 100.0 ms: 1.29x faster                                                          |
| regex_effbot   | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 146 us: 1.43x faster                                                            |
| tomli_loads          | 2.20 sec                                                        | 1.62 sec: 1.35x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 219 us: 1.31x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 42.4 ms: 1.26x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 60.1 ms: 1.20x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 103 ms: 1.09x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.94 ms: 1.07x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.87 us: 1.03x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 20.4 us: 1.02x slower                                                           |
| pickle               | 7.79 us                                                         | 8.01 us: 1.03x slower                                                           |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                           |
| python_startup         | 22.4 ms                                                         | 23.0 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.97 ms: 1.43x faster                                                           |
| django_template | 36.9 ms                                                         | 30.6 ms: 1.21x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.31x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.3 ms: 1.81x faster                                                           |
| logging_silent             | 101 ns                                                          | 58.2 ns: 1.74x faster                                                           |
| nbody                      | 127 ms                                                          | 73.9 ms: 1.72x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 23.4 us: 1.64x faster                                                           |
| raytrace                   | 308 ms                                                          | 190 ms: 1.62x faster                                                            |
| scimark_sor                | 130 ms                                                          | 80.6 ms: 1.61x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.61x faster                                                           |
| comprehensions             | 19.2 us                                                         | 12.0 us: 1.59x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.30 ms: 1.59x faster                                                           |
| spectral_norm              | 104 ms                                                          | 66.3 ms: 1.57x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 60.0 ms: 1.55x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.0 ms: 1.48x faster                                                           |
| float                      | 76.7 ms                                                         | 52.6 ms: 1.46x faster                                                           |
| chaos                      | 69.4 ms                                                         | 47.9 ms: 1.45x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 146 us: 1.43x faster                                                            |
| mako                       | 9.96 ms                                                         | 6.97 ms: 1.43x faster                                                           |
| pyflate                    | 424 ms                                                          | 307 ms: 1.38x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 256 ms: 1.37x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.83 ms: 1.36x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.4 ms: 1.35x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.62 sec: 1.35x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 69.3 ms: 1.35x faster                                                           |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                            |
| sqlglot_parse              | 1.25 ms                                                         | 934 us: 1.34x faster                                                            |
| fannkuch                   | 354 ms                                                          | 266 ms: 1.33x faster                                                            |
| richards_super             | 46.5 ms                                                         | 34.9 ms: 1.33x faster                                                           |
| richards                   | 41.3 ms                                                         | 31.2 ms: 1.33x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 5.85 ms: 1.32x faster                                                           |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 278 ms: 1.31x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.17 ms: 1.31x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 219 us: 1.31x faster                                                            |
| async_tree_io              | 693 ms                                                          | 532 ms: 1.30x faster                                                            |
| async_tree_none            | 298 ms                                                          | 230 ms: 1.29x faster                                                            |
| regex_compile              | 129 ms                                                          | 100.0 ms: 1.29x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.61 us: 1.28x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                            |
| deepcopy                   | 360 us                                                          | 282 us: 1.28x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.23 us: 1.26x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 42.4 ms: 1.26x faster                                                           |
| pycparser                  | 978 ms                                                          | 786 ms: 1.24x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.1 ms: 1.23x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.63 us: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 445 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 466 ms: 1.21x faster                                                            |
| django_template            | 36.9 ms                                                         | 30.6 ms: 1.21x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 40.2 ms: 1.21x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.6 ms: 1.20x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 60.1 ms: 1.20x faster                                                           |
| 2to3                       | 280 ms                                                          | 233 ms: 1.20x faster                                                            |
| pprint_pformat             | 1.50 sec                                                        | 1.25 sec: 1.20x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 14.8 ms: 1.19x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 611 ms: 1.18x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 74.7 ms: 1.16x faster                                                           |
| async_generators           | 313 ms                                                          | 271 ms: 1.16x faster                                                            |
| sympy_str                  | 240 ms                                                          | 209 ms: 1.15x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.67 sec: 1.14x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 969 us: 1.14x faster                                                            |
| tornado_http               | 105 ms                                                          | 94.2 ms: 1.12x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.79 sec: 1.11x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 83.3 ms: 1.10x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 103 ms: 1.09x faster                                                            |
| sympy_expand               | 398 ms                                                          | 367 ms: 1.09x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 69.5 ms: 1.08x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.94 ms: 1.07x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                          |
| sqlite_synth               | 2.07 us                                                         | 2.00 us: 1.04x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.97 ms: 1.03x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.87 us: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.01x faster                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 18.9 ms: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 20.4 us: 1.02x slower                                                           |
| python_startup             | 22.4 ms                                                         | 23.0 ms: 1.03x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.01 us: 1.03x slower                                                           |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.04x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.8 ms: 1.05x slower                                                           |
| json                       | 4.15 ms                                                         | 4.36 ms: 1.05x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 139 us: 1.10x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.15 ms: 1.12x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 745 us: 1.14x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 207 ms: 2.07x slower                                                            |
| coverage                   | 48.4 ms                                                         | 304 ms: 6.28x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.18x faster                                                                    |

Benchmark hidden because not significant (2): regex_dna, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown