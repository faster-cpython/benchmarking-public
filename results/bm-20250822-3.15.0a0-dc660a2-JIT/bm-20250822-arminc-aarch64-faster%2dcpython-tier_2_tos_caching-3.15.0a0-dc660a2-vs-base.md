# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.007x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 310 ms                                                                  | 307 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark      | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines     | 31.5 ms                                                                 | 29.9 ms: 1.06x faster                                                           |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_memoization, async_tree_io, async_tree_none_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed_tg, async_generators, async_tree_cpu_io_mixed, async_tree_io_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 127 ms                                                                  | 106 ms: 1.21x faster                                                            |
| float          | 81.3 ms                                                                 | 75.9 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                                   | 1.09x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 223 ms                                                                  | 218 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads       | 2.31 sec                                                                | 2.22 sec: 1.04x faster                                                          |
| xml_etree_process | 76.7 ms                                                                 | 75.8 ms: 1.01x faster                                                           |
| Geometric mean    | (ref)                                                                   | 1.01x faster                                                                    |

Benchmark hidden because not significant (7): unpickle_pure_python, json_dumps, json_loads, xml_etree_iterparse, xml_etree_parse, pickle_pure_python, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml     | 62.1 ms                                                                 | 62.8 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                    |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark            | bm-20250822-arminc-aarch64-python-f278afcabf1a1c4162a0-3.15.0a0-f278afc | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                | 127 ms                                                                  | 106 ms: 1.21x faster                                                            |
| float                | 81.3 ms                                                                 | 75.9 ms: 1.07x faster                                                           |
| pyflate              | 535 ms                                                                  | 506 ms: 1.06x faster                                                            |
| coroutines           | 31.5 ms                                                                 | 29.9 ms: 1.06x faster                                                           |
| scimark_fft          | 409 ms                                                                  | 390 ms: 1.05x faster                                                            |
| tomli_loads          | 2.31 sec                                                                | 2.22 sec: 1.04x faster                                                          |
| chaos                | 68.8 ms                                                                 | 66.5 ms: 1.03x faster                                                           |
| deltablue            | 3.80 ms                                                                 | 3.68 ms: 1.03x faster                                                           |
| json                 | 5.82 ms                                                                 | 5.63 ms: 1.03x faster                                                           |
| richards             | 43.0 ms                                                                 | 41.7 ms: 1.03x faster                                                           |
| regex_dna            | 223 ms                                                                  | 218 ms: 1.03x faster                                                            |
| shortest_path        | 596 ms                                                                  | 580 ms: 1.03x faster                                                            |
| pprint_pformat       | 2.30 sec                                                                | 2.25 sec: 1.02x faster                                                          |
| create_gc_cycles     | 3.81 ms                                                                 | 3.73 ms: 1.02x faster                                                           |
| connected_components | 570 ms                                                                  | 559 ms: 1.02x faster                                                            |
| bpe_tokeniser        | 5.33 sec                                                                | 5.24 sec: 1.02x faster                                                          |
| xml_etree_process    | 76.7 ms                                                                 | 75.8 ms: 1.01x faster                                                           |
| logging_format       | 7.34 us                                                                 | 7.26 us: 1.01x faster                                                           |
| 2to3                 | 310 ms                                                                  | 307 ms: 1.01x faster                                                            |
| genshi_xml           | 62.1 ms                                                                 | 62.8 ms: 1.01x slower                                                           |
| subparsers           | 47.1 ms                                                                 | 47.8 ms: 1.01x slower                                                           |
| dulwich_log          | 52.5 ms                                                                 | 55.4 ms: 1.06x slower                                                           |
| Geometric mean       | (ref)                                                                   | 1.01x faster                                                                    |

Benchmark hidden because not significant (71): scimark_monte_carlo, scimark_sor, generators, sqlglot_v2_normalize, sympy_str, unpickle_pure_python, raytrace, spectral_norm, scimark_sparse_mat_mult, crypto_pyaes, pidigits, json_dumps, regex_v8, sqlglot_v2_optimize, json_loads, async_tree_memoization, deepcopy_reduce, mdp, hexiom, async_tree_io, go, sqlglot_v2_transpile, xml_etree_iterparse, sqlite_synth, sympy_sum, async_tree_none_tg, richards_super, async_tree_memoization_tg, sympy_integrate, k_core, async_tree_none, pycparser, python_startup, pathlib, pprint_safe_repr, sympy_expand, async_tree_cpu_io_mixed_tg, async_generators, sqlglot_v2_parse, djangocms, mako, django_template, async_tree_cpu_io_mixed, gc_traversal, pylint, xml_etree_parse, docutils, nqueens, comprehensions, regex_compile, scimark_lu, deepcopy, python_startup_no_site, coverage, regex_effbot, async_tree_io_tg, pickle_pure_python, sphinx, fannkuch, asyncio_websockets, html5lib, xml_etree_generate, logging_silent, telco, logging_simple, deepcopy_memo, meteor_contest, genshi_text, many_optionals, thrift, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.007x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x