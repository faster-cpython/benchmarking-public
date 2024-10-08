# Results vs. 3.13.0b2

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.02x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 297 ms: 1.03x faster                                                |
| docutils       | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                              |
| Geometric mean | (ref)                                                        | 1.02x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none            | 492 ms                                                       | 427 ms: 1.15x faster                                                |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                              |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 114 ms                                                       | 109 ms: 1.05x faster                                                |
| float          | 91.4 ms                                                      | 94.2 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 128 ms                                                       | 124 ms: 1.03x faster                                                |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (2): regex_v8, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle           | 19.8 us                                                      | 19.3 us: 1.02x faster                                               |
| json_loads         | 32.1 us                                                      | 31.4 us: 1.02x faster                                               |
| unpickle_list      | 6.52 us                                                      | 6.38 us: 1.02x faster                                               |
| xml_etree_process  | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                               |
| pickle_list        | 5.27 us                                                      | 5.19 us: 1.02x faster                                               |
| json_dumps         | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                               |
| tomli_loads        | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                              |
| pickle             | 13.4 us                                                      | 13.7 us: 1.02x slower                                               |
| pickle_pure_python | 359 us                                                       | 368 us: 1.03x slower                                                |
| Geometric mean     | (ref)                                                        | 1.00x slower                                                        |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_parse, unpickle_pure_python, pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako           | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                        |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------:|
| deepcopy_memo              | 50.8 us                                                      | 37.3 us: 1.36x faster                                               |
| deepcopy                   | 448 us                                                       | 337 us: 1.33x faster                                                |
| go                         | 161 ms                                                       | 137 ms: 1.17x faster                                                |
| async_tree_none            | 492 ms                                                       | 427 ms: 1.15x faster                                                |
| async_tree_memoization     | 645 ms                                                       | 562 ms: 1.15x faster                                                |
| async_tree_none_tg         | 476 ms                                                       | 416 ms: 1.14x faster                                                |
| deepcopy_reduce            | 4.04 us                                                      | 3.57 us: 1.13x faster                                               |
| async_tree_memoization_tg  | 604 ms                                                       | 550 ms: 1.10x faster                                                |
| pathlib                    | 22.8 ms                                                      | 20.9 ms: 1.09x faster                                               |
| async_tree_io_tg           | 1.27 sec                                                     | 1.18 sec: 1.08x faster                                              |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 734 ms: 1.08x faster                                                |
| async_tree_io              | 1.22 sec                                                     | 1.14 sec: 1.08x faster                                              |
| generators                 | 37.1 ms                                                      | 34.8 ms: 1.07x faster                                               |
| richards                   | 55.9 ms                                                      | 52.7 ms: 1.06x faster                                               |
| scimark_lu                 | 141 ms                                                       | 134 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 725 ms: 1.05x faster                                                |
| nbody                      | 114 ms                                                       | 109 ms: 1.05x faster                                                |
| richards_super             | 62.3 ms                                                      | 59.5 ms: 1.05x faster                                               |
| asyncio_tcp                | 584 ms                                                       | 566 ms: 1.03x faster                                                |
| regex_compile              | 128 ms                                                       | 124 ms: 1.03x faster                                                |
| 2to3                       | 305 ms                                                       | 297 ms: 1.03x faster                                                |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 6.39 ms: 1.02x faster                                               |
| scimark_sor                | 159 ms                                                       | 156 ms: 1.02x faster                                                |
| docutils                   | 3.10 sec                                                     | 3.03 sec: 1.02x faster                                              |
| unpickle                   | 19.8 us                                                      | 19.3 us: 1.02x faster                                               |
| json_loads                 | 32.1 us                                                      | 31.4 us: 1.02x faster                                               |
| unpickle_list              | 6.52 us                                                      | 6.38 us: 1.02x faster                                               |
| xml_etree_process          | 80.8 ms                                                      | 79.1 ms: 1.02x faster                                               |
| sqlite_synth               | 3.90 us                                                      | 3.82 us: 1.02x faster                                               |
| coroutines                 | 29.0 ms                                                      | 28.4 ms: 1.02x faster                                               |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                |
| scimark_monte_carlo        | 82.3 ms                                                      | 80.7 ms: 1.02x faster                                               |
| thrift                     | 962 us                                                       | 943 us: 1.02x faster                                                |
| json                       | 5.64 ms                                                      | 5.54 ms: 1.02x faster                                               |
| bench_thread_pool          | 1.26 ms                                                      | 1.24 ms: 1.02x faster                                               |
| sympy_integrate            | 20.9 ms                                                      | 20.5 ms: 1.02x faster                                               |
| meteor_contest             | 113 ms                                                       | 112 ms: 1.02x faster                                                |
| pickle_list                | 5.27 us                                                      | 5.19 us: 1.02x faster                                               |
| coverage                   | 98.4 ms                                                      | 97.0 ms: 1.01x faster                                               |
| logging_format             | 7.82 us                                                      | 7.72 us: 1.01x faster                                               |
| scimark_fft                | 445 ms                                                       | 440 ms: 1.01x faster                                                |
| pprint_pformat             | 1.93 sec                                                     | 1.91 sec: 1.01x faster                                              |
| pprint_safe_repr           | 933 ms                                                       | 923 ms: 1.01x faster                                                |
| python_startup             | 13.0 ms                                                      | 13.0 ms: 1.00x slower                                               |
| crypto_pyaes               | 82.0 ms                                                      | 82.9 ms: 1.01x slower                                               |
| bench_mp_pool              | 7.03 ms                                                      | 7.11 ms: 1.01x slower                                               |
| json_dumps                 | 13.1 ms                                                      | 13.3 ms: 1.01x slower                                               |
| mako                       | 13.2 ms                                                      | 13.3 ms: 1.01x slower                                               |
| sqlglot_transpile          | 1.71 ms                                                      | 1.74 ms: 1.02x slower                                               |
| raytrace                   | 297 ms                                                       | 301 ms: 1.02x slower                                                |
| tomli_loads                | 2.57 sec                                                     | 2.61 sec: 1.02x slower                                              |
| nqueens                    | 98.9 ms                                                      | 101 ms: 1.02x slower                                                |
| pickle                     | 13.4 us                                                      | 13.7 us: 1.02x slower                                               |
| telco                      | 10.0 ms                                                      | 10.3 ms: 1.02x slower                                               |
| pickle_pure_python         | 359 us                                                       | 368 us: 1.03x slower                                                |
| float                      | 91.4 ms                                                      | 94.2 ms: 1.03x slower                                               |
| pyflate                    | 557 ms                                                       | 579 ms: 1.04x slower                                                |
| fannkuch                   | 451 ms                                                       | 471 ms: 1.04x slower                                                |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                        |

Benchmark hidden because not significant (38): logging_silent, tornado_http, sympy_sum, async_generators, regex_v8, comprehensions, xml_etree_generate, html5lib, gc_traversal, logging_simple, sqlglot_parse, pycparser, sympy_str, spectral_norm, hexiom, dulwich_log, chaos, xml_etree_parse, pidigits, sqlglot_normalize, typing_runtime_protocols, bpe_tokeniser, genshi_xml, mdp, asyncio_tcp_ssl, asyncio_websockets, deltablue, unpickle_pure_python, sqlglot_optimize, regex_effbot, pickle_dict, python_startup_no_site, sympy_expand, django_template, genshi_text, create_gc_cycles, xml_etree_iterparse, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: unpack_sequence

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x