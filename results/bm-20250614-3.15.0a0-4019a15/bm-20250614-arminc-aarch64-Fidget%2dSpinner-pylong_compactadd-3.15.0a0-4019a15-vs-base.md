# Results vs. base

- fork: Fidget-Spinner
- ref: pylong_compactadd
- machine: linux-aarch64
- commit hash: 4019a15
- commit date: 2025-06-14
- overall geometric mean: 1.000x slower
- HPT reliability: 67.75%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| docutils       | 2.89 sec                                                                | 2.94 sec: 1.02x slower                                                         |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                   |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_memoization, async_tree_io, async_tree_none_tg, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_none, async_tree_memoization_tg, async_generators

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 225 ms                                                                  | 220 ms: 1.02x faster                                                           |
| regex_v8       | 26.3 ms                                                                 | 27.7 ms: 1.05x slower                                                          |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                   |

Benchmark hidden because not significant (2): regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|--------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads        | 2.48 sec                                                                | 2.43 sec: 1.02x faster                                                         |
| pickle_pure_python | 383 us                                                                  | 379 us: 1.01x faster                                                           |
| json_dumps         | 13.5 ms                                                                 | 13.7 ms: 1.01x slower                                                          |
| Geometric mean     | (ref)                                                                   | 1.00x slower                                                                   |

Benchmark hidden because not significant (6): xml_etree_parse, xml_etree_process, xml_etree_iterparse, json_loads, xml_etree_generate, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup | 15.0 ms                                                                 | 15.1 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark            | bm-20250613-arminc-aarch64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 | bm-20250614-arminc-aarch64-Fidget%2dSpinner-pylong_compactadd-3.15.0a0-4019a15 |
|----------------------|:-----------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| pathlib              | 23.1 ms                                                                 | 22.1 ms: 1.05x faster                                                          |
| sympy_str            | 274 ms                                                                  | 262 ms: 1.05x faster                                                           |
| mdp                  | 1.69 sec                                                                | 1.62 sec: 1.04x faster                                                         |
| pprint_safe_repr     | 1.02 sec                                                                | 983 ms: 1.03x faster                                                           |
| pprint_pformat       | 2.07 sec                                                                | 2.02 sec: 1.03x faster                                                         |
| regex_dna            | 225 ms                                                                  | 220 ms: 1.02x faster                                                           |
| logging_format       | 8.27 us                                                                 | 8.10 us: 1.02x faster                                                          |
| tomli_loads          | 2.48 sec                                                                | 2.43 sec: 1.02x faster                                                         |
| connected_components | 565 ms                                                                  | 555 ms: 1.02x faster                                                           |
| pickle_pure_python   | 383 us                                                                  | 379 us: 1.01x faster                                                           |
| scimark_lu           | 148 ms                                                                  | 147 ms: 1.00x faster                                                           |
| python_startup       | 15.0 ms                                                                 | 15.1 ms: 1.01x slower                                                          |
| json_dumps           | 13.5 ms                                                                 | 13.7 ms: 1.01x slower                                                          |
| shortest_path        | 585 ms                                                                  | 595 ms: 1.02x slower                                                           |
| pyflate              | 525 ms                                                                  | 535 ms: 1.02x slower                                                           |
| docutils             | 2.89 sec                                                                | 2.94 sec: 1.02x slower                                                         |
| gc_traversal         | 6.86 ms                                                                 | 7.02 ms: 1.02x slower                                                          |
| regex_v8             | 26.3 ms                                                                 | 27.7 ms: 1.05x slower                                                          |
| dulwich_log          | 50.3 ms                                                                 | 53.2 ms: 1.06x slower                                                          |
| create_gc_cycles     | 3.71 ms                                                                 | 3.97 ms: 1.07x slower                                                          |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                                   |

Benchmark hidden because not significant (72): sqlglot_v2_transpile, nbody, richards_super, spectral_norm, chaos, meteor_contest, hexiom, nqueens, sqlglot_v2_normalize, regex_compile, xml_etree_parse, genshi_xml, many_optionals, k_core, sphinx, scimark_fft, sympy_integrate, scimark_sparse_mat_mult, async_tree_memoization, async_tree_io, scimark_sor, raytrace, logging_simple, 2to3, async_tree_none_tg, typing_runtime_protocols, asyncio_websockets, coverage, sqlglot_v2_parse, thrift, richards, xml_etree_process, sqlite_synth, coroutines, mako, bpe_tokeniser, sympy_sum, float, telco, generators, python_startup_no_site, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, subparsers, pylint, async_tree_io_tg, xml_etree_iterparse, genshi_text, deepcopy_memo, sympy_expand, logging_silent, comprehensions, go, async_tree_none, django_template, deepcopy_reduce, async_tree_memoization_tg, fannkuch, pycparser, async_generators, sqlglot_v2_optimize, json_loads, pidigits, deltablue, xml_etree_generate, unpickle_pure_python, crypto_pyaes, deepcopy, json, regex_effbot, html5lib, scimark_monte_carlo

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 67.75% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x