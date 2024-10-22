# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.14x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.40x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 94.3 ms: 1.35x faster                                                          |
| float          | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| pidigits       | 199 ms                                                          | 201 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| regex_dna      | 127 ms                                                          | 118 ms: 1.07x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 183 us: 1.15x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 68.8 ms: 1.13x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 263 us: 1.09x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.5 ms: 1.07x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| Geometric mean       | (ref)                                                           | 1.08x faster                                                                   |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.08x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.24 ms: 1.21x faster                                                          |
| django_template | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.2 us: 1.73x faster                                                          |
| deepcopy                   | 360 us                                                          | 242 us: 1.49x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.8 ms: 1.44x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 249 ms: 1.41x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.7 us: 1.41x faster                                                          |
| async_tree_none            | 298 ms                                                          | 213 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 199 ms: 1.40x faster                                                           |
| logging_silent             | 101 ns                                                          | 73.1 ns: 1.38x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 68.7 ms: 1.36x faster                                                          |
| nbody                      | 127 ms                                                          | 94.3 ms: 1.35x faster                                                          |
| raytrace                   | 308 ms                                                          | 229 ms: 1.35x faster                                                           |
| spectral_norm              | 104 ms                                                          | 77.6 ms: 1.34x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.42 us: 1.33x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 274 ms: 1.33x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.71 ms: 1.32x faster                                                          |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 515 ms: 1.32x faster                                                           |
| chaos                      | 69.4 ms                                                         | 52.8 ms: 1.31x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.20 ms: 1.31x faster                                                          |
| async_tree_io              | 693 ms                                                          | 533 ms: 1.30x faster                                                           |
| scimark_sor                | 130 ms                                                          | 103 ms: 1.26x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 75.3 ms: 1.24x faster                                                          |
| float                      | 76.7 ms                                                         | 62.2 ms: 1.23x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.14 ms: 1.23x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.94 us: 1.23x faster                                                          |
| crypto_pyaes               | 69.2 ms                                                         | 56.7 ms: 1.22x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 464 ms: 1.22x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.61 us: 1.21x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.24 ms: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.4 ms: 1.20x faster                                                          |
| pyflate                    | 424 ms                                                          | 354 ms: 1.20x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.84 sec: 1.19x faster                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 460 ms: 1.19x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.9 ms: 1.17x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.4 ms: 1.16x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.32 ms: 1.16x faster                                                          |
| django_template            | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 183 us: 1.15x faster                                                           |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.14x faster                                                           |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                           |
| pycparser                  | 978 ms                                                          | 862 ms: 1.13x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                         |
| xml_etree_iterparse        | 77.6 ms                                                         | 68.8 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 248 ms: 1.13x faster                                                           |
| pprint_safe_repr           | 721 ms                                                          | 642 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 215 ms: 1.12x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 43.8 ms: 1.11x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 263 us: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.03 ms: 1.08x faster                                                          |
| async_generators           | 313 ms                                                          | 292 ms: 1.07x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.07x faster                                                           |
| xml_etree_generate         | 72.1 ms                                                         | 67.5 ms: 1.07x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 49.9 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| richards_super             | 46.5 ms                                                         | 43.9 ms: 1.06x faster                                                          |
| fannkuch                   | 354 ms                                                          | 336 ms: 1.05x faster                                                           |
| richards                   | 41.3 ms                                                         | 39.4 ms: 1.05x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.8 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 87.4 ms: 1.05x faster                                                          |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 109 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 73.2 ms: 1.03x faster                                                          |
| pidigits                   | 199 ms                                                          | 201 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.30 ms: 1.04x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 20.1 ms: 1.05x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.08x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 722 ms: 1.09x slower                                                           |
| coverage                   | 48.4 ms                                                         | 53.6 ms: 1.11x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 143 us: 1.13x slower                                                           |
| create_gc_cycles           | 652 us                                                          | 744 us: 1.14x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.69 ms: 1.21x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 225 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.14x faster                                                                   |

Benchmark hidden because not significant (4): tornado_http, json_loads, json_dumps, gc_traversal
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown