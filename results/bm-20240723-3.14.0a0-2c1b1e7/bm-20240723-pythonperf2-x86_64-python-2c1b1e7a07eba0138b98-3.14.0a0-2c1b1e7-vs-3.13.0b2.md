# Results vs. 3.13.0b2

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-x86_64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 99.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| html5lib       | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 767 ms: 1.17x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 305 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 553 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| float          | 80.2 ms                                                          | 81.3 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 83.8 ms: 1.02x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.44 sec: 1.02x slower                                                      |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.07 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.6 ms: 1.01x faster                                                       |
| django_template | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 288 us: 1.31x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.0 us: 1.29x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.3 ms: 1.19x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 767 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.92 us: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 305 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                        |
| scimark_sor                | 119 ms                                                           | 110 ms: 1.08x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.80 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.58 ms: 1.07x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 54.2 ms: 1.07x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.01 ms: 1.07x faster                                                       |
| coverage                   | 83.5 ms                                                          | 78.7 ms: 1.06x faster                                                       |
| scimark_fft                | 312 ms                                                           | 294 ms: 1.06x faster                                                        |
| regex_dna                  | 249 ms                                                           | 237 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.92 sec: 1.04x faster                                                      |
| bench_thread_pool          | 908 us                                                           | 872 us: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 553 ms: 1.04x faster                                                        |
| richards_super             | 61.2 ms                                                          | 59.1 ms: 1.03x faster                                                       |
| nbody                      | 87.8 ms                                                          | 85.1 ms: 1.03x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 94.9 ms: 1.03x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.26 us: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 83.8 ms: 1.02x faster                                                       |
| dask                       | 391 ms                                                           | 383 ms: 1.02x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 66.0 ms: 1.02x faster                                                       |
| go                         | 165 ms                                                           | 162 ms: 1.02x faster                                                        |
| richards                   | 53.4 ms                                                          | 52.5 ms: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| logging_format             | 7.11 us                                                          | 7.00 us: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.6 ms: 1.01x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 73.9 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 73.0 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 392 ms: 1.01x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.9 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| async_generators           | 363 ms                                                           | 361 ms: 1.00x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 814 ms: 1.00x faster                                                        |
| sympy_str                  | 295 ms                                                           | 294 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| hexiom                     | 6.35 ms                                                          | 6.37 ms: 1.00x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 156 ms: 1.00x slower                                                        |
| coroutines                 | 22.0 ms                                                          | 22.1 ms: 1.01x slower                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.72 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 172 us: 1.01x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                       |
| json                       | 5.35 ms                                                          | 5.41 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.6 ms: 1.01x slower                                                       |
| float                      | 80.2 ms                                                          | 81.3 ms: 1.01x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.44 sec: 1.02x slower                                                      |
| deltablue                  | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                                       |
| chaos                      | 59.6 ms                                                          | 60.6 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.9 ns: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 9.07 ms: 1.03x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                        |
| fannkuch                   | 353 ms                                                           | 367 ms: 1.04x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| pyflate                    | 482 ms                                                           | 504 ms: 1.05x slower                                                        |
| raytrace                   | 260 ms                                                           | 273 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.9 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (12): tornado_http, asyncio_tcp, scimark_lu, pprint_pformat, docutils, sympy_expand, json_loads, create_gc_cycles, thrift, xml_etree_iterparse, mako, pylint
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x