# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: windows-x86
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 256 ms: 1.09x faster                                                |
| chameleon      | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                               |
| docutils       | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                              |
| tornado_http   | 105 ms                                                          | 99.9 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                           | 1.13x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 298 ms                                                          | 260 ms: 1.15x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 313 ms: 1.12x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 325 ms: 1.12x faster                                                |
| async_tree_io              | 693 ms                                                          | 624 ms: 1.11x faster                                                |
| async_tree_io_tg           | 677 ms                                                          | 612 ms: 1.11x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 503 ms: 1.09x faster                                                |
| Geometric mean             | (ref)                                                           | 1.11x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                               |
| nbody          | 127 ms                                                          | 89.7 ms: 1.42x faster                                               |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                           | 1.26x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 110 ms: 1.17x faster                                                |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.06x faster                                               |
| regex_dna      | 127 ms                                                          | 120 ms: 1.06x faster                                                |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                               |
| Geometric mean | (ref)                                                           | 1.05x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 156 us: 1.35x faster                                                |
| tomli_loads          | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                              |
| pickle_pure_python   | 286 us                                                          | 223 us: 1.28x faster                                                |
| xml_etree_process    | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                               |
| xml_etree_generate   | 72.1 ms                                                         | 60.2 ms: 1.20x faster                                               |
| xml_etree_iterparse  | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                               |
| json_dumps           | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                               |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.03x faster                                                |
| unpickle_list        | 2.95 us                                                         | 2.87 us: 1.03x faster                                               |
| pickle               | 7.79 us                                                         | 8.11 us: 1.04x slower                                               |
| unpickle             | 9.71 us                                                         | 10.1 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                        |

Benchmark hidden because not significant (3): pickle_list, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 22.4 ms                                                         | 22.5 ms: 1.01x slower                                               |
| python_startup_no_site | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                               |
| Geometric mean         | (ref)                                                           | 1.04x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 9.96 ms                                                         | 7.43 ms: 1.34x faster                                               |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf1_win32-x86-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 24.6 ms: 1.57x faster                                               |
| deepcopy_memo              | 38.4 us                                                         | 25.3 us: 1.52x faster                                               |
| logging_silent             | 101 ns                                                          | 67.1 ns: 1.51x faster                                               |
| unpack_sequence            | 62.5 ns                                                         | 42.6 ns: 1.47x faster                                               |
| scimark_sor                | 130 ms                                                          | 89.6 ms: 1.45x faster                                               |
| float                      | 76.7 ms                                                         | 53.9 ms: 1.42x faster                                               |
| scimark_lu                 | 93.2 ms                                                         | 65.6 ms: 1.42x faster                                               |
| spectral_norm              | 104 ms                                                          | 73.2 ms: 1.42x faster                                               |
| nbody                      | 127 ms                                                          | 89.7 ms: 1.42x faster                                               |
| coroutines                 | 20.9 ms                                                         | 14.9 ms: 1.40x faster                                               |
| deltablue                  | 3.58 ms                                                         | 2.58 ms: 1.39x faster                                               |
| comprehensions             | 19.2 us                                                         | 14.1 us: 1.36x faster                                               |
| unpickle_pure_python       | 210 us                                                          | 156 us: 1.35x faster                                                |
| mako                       | 9.96 ms                                                         | 7.43 ms: 1.34x faster                                               |
| tomli_loads                | 2.20 sec                                                        | 1.65 sec: 1.33x faster                                              |
| sqlglot_parse              | 1.25 ms                                                         | 961 us: 1.30x faster                                                |
| chameleon                  | 7.75 ms                                                         | 6.01 ms: 1.29x faster                                               |
| deepcopy_reduce            | 3.23 us                                                         | 2.51 us: 1.29x faster                                               |
| richards                   | 41.3 ms                                                         | 32.2 ms: 1.28x faster                                               |
| raytrace                   | 308 ms                                                          | 240 ms: 1.28x faster                                                |
| pickle_pure_python         | 286 us                                                          | 223 us: 1.28x faster                                                |
| typing_runtime_protocols   | 126 us                                                          | 98.7 us: 1.28x faster                                               |
| richards_super             | 46.5 ms                                                         | 36.5 ms: 1.27x faster                                               |
| sqlglot_transpile          | 1.53 ms                                                         | 1.21 ms: 1.26x faster                                               |
| deepcopy                   | 360 us                                                          | 285 us: 1.26x faster                                                |
| xml_etree_process          | 53.2 ms                                                         | 42.8 ms: 1.24x faster                                               |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                               |
| xml_etree_generate         | 72.1 ms                                                         | 60.2 ms: 1.20x faster                                               |
| xml_etree_iterparse        | 77.6 ms                                                         | 65.9 ms: 1.18x faster                                               |
| regex_compile              | 129 ms                                                          | 110 ms: 1.17x faster                                                |
| logging_simple             | 9.75 us                                                         | 8.35 us: 1.17x faster                                               |
| logging_format             | 10.4 us                                                         | 8.97 us: 1.16x faster                                               |
| async_tree_none            | 298 ms                                                          | 260 ms: 1.15x faster                                                |
| pyflate                    | 424 ms                                                          | 370 ms: 1.15x faster                                                |
| chaos                      | 69.4 ms                                                         | 61.0 ms: 1.14x faster                                               |
| crypto_pyaes               | 69.2 ms                                                         | 61.0 ms: 1.13x faster                                               |
| scimark_fft                | 271 ms                                                          | 239 ms: 1.13x faster                                                |
| async_tree_none_tg         | 278 ms                                                          | 246 ms: 1.13x faster                                                |
| go                         | 137 ms                                                          | 123 ms: 1.12x faster                                                |
| async_tree_memoization_tg  | 350 ms                                                          | 313 ms: 1.12x faster                                                |
| async_tree_memoization     | 364 ms                                                          | 325 ms: 1.12x faster                                                |
| sqlite_synth               | 2.07 us                                                         | 1.85 us: 1.12x faster                                               |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.11x faster                                                |
| async_tree_io              | 693 ms                                                          | 624 ms: 1.11x faster                                                |
| sqlglot_optimize           | 48.5 ms                                                         | 43.7 ms: 1.11x faster                                               |
| async_tree_io_tg           | 677 ms                                                          | 612 ms: 1.11x faster                                                |
| fannkuch                   | 354 ms                                                          | 322 ms: 1.10x faster                                                |
| sympy_integrate            | 17.5 ms                                                         | 16.0 ms: 1.10x faster                                               |
| pycparser                  | 978 ms                                                          | 891 ms: 1.10x faster                                                |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 515 ms: 1.10x faster                                                |
| 2to3                       | 280 ms                                                          | 256 ms: 1.09x faster                                                |
| docutils                   | 1.98 sec                                                        | 1.82 sec: 1.09x faster                                              |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 503 ms: 1.09x faster                                                |
| pathlib                    | 91.4 ms                                                         | 84.3 ms: 1.08x faster                                               |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                               |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.06x faster                                               |
| json_dumps                 | 7.40 ms                                                         | 6.95 ms: 1.06x faster                                               |
| regex_dna                  | 127 ms                                                          | 120 ms: 1.06x faster                                                |
| nqueens                    | 93.7 ms                                                         | 88.7 ms: 1.06x faster                                               |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.7 sec: 1.05x faster                                              |
| bench_mp_pool              | 75.4 ms                                                         | 71.5 ms: 1.05x faster                                               |
| tornado_http               | 105 ms                                                          | 99.9 ms: 1.05x faster                                               |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                |
| asyncio_tcp                | 662 ms                                                          | 632 ms: 1.05x faster                                                |
| async_generators           | 313 ms                                                          | 300 ms: 1.05x faster                                                |
| meteor_contest             | 86.9 ms                                                         | 83.8 ms: 1.04x faster                                               |
| mdp                        | 1.91 sec                                                        | 1.85 sec: 1.04x faster                                              |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.03x faster                                                |
| hexiom                     | 6.82 ms                                                         | 6.61 ms: 1.03x faster                                               |
| unpickle_list              | 2.95 us                                                         | 2.87 us: 1.03x faster                                               |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.02x faster                                               |
| pprint_pformat             | 1.50 sec                                                        | 1.47 sec: 1.02x faster                                              |
| pprint_safe_repr           | 721 ms                                                          | 713 ms: 1.01x faster                                                |
| python_startup             | 22.4 ms                                                         | 22.5 ms: 1.01x slower                                               |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                |
| json                       | 4.15 ms                                                         | 4.27 ms: 1.03x slower                                               |
| pickle                     | 7.79 us                                                         | 8.11 us: 1.04x slower                                               |
| unpickle                   | 9.71 us                                                         | 10.1 us: 1.04x slower                                               |
| python_startup_no_site     | 19.1 ms                                                         | 20.3 ms: 1.07x slower                                               |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.07x slower                                               |
| scimark_monte_carlo        | 66.4 ms                                                         | 71.6 ms: 1.08x slower                                               |
| telco                      | 5.51 ms                                                         | 6.55 ms: 1.19x slower                                               |
| dask                       | 323 ms                                                          | 432 ms: 1.34x slower                                                |
| sqlglot_normalize          | 100 ms                                                          | 224 ms: 2.23x slower                                                |
| coverage                   | 48.4 ms                                                         | 464 ms: 9.59x slower                                                |
| Geometric mean             | (ref)                                                           | 1.10x faster                                                        |

Benchmark hidden because not significant (4): create_gc_cycles, pickle_list, pickle_dict, json_loads
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x


# Memory

- memory change: unknown