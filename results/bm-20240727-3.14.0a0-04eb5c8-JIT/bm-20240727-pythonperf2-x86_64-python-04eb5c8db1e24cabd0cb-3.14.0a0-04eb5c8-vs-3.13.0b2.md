# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 82.54%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.15 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 70.6 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 789 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                        |
| async_tree_io              | 873 ms                                                           | 826 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.5 ms: 1.08x faster                                                       |
| nbody          | 87.8 ms                                                          | 84.0 ms: 1.05x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 134 ms: 1.07x faster                                                        |
| regex_dna      | 249 ms                                                           | 259 ms: 1.04x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 211 us: 1.07x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 97.8 ms: 1.05x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 320 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.07 ms: 1.14x faster                                                       |
| django_template | 39.0 ms                                                          | 41.4 ms: 1.06x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.5 ms: 1.11x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.8 us: 1.30x faster                                                       |
| deepcopy                   | 377 us                                                           | 308 us: 1.23x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                       |
| richards                   | 53.4 ms                                                          | 45.5 ms: 1.17x faster                                                       |
| richards_super             | 61.2 ms                                                          | 52.3 ms: 1.17x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.9 ms: 1.16x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.10 sec: 1.15x faster                                                      |
| mako                       | 10.4 ms                                                          | 9.07 ms: 1.14x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 789 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 3.02 us: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| pyflate                    | 482 ms                                                           | 433 ms: 1.11x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.35 ms: 1.08x faster                                                       |
| float                      | 80.2 ms                                                          | 74.5 ms: 1.08x faster                                                       |
| regex_compile              | 144 ms                                                           | 134 ms: 1.07x faster                                                        |
| scimark_fft                | 312 ms                                                           | 292 ms: 1.07x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.82 sec: 1.07x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 211 us: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 568 ms: 1.06x faster                                                        |
| async_tree_io              | 873 ms                                                           | 826 ms: 1.06x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 70.6 ms: 1.06x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 69.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 97.8 ms: 1.05x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.02 ms: 1.05x faster                                                       |
| nbody                      | 87.8 ms                                                          | 84.0 ms: 1.05x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 82.3 ms: 1.04x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 57.6 ms: 1.04x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.94 ms: 1.03x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.16 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 796 ms: 1.03x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| coverage                   | 83.5 ms                                                          | 81.9 ms: 1.02x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.3 ms: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| logging_format             | 7.11 us                                                          | 7.03 us: 1.01x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.35 us: 1.01x faster                                                       |
| fannkuch                   | 353 ms                                                           | 351 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 166 ms: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                      |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 903 us: 1.03x slower                                                        |
| regex_dna                  | 249 ms                                                           | 259 ms: 1.04x slower                                                        |
| json                       | 5.35 ms                                                          | 5.56 ms: 1.04x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 6.60 ms: 1.04x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 320 us: 1.04x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.84 ms: 1.04x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| sympy_expand               | 501 ms                                                           | 524 ms: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.57 sec: 1.05x slower                                                      |
| sympy_str                  | 295 ms                                                           | 310 ms: 1.05x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.15 sec: 1.05x slower                                                      |
| 2to3                       | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.60 ms: 1.06x slower                                                       |
| django_template            | 39.0 ms                                                          | 41.4 ms: 1.06x slower                                                       |
| async_generators           | 363 ms                                                           | 387 ms: 1.07x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 166 ms: 1.07x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.61 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 63.8 ms: 1.07x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.2 us: 1.07x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 96.1 ms: 1.09x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 131 ms: 1.09x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 188 us: 1.10x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 25.6 ms: 1.11x slower                                                       |
| chaos                      | 59.6 ms                                                          | 66.0 ms: 1.11x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 64.5 ms: 1.11x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 29.1 ms: 1.12x slower                                                       |
| pylint                     | 339 ms                                                           | 383 ms: 1.13x slower                                                        |
| raytrace                   | 260 ms                                                           | 300 ms: 1.15x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 113 ms: 1.16x slower                                                        |
| scimark_sor                | 119 ms                                                           | 142 ms: 1.20x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (7): bench_mp_pool, bench_thread_pool, asyncio_tcp, asyncio_tcp_ssl, dask, json_dumps, tornado_http
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 82.54% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x