# Results vs. 3.13.0

- fork: python
- ref: v3.14.0a1
- machine: linux-aarch64
- commit hash: 8cdaca8
- commit date: 2024-10-15
- overall geometric mean: 1.020x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 293 ms: 1.04x faster                                         |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                       |
| Geometric mean | (ref)                                                    | 1.01x faster                                                 |

Benchmark hidden because not significant (3): html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                         |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.15x faster                                         |
| async_tree_none            | 497 ms                                                   | 438 ms: 1.13x faster                                         |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 724 ms: 1.06x faster                                         |
| async_tree_none_tg         | 470 ms                                                   | 447 ms: 1.05x faster                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                         |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.21 sec: 1.07x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                       |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 95.4 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 243 ms: 1.04x faster                                         |
| regex_v8       | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                        |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                    | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 191 ms: 1.03x faster                                         |
| json_loads           | 31.7 us                                                  | 31.2 us: 1.02x faster                                        |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                         |
| pickle_pure_python   | 357 us                                                   | 365 us: 1.02x slower                                         |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                       |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_iterparse, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                        |
| Geometric mean | (ref)                                                    | 1.04x faster                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                        |
| mako            | 13.4 ms                                                  | 13.7 ms: 1.02x slower                                        |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8 |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy                   | 447 us                                                   | 333 us: 1.34x faster                                         |
| deepcopy_memo              | 50.4 us                                                  | 38.2 us: 1.32x faster                                        |
| async_tree_memoization_tg  | 649 ms                                                   | 538 ms: 1.21x faster                                         |
| go                         | 160 ms                                                   | 136 ms: 1.18x faster                                         |
| async_tree_memoization     | 651 ms                                                   | 563 ms: 1.15x faster                                         |
| deepcopy_reduce            | 4.07 us                                                  | 3.56 us: 1.14x faster                                        |
| async_tree_none            | 497 ms                                                   | 438 ms: 1.13x faster                                         |
| generators                 | 37.6 ms                                                  | 34.8 ms: 1.08x faster                                        |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                        |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 724 ms: 1.06x faster                                         |
| python_startup             | 15.4 ms                                                  | 14.5 ms: 1.06x faster                                        |
| async_tree_none_tg         | 470 ms                                                   | 447 ms: 1.05x faster                                         |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                       |
| json                       | 5.73 ms                                                  | 5.46 ms: 1.05x faster                                        |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                         |
| thrift                     | 968 us                                                   | 929 us: 1.04x faster                                         |
| logging_format             | 7.82 us                                                  | 7.51 us: 1.04x faster                                        |
| regex_dna                  | 253 ms                                                   | 243 ms: 1.04x faster                                         |
| sympy_sum                  | 144 ms                                                   | 138 ms: 1.04x faster                                         |
| logging_simple             | 7.07 us                                                  | 6.82 us: 1.04x faster                                        |
| 2to3                       | 304 ms                                                   | 293 ms: 1.04x faster                                         |
| crypto_pyaes               | 83.7 ms                                                  | 80.9 ms: 1.03x faster                                        |
| scimark_fft                | 447 ms                                                   | 433 ms: 1.03x faster                                         |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 743 ms: 1.03x faster                                         |
| xml_etree_parse            | 197 ms                                                   | 191 ms: 1.03x faster                                         |
| meteor_contest             | 114 ms                                                   | 110 ms: 1.03x faster                                         |
| regex_v8                   | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                        |
| telco                      | 9.74 ms                                                  | 9.54 ms: 1.02x faster                                        |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                         |
| hexiom                     | 7.11 ms                                                  | 6.97 ms: 1.02x faster                                        |
| pprint_safe_repr           | 926 ms                                                   | 909 ms: 1.02x faster                                         |
| bpe_tokeniser              | 5.87 sec                                                 | 5.76 sec: 1.02x faster                                       |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                         |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                         |
| coverage                   | 99.1 ms                                                  | 97.6 ms: 1.02x faster                                        |
| json_loads                 | 31.7 us                                                  | 31.2 us: 1.02x faster                                        |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                       |
| sympy_str                  | 264 ms                                                   | 261 ms: 1.01x faster                                         |
| sqlglot_normalize          | 127 ms                                                   | 126 ms: 1.00x faster                                         |
| django_template            | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                        |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                        |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                         |
| fannkuch                   | 461 ms                                                   | 469 ms: 1.02x slower                                         |
| chaos                      | 68.0 ms                                                  | 69.3 ms: 1.02x slower                                        |
| mako                       | 13.4 ms                                                  | 13.7 ms: 1.02x slower                                        |
| bench_thread_pool          | 1.27 ms                                                  | 1.30 ms: 1.02x slower                                        |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                        |
| float                      | 93.3 ms                                                  | 95.4 ms: 1.02x slower                                        |
| pickle_pure_python         | 357 us                                                   | 365 us: 1.02x slower                                         |
| deltablue                  | 3.82 ms                                                  | 3.95 ms: 1.03x slower                                        |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.04x slower                                       |
| raytrace                   | 300 ms                                                   | 311 ms: 1.04x slower                                         |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                       |
| pyflate                    | 556 ms                                                   | 585 ms: 1.05x slower                                         |
| async_tree_io_tg           | 1.13 sec                                                 | 1.21 sec: 1.07x slower                                       |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                       |
| gc_traversal               | 5.77 ms                                                  | 6.25 ms: 1.08x slower                                        |
| create_gc_cycles           | 3.35 ms                                                  | 3.67 ms: 1.10x slower                                        |
| bench_mp_pool              | 7.68 ms                                                  | 4.94 sec: 643.07x slower                                     |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                 |

Benchmark hidden because not significant (29): html5lib, tornado_http, nqueens, python_startup_no_site, nbody, genshi_text, scimark_sparse_mat_mult, sqlglot_optimize, spectral_norm, logging_silent, richards, richards_super, regex_effbot, asyncio_websockets, sympy_expand, xml_etree_process, scimark_monte_carlo, xml_etree_iterparse, typing_runtime_protocols, pidigits, mdp, sympy_integrate, xml_etree_generate, sphinx, coroutines, sqlglot_transpile, genshi_xml, pylint, json_dumps
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241015-3.14.0a1-8cdaca8/bm-20241015-arminc-aarch64-python-v3.14.0a1-3.14.0a1-8cdaca8.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x