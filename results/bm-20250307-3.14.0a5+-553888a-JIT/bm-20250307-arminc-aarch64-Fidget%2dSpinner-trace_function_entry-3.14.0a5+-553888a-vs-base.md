# Results vs. base

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.001x slower
- HPT reliability: 79.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_generators        | 464 ms                                                                   | 427 ms: 1.09x faster                                                               |
| async_tree_cpu_io_mixed | 655 ms                                                                   | 662 ms: 1.01x slower                                                               |
| async_tree_memoization  | 468 ms                                                                   | 478 ms: 1.02x slower                                                               |
| async_tree_none         | 367 ms                                                                   | 379 ms: 1.03x slower                                                               |
| Geometric mean          | (ref)                                                                    | 1.00x slower                                                                       |

Benchmark hidden because not significant (7): async_tree_none_tg, coroutines, async_tree_cpu_io_mixed_tg, asyncio_websockets, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 82.2 ms                                                                  | 82.8 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                       |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_dna      | 250 ms                                                                   | 242 ms: 1.03x faster                                                               |
| regex_v8       | 30.2 ms                                                                  | 29.8 ms: 1.01x faster                                                              |
| regex_compile  | 127 ms                                                                   | 128 ms: 1.01x slower                                                               |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|--------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate | 108 ms                                                                   | 106 ms: 1.02x faster                                                               |
| xml_etree_process  | 77.0 ms                                                                  | 75.7 ms: 1.02x faster                                                              |
| xml_etree_parse    | 177 ms                                                                   | 176 ms: 1.01x faster                                                               |
| tomli_loads        | 2.40 sec                                                                 | 2.49 sec: 1.04x slower                                                             |
| Geometric mean     | (ref)                                                                    | 1.00x slower                                                                       |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_iterparse, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 10.0 ms                                                                  | 10.1 ms: 1.01x slower                                                              |
| Geometric mean         | (ref)                                                                    | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                  | 13.2 ms: 1.01x faster                                                              |
| genshi_text    | 26.4 ms                                                                  | 26.6 ms: 1.01x slower                                                              |
| Geometric mean | (ref)                                                                    | 1.00x faster                                                                       |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark               | bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| bench_mp_pool           | 2.44 sec                                                                 | 548 ms: 4.45x faster                                                               |
| async_generators        | 464 ms                                                                   | 427 ms: 1.09x faster                                                               |
| create_gc_cycles        | 3.63 ms                                                                  | 3.51 ms: 1.03x faster                                                              |
| regex_dna               | 250 ms                                                                   | 242 ms: 1.03x faster                                                               |
| comprehensions          | 24.4 us                                                                  | 23.6 us: 1.03x faster                                                              |
| deepcopy                | 328 us                                                                   | 320 us: 1.03x faster                                                               |
| deepcopy_memo           | 38.3 us                                                                  | 37.4 us: 1.02x faster                                                              |
| xml_etree_generate      | 108 ms                                                                   | 106 ms: 1.02x faster                                                               |
| xml_etree_process       | 77.0 ms                                                                  | 75.7 ms: 1.02x faster                                                              |
| k_core                  | 2.91 sec                                                                 | 2.86 sec: 1.02x faster                                                             |
| regex_v8                | 30.2 ms                                                                  | 29.8 ms: 1.01x faster                                                              |
| pyflate                 | 561 ms                                                                   | 553 ms: 1.01x faster                                                               |
| sympy_integrate         | 21.3 ms                                                                  | 21.1 ms: 1.01x faster                                                              |
| mako                    | 13.4 ms                                                                  | 13.2 ms: 1.01x faster                                                              |
| sympy_str               | 272 ms                                                                   | 269 ms: 1.01x faster                                                               |
| xml_etree_parse         | 177 ms                                                                   | 176 ms: 1.01x faster                                                               |
| go                      | 138 ms                                                                   | 138 ms: 1.01x faster                                                               |
| python_startup_no_site  | 10.0 ms                                                                  | 10.1 ms: 1.01x slower                                                              |
| float                   | 82.2 ms                                                                  | 82.8 ms: 1.01x slower                                                              |
| logging_simple          | 6.83 us                                                                  | 6.88 us: 1.01x slower                                                              |
| scimark_sparse_mat_mult | 6.64 ms                                                                  | 6.69 ms: 1.01x slower                                                              |
| regex_compile           | 127 ms                                                                   | 128 ms: 1.01x slower                                                               |
| genshi_text             | 26.4 ms                                                                  | 26.6 ms: 1.01x slower                                                              |
| meteor_contest          | 119 ms                                                                   | 121 ms: 1.01x slower                                                               |
| async_tree_cpu_io_mixed | 655 ms                                                                   | 662 ms: 1.01x slower                                                               |
| generators              | 35.7 ms                                                                  | 36.2 ms: 1.02x slower                                                              |
| async_tree_memoization  | 468 ms                                                                   | 478 ms: 1.02x slower                                                               |
| sqlglot_transpile       | 1.82 ms                                                                  | 1.88 ms: 1.03x slower                                                              |
| async_tree_none         | 367 ms                                                                   | 379 ms: 1.03x slower                                                               |
| tomli_loads             | 2.40 sec                                                                 | 2.49 sec: 1.04x slower                                                             |
| sqlglot_parse           | 1.49 ms                                                                  | 1.54 ms: 1.04x slower                                                              |
| crypto_pyaes            | 96.7 ms                                                                  | 102 ms: 1.05x slower                                                               |
| dulwich_log             | 63.6 ms                                                                  | 67.6 ms: 1.06x slower                                                              |
| sqlalchemy_imperative   | 15.6 ms                                                                  | 16.9 ms: 1.08x slower                                                              |
| Geometric mean          | (ref)                                                                    | 1.01x faster                                                                       |

Benchmark hidden because not significant (57): deepcopy_reduce, chaos, json_dumps, deltablue, json, many_optionals, sympy_expand, raytrace, sqlite_synth, genshi_xml, async_tree_none_tg, spectral_norm, logging_silent, nbody, coroutines, pycparser, bpe_tokeniser, scimark_fft, python_startup, regex_effbot, hexiom, logging_format, pylint, shortest_path, html5lib, async_tree_cpu_io_mixed_tg, pathlib, json_loads, mdp, connected_components, bench_thread_pool, subparsers, 2to3, sqlalchemy_declarative, typing_runtime_protocols, scimark_sor, asyncio_websockets, sphinx, async_tree_io, nqueens, django_template, gc_traversal, async_tree_memoization_tg, telco, scimark_monte_carlo, xml_etree_iterparse, unpickle_pure_python, async_tree_io_tg, pickle_pure_python, sympy_sum, richards_super, pidigits, coverage, fannkuch, scimark_lu, thrift, richards
Ignored benchmarks (5) of results/bm-20250306-3.14.0a5+-052cb71-JIT/bm-20250306-arminc-aarch64-python-052cb717f5f97d08d207-3.14.0a5+-052cb71.json: docutils, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 79.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x