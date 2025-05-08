# Results vs. 3.13.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.031x faster
- HPT reliability: 86.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                          |
| html5lib       | 65.6 ms                                                  | 63.6 ms: 1.03x faster                                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                            |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 899 ms: 1.27x faster                                                            |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 935 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                            |
| async_generators           | 500 ms                                                   | 475 ms: 1.05x faster                                                            |
| Geometric mean             | (ref)                                                    | 1.20x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 95.8 ms                                                  | 88.6 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                           |
| regex_v8       | 32.5 ms                                                  | 28.4 ms: 1.14x faster                                                           |
| regex_dna      | 263 ms                                                   | 238 ms: 1.11x faster                                                            |
| Geometric mean | (ref)                                                    | 1.14x faster                                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|---------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 150 ms: 1.06x faster                                                            |
| xml_etree_parse     | 203 ms                                                   | 191 ms: 1.06x faster                                                            |
| tomli_loads         | 2.67 sec                                                 | 2.55 sec: 1.05x faster                                                          |
| pickle_pure_python  | 374 us                                                   | 402 us: 1.08x slower                                                            |
| json_loads          | 32.8 us                                                  | 36.0 us: 1.10x slower                                                           |
| json_dumps          | 14.2 ms                                                  | 15.7 ms: 1.11x slower                                                           |
| Geometric mean      | (ref)                                                    | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                    | 1.03x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 61.6 ms                                                  | 64.6 ms: 1.05x slower                                                           |
| django_template | 39.4 ms                                                  | 42.0 ms: 1.07x slower                                                           |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------------|:--------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 3.45 sec                                                 | 1.71 sec: 2.02x faster                                                          |
| async_tree_memoization_tg  | 663 ms                                                   | 469 ms: 1.41x faster                                                            |
| async_tree_memoization     | 664 ms                                                   | 471 ms: 1.41x faster                                                            |
| deepcopy                   | 479 us                                                   | 346 us: 1.38x faster                                                            |
| deepcopy_memo              | 53.0 us                                                  | 39.4 us: 1.35x faster                                                           |
| regex_effbot               | 5.10 ms                                                  | 3.95 ms: 1.29x faster                                                           |
| async_tree_none_tg         | 484 ms                                                   | 379 ms: 1.28x faster                                                            |
| async_tree_io              | 1.14 sec                                                 | 899 ms: 1.27x faster                                                            |
| go                         | 164 ms                                                   | 130 ms: 1.26x faster                                                            |
| async_tree_none            | 504 ms                                                   | 401 ms: 1.26x faster                                                            |
| async_tree_io_tg           | 1.16 sec                                                 | 935 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 656 ms: 1.22x faster                                                            |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 665 ms: 1.19x faster                                                            |
| deepcopy_reduce            | 4.24 us                                                  | 3.70 us: 1.15x faster                                                           |
| regex_v8                   | 32.5 ms                                                  | 28.4 ms: 1.14x faster                                                           |
| regex_dna                  | 263 ms                                                   | 238 ms: 1.11x faster                                                            |
| pylint                     | 345 ms                                                   | 314 ms: 1.10x faster                                                            |
| scimark_sor                | 164 ms                                                   | 150 ms: 1.10x faster                                                            |
| generators                 | 40.3 ms                                                  | 36.8 ms: 1.10x faster                                                           |
| spectral_norm              | 143 ms                                                   | 132 ms: 1.09x faster                                                            |
| float                      | 95.8 ms                                                  | 88.6 ms: 1.08x faster                                                           |
| pathlib                    | 24.3 ms                                                  | 22.8 ms: 1.07x faster                                                           |
| scimark_monte_carlo        | 87.8 ms                                                  | 82.6 ms: 1.06x faster                                                           |
| xml_etree_iterparse        | 159 ms                                                   | 150 ms: 1.06x faster                                                            |
| xml_etree_parse            | 203 ms                                                   | 191 ms: 1.06x faster                                                            |
| python_startup             | 16.0 ms                                                  | 15.2 ms: 1.06x faster                                                           |
| async_generators           | 500 ms                                                   | 475 ms: 1.05x faster                                                            |
| logging_silent             | 135 ns                                                   | 128 ns: 1.05x faster                                                            |
| bpe_tokeniser              | 6.02 sec                                                 | 5.72 sec: 1.05x faster                                                          |
| richards_super             | 60.8 ms                                                  | 58.0 ms: 1.05x faster                                                           |
| tomli_loads                | 2.67 sec                                                 | 2.55 sec: 1.05x faster                                                          |
| k_core                     | 2.99 sec                                                 | 2.87 sec: 1.04x faster                                                          |
| pycparser                  | 1.34 sec                                                 | 1.30 sec: 1.03x faster                                                          |
| html5lib                   | 65.6 ms                                                  | 63.6 ms: 1.03x faster                                                           |
| djangocms                  | 66.2 us                                                  | 65.0 us: 1.02x faster                                                           |
| docutils                   | 2.96 sec                                                 | 3.00 sec: 1.01x slower                                                          |
| coverage                   | 106 ms                                                   | 110 ms: 1.04x slower                                                            |
| typing_runtime_protocols   | 197 us                                                   | 206 us: 1.04x slower                                                            |
| genshi_xml                 | 61.6 ms                                                  | 64.6 ms: 1.05x slower                                                           |
| connected_components       | 547 ms                                                   | 574 ms: 1.05x slower                                                            |
| crypto_pyaes               | 84.9 ms                                                  | 89.3 ms: 1.05x slower                                                           |
| shortest_path              | 565 ms                                                   | 598 ms: 1.06x slower                                                            |
| fannkuch                   | 478 ms                                                   | 509 ms: 1.07x slower                                                            |
| sympy_str                  | 265 ms                                                   | 283 ms: 1.07x slower                                                            |
| django_template            | 39.4 ms                                                  | 42.0 ms: 1.07x slower                                                           |
| raytrace                   | 310 ms                                                   | 331 ms: 1.07x slower                                                            |
| json                       | 5.94 ms                                                  | 6.34 ms: 1.07x slower                                                           |
| scimark_lu                 | 146 ms                                                   | 157 ms: 1.07x slower                                                            |
| pickle_pure_python         | 374 us                                                   | 402 us: 1.08x slower                                                            |
| create_gc_cycles           | 3.39 ms                                                  | 3.71 ms: 1.09x slower                                                           |
| json_loads                 | 32.8 us                                                  | 36.0 us: 1.10x slower                                                           |
| comprehensions             | 20.8 us                                                  | 22.9 us: 1.10x slower                                                           |
| json_dumps                 | 14.2 ms                                                  | 15.7 ms: 1.11x slower                                                           |
| gc_traversal               | 5.92 ms                                                  | 6.91 ms: 1.17x slower                                                           |
| many_optionals             | 626 us                                                   | 877 us: 1.40x slower                                                            |
| subparsers                 | 20.3 ms                                                  | 28.5 ms: 1.40x slower                                                           |
| bench_mp_pool              | 8.07 ms                                                  | 2.21 sec: 273.34x slower                                                        |
| Geometric mean             | (ref)                                                    | 1.03x slower                                                                    |

Benchmark hidden because not significant (33): regex_compile, richards, sympy_integrate, telco, scimark_fft, hexiom, thrift, deltablue, pprint_safe_repr, pprint_pformat, sympy_sum, pyflate, sphinx, python_startup_no_site, sqlite_synth, asyncio_websockets, chaos, logging_simple, pidigits, 2to3, meteor_contest, genshi_text, mako, logging_format, xml_etree_generate, coroutines, bench_thread_pool, nqueens, unpickle_pure_python, xml_etree_process, sympy_expand, scimark_sparse_mat_mult, nbody
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (5) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: dulwich_log, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.031x faster

# HPT report

- Reliability score: 86.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.05x