# Results vs. 3.13.0

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.005x faster
- HPT reliability: 89.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| Geometric mean | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 509 ms: 1.30x faster                                                     |
| async_tree_memoization     | 664 ms                                                   | 514 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 941 ms: 1.24x faster                                                     |
| async_tree_none            | 504 ms                                                   | 411 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 948 ms: 1.20x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 405 ms: 1.20x faster                                                     |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 704 ms: 1.12x faster                                                     |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                     |
| Geometric mean             | (ref)                                                    | 1.15x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.8 ms: 1.08x faster                                                    |
| Geometric mean | (ref)                                                    | 1.00x faster                                                             |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| regex_dna      | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| regex_compile  | 134 ms                                                   | 127 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                    | 1.10x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 203 ms                                                   | 182 ms: 1.12x faster                                                     |
| tomli_loads          | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                   |
| unpickle_pure_python | 265 us                                                   | 282 us: 1.06x slower                                                     |
| pickle_pure_python   | 374 us                                                   | 416 us: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.00x slower                                                             |

Benchmark hidden because not significant (5): xml_etree_iterparse, xml_etree_generate, xml_etree_process, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.11 ms: 1.04x slower                                                    |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                             |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 42.1 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.01x slower                                                             |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 341 us: 1.40x faster                                                     |
| deepcopy_memo              | 53.0 us                                                  | 40.5 us: 1.31x faster                                                    |
| async_tree_memoization_tg  | 663 ms                                                   | 509 ms: 1.30x faster                                                     |
| regex_effbot               | 5.10 ms                                                  | 3.92 ms: 1.30x faster                                                    |
| async_tree_memoization     | 664 ms                                                   | 514 ms: 1.29x faster                                                     |
| async_tree_io_tg           | 1.16 sec                                                 | 941 ms: 1.24x faster                                                     |
| async_tree_none            | 504 ms                                                   | 411 ms: 1.23x faster                                                     |
| async_tree_io              | 1.14 sec                                                 | 948 ms: 1.20x faster                                                     |
| async_tree_none_tg         | 484 ms                                                   | 405 ms: 1.20x faster                                                     |
| spectral_norm              | 143 ms                                                   | 121 ms: 1.19x faster                                                     |
| deepcopy_reduce            | 4.24 us                                                  | 3.60 us: 1.18x faster                                                    |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 690 ms: 1.16x faster                                                     |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 704 ms: 1.12x faster                                                     |
| xml_etree_parse            | 203 ms                                                   | 182 ms: 1.12x faster                                                     |
| generators                 | 40.3 ms                                                  | 37.0 ms: 1.09x faster                                                    |
| pylint                     | 345 ms                                                   | 319 ms: 1.08x faster                                                     |
| float                      | 95.8 ms                                                  | 88.8 ms: 1.08x faster                                                    |
| telco                      | 10.5 ms                                                  | 9.74 ms: 1.07x faster                                                    |
| thrift                     | 1.01 ms                                                  | 942 us: 1.07x faster                                                     |
| regex_dna                  | 263 ms                                                   | 246 ms: 1.07x faster                                                     |
| tomli_loads                | 2.67 sec                                                 | 2.50 sec: 1.07x faster                                                   |
| scimark_fft                | 463 ms                                                   | 438 ms: 1.06x faster                                                     |
| regex_compile              | 134 ms                                                   | 127 ms: 1.05x faster                                                     |
| scimark_sor                | 164 ms                                                   | 156 ms: 1.05x faster                                                     |
| scimark_lu                 | 146 ms                                                   | 140 ms: 1.05x faster                                                     |
| sqlite_synth               | 4.08 us                                                  | 3.93 us: 1.04x faster                                                    |
| async_generators           | 500 ms                                                   | 485 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 6.02 sec                                                 | 5.85 sec: 1.03x faster                                                   |
| shortest_path              | 565 ms                                                   | 578 ms: 1.02x slower                                                     |
| python_startup_no_site     | 8.79 ms                                                  | 9.11 ms: 1.04x slower                                                    |
| deltablue                  | 3.97 ms                                                  | 4.18 ms: 1.06x slower                                                    |
| sympy_expand               | 472 ms                                                   | 500 ms: 1.06x slower                                                     |
| unpickle_pure_python       | 265 us                                                   | 282 us: 1.06x slower                                                     |
| django_template            | 39.4 ms                                                  | 42.1 ms: 1.07x slower                                                    |
| raytrace                   | 310 ms                                                   | 333 ms: 1.07x slower                                                     |
| pycparser                  | 1.34 sec                                                 | 1.45 sec: 1.08x slower                                                   |
| meteor_contest             | 117 ms                                                   | 126 ms: 1.08x slower                                                     |
| sympy_str                  | 265 ms                                                   | 286 ms: 1.08x slower                                                     |
| sympy_integrate            | 21.4 ms                                                  | 23.2 ms: 1.08x slower                                                    |
| docutils                   | 2.96 sec                                                 | 3.23 sec: 1.09x slower                                                   |
| create_gc_cycles           | 3.39 ms                                                  | 3.72 ms: 1.10x slower                                                    |
| pickle_pure_python         | 374 us                                                   | 416 us: 1.11x slower                                                     |
| typing_runtime_protocols   | 197 us                                                   | 222 us: 1.12x slower                                                     |
| sqlglot_parse              | 1.43 ms                                                  | 1.64 ms: 1.15x slower                                                    |
| fannkuch                   | 478 ms                                                   | 552 ms: 1.15x slower                                                     |
| hexiom                     | 7.34 ms                                                  | 8.60 ms: 1.17x slower                                                    |
| gc_traversal               | 5.92 ms                                                  | 6.98 ms: 1.18x slower                                                    |
| comprehensions             | 20.8 us                                                  | 24.6 us: 1.18x slower                                                    |
| crypto_pyaes               | 84.9 ms                                                  | 101 ms: 1.19x slower                                                     |
| subparsers                 | 20.3 ms                                                  | 26.3 ms: 1.29x slower                                                    |
| pprint_safe_repr           | 962 ms                                                   | 1.27 sec: 1.32x slower                                                   |
| pprint_pformat             | 1.99 sec                                                 | 2.64 sec: 1.33x slower                                                   |
| many_optionals             | 626 us                                                   | 882 us: 1.41x slower                                                     |
| bench_mp_pool              | 8.07 ms                                                  | 2.72 sec: 336.87x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (41): pathlib, xml_etree_iterparse, logging_format, genshi_text, coverage, pyflate, go, xml_etree_generate, scimark_monte_carlo, chaos, sympy_sum, html5lib, richards, json, asyncio_websockets, logging_simple, sqlalchemy_declarative, k_core, mdp, logging_silent, sqlglot_normalize, sphinx, regex_v8, connected_components, mako, sqlalchemy_imperative, coroutines, nqueens, bench_thread_pool, pidigits, genshi_xml, python_startup, sqlglot_optimize, xml_etree_process, richards_super, 2to3, json_dumps, nbody, json_loads, sqlglot_transpile, scimark_sparse_mat_mult
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (9) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 89.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.04x