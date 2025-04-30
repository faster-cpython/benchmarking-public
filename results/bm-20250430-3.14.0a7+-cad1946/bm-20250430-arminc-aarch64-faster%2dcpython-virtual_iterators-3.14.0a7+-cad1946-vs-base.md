# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.002x faster
- HPT reliability: 77.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 298 ms                                                                   | 294 ms: 1.01x faster                                                            |
| docutils       | 2.98 sec                                                                 | 2.91 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 393 ms                                                                   | 381 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed | 676 ms                                                                   | 663 ms: 1.02x faster                                                            |
| async_tree_io           | 897 ms                                                                   | 882 ms: 1.02x faster                                                            |
| async_tree_memoization  | 466 ms                                                                   | 459 ms: 1.01x faster                                                            |
| Geometric mean          | (ref)                                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (7): async_generators, async_tree_memoization_tg, asyncio_websockets, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_io_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                   | 241 ms: 1.02x slower                                                            |
| regex_v8       | 27.4 ms                                                                  | 28.3 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|---------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 141 ms                                                                   | 144 ms: 1.02x slower                                                            |
| xml_etree_parse     | 176 ms                                                                   | 182 ms: 1.03x slower                                                            |
| Geometric mean      | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (7): json_dumps, xml_etree_generate, xml_etree_process, json_loads, tomli_loads, pickle_pure_python, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                           |
| python_startup_no_site | 8.62 ms                                                                  | 8.68 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 14.0 ms                                                                  | 14.3 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                    |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 | bm-20250430-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| bench_mp_pool           | 2.81 sec                                                                 | 1.87 sec: 1.51x faster                                                          |
| coverage                | 111 ms                                                                   | 103 ms: 1.08x faster                                                            |
| create_gc_cycles        | 3.71 ms                                                                  | 3.59 ms: 1.03x faster                                                           |
| async_tree_none         | 393 ms                                                                   | 381 ms: 1.03x faster                                                            |
| mdp                     | 1.68 sec                                                                 | 1.64 sec: 1.03x faster                                                          |
| docutils                | 2.98 sec                                                                 | 2.91 sec: 1.02x faster                                                          |
| gc_traversal            | 6.66 ms                                                                  | 6.53 ms: 1.02x faster                                                           |
| async_tree_cpu_io_mixed | 676 ms                                                                   | 663 ms: 1.02x faster                                                            |
| k_core                  | 2.85 sec                                                                 | 2.79 sec: 1.02x faster                                                          |
| json                    | 6.10 ms                                                                  | 6.00 ms: 1.02x faster                                                           |
| async_tree_io           | 897 ms                                                                   | 882 ms: 1.02x faster                                                            |
| async_tree_memoization  | 466 ms                                                                   | 459 ms: 1.01x faster                                                            |
| 2to3                    | 298 ms                                                                   | 294 ms: 1.01x faster                                                            |
| logging_format          | 7.72 us                                                                  | 7.62 us: 1.01x faster                                                           |
| hexiom                  | 6.96 ms                                                                  | 6.87 ms: 1.01x faster                                                           |
| connected_components    | 563 ms                                                                   | 557 ms: 1.01x faster                                                            |
| go                      | 129 ms                                                                   | 128 ms: 1.01x faster                                                            |
| crypto_pyaes            | 85.7 ms                                                                  | 85.0 ms: 1.01x faster                                                           |
| logging_simple          | 6.97 us                                                                  | 6.92 us: 1.01x faster                                                           |
| python_startup          | 16.1 ms                                                                  | 16.2 ms: 1.01x slower                                                           |
| python_startup_no_site  | 8.62 ms                                                                  | 8.68 ms: 1.01x slower                                                           |
| subparsers              | 25.8 ms                                                                  | 26.1 ms: 1.01x slower                                                           |
| xml_etree_iterparse     | 141 ms                                                                   | 144 ms: 1.02x slower                                                            |
| regex_dna               | 236 ms                                                                   | 241 ms: 1.02x slower                                                            |
| mako                    | 14.0 ms                                                                  | 14.3 ms: 1.02x slower                                                           |
| regex_v8                | 27.4 ms                                                                  | 28.3 ms: 1.03x slower                                                           |
| xml_etree_parse         | 176 ms                                                                   | 182 ms: 1.03x slower                                                            |
| deltablue               | 3.77 ms                                                                  | 3.92 ms: 1.04x slower                                                           |
| Geometric mean          | (ref)                                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (62): comprehensions, regex_compile, many_optionals, genshi_xml, dulwich_log, pathlib, sqlglot_v2_normalize, spectral_norm, json_dumps, pycparser, deepcopy_memo, pprint_safe_repr, async_generators, xml_etree_generate, typing_runtime_protocols, sphinx, logging_silent, sqlglot_v2_optimize, sqlglot_v2_transpile, pprint_pformat, scimark_monte_carlo, xml_etree_process, deepcopy, generators, scimark_sparse_mat_mult, regex_effbot, json_loads, tomli_loads, async_tree_memoization_tg, asyncio_websockets, pickle_pure_python, async_tree_none_tg, pidigits, float, async_tree_cpu_io_mixed_tg, meteor_contest, pyflate, sqlglot_v2_parse, bpe_tokeniser, deepcopy_reduce, shortest_path, nqueens, unpickle_pure_python, scimark_fft, nbody, scimark_sor, fannkuch, async_tree_io_tg, raytrace, sqlalchemy_imperative, scimark_lu, coroutines, sqlalchemy_declarative, telco, chaos, richards_super, bench_thread_pool, richards, html5lib, sqlite_synth, django_template, genshi_text
Ignored benchmarks (5) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-arminc-aarch64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 77.51% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x