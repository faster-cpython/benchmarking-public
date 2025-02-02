# Results vs. 3.12.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: windows-x86
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.130x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| docutils       | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| Geometric mean | (ref)                                                           | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                           |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 552 ms: 1.26x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                           |
| Geometric mean             | (ref)                                                           | 1.29x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 93.3 ms: 1.36x faster                                                          |
| float          | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                          |
| pidigits       | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                           | 1.20x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| regex_dna      | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| regex_effbot   | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                          |
| regex_v8       | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                           | 1.06x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| unpickle_pure_python | 210 us                                                          | 178 us: 1.18x faster                                                           |
| tomli_loads          | 2.20 sec                                                        | 1.88 sec: 1.17x faster                                                         |
| pickle_pure_python   | 286 us                                                          | 254 us: 1.13x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 69.0 ms: 1.13x faster                                                          |
| xml_etree_parse      | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| xml_etree_process    | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                          |
| xml_etree_generate   | 72.1 ms                                                         | 70.0 ms: 1.03x faster                                                          |
| json_dumps           | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                   |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| python_startup         | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| Geometric mean         | (ref)                                                           | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 8.13 ms: 1.22x faster                                                          |
| django_template | 36.9 ms                                                         | 31.8 ms: 1.16x faster                                                          |
| Geometric mean  | (ref)                                                           | 1.19x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:---------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy_memo              | 38.4 us                                                         | 22.8 us: 1.68x faster                                                          |
| raytrace                   | 308 ms                                                          | 218 ms: 1.41x faster                                                           |
| generators                 | 38.5 ms                                                         | 27.2 ms: 1.41x faster                                                          |
| deepcopy                   | 360 us                                                          | 255 us: 1.41x faster                                                           |
| async_tree_memoization_tg  | 350 ms                                                          | 252 ms: 1.39x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 200 ms: 1.39x faster                                                           |
| comprehensions             | 19.2 us                                                         | 13.8 us: 1.39x faster                                                          |
| nbody                      | 127 ms                                                          | 93.3 ms: 1.36x faster                                                          |
| scimark_lu                 | 93.2 ms                                                         | 69.4 ms: 1.34x faster                                                          |
| chaos                      | 69.4 ms                                                         | 52.0 ms: 1.33x faster                                                          |
| spectral_norm              | 104 ms                                                          | 78.2 ms: 1.33x faster                                                          |
| async_tree_io_tg           | 677 ms                                                          | 513 ms: 1.32x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.72 ms: 1.32x faster                                                          |
| logging_silent             | 101 ns                                                          | 77.1 ns: 1.31x faster                                                          |
| async_tree_none            | 298 ms                                                          | 228 ms: 1.31x faster                                                           |
| scimark_sor                | 130 ms                                                          | 99.6 ms: 1.30x faster                                                          |
| async_tree_memoization     | 364 ms                                                          | 279 ms: 1.30x faster                                                           |
| hexiom                     | 6.82 ms                                                         | 5.33 ms: 1.28x faster                                                          |
| deepcopy_reduce            | 3.23 us                                                         | 2.55 us: 1.27x faster                                                          |
| async_tree_io              | 693 ms                                                          | 552 ms: 1.26x faster                                                           |
| float                      | 76.7 ms                                                         | 61.2 ms: 1.25x faster                                                          |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.12 ms: 1.24x faster                                                          |
| logging_simple             | 9.75 us                                                         | 7.95 us: 1.23x faster                                                          |
| mako                       | 9.96 ms                                                         | 8.13 ms: 1.22x faster                                                          |
| logging_format             | 10.4 us                                                         | 8.57 us: 1.21x faster                                                          |
| regex_compile              | 129 ms                                                          | 107 ms: 1.21x faster                                                           |
| crypto_pyaes               | 69.2 ms                                                         | 57.6 ms: 1.20x faster                                                          |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 472 ms: 1.20x faster                                                           |
| coroutines                 | 20.9 ms                                                         | 17.6 ms: 1.18x faster                                                          |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 462 ms: 1.18x faster                                                           |
| scimark_fft                | 271 ms                                                          | 230 ms: 1.18x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 178 us: 1.18x faster                                                           |
| dulwich_log                | 58.5 ms                                                         | 49.8 ms: 1.17x faster                                                          |
| tomli_loads                | 2.20 sec                                                        | 1.88 sec: 1.17x faster                                                         |
| django_template            | 36.9 ms                                                         | 31.8 ms: 1.16x faster                                                          |
| go                         | 137 ms                                                          | 118 ms: 1.16x faster                                                           |
| nqueens                    | 93.7 ms                                                         | 80.6 ms: 1.16x faster                                                          |
| scimark_monte_carlo        | 66.4 ms                                                         | 57.5 ms: 1.16x faster                                                          |
| sqlglot_parse              | 1.25 ms                                                         | 1.09 ms: 1.15x faster                                                          |
| pycparser                  | 978 ms                                                          | 858 ms: 1.14x faster                                                           |
| sqlglot_transpile          | 1.53 ms                                                         | 1.35 ms: 1.14x faster                                                          |
| pprint_safe_repr           | 721 ms                                                          | 639 ms: 1.13x faster                                                           |
| pickle_pure_python         | 286 us                                                          | 254 us: 1.13x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 69.0 ms: 1.13x faster                                                          |
| pyflate                    | 424 ms                                                          | 379 ms: 1.12x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 15.7 ms: 1.12x faster                                                          |
| mdp                        | 1.91 sec                                                        | 1.71 sec: 1.12x faster                                                         |
| sympy_sum                  | 123 ms                                                          | 110 ms: 1.11x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 43.8 ms: 1.11x faster                                                          |
| 2to3                       | 280 ms                                                          | 254 ms: 1.10x faster                                                           |
| pprint_pformat             | 1.50 sec                                                        | 1.36 sec: 1.10x faster                                                         |
| sympy_str                  | 240 ms                                                          | 220 ms: 1.09x faster                                                           |
| bench_thread_pool          | 1.10 ms                                                         | 1.02 ms: 1.08x faster                                                          |
| regex_dna                  | 127 ms                                                          | 119 ms: 1.07x faster                                                           |
| richards_super             | 46.5 ms                                                         | 43.6 ms: 1.06x faster                                                          |
| richards                   | 41.3 ms                                                         | 38.8 ms: 1.06x faster                                                          |
| regex_effbot               | 2.04 ms                                                         | 1.93 ms: 1.06x faster                                                          |
| meteor_contest             | 86.9 ms                                                         | 82.9 ms: 1.05x faster                                                          |
| pathlib                    | 91.4 ms                                                         | 87.3 ms: 1.05x faster                                                          |
| xml_etree_parse            | 113 ms                                                          | 108 ms: 1.04x faster                                                           |
| sympy_expand               | 398 ms                                                          | 382 ms: 1.04x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 51.2 ms: 1.04x faster                                                          |
| bench_mp_pool              | 75.4 ms                                                         | 72.7 ms: 1.04x faster                                                          |
| xml_etree_generate         | 72.1 ms                                                         | 70.0 ms: 1.03x faster                                                          |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 17.2 sec: 1.03x faster                                                         |
| docutils                   | 1.98 sec                                                        | 1.94 sec: 1.02x faster                                                         |
| fannkuch                   | 354 ms                                                          | 347 ms: 1.02x faster                                                           |
| async_generators           | 313 ms                                                          | 307 ms: 1.02x faster                                                           |
| pidigits                   | 199 ms                                                          | 198 ms: 1.01x faster                                                           |
| json                       | 4.15 ms                                                         | 4.22 ms: 1.02x slower                                                          |
| python_startup_no_site     | 19.1 ms                                                         | 19.9 ms: 1.04x slower                                                          |
| json_dumps                 | 7.40 ms                                                         | 7.70 ms: 1.04x slower                                                          |
| python_startup             | 22.4 ms                                                         | 24.0 ms: 1.07x slower                                                          |
| regex_v8                   | 15.0 ms                                                         | 16.2 ms: 1.08x slower                                                          |
| coverage                   | 48.4 ms                                                         | 53.0 ms: 1.09x slower                                                          |
| asyncio_tcp                | 662 ms                                                          | 733 ms: 1.11x slower                                                           |
| telco                      | 5.51 ms                                                         | 6.20 ms: 1.12x slower                                                          |
| create_gc_cycles           | 652 us                                                          | 746 us: 1.14x slower                                                           |
| typing_runtime_protocols   | 126 us                                                          | 145 us: 1.15x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 230 ms: 2.29x slower                                                           |
| Geometric mean             | (ref)                                                           | 1.13x faster                                                                   |

Benchmark hidden because not significant (3): json_loads, tornado_http, gc_traversal
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240815-3.14.0a0-e913d2c/bm-20240815-pythonperf1_win32-x86-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c.json: genshi_text, genshi_xml, html5lib, pylint, thrift

- Geometric mean (including insignificant results): 1.130x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown