# Results vs. 3.13.0b2

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 99.93%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 285 ms: 1.02x faster                                                        |
| html5lib       | 74.7 ms                                                          | 72.9 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 778 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 381 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 573 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_dna      | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.20 sec: 1.09x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 218 us: 1.03x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 85.0 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| json_loads           | 25.0 us                                                          | 25.7 us: 1.03x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 320 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.9 ms                                                          | 25.1 ms: 1.03x faster                                                       |
| genshi_xml      | 58.1 ms                                                          | 56.6 ms: 1.03x faster                                                       |
| django_template | 39.0 ms                                                          | 38.7 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.5 us: 1.22x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.8 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.16x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 778 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 402 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 381 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.20 sec: 1.09x faster                                                      |
| gc_traversal               | 4.69 ms                                                          | 4.35 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| richards_super             | 61.2 ms                                                          | 57.2 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.61 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 573 ms: 1.05x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 861 us: 1.05x faster                                                        |
| go                         | 165 ms                                                           | 158 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.91 sec: 1.05x faster                                                      |
| richards                   | 53.4 ms                                                          | 51.4 ms: 1.04x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.11 ms: 1.04x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.87 us: 1.03x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.1 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_dna                  | 249 ms                                                           | 242 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.22 us: 1.03x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 218 us: 1.03x faster                                                        |
| dask                       | 391 ms                                                           | 380 ms: 1.03x faster                                                        |
| scimark_fft                | 312 ms                                                           | 304 ms: 1.03x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 56.6 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.9 ms: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                           | 285 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                                       |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.4 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| thrift                     | 880 us                                                           | 866 us: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.2 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 85.0 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                        |
| django_template            | 39.0 ms                                                          | 38.7 ms: 1.01x faster                                                       |
| pyflate                    | 482 ms                                                           | 479 ms: 1.01x faster                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.76 ms: 1.00x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.1 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| nqueens                    | 88.4 ms                                                          | 88.1 ms: 1.00x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.34 ms: 1.00x faster                                                       |
| sympy_expand               | 501 ms                                                           | 502 ms: 1.00x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.40 ms: 1.01x slower                                                       |
| meteor_contest             | 128 ms                                                           | 129 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| coverage                   | 83.5 ms                                                          | 84.2 ms: 1.01x slower                                                       |
| json                       | 5.35 ms                                                          | 5.41 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| float                      | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 98.6 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| async_generators           | 363 ms                                                           | 367 ms: 1.01x slower                                                        |
| scimark_sor                | 119 ms                                                           | 120 ms: 1.01x slower                                                        |
| fannkuch                   | 353 ms                                                           | 359 ms: 1.02x slower                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 105 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 838 ms: 1.03x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.7 us: 1.03x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.71 sec: 1.03x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.03x slower                                                        |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.03x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 320 us: 1.04x slower                                                        |
| raytrace                   | 260 ms                                                           | 274 ms: 1.05x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.9 ms: 1.05x slower                                                       |
| chaos                      | 59.6 ms                                                          | 62.8 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (10): create_gc_cycles, nbody, pycparser, docutils, pidigits, sqlglot_parse, crypto_pyaes, logging_silent, mako, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.93% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x