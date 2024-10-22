# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 297 ms: 1.02x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.78 ms: 1.05x slower                                            |
| docutils       | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.04x faster                                             |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| async_generators           | 359 ms                                                       | 399 ms: 1.11x slower                                             |
| async_tree_none            | 372 ms                                                       | 439 ms: 1.18x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 713 ms: 1.19x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 557 ms: 1.23x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 571 ms: 1.24x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 727 ms: 1.26x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.09 sec: 1.29x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 447 ms: 1.32x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.11 sec: 1.35x slower                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                     |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 81.5 ms: 1.00x faster                                            |
| pidigits       | 253 ms                                                       | 264 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| regex_compile  | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| regex_effbot   | 3.37 ms                                                      | 3.55 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.24 sec: 1.07x faster                                           |
| unpickle             | 15.1 us                                                      | 14.3 us: 1.06x faster                                            |
| pickle               | 10.5 us                                                      | 10.1 us: 1.04x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                            |
| pickle_list          | 4.59 us                                                      | 4.45 us: 1.03x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                            |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                             |
| json_loads           | 24.0 us                                                      | 24.3 us: 1.01x slower                                            |
| xml_etree_generate   | 85.3 ms                                                      | 87.3 ms: 1.02x slower                                            |
| pickle_dict          | 32.1 us                                                      | 32.9 us: 1.03x slower                                            |
| unpickle_pure_python | 214 us                                                       | 220 us: 1.03x slower                                             |
| xml_etree_parse      | 145 ms                                                       | 152 ms: 1.05x slower                                             |
| xml_etree_iterparse  | 100 ms                                                       | 110 ms: 1.10x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 12.6 ms: 1.05x faster                                            |
| python_startup_no_site | 8.94 ms                                                      | 8.70 ms: 1.03x faster                                            |
| Geometric mean         | (ref)                                                        | 1.04x faster                                                     |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 174 us                                                       | 155 us: 1.13x faster                                             |
| unpack_sequence            | 56.8 ns                                                      | 50.9 ns: 1.12x faster                                            |
| create_gc_cycles           | 1.76 ms                                                      | 1.58 ms: 1.11x faster                                            |
| tomli_loads                | 2.41 sec                                                     | 2.24 sec: 1.07x faster                                           |
| unpickle                   | 15.1 us                                                      | 14.3 us: 1.06x faster                                            |
| spectral_norm              | 97.4 ms                                                      | 92.3 ms: 1.05x faster                                            |
| python_startup             | 13.3 ms                                                      | 12.6 ms: 1.05x faster                                            |
| raytrace                   | 289 ms                                                       | 276 ms: 1.05x faster                                             |
| deepcopy                   | 397 us                                                       | 379 us: 1.05x faster                                             |
| deepcopy_reduce            | 3.54 us                                                      | 3.39 us: 1.04x faster                                            |
| gc_traversal               | 4.11 ms                                                      | 3.95 ms: 1.04x faster                                            |
| telco                      | 8.58 ms                                                      | 8.25 ms: 1.04x faster                                            |
| pickle                     | 10.5 us                                                      | 10.1 us: 1.04x faster                                            |
| asyncio_tcp                | 380 ms                                                       | 367 ms: 1.04x faster                                             |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                            |
| sqlite_synth               | 2.79 us                                                      | 2.70 us: 1.03x faster                                            |
| pickle_list                | 4.59 us                                                      | 4.45 us: 1.03x faster                                            |
| python_startup_no_site     | 8.94 ms                                                      | 8.70 ms: 1.03x faster                                            |
| deepcopy_memo              | 39.5 us                                                      | 38.6 us: 1.02x faster                                            |
| json                       | 5.22 ms                                                      | 5.12 ms: 1.02x faster                                            |
| sympy_expand               | 505 ms                                                       | 494 ms: 1.02x faster                                             |
| xml_etree_process          | 60.9 ms                                                      | 59.9 ms: 1.02x faster                                            |
| sqlglot_normalize          | 118 ms                                                       | 117 ms: 1.02x faster                                             |
| sqlglot_optimize           | 59.7 ms                                                      | 58.8 ms: 1.01x faster                                            |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                             |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                             |
| float                      | 81.9 ms                                                      | 81.5 ms: 1.00x faster                                            |
| mdp                        | 2.52 sec                                                     | 2.52 sec: 1.00x faster                                           |
| scimark_fft                | 314 ms                                                       | 315 ms: 1.00x slower                                             |
| logging_silent             | 97.7 ns                                                      | 98.3 ns: 1.01x slower                                            |
| crypto_pyaes               | 72.8 ms                                                      | 73.4 ms: 1.01x slower                                            |
| nqueens                    | 88.2 ms                                                      | 89.2 ms: 1.01x slower                                            |
| json_loads                 | 24.0 us                                                      | 24.3 us: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.34 ms: 1.01x slower                                            |
| asyncio_websockets         | 382 ms                                                       | 389 ms: 1.02x slower                                             |
| chaos                      | 61.7 ms                                                      | 62.7 ms: 1.02x slower                                            |
| meteor_contest             | 128 ms                                                       | 131 ms: 1.02x slower                                             |
| pprint_safe_repr           | 812 ms                                                       | 829 ms: 1.02x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                           |
| xml_etree_generate         | 85.3 ms                                                      | 87.3 ms: 1.02x slower                                            |
| 2to3                       | 291 ms                                                       | 297 ms: 1.02x slower                                             |
| docutils                   | 2.81 sec                                                     | 2.88 sec: 1.02x slower                                           |
| pickle_dict                | 32.1 us                                                      | 32.9 us: 1.03x slower                                            |
| unpickle_pure_python       | 214 us                                                       | 220 us: 1.03x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                            |
| coverage                   | 81.1 ms                                                      | 83.6 ms: 1.03x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                            |
| richards_super             | 59.8 ms                                                      | 61.7 ms: 1.03x slower                                            |
| hexiom                     | 6.33 ms                                                      | 6.54 ms: 1.03x slower                                            |
| sympy_str                  | 296 ms                                                       | 307 ms: 1.04x slower                                             |
| sympy_integrate            | 23.3 ms                                                      | 24.2 ms: 1.04x slower                                            |
| regex_compile              | 144 ms                                                       | 150 ms: 1.04x slower                                             |
| pyflate                    | 492 ms                                                       | 513 ms: 1.04x slower                                             |
| pidigits                   | 253 ms                                                       | 264 ms: 1.05x slower                                             |
| coroutines                 | 21.6 ms                                                      | 22.6 ms: 1.05x slower                                            |
| sympy_sum                  | 154 ms                                                       | 161 ms: 1.05x slower                                             |
| chameleon                  | 7.42 ms                                                      | 7.78 ms: 1.05x slower                                            |
| scimark_lu                 | 97.8 ms                                                      | 103 ms: 1.05x slower                                             |
| xml_etree_parse            | 145 ms                                                       | 152 ms: 1.05x slower                                             |
| richards                   | 52.7 ms                                                      | 55.4 ms: 1.05x slower                                            |
| logging_format             | 7.07 us                                                      | 7.44 us: 1.05x slower                                            |
| regex_effbot               | 3.37 ms                                                      | 3.55 ms: 1.05x slower                                            |
| dulwich_log                | 65.5 ms                                                      | 69.2 ms: 1.06x slower                                            |
| generators                 | 33.5 ms                                                      | 35.4 ms: 1.06x slower                                            |
| pycparser                  | 1.26 sec                                                     | 1.33 sec: 1.06x slower                                           |
| logging_simple             | 6.40 us                                                      | 6.79 us: 1.06x slower                                            |
| bench_thread_pool          | 901 us                                                       | 961 us: 1.07x slower                                             |
| deltablue                  | 3.41 ms                                                      | 3.66 ms: 1.07x slower                                            |
| go                         | 160 ms                                                       | 172 ms: 1.07x slower                                             |
| fannkuch                   | 365 ms                                                       | 396 ms: 1.09x slower                                             |
| scimark_monte_carlo        | 64.9 ms                                                      | 71.0 ms: 1.09x slower                                            |
| xml_etree_iterparse        | 100 ms                                                       | 110 ms: 1.10x slower                                             |
| async_generators           | 359 ms                                                       | 399 ms: 1.11x slower                                             |
| pathlib                    | 17.4 ms                                                      | 19.3 ms: 1.11x slower                                            |
| async_tree_none            | 372 ms                                                       | 439 ms: 1.18x slower                                             |
| scimark_sor                | 126 ms                                                       | 149 ms: 1.19x slower                                             |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 713 ms: 1.19x slower                                             |
| async_tree_memoization     | 452 ms                                                       | 557 ms: 1.23x slower                                             |
| async_tree_memoization_tg  | 461 ms                                                       | 571 ms: 1.24x slower                                             |
| comprehensions             | 17.3 us                                                      | 21.5 us: 1.25x slower                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 727 ms: 1.26x slower                                             |
| async_tree_io              | 847 ms                                                       | 1.09 sec: 1.29x slower                                           |
| async_tree_none_tg         | 340 ms                                                       | 447 ms: 1.32x slower                                             |
| async_tree_io_tg           | 819 ms                                                       | 1.11 sec: 1.35x slower                                           |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (7): mako, nbody, unpickle_list, regex_v8, asyncio_tcp_ssl, tornado_http, bench_mp_pool
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, bpe_tokeniser, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.95x