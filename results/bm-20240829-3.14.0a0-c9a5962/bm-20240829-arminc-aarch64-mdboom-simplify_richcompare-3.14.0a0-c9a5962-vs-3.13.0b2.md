# Results vs. 3.13.0b2

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| docutils       | 3.10 sec                                                     | 3.04 sec: 1.02x faster                                                  |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 426 ms: 1.15x faster                                                    |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| Geometric mean             | (ref)                                                        | 1.11x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| float          | 91.4 ms                                                      | 93.4 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| regex_dna      | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| regex_compile  | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| regex_effbot   | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                        | 1.02x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| json_loads     | 32.1 us                                                      | 32.4 us: 1.01x slower                                                   |
| json_dumps     | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| tomli_loads    | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                            |

Benchmark hidden because not significant (6): xml_etree_process, xml_etree_generate, xml_etree_parse, pickle_pure_python, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| Geometric mean | (ref)                                                        | 1.01x slower                                                            |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy                   | 448 us                                                       | 330 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.8 us                                                      | 37.9 us: 1.34x faster                                                   |
| go                         | 161 ms                                                       | 137 ms: 1.18x faster                                                    |
| async_tree_memoization     | 645 ms                                                       | 553 ms: 1.17x faster                                                    |
| async_tree_none            | 492 ms                                                       | 426 ms: 1.15x faster                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 3.50 us: 1.15x faster                                                   |
| async_tree_none_tg         | 476 ms                                                       | 417 ms: 1.14x faster                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 548 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 726 ms: 1.09x faster                                                    |
| async_tree_io_tg           | 1.27 sec                                                     | 1.17 sec: 1.09x faster                                                  |
| generators                 | 37.1 ms                                                      | 34.7 ms: 1.07x faster                                                   |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.07x faster                                                  |
| gc_traversal               | 5.17 ms                                                      | 4.85 ms: 1.07x faster                                                   |
| pathlib                    | 22.8 ms                                                      | 21.4 ms: 1.06x faster                                                   |
| richards                   | 55.9 ms                                                      | 53.0 ms: 1.05x faster                                                   |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                    |
| richards_super             | 62.3 ms                                                      | 59.4 ms: 1.05x faster                                                   |
| scimark_lu                 | 141 ms                                                       | 135 ms: 1.05x faster                                                    |
| pprint_pformat             | 1.93 sec                                                     | 1.85 sec: 1.04x faster                                                  |
| 2to3                       | 305 ms                                                       | 295 ms: 1.03x faster                                                    |
| thrift                     | 962 us                                                       | 930 us: 1.03x faster                                                    |
| asyncio_tcp                | 584 ms                                                       | 566 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 933 ms                                                       | 904 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                       | 140 ms: 1.03x faster                                                    |
| logging_simple             | 7.21 us                                                      | 7.02 us: 1.03x faster                                                   |
| nbody                      | 114 ms                                                       | 111 ms: 1.03x faster                                                    |
| regex_v8                   | 31.1 ms                                                      | 30.3 ms: 1.03x faster                                                   |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                      | 7.64 us: 1.02x faster                                                   |
| docutils                   | 3.10 sec                                                     | 3.04 sec: 1.02x faster                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 61.4 ms: 1.02x faster                                                   |
| regex_dna                  | 259 ms                                                       | 254 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                                   |
| sympy_str                  | 265 ms                                                       | 261 ms: 1.02x faster                                                    |
| regex_compile              | 128 ms                                                       | 126 ms: 1.02x faster                                                    |
| coroutines                 | 29.0 ms                                                      | 28.5 ms: 1.02x faster                                                   |
| typing_runtime_protocols   | 193 us                                                       | 190 us: 1.02x faster                                                    |
| async_generators           | 488 ms                                                       | 480 ms: 1.02x faster                                                    |
| regex_effbot               | 4.98 ms                                                      | 4.91 ms: 1.01x faster                                                   |
| spectral_norm              | 141 ms                                                       | 140 ms: 1.01x faster                                                    |
| scimark_fft                | 445 ms                                                       | 441 ms: 1.01x faster                                                    |
| mdp                        | 3.33 sec                                                     | 3.31 sec: 1.01x faster                                                  |
| bpe_tokeniser              | 5.83 sec                                                     | 5.86 sec: 1.01x slower                                                  |
| python_startup             | 13.0 ms                                                      | 13.1 ms: 1.01x slower                                                   |
| json_loads                 | 32.1 us                                                      | 32.4 us: 1.01x slower                                                   |
| sqlglot_transpile          | 1.71 ms                                                      | 1.73 ms: 1.01x slower                                                   |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.02x slower                                                   |
| float                      | 91.4 ms                                                      | 93.4 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 8.79 ms: 1.02x slower                                                   |
| raytrace                   | 297 ms                                                       | 304 ms: 1.02x slower                                                    |
| mako                       | 13.2 ms                                                      | 13.5 ms: 1.03x slower                                                   |
| tomli_loads                | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                                  |
| pyflate                    | 557 ms                                                       | 581 ms: 1.04x slower                                                    |
| fannkuch                   | 451 ms                                                       | 475 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                            |

Benchmark hidden because not significant (35): sqlglot_parse, create_gc_cycles, html5lib, scimark_sor, sympy_integrate, scimark_monte_carlo, sqlglot_normalize, xml_etree_process, pycparser, xml_etree_generate, telco, sympy_expand, genshi_xml, coverage, logging_silent, xml_etree_parse, pickle_pure_python, pidigits, xml_etree_iterparse, crypto_pyaes, meteor_contest, asyncio_tcp_ssl, tornado_http, asyncio_websockets, unpickle_pure_python, genshi_text, hexiom, django_template, chaos, nqueens, json, comprehensions, bench_mp_pool, deltablue, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x