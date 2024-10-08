# Results vs. 3.13.0b2

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.02x faster
- HPT reliability: 99.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_none            | 492 ms                                                       | 446 ms: 1.10x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 732 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|--------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_generate | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| pickle_pure_python | 359 us                                                       | 364 us: 1.01x slower                                                    |
| json_dumps         | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| json_loads         | 32.1 us                                                      | 33.5 us: 1.04x slower                                                   |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, unpickle_pure_python, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                      | 8.87 ms: 1.03x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.5 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): django_template, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 332 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 38.7 us: 1.31x faster                                                   |
| deepcopy_reduce            | 4.04 us                                                      | 3.50 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 413 ms: 1.15x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 536 ms: 1.13x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 574 ms: 1.12x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.14 sec: 1.12x faster                                                  |
| async_tree_none            | 492 ms                                                       | 446 ms: 1.10x faster                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.12 sec: 1.10x faster                                                  |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 732 ms: 1.08x faster                                                    |
| richards                   | 55.9 ms                                                      | 52.3 ms: 1.07x faster                                                   |
| generators                 | 37.1 ms                                                      | 34.9 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 718 ms: 1.06x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.2 ms: 1.05x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.6 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 136 ms: 1.04x faster                                                    |
| gc_traversal               | 5.17 ms                                                      | 4.99 ms: 1.04x faster                                                   |
| logging_silent             | 133 ns                                                       | 129 ns: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 251 ms: 1.03x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.2 ms: 1.03x faster                                                   |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| asyncio_tcp                | 584 ms                                                       | 572 ms: 1.02x faster                                                    |
| meteor_contest             | 113 ms                                                       | 111 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.43 ms: 1.02x faster                                                   |
| xml_etree_generate         | 114 ms                                                       | 112 ms: 1.01x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| hexiom                     | 7.08 ms                                                      | 6.99 ms: 1.01x faster                                                   |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.01x faster                                                   |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                                  |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.20 sec: 1.01x faster                                                  |
| float                      | 91.4 ms                                                      | 91.9 ms: 1.01x slower                                                   |
| mdp                        | 3.33 sec                                                     | 3.35 sec: 1.01x slower                                                  |
| coverage                   | 98.4 ms                                                      | 99.4 ms: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| fannkuch                   | 451 ms                                                       | 458 ms: 1.01x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 364 us: 1.01x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 13.4 ms: 1.02x slower                                                   |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.02x slower                                                   |
| pyflate                    | 557 ms                                                       | 574 ms: 1.03x slower                                                    |
| json                       | 5.64 ms                                                      | 5.81 ms: 1.03x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.87 ms: 1.03x slower                                                   |
| json_loads                 | 32.1 us                                                      | 33.5 us: 1.04x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (48): xml_etree_parse, dask, deltablue, sqlglot_optimize, django_template, scimark_monte_carlo, sqlglot_normalize, telco, spectral_norm, 2to3, scimark_sor, sqlglot_parse, pylint, go, logging_simple, tomli_loads, docutils, sympy_expand, pidigits, regex_compile, nbody, thrift, unpickle_pure_python, python_startup, xml_etree_iterparse, create_gc_cycles, crypto_pyaes, asyncio_websockets, xml_etree_process, logging_format, bpe_tokeniser, sympy_sum, typing_runtime_protocols, chaos, comprehensions, genshi_text, sympy_str, pycparser, pprint_safe_repr, nqueens, bench_mp_pool, genshi_xml, dulwich_log, async_generators, sympy_integrate, raytrace, tornado_http, html5lib
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x