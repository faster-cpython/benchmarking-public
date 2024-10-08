# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.92 sec: 1.02x faster                                                      |
| html5lib       | 74.7 ms                                                          | 70.2 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 791 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 91.4 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 232 ms: 1.07x faster                                                        |
| regex_compile  | 144 ms                                                           | 141 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 60.0 ms: 1.00x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 86.3 ms: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (3): json_dumps, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                       |
| django_template | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240903-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 288 us: 1.31x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.5 us: 1.26x faster                                                       |
| go                         | 165 ms                                                           | 136 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.92 us: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| generators                 | 33.5 ms                                                          | 29.4 ms: 1.14x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 791 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.6 ms: 1.10x faster                                                       |
| richards_super             | 61.2 ms                                                          | 56.4 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| regex_dna                  | 249 ms                                                           | 232 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 818 ms: 1.07x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.2 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 70.2 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 569 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.43 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 543 ms: 1.05x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.88 sec: 1.05x faster                                                      |
| bench_thread_pool          | 908 us                                                           | 864 us: 1.05x faster                                                        |
| scimark_fft                | 312 ms                                                           | 300 ms: 1.04x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.86 us: 1.04x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.16 ms: 1.03x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 94.8 ms: 1.03x faster                                                       |
| thrift                     | 880 us                                                           | 856 us: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 141 ms: 1.03x faster                                                        |
| meteor_contest             | 128 ms                                                           | 125 ms: 1.03x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.21 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 370 ms: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.26 us: 1.02x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.21 ms: 1.02x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.92 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 818 ms                                                           | 801 ms: 1.02x faster                                                        |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                                       |
| json                       | 5.35 ms                                                          | 5.28 ms: 1.01x faster                                                       |
| pyflate                    | 482 ms                                                           | 476 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| sympy_expand               | 501 ms                                                           | 496 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.8 ms: 1.01x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.6 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 72.8 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| scimark_sor                | 119 ms                                                           | 118 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                      |
| async_generators           | 363 ms                                                           | 360 ms: 1.01x faster                                                        |
| nqueens                    | 88.4 ms                                                          | 87.8 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.3 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 60.0 ms: 1.00x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.47 sec: 1.00x slower                                                      |
| xml_etree_generate         | 85.7 ms                                                          | 86.3 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 97.4 ns: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.7 ms: 1.02x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.02x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 314 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 362 ms: 1.03x slower                                                        |
| raytrace                   | 260 ms                                                           | 268 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 27.0 ms: 1.04x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.8 ms: 1.04x slower                                                       |
| nbody                      | 87.8 ms                                                          | 91.4 ms: 1.04x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (11): bench_mp_pool, float, genshi_text, spectral_norm, sqlglot_normalize, json_dumps, create_gc_cycles, mako, xml_etree_iterparse, json_loads, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x