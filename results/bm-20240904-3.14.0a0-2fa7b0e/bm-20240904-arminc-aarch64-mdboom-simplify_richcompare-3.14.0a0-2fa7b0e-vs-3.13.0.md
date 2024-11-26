# Results vs. 3.13.0

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: 2fa7b0e
- commit date: 2024-09-04
- overall geometric mean: 1.028x faster
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| docutils       | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 568 ms: 1.14x faster                                                    |
| async_tree_none            | 497 ms                                                   | 437 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 739 ms: 1.04x faster                                                    |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.05x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| float          | 93.3 ms                                                  | 92.6 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (3): regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|---------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse     | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| xml_etree_iterparse | 149 ms                                                   | 146 ms: 1.03x faster                                                    |
| xml_etree_generate  | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| json_loads          | 31.7 us                                                  | 32.7 us: 1.03x slower                                                   |
| tomli_loads         | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                  |
| Geometric mean      | (ref)                                                    | 1.00x faster                                                            |

Benchmark hidden because not significant (4): json_dumps, xml_etree_process, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text    | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| mako           | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.30 ms: 1.46x faster                                                   |
| deepcopy                   | 447 us                                                   | 329 us: 1.36x faster                                                    |
| deepcopy_memo              | 50.4 us                                                  | 38.4 us: 1.31x faster                                                   |
| go                         | 160 ms                                                   | 136 ms: 1.17x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 553 ms: 1.17x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.48 us: 1.17x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.99 ms: 1.16x faster                                                   |
| async_tree_memoization     | 651 ms                                                   | 568 ms: 1.14x faster                                                    |
| async_tree_none            | 497 ms                                                   | 437 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 419 ms: 1.12x faster                                                    |
| generators                 | 37.6 ms                                                  | 34.6 ms: 1.09x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.09 ms: 1.08x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 20.9 ms: 1.08x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                    |
| nbody                      | 114 ms                                                   | 109 ms: 1.05x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 30.5 ms: 1.04x faster                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.23 ms: 1.04x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 739 ms: 1.04x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 189 ms: 1.04x faster                                                    |
| pycparser                  | 1.27 sec                                                 | 1.23 sec: 1.03x faster                                                  |
| 2to3                       | 304 ms                                                   | 294 ms: 1.03x faster                                                    |
| scimark_lu                 | 139 ms                                                   | 135 ms: 1.03x faster                                                    |
| thrift                     | 968 us                                                   | 939 us: 1.03x faster                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 146 ms: 1.03x faster                                                    |
| pprint_safe_repr           | 926 ms                                                   | 905 ms: 1.02x faster                                                    |
| genshi_text                | 27.7 ms                                                  | 27.1 ms: 1.02x faster                                                   |
| async_generators           | 489 ms                                                   | 479 ms: 1.02x faster                                                    |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| pprint_pformat             | 1.90 sec                                                 | 1.87 sec: 1.02x faster                                                  |
| scimark_fft                | 447 ms                                                   | 440 ms: 1.02x faster                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 82.2 ms: 1.02x faster                                                   |
| richards_super             | 60.1 ms                                                  | 59.2 ms: 1.02x faster                                                   |
| scimark_sor                | 160 ms                                                   | 157 ms: 1.01x faster                                                    |
| float                      | 93.3 ms                                                  | 92.6 ms: 1.01x faster                                                   |
| coroutines                 | 28.5 ms                                                  | 28.3 ms: 1.01x faster                                                   |
| mdp                        | 3.34 sec                                                 | 3.35 sec: 1.00x slower                                                  |
| mako                       | 13.4 ms                                                  | 13.5 ms: 1.01x slower                                                   |
| fannkuch                   | 461 ms                                                   | 465 ms: 1.01x slower                                                    |
| sympy_expand               | 457 ms                                                   | 461 ms: 1.01x slower                                                    |
| raytrace                   | 300 ms                                                   | 303 ms: 1.01x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 5.94 sec: 1.01x slower                                                  |
| comprehensions             | 20.4 us                                                  | 20.6 us: 1.01x slower                                                   |
| meteor_contest             | 114 ms                                                   | 115 ms: 1.01x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 3.88 ms: 1.02x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 197 us: 1.02x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.41 ms: 1.02x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.1 ms: 1.03x slower                                                   |
| json_loads                 | 31.7 us                                                  | 32.7 us: 1.03x slower                                                   |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.01 sec: 1.04x slower                                                  |
| pyflate                    | 556 ms                                                   | 582 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (33): html5lib, scimark_sparse_mat_mult, logging_format, genshi_xml, nqueens, tornado_http, logging_simple, logging_silent, crypto_pyaes, richards, sympy_sum, json_dumps, spectral_norm, sqlglot_normalize, sqlglot_transpile, regex_compile, sympy_integrate, sqlglot_optimize, json, sympy_str, django_template, coverage, pidigits, xml_etree_process, asyncio_websockets, pickle_pure_python, regex_dna, python_startup_no_site, chaos, unpickle_pure_python, regex_effbot, hexiom, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240904-3.14.0a0-2fa7b0e/bm-20240904-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-2fa7b0e.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 99.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x