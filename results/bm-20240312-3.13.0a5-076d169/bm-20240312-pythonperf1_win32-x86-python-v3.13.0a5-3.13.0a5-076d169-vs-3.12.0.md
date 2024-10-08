# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a5
- machine: windows-x86
- commit hash: 076d169
- commit date: 2024-03-12
- overall geometric mean: 1.21x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 237 ms: 1.18x faster                                                |
| chameleon      | 7.75 ms                                                         | 5.53 ms: 1.40x faster                                               |
| docutils       | 1.98 sec                                                        | 1.70 sec: 1.17x faster                                              |
| tornado_http   | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| Geometric mean | (ref)                                                           | 1.21x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 291 ms: 1.21x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 233 ms: 1.19x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 574 ms: 1.18x faster                                                |
| async_tree_io              | 693 ms                                                          | 591 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 477 ms: 1.15x faster                                                |
| Geometric mean             | (ref)                                                           | 1.19x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 74.7 ms: 1.70x faster                                               |
| float          | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                               |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                           | 1.35x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 94.7 ms: 1.36x faster                                               |
| regex_effbot   | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                               |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                               |
| Geometric mean | (ref)                                                           | 1.10x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 139 us: 1.51x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                              |
| pickle_pure_python   | 286 us                                                          | 206 us: 1.39x faster                                                |
| xml_etree_process    | 53.2 ms                                                         | 40.5 ms: 1.31x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 57.9 ms: 1.25x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.4 ms: 1.19x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.05x faster                                                |
| pickle_list          | 3.37 us                                                         | 3.22 us: 1.05x faster                                               |
| unpickle_list        | 2.95 us                                                         | 2.82 us: 1.05x faster                                               |
| json_loads           | 20.4 us                                                         | 20.1 us: 1.01x faster                                               |
| pickle               | 7.79 us                                                         | 7.74 us: 1.01x faster                                               |
| pickle_dict          | 19.9 us                                                         | 20.0 us: 1.00x slower                                               |
| unpickle             | 9.71 us                                                         | 9.87 us: 1.02x slower                                               |
| Geometric mean       | (ref)                                                           | 1.15x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                               |
| python_startup_no_site | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                               |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 6.75 ms: 1.47x faster                                               |
| django_template | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                               |
| Geometric mean  | (ref)                                                           | 1.38x faster                                                        |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| logging_silent             | 101 ns                                                          | 57.3 ns: 1.76x faster                                               |
| generators                 | 38.5 ms                                                         | 21.9 ms: 1.76x faster                                               |
| comprehensions             | 19.2 us                                                         | 11.0 us: 1.74x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 22.4 us: 1.71x faster                                               |
| nbody                      | 127 ms                                                          | 74.7 ms: 1.70x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.13 ms: 1.68x faster                                               |
| hexiom                     | 6.82 ms                                                         | 4.16 ms: 1.64x faster                                               |
| scimark_sor                | 130 ms                                                          | 79.3 ms: 1.64x faster                                               |
| raytrace                   | 308 ms                                                          | 192 ms: 1.61x faster                                                |
| scimark_lu                 | 93.2 ms                                                         | 58.7 ms: 1.59x faster                                               |
| spectral_norm              | 104 ms                                                          | 65.6 ms: 1.58x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 139 us: 1.51x faster                                                |
| scimark_monte_carlo        | 66.4 ms                                                         | 44.5 ms: 1.49x faster                                               |
| coroutines                 | 20.9 ms                                                         | 14.1 ms: 1.48x faster                                               |
| mako                       | 9.96 ms                                                         | 6.75 ms: 1.47x faster                                               |
| richards                   | 41.3 ms                                                         | 28.2 ms: 1.46x faster                                               |
| richards_super             | 46.5 ms                                                         | 31.8 ms: 1.46x faster                                               |
| chaos                      | 69.4 ms                                                         | 47.5 ms: 1.46x faster                                               |
| sqlglot_parse              | 1.25 ms                                                         | 856 us: 1.46x faster                                                |
| go                         | 137 ms                                                          | 94.3 ms: 1.46x faster                                               |
| float                      | 76.7 ms                                                         | 53.8 ms: 1.43x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.08 ms: 1.41x faster                                               |
| typing_runtime_protocols   | 126 us                                                          | 90.2 us: 1.40x faster                                               |
| chameleon                  | 7.75 ms                                                         | 5.53 ms: 1.40x faster                                               |
| tomli_loads                | 2.20 sec                                                        | 1.58 sec: 1.39x faster                                              |
| deepcopy_reduce            | 3.23 us                                                         | 2.32 us: 1.39x faster                                               |
| pickle_pure_python         | 286 us                                                          | 206 us: 1.39x faster                                                |
| nqueens                    | 93.7 ms                                                         | 67.6 ms: 1.39x faster                                               |
| deepcopy                   | 360 us                                                          | 261 us: 1.38x faster                                                |
| pyflate                    | 424 ms                                                          | 309 ms: 1.37x faster                                                |
| regex_compile              | 129 ms                                                          | 94.7 ms: 1.36x faster                                               |
| scimark_fft                | 271 ms                                                          | 201 ms: 1.35x faster                                                |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.91 ms: 1.33x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 52.3 ms: 1.32x faster                                               |
| fannkuch                   | 354 ms                                                          | 268 ms: 1.32x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 40.5 ms: 1.31x faster                                               |
| logging_simple             | 9.75 us                                                         | 7.53 us: 1.30x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.16 sec: 1.29x faster                                              |
| sqlglot_optimize           | 48.5 ms                                                         | 37.6 ms: 1.29x faster                                               |
| django_template            | 36.9 ms                                                         | 28.6 ms: 1.29x faster                                               |
| logging_format             | 10.4 us                                                         | 8.10 us: 1.28x faster                                               |
| pprint_safe_repr           | 721 ms                                                          | 565 ms: 1.27x faster                                                |
| pycparser                  | 978 ms                                                          | 777 ms: 1.26x faster                                                |
| sympy_sum                  | 123 ms                                                          | 98.5 ms: 1.25x faster                                               |
| sympy_integrate            | 17.5 ms                                                         | 14.1 ms: 1.25x faster                                               |
| xml_etree_generate         | 72.1 ms                                                         | 57.9 ms: 1.25x faster                                               |
| async_tree_none            | 298 ms                                                          | 241 ms: 1.24x faster                                                |
| sympy_str                  | 240 ms                                                          | 195 ms: 1.23x faster                                                |
| mdp                        | 1.91 sec                                                        | 1.58 sec: 1.21x faster                                              |
| async_tree_memoization     | 364 ms                                                          | 301 ms: 1.21x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 291 ms: 1.21x faster                                                |
| async_generators           | 313 ms                                                          | 261 ms: 1.20x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 233 ms: 1.19x faster                                                |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.4 ms: 1.19x faster                                               |
| 2to3                       | 280 ms                                                          | 237 ms: 1.18x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 574 ms: 1.18x faster                                                |
| async_tree_io              | 693 ms                                                          | 591 ms: 1.17x faster                                                |
| docutils                   | 1.98 sec                                                        | 1.70 sec: 1.17x faster                                              |
| sympy_expand               | 398 ms                                                          | 341 ms: 1.17x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 484 ms: 1.16x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 74.9 ms: 1.16x faster                                               |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 477 ms: 1.15x faster                                                |
| tornado_http               | 105 ms                                                          | 93.5 ms: 1.12x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 986 us: 1.12x faster                                                |
| json_dumps                 | 7.40 ms                                                         | 6.67 ms: 1.11x faster                                               |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.90 ms: 1.07x faster                                               |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                |
| asyncio_tcp                | 662 ms                                                          | 622 ms: 1.07x faster                                                |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.05x faster                                              |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.05x faster                                                |
| pickle_list                | 3.37 us                                                         | 3.22 us: 1.05x faster                                               |
| unpickle_list              | 2.95 us                                                         | 2.82 us: 1.05x faster                                               |
| gc_traversal               | 1.44 ms                                                         | 1.40 ms: 1.03x faster                                               |
| pathlib                    | 91.4 ms                                                         | 89.2 ms: 1.02x faster                                               |
| bench_mp_pool              | 75.4 ms                                                         | 74.1 ms: 1.02x faster                                               |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                |
| json                       | 4.15 ms                                                         | 4.10 ms: 1.01x faster                                               |
| json_loads                 | 20.4 us                                                         | 20.1 us: 1.01x faster                                               |
| pickle                     | 7.79 us                                                         | 7.74 us: 1.01x faster                                               |
| pickle_dict                | 19.9 us                                                         | 20.0 us: 1.00x slower                                               |
| unpickle                   | 9.71 us                                                         | 9.87 us: 1.02x slower                                               |
| python_startup             | 22.4 ms                                                         | 22.8 ms: 1.02x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.06x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 20.6 ms: 1.08x slower                                               |
| telco                      | 5.51 ms                                                         | 5.99 ms: 1.09x slower                                               |
| sqlglot_normalize          | 100 ms                                                          | 193 ms: 1.93x slower                                                |
| coverage                   | 48.4 ms                                                         | 497 ms: 10.26x slower                                               |
| Geometric mean             | (ref)                                                           | 1.21x faster                                                        |

Benchmark hidden because not significant (1): create_gc_cycles
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240312-3.13.0a5-076d169/bm-20240312-pythonperf1_win32-x86-python-v3.13.0a5-3.13.0a5-076d169.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: unknown