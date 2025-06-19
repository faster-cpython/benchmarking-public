# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.005x faster
- HPT reliability: 77.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization | 472 ms                                                                  | 476 ms: 1.01x slower                                                            |
| async_tree_io          | 899 ms                                                                  | 910 ms: 1.01x slower                                                            |
| async_tree_io_tg       | 918 ms                                                                  | 933 ms: 1.02x slower                                                            |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (8): asyncio_websockets, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_generators, async_tree_none_tg, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 125 ms                                                                  | 105 ms: 1.19x faster                                                            |
| float          | 83.4 ms                                                                 | 77.3 ms: 1.08x faster                                                           |
| Geometric mean | (ref)                                                                   | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                  | 216 ms: 1.04x faster                                                            |
| Geometric mean | (ref)                                                                   | 1.02x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|---------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python  | 405 us                                                                  | 391 us: 1.04x faster                                                            |
| xml_etree_process   | 78.8 ms                                                                 | 77.2 ms: 1.02x faster                                                           |
| tomli_loads         | 2.32 sec                                                                | 2.29 sec: 1.01x faster                                                          |
| xml_etree_iterparse | 144 ms                                                                  | 142 ms: 1.01x faster                                                            |
| Geometric mean      | (ref)                                                                   | 1.01x faster                                                                    |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_generate, json_loads, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 8.69 ms                                                                 | 8.58 ms: 1.01x faster                                                           |
| python_startup         | 15.2 ms                                                                 | 15.0 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark              | bm-20250619-arminc-aarch64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 | bm-20250619-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                  | 125 ms                                                                  | 105 ms: 1.19x faster                                                            |
| float                  | 83.4 ms                                                                 | 77.3 ms: 1.08x faster                                                           |
| dulwich_log            | 56.5 ms                                                                 | 53.9 ms: 1.05x faster                                                           |
| pyflate                | 542 ms                                                                  | 522 ms: 1.04x faster                                                            |
| regex_dna              | 225 ms                                                                  | 216 ms: 1.04x faster                                                            |
| deltablue              | 3.87 ms                                                                 | 3.73 ms: 1.04x faster                                                           |
| pickle_pure_python     | 405 us                                                                  | 391 us: 1.04x faster                                                            |
| create_gc_cycles       | 3.82 ms                                                                 | 3.69 ms: 1.03x faster                                                           |
| scimark_fft            | 405 ms                                                                  | 391 ms: 1.03x faster                                                            |
| shortest_path          | 591 ms                                                                  | 575 ms: 1.03x faster                                                            |
| generators             | 36.0 ms                                                                 | 35.2 ms: 1.02x faster                                                           |
| connected_components   | 566 ms                                                                  | 554 ms: 1.02x faster                                                            |
| xml_etree_process      | 78.8 ms                                                                 | 77.2 ms: 1.02x faster                                                           |
| bpe_tokeniser          | 5.39 sec                                                                | 5.31 sec: 1.01x faster                                                          |
| python_startup_no_site | 8.69 ms                                                                 | 8.58 ms: 1.01x faster                                                           |
| tomli_loads            | 2.32 sec                                                                | 2.29 sec: 1.01x faster                                                          |
| python_startup         | 15.2 ms                                                                 | 15.0 ms: 1.01x faster                                                           |
| xml_etree_iterparse    | 144 ms                                                                  | 142 ms: 1.01x faster                                                            |
| meteor_contest         | 113 ms                                                                  | 113 ms: 1.01x faster                                                            |
| async_tree_memoization | 472 ms                                                                  | 476 ms: 1.01x slower                                                            |
| deepcopy_reduce        | 3.66 us                                                                 | 3.69 us: 1.01x slower                                                           |
| async_tree_io          | 899 ms                                                                  | 910 ms: 1.01x slower                                                            |
| pathlib                | 22.3 ms                                                                 | 22.6 ms: 1.01x slower                                                           |
| async_tree_io_tg       | 918 ms                                                                  | 933 ms: 1.02x slower                                                            |
| logging_simple         | 7.72 us                                                                 | 7.85 us: 1.02x slower                                                           |
| sqlglot_v2_normalize   | 128 ms                                                                  | 130 ms: 1.02x slower                                                            |
| many_optionals         | 814 us                                                                  | 846 us: 1.04x slower                                                            |
| thrift                 | 958 us                                                                  | 1.00 ms: 1.04x slower                                                           |
| sqlglot_v2_optimize    | 62.4 ms                                                                 | 66.1 ms: 1.06x slower                                                           |
| Geometric mean         | (ref)                                                                   | 1.00x faster                                                                    |

Benchmark hidden because not significant (64): scimark_monte_carlo, nqueens, logging_silent, sqlite_synth, spectral_norm, scimark_sparse_mat_mult, genshi_text, json, crypto_pyaes, typing_runtime_protocols, regex_v8, scimark_sor, sqlglot_v2_parse, deepcopy, raytrace, regex_effbot, sympy_integrate, richards, pprint_safe_repr, pprint_pformat, k_core, unpickle_pure_python, comprehensions, hexiom, 2to3, docutils, sympy_expand, xml_etree_generate, regex_compile, djangocms, json_loads, sqlglot_v2_transpile, pidigits, pycparser, xml_etree_parse, sympy_sum, sphinx, telco, asyncio_websockets, mdp, fannkuch, mako, async_tree_cpu_io_mixed, async_tree_none, go, genshi_xml, async_tree_cpu_io_mixed_tg, sympy_str, async_generators, richards_super, async_tree_none_tg, html5lib, async_tree_memoization_tg, chaos, gc_traversal, json_dumps, coverage, pylint, django_template, deepcopy_memo, logging_format, scimark_lu, coroutines, subparsers

- Geometric mean (including insignificant results): 1.005x faster

# HPT report

- Reliability score: 77.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x