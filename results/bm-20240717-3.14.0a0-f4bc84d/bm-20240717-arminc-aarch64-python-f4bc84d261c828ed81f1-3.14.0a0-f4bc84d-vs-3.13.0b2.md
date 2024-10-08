# Results vs. 3.13.0b2

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-aarch64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.01x faster
- HPT reliability: 57.92%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 301 ms: 1.01x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.06 sec: 1.01x faster                                                  |
| html5lib       | 66.1 ms                                                      | 68.0 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.13x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| regex_v8       | 31.1 ms                                                      | 30.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| tomli_loads        | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                  |
| json_loads         | 32.1 us                                                      | 33.1 us: 1.03x slower                                                   |
| json_dumps         | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, xml_etree_iterparse, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 60.4 ms                                                      | 62.3 ms: 1.03x slower                                                   |
| mako           | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| genshi_text    | 27.4 ms                                                      | 28.8 ms: 1.05x slower                                                   |
| Geometric mean | (ref)                                                        | 1.03x slower                                                            |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 39.3 us: 1.29x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.42 us: 1.18x faster                                                   |
| async_tree_memoization     | 645 ms                                                       | 551 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 407 ms: 1.17x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.10 sec: 1.16x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.07 sec: 1.14x faster                                                  |
| async_tree_memoization_tg  | 604 ms                                                       | 534 ms: 1.13x faster                                                    |
| async_tree_none            | 492 ms                                                       | 439 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 729 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.8 ms: 1.04x faster                                                   |
| richards_super             | 62.3 ms                                                      | 60.3 ms: 1.03x faster                                                   |
| regex_dna                  | 259 ms                                                       | 252 ms: 1.03x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 5.07 ms: 1.02x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 139 ms: 1.02x faster                                                    |
| create_gc_cycles           | 2.33 ms                                                      | 2.29 ms: 1.02x faster                                                   |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.06 sec: 1.01x faster                                                  |
| 2to3                       | 305 ms                                                       | 301 ms: 1.01x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.8 ms: 1.01x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 113 ms: 1.01x faster                                                    |
| tomli_loads                | 2.57 sec                                                     | 2.56 sec: 1.00x faster                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.22 sec: 1.01x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 939 ms: 1.01x slower                                                    |
| coverage                   | 98.4 ms                                                      | 99.2 ms: 1.01x slower                                                   |
| sympy_str                  | 265 ms                                                       | 268 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| sympy_expand               | 457 ms                                                       | 463 ms: 1.01x slower                                                    |
| raytrace                   | 297 ms                                                       | 300 ms: 1.01x slower                                                    |
| dulwich_log                | 58.5 ms                                                      | 59.5 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 93.1 ms: 1.02x slower                                                   |
| generators                 | 37.1 ms                                                      | 37.8 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.67 ms: 1.02x slower                                                   |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                   |
| html5lib                   | 66.1 ms                                                      | 68.0 ms: 1.03x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.1 us: 1.03x slower                                                   |
| genshi_xml                 | 60.4 ms                                                      | 62.3 ms: 1.03x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 200 us: 1.03x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.6 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.90 ms: 1.04x slower                                                   |
| json                       | 5.64 ms                                                      | 5.85 ms: 1.04x slower                                                   |
| pyflate                    | 557 ms                                                       | 580 ms: 1.04x slower                                                    |
| fannkuch                   | 451 ms                                                       | 470 ms: 1.04x slower                                                    |
| genshi_text                | 27.4 ms                                                      | 28.8 ms: 1.05x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.9 ms: 1.06x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (41): xml_etree_parse, sqlglot_parse, asyncio_tcp, async_generators, pickle_pure_python, pprint_pformat, nbody, deltablue, crypto_pyaes, spectral_norm, mdp, sqlglot_optimize, pidigits, coroutines, comprehensions, bpe_tokeniser, asyncio_websockets, chaos, scimark_monte_carlo, python_startup, nqueens, django_template, sqlglot_normalize, xml_etree_iterparse, go, scimark_sor, scimark_fft, pylint, logging_format, bench_mp_pool, pycparser, xml_etree_process, hexiom, unpickle_pure_python, thrift, logging_silent, logging_simple, regex_compile, sympy_sum, tornado_http, sympy_integrate
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 57.92% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x