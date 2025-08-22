# Results vs. base

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-aarch64
- commit hash: efe4628
- commit date: 2025-08-22
- overall geometric mean: 1.004x faster
- HPT reliability: 96.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| html5lib       | 60.8 ms                                                                 | 61.7 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): 2to3, docutils, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 651 ms                                                                  | 644 ms: 1.01x faster                                                            |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                                    |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_io_tg, asyncio_websockets, async_tree_io, async_generators, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 125 ms                                                                  | 106 ms: 1.19x faster                                                            |
| float          | 81.8 ms                                                                 | 76.3 ms: 1.07x faster                                                           |
| Geometric mean | (ref)                                                                   | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 222 ms                                                                  | 226 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                                    |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|--------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads        | 2.31 sec                                                                | 2.24 sec: 1.03x faster                                                          |
| xml_etree_process  | 77.2 ms                                                                 | 76.3 ms: 1.01x faster                                                           |
| pickle_pure_python | 383 us                                                                  | 389 us: 1.01x slower                                                            |
| Geometric mean     | (ref)                                                                   | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                           |
| python_startup_no_site | 8.66 ms                                                                 | 8.61 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                                 | 27.0 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                    |

Benchmark hidden because not significant (3): django_template, mako, genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20250821-arminc-aarch64-python-a8d9d947843200a09c15-3.15.0a0-a8d9d94 | bm-20250822-arminc-aarch64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-efe4628 |
|----------------------------|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody                      | 125 ms                                                                  | 106 ms: 1.19x faster                                                            |
| float                      | 81.8 ms                                                                 | 76.3 ms: 1.07x faster                                                           |
| scimark_fft                | 407 ms                                                                  | 382 ms: 1.07x faster                                                            |
| hexiom                     | 7.43 ms                                                                 | 7.03 ms: 1.06x faster                                                           |
| shortest_path              | 605 ms                                                                  | 579 ms: 1.05x faster                                                            |
| spectral_norm              | 115 ms                                                                  | 111 ms: 1.04x faster                                                            |
| connected_components       | 578 ms                                                                  | 555 ms: 1.04x faster                                                            |
| tomli_loads                | 2.31 sec                                                                | 2.24 sec: 1.03x faster                                                          |
| k_core                     | 2.85 sec                                                                | 2.79 sec: 1.02x faster                                                          |
| sqlite_synth               | 3.71 us                                                                 | 3.65 us: 1.02x faster                                                           |
| bpe_tokeniser              | 5.35 sec                                                                | 5.28 sec: 1.01x faster                                                          |
| async_tree_cpu_io_mixed_tg | 651 ms                                                                  | 644 ms: 1.01x faster                                                            |
| xml_etree_process          | 77.2 ms                                                                 | 76.3 ms: 1.01x faster                                                           |
| python_startup             | 15.3 ms                                                                 | 15.1 ms: 1.01x faster                                                           |
| python_startup_no_site     | 8.66 ms                                                                 | 8.61 ms: 1.01x faster                                                           |
| html5lib                   | 60.8 ms                                                                 | 61.7 ms: 1.01x slower                                                           |
| genshi_text                | 26.6 ms                                                                 | 27.0 ms: 1.01x slower                                                           |
| pickle_pure_python         | 383 us                                                                  | 389 us: 1.01x slower                                                            |
| coverage                   | 102 ms                                                                  | 104 ms: 1.02x slower                                                            |
| regex_dna                  | 222 ms                                                                  | 226 ms: 1.02x slower                                                            |
| mdp                        | 1.63 sec                                                                | 1.66 sec: 1.02x slower                                                          |
| pprint_safe_repr           | 1.11 sec                                                                | 1.13 sec: 1.02x slower                                                          |
| subparsers                 | 47.4 ms                                                                 | 49.2 ms: 1.04x slower                                                           |
| pathlib                    | 21.8 ms                                                                 | 23.2 ms: 1.06x slower                                                           |
| Geometric mean             | (ref)                                                                   | 1.00x faster                                                                    |

Benchmark hidden because not significant (69): generators, regex_v8, sqlglot_v2_normalize, django_template, scimark_sparse_mat_mult, comprehensions, go, json, nqueens, async_tree_cpu_io_mixed, sqlglot_v2_parse, fannkuch, thrift, regex_compile, deepcopy_memo, async_tree_none_tg, async_tree_memoization, sympy_sum, 2to3, scimark_monte_carlo, pyflate, async_tree_memoization_tg, xml_etree_parse, logging_silent, mako, logging_simple, djangocms, xml_etree_iterparse, sphinx, async_tree_none, gc_traversal, pycparser, async_tree_io_tg, chaos, sympy_expand, deepcopy_reduce, telco, unpickle_pure_python, docutils, logging_format, asyncio_websockets, json_loads, sqlglot_v2_optimize, xml_etree_generate, richards_super, async_tree_io, deltablue, regex_effbot, pprint_pformat, async_generators, sympy_integrate, json_dumps, deepcopy, pidigits, coroutines, crypto_pyaes, richards, meteor_contest, sympy_str, sqlglot_v2_transpile, create_gc_cycles, raytrace, genshi_xml, scimark_sor, pylint, many_optionals, dulwich_log, scimark_lu, typing_runtime_protocols

- Geometric mean (including insignificant results): 1.004x faster

# HPT report

- Reliability score: 96.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x