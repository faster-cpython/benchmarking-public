# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 15b187e
- commit date: 2024-08-29
- overall geometric mean: 1.031x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 292 ms: 1.04x faster                                                    |
| docutils       | 2.89 sec                                                 | 2.98 sec: 1.03x slower                                                  |
| html5lib       | 66.4 ms                                                  | 63.5 ms: 1.05x faster                                                   |
| tornado_http   | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 556 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 412 ms: 1.14x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 724 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                                   |
| regex_dna      | 253 ms                                                   | 246 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| unpickle_pure_python | 251 us                                                   | 254 us: 1.01x slower                                                    |
| json_loads           | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, xml_etree_generate, json_dumps, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| django_template | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x slower                                                            |

Benchmark hidden because not significant (3): genshi_text, genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 337 us: 1.33x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.0 us: 1.33x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 545 ms: 1.19x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 556 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.49 us: 1.17x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.97 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 412 ms: 1.14x faster                                                    |
| go                         | 160 ms                                                   | 140 ms: 1.14x faster                                                    |
| generators                 | 37.6 ms                                                  | 34.6 ms: 1.09x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.1 ms: 1.07x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.15 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 721 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 724 ms: 1.06x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.05x faster                                                  |
| regex_v8                   | 31.8 ms                                                  | 30.4 ms: 1.05x faster                                                   |
| html5lib                   | 66.4 ms                                                  | 63.5 ms: 1.05x faster                                                   |
| thrift                     | 968 us                                                   | 926 us: 1.05x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| 2to3                       | 304 ms                                                   | 292 ms: 1.04x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| regex_dna                  | 253 ms                                                   | 246 ms: 1.03x faster                                                    |
| tornado_http               | 128 ms                                                   | 124 ms: 1.03x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 81.5 ms: 1.03x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 136 ms: 1.03x faster                                                    |
| nbody                      | 114 ms                                                   | 112 ms: 1.02x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 910 ms: 1.02x faster                                                    |
| richards                   | 53.6 ms                                                  | 52.7 ms: 1.02x faster                                                   |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                                  |
| richards_super             | 60.1 ms                                                  | 59.2 ms: 1.01x faster                                                   |
| sympy_sum                  | 144 ms                                                   | 142 ms: 1.01x faster                                                    |
| meteor_contest             | 114 ms                                                   | 112 ms: 1.01x faster                                                    |
| mdp                        | 3.34 sec                                                 | 3.37 sec: 1.01x slower                                                  |
| pyflate                    | 556 ms                                                   | 562 ms: 1.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 196 us: 1.01x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 254 us: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 303 ms: 1.01x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.88 ms: 1.01x slower                                                   |
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.5 ms: 1.02x slower                                                   |
| telco                      | 9.74 ms                                                  | 9.94 ms: 1.02x slower                                                   |
| docutils                   | 2.89 sec                                                 | 2.98 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.16 sec: 1.03x slower                                                  |
| json_loads                 | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (36): xml_etree_process, scimark_sparse_mat_mult, spectral_norm, crypto_pyaes, sqlglot_transpile, logging_format, logging_simple, scimark_sor, genshi_text, regex_effbot, coverage, genshi_xml, scimark_fft, float, sympy_str, regex_compile, nqueens, xml_etree_generate, sympy_integrate, python_startup_no_site, sympy_expand, sqlglot_optimize, pidigits, json_dumps, logging_silent, mako, pickle_pure_python, bpe_tokeniser, asyncio_websockets, json, fannkuch, chaos, hexiom, sqlglot_parse, sqlglot_normalize, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240829-3.14.0a0-15b187e/bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-15b187e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x