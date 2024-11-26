# Results vs. 3.12.0

- fork: mdboom
- ref: simplify_richcompare
- machine: windows-x86
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.134x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| Geometric mean | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.41x faster                                                           |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.31x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.32x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 96.0 ms: 1.32x faster                                                          |
| float          | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                          |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.18x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| regex_dna      | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                          |
| Geometric mean | (ref)                                                           | 1.05x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                         |
| unpickle_pure_python | 210 us                                                          | 179 us: 1.17x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 251 us: 1.14x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| json_loads           | 20.4 us                                                         | 21.1 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.09x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.7 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.05x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.20 ms: 1.21x faster                                                          |
| django_template | 36.9 ms                                                         | 32.9 ms: 1.12x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.17x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.0 us: 1.74x faster                                                          |
| deepcopy                   | 360 us                                                          | 238 us: 1.51x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 247 ms: 1.42x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.41x faster                                                          |
| async_tree_none_tg         | 278 ms                                                          | 198 ms: 1.41x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.6 ms: 1.39x faster                                                          |
| async_tree_none            | 298 ms                                                          | 216 ms: 1.38x faster                                                           |
| logging_silent             | 101 ns                                                          | 74.8 ns: 1.35x faster                                                          |
| spectral_norm              | 104 ms                                                          | 76.9 ms: 1.35x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 272 ms: 1.34x faster                                                           |
| raytrace                   | 308 ms                                                          | 231 ms: 1.33x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 70.0 ms: 1.33x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 509 ms: 1.33x faster                                                           |
| go                         | 137 ms                                                          | 104 ms: 1.32x faster                                                           |
| nbody                      | 127 ms                                                          | 96.0 ms: 1.32x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.46 us: 1.31x faster                                                          |
| async_tree_io              | 693 ms                                                          | 531 ms: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.30x faster                                                          |
| chaos                      | 69.4 ms                                                         | 54.1 ms: 1.28x faster                                                          |
| scimark_sor                | 130 ms                                                          | 102 ms: 1.27x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.36 ms: 1.27x faster                                                          |
| float                      | 76.7 ms                                                         | 61.5 ms: 1.25x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.92 us: 1.23x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.15 ms: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.20 ms: 1.21x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 465 ms: 1.21x faster                                                           |
| regex_compile              | 129 ms                                                          | 107 ms: 1.20x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.65 us: 1.20x faster                                                          |
| dulwich_log                | 58.5 ms                                                         | 49.2 ms: 1.19x faster                                                          |
| pyflate                    | 424 ms                                                          | 358 ms: 1.19x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.86 sec: 1.18x faster                                                         |
| nqueens                    | 93.7 ms                                                         | 79.3 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 463 ms: 1.18x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 56.4 ms: 1.18x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 17.8 ms: 1.17x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 179 us: 1.17x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 59.5 ms: 1.16x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.07 ms: 1.16x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 107 ms: 1.15x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.33 ms: 1.15x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.7 ms: 1.15x faster                                                          |
| scimark_fft                | 271 ms                                                          | 237 ms: 1.14x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 251 us: 1.14x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.5 ms: 1.13x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.32 sec: 1.13x faster                                                         |
| sqlglot_optimize           | 48.5 ms                                                         | 42.9 ms: 1.13x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.70 sec: 1.13x faster                                                         |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| django_template            | 36.9 ms                                                         | 32.9 ms: 1.12x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 643 ms: 1.12x faster                                                           |
| sympy_str                  | 240 ms                                                          | 216 ms: 1.11x faster                                                           |
| pycparser                  | 978 ms                                                          | 888 ms: 1.10x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.01 ms: 1.09x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 67.3 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.86 sec: 1.07x faster                                                         |
| xml_etree_process          | 53.2 ms                                                         | 50.0 ms: 1.06x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.0 ms: 1.06x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 107 ms: 1.06x faster                                                           |
| async_generators           | 313 ms                                                          | 297 ms: 1.06x faster                                                           |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 86.9 ms: 1.05x faster                                                          |
| regex_dna                  | 127 ms                                                          | 121 ms: 1.05x faster                                                           |
| fannkuch                   | 354 ms                                                          | 342 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 384 ms: 1.04x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.1 sec: 1.03x faster                                                         |
| bench_mp_pool              | 75.4 ms                                                         | 73.2 ms: 1.03x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.46 ms: 1.01x slower                                                          |
| richards_super             | 46.5 ms                                                         | 46.9 ms: 1.01x slower                                                          |
| richards                   | 41.3 ms                                                         | 41.9 ms: 1.01x slower                                                          |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                           |
| json                       | 4.15 ms                                                         | 4.28 ms: 1.03x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.1 us: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.7 ms: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 23.8 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 51.8 ms: 1.07x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 716 ms: 1.08x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.4 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 754 us: 1.16x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 149 us: 1.18x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.77 ms: 1.23x slower                                                          |
| sqlglot_normalize          | 100 ms                                                          | 223 ms: 2.23x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (2): tornado_http, gc_traversal
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-pythonperf1_win32-x86-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.134x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown