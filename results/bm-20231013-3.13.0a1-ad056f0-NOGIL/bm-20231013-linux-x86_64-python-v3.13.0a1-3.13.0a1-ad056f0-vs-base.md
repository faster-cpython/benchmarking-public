# Results vs. base

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.58x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| 2to3           | 269 ms                                                                                               | 276 ms: 1.03x slower                                                                                       |
| chameleon      | 7.07 ms                                                                                              | 7.13 ms: 1.01x slower                                                                                      |
| docutils       | 2.64 sec                                                                                             | 2.71 sec: 1.03x slower                                                                                     |
| tornado_http   | 96.0 ms                                                                                              | 99.1 ms: 1.03x slower                                                                                      |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| async_tree_memoization     | 564 ms                                                                                               | 572 ms: 1.02x slower                                                                                       |
| async_tree_io_tg           | 1.23 sec                                                                                             | 1.25 sec: 1.02x slower                                                                                     |
| async_tree_io              | 1.19 sec                                                                                             | 1.21 sec: 1.02x slower                                                                                     |
| async_tree_cpu_io_mixed    | 712 ms                                                                                               | 726 ms: 1.02x slower                                                                                       |
| async_tree_none            | 437 ms                                                                                               | 446 ms: 1.02x slower                                                                                       |
| async_tree_none_tg         | 453 ms                                                                                               | 463 ms: 1.02x slower                                                                                       |
| async_tree_cpu_io_mixed_tg | 741 ms                                                                                               | 759 ms: 1.02x slower                                                                                       |
| async_tree_memoization_tg  | 595 ms                                                                                               | 610 ms: 1.02x slower                                                                                       |
| Geometric mean             | (ref)                                                                                                | 1.02x slower                                                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| pidigits       | 195 ms                                                                                               | 190 ms: 1.03x faster                                                                                       |
| float          | 81.6 ms                                                                                              | 83.4 ms: 1.02x slower                                                                                      |
| nbody          | 88.6 ms                                                                                              | 95.7 ms: 1.08x slower                                                                                      |
| Geometric mean | (ref)                                                                                                | 1.02x slower                                                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                                                              | 3.56 ms: 1.03x faster                                                                                      |
| regex_dna      | 212 ms                                                                                               | 209 ms: 1.02x faster                                                                                       |
| regex_v8       | 24.7 ms                                                                                              | 25.3 ms: 1.02x slower                                                                                      |
| regex_compile  | 138 ms                                                                                               | 142 ms: 1.03x slower                                                                                       |
| Geometric mean | (ref)                                                                                                | 1.00x slower                                                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.9 ms                                                                                              | 87.7 ms: 1.01x slower                                                                                      |
| xml_etree_process    | 59.9 ms                                                                                              | 60.5 ms: 1.01x slower                                                                                      |
| xml_etree_iterparse  | 106 ms                                                                                               | 107 ms: 1.01x slower                                                                                       |
| xml_etree_parse      | 157 ms                                                                                               | 160 ms: 1.02x slower                                                                                       |
| unpickle_pure_python | 222 us                                                                                               | 226 us: 1.02x slower                                                                                       |
| pickle_list          | 5.10 us                                                                                              | 5.21 us: 1.02x slower                                                                                      |
| pickle_dict          | 34.6 us                                                                                              | 35.4 us: 1.02x slower                                                                                      |
| pickle_pure_python   | 300 us                                                                                               | 307 us: 1.02x slower                                                                                       |
| tomli_loads          | 2.15 sec                                                                                             | 2.25 sec: 1.05x slower                                                                                     |
| Geometric mean       | (ref)                                                                                                | 1.01x slower                                                                                               |

Benchmark hidden because not significant (5): json_dumps, unpickle, json_loads, pickle, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 6.87 ms                                                                                              | 7.05 ms: 1.03x slower                                                                                      |
| python_startup         | 10.1 ms                                                                                              | 10.4 ms: 1.03x slower                                                                                      |
| Geometric mean         | (ref)                                                                                                | 1.03x slower                                                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|-----------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| mako      | 11.2 ms                                                                                              | 11.7 ms: 1.04x slower                                                                                      |

All benchmarks:
===============

| Benchmark                  | results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json | results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json |
|----------------------------|:----------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------:|
| mdp                        | 2.74 sec                                                                                             | 2.58 sec: 1.06x faster                                                                                     |
| regex_effbot               | 3.67 ms                                                                                              | 3.56 ms: 1.03x faster                                                                                      |
| pidigits                   | 195 ms                                                                                               | 190 ms: 1.03x faster                                                                                       |
| regex_dna                  | 212 ms                                                                                               | 209 ms: 1.02x faster                                                                                       |
| typing_runtime_protocols   | 156 us                                                                                               | 153 us: 1.01x faster                                                                                       |
| generators                 | 29.9 ms                                                                                              | 29.5 ms: 1.01x faster                                                                                      |
| nqueens                    | 81.9 ms                                                                                              | 81.0 ms: 1.01x faster                                                                                      |
| bench_mp_pool              | 24.0 ms                                                                                              | 23.9 ms: 1.01x faster                                                                                      |
| chameleon                  | 7.07 ms                                                                                              | 7.13 ms: 1.01x slower                                                                                      |
| xml_etree_generate         | 86.9 ms                                                                                              | 87.7 ms: 1.01x slower                                                                                      |
| meteor_contest             | 109 ms                                                                                               | 111 ms: 1.01x slower                                                                                       |
| xml_etree_process          | 59.9 ms                                                                                              | 60.5 ms: 1.01x slower                                                                                      |
| pathlib                    | 19.4 ms                                                                                              | 19.6 ms: 1.01x slower                                                                                      |
| scimark_monte_carlo        | 69.5 ms                                                                                              | 70.2 ms: 1.01x slower                                                                                      |
| pprint_pformat             | 1.53 sec                                                                                             | 1.54 sec: 1.01x slower                                                                                     |
| sqlglot_optimize           | 53.9 ms                                                                                              | 54.5 ms: 1.01x slower                                                                                      |
| coroutines                 | 23.4 ms                                                                                              | 23.7 ms: 1.01x slower                                                                                      |
| sqlglot_normalize          | 107 ms                                                                                               | 108 ms: 1.01x slower                                                                                       |
| xml_etree_iterparse        | 106 ms                                                                                               | 107 ms: 1.01x slower                                                                                       |
| scimark_fft                | 369 ms                                                                                               | 375 ms: 1.01x slower                                                                                       |
| logging_silent             | 107 ns                                                                                               | 109 ns: 1.01x slower                                                                                       |
| xml_etree_parse            | 157 ms                                                                                               | 160 ms: 1.02x slower                                                                                       |
| async_tree_memoization     | 564 ms                                                                                               | 572 ms: 1.02x slower                                                                                       |
| async_tree_io_tg           | 1.23 sec                                                                                             | 1.25 sec: 1.02x slower                                                                                     |
| deltablue                  | 3.34 ms                                                                                              | 3.40 ms: 1.02x slower                                                                                      |
| scimark_lu                 | 115 ms                                                                                               | 117 ms: 1.02x slower                                                                                       |
| create_gc_cycles           | 1.48 ms                                                                                              | 1.50 ms: 1.02x slower                                                                                      |
| sympy_str                  | 281 ms                                                                                               | 286 ms: 1.02x slower                                                                                       |
| pyflate                    | 473 ms                                                                                               | 482 ms: 1.02x slower                                                                                       |
| richards_super             | 55.0 ms                                                                                              | 56.0 ms: 1.02x slower                                                                                      |
| sqlglot_transpile          | 1.60 ms                                                                                              | 1.63 ms: 1.02x slower                                                                                      |
| sqlglot_parse              | 1.29 ms                                                                                              | 1.31 ms: 1.02x slower                                                                                      |
| async_tree_io              | 1.19 sec                                                                                             | 1.21 sec: 1.02x slower                                                                                     |
| async_tree_cpu_io_mixed    | 712 ms                                                                                               | 726 ms: 1.02x slower                                                                                       |
| unpickle_pure_python       | 222 us                                                                                               | 226 us: 1.02x slower                                                                                       |
| logging_simple             | 5.90 us                                                                                              | 6.02 us: 1.02x slower                                                                                      |
| dulwich_log                | 67.1 ms                                                                                              | 68.5 ms: 1.02x slower                                                                                      |
| regex_v8                   | 24.7 ms                                                                                              | 25.3 ms: 1.02x slower                                                                                      |
| deepcopy_reduce            | 3.14 us                                                                                              | 3.20 us: 1.02x slower                                                                                      |
| async_tree_none            | 437 ms                                                                                               | 446 ms: 1.02x slower                                                                                       |
| json                       | 5.16 ms                                                                                              | 5.27 ms: 1.02x slower                                                                                      |
| asyncio_websockets         | 552 ms                                                                                               | 563 ms: 1.02x slower                                                                                       |
| bench_thread_pool          | 815 us                                                                                               | 833 us: 1.02x slower                                                                                       |
| async_tree_none_tg         | 453 ms                                                                                               | 463 ms: 1.02x slower                                                                                       |
| pickle_list                | 5.10 us                                                                                              | 5.21 us: 1.02x slower                                                                                      |
| float                      | 81.6 ms                                                                                              | 83.4 ms: 1.02x slower                                                                                      |
| deepcopy                   | 353 us                                                                                               | 361 us: 1.02x slower                                                                                       |
| pickle_dict                | 34.6 us                                                                                              | 35.4 us: 1.02x slower                                                                                      |
| async_tree_cpu_io_mixed_tg | 741 ms                                                                                               | 759 ms: 1.02x slower                                                                                       |
| deepcopy_memo              | 38.7 us                                                                                              | 39.6 us: 1.02x slower                                                                                      |
| pickle_pure_python         | 300 us                                                                                               | 307 us: 1.02x slower                                                                                       |
| sympy_expand               | 452 ms                                                                                               | 463 ms: 1.02x slower                                                                                       |
| asyncio_tcp_ssl            | 1.79 sec                                                                                             | 1.83 sec: 1.02x slower                                                                                     |
| async_tree_memoization_tg  | 595 ms                                                                                               | 610 ms: 1.02x slower                                                                                       |
| regex_compile              | 138 ms                                                                                               | 142 ms: 1.03x slower                                                                                       |
| 2to3                       | 269 ms                                                                                               | 276 ms: 1.03x slower                                                                                       |
| docutils                   | 2.64 sec                                                                                             | 2.71 sec: 1.03x slower                                                                                     |
| python_startup_no_site     | 6.87 ms                                                                                              | 7.05 ms: 1.03x slower                                                                                      |
| sympy_integrate            | 20.2 ms                                                                                              | 20.8 ms: 1.03x slower                                                                                      |
| sympy_sum                  | 156 ms                                                                                               | 160 ms: 1.03x slower                                                                                       |
| richards                   | 48.6 ms                                                                                              | 49.9 ms: 1.03x slower                                                                                      |
| scimark_sparse_mat_mult    | 4.79 ms                                                                                              | 4.93 ms: 1.03x slower                                                                                      |
| telco                      | 8.17 ms                                                                                              | 8.41 ms: 1.03x slower                                                                                      |
| asyncio_tcp                | 484 ms                                                                                               | 498 ms: 1.03x slower                                                                                       |
| scimark_sor                | 123 ms                                                                                               | 127 ms: 1.03x slower                                                                                       |
| tornado_http               | 96.0 ms                                                                                              | 99.1 ms: 1.03x slower                                                                                      |
| python_startup             | 10.1 ms                                                                                              | 10.4 ms: 1.03x slower                                                                                      |
| pycparser                  | 1.20 sec                                                                                             | 1.24 sec: 1.03x slower                                                                                     |
| comprehensions             | 20.8 us                                                                                              | 21.5 us: 1.03x slower                                                                                      |
| go                         | 141 ms                                                                                               | 146 ms: 1.04x slower                                                                                       |
| chaos                      | 61.7 ms                                                                                              | 64.0 ms: 1.04x slower                                                                                      |
| logging_format             | 6.47 us                                                                                              | 6.71 us: 1.04x slower                                                                                      |
| hexiom                     | 6.16 ms                                                                                              | 6.40 ms: 1.04x slower                                                                                      |
| async_generators           | 453 ms                                                                                               | 472 ms: 1.04x slower                                                                                       |
| raytrace                   | 274 ms                                                                                               | 285 ms: 1.04x slower                                                                                       |
| mako                       | 11.2 ms                                                                                              | 11.7 ms: 1.04x slower                                                                                      |
| fannkuch                   | 402 ms                                                                                               | 420 ms: 1.05x slower                                                                                       |
| tomli_loads                | 2.15 sec                                                                                             | 2.25 sec: 1.05x slower                                                                                     |
| crypto_pyaes               | 71.8 ms                                                                                              | 75.1 ms: 1.05x slower                                                                                      |
| spectral_norm              | 110 ms                                                                                               | 116 ms: 1.06x slower                                                                                       |
| gc_traversal               | 3.87 ms                                                                                              | 4.15 ms: 1.07x slower                                                                                      |
| nbody                      | 88.6 ms                                                                                              | 95.7 ms: 1.08x slower                                                                                      |
| sqlite_synth               | 2.80 us                                                                                              | 3.11 us: 1.11x slower                                                                                      |
| coverage                   | 94.4 ms                                                                                              | 700 ms: 7.41x slower                                                                                       |
| Geometric mean             | (ref)                                                                                                | 1.04x slower                                                                                               |

Benchmark hidden because not significant (6): json_dumps, pprint_safe_repr, unpickle, json_loads, pickle, unpickle_list
Ignored benchmarks (1) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: unpack_sequence
Ignored benchmarks (11) of results/bm-20231013-3.13.0a1-ad056f0-NOGIL/bm-20231013-linux-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: aiohttp, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.58x