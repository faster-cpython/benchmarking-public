# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 6d5be6d
- commit date: 2024-09-03
- overall geometric mean: 1.033x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 296 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| html5lib       | 66.4 ms                                                  | 63.2 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 418 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 724 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 727 ms: 1.05x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.06x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| float          | 93.3 ms                                                  | 92.4 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| regex_compile  | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 197 ms                                                   | 190 ms: 1.03x faster                                                    |
| xml_etree_iterparse | 149 ms                                                   | 147 ms: 1.02x faster                                                    |
| json_loads          | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| tomli_loads         | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_dumps, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 27.7 ms                                                  | 27.5 ms: 1.01x faster                                                   |
| django_template | 41.6 ms                                                  | 42.4 ms: 1.02x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 333 us: 1.34x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.18x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 551 ms: 1.18x faster                                                    |
| async_tree_none            | 497 ms                                                   | 423 ms: 1.17x faster                                                    |
| go                         | 160 ms                                                   | 136 ms: 1.17x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.47 us: 1.17x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 558 ms: 1.17x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 4.99 ms: 1.16x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 418 ms: 1.12x faster                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 6.94 ms: 1.11x faster                                                   |
| generators                 | 37.6 ms                                                  | 34.7 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.2 ms: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 724 ms: 1.06x faster                                                    |
| nbody                      | 114 ms                                                   | 108 ms: 1.06x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 727 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.3 ms: 1.05x faster                                                   |
| html5lib                   | 66.4 ms                                                  | 63.2 ms: 1.05x faster                                                   |
| scimark_lu                 | 139 ms                                                   | 133 ms: 1.05x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.22 sec: 1.04x faster                                                  |
| scimark_monte_carlo        | 83.6 ms                                                  | 80.4 ms: 1.04x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 190 ms: 1.03x faster                                                    |
| meteor_contest             | 114 ms                                                   | 110 ms: 1.03x faster                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.24 ms: 1.03x faster                                                   |
| nqueens                    | 100 ms                                                   | 97.4 ms: 1.03x faster                                                   |
| 2to3                       | 304 ms                                                   | 296 ms: 1.03x faster                                                    |
| sympy_sum                  | 144 ms                                                   | 140 ms: 1.02x faster                                                    |
| scimark_sor                | 160 ms                                                   | 156 ms: 1.02x faster                                                    |
| logging_format             | 7.82 us                                                  | 7.64 us: 1.02x faster                                                   |
| thrift                     | 968 us                                                   | 947 us: 1.02x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 907 ms: 1.02x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 82.1 ms: 1.02x faster                                                   |
| regex_compile              | 127 ms                                                   | 125 ms: 1.02x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 147 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.01x faster                                                  |
| coverage                   | 99.1 ms                                                  | 97.8 ms: 1.01x faster                                                   |
| hexiom                     | 7.11 ms                                                  | 7.02 ms: 1.01x faster                                                   |
| logging_silent             | 133 ns                                                   | 131 ns: 1.01x faster                                                    |
| float                      | 93.3 ms                                                  | 92.4 ms: 1.01x faster                                                   |
| genshi_text                | 27.7 ms                                                  | 27.5 ms: 1.01x faster                                                   |
| mdp                        | 3.34 sec                                                 | 3.32 sec: 1.01x faster                                                  |
| comprehensions             | 20.4 us                                                  | 20.3 us: 1.01x faster                                                   |
| deltablue                  | 3.82 ms                                                  | 3.84 ms: 1.01x slower                                                   |
| django_template            | 41.6 ms                                                  | 42.4 ms: 1.02x slower                                                   |
| pyflate                    | 556 ms                                                   | 575 ms: 1.03x slower                                                    |
| json_loads                 | 31.7 us                                                  | 32.9 us: 1.04x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.05x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (35): scimark_sparse_mat_mult, xml_etree_generate, genshi_xml, xml_etree_process, tornado_http, spectral_norm, sympy_integrate, json_dumps, typing_runtime_protocols, logging_simple, richards, richards_super, sqlglot_optimize, bpe_tokeniser, fannkuch, scimark_fft, mako, sqlglot_transpile, json, regex_dna, raytrace, coroutines, sqlglot_normalize, regex_effbot, pickle_pure_python, sympy_str, sympy_expand, asyncio_websockets, pidigits, chaos, unpickle_pure_python, python_startup_no_site, telco, sqlglot_parse, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240903-3.14.0a0-6d5be6d/bm-20240903-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-6d5be6d.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.033x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x