# Results vs. 3.13.0b2

- fork: python
- ref: 5436d8b9c397c48d9b0d
- machine: linux-aarch64
- commit hash: 5436d8b
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.02 sec: 1.03x faster                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 425 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 560 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.07x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 729 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| float          | 91.4 ms                                                      | 91.8 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse    | 191 ms                                                       | 185 ms: 1.03x faster                                                    |
| xml_etree_process  | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| unpickle_list      | 6.52 us                                                      | 6.38 us: 1.02x faster                                                   |
| unpickle           | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| json_loads         | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| pickle_list        | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| tomli_loads        | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python | 359 us                                                       | 368 us: 1.03x slower                                                    |
| json_dumps         | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_iterparse, pickle_dict, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| mako            | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 331 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.6 us: 1.35x faster                                                   |
| go                         | 161 ms                                                       | 138 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 425 ms: 1.16x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 560 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.54 us: 1.14x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 422 ms: 1.13x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 553 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 725 ms: 1.09x faster                                                    |
| pathlib                    | 22.8 ms                                                      | 20.9 ms: 1.09x faster                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.07x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 551 ms: 1.06x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.9 ms: 1.06x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.17 sec: 1.05x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 729 ms: 1.05x faster                                                    |
| regex_dna                  | 259 ms                                                       | 247 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.6 ms: 1.04x faster                                                   |
| thrift                     | 962 us                                                       | 924 us: 1.04x faster                                                    |
| nbody                      | 114 ms                                                       | 110 ms: 1.04x faster                                                    |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| xml_etree_parse            | 191 ms                                                       | 185 ms: 1.03x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.88 sec: 1.03x faster                                                  |
| docutils                   | 3.10 sec                                                     | 3.02 sec: 1.03x faster                                                  |
| bench_thread_pool          | 1.26 ms                                                      | 1.23 ms: 1.02x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 2.28 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 933 ms                                                       | 911 ms: 1.02x faster                                                    |
| django_template            | 42.3 ms                                                      | 41.4 ms: 1.02x faster                                                   |
| xml_etree_process          | 80.8 ms                                                      | 79.0 ms: 1.02x faster                                                   |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                                   |
| unpickle_list              | 6.52 us                                                      | 6.38 us: 1.02x faster                                                   |
| unpickle                   | 19.8 us                                                      | 19.4 us: 1.02x faster                                                   |
| logging_simple             | 7.21 us                                                      | 7.06 us: 1.02x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.89 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.69 us: 1.02x faster                                                   |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| json_loads                 | 32.1 us                                                      | 31.7 us: 1.01x faster                                                   |
| scimark_sor                | 159 ms                                                       | 157 ms: 1.01x faster                                                    |
| comprehensions             | 20.5 us                                                      | 20.3 us: 1.01x faster                                                   |
| sympy_integrate            | 20.9 ms                                                      | 20.6 ms: 1.01x faster                                                   |
| gc_traversal               | 5.17 ms                                                      | 5.12 ms: 1.01x faster                                                   |
| pickle_list                | 5.27 us                                                      | 5.23 us: 1.01x faster                                                   |
| float                      | 91.4 ms                                                      | 91.8 ms: 1.00x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                                   |
| asyncio_websockets         | 657 ms                                                       | 663 ms: 1.01x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| spectral_norm              | 141 ms                                                       | 143 ms: 1.01x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 100 ms: 1.01x slower                                                    |
| fannkuch                   | 451 ms                                                       | 459 ms: 1.02x slower                                                    |
| raytrace                   | 297 ms                                                       | 302 ms: 1.02x slower                                                    |
| telco                      | 10.0 ms                                                      | 10.2 ms: 1.02x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.63 sec: 1.02x slower                                                  |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                                   |
| pickle_pure_python         | 359 us                                                       | 368 us: 1.03x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| scimark_fft                | 445 ms                                                       | 471 ms: 1.06x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (39): sqlglot_normalize, dulwich_log, json, sympy_sum, sqlglot_parse, meteor_contest, scimark_sparse_mat_mult, logging_silent, xml_etree_generate, pycparser, coverage, sympy_str, typing_runtime_protocols, tornado_http, genshi_text, html5lib, sqlglot_optimize, scimark_monte_carlo, crypto_pyaes, python_startup_no_site, regex_v8, python_startup, xml_etree_iterparse, bench_mp_pool, pidigits, asyncio_tcp_ssl, pyflate, async_generators, deltablue, mdp, hexiom, bpe_tokeniser, pickle_dict, chaos, sqlite_synth, sympy_expand, genshi_xml, unpickle_pure_python, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-5436d8b/bm-20240911-arminc-aarch64-python-5436d8b9c397c48d9b0d-3.14.0a0-5436d8b.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x