# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 426 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 417 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| json_loads          | 31.7 us                                                  | 32.4 us: 1.02x slower                                                   |
| tomli_loads         | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (6): xml_etree_parse, json_dumps, xml_etree_generate, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| django_template | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 330 us: 1.35x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.85 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 548 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                    |
| go                         | 160 ms                                                   | 137 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 426 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 417 ms: 1.13x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 7.09 ms: 1.08x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.4 ms: 1.06x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 725 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 726 ms: 1.06x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| pycparser                  | 1.27 sec                                                 | 1.21 sec: 1.05x faster                                                  |
| thrift                     | 968 us                                                   | 930 us: 1.04x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 904 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.6 ms: 1.02x faster                                                   |
| logging_format             | 7.82 us                                                  | 7.64 us: 1.02x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.85 sec: 1.02x faster                                                  |
| crypto_pyaes               | 83.7 ms                                                  | 81.9 ms: 1.02x faster                                                   |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.39 ms: 1.02x faster                                                   |
| async_generators           | 489 ms                                                   | 480 ms: 1.02x faster                                                    |
| typing_runtime_protocols   | 193 us                                                   | 190 us: 1.02x faster                                                    |
| scimark_fft                | 447 ms                                                   | 441 ms: 1.01x faster                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 61.4 ms: 1.01x faster                                                   |
| sympy_str                  | 264 ms                                                   | 261 ms: 1.01x faster                                                    |
| richards_super             | 60.1 ms                                                  | 59.4 ms: 1.01x faster                                                   |
| mdp                        | 3.34 sec                                                 | 3.31 sec: 1.01x faster                                                  |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| raytrace                   | 300 ms                                                   | 304 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.7 us: 1.01x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| telco                      | 9.74 ms                                                  | 9.97 ms: 1.02x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 3.91 ms: 1.02x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.4 us: 1.02x slower                                                   |
| fannkuch                   | 461 ms                                                   | 475 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 581 ms: 1.04x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.04 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (35): xml_etree_parse, html5lib, json_dumps, scimark_sor, richards, coverage, regex_compile, sympy_integrate, genshi_text, json, logging_simple, nqueens, xml_etree_generate, xml_etree_process, genshi_xml, sympy_expand, asyncio_websockets, sqlglot_transpile, bpe_tokeniser, meteor_contest, hexiom, float, tornado_http, coroutines, pidigits, logging_silent, regex_dna, pickle_pure_python, unpickle_pure_python, regex_effbot, python_startup_no_site, chaos, sqlglot_parse, sqlglot_normalize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x