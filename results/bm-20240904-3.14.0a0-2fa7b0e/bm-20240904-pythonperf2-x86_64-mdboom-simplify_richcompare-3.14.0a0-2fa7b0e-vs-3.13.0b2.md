# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-x86_64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.03x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.92 sec: 1.02x faster                                                      |
| html5lib       | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 548 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.8 ms: 1.02x faster                                                       |
| float          | 80.2 ms                                                          | 79.2 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.03x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                       |
| regex_dna      | 249 ms                                                           | 255 ms: 1.02x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 310 us: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| tomli_loads          | 2.40 sec                                                         | 2.56 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.8 ms: 1.06x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| django_template | 39.0 ms                                                          | 40.3 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240904-pythonperf2-x86_64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 285 us: 1.33x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.4 us: 1.27x faster                                                       |
| go                         | 165 ms                                                           | 134 ms: 1.23x faster                                                        |
| generators                 | 33.5 ms                                                          | 28.4 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 397 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 792 ms: 1.14x faster                                                        |
| coverage                   | 83.5 ms                                                          | 74.9 ms: 1.12x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 309 ms: 1.10x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.0 ms: 1.09x faster                                                       |
| scimark_sor                | 119 ms                                                           | 109 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.53 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 816 ms: 1.07x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.1 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 570 ms: 1.06x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.8 ms: 1.06x faster                                                       |
| scimark_fft                | 312 ms                                                           | 296 ms: 1.06x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 70.9 ms: 1.05x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 863 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 548 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.96 sec: 1.04x faster                                                      |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.88 us: 1.03x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 366 ms: 1.03x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.17 ms: 1.03x faster                                                       |
| thrift                     | 880 us                                                           | 857 us: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 141 ms: 1.03x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.18 ms: 1.02x faster                                                       |
| nbody                      | 87.8 ms                                                          | 85.8 ms: 1.02x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.92 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 818 ms                                                           | 802 ms: 1.02x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 95.7 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| json                       | 5.35 ms                                                          | 5.28 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.0 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| float                      | 80.2 ms                                                          | 79.2 ms: 1.01x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.63 ms: 1.01x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.34 us: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.32 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 59.3 ms: 1.00x faster                                                       |
| sympy_str                  | 295 ms                                                           | 294 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x slower                                                        |
| sympy_expand               | 501 ms                                                           | 503 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 121 ms: 1.01x slower                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 74.1 ms: 1.01x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 310 us: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.42 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.7 ms: 1.02x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 22.4 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                                      |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.47 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 360 ms: 1.02x slower                                                        |
| async_generators           | 363 ms                                                           | 371 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| regex_dna                  | 249 ms                                                           | 255 ms: 1.02x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.08 ms: 1.03x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.03x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.8 ms: 1.03x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                       |
| django_template            | 39.0 ms                                                          | 40.3 ms: 1.04x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.4 ms: 1.04x slower                                                       |
| chaos                      | 59.6 ms                                                          | 62.8 ms: 1.05x slower                                                       |
| raytrace                   | 260 ms                                                           | 275 ms: 1.05x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.56 sec: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (8): create_gc_cycles, pyflate, asyncio_tcp_ssl, xml_etree_iterparse, json_loads, pycparser, mako, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x