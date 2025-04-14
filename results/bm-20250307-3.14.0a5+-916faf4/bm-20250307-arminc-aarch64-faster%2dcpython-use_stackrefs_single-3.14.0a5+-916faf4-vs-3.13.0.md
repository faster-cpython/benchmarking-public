# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs_single
- machine: linux-aarch64
- commit hash: 916faf4
- commit date: 2025-03-07
- overall geometric mean: 1.017x faster
- HPT reliability: 84.55%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 2.96 sec                                                 | 3.06 sec: 1.03x slower                                                             |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                       |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                               |
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                               |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                               |
| async_tree_io_tg           | 1.16 sec                                                 | 941 ms: 1.24x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                               |
| async_tree_io              | 1.14 sec                                                 | 933 ms: 1.22x faster                                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 695 ms: 1.14x faster                                                               |
| async_generators           | 500 ms                                                   | 467 ms: 1.07x faster                                                               |
| Geometric mean             | (ref)                                                    | 1.18x faster                                                                       |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 118 ms                                                   | 128 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                    | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                              |
| Geometric mean | (ref)                                                    | 1.06x faster                                                                       |

Benchmark hidden because not significant (3): regex_dna, regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|---------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_iterparse | 159 ms                                                   | 147 ms: 1.08x faster                                                               |
| xml_etree_parse     | 203 ms                                                   | 189 ms: 1.07x faster                                                               |
| tomli_loads         | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                             |
| pickle_pure_python  | 374 us                                                   | 405 us: 1.08x slower                                                               |
| Geometric mean      | (ref)                                                    | 1.01x slower                                                                       |

Benchmark hidden because not significant (5): xml_etree_generate, xml_etree_process, json_dumps, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.79 ms                                                  | 9.10 ms: 1.03x slower                                                              |
| Geometric mean         | (ref)                                                    | 1.03x slower                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 39.4 ms                                                  | 40.8 ms: 1.04x slower                                                              |
| mako            | 14.0 ms                                                  | 14.9 ms: 1.06x slower                                                              |
| Geometric mean  | (ref)                                                    | 1.03x slower                                                                       |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| deepcopy                   | 479 us                                                   | 347 us: 1.38x faster                                                               |
| async_tree_memoization     | 664 ms                                                   | 486 ms: 1.37x faster                                                               |
| async_tree_memoization_tg  | 663 ms                                                   | 486 ms: 1.36x faster                                                               |
| deepcopy_memo              | 53.0 us                                                  | 40.4 us: 1.31x faster                                                              |
| async_tree_none            | 504 ms                                                   | 394 ms: 1.28x faster                                                               |
| regex_effbot               | 5.10 ms                                                  | 4.04 ms: 1.26x faster                                                              |
| async_tree_io_tg           | 1.16 sec                                                 | 941 ms: 1.24x faster                                                               |
| async_tree_none_tg         | 484 ms                                                   | 393 ms: 1.23x faster                                                               |
| async_tree_io              | 1.14 sec                                                 | 933 ms: 1.22x faster                                                               |
| async_tree_cpu_io_mixed_tg | 801 ms                                                   | 679 ms: 1.18x faster                                                               |
| deepcopy_reduce            | 4.24 us                                                  | 3.62 us: 1.17x faster                                                              |
| spectral_norm              | 143 ms                                                   | 125 ms: 1.15x faster                                                               |
| async_tree_cpu_io_mixed    | 789 ms                                                   | 695 ms: 1.14x faster                                                               |
| go                         | 164 ms                                                   | 147 ms: 1.12x faster                                                               |
| xml_etree_iterparse        | 159 ms                                                   | 147 ms: 1.08x faster                                                               |
| generators                 | 40.3 ms                                                  | 37.4 ms: 1.08x faster                                                              |
| xml_etree_parse            | 203 ms                                                   | 189 ms: 1.07x faster                                                               |
| async_generators           | 500 ms                                                   | 467 ms: 1.07x faster                                                               |
| telco                      | 10.5 ms                                                  | 9.79 ms: 1.07x faster                                                              |
| scimark_fft                | 463 ms                                                   | 435 ms: 1.06x faster                                                               |
| tomli_loads                | 2.67 sec                                                 | 2.58 sec: 1.03x faster                                                             |
| bpe_tokeniser              | 6.02 sec                                                 | 5.82 sec: 1.03x faster                                                             |
| pprint_pformat             | 1.99 sec                                                 | 2.05 sec: 1.03x slower                                                             |
| docutils                   | 2.96 sec                                                 | 3.06 sec: 1.03x slower                                                             |
| python_startup_no_site     | 8.79 ms                                                  | 9.10 ms: 1.03x slower                                                              |
| django_template            | 39.4 ms                                                  | 40.8 ms: 1.04x slower                                                              |
| pyflate                    | 582 ms                                                   | 607 ms: 1.04x slower                                                               |
| pprint_safe_repr           | 962 ms                                                   | 1.00 sec: 1.04x slower                                                             |
| sympy_str                  | 265 ms                                                   | 278 ms: 1.05x slower                                                               |
| connected_components       | 547 ms                                                   | 577 ms: 1.06x slower                                                               |
| create_gc_cycles           | 3.39 ms                                                  | 3.60 ms: 1.06x slower                                                              |
| raytrace                   | 310 ms                                                   | 329 ms: 1.06x slower                                                               |
| shortest_path              | 565 ms                                                   | 600 ms: 1.06x slower                                                               |
| sqlglot_parse              | 1.43 ms                                                  | 1.52 ms: 1.06x slower                                                              |
| mako                       | 14.0 ms                                                  | 14.9 ms: 1.06x slower                                                              |
| comprehensions             | 20.8 us                                                  | 22.4 us: 1.07x slower                                                              |
| scimark_lu                 | 146 ms                                                   | 157 ms: 1.08x slower                                                               |
| nbody                      | 118 ms                                                   | 128 ms: 1.08x slower                                                               |
| pickle_pure_python         | 374 us                                                   | 405 us: 1.08x slower                                                               |
| crypto_pyaes               | 84.9 ms                                                  | 93.4 ms: 1.10x slower                                                              |
| fannkuch                   | 478 ms                                                   | 528 ms: 1.11x slower                                                               |
| gc_traversal               | 5.92 ms                                                  | 7.13 ms: 1.20x slower                                                              |
| subparsers                 | 20.3 ms                                                  | 27.8 ms: 1.37x slower                                                              |
| many_optionals             | 626 us                                                   | 895 us: 1.43x slower                                                               |
| bench_mp_pool              | 8.07 ms                                                  | 4.66 sec: 577.24x slower                                                           |
| Geometric mean             | (ref)                                                    | 1.06x slower                                                                       |

Benchmark hidden because not significant (50): pylint, sympy_sum, pathlib, float, coverage, sqlglot_optimize, k_core, thrift, sqlalchemy_declarative, scimark_sor, pidigits, regex_dna, logging_format, sphinx, pycparser, 2to3, mdp, regex_compile, xml_etree_generate, genshi_text, regex_v8, scimark_monte_carlo, sqlglot_normalize, sympy_expand, scimark_sparse_mat_mult, richards, asyncio_websockets, sqlglot_transpile, html5lib, nqueens, sqlite_synth, xml_etree_process, json, logging_silent, json_dumps, python_startup, sqlalchemy_imperative, genshi_xml, typing_runtime_protocols, bench_thread_pool, meteor_contest, sympy_integrate, richards_super, chaos, hexiom, coroutines, json_loads, logging_simple, deltablue, unpickle_pure_python
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20250307-3.14.0a5+-916faf4/bm-20250307-arminc-aarch64-faster%2dcpython-use_stackrefs_single-3.14.0a5+-916faf4.json: dulwich_log

- Geometric mean (including insignificant results): 1.017x faster

# HPT report

- Reliability score: 84.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.02x