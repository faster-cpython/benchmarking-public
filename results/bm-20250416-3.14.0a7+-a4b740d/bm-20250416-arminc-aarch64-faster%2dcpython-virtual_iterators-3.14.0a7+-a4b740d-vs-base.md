# Results vs. base

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-aarch64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.003x faster
- HPT reliability: 98.03%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 292 ms                                                                   | 290 ms: 1.01x faster                                                            |
| docutils       | 2.97 sec                                                                 | 2.89 sec: 1.03x faster                                                          |
| html5lib       | 63.0 ms                                                                  | 62.2 ms: 1.01x faster                                                           |
| sphinx         | 1.15 sec                                                                 | 1.13 sec: 1.02x faster                                                          |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg       | 902 ms                                                                   | 886 ms: 1.02x faster                                                            |
| async_tree_memoization | 463 ms                                                                   | 457 ms: 1.01x faster                                                            |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (9): coroutines, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_generators, async_tree_io, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_compile, regex_effbot, regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads    | 2.39 sec                                                                 | 2.41 sec: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (8): pickle_pure_python, unpickle_pure_python, xml_etree_process, xml_etree_iterparse, xml_etree_parse, xml_etree_generate, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 13.9 ms                                                                  | 13.8 ms: 1.01x faster                                                           |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c | bm-20250416-arminc-aarch64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|--------------------------|:------------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 195 us                                                                   | 186 us: 1.05x faster                                                            |
| meteor_contest           | 113 ms                                                                   | 109 ms: 1.04x faster                                                            |
| pyflate                  | 553 ms                                                                   | 536 ms: 1.03x faster                                                            |
| gc_traversal             | 6.75 ms                                                                  | 6.54 ms: 1.03x faster                                                           |
| docutils                 | 2.97 sec                                                                 | 2.89 sec: 1.03x faster                                                          |
| sphinx                   | 1.15 sec                                                                 | 1.13 sec: 1.02x faster                                                          |
| async_tree_io_tg         | 902 ms                                                                   | 886 ms: 1.02x faster                                                            |
| async_tree_memoization   | 463 ms                                                                   | 457 ms: 1.01x faster                                                            |
| logging_simple           | 6.91 us                                                                  | 6.82 us: 1.01x faster                                                           |
| html5lib                 | 63.0 ms                                                                  | 62.2 ms: 1.01x faster                                                           |
| sqlite_synth             | 3.81 us                                                                  | 3.77 us: 1.01x faster                                                           |
| scimark_monte_carlo      | 78.5 ms                                                                  | 77.6 ms: 1.01x faster                                                           |
| mako                     | 13.9 ms                                                                  | 13.8 ms: 1.01x faster                                                           |
| 2to3                     | 292 ms                                                                   | 290 ms: 1.01x faster                                                            |
| tomli_loads              | 2.39 sec                                                                 | 2.41 sec: 1.01x slower                                                          |
| bpe_tokeniser            | 5.52 sec                                                                 | 5.57 sec: 1.01x slower                                                          |
| deltablue                | 3.80 ms                                                                  | 3.84 ms: 1.01x slower                                                           |
| spectral_norm            | 121 ms                                                                   | 127 ms: 1.05x slower                                                            |
| bench_mp_pool            | 2.58 sec                                                                 | 6.60 sec: 2.56x slower                                                          |
| Geometric mean           | (ref)                                                                    | 1.00x slower                                                                    |

Benchmark hidden because not significant (71): sqlglot_v2_normalize, comprehensions, genshi_xml, sqlglot_v2_optimize, coroutines, logging_format, pidigits, crypto_pyaes, sqlglot_v2_transpile, pickle_pure_python, hexiom, deepcopy_memo, many_optionals, chaos, sqlglot_v2_parse, dulwich_log, richards, generators, pycparser, genshi_text, k_core, deepcopy, regex_compile, regex_effbot, async_tree_cpu_io_mixed_tg, unpickle_pure_python, async_tree_none_tg, regex_dna, async_tree_none, subparsers, logging_silent, coverage, async_tree_cpu_io_mixed, telco, mdp, async_tree_memoization_tg, async_generators, async_tree_io, asyncio_websockets, scimark_fft, nbody, connected_components, float, bench_thread_pool, django_template, pathlib, python_startup_no_site, python_startup, shortest_path, fannkuch, json, pprint_safe_repr, xml_etree_process, xml_etree_iterparse, pprint_pformat, xml_etree_parse, scimark_sor, richards_super, go, nqueens, regex_v8, create_gc_cycles, xml_etree_generate, sqlalchemy_declarative, json_dumps, scimark_sparse_mat_mult, deepcopy_reduce, raytrace, json_loads, sqlalchemy_imperative, scimark_lu
Ignored benchmarks (5) of results/bm-20250414-3.14.0a7+-844596c/bm-20250414-arminc-aarch64-python-844596c09fc812a58ac1-3.14.0a7+-844596c.json: pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum

- Geometric mean (including insignificant results): 1.003x faster

# HPT report

- Reliability score: 98.03% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x