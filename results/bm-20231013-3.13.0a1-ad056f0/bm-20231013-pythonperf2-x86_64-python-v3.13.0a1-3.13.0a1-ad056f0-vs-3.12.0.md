
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.03x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.86x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 297 ms: 1.04x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.78 ms: 1.08x slower                                            |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                           |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 439 ms: 1.03x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 557 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 713 ms: 1.02x slower                                             |
| async_tree_none_tg         | 431 ms                                                       | 447 ms: 1.04x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 727 ms: 1.04x slower                                             |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                           |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.05x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 571 ms: 1.06x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 264 ms: 1.00x faster                                             |
| float          | 76.6 ms                                                      | 81.5 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                            |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                        | 1.04x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle               | 10.5 us                                                      | 10.1 us: 1.04x faster                                            |
| unpickle             | 14.8 us                                                      | 14.3 us: 1.03x faster                                            |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                             |
| unpickle_list        | 4.66 us                                                      | 4.61 us: 1.01x faster                                            |
| pickle_dict          | 32.5 us                                                      | 32.9 us: 1.01x slower                                            |
| xml_etree_generate   | 86.1 ms                                                      | 87.3 ms: 1.01x slower                                            |
| xml_etree_process    | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.24 sec: 1.04x slower                                           |
| unpickle_pure_python | 210 us                                                       | 220 us: 1.05x slower                                             |
| xml_etree_parse      | 144 ms                                                       | 152 ms: 1.06x slower                                             |
| xml_etree_iterparse  | 103 ms                                                       | 110 ms: 1.07x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): json_loads, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.70 ms: 1.01x slower                                            |
| python_startup         | 11.6 ms                                                      | 12.6 ms: 1.09x slower                                            |
| Geometric mean         | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| crypto_pyaes               | 80.3 ms                                                      | 73.4 ms: 1.09x faster                                            |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                             |
| generators                 | 37.4 ms                                                      | 35.4 ms: 1.06x faster                                            |
| unpack_sequence            | 53.2 ns                                                      | 50.9 ns: 1.04x faster                                            |
| pickle                     | 10.5 us                                                      | 10.1 us: 1.04x faster                                            |
| unpickle                   | 14.8 us                                                      | 14.3 us: 1.03x faster                                            |
| asyncio_tcp                | 378 ms                                                       | 367 ms: 1.03x faster                                             |
| async_tree_none            | 452 ms                                                       | 439 ms: 1.03x faster                                             |
| sqlite_synth               | 2.77 us                                                      | 2.70 us: 1.03x faster                                            |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                           |
| chaos                      | 64.0 ms                                                      | 62.7 ms: 1.02x faster                                            |
| comprehensions             | 21.9 us                                                      | 21.5 us: 1.02x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                            |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                             |
| unpickle_list              | 4.66 us                                                      | 4.61 us: 1.01x faster                                            |
| nqueens                    | 89.9 ms                                                      | 89.2 ms: 1.01x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.55 ms: 1.01x faster                                            |
| logging_format             | 7.48 us                                                      | 7.44 us: 1.01x faster                                            |
| sympy_sum                  | 162 ms                                                       | 161 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| pidigits                   | 265 ms                                                       | 264 ms: 1.00x faster                                             |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.39 us: 1.01x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 8.70 ms: 1.01x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                             |
| spectral_norm              | 91.6 ms                                                      | 92.3 ms: 1.01x slower                                            |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| pickle_dict                | 32.5 us                                                      | 32.9 us: 1.01x slower                                            |
| logging_simple             | 6.71 us                                                      | 6.79 us: 1.01x slower                                            |
| sympy_integrate            | 23.9 ms                                                      | 24.2 ms: 1.01x slower                                            |
| xml_etree_generate         | 86.1 ms                                                      | 87.3 ms: 1.01x slower                                            |
| sympy_str                  | 302 ms                                                       | 307 ms: 1.02x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                           |
| typing_runtime_protocols   | 152 us                                                       | 155 us: 1.02x slower                                             |
| async_generators           | 390 ms                                                       | 399 ms: 1.02x slower                                             |
| sympy_expand               | 484 ms                                                       | 494 ms: 1.02x slower                                             |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 58.8 ms: 1.02x slower                                            |
| pathlib                    | 18.9 ms                                                      | 19.3 ms: 1.02x slower                                            |
| async_tree_memoization     | 544 ms                                                       | 557 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 713 ms: 1.02x slower                                             |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                            |
| pprint_safe_repr           | 807 ms                                                       | 829 ms: 1.03x slower                                             |
| deepcopy                   | 368 us                                                       | 379 us: 1.03x slower                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 71.0 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.34 ms: 1.03x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.04x slower                                            |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |
| async_tree_none_tg         | 431 ms                                                       | 447 ms: 1.04x slower                                             |
| scimark_lu                 | 98.8 ms                                                      | 103 ms: 1.04x slower                                             |
| tomli_loads                | 2.16 sec                                                     | 2.24 sec: 1.04x slower                                           |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 727 ms: 1.04x slower                                             |
| logging_silent             | 94.4 ns                                                      | 98.3 ns: 1.04x slower                                            |
| 2to3                       | 285 ms                                                       | 297 ms: 1.04x slower                                             |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| scimark_fft                | 301 ms                                                       | 315 ms: 1.05x slower                                             |
| deepcopy_memo              | 36.8 us                                                      | 38.6 us: 1.05x slower                                            |
| async_tree_io              | 1.04 sec                                                     | 1.09 sec: 1.05x slower                                           |
| unpickle_pure_python       | 210 us                                                       | 220 us: 1.05x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.11 sec: 1.05x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 571 ms: 1.06x slower                                             |
| xml_etree_parse            | 144 ms                                                       | 152 ms: 1.06x slower                                             |
| dulwich_log                | 65.4 ms                                                      | 69.2 ms: 1.06x slower                                            |
| float                      | 76.6 ms                                                      | 81.5 ms: 1.06x slower                                            |
| xml_etree_iterparse        | 103 ms                                                       | 110 ms: 1.07x slower                                             |
| chameleon                  | 7.23 ms                                                      | 7.78 ms: 1.08x slower                                            |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                           |
| python_startup             | 11.6 ms                                                      | 12.6 ms: 1.09x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.54 ms: 1.10x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.66 ms: 1.13x slower                                            |
| fannkuch                   | 350 ms                                                       | 396 ms: 1.13x slower                                             |
| gc_traversal               | 3.48 ms                                                      | 3.95 ms: 1.14x slower                                            |
| go                         | 150 ms                                                       | 172 ms: 1.15x slower                                             |
| pyflate                    | 439 ms                                                       | 513 ms: 1.17x slower                                             |
| telco                      | 6.96 ms                                                      | 8.25 ms: 1.18x slower                                            |
| richards_super             | 51.3 ms                                                      | 61.7 ms: 1.20x slower                                            |
| richards                   | 45.7 ms                                                      | 55.4 ms: 1.21x slower                                            |
| coverage                   | 66.7 ms                                                      | 83.6 ms: 1.25x slower                                            |
| scimark_sor                | 109 ms                                                       | 149 ms: 1.37x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (9): bench_mp_pool, create_gc_cycles, nbody, json_loads, json, tornado_http, asyncio_websockets, pickle_list, bench_thread_pool
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, dask, django_template, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 0.86x