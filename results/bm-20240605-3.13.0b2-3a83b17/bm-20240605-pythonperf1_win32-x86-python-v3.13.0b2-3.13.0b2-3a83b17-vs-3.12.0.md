# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: windows-x86
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 233 ms: 1.20x faster                                                |
| chameleon      | 7.75 ms                                                         | 5.71 ms: 1.36x faster                                               |
| docutils       | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                              |
| tornado_http   | 105 ms                                                          | 94.3 ms: 1.11x faster                                               |
| Geometric mean | (ref)                                                           | 1.19x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                |
| async_tree_io              | 693 ms                                                          | 530 ms: 1.31x faster                                                |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 76.9 ms: 1.65x faster                                               |
| float          | 76.7 ms                                                         | 52.4 ms: 1.46x faster                                               |
| pidigits       | 199 ms                                                          | 199 ms: 1.00x faster                                                |
| Geometric mean | (ref)                                                           | 1.34x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 99.9 ms: 1.29x faster                                               |
| regex_effbot   | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                               |
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.7 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                           | 1.09x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 147 us: 1.43x faster                                                |
| pickle_pure_python   | 286 us                                                          | 213 us: 1.34x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                              |
| xml_etree_process    | 53.2 ms                                                         | 42.1 ms: 1.27x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 64.2 ms: 1.21x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                |
| json_dumps           | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                               |
| json_loads           | 20.4 us                                                         | 20.5 us: 1.01x slower                                               |
| unpickle             | 9.71 us                                                         | 9.79 us: 1.01x slower                                               |
| pickle               | 7.79 us                                                         | 8.07 us: 1.04x slower                                               |
| pickle_dict          | 19.9 us                                                         | 20.8 us: 1.04x slower                                               |
| pickle_list          | 3.37 us                                                         | 3.57 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                        |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.2 ms: 1.05x faster                                               |
| python_startup         | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                               |
| Geometric mean         | (ref)                                                           | 1.03x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.94 ms: 1.43x faster                                               |
| django_template | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                               |
| Geometric mean  | (ref)                                                           | 1.33x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 21.2 ms: 1.82x faster                                               |
| logging_silent             | 101 ns                                                          | 57.9 ns: 1.75x faster                                               |
| nbody                      | 127 ms                                                          | 76.9 ms: 1.65x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 23.5 us: 1.63x faster                                               |
| raytrace                   | 308 ms                                                          | 189 ms: 1.63x faster                                                |
| comprehensions             | 19.2 us                                                         | 11.9 us: 1.62x faster                                               |
| hexiom                     | 6.82 ms                                                         | 4.23 ms: 1.61x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.23 ms: 1.60x faster                                               |
| scimark_sor                | 130 ms                                                          | 81.0 ms: 1.60x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 59.4 ms: 1.57x faster                                               |
| spectral_norm              | 104 ms                                                          | 68.0 ms: 1.53x faster                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 45.2 ms: 1.47x faster                                               |
| float                      | 76.7 ms                                                         | 52.4 ms: 1.46x faster                                               |
| chaos                      | 69.4 ms                                                         | 48.0 ms: 1.45x faster                                               |
| mako                       | 9.96 ms                                                         | 6.94 ms: 1.43x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 147 us: 1.43x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 254 ms: 1.38x faster                                                |
| pyflate                    | 424 ms                                                          | 308 ms: 1.38x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 203 ms: 1.37x faster                                                |
| scimark_fft                | 271 ms                                                          | 198 ms: 1.37x faster                                                |
| go                         | 137 ms                                                          | 101 ms: 1.36x faster                                                |
| nqueens                    | 93.7 ms                                                         | 68.7 ms: 1.36x faster                                               |
| chameleon                  | 7.75 ms                                                         | 5.71 ms: 1.36x faster                                               |
| coroutines                 | 20.9 ms                                                         | 15.5 ms: 1.35x faster                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.87 ms: 1.34x faster                                               |
| pickle_pure_python         | 286 us                                                          | 213 us: 1.34x faster                                                |
| tomli_loads                | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                              |
| richards                   | 41.3 ms                                                         | 31.2 ms: 1.32x faster                                               |
| async_tree_memoization     | 364 ms                                                          | 275 ms: 1.32x faster                                                |
| richards_super             | 46.5 ms                                                         | 35.5 ms: 1.31x faster                                               |
| fannkuch                   | 354 ms                                                          | 270 ms: 1.31x faster                                                |
| async_tree_io              | 693 ms                                                          | 530 ms: 1.31x faster                                                |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                |
| logging_simple             | 9.75 us                                                         | 7.47 us: 1.31x faster                                               |
| sqlglot_parse              | 1.25 ms                                                         | 964 us: 1.29x faster                                                |
| regex_compile              | 129 ms                                                          | 99.9 ms: 1.29x faster                                               |
| deepcopy                   | 360 us                                                          | 280 us: 1.29x faster                                                |
| sqlglot_transpile          | 1.53 ms                                                         | 1.19 ms: 1.29x faster                                               |
| logging_format             | 10.4 us                                                         | 8.13 us: 1.28x faster                                               |
| async_tree_io_tg           | 677 ms                                                          | 529 ms: 1.28x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 42.1 ms: 1.27x faster                                               |
| pycparser                  | 978 ms                                                          | 777 ms: 1.26x faster                                                |
| deepcopy_reduce            | 3.23 us                                                         | 2.59 us: 1.25x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 55.8 ms: 1.24x faster                                               |
| django_template            | 36.9 ms                                                         | 30.1 ms: 1.23x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 447 ms: 1.22x faster                                                |
| sqlglot_optimize           | 48.5 ms                                                         | 39.7 ms: 1.22x faster                                               |
| xml_etree_generate         | 72.1 ms                                                         | 59.6 ms: 1.21x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 64.2 ms: 1.21x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.24 sec: 1.21x faster                                              |
| 2to3                       | 280 ms                                                          | 233 ms: 1.20x faster                                                |
| sympy_integrate            | 17.5 ms                                                         | 14.6 ms: 1.20x faster                                               |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 471 ms: 1.20x faster                                                |
| mdp                        | 1.91 sec                                                        | 1.60 sec: 1.19x faster                                              |
| pprint_safe_repr           | 721 ms                                                          | 607 ms: 1.19x faster                                                |
| async_generators           | 313 ms                                                          | 266 ms: 1.18x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 74.1 ms: 1.17x faster                                               |
| sympy_sum                  | 123 ms                                                          | 105 ms: 1.17x faster                                                |
| sympy_str                  | 240 ms                                                          | 211 ms: 1.13x faster                                                |
| bench_thread_pool          | 1.10 ms                                                         | 985 us: 1.12x faster                                                |
| tornado_http               | 105 ms                                                          | 94.3 ms: 1.11x faster                                               |
| docutils                   | 1.98 sec                                                        | 1.81 sec: 1.09x faster                                              |
| pathlib                    | 91.4 ms                                                         | 83.9 ms: 1.09x faster                                               |
| bench_mp_pool              | 75.4 ms                                                         | 69.4 ms: 1.09x faster                                               |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.84 ms: 1.08x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.88 ms: 1.08x faster                                               |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                |
| sympy_expand               | 398 ms                                                          | 375 ms: 1.06x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.96 us: 1.06x faster                                               |
| python_startup_no_site     | 19.1 ms                                                         | 18.2 ms: 1.05x faster                                               |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.05x faster                                              |
| json                       | 4.15 ms                                                         | 4.10 ms: 1.01x faster                                               |
| python_startup             | 22.4 ms                                                         | 22.2 ms: 1.01x faster                                               |
| pidigits                   | 199 ms                                                          | 199 ms: 1.00x faster                                                |
| json_loads                 | 20.4 us                                                         | 20.5 us: 1.01x slower                                               |
| unpickle                   | 9.71 us                                                         | 9.79 us: 1.01x slower                                               |
| pickle                     | 7.79 us                                                         | 8.07 us: 1.04x slower                                               |
| pickle_dict                | 19.9 us                                                         | 20.8 us: 1.04x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 15.7 ms: 1.05x slower                                               |
| pickle_list                | 3.37 us                                                         | 3.57 us: 1.06x slower                                               |
| typing_runtime_protocols   | 126 us                                                          | 136 us: 1.07x slower                                                |
| telco                      | 5.51 ms                                                         | 6.03 ms: 1.09x slower                                               |
| create_gc_cycles           | 652 us                                                          | 756 us: 1.16x slower                                                |
| sqlglot_normalize          | 100 ms                                                          | 206 ms: 2.06x slower                                                |
| coverage                   | 48.4 ms                                                         | 307 ms: 6.34x slower                                                |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                        |

Benchmark hidden because not significant (3): gc_traversal, unpickle_list, asyncio_tcp
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf1_win32-x86-python-v3.13.0b2-3.13.0b2-3a83b17.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown