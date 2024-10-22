# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.13x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 251 ms: 1.11x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 516 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 460 ms: 1.23x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.31x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 96.8 ms: 1.31x faster                                                          |
| float          | 76.7 ms                                                         | 60.8 ms: 1.26x faster                                                          |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 171 us: 1.23x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 254 us: 1.12x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.3 ms: 1.08x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.07x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.38 ms: 1.19x faster                                                          |
| django_template | 36.9 ms                                                         | 32.3 ms: 1.14x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.16x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.5 us: 1.71x faster                                                          |
| deepcopy                   | 360 us                                                          | 247 us: 1.46x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.5 us: 1.42x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.40x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.7 ms: 1.39x faster                                                          |
| async_tree_none            | 298 ms                                                          | 217 ms: 1.37x faster                                                           |
| spectral_norm              | 104 ms                                                          | 75.8 ms: 1.37x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.64 ms: 1.36x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.7 ns: 1.35x faster                                                          |
| go                         | 137 ms                                                          | 102 ms: 1.35x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 70.2 ms: 1.33x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.43 us: 1.33x faster                                                          |
| scimark_sor                | 130 ms                                                          | 98.5 ms: 1.32x faster                                                          |
| nbody                      | 127 ms                                                          | 96.8 ms: 1.31x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 516 ms: 1.31x faster                                                           |
| raytrace                   | 308 ms                                                          | 236 ms: 1.31x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.27 ms: 1.29x faster                                                          |
| async_tree_io              | 693 ms                                                          | 537 ms: 1.29x faster                                                           |
| chaos                      | 69.4 ms                                                         | 54.6 ms: 1.27x faster                                                          |
| float                      | 76.7 ms                                                         | 60.8 ms: 1.26x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.92 us: 1.23x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 76.1 ms: 1.23x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 171 us: 1.23x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 460 ms: 1.23x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.55 us: 1.22x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.0 ms: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.8 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 456 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 357 ms: 1.19x faster                                                           |
| mako                       | 9.96 ms                                                         | 8.38 ms: 1.19x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.7 ms: 1.18x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.89 sec: 1.16x faster                                                         |
| sqlglot_parse              | 1.25 ms                                                         | 1.08 ms: 1.16x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.9 ms: 1.14x faster                                                          |
| django_template            | 36.9 ms                                                         | 32.3 ms: 1.14x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 42.8 ms: 1.13x faster                                                          |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 254 us: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.12x faster                                                         |
| scimark_fft                | 271 ms                                                          | 241 ms: 1.12x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.34 sec: 1.12x faster                                                         |
| pycparser                  | 978 ms                                                          | 878 ms: 1.11x faster                                                           |
| 2to3                       | 280 ms                                                          | 251 ms: 1.11x faster                                                           |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.11x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 651 ms: 1.11x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.3 ms: 1.08x faster                                                          |
| fannkuch                   | 354 ms                                                          | 328 ms: 1.08x faster                                                           |
| richards                   | 41.3 ms                                                         | 38.5 ms: 1.07x faster                                                          |
| richards_super             | 46.5 ms                                                         | 43.3 ms: 1.07x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| xml_etree_generate         | 72.1 ms                                                         | 67.9 ms: 1.06x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.2 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                          |
| sympy_expand               | 398 ms                                                          | 379 ms: 1.05x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.05x faster                                                           |
| async_generators           | 313 ms                                                          | 299 ms: 1.05x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 87.8 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| regex_dna                  | 127 ms                                                          | 123 ms: 1.03x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.42 ms: 1.02x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 74.9 ms: 1.01x faster                                                          |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.19 ms: 1.01x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.0 ms: 1.05x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.5 ms: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.2 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 745 ms: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 751 us: 1.15x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.19x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.92 ms: 1.25x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 223 ms: 2.23x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): json_loads, tornado_http, json_dumps
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown