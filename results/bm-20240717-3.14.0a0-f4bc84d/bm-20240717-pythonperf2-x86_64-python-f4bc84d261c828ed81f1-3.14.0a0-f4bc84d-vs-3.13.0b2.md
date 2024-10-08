# Results vs. 3.13.0b2

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-x86_64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| html5lib       | 74.7 ms                                                          | 73.4 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 766 ms: 1.17x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 796 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.9 ms: 1.00x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| nbody          | 87.8 ms                                                          | 90.9 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.3 ms: 1.01x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|---------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate  | 85.7 ms                                                          | 84.5 ms: 1.01x faster                                                       |
| tomli_loads         | 2.40 sec                                                         | 2.43 sec: 1.01x slower                                                      |
| json_loads          | 25.0 us                                                          | 25.4 us: 1.02x slower                                                       |
| pickle_pure_python  | 307 us                                                           | 313 us: 1.02x slower                                                        |
| json_dumps          | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| xml_etree_iterparse | 103 ms                                                           | 105 ms: 1.03x slower                                                        |
| Geometric mean      | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (3): unpickle_pure_python, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.11 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 56.0 ms: 1.04x faster                                                       |
| genshi_text    | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| mako           | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 283 us: 1.33x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.3 us: 1.27x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 766 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.89 us: 1.17x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.12x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 796 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                        |
| scimark_sor                | 119 ms                                                           | 110 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.04 ms: 1.06x faster                                                       |
| go                         | 165 ms                                                           | 156 ms: 1.06x faster                                                        |
| richards_super             | 61.2 ms                                                          | 57.9 ms: 1.06x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.48 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 578 ms: 1.04x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.1 ms: 1.04x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.93 sec: 1.04x faster                                                      |
| richards                   | 53.4 ms                                                          | 51.5 ms: 1.04x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 875 us: 1.04x faster                                                        |
| coverage                   | 83.5 ms                                                          | 80.6 ms: 1.04x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 56.0 ms: 1.04x faster                                                       |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                           | 124 ms: 1.03x faster                                                        |
| pyflate                    | 482 ms                                                           | 468 ms: 1.03x faster                                                        |
| scimark_fft                | 312 ms                                                           | 303 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 71.6 ms: 1.03x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.96 us: 1.02x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.21 ms: 1.02x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 73.4 ms: 1.02x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.27 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.31 us: 1.01x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 96.1 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.5 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 373 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.8 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                       |
| 2to3                       | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 171 us                                                           | 169 us: 1.01x faster                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.0 ms: 1.01x faster                                                       |
| float                      | 80.2 ms                                                          | 79.9 ms: 1.00x faster                                                       |
| sympy_str                  | 295 ms                                                           | 294 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 23.2 ms: 1.00x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.67 sec: 1.00x slower                                                      |
| json                       | 5.35 ms                                                          | 5.38 ms: 1.01x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 156 ms: 1.01x slower                                                        |
| sympy_expand               | 501 ms                                                           | 505 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.43 sec: 1.01x slower                                                      |
| regex_v8                   | 26.0 ms                                                          | 26.3 ms: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                       |
| generators                 | 33.5 ms                                                          | 33.9 ms: 1.01x slower                                                       |
| dulwich_log                | 67.3 ms                                                          | 68.2 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.8 ns: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 313 us: 1.02x slower                                                        |
| json_dumps                 | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.5 ms: 1.02x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 900 us: 1.02x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 105 ms: 1.03x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.11 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| fannkuch                   | 353 ms                                                           | 365 ms: 1.04x slower                                                        |
| nbody                      | 87.8 ms                                                          | 90.9 ms: 1.04x slower                                                       |
| raytrace                   | 260 ms                                                           | 272 ms: 1.05x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (14): bench_mp_pool, pylint, unpickle_pure_python, xml_etree_parse, tornado_http, docutils, create_gc_cycles, django_template, async_generators, nqueens, asyncio_tcp_ssl, pprint_safe_repr, comprehensions, xml_etree_process
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x