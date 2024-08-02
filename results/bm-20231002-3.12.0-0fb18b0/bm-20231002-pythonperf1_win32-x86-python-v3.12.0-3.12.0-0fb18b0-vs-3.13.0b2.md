# Results vs. 3.13.0b2

- fork: python
- ref: v3.12.0
- machine: windows-x86
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.19x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 233 ms                                                              | 280 ms: 1.20x slower                                            |
| chameleon      | 5.71 ms                                                             | 7.75 ms: 1.36x slower                                           |
| docutils       | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                          |
| tornado_http   | 94.3 ms                                                             | 105 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                               | 1.19x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 471 ms                                                              | 564 ms: 1.20x slower                                            |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 546 ms: 1.22x slower                                            |
| async_tree_io_tg           | 529 ms                                                              | 677 ms: 1.28x slower                                            |
| async_tree_none            | 228 ms                                                              | 298 ms: 1.31x slower                                            |
| async_tree_io              | 530 ms                                                              | 693 ms: 1.31x slower                                            |
| async_tree_memoization     | 275 ms                                                              | 364 ms: 1.32x slower                                            |
| async_tree_none_tg         | 203 ms                                                              | 278 ms: 1.37x slower                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 350 ms: 1.38x slower                                            |
| Geometric mean             | (ref)                                                               | 1.30x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 199 ms                                                              | 199 ms: 1.00x slower                                            |
| float          | 52.4 ms                                                             | 76.7 ms: 1.46x slower                                           |
| nbody          | 76.9 ms                                                             | 127 ms: 1.65x slower                                            |
| Geometric mean | (ref)                                                               | 1.34x slower                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 15.7 ms                                                             | 15.0 ms: 1.05x faster                                           |
| regex_dna      | 118 ms                                                              | 127 ms: 1.08x slower                                            |
| regex_effbot   | 1.88 ms                                                             | 2.04 ms: 1.08x slower                                           |
| regex_compile  | 99.9 ms                                                             | 129 ms: 1.29x slower                                            |
| Geometric mean | (ref)                                                               | 1.09x slower                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pickle_list          | 3.57 us                                                             | 3.37 us: 1.06x faster                                           |
| pickle_dict          | 20.8 us                                                             | 19.9 us: 1.04x faster                                           |
| pickle               | 8.07 us                                                             | 7.79 us: 1.04x faster                                           |
| unpickle             | 9.79 us                                                             | 9.71 us: 1.01x faster                                           |
| json_loads           | 20.5 us                                                             | 20.4 us: 1.01x faster                                           |
| json_dumps           | 6.84 ms                                                             | 7.40 ms: 1.08x slower                                           |
| xml_etree_parse      | 104 ms                                                              | 113 ms: 1.08x slower                                            |
| xml_etree_iterparse  | 64.2 ms                                                             | 77.6 ms: 1.21x slower                                           |
| xml_etree_generate   | 59.6 ms                                                             | 72.1 ms: 1.21x slower                                           |
| xml_etree_process    | 42.1 ms                                                             | 53.2 ms: 1.27x slower                                           |
| tomli_loads          | 1.65 sec                                                            | 2.20 sec: 1.33x slower                                          |
| pickle_pure_python   | 213 us                                                              | 286 us: 1.34x slower                                            |
| unpickle_pure_python | 147 us                                                              | 210 us: 1.43x slower                                            |
| Geometric mean       | (ref)                                                               | 1.12x slower                                                    |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 22.2 ms                                                             | 22.4 ms: 1.01x slower                                           |
| python_startup_no_site | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                           |
| Geometric mean         | (ref)                                                               | 1.03x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 30.1 ms                                                             | 36.9 ms: 1.23x slower                                           |
| mako            | 6.94 ms                                                             | 9.96 ms: 1.43x slower                                           |
| Geometric mean  | (ref)                                                               | 1.33x slower                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coverage                   | 307 ms                                                              | 48.4 ms: 6.34x faster                                           |
| sqlglot_normalize          | 206 ms                                                              | 100 ms: 2.06x faster                                            |
| create_gc_cycles           | 756 us                                                              | 652 us: 1.16x faster                                            |
| telco                      | 6.03 ms                                                             | 5.51 ms: 1.09x faster                                           |
| typing_runtime_protocols   | 136 us                                                              | 126 us: 1.07x faster                                            |
| pickle_list                | 3.57 us                                                             | 3.37 us: 1.06x faster                                           |
| regex_v8                   | 15.7 ms                                                             | 15.0 ms: 1.05x faster                                           |
| pickle_dict                | 20.8 us                                                             | 19.9 us: 1.04x faster                                           |
| pickle                     | 8.07 us                                                             | 7.79 us: 1.04x faster                                           |
| unpickle                   | 9.79 us                                                             | 9.71 us: 1.01x faster                                           |
| json_loads                 | 20.5 us                                                             | 20.4 us: 1.01x faster                                           |
| pidigits                   | 199 ms                                                              | 199 ms: 1.00x slower                                            |
| python_startup             | 22.2 ms                                                             | 22.4 ms: 1.01x slower                                           |
| json                       | 4.10 ms                                                             | 4.15 ms: 1.01x slower                                           |
| asyncio_tcp_ssl            | 16.9 sec                                                            | 17.7 sec: 1.05x slower                                          |
| python_startup_no_site     | 18.2 ms                                                             | 19.1 ms: 1.05x slower                                           |
| sqlite_synth               | 1.96 us                                                             | 2.07 us: 1.06x slower                                           |
| sympy_expand               | 375 ms                                                              | 398 ms: 1.06x slower                                            |
| regex_dna                  | 118 ms                                                              | 127 ms: 1.08x slower                                            |
| regex_effbot               | 1.88 ms                                                             | 2.04 ms: 1.08x slower                                           |
| json_dumps                 | 6.84 ms                                                             | 7.40 ms: 1.08x slower                                           |
| xml_etree_parse            | 104 ms                                                              | 113 ms: 1.08x slower                                            |
| bench_mp_pool              | 69.4 ms                                                             | 75.4 ms: 1.09x slower                                           |
| pathlib                    | 83.9 ms                                                             | 91.4 ms: 1.09x slower                                           |
| docutils                   | 1.81 sec                                                            | 1.98 sec: 1.09x slower                                          |
| tornado_http               | 94.3 ms                                                             | 105 ms: 1.11x slower                                            |
| bench_thread_pool          | 985 us                                                              | 1.10 ms: 1.12x slower                                           |
| sympy_str                  | 211 ms                                                              | 240 ms: 1.13x slower                                            |
| sympy_sum                  | 105 ms                                                              | 123 ms: 1.17x slower                                            |
| meteor_contest             | 74.1 ms                                                             | 86.9 ms: 1.17x slower                                           |
| async_generators           | 266 ms                                                              | 313 ms: 1.18x slower                                            |
| pprint_safe_repr           | 607 ms                                                              | 721 ms: 1.19x slower                                            |
| mdp                        | 1.60 sec                                                            | 1.91 sec: 1.19x slower                                          |
| async_tree_cpu_io_mixed    | 471 ms                                                              | 564 ms: 1.20x slower                                            |
| sympy_integrate            | 14.6 ms                                                             | 17.5 ms: 1.20x slower                                           |
| 2to3                       | 233 ms                                                              | 280 ms: 1.20x slower                                            |
| pprint_pformat             | 1.24 sec                                                            | 1.50 sec: 1.21x slower                                          |
| xml_etree_iterparse        | 64.2 ms                                                             | 77.6 ms: 1.21x slower                                           |
| xml_etree_generate         | 59.6 ms                                                             | 72.1 ms: 1.21x slower                                           |
| sqlglot_optimize           | 39.7 ms                                                             | 48.5 ms: 1.22x slower                                           |
| async_tree_cpu_io_mixed_tg | 447 ms                                                              | 546 ms: 1.22x slower                                            |
| django_template            | 30.1 ms                                                             | 36.9 ms: 1.23x slower                                           |
| crypto_pyaes               | 55.8 ms                                                             | 69.2 ms: 1.24x slower                                           |
| deepcopy_reduce            | 2.59 us                                                             | 3.23 us: 1.25x slower                                           |
| pycparser                  | 777 ms                                                              | 978 ms: 1.26x slower                                            |
| xml_etree_process          | 42.1 ms                                                             | 53.2 ms: 1.27x slower                                           |
| async_tree_io_tg           | 529 ms                                                              | 677 ms: 1.28x slower                                            |
| logging_format             | 8.13 us                                                             | 10.4 us: 1.28x slower                                           |
| sqlglot_transpile          | 1.19 ms                                                             | 1.53 ms: 1.29x slower                                           |
| deepcopy                   | 280 us                                                              | 360 us: 1.29x slower                                            |
| regex_compile              | 99.9 ms                                                             | 129 ms: 1.29x slower                                            |
| sqlglot_parse              | 964 us                                                              | 1.25 ms: 1.29x slower                                           |
| logging_simple             | 7.47 us                                                             | 9.75 us: 1.31x slower                                           |
| async_tree_none            | 228 ms                                                              | 298 ms: 1.31x slower                                            |
| async_tree_io              | 530 ms                                                              | 693 ms: 1.31x slower                                            |
| fannkuch                   | 270 ms                                                              | 354 ms: 1.31x slower                                            |
| richards_super             | 35.5 ms                                                             | 46.5 ms: 1.31x slower                                           |
| async_tree_memoization     | 275 ms                                                              | 364 ms: 1.32x slower                                            |
| richards                   | 31.2 ms                                                             | 41.3 ms: 1.32x slower                                           |
| tomli_loads                | 1.65 sec                                                            | 2.20 sec: 1.33x slower                                          |
| pickle_pure_python         | 213 us                                                              | 286 us: 1.34x slower                                            |
| scimark_sparse_mat_mult    | 2.87 ms                                                             | 3.86 ms: 1.34x slower                                           |
| coroutines                 | 15.5 ms                                                             | 20.9 ms: 1.35x slower                                           |
| chameleon                  | 5.71 ms                                                             | 7.75 ms: 1.36x slower                                           |
| nqueens                    | 68.7 ms                                                             | 93.7 ms: 1.36x slower                                           |
| go                         | 101 ms                                                              | 137 ms: 1.36x slower                                            |
| scimark_fft                | 198 ms                                                              | 271 ms: 1.37x slower                                            |
| async_tree_none_tg         | 203 ms                                                              | 278 ms: 1.37x slower                                            |
| pyflate                    | 308 ms                                                              | 424 ms: 1.38x slower                                            |
| async_tree_memoization_tg  | 254 ms                                                              | 350 ms: 1.38x slower                                            |
| unpickle_pure_python       | 147 us                                                              | 210 us: 1.43x slower                                            |
| mako                       | 6.94 ms                                                             | 9.96 ms: 1.43x slower                                           |
| chaos                      | 48.0 ms                                                             | 69.4 ms: 1.45x slower                                           |
| float                      | 52.4 ms                                                             | 76.7 ms: 1.46x slower                                           |
| scimark_monte_carlo        | 45.2 ms                                                             | 66.4 ms: 1.47x slower                                           |
| spectral_norm              | 68.0 ms                                                             | 104 ms: 1.53x slower                                            |
| scimark_lu                 | 59.4 ms                                                             | 93.2 ms: 1.57x slower                                           |
| scimark_sor                | 81.0 ms                                                             | 130 ms: 1.60x slower                                            |
| deltablue                  | 2.23 ms                                                             | 3.58 ms: 1.60x slower                                           |
| hexiom                     | 4.23 ms                                                             | 6.82 ms: 1.61x slower                                           |
| comprehensions             | 11.9 us                                                             | 19.2 us: 1.62x slower                                           |
| raytrace                   | 189 ms                                                              | 308 ms: 1.63x slower                                            |
| deepcopy_memo              | 23.5 us                                                             | 38.4 us: 1.63x slower                                           |
| nbody                      | 76.9 ms                                                             | 127 ms: 1.65x slower                                            |
| logging_silent             | 57.9 ns                                                             | 101 ns: 1.75x slower                                            |
| generators                 | 21.2 ms                                                             | 38.5 ms: 1.82x slower                                           |
| Geometric mean             | (ref)                                                               | 1.19x slower                                                    |

Benchmark hidden because not significant (3): asyncio_tcp, unpickle_list, gc_traversal
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.20x
- 95% likely to have a slowdown of 1.19x
- 99% likely to have a slowdown of 1.18x

# Memory
- memory change: unknown