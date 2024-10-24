# Results vs. 3.12.0

- fork: python
- ref: a2bec77d25b11f50362a
- machine: windows-x86
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| tornado_http   | 105 ms                                                          | 95.0 ms: 1.11x faster                                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 506 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.33x faster                                                           |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 89.0 ms: 1.43x faster                                                          |
| float          | 76.7 ms                                                         | 58.9 ms: 1.30x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.24x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| regex_dna      | 127 ms                                                          | 124 ms: 1.03x faster                                                           |
| regex_v8       | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 167 us: 1.26x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.79 sec: 1.22x faster                                                         |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.0 ms: 1.18x faster                                                          |
| pickle_pure_python   | 286 us                                                          | 250 us: 1.14x faster                                                           |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.7 ms: 1.07x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| json_loads           | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.11x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.95 ms: 1.25x faster                                                          |
| django_template | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.4 us: 1.80x faster                                                          |
| deepcopy                   | 360 us                                                          | 241 us: 1.50x faster                                                           |
| generators                 | 38.5 ms                                                         | 26.6 ms: 1.45x faster                                                          |
| comprehensions             | 19.2 us                                                         | 13.3 us: 1.44x faster                                                          |
| raytrace                   | 308 ms                                                          | 215 ms: 1.43x faster                                                           |
| nbody                      | 127 ms                                                          | 89.0 ms: 1.43x faster                                                          |
| async_tree_memoization_tg  | 350 ms                                                          | 246 ms: 1.42x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 67.2 ms: 1.39x faster                                                          |
| spectral_norm              | 104 ms                                                          | 75.3 ms: 1.38x faster                                                          |
| deltablue                  | 3.58 ms                                                         | 2.61 ms: 1.37x faster                                                          |
| scimark_sor                | 130 ms                                                          | 95.0 ms: 1.37x faster                                                          |
| hexiom                     | 6.82 ms                                                         | 5.01 ms: 1.36x faster                                                          |
| logging_silent             | 101 ns                                                          | 74.9 ns: 1.35x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 506 ms: 1.34x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 273 ms: 1.33x faster                                                           |
| async_tree_none            | 298 ms                                                          | 225 ms: 1.33x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.47 us: 1.31x faster                                                          |
| float                      | 76.7 ms                                                         | 58.9 ms: 1.30x faster                                                          |
| chaos                      | 69.4 ms                                                         | 53.8 ms: 1.29x faster                                                          |
| nqueens                    | 93.7 ms                                                         | 73.1 ms: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 546 ms: 1.27x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 52.4 ms: 1.27x faster                                                          |
| pyflate                    | 424 ms                                                          | 335 ms: 1.26x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.74 us: 1.26x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 167 us: 1.26x faster                                                           |
| mako                       | 9.96 ms                                                         | 7.95 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.09 ms: 1.25x faster                                                          |
| regex_compile              | 129 ms                                                          | 103 ms: 1.25x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.43 us: 1.23x faster                                                          |
| scimark_fft                | 271 ms                                                          | 220 ms: 1.23x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.79 sec: 1.22x faster                                                         |
| coroutines                 | 20.9 ms                                                         | 17.2 ms: 1.22x faster                                                          |
| go                         | 137 ms                                                          | 114 ms: 1.21x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.7 ms: 1.20x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.28 ms: 1.19x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.05 ms: 1.19x faster                                                          |
| pycparser                  | 978 ms                                                          | 824 ms: 1.19x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.0 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 466 ms: 1.17x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.30 sec: 1.16x faster                                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.3 ms: 1.15x faster                                                          |
| fannkuch                   | 354 ms                                                          | 309 ms: 1.14x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 250 us: 1.14x faster                                                           |
| richards_super             | 46.5 ms                                                         | 40.7 ms: 1.14x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 108 ms: 1.14x faster                                                           |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 634 ms: 1.14x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.1 ms: 1.13x faster                                                          |
| 2to3                       | 280 ms                                                          | 249 ms: 1.12x faster                                                           |
| richards                   | 41.3 ms                                                         | 36.8 ms: 1.12x faster                                                          |
| bench_thread_pool          | 1.10 ms                                                         | 990 us: 1.11x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 82.2 ms: 1.11x faster                                                          |
| django_template            | 36.9 ms                                                         | 33.3 ms: 1.11x faster                                                          |
| tornado_http               | 105 ms                                                          | 95.0 ms: 1.11x faster                                                          |
| sympy_str                  | 240 ms                                                          | 218 ms: 1.10x faster                                                           |
| async_generators           | 313 ms                                                          | 285 ms: 1.10x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 79.1 ms: 1.10x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.07x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.7 ms: 1.07x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 70.5 ms: 1.07x faster                                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                                         |
| regex_effbot               | 2.04 ms                                                         | 1.92 ms: 1.06x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 68.3 ms: 1.06x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                                         |
| sympy_expand               | 398 ms                                                          | 381 ms: 1.04x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 7.14 ms: 1.04x faster                                                          |
| regex_dna                  | 127 ms                                                          | 124 ms: 1.03x faster                                                           |
| pidigits                   | 199 ms                                                          | 196 ms: 1.01x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                                          |
| python_startup             | 22.4 ms                                                         | 22.9 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 21.2 us: 1.04x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.0 ms: 1.06x slower                                                          |
| json                       | 4.15 ms                                                         | 4.41 ms: 1.06x slower                                                          |
| coverage                   | 48.4 ms                                                         | 52.6 ms: 1.09x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 748 us: 1.15x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.35 ms: 1.15x slower                                                          |
| typing_runtime_protocols   | 126 us                                                          | 153 us: 1.21x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 226 ms: 2.25x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                                   |

Benchmark hidden because not significant (2): asyncio_tcp, python_startup_no_site
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240713-3.14.0a0-a2bec77/bm-20240713-pythonperf1_win32-x86-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown