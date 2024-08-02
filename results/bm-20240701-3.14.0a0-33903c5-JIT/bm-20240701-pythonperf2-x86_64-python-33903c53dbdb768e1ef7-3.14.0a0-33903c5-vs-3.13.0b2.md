# Results vs. 3.13.0b2

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-x86_64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.00x faster
- HPT reliability: 72.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 799 ms: 1.13x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 385 ms: 1.09x faster                                                        |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 582 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.09x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                       |
| nbody          | 87.8 ms                                                          | 85.2 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| regex_dna      | 249 ms                                                           | 264 ms: 1.06x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.74 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 82.1 ms: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 99.4 ms: 1.03x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.5 ms: 1.02x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.26 ms: 1.12x faster                                                       |
| django_template | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 28.4 ms: 1.09x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 65.5 ms: 1.13x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.04x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240701-pythonperf2-x86_64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.5 us: 1.26x faster                                                       |
| deepcopy                   | 377 us                                                           | 306 us: 1.23x faster                                                        |
| richards                   | 53.4 ms                                                          | 45.8 ms: 1.17x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| richards_super             | 61.2 ms                                                          | 53.7 ms: 1.14x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 799 ms: 1.13x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 409 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| mako                       | 10.4 ms                                                          | 9.26 ms: 1.12x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 87.4 ms: 1.11x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 385 ms: 1.09x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 3.12 us: 1.09x faster                                                       |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| float                      | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.01 ms: 1.07x faster                                                       |
| scimark_fft                | 312 ms                                                           | 294 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| regex_compile              | 144 ms                                                           | 137 ms: 1.05x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.13 us: 1.04x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 82.1 ms: 1.04x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.84 us: 1.04x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 70.7 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 582 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.93 ms: 1.04x faster                                                       |
| pyflate                    | 482 ms                                                           | 466 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 99.4 ms: 1.03x faster                                                       |
| nbody                      | 87.8 ms                                                          | 85.2 ms: 1.03x faster                                                       |
| fannkuch                   | 353 ms                                                           | 343 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.21 ms: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.5 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 806 ms: 1.01x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 66.4 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                       |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                      |
| gc_traversal               | 4.69 ms                                                          | 4.66 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                      |
| bpe_tokeniser              | 5.14 sec                                                         | 5.12 sec: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.0 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| json                       | 5.35 ms                                                          | 5.43 ms: 1.01x slower                                                       |
| dask                       | 391 ms                                                           | 397 ms: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 929 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                        |
| generators                 | 33.5 ms                                                          | 34.6 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.83 ms: 1.04x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| sympy_expand               | 501 ms                                                           | 522 ms: 1.04x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.12 sec: 1.05x slower                                                      |
| 2to3                       | 291 ms                                                           | 305 ms: 1.05x slower                                                        |
| thrift                     | 880 us                                                           | 922 us: 1.05x slower                                                        |
| sympy_str                  | 295 ms                                                           | 309 ms: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                      |
| sqlglot_optimize           | 59.5 ms                                                          | 62.7 ms: 1.05x slower                                                       |
| django_template            | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                       |
| regex_dna                  | 249 ms                                                           | 264 ms: 1.06x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 6.75 ms: 1.06x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 165 ms: 1.07x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.63 ms: 1.08x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 130 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 185 us: 1.08x slower                                                        |
| scimark_sor                | 119 ms                                                           | 129 ms: 1.09x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 105 ns: 1.09x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 96.1 ms: 1.09x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.5 us: 1.09x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 28.4 ms: 1.09x slower                                                       |
| async_generators           | 363 ms                                                           | 398 ms: 1.10x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 25.5 ms: 1.10x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.74 ms: 1.10x slower                                                       |
| raytrace                   | 260 ms                                                           | 288 ms: 1.11x slower                                                        |
| chaos                      | 59.6 ms                                                          | 66.4 ms: 1.11x slower                                                       |
| pylint                     | 339 ms                                                           | 378 ms: 1.11x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 65.5 ms: 1.13x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 114 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, json_loads, coverage, asyncio_tcp, tornado_http
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 72.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x