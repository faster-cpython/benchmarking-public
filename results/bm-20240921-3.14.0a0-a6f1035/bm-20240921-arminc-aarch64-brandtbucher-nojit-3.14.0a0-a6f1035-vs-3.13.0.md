# Results vs. 3.13.0

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.027x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 297 ms: 1.02x faster                                           |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                         |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 417 ms: 1.19x faster                                           |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                           |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                           |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                           |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                           |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 736 ms: 1.04x faster                                           |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                           |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                         |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                   |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.04x faster                                           |
| float          | 93.3 ms                                                  | 94.9 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                    | 1.01x faster                                                   |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                           |
| xml_etree_generate   | 113 ms                                                   | 112 ms: 1.02x faster                                           |
| pickle_pure_python   | 357 us                                                   | 360 us: 1.01x slower                                           |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                           |
| tomli_loads          | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                         |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                   |

Benchmark hidden because not significant (4): json_dumps, xml_etree_process, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                          |
| Geometric mean | (ref)                                                    | 1.09x faster                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                          |
| deepcopy                   | 447 us                                                   | 335 us: 1.33x faster                                           |
| deepcopy_memo              | 50.4 us                                                  | 39.2 us: 1.28x faster                                          |
| async_tree_none            | 497 ms                                                   | 417 ms: 1.19x faster                                           |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                          |
| async_tree_memoization_tg  | 649 ms                                                   | 552 ms: 1.18x faster                                           |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                           |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                           |
| gc_traversal               | 5.77 ms                                                  | 5.04 ms: 1.14x faster                                          |
| deepcopy_reduce            | 4.07 us                                                  | 3.58 us: 1.14x faster                                          |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                           |
| bench_mp_pool              | 7.68 ms                                                  | 7.12 ms: 1.08x faster                                          |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                           |
| pathlib                    | 22.7 ms                                                  | 21.4 ms: 1.06x faster                                          |
| generators                 | 37.6 ms                                                  | 35.4 ms: 1.06x faster                                          |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                           |
| regex_v8                   | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                          |
| thrift                     | 968 us                                                   | 926 us: 1.05x faster                                           |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 736 ms: 1.04x faster                                           |
| nbody                      | 114 ms                                                   | 111 ms: 1.04x faster                                           |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                           |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.03x faster                                         |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.02x faster                                           |
| 2to3                       | 304 ms                                                   | 297 ms: 1.02x faster                                           |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                           |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.0 ms: 1.02x faster                                          |
| pprint_safe_repr           | 926 ms                                                   | 911 ms: 1.02x faster                                           |
| xml_etree_generate         | 113 ms                                                   | 112 ms: 1.02x faster                                           |
| coverage                   | 99.1 ms                                                  | 97.9 ms: 1.01x faster                                          |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                          |
| bench_thread_pool          | 1.27 ms                                                  | 1.26 ms: 1.01x faster                                          |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                         |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                           |
| fannkuch                   | 461 ms                                                   | 465 ms: 1.01x slower                                           |
| pickle_pure_python         | 357 us                                                   | 360 us: 1.01x slower                                           |
| raytrace                   | 300 ms                                                   | 302 ms: 1.01x slower                                           |
| pyflate                    | 556 ms                                                   | 563 ms: 1.01x slower                                           |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                          |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                           |
| float                      | 93.3 ms                                                  | 94.9 ms: 1.02x slower                                          |
| chaos                      | 68.0 ms                                                  | 69.2 ms: 1.02x slower                                          |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.03x slower                                          |
| deltablue                  | 3.82 ms                                                  | 3.94 ms: 1.03x slower                                          |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                         |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                         |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                         |
| tomli_loads                | 2.54 sec                                                 | 2.66 sec: 1.05x slower                                         |
| telco                      | 9.74 ms                                                  | 10.3 ms: 1.06x slower                                          |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                   |

Benchmark hidden because not significant (39): html5lib, json_dumps, richards, crypto_pyaes, logging_format, tornado_http, regex_dna, scimark_sparse_mat_mult, genshi_text, json, xml_etree_process, typing_runtime_protocols, nqueens, sqlglot_normalize, python_startup_no_site, regex_compile, sympy_sum, spectral_norm, xml_etree_iterparse, logging_silent, sqlglot_transpile, mako, bpe_tokeniser, meteor_contest, sqlglot_optimize, pidigits, asyncio_websockets, mdp, logging_simple, django_template, json_loads, regex_effbot, sympy_expand, sympy_integrate, coroutines, hexiom, sympy_str, genshi_xml, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x