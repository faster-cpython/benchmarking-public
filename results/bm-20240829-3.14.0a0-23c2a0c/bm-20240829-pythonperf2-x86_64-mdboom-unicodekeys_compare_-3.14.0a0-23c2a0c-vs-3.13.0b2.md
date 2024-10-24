# Results vs. 3.13.0b2

- fork: mdboom
- ref: unicodekeys_compare_
- machine: linux-x86_64
- commit hash: 23c2a0c
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                                      |
| html5lib       | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.11x faster                                                        |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.2 ms: 1.03x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| float          | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 221 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 313 us: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.07 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| django_template | 39.0 ms                                                          | 40.7 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-pythonperf2-x86_64-mdboom-unicodekeys_compare_-3.14.0a0-23c2a0c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 288 us: 1.31x faster                                                        |
| go                         | 165 ms                                                           | 134 ms: 1.23x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.5 us: 1.22x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.7 ms: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                       |
| async_tree_none            | 365 ms                                                           | 320 ms: 1.14x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.11x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.2 ms: 1.09x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.52 ms: 1.09x faster                                                       |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 391 ms: 1.08x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 849 us: 1.07x faster                                                        |
| regex_dna                  | 249 ms                                                           | 233 ms: 1.07x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.4 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 70.7 ms: 1.06x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 55.2 ms: 1.05x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                       |
| coverage                   | 83.5 ms                                                          | 79.6 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.93 sec: 1.04x faster                                                      |
| logging_format             | 7.11 us                                                          | 6.84 us: 1.04x faster                                                       |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 150 ms: 1.03x faster                                                        |
| nbody                      | 87.8 ms                                                          | 85.2 ms: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                           | 283 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.91 sec: 1.02x faster                                                      |
| scimark_lu                 | 97.5 ms                                                          | 95.2 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.26 us: 1.02x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| sympy_str                  | 295 ms                                                           | 289 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 371 ms: 1.02x faster                                                        |
| json                       | 5.35 ms                                                          | 5.27 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 221 us: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.22 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| sympy_expand               | 501 ms                                                           | 495 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 809 ms: 1.01x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 84.9 ms: 1.01x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.30 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.6 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                      |
| pyflate                    | 482 ms                                                           | 479 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 73.3 ms: 1.00x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 120 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| regex_v8                   | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| xml_etree_parse            | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| float                      | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.4 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| async_generators           | 363 ms                                                           | 369 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.5 ms: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 313 us: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                          | 17.2 us: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 98.0 ns: 1.02x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.44 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 359 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| python_startup_no_site     | 8.85 ms                                                          | 9.07 ms: 1.02x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.9 ms: 1.04x slower                                                       |
| django_template            | 39.0 ms                                                          | 40.7 ms: 1.04x slower                                                       |
| raytrace                   | 260 ms                                                           | 276 ms: 1.06x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.57 sec: 1.07x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (8): create_gc_cycles, telco, thrift, typing_runtime_protocols, mako, scimark_sor, xml_etree_process, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x