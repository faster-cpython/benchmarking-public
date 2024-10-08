# Results vs. 3.12.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: windows-x86
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.20x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 258 ms: 1.08x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                         |
| tornado_http   | 105 ms                                                          | 106 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 507 ms: 1.34x faster                                                           |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.30x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 52.3 ms: 2.43x faster                                                          |
| float          | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                          |
| pidigits       | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| Geometric mean | (ref)                                                           | 1.64x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 95.2 ms: 1.36x faster                                                          |
| regex_dna      | 127 ms                                                          | 128 ms: 1.01x slower                                                           |
| regex_effbot   | 2.04 ms                                                         | 2.08 ms: 1.02x slower                                                          |
| regex_v8       | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 146 us: 1.43x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.55 sec: 1.42x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 213 us: 1.34x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 57.7 ms: 1.25x faster                                                          |
| xml_etree_iterparse  | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 43.7 ms: 1.22x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 7.09 ms: 1.04x faster                                                          |
| json_loads           | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.21x faster                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 5.49 ms: 1.81x faster                                                          |
| django_template | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.41x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody                      | 127 ms                                                          | 52.3 ms: 2.43x faster                                                          |
| deepcopy_memo              | 38.4 us                                                         | 15.8 us: 2.43x faster                                                          |
| spectral_norm              | 104 ms                                                          | 47.7 ms: 2.18x faster                                                          |
| mako                       | 9.96 ms                                                         | 5.49 ms: 1.81x faster                                                          |
| float                      | 76.7 ms                                                         | 43.0 ms: 1.78x faster                                                          |
| logging_silent             | 101 ns                                                          | 57.7 ns: 1.75x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 2.31 ms: 1.67x faster                                                          |
| scimark_fft                | 271 ms                                                          | 165 ms: 1.64x faster                                                           |
| comprehensions             | 19.2 us                                                         | 11.8 us: 1.63x faster                                                          |
| pyflate                    | 424 ms                                                          | 261 ms: 1.62x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 41.6 ms: 1.60x faster                                                          |
| fannkuch                   | 354 ms                                                          | 233 ms: 1.52x faster                                                           |
| deepcopy                   | 360 us                                                          | 249 us: 1.44x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 4.73 ms: 1.44x faster                                                          |
| unpickle_pure_python       | 210 us                                                          | 146 us: 1.43x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 48.3 ms: 1.43x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.55 sec: 1.42x faster                                                         |
| async_tree_none_tg         | 278 ms                                                          | 197 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 250 ms: 1.40x faster                                                           |
| regex_compile              | 129 ms                                                          | 95.2 ms: 1.36x faster                                                          |
| generators                 | 38.5 ms                                                         | 28.5 ms: 1.35x faster                                                          |
| raytrace                   | 308 ms                                                          | 228 ms: 1.35x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 213 us: 1.34x faster                                                           |
| scimark_sor                | 130 ms                                                          | 96.9 ms: 1.34x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 507 ms: 1.34x faster                                                           |
| chaos                      | 69.4 ms                                                         | 52.8 ms: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 226 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 277 ms: 1.31x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.75 ms: 1.30x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 965 us: 1.29x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 73.0 ms: 1.28x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.52 us: 1.28x faster                                                          |
| async_tree_io              | 693 ms                                                          | 548 ms: 1.27x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 73.9 ms: 1.26x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 57.7 ms: 1.25x faster                                                          |
| sqlglot_transpile          | 1.53 ms                                                         | 1.23 ms: 1.25x faster                                                          |
| richards                   | 41.3 ms                                                         | 33.3 ms: 1.24x faster                                                          |
| go                         | 137 ms                                                          | 111 ms: 1.24x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 70.1 ms: 1.24x faster                                                          |
| xml_etree_iterparse        | 77.6 ms                                                         | 63.0 ms: 1.23x faster                                                          |
| xml_etree_process          | 53.2 ms                                                         | 43.7 ms: 1.22x faster                                                          |
| pycparser                  | 978 ms                                                          | 806 ms: 1.21x faster                                                           |
| logging_simple             | 9.75 us                                                         | 8.06 us: 1.21x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.24 sec: 1.21x faster                                                         |
| pprint_safe_repr           | 721 ms                                                          | 599 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 455 ms: 1.20x faster                                                           |
| richards_super             | 46.5 ms                                                         | 39.1 ms: 1.19x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.76 us: 1.19x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 477 ms: 1.18x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 50.2 ms: 1.17x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 18.0 ms: 1.16x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.72 sec: 1.11x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 112 ms: 1.10x faster                                                           |
| django_template            | 36.9 ms                                                         | 33.9 ms: 1.09x faster                                                          |
| sqlglot_optimize           | 48.5 ms                                                         | 44.6 ms: 1.09x faster                                                          |
| 2to3                       | 280 ms                                                          | 258 ms: 1.08x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                           |
| sympy_str                  | 240 ms                                                          | 223 ms: 1.08x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.3 ms: 1.07x faster                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.09 ms: 1.04x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.3 sec: 1.02x faster                                                         |
| pidigits                   | 199 ms                                                          | 196 ms: 1.02x faster                                                           |
| gc_traversal               | 1.44 ms                                                         | 1.45 ms: 1.01x slower                                                          |
| sympy_expand               | 398 ms                                                          | 401 ms: 1.01x slower                                                           |
| regex_dna                  | 127 ms                                                          | 128 ms: 1.01x slower                                                           |
| tornado_http               | 105 ms                                                          | 106 ms: 1.01x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.02 sec: 1.02x slower                                                         |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                          |
| async_generators           | 313 ms                                                          | 320 ms: 1.02x slower                                                           |
| regex_effbot               | 2.04 ms                                                         | 2.08 ms: 1.02x slower                                                          |
| json_loads                 | 20.4 us                                                         | 20.9 us: 1.03x slower                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 77.4 ms: 1.03x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.05x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 695 ms: 1.05x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 15.9 ms: 1.05x slower                                                          |
| telco                      | 5.51 ms                                                         | 5.87 ms: 1.06x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.6 ms: 1.11x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 775 us: 1.19x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 161 us: 1.28x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 239 ms: 2.38x slower                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 3.09 ms: 2.80x slower                                                          |
| Geometric mean             | (ref)                                                           | 1.20x faster                                                                   |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-pythonperf1_win32-x86-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: unknown