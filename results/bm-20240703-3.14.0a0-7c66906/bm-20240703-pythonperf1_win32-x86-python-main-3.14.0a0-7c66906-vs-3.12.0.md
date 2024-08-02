# Results vs. 3.12.0

- fork: python
- ref: main
- machine: windows-x86
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.16x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 249 ms: 1.13x faster                                           |
| docutils       | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                         |
| tornado_http   | 105 ms                                                          | 95.4 ms: 1.10x faster                                          |
| Geometric mean | (ref)                                                           | 1.10x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 192 ms: 1.45x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 242 ms: 1.45x faster                                           |
| async_tree_io_tg           | 677 ms                                                          | 494 ms: 1.37x faster                                           |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                           |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                           |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 463 ms: 1.22x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                           |
| Geometric mean             | (ref)                                                           | 1.33x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.9 ms: 1.35x faster                                          |
| float          | 76.7 ms                                                         | 60.0 ms: 1.28x faster                                          |
| Geometric mean | (ref)                                                           | 1.20x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 106 ms: 1.22x faster                                           |
| regex_effbot   | 2.04 ms                                                         | 1.87 ms: 1.09x faster                                          |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                           |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                           | 1.08x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                         |
| unpickle_pure_python | 210 us                                                          | 170 us: 1.23x faster                                           |
| pickle_pure_python   | 286 us                                                          | 245 us: 1.17x faster                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                          |
| xml_etree_generate   | 72.1 ms                                                         | 66.0 ms: 1.09x faster                                          |
| xml_etree_parse      | 113 ms                                                          | 105 ms: 1.08x faster                                           |
| xml_etree_process    | 53.2 ms                                                         | 49.8 ms: 1.07x faster                                          |
| json_dumps           | 7.40 ms                                                         | 6.93 ms: 1.07x faster                                          |
| Geometric mean       | (ref)                                                           | 1.12x faster                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                          |
| Geometric mean | (ref)                                                           | 1.01x slower                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|-----------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.93 ms: 1.25x faster                                          |
| django_template | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                          |
| Geometric mean  | (ref)                                                           | 1.18x faster                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906 |
|----------------------------|:---------------------------------------------------------------:|:--------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 21.6 us: 1.77x faster                                          |
| deepcopy                   | 360 us                                                          | 241 us: 1.49x faster                                           |
| async_tree_none_tg         | 278 ms                                                          | 192 ms: 1.45x faster                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 242 ms: 1.45x faster                                           |
| generators                 | 38.5 ms                                                         | 27.0 ms: 1.43x faster                                          |
| comprehensions             | 19.2 us                                                         | 13.6 us: 1.42x faster                                          |
| raytrace                   | 308 ms                                                          | 220 ms: 1.40x faster                                           |
| spectral_norm              | 104 ms                                                          | 75.3 ms: 1.38x faster                                          |
| async_tree_io_tg           | 677 ms                                                          | 494 ms: 1.37x faster                                           |
| scimark_lu                 | 93.2 ms                                                         | 68.4 ms: 1.36x faster                                          |
| logging_silent             | 101 ns                                                          | 74.2 ns: 1.36x faster                                          |
| nbody                      | 127 ms                                                          | 93.9 ms: 1.35x faster                                          |
| async_tree_none            | 298 ms                                                          | 221 ms: 1.35x faster                                           |
| deltablue                  | 3.58 ms                                                         | 2.66 ms: 1.35x faster                                          |
| async_tree_memoization     | 364 ms                                                          | 270 ms: 1.35x faster                                           |
| hexiom                     | 6.82 ms                                                         | 5.12 ms: 1.33x faster                                          |
| scimark_sor                | 130 ms                                                          | 98.4 ms: 1.32x faster                                          |
| chaos                      | 69.4 ms                                                         | 52.6 ms: 1.32x faster                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.45 us: 1.32x faster                                          |
| async_tree_io              | 693 ms                                                          | 536 ms: 1.29x faster                                           |
| float                      | 76.7 ms                                                         | 60.0 ms: 1.28x faster                                          |
| mako                       | 9.96 ms                                                         | 7.93 ms: 1.25x faster                                          |
| pyflate                    | 424 ms                                                          | 338 ms: 1.25x faster                                           |
| logging_simple             | 9.75 us                                                         | 7.82 us: 1.25x faster                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.10 ms: 1.24x faster                                          |
| tomli_loads                | 2.20 sec                                                        | 1.77 sec: 1.24x faster                                         |
| nqueens                    | 93.7 ms                                                         | 75.5 ms: 1.24x faster                                          |
| unpickle_pure_python       | 210 us                                                          | 170 us: 1.23x faster                                           |
| scimark_fft                | 271 ms                                                          | 220 ms: 1.23x faster                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 54.0 ms: 1.23x faster                                          |
| regex_compile              | 129 ms                                                          | 106 ms: 1.22x faster                                           |
| logging_format             | 10.4 us                                                         | 8.52 us: 1.22x faster                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 463 ms: 1.22x faster                                           |
| go                         | 137 ms                                                          | 114 ms: 1.21x faster                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.7 ms: 1.20x faster                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.04 ms: 1.20x faster                                          |
| coroutines                 | 20.9 ms                                                         | 17.5 ms: 1.19x faster                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.19x faster                                          |
| pickle_pure_python         | 286 us                                                          | 245 us: 1.17x faster                                           |
| pycparser                  | 978 ms                                                          | 841 ms: 1.16x faster                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 67.1 ms: 1.16x faster                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.30 sec: 1.15x faster                                         |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                         |
| sympy_integrate            | 17.5 ms                                                         | 15.4 ms: 1.14x faster                                          |
| bench_thread_pool          | 1.10 ms                                                         | 971 us: 1.14x faster                                           |
| sympy_sum                  | 123 ms                                                          | 109 ms: 1.13x faster                                           |
| pprint_safe_repr           | 721 ms                                                          | 638 ms: 1.13x faster                                           |
| 2to3                       | 280 ms                                                          | 249 ms: 1.13x faster                                           |
| richards                   | 41.3 ms                                                         | 37.1 ms: 1.11x faster                                          |
| django_template            | 36.9 ms                                                         | 33.2 ms: 1.11x faster                                          |
| fannkuch                   | 354 ms                                                          | 318 ms: 1.11x faster                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.7 ms: 1.11x faster                                          |
| sympy_str                  | 240 ms                                                          | 217 ms: 1.10x faster                                           |
| tornado_http               | 105 ms                                                          | 95.4 ms: 1.10x faster                                          |
| pathlib                    | 91.4 ms                                                         | 83.5 ms: 1.09x faster                                          |
| richards_super             | 46.5 ms                                                         | 42.5 ms: 1.09x faster                                          |
| async_generators           | 313 ms                                                          | 287 ms: 1.09x faster                                           |
| xml_etree_generate         | 72.1 ms                                                         | 66.0 ms: 1.09x faster                                          |
| meteor_contest             | 86.9 ms                                                         | 79.7 ms: 1.09x faster                                          |
| regex_effbot               | 2.04 ms                                                         | 1.87 ms: 1.09x faster                                          |
| xml_etree_parse            | 113 ms                                                          | 105 ms: 1.08x faster                                           |
| bench_mp_pool              | 75.4 ms                                                         | 70.4 ms: 1.07x faster                                          |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                           |
| xml_etree_process          | 53.2 ms                                                         | 49.8 ms: 1.07x faster                                          |
| json_dumps                 | 7.40 ms                                                         | 6.93 ms: 1.07x faster                                          |
| docutils                   | 1.98 sec                                                        | 1.87 sec: 1.06x faster                                         |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.8 sec: 1.05x faster                                         |
| sympy_expand               | 398 ms                                                          | 383 ms: 1.04x faster                                           |
| gc_traversal               | 1.44 ms                                                         | 1.43 ms: 1.01x faster                                          |
| python_startup             | 22.4 ms                                                         | 23.1 ms: 1.03x slower                                          |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                          |
| coverage                   | 48.4 ms                                                         | 51.3 ms: 1.06x slower                                          |
| telco                      | 5.51 ms                                                         | 6.02 ms: 1.09x slower                                          |
| create_gc_cycles           | 652 us                                                          | 753 us: 1.16x slower                                           |
| typing_runtime_protocols   | 126 us                                                          | 151 us: 1.20x slower                                           |
| sqlglot_normalize          | 100 ms                                                          | 228 ms: 2.28x slower                                           |
| Geometric mean             | (ref)                                                           | 1.16x faster                                                   |

Benchmark hidden because not significant (5): json, python_startup_no_site, asyncio_tcp, json_loads, pidigits
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, dulwich_log, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240703-3.14.0a0-7c66906/bm-20240703-pythonperf1_win32-x86-python-main-3.14.0a0-7c66906.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown