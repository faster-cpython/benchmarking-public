# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 69.2 ms: 1.08x faster                                                       |
| tornado_http   | 119 ms                                                           | 115 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 395 ms: 1.16x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 779 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 817 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                       |
| float          | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.42 ms: 1.01x slower                                                       |
| regex_dna      | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 212 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 313 us: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.60 sec: 1.08x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.5 ms: 1.07x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| django_template | 39.0 ms                                                          | 40.2 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 28.9 us: 1.29x faster                                                       |
| go                         | 165 ms                                                           | 135 ms: 1.23x faster                                                        |
| generators                 | 33.5 ms                                                          | 28.5 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 395 ms: 1.16x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 779 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| richards_super             | 61.2 ms                                                          | 55.7 ms: 1.10x faster                                                       |
| scimark_sor                | 119 ms                                                           | 109 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 387 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 69.2 ms: 1.08x faster                                                       |
| richards                   | 53.4 ms                                                          | 49.6 ms: 1.08x faster                                                       |
| async_tree_io              | 873 ms                                                           | 817 ms: 1.07x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.5 ms: 1.07x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 852 us: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 212 us: 1.06x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| thrift                     | 880 us                                                           | 841 us: 1.05x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.48 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.91 sec: 1.05x faster                                                      |
| logging_format             | 7.11 us                                                          | 6.81 us: 1.04x faster                                                       |
| nbody                      | 87.8 ms                                                          | 84.1 ms: 1.04x faster                                                       |
| scimark_fft                | 312 ms                                                           | 299 ms: 1.04x faster                                                        |
| tornado_http               | 119 ms                                                           | 115 ms: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.22 us: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 367 ms: 1.03x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 796 ms: 1.03x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.91 sec: 1.03x faster                                                      |
| json                       | 5.35 ms                                                          | 5.23 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 151 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.24 ms: 1.02x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.1 ms: 1.02x faster                                                       |
| float                      | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 96.0 ms: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.8 ms: 1.02x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.02x faster                                                      |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.0 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.7 ms: 1.01x faster                                                       |
| sympy_expand               | 501 ms                                                           | 496 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.31 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.26 ms: 1.01x faster                                                       |
| async_generators           | 363 ms                                                           | 361 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| fannkuch                   | 353 ms                                                           | 354 ms: 1.00x slower                                                        |
| pyflate                    | 482 ms                                                           | 484 ms: 1.01x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.42 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.4 ms: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.5 ns: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| chaos                      | 59.6 ms                                                          | 60.5 ms: 1.01x slower                                                       |
| regex_dna                  | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 313 us: 1.02x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 268 ms: 1.03x slower                                                        |
| django_template            | 39.0 ms                                                          | 40.2 ms: 1.03x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 27.3 ms: 1.05x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.60 sec: 1.08x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (12): bench_mp_pool, mako, sqlglot_normalize, deltablue, xml_etree_parse, pycparser, crypto_pyaes, create_gc_cycles, json_loads, json_dumps, typing_runtime_protocols, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.01x