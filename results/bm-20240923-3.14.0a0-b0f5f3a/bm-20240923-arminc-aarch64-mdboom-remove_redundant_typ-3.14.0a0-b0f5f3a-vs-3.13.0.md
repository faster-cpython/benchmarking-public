# Results vs. 3.13.0

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.031x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.90x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| tornado_http   | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none            | 497 ms                                                   | 419 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 723 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 483 ms: 1.01x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| pickle_pure_python   | 357 us                                                   | 361 us: 1.01x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 256 us: 1.02x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (5): json_dumps, xml_etree_process, xml_etree_generate, xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                   |
| mako           | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (2): django_template, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                   |
| deepcopy                   | 447 us                                                   | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.0 us: 1.33x faster                                                   |
| async_tree_none            | 497 ms                                                   | 419 ms: 1.19x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 549 ms: 1.18x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 553 ms: 1.18x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.50 us: 1.16x faster                                                   |
| go                         | 160 ms                                                   | 138 ms: 1.15x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.09 ms: 1.13x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 416 ms: 1.13x faster                                                    |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.12 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 718 ms: 1.07x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 723 ms: 1.06x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 186 ms: 1.06x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                                  |
| regex_v8                   | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| thrift                     | 968 us                                                   | 932 us: 1.04x faster                                                    |
| tornado_http               | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 139 ms: 1.03x faster                                                    |
| 2to3                       | 304 ms                                                   | 295 ms: 1.03x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 81.4 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.65 us: 1.02x faster                                                   |
| spectral_norm              | 143 ms                                                   | 140 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.2 ms: 1.02x faster                                                   |
| richards_super             | 60.1 ms                                                  | 59.1 ms: 1.02x faster                                                   |
| richards                   | 53.6 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 914 ms: 1.01x faster                                                    |
| async_generators           | 489 ms                                                   | 483 ms: 1.01x faster                                                    |
| mdp                        | 3.34 sec                                                 | 3.31 sec: 1.01x faster                                                  |
| logging_silent             | 133 ns                                                   | 132 ns: 1.01x faster                                                    |
| meteor_contest             | 114 ms                                                   | 113 ms: 1.01x faster                                                    |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.88 sec: 1.01x faster                                                  |
| mako                       | 13.4 ms                                                  | 13.3 ms: 1.01x faster                                                   |
| raytrace                   | 300 ms                                                   | 302 ms: 1.01x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 361 us: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| chaos                      | 68.0 ms                                                  | 68.9 ms: 1.01x slower                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.96 ms: 1.01x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 256 us: 1.02x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.93 ms: 1.03x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 580 ms: 1.04x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.03 sec: 1.05x slower                                                  |
| telco                      | 9.74 ms                                                  | 10.3 ms: 1.05x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (32): json_dumps, xml_etree_process, html5lib, sympy_integrate, xml_etree_generate, logging_simple, regex_compile, sympy_str, regex_dna, xml_etree_iterparse, python_startup_no_site, fannkuch, bpe_tokeniser, scimark_monte_carlo, hexiom, float, json_loads, coverage, coroutines, pidigits, scimark_sparse_mat_mult, asyncio_websockets, sqlglot_optimize, sympy_expand, django_template, typing_runtime_protocols, sqlglot_transpile, nqueens, sqlglot_parse, sqlglot_normalize, genshi_xml, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.90x