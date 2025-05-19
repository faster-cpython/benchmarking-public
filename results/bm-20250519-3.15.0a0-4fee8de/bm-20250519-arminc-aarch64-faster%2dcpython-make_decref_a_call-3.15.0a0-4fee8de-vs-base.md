# Results vs. base

- fork: faster-cpython
- ref: make_decref_a_call
- machine: linux-aarch64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.060x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                                  | 319 ms: 1.05x slower                                                            |
| docutils       | 2.98 sec                                                                | 3.01 sec: 1.01x slower                                                          |
| html5lib       | 62.1 ms                                                                 | 63.7 ms: 1.03x slower                                                           |
| sphinx         | 1.16 sec                                                                | 1.18 sec: 1.02x slower                                                          |
| Geometric mean | (ref)                                                                   | 1.03x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|--------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none_tg | 376 ms                                                                  | 383 ms: 1.02x slower                                                            |
| async_tree_io      | 888 ms                                                                  | 907 ms: 1.02x slower                                                            |
| async_tree_io_tg   | 910 ms                                                                  | 938 ms: 1.03x slower                                                            |
| async_generators   | 456 ms                                                                  | 480 ms: 1.05x slower                                                            |
| Geometric mean     | (ref)                                                                   | 1.02x slower                                                                    |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 86.9 ms                                                                 | 88.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 236 ms                                                                  | 232 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): regex_effbot, regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|---------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_loads          | 35.2 us                                                                 | 36.0 us: 1.02x slower                                                           |
| json_dumps          | 13.4 ms                                                                 | 13.7 ms: 1.03x slower                                                           |
| xml_etree_generate  | 112 ms                                                                  | 116 ms: 1.04x slower                                                            |
| xml_etree_process   | 79.2 ms                                                                 | 82.8 ms: 1.04x slower                                                           |
| tomli_loads         | 2.43 sec                                                                | 2.56 sec: 1.05x slower                                                          |
| xml_etree_iterparse | 143 ms                                                                  | 152 ms: 1.06x slower                                                            |
| xml_etree_parse     | 179 ms                                                                  | 191 ms: 1.07x slower                                                            |
| Geometric mean      | (ref)                                                                   | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                                 | 8.70 ms: 1.01x slower                                                           |
| python_startup         | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                                           |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.0 ms                                                                 | 14.5 ms: 1.04x slower                                                           |
| django_template | 39.4 ms                                                                 | 42.5 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                                   | 1.04x slower                                                                    |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20250519-arminc-aarch64-python-605022aeb69ae19cae1c-3.15.0a0-605022a | bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| thrift                  | 194 ms                                                                  | 1.02 ms: 190.67x faster                                                         |
| coverage                | 559 ms                                                                  | 113 ms: 4.96x faster                                                            |
| create_gc_cycles        | 3.95 ms                                                                 | 3.80 ms: 1.04x faster                                                           |
| gc_traversal            | 7.17 ms                                                                 | 6.92 ms: 1.04x faster                                                           |
| shortest_path           | 611 ms                                                                  | 590 ms: 1.04x faster                                                            |
| connected_components    | 575 ms                                                                  | 561 ms: 1.03x faster                                                            |
| k_core                  | 2.89 sec                                                                | 2.83 sec: 1.02x faster                                                          |
| regex_dna               | 236 ms                                                                  | 232 ms: 1.02x faster                                                            |
| python_startup_no_site  | 8.64 ms                                                                 | 8.70 ms: 1.01x slower                                                           |
| deltablue               | 3.79 ms                                                                 | 3.82 ms: 1.01x slower                                                           |
| python_startup          | 15.1 ms                                                                 | 15.2 ms: 1.01x slower                                                           |
| docutils                | 2.98 sec                                                                | 3.01 sec: 1.01x slower                                                          |
| float                   | 86.9 ms                                                                 | 88.0 ms: 1.01x slower                                                           |
| bench_thread_pool       | 1.35 ms                                                                 | 1.37 ms: 1.01x slower                                                           |
| many_optionals          | 859 us                                                                  | 873 us: 1.02x slower                                                            |
| sphinx                  | 1.16 sec                                                                | 1.18 sec: 1.02x slower                                                          |
| async_tree_none_tg      | 376 ms                                                                  | 383 ms: 1.02x slower                                                            |
| async_tree_io           | 888 ms                                                                  | 907 ms: 1.02x slower                                                            |
| json_loads              | 35.2 us                                                                 | 36.0 us: 1.02x slower                                                           |
| logging_simple          | 7.68 us                                                                 | 7.88 us: 1.03x slower                                                           |
| html5lib                | 62.1 ms                                                                 | 63.7 ms: 1.03x slower                                                           |
| json_dumps              | 13.4 ms                                                                 | 13.7 ms: 1.03x slower                                                           |
| subparsers              | 28.4 ms                                                                 | 29.2 ms: 1.03x slower                                                           |
| logging_silent          | 612 ns                                                                  | 629 ns: 1.03x slower                                                            |
| async_tree_io_tg        | 910 ms                                                                  | 938 ms: 1.03x slower                                                            |
| hexiom                  | 6.98 ms                                                                 | 7.20 ms: 1.03x slower                                                           |
| pprint_safe_repr        | 915 ms                                                                  | 947 ms: 1.04x slower                                                            |
| mako                    | 14.0 ms                                                                 | 14.5 ms: 1.04x slower                                                           |
| deepcopy_memo           | 37.7 us                                                                 | 39.1 us: 1.04x slower                                                           |
| crypto_pyaes            | 84.7 ms                                                                 | 88.0 ms: 1.04x slower                                                           |
| pycparser               | 1.24 sec                                                                | 1.29 sec: 1.04x slower                                                          |
| xml_etree_generate      | 112 ms                                                                  | 116 ms: 1.04x slower                                                            |
| pprint_pformat          | 1.85 sec                                                                | 1.93 sec: 1.04x slower                                                          |
| nqueens                 | 100 ms                                                                  | 105 ms: 1.04x slower                                                            |
| xml_etree_process       | 79.2 ms                                                                 | 82.8 ms: 1.04x slower                                                           |
| sympy_expand            | 468 ms                                                                  | 489 ms: 1.05x slower                                                            |
| mdp                     | 1.65 sec                                                                | 1.73 sec: 1.05x slower                                                          |
| 2to3                    | 304 ms                                                                  | 319 ms: 1.05x slower                                                            |
| logging_format          | 8.37 us                                                                 | 8.79 us: 1.05x slower                                                           |
| async_generators        | 456 ms                                                                  | 480 ms: 1.05x slower                                                            |
| scimark_monte_carlo     | 80.2 ms                                                                 | 84.3 ms: 1.05x slower                                                           |
| sqlglot_v2_normalize    | 126 ms                                                                  | 133 ms: 1.05x slower                                                            |
| bpe_tokeniser           | 5.45 sec                                                                | 5.74 sec: 1.05x slower                                                          |
| pyflate                 | 532 ms                                                                  | 560 ms: 1.05x slower                                                            |
| tomli_loads             | 2.43 sec                                                                | 2.56 sec: 1.05x slower                                                          |
| telco                   | 9.39 ms                                                                 | 9.94 ms: 1.06x slower                                                           |
| comprehensions          | 21.2 us                                                                 | 22.5 us: 1.06x slower                                                           |
| sympy_sum               | 143 ms                                                                  | 152 ms: 1.06x slower                                                            |
| xml_etree_iterparse     | 143 ms                                                                  | 152 ms: 1.06x slower                                                            |
| xml_etree_parse         | 179 ms                                                                  | 191 ms: 1.07x slower                                                            |
| scimark_lu              | 146 ms                                                                  | 157 ms: 1.08x slower                                                            |
| sqlglot_v2_optimize     | 60.1 ms                                                                 | 64.9 ms: 1.08x slower                                                           |
| django_template         | 39.4 ms                                                                 | 42.5 ms: 1.08x slower                                                           |
| fannkuch                | 467 ms                                                                  | 510 ms: 1.09x slower                                                            |
| scimark_sparse_mat_mult | 7.00 ms                                                                 | 7.86 ms: 1.12x slower                                                           |
| bench_mp_pool           | 2.60 sec                                                                | 4.80 sec: 1.85x slower                                                          |
| Geometric mean          | (ref)                                                                   | 1.04x faster                                                                    |

Benchmark hidden because not significant (38): go, sqlite_synth, pathlib, nbody, richards, sympy_integrate, regex_effbot, dulwich_log, asyncio_websockets, pylint, async_tree_cpu_io_mixed, sympy_str, async_tree_memoization, deepcopy_reduce, async_tree_cpu_io_mixed_tg, regex_v8, async_tree_none, pidigits, async_tree_memoization_tg, richards_super, sqlglot_v2_parse, scimark_fft, generators, deepcopy, genshi_xml, unpickle_pure_python, json, coroutines, scimark_sor, spectral_norm, sqlglot_v2_transpile, chaos, genshi_text, typing_runtime_protocols, meteor_contest, regex_compile, raytrace, pickle_pure_python
Ignored benchmarks (1) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-arminc-aarch64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: djangocms

- Geometric mean (including insignificant results): 1.060x faster

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.99x