# Results vs. 3.13.0b2

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-x86_64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.00x slower
- HPT reliability: 99.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 288 ms: 1.01x faster                                                        |
| chameleon      | 7.40 ms                                                          | 7.50 ms: 1.01x slower                                                       |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| html5lib       | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 917 ms: 1.02x slower                                                        |
| async_tree_none_tg        | 340 ms                                                           | 351 ms: 1.03x slower                                                        |
| async_tree_memoization_tg | 421 ms                                                           | 435 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 627 ms: 1.04x slower                                                        |
| async_tree_io             | 873 ms                                                           | 907 ms: 1.04x slower                                                        |
| async_tree_none           | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| async_tree_memoization    | 460 ms                                                           | 483 ms: 1.05x slower                                                        |
| Geometric mean            | (ref)                                                            | 1.03x slower                                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.1 ms: 1.04x faster                                                       |
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                           | 144 ms: 1.00x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| pickle_dict          | 32.8 us                                                          | 31.5 us: 1.04x faster                                                       |
| json_loads           | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| pickle_list          | 4.44 us                                                          | 4.39 us: 1.01x faster                                                       |
| pickle               | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 86.4 ms: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                           | 146 ms: 1.01x slower                                                        |
| xml_etree_process    | 59.7 ms                                                          | 60.8 ms: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.48 sec: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (3): json_dumps, xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.1 ms: 1.01x faster                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.83 ms: 1.00x faster                                                       |
| Geometric mean         | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 58.6 ms: 1.01x slower                                                       |
| django_template | 39.0 ms                                                          | 40.1 ms: 1.03x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 26.7 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240525-pythonperf2-x86_64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|---------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pathlib                   | 17.1 ms                                                          | 16.1 ms: 1.06x faster                                                       |
| go                        | 165 ms                                                           | 156 ms: 1.06x faster                                                        |
| unpickle_pure_python      | 224 us                                                           | 213 us: 1.05x faster                                                        |
| pickle_dict               | 32.8 us                                                          | 31.5 us: 1.04x faster                                                       |
| richards_super            | 61.2 ms                                                          | 58.9 ms: 1.04x faster                                                       |
| regex_v8                  | 26.0 ms                                                          | 25.1 ms: 1.04x faster                                                       |
| richards                  | 53.4 ms                                                          | 51.9 ms: 1.03x faster                                                       |
| scimark_monte_carlo       | 65.5 ms                                                          | 63.6 ms: 1.03x faster                                                       |
| json                      | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                                       |
| coverage                  | 83.5 ms                                                          | 81.2 ms: 1.03x faster                                                       |
| json_loads                | 25.0 us                                                          | 24.5 us: 1.02x faster                                                       |
| regex_dna                 | 249 ms                                                           | 245 ms: 1.02x faster                                                        |
| html5lib                  | 74.7 ms                                                          | 73.3 ms: 1.02x faster                                                       |
| meteor_contest            | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| asyncio_tcp               | 378 ms                                                           | 373 ms: 1.01x faster                                                        |
| unpickle                  | 15.7 us                                                          | 15.5 us: 1.01x faster                                                       |
| pickle_list               | 4.44 us                                                          | 4.39 us: 1.01x faster                                                       |
| 2to3                      | 291 ms                                                           | 288 ms: 1.01x faster                                                        |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| python_startup            | 13.2 ms                                                          | 13.1 ms: 1.01x faster                                                       |
| crypto_pyaes              | 73.6 ms                                                          | 72.9 ms: 1.01x faster                                                       |
| pyflate                   | 482 ms                                                           | 478 ms: 1.01x faster                                                        |
| docutils                  | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                      |
| python_startup_no_site    | 8.85 ms                                                          | 8.83 ms: 1.00x faster                                                       |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.27 ms: 1.00x faster                                                       |
| pidigits                  | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| regex_compile             | 144 ms                                                           | 144 ms: 1.00x slower                                                        |
| hexiom                    | 6.35 ms                                                          | 6.38 ms: 1.00x slower                                                       |
| sqlglot_normalize         | 120 ms                                                           | 121 ms: 1.01x slower                                                        |
| sympy_str                 | 295 ms                                                           | 296 ms: 1.01x slower                                                        |
| spectral_norm             | 97.3 ms                                                          | 97.9 ms: 1.01x slower                                                       |
| sqlite_synth              | 2.80 us                                                          | 2.81 us: 1.01x slower                                                       |
| gc_traversal              | 4.69 ms                                                          | 4.71 ms: 1.01x slower                                                       |
| pickle                    | 10.6 us                                                          | 10.7 us: 1.01x slower                                                       |
| dulwich_log               | 67.3 ms                                                          | 67.8 ms: 1.01x slower                                                       |
| xml_etree_generate        | 85.7 ms                                                          | 86.4 ms: 1.01x slower                                                       |
| sqlglot_parse             | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                       |
| sympy_integrate           | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                       |
| genshi_xml                | 58.1 ms                                                          | 58.6 ms: 1.01x slower                                                       |
| pprint_safe_repr          | 818 ms                                                           | 826 ms: 1.01x slower                                                        |
| mdp                       | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| generators                | 33.5 ms                                                          | 33.9 ms: 1.01x slower                                                       |
| thrift                    | 880 us                                                           | 889 us: 1.01x slower                                                        |
| fannkuch                  | 353 ms                                                           | 357 ms: 1.01x slower                                                        |
| sympy_expand              | 501 ms                                                           | 507 ms: 1.01x slower                                                        |
| async_generators          | 363 ms                                                           | 367 ms: 1.01x slower                                                        |
| pprint_pformat            | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                      |
| xml_etree_parse           | 144 ms                                                           | 146 ms: 1.01x slower                                                        |
| chameleon                 | 7.40 ms                                                          | 7.50 ms: 1.01x slower                                                       |
| typing_runtime_protocols  | 171 us                                                           | 173 us: 1.02x slower                                                        |
| dask                      | 391 ms                                                           | 397 ms: 1.02x slower                                                        |
| regex_effbot              | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                       |
| xml_etree_process         | 59.7 ms                                                          | 60.8 ms: 1.02x slower                                                       |
| async_tree_io_tg          | 900 ms                                                           | 917 ms: 1.02x slower                                                        |
| logging_simple            | 6.40 us                                                          | 6.52 us: 1.02x slower                                                       |
| logging_silent            | 96.3 ns                                                          | 98.3 ns: 1.02x slower                                                       |
| pickle_pure_python        | 307 us                                                           | 316 us: 1.03x slower                                                        |
| django_template           | 39.0 ms                                                          | 40.1 ms: 1.03x slower                                                       |
| pycparser                 | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                      |
| raytrace                  | 260 ms                                                           | 268 ms: 1.03x slower                                                        |
| deepcopy                  | 377 us                                                           | 388 us: 1.03x slower                                                        |
| genshi_text               | 25.9 ms                                                          | 26.7 ms: 1.03x slower                                                       |
| async_tree_none_tg        | 340 ms                                                           | 351 ms: 1.03x slower                                                        |
| deepcopy_reduce           | 3.39 us                                                          | 3.50 us: 1.03x slower                                                       |
| tomli_loads               | 2.40 sec                                                         | 2.48 sec: 1.03x slower                                                      |
| async_tree_memoization_tg | 421 ms                                                           | 435 ms: 1.04x slower                                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 627 ms: 1.04x slower                                                        |
| async_tree_io             | 873 ms                                                           | 907 ms: 1.04x slower                                                        |
| chaos                     | 59.6 ms                                                          | 61.9 ms: 1.04x slower                                                       |
| async_tree_none           | 365 ms                                                           | 380 ms: 1.04x slower                                                        |
| scimark_sor               | 119 ms                                                           | 124 ms: 1.04x slower                                                        |
| deepcopy_memo             | 37.3 us                                                          | 39.1 us: 1.05x slower                                                       |
| async_tree_memoization    | 460 ms                                                           | 483 ms: 1.05x slower                                                        |
| nqueens                   | 88.4 ms                                                          | 93.4 ms: 1.06x slower                                                       |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (24): bench_mp_pool, scimark_fft, telco, mako, coroutines, float, tornado_http, scimark_lu, asyncio_tcp_ssl, sqlglot_optimize, deltablue, sqlglot_transpile, json_dumps, sympy_sum, comprehensions, create_gc_cycles, xml_etree_iterparse, logging_format, unpickle_list, bench_thread_pool, flaskblogging, nbody, pylint, async_tree_cpu_io_mixed_tg
Ignored benchmarks (4) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, gunicorn, mypy2

# HPT report

- Reliability score: 99.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x