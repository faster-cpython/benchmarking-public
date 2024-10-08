# Results vs. 3.13.0b2

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 285 ms: 1.02x faster                                                        |
| html5lib       | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 784 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 331 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 381 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 808 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 89.8 ms: 1.02x slower                                                       |
| float          | 80.2 ms                                                          | 82.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.26 sec: 1.06x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 83.8 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 313 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (2): json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.3 ms: 1.05x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.1 ms: 1.03x faster                                                       |
| django_template | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.3 us: 1.23x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.7 ms: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 784 ms: 1.15x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.97 us: 1.14x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                        |
| async_tree_none            | 365 ms                                                           | 331 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 381 ms: 1.10x faster                                                        |
| scimark_sor                | 119 ms                                                           | 108 ms: 1.10x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.51 ms: 1.09x faster                                                       |
| async_tree_io              | 873 ms                                                           | 808 ms: 1.08x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.7 ms: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| richards                   | 53.4 ms                                                          | 50.1 ms: 1.07x faster                                                       |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.40 ms: 1.07x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.26 sec: 1.06x faster                                                      |
| telco                      | 8.40 ms                                                          | 7.90 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.89 sec: 1.05x faster                                                      |
| genshi_xml                 | 58.1 ms                                                          | 55.3 ms: 1.05x faster                                                       |
| coverage                   | 83.5 ms                                                          | 79.6 ms: 1.05x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.80 us: 1.05x faster                                                       |
| scimark_fft                | 312 ms                                                           | 299 ms: 1.04x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 870 us: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 94.1 ms: 1.04x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.18 us: 1.04x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.1 ms: 1.03x faster                                                       |
| async_generators           | 363 ms                                                           | 352 ms: 1.03x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 83.8 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                           | 285 ms: 1.02x faster                                                        |
| thrift                     | 880 us                                                           | 863 us: 1.02x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.01x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                       |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 72.8 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| sympy_str                  | 295 ms                                                           | 293 ms: 1.01x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.32 ms: 1.01x faster                                                       |
| sympy_expand               | 501 ms                                                           | 499 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 22.1 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 121 ms: 1.00x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.77 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                       |
| json                       | 5.35 ms                                                          | 5.41 ms: 1.01x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                      |
| django_template            | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                                       |
| raytrace                   | 260 ms                                                           | 265 ms: 1.02x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 98.1 ns: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 313 us: 1.02x slower                                                        |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                       |
| pyflate                    | 482 ms                                                           | 491 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.70 sec: 1.02x slower                                                      |
| nbody                      | 87.8 ms                                                          | 89.8 ms: 1.02x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 90.4 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 839 ms: 1.03x slower                                                        |
| float                      | 80.2 ms                                                          | 82.3 ms: 1.03x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 175 us: 1.03x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.4 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.54 sec: 1.03x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                       |
| fannkuch                   | 353 ms                                                           | 374 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (9): create_gc_cycles, json_dumps, mako, docutils, xml_etree_parse, asyncio_tcp_ssl, sympy_integrate, sqlglot_parse, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x