# Results vs. 3.12.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: windows-x86
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 262 ms: 1.07x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.15 ms: 1.26x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                          |
| tornado_http   | 105 ms                                                          | 99.2 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg           | 677 ms                                                          | 522 ms: 1.30x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.28x faster                                                            |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.25x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 292 ms: 1.25x faster                                                            |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.23x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 52.7 ms: 1.46x faster                                                           |
| nbody          | 127 ms                                                          | 97.1 ms: 1.31x faster                                                           |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 224 us: 1.27x faster                                                            |
| unpickle_pure_python | 210 us                                                          | 168 us: 1.25x faster                                                            |
| xml_etree_process    | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.81 ms: 1.09x faster                                                           |
| unpickle_list        | 2.95 us                                                         | 2.72 us: 1.08x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| pickle_list          | 3.37 us                                                         | 3.22 us: 1.04x faster                                                           |
| pickle_dict          | 19.9 us                                                         | 19.8 us: 1.01x faster                                                           |
| pickle               | 7.79 us                                                         | 7.88 us: 1.01x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.0 us: 1.03x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| python_startup_no_site | 19.1 ms                                                         | 23.3 ms: 1.22x slower                                                           |
| Geometric mean         | (ref)                                                           | 1.19x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.20 ms: 1.38x faster                                                           |
| django_template | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.25x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 25.0 ms: 1.54x faster                                                           |
| logging_silent             | 101 ns                                                          | 69.4 ns: 1.46x faster                                                           |
| float                      | 76.7 ms                                                         | 52.7 ms: 1.46x faster                                                           |
| spectral_norm              | 104 ms                                                          | 71.6 ms: 1.45x faster                                                           |
| unpack_sequence            | 62.5 ns                                                         | 44.3 ns: 1.41x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 27.3 us: 1.41x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 15.1 ms: 1.38x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.20 ms: 1.38x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.62 ms: 1.37x faster                                                           |
| typing_runtime_protocols   | 126 us                                                          | 93.9 us: 1.34x faster                                                           |
| nbody                      | 127 ms                                                          | 97.1 ms: 1.31x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 522 ms: 1.30x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 273 ms: 1.29x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 216 ms: 1.28x faster                                                            |
| tomli_loads                | 2.20 sec                                                        | 1.71 sec: 1.28x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 224 us: 1.27x faster                                                            |
| chameleon                  | 7.75 ms                                                         | 6.15 ms: 1.26x faster                                                           |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                            |
| async_tree_none            | 298 ms                                                          | 237 ms: 1.25x faster                                                            |
| unpickle_pure_python       | 210 us                                                          | 168 us: 1.25x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 292 ms: 1.25x faster                                                            |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.25x faster                                                           |
| deepcopy                   | 360 us                                                          | 289 us: 1.24x faster                                                            |
| async_tree_io              | 693 ms                                                          | 559 ms: 1.24x faster                                                            |
| comprehensions             | 19.2 us                                                         | 15.6 us: 1.23x faster                                                           |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.03 ms: 1.22x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.0 ms: 1.21x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.20x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.7 ms: 1.16x faster                                                           |
| chaos                      | 69.4 ms                                                         | 59.7 ms: 1.16x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 62.4 ms: 1.16x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.44 us: 1.15x faster                                                           |
| logging_format             | 10.4 us                                                         | 9.06 us: 1.15x faster                                                           |
| pycparser                  | 978 ms                                                          | 854 ms: 1.14x faster                                                            |
| regex_compile              | 129 ms                                                          | 113 ms: 1.14x faster                                                            |
| richards                   | 41.3 ms                                                         | 36.3 ms: 1.14x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 61.0 ms: 1.13x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 484 ms: 1.13x faster                                                            |
| django_template            | 36.9 ms                                                         | 32.7 ms: 1.13x faster                                                           |
| richards_super             | 46.5 ms                                                         | 41.3 ms: 1.13x faster                                                           |
| pyflate                    | 424 ms                                                          | 377 ms: 1.13x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 6.07 ms: 1.12x faster                                                           |
| scimark_fft                | 271 ms                                                          | 244 ms: 1.11x faster                                                            |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                                            |
| sympy_sum                  | 123 ms                                                          | 111 ms: 1.10x faster                                                            |
| raytrace                   | 308 ms                                                          | 280 ms: 1.10x faster                                                            |
| scimark_lu                 | 93.2 ms                                                         | 85.0 ms: 1.10x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.81 ms: 1.09x faster                                                           |
| unpickle_list              | 2.95 us                                                         | 2.72 us: 1.08x faster                                                           |
| go                         | 137 ms                                                          | 127 ms: 1.08x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.92 us: 1.08x faster                                                           |
| async_generators           | 313 ms                                                          | 293 ms: 1.07x faster                                                            |
| 2to3                       | 280 ms                                                          | 262 ms: 1.07x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.79 sec: 1.07x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                            |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.06x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 86.4 ms: 1.06x faster                                                           |
| tornado_http               | 105 ms                                                          | 99.2 ms: 1.06x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.6 ms: 1.06x faster                                                           |
| fannkuch                   | 354 ms                                                          | 337 ms: 1.05x faster                                                            |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                            |
| sqlglot_optimize           | 48.5 ms                                                         | 46.2 ms: 1.05x faster                                                           |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                            |
| pickle_list                | 3.37 us                                                         | 3.22 us: 1.04x faster                                                           |
| asyncio_tcp                | 662 ms                                                          | 634 ms: 1.04x faster                                                            |
| meteor_contest             | 86.9 ms                                                         | 83.3 ms: 1.04x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.38 ms: 1.04x faster                                                           |
| docutils                   | 1.98 sec                                                        | 1.93 sec: 1.03x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.1 ms: 1.02x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 92.2 ms: 1.02x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 65.6 ms: 1.01x faster                                                           |
| json                       | 4.15 ms                                                         | 4.11 ms: 1.01x faster                                                           |
| create_gc_cycles           | 652 us                                                          | 646 us: 1.01x faster                                                            |
| pickle_dict                | 19.9 us                                                         | 19.8 us: 1.01x faster                                                           |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                            |
| pickle                     | 7.79 us                                                         | 7.88 us: 1.01x slower                                                           |
| pprint_safe_repr           | 721 ms                                                          | 731 ms: 1.01x slower                                                            |
| unpickle                   | 9.71 us                                                         | 10.0 us: 1.03x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.1 ms: 1.07x slower                                                           |
| python_startup             | 22.4 ms                                                         | 26.1 ms: 1.17x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.46 ms: 1.17x slower                                                           |
| python_startup_no_site     | 19.1 ms                                                         | 23.3 ms: 1.22x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 240 ms: 2.40x slower                                                            |
| coverage                   | 48.4 ms                                                         | 484 ms: 10.00x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (2): json_loads, pprint_pformat
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240323-3.13.0a5+-d610d82-JIT/bm-20240323-pythonperf1_win32-x86-python-d610d821fd210dce63a1-3.13.0a5+-d610d82.json: genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown