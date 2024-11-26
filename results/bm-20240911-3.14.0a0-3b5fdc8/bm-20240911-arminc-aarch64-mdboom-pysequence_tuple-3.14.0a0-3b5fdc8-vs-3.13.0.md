# Results vs. 3.13.0

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.029x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 297 ms: 1.02x faster                                                |
| docutils       | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                              |
| Geometric mean | (ref)                                                    | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                |
| async_tree_none            | 497 ms                                                   | 427 ms: 1.16x faster                                                |
| async_tree_memoization     | 651 ms                                                   | 562 ms: 1.16x faster                                                |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 734 ms: 1.04x faster                                                |
| async_generators           | 489 ms                                                   | 482 ms: 1.02x faster                                                |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                              |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                              |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                        |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                |
| float          | 93.3 ms                                                  | 94.2 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                    | 1.01x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                               |
| regex_compile  | 127 ms                                                   | 124 ms: 1.02x faster                                                |
| regex_effbot   | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                    | 1.01x faster                                                        |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_loads         | 31.7 us                                                  | 31.4 us: 1.01x faster                                               |
| tomli_loads        | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                              |
| pickle_pure_python | 357 us                                                   | 368 us: 1.03x slower                                                |
| Geometric mean     | (ref)                                                    | 1.00x faster                                                        |

Benchmark hidden because not significant (6): xml_etree_parse, json_dumps, xml_etree_process, xml_etree_generate, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                               |
| Geometric mean | (ref)                                                    | 1.09x faster                                                        |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                        |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.37 ms: 1.41x faster                                               |
| deepcopy_memo              | 50.4 us                                                  | 37.3 us: 1.35x faster                                               |
| deepcopy                   | 447 us                                                   | 337 us: 1.33x faster                                                |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                               |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                                |
| go                         | 160 ms                                                   | 137 ms: 1.16x faster                                                |
| async_tree_none            | 497 ms                                                   | 427 ms: 1.16x faster                                                |
| async_tree_memoization     | 651 ms                                                   | 562 ms: 1.16x faster                                                |
| deepcopy_reduce            | 4.07 us                                                  | 3.57 us: 1.14x faster                                               |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                |
| gc_traversal               | 5.77 ms                                                  | 5.13 ms: 1.13x faster                                               |
| pathlib                    | 22.7 ms                                                  | 20.9 ms: 1.09x faster                                               |
| bench_mp_pool              | 7.68 ms                                                  | 7.11 ms: 1.08x faster                                               |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                               |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                              |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 734 ms: 1.04x faster                                                |
| scimark_lu                 | 139 ms                                                   | 134 ms: 1.04x faster                                                |
| regex_v8                   | 31.8 ms                                                  | 30.7 ms: 1.04x faster                                               |
| scimark_monte_carlo        | 83.6 ms                                                  | 80.7 ms: 1.04x faster                                               |
| json                       | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                               |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                               |
| thrift                     | 968 us                                                   | 943 us: 1.03x faster                                                |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.03x faster                                                |
| regex_compile              | 127 ms                                                   | 124 ms: 1.02x faster                                                |
| coverage                   | 99.1 ms                                                  | 97.0 ms: 1.02x faster                                               |
| 2to3                       | 304 ms                                                   | 297 ms: 1.02x faster                                                |
| richards                   | 53.6 ms                                                  | 52.7 ms: 1.02x faster                                               |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.02x faster                                                |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                |
| sympy_integrate            | 20.8 ms                                                  | 20.5 ms: 1.02x faster                                               |
| async_generators           | 489 ms                                                   | 482 ms: 1.02x faster                                                |
| richards_super             | 60.1 ms                                                  | 59.5 ms: 1.01x faster                                               |
| bpe_tokeniser              | 5.87 sec                                                 | 5.83 sec: 1.01x faster                                              |
| json_loads                 | 31.7 us                                                  | 31.4 us: 1.01x faster                                               |
| pprint_pformat             | 1.90 sec                                                 | 1.91 sec: 1.01x slower                                              |
| float                      | 93.3 ms                                                  | 94.2 ms: 1.01x slower                                               |
| deltablue                  | 3.82 ms                                                  | 3.89 ms: 1.02x slower                                               |
| fannkuch                   | 461 ms                                                   | 471 ms: 1.02x slower                                                |
| django_template            | 41.6 ms                                                  | 42.6 ms: 1.02x slower                                               |
| regex_effbot               | 4.89 ms                                                  | 5.01 ms: 1.02x slower                                               |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.03x slower                                               |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                              |
| tomli_loads                | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                              |
| pickle_pure_python         | 357 us                                                   | 368 us: 1.03x slower                                                |
| pyflate                    | 556 ms                                                   | 579 ms: 1.04x slower                                                |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                              |
| docutils                   | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                              |
| telco                      | 9.74 ms                                                  | 10.3 ms: 1.05x slower                                               |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                        |

Benchmark hidden because not significant (37): xml_etree_parse, json_dumps, scimark_sparse_mat_mult, xml_etree_process, tornado_http, spectral_norm, sympy_sum, html5lib, logging_format, logging_silent, crypto_pyaes, python_startup_no_site, xml_etree_generate, hexiom, pprint_safe_repr, comprehensions, coroutines, mdp, genshi_text, mako, sympy_str, asyncio_websockets, genshi_xml, typing_runtime_protocols, pidigits, regex_dna, chaos, sqlglot_transpile, raytrace, unpickle_pure_python, sympy_expand, sqlglot_optimize, logging_simple, nqueens, xml_etree_iterparse, sqlglot_normalize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.029x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x