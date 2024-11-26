# Results vs. 3.13.0

- fork: mdboom
- ref: marshal_slice
- machine: linux-aarch64
- commit hash: 0e19ac7
- commit date: 2024-10-07
- overall geometric mean: 1.030x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 296 ms: 1.03x faster                                             |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                           |
| html5lib       | 66.4 ms                                                  | 63.1 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                             |
| async_tree_none            | 497 ms                                                   | 429 ms: 1.16x faster                                             |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 705 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 714 ms: 1.07x faster                                             |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                             |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                           |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| float          | 93.3 ms                                                  | 94.4 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.8 ms: 1.03x faster                                            |
| regex_compile  | 127 ms                                                   | 125 ms: 1.01x faster                                             |
| regex_effbot   | 4.89 ms                                                  | 4.99 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                    | 1.01x faster                                                     |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| json_loads           | 31.7 us                                                  | 31.1 us: 1.02x faster                                            |
| unpickle_pure_python | 251 us                                                   | 255 us: 1.02x slower                                             |
| pickle_pure_python   | 357 us                                                   | 366 us: 1.03x slower                                             |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                           |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                     |

Benchmark hidden because not significant (5): json_dumps, xml_etree_parse, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                            |
| Geometric mean | (ref)                                                    | 1.09x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                            |
| django_template | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                     |

Benchmark hidden because not significant (2): mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.35 ms: 1.42x faster                                            |
| deepcopy                   | 447 us                                                   | 331 us: 1.35x faster                                             |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                            |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                            |
| deepcopy_reduce            | 4.07 us                                                  | 3.45 us: 1.18x faster                                            |
| async_tree_memoization_tg  | 649 ms                                                   | 550 ms: 1.18x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                             |
| async_tree_none            | 497 ms                                                   | 429 ms: 1.16x faster                                             |
| go                         | 160 ms                                                   | 138 ms: 1.16x faster                                             |
| gc_traversal               | 5.77 ms                                                  | 5.07 ms: 1.14x faster                                            |
| async_tree_none_tg         | 470 ms                                                   | 421 ms: 1.11x faster                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 705 ms: 1.09x faster                                             |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 714 ms: 1.07x faster                                             |
| generators                 | 37.6 ms                                                  | 35.2 ms: 1.07x faster                                            |
| scimark_lu                 | 139 ms                                                   | 132 ms: 1.06x faster                                             |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.05x faster                                            |
| telco                      | 9.74 ms                                                  | 9.25 ms: 1.05x faster                                            |
| html5lib                   | 66.4 ms                                                  | 63.1 ms: 1.05x faster                                            |
| scimark_fft                | 447 ms                                                   | 426 ms: 1.05x faster                                             |
| json                       | 5.73 ms                                                  | 5.50 ms: 1.04x faster                                            |
| nbody                      | 114 ms                                                   | 110 ms: 1.04x faster                                             |
| regex_v8                   | 31.8 ms                                                  | 30.8 ms: 1.03x faster                                            |
| async_generators           | 489 ms                                                   | 475 ms: 1.03x faster                                             |
| pycparser                  | 1.27 sec                                                 | 1.24 sec: 1.03x faster                                           |
| bpe_tokeniser              | 5.87 sec                                                 | 5.72 sec: 1.03x faster                                           |
| 2to3                       | 304 ms                                                   | 296 ms: 1.03x faster                                             |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.03x faster                                             |
| meteor_contest             | 114 ms                                                   | 111 ms: 1.02x faster                                             |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.02x faster                                             |
| crypto_pyaes               | 83.7 ms                                                  | 82.0 ms: 1.02x faster                                            |
| pprint_pformat             | 1.90 sec                                                 | 1.86 sec: 1.02x faster                                           |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.39 ms: 1.02x faster                                            |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                             |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                            |
| richards                   | 53.6 ms                                                  | 52.7 ms: 1.02x faster                                            |
| json_loads                 | 31.7 us                                                  | 31.1 us: 1.02x faster                                            |
| nqueens                    | 100 ms                                                   | 98.5 ms: 1.02x faster                                            |
| regex_compile              | 127 ms                                                   | 125 ms: 1.01x faster                                             |
| django_template            | 41.6 ms                                                  | 42.1 ms: 1.01x slower                                            |
| float                      | 93.3 ms                                                  | 94.4 ms: 1.01x slower                                            |
| sympy_integrate            | 20.8 ms                                                  | 21.1 ms: 1.01x slower                                            |
| raytrace                   | 300 ms                                                   | 304 ms: 1.02x slower                                             |
| unpickle_pure_python       | 251 us                                                   | 255 us: 1.02x slower                                             |
| regex_effbot               | 4.89 ms                                                  | 4.99 ms: 1.02x slower                                            |
| fannkuch                   | 461 ms                                                   | 471 ms: 1.02x slower                                             |
| chaos                      | 68.0 ms                                                  | 69.7 ms: 1.03x slower                                            |
| pickle_pure_python         | 357 us                                                   | 366 us: 1.03x slower                                             |
| deltablue                  | 3.82 ms                                                  | 3.93 ms: 1.03x slower                                            |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                           |
| sqlglot_parse              | 1.38 ms                                                  | 1.43 ms: 1.04x slower                                            |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                           |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                           |
| pyflate                    | 556 ms                                                   | 583 ms: 1.05x slower                                             |
| async_tree_io              | 1.11 sec                                                 | 1.17 sec: 1.06x slower                                           |
| bench_mp_pool              | 7.68 ms                                                  | 5.20 sec: 677.12x slower                                         |
| Geometric mean             | (ref)                                                    | 1.05x slower                                                     |

Benchmark hidden because not significant (32): json_dumps, xml_etree_parse, tornado_http, scimark_monte_carlo, hexiom, logging_silent, spectral_norm, richards_super, thrift, xml_etree_generate, python_startup_no_site, xml_etree_process, sqlglot_optimize, logging_format, coverage, mako, bench_thread_pool, asyncio_websockets, mdp, genshi_xml, sqlglot_normalize, pidigits, regex_dna, sympy_str, comprehensions, logging_simple, sympy_expand, typing_runtime_protocols, sqlglot_transpile, coroutines, xml_etree_iterparse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241007-3.14.0a0-0e19ac7/bm-20241007-arminc-aarch64-mdboom-marshal_slice-3.14.0a0-0e19ac7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.030x faster
# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x