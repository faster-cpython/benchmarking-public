# Results vs. base

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.002x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg          | 1.20 sec                                                                 | 1.14 sec: 1.05x faster                                                 |
| async_tree_memoization_tg | 637 ms                                                                   | 616 ms: 1.03x faster                                                   |
| async_tree_io             | 1.21 sec                                                                 | 1.18 sec: 1.03x faster                                                 |
| Geometric mean            | (ref)                                                                    | 1.02x faster                                                           |

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_generators, async_tree_none, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_compile, regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_iterparse, json_loads, xml_etree_generate, xml_etree_parse, json_dumps, tomli_loads, unpickle_pure_python, xml_etree_process, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 65.0 ms                                                                  | 66.8 ms: 1.03x slower                                                  |
| Geometric mean  | (ref)                                                                    | 1.01x slower                                                           |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20250105-arminc-aarch64-python-2228e92da31ca7344a16-3.14.0a3+-2228e92 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|---------------------------|:------------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| sympy_str                 | 409 ms                                                                   | 381 ms: 1.07x faster                                                   |
| logging_silent            | 270 ns                                                                   | 255 ns: 1.06x faster                                                   |
| async_tree_io_tg          | 1.20 sec                                                                 | 1.14 sec: 1.05x faster                                                 |
| async_tree_memoization_tg | 637 ms                                                                   | 616 ms: 1.03x faster                                                   |
| async_tree_io             | 1.21 sec                                                                 | 1.18 sec: 1.03x faster                                                 |
| mypy2                     | 1.51 sec                                                                 | 1.48 sec: 1.02x faster                                                 |
| k_core                    | 3.32 sec                                                                 | 3.28 sec: 1.01x faster                                                 |
| bpe_tokeniser             | 8.00 sec                                                                 | 7.94 sec: 1.01x faster                                                 |
| django_template           | 65.0 ms                                                                  | 66.8 ms: 1.03x slower                                                  |
| sympy_expand              | 638 ms                                                                   | 674 ms: 1.06x slower                                                   |
| Geometric mean            | (ref)                                                                    | 1.00x faster                                                           |

Benchmark hidden because not significant (87): typing_runtime_protocols, regex_v8, json, hexiom, async_tree_none_tg, bench_mp_pool, async_tree_memoization, chaos, crypto_pyaes, xml_etree_iterparse, scimark_lu, html5lib, async_tree_cpu_io_mixed_tg, sqlglot_parse, pylint, json_loads, meteor_contest, scimark_sparse_mat_mult, pyflate, sqlglot_optimize, scimark_fft, nbody, sphinx, genshi_xml, shortest_path, async_tree_cpu_io_mixed, 2to3, comprehensions, python_startup, deepcopy_memo, async_generators, float, sqlglot_normalize, pycparser, sympy_integrate, raytrace, many_optionals, generators, scimark_sor, xml_etree_generate, connected_components, pprint_pformat, async_tree_none, telco, sqlalchemy_imperative, nqueens, python_startup_no_site, go, xml_etree_parse, deepcopy_reduce, deepcopy, pathlib, json_dumps, mako, sqlite_synth, regex_compile, fannkuch, coroutines, tomli_loads, docutils, richards, asyncio_websockets, pprint_safe_repr, mdp, scimark_monte_carlo, logging_simple, thrift, bench_thread_pool, unpickle_pure_python, subparsers, spectral_norm, xml_etree_process, gc_traversal, genshi_text, regex_effbot, sqlalchemy_declarative, create_gc_cycles, sympy_sum, deltablue, pickle_pure_python, logging_format, coverage, regex_dna, richards_super, pidigits, sqlglot_transpile, dulwich_log

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x