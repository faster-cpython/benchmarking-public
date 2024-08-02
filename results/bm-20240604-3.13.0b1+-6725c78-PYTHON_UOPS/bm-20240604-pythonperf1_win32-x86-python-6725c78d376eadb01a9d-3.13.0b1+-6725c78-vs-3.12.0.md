# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: windows-x86
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.12x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.33 ms: 1.22x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                          |
| tornado_http   | 105 ms                                                          | 99.7 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.09x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                            |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                            |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 542 ms: 1.25x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.25x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 75.2 ms: 1.69x faster                                                           |
| float          | 76.7 ms                                                         | 52.9 ms: 1.45x faster                                                           |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                           | 1.35x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| regex_compile  | 129 ms                                                          | 124 ms: 1.04x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| Geometric mean | (ref)                                                           | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 43.1 ms: 1.24x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 172 us: 1.22x faster                                                            |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.2 ms: 1.21x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                           |
| pickle_pure_python   | 286 us                                                          | 247 us: 1.16x faster                                                            |
| json_dumps           | 7.40 ms                                                         | 6.74 ms: 1.10x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.09x faster                                                            |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.6 us: 1.03x slower                                                           |
| pickle               | 7.79 us                                                         | 8.25 us: 1.06x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| python_startup         | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.24 ms: 1.37x faster                                                           |
| django_template | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 75.2 ms: 1.69x faster                                                           |
| generators                 | 38.5 ms                                                         | 23.6 ms: 1.63x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.5 ms: 1.45x faster                                                           |
| raytrace                   | 308 ms                                                          | 212 ms: 1.45x faster                                                            |
| float                      | 76.7 ms                                                         | 52.9 ms: 1.45x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.40x faster                                                           |
| scimark_sor                | 130 ms                                                          | 93.0 ms: 1.40x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 27.6 us: 1.39x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.24 ms: 1.37x faster                                                           |
| logging_silent             | 101 ns                                                          | 74.2 ns: 1.36x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.62 sec: 1.36x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 49.5 ms: 1.34x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.6 ms: 1.34x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 263 ms: 1.33x faster                                                            |
| richards                   | 41.3 ms                                                         | 31.3 ms: 1.32x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 210 ms: 1.32x faster                                                            |
| richards_super             | 46.5 ms                                                         | 35.4 ms: 1.31x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.0 ms: 1.31x faster                                                           |
| scimark_fft                | 271 ms                                                          | 207 ms: 1.31x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.01 ms: 1.28x faster                                                           |
| fannkuch                   | 354 ms                                                          | 277 ms: 1.28x faster                                                            |
| async_tree_io              | 693 ms                                                          | 545 ms: 1.27x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 73.6 ms: 1.27x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.69 us: 1.27x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.83 ms: 1.27x faster                                                           |
| async_tree_none            | 298 ms                                                          | 236 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 542 ms: 1.25x faster                                                            |
| logging_format             | 10.4 us                                                         | 8.41 us: 1.24x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 43.1 ms: 1.24x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 295 ms: 1.23x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 6.33 ms: 1.22x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.02 ms: 1.22x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 172 us: 1.22x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 56.6 ms: 1.22x faster                                                           |
| go                         | 137 ms                                                          | 113 ms: 1.21x faster                                                            |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.2 ms: 1.21x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.66 ms: 1.21x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 60.0 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.20x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.27 sec: 1.18x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 615 ms: 1.17x faster                                                            |
| deepcopy                   | 360 us                                                          | 308 us: 1.17x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 80.0 ms: 1.17x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 486 ms: 1.16x faster                                                            |
| pickle_pure_python         | 286 us                                                          | 247 us: 1.16x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.79 us: 1.16x faster                                                           |
| pyflate                    | 424 ms                                                          | 371 ms: 1.14x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.4 ms: 1.14x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 76.4 ms: 1.14x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                                          |
| pycparser                  | 978 ms                                                          | 882 ms: 1.11x faster                                                            |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                            |
| async_generators           | 313 ms                                                          | 285 ms: 1.10x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 44.1 ms: 1.10x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.74 ms: 1.10x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.09x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 83.9 ms: 1.09x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 615 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.93 us: 1.07x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.4 ms: 1.07x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                           |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.06x faster                                                            |
| bench_mp_pool              | 75.4 ms                                                         | 71.4 ms: 1.06x faster                                                           |
| tornado_http               | 105 ms                                                          | 99.7 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                                          |
| regex_compile              | 129 ms                                                          | 124 ms: 1.04x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.3 ms: 1.04x faster                                                           |
| sympy_str                  | 240 ms                                                          | 237 ms: 1.01x faster                                                            |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                            |
| docutils                   | 1.98 sec                                                        | 2.00 sec: 1.01x slower                                                          |
| python_startup             | 22.4 ms                                                         | 22.6 ms: 1.01x slower                                                           |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.6 us: 1.03x slower                                                           |
| telco                      | 5.51 ms                                                         | 5.80 ms: 1.05x slower                                                           |
| sympy_expand               | 398 ms                                                          | 419 ms: 1.05x slower                                                            |
| pickle                     | 7.79 us                                                         | 8.25 us: 1.06x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.4 us: 1.07x slower                                                           |
| pickle_list                | 3.37 us                                                         | 3.65 us: 1.08x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 147 us: 1.16x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 766 us: 1.18x slower                                                            |
| sqlglot_normalize          | 100 ms                                                          | 229 ms: 2.29x slower                                                            |
| coverage                   | 48.4 ms                                                         | 325 ms: 6.70x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.12x faster                                                                    |

Benchmark hidden because not significant (3): gc_traversal, unpickle_list, json
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78-PYTHON_UOPS/bm-20240604-pythonperf1_win32-x86-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown