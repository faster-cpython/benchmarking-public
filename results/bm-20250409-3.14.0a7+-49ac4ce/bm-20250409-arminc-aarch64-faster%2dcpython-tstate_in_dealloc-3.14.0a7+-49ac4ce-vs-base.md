# Results vs. base

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-aarch64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.000x faster
- HPT reliability: 76.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| docutils       | 2.95 sec                                                                 | 2.92 sec: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|--------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg | 375 ms                                                                   | 367 ms: 1.02x faster                                                            |
| async_tree_none    | 396 ms                                                                   | 389 ms: 1.02x faster                                                            |
| async_tree_io      | 887 ms                                                                   | 878 ms: 1.01x faster                                                            |
| Geometric mean     | (ref)                                                                    | 1.00x faster                                                                    |

Benchmark hidden because not significant (8): asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 83.2 ms                                                                  | 86.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                   | 242 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|---------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 388 us                                                                   | 371 us: 1.05x faster                                                            |
| xml_etree_iterparse | 140 ms                                                                   | 141 ms: 1.01x slower                                                            |
| Geometric mean      | (ref)                                                                    | 1.01x slower                                                                    |

Benchmark hidden because not significant (7): json_dumps, xml_etree_parse, tomli_loads, json_loads, xml_etree_generate, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): mako, django_template, genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250408-arminc-aarch64-python-c5e856a5dc8eed4813ec-3.14.0a7+-c5e856a | bm-20250409-arminc-aarch64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python      | 388 us                                                                   | 371 us: 1.05x faster                                                            |
| regex_dna               | 250 ms                                                                   | 242 ms: 1.03x faster                                                            |
| pprint_safe_repr        | 930 ms                                                                   | 902 ms: 1.03x faster                                                            |
| pprint_pformat          | 1.90 sec                                                                 | 1.86 sec: 1.02x faster                                                          |
| async_tree_none_tg      | 375 ms                                                                   | 367 ms: 1.02x faster                                                            |
| connected_components    | 561 ms                                                                   | 550 ms: 1.02x faster                                                            |
| async_tree_none         | 396 ms                                                                   | 389 ms: 1.02x faster                                                            |
| logging_format          | 7.90 us                                                                  | 7.79 us: 1.01x faster                                                           |
| deepcopy_reduce         | 3.46 us                                                                  | 3.42 us: 1.01x faster                                                           |
| docutils                | 2.95 sec                                                                 | 2.92 sec: 1.01x faster                                                          |
| async_tree_io           | 887 ms                                                                   | 878 ms: 1.01x faster                                                            |
| generators              | 36.4 ms                                                                  | 36.0 ms: 1.01x faster                                                           |
| logging_simple          | 7.12 us                                                                  | 7.07 us: 1.01x faster                                                           |
| xml_etree_iterparse     | 140 ms                                                                   | 141 ms: 1.01x slower                                                            |
| sqlite_synth            | 3.81 us                                                                  | 3.85 us: 1.01x slower                                                           |
| scimark_sparse_mat_mult | 6.70 ms                                                                  | 6.82 ms: 1.02x slower                                                           |
| bench_thread_pool       | 1.33 ms                                                                  | 1.35 ms: 1.02x slower                                                           |
| mdp                     | 1.61 sec                                                                 | 1.66 sec: 1.03x slower                                                          |
| float                   | 83.2 ms                                                                  | 86.0 ms: 1.03x slower                                                           |
| scimark_fft             | 416 ms                                                                   | 433 ms: 1.04x slower                                                            |
| pathlib                 | 21.8 ms                                                                  | 22.9 ms: 1.05x slower                                                           |
| Geometric mean          | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (74): bench_mp_pool, sqlglot_v2_transpile, subparsers, typing_runtime_protocols, sqlglot_v2_parse, regex_effbot, richards_super, sympy_sum, scimark_lu, asyncio_websockets, deepcopy_memo, nqueens, logging_silent, dulwich_log, regex_v8, shortest_path, deltablue, sqlglot_v2_normalize, comprehensions, fannkuch, mako, gc_traversal, sympy_expand, python_startup, coroutines, many_optionals, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, pidigits, bpe_tokeniser, sqlalchemy_declarative, richards, json_dumps, deepcopy, python_startup_no_site, html5lib, xml_etree_parse, sqlglot_v2_optimize, async_tree_cpu_io_mixed, tomli_loads, json, k_core, sphinx, sympy_integrate, nbody, go, coverage, json_loads, raytrace, scimark_monte_carlo, spectral_norm, pyflate, pycparser, sqlalchemy_imperative, crypto_pyaes, async_generators, create_gc_cycles, meteor_contest, telco, 2to3, regex_compile, xml_etree_generate, chaos, django_template, pylint, unpickle_pure_python, genshi_xml, xml_etree_process, sympy_str, hexiom, scimark_sor, genshi_text

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 76.43% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x