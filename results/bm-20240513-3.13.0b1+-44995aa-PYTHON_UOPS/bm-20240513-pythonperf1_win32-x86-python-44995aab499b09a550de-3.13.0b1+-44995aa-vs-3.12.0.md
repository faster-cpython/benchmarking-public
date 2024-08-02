# Results vs. 3.12.0

- fork: python
- ref: 44995aab499b09a550de
- machine: windows-x86
- commit hash: 44995aa
- commit date: 2024-05-13
- overall geometric mean: 1.09x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 280 ms                                                          | 257 ms: 1.09x faster                                                            |
| chameleon      | 7.75 ms                                                         | 6.38 ms: 1.21x faster                                                           |
| docutils       | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                          |
| tornado_http   | 105 ms                                                          | 99.6 ms: 1.05x faster                                                           |
| Geometric mean | (ref)                                                           | 1.08x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                            |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                            |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 282 ms: 1.29x faster                                                            |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                            |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                            |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                            |
| Geometric mean             | (ref)                                                           | 1.27x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                          | 79.5 ms: 1.60x faster                                                           |
| float          | 76.7 ms                                                         | 57.2 ms: 1.34x faster                                                           |
| pidigits       | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                           | 1.28x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| regex_effbot   | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| regex_compile  | 129 ms                                                          | 126 ms: 1.02x faster                                                            |
| regex_v8       | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                           |
| Geometric mean | (ref)                                                           | 1.02x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.20 sec                                                        | 1.68 sec: 1.31x faster                                                          |
| xml_etree_process    | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                           |
| xml_etree_iterparse  | 77.6 ms                                                         | 66.5 ms: 1.17x faster                                                           |
| xml_etree_generate   | 72.1 ms                                                         | 62.0 ms: 1.16x faster                                                           |
| unpickle_pure_python | 210 us                                                          | 181 us: 1.16x faster                                                            |
| pickle_pure_python   | 286 us                                                          | 255 us: 1.12x faster                                                            |
| xml_etree_parse      | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| unpickle_list        | 2.95 us                                                         | 2.73 us: 1.08x faster                                                           |
| json_dumps           | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                           |
| json_loads           | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| pickle_dict          | 19.9 us                                                         | 20.7 us: 1.04x slower                                                           |
| unpickle             | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle               | 7.79 us                                                         | 8.24 us: 1.06x slower                                                           |
| pickle_list          | 3.37 us                                                         | 3.64 us: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                           | 1.07x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                           |
| Geometric mean         | (ref)                                                           | 1.02x faster                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|-----------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| django_template | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                           | 1.22x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0 | bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa |
|----------------------------|:---------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| generators                 | 38.5 ms                                                         | 23.4 ms: 1.65x faster                                                           |
| nbody                      | 127 ms                                                          | 79.5 ms: 1.60x faster                                                           |
| raytrace                   | 308 ms                                                          | 214 ms: 1.44x faster                                                            |
| async_tree_memoization_tg  | 350 ms                                                          | 261 ms: 1.34x faster                                                            |
| float                      | 76.7 ms                                                         | 57.2 ms: 1.34x faster                                                           |
| scimark_sor                | 130 ms                                                          | 97.1 ms: 1.34x faster                                                           |
| async_tree_none_tg         | 278 ms                                                          | 208 ms: 1.33x faster                                                            |
| spectral_norm              | 104 ms                                                          | 78.6 ms: 1.32x faster                                                           |
| tomli_loads                | 2.20 sec                                                        | 1.68 sec: 1.31x faster                                                          |
| coroutines                 | 20.9 ms                                                         | 16.0 ms: 1.31x faster                                                           |
| comprehensions             | 19.2 us                                                         | 14.7 us: 1.30x faster                                                           |
| chaos                      | 69.4 ms                                                         | 53.3 ms: 1.30x faster                                                           |
| async_tree_io              | 693 ms                                                          | 534 ms: 1.30x faster                                                            |
| async_tree_memoization     | 364 ms                                                          | 282 ms: 1.29x faster                                                            |
| mako                       | 9.96 ms                                                         | 7.78 ms: 1.28x faster                                                           |
| async_tree_none            | 298 ms                                                          | 233 ms: 1.28x faster                                                            |
| richards                   | 41.3 ms                                                         | 32.6 ms: 1.27x faster                                                           |
| deepcopy_memo              | 38.4 us                                                         | 30.3 us: 1.27x faster                                                           |
| async_tree_io_tg           | 677 ms                                                          | 538 ms: 1.26x faster                                                            |
| richards_super             | 46.5 ms                                                         | 37.1 ms: 1.25x faster                                                           |
| logging_simple             | 9.75 us                                                         | 7.82 us: 1.25x faster                                                           |
| logging_silent             | 101 ns                                                          | 81.3 ns: 1.24x faster                                                           |
| logging_format             | 10.4 us                                                         | 8.40 us: 1.24x faster                                                           |
| deltablue                  | 3.58 ms                                                         | 2.90 ms: 1.24x faster                                                           |
| scimark_fft                | 271 ms                                                          | 220 ms: 1.23x faster                                                            |
| nqueens                    | 93.7 ms                                                         | 76.8 ms: 1.22x faster                                                           |
| chameleon                  | 7.75 ms                                                         | 6.38 ms: 1.21x faster                                                           |
| sqlglot_parse              | 1.25 ms                                                         | 1.03 ms: 1.21x faster                                                           |
| scimark_monte_carlo        | 66.4 ms                                                         | 55.1 ms: 1.21x faster                                                           |
| xml_etree_process          | 53.2 ms                                                         | 44.5 ms: 1.20x faster                                                           |
| async_tree_cpu_io_mixed_tg | 546 ms                                                          | 458 ms: 1.19x faster                                                            |
| sqlglot_transpile          | 1.53 ms                                                         | 1.29 ms: 1.19x faster                                                           |
| fannkuch                   | 354 ms                                                          | 299 ms: 1.18x faster                                                            |
| scimark_sparse_mat_mult    | 3.86 ms                                                         | 3.29 ms: 1.17x faster                                                           |
| xml_etree_iterparse        | 77.6 ms                                                         | 66.5 ms: 1.17x faster                                                           |
| go                         | 137 ms                                                          | 118 ms: 1.17x faster                                                            |
| xml_etree_generate         | 72.1 ms                                                         | 62.0 ms: 1.16x faster                                                           |
| unpickle_pure_python       | 210 us                                                          | 181 us: 1.16x faster                                                            |
| django_template            | 36.9 ms                                                         | 31.9 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 564 ms                                                          | 487 ms: 1.16x faster                                                            |
| crypto_pyaes               | 69.2 ms                                                         | 60.2 ms: 1.15x faster                                                           |
| deepcopy_reduce            | 3.23 us                                                         | 2.81 us: 1.15x faster                                                           |
| pycparser                  | 978 ms                                                          | 853 ms: 1.15x faster                                                            |
| mdp                        | 1.91 sec                                                        | 1.68 sec: 1.14x faster                                                          |
| pprint_pformat             | 1.50 sec                                                        | 1.33 sec: 1.13x faster                                                          |
| pickle_pure_python         | 286 us                                                          | 255 us: 1.12x faster                                                            |
| deepcopy                   | 360 us                                                          | 321 us: 1.12x faster                                                            |
| pprint_safe_repr           | 721 ms                                                          | 648 ms: 1.11x faster                                                            |
| hexiom                     | 6.82 ms                                                         | 6.16 ms: 1.11x faster                                                           |
| scimark_lu                 | 93.2 ms                                                         | 84.5 ms: 1.10x faster                                                           |
| sqlglot_optimize           | 48.5 ms                                                         | 44.2 ms: 1.10x faster                                                           |
| meteor_contest             | 86.9 ms                                                         | 79.7 ms: 1.09x faster                                                           |
| 2to3                       | 280 ms                                                          | 257 ms: 1.09x faster                                                            |
| sqlite_synth               | 2.07 us                                                         | 1.91 us: 1.09x faster                                                           |
| xml_etree_parse            | 113 ms                                                          | 104 ms: 1.08x faster                                                            |
| async_generators           | 313 ms                                                          | 290 ms: 1.08x faster                                                            |
| unpickle_list              | 2.95 us                                                         | 2.73 us: 1.08x faster                                                           |
| regex_dna                  | 127 ms                                                          | 118 ms: 1.08x faster                                                            |
| regex_effbot               | 2.04 ms                                                         | 1.91 ms: 1.07x faster                                                           |
| pyflate                    | 424 ms                                                          | 397 ms: 1.07x faster                                                            |
| bench_thread_pool          | 1.10 ms                                                         | 1.04 ms: 1.06x faster                                                           |
| json_dumps                 | 7.40 ms                                                         | 6.98 ms: 1.06x faster                                                           |
| tornado_http               | 105 ms                                                          | 99.6 ms: 1.05x faster                                                           |
| sympy_integrate            | 17.5 ms                                                         | 16.7 ms: 1.05x faster                                                           |
| asyncio_tcp_ssl            | 17.7 sec                                                        | 16.9 sec: 1.04x faster                                                          |
| sympy_sum                  | 123 ms                                                          | 118 ms: 1.04x faster                                                            |
| python_startup_no_site     | 19.1 ms                                                         | 18.4 ms: 1.04x faster                                                           |
| pathlib                    | 91.4 ms                                                         | 88.3 ms: 1.04x faster                                                           |
| bench_mp_pool              | 75.4 ms                                                         | 72.8 ms: 1.04x faster                                                           |
| regex_compile              | 129 ms                                                          | 126 ms: 1.02x faster                                                            |
| sympy_str                  | 240 ms                                                          | 237 ms: 1.01x faster                                                            |
| gc_traversal               | 1.44 ms                                                         | 1.46 ms: 1.01x slower                                                           |
| docutils                   | 1.98 sec                                                        | 2.01 sec: 1.01x slower                                                          |
| pidigits                   | 199 ms                                                          | 202 ms: 1.01x slower                                                            |
| json_loads                 | 20.4 us                                                         | 20.7 us: 1.02x slower                                                           |
| json                       | 4.15 ms                                                         | 4.25 ms: 1.02x slower                                                           |
| pickle_dict                | 19.9 us                                                         | 20.7 us: 1.04x slower                                                           |
| unpickle                   | 9.71 us                                                         | 10.2 us: 1.05x slower                                                           |
| pickle                     | 7.79 us                                                         | 8.24 us: 1.06x slower                                                           |
| sympy_expand               | 398 ms                                                          | 421 ms: 1.06x slower                                                            |
| pickle_list                | 3.37 us                                                         | 3.64 us: 1.08x slower                                                           |
| regex_v8                   | 15.0 ms                                                         | 16.3 ms: 1.08x slower                                                           |
| asyncio_tcp                | 662 ms                                                          | 719 ms: 1.09x slower                                                            |
| typing_runtime_protocols   | 126 us                                                          | 146 us: 1.16x slower                                                            |
| create_gc_cycles           | 652 us                                                          | 761 us: 1.17x slower                                                            |
| telco                      | 5.51 ms                                                         | 6.89 ms: 1.25x slower                                                           |
| sqlglot_normalize          | 100 ms                                                          | 227 ms: 2.26x slower                                                            |
| coverage                   | 48.4 ms                                                         | 331 ms: 6.84x slower                                                            |
| Geometric mean             | (ref)                                                           | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf1_win32-x86-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, dulwich_log, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240513-3.13.0b1+-44995aa-PYTHON_UOPS/bm-20240513-pythonperf1_win32-x86-python-44995aab499b09a550de-3.13.0b1+-44995aa.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: unknown