# Results vs. base

- fork: python
- ref: v3.14.0a5
- machine: linux-aarch64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.001x slower
- HPT reliability: 95.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed, async_tree_none, asyncio_websockets, coroutines, async_generators, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.91 ms                                                                  | 4.10 ms: 1.05x slower                                        |
| regex_dna      | 244 ms                                                                   | 262 ms: 1.07x slower                                         |
| Geometric mean | (ref)                                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads     | 2.54 sec                                                                 | 2.48 sec: 1.02x faster                                       |
| xml_etree_parse | 179 ms                                                                   | 188 ms: 1.05x slower                                         |
| Geometric mean  | (ref)                                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (7): xml_etree_process, json_loads, json_dumps, xml_etree_iterparse, unpickle_pure_python, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark             | bm-20250212-arminc-aarch64-python-5cdd6e5e758a3fc0a5da-3.14.0a4+-5cdd6e5 | bm-20250211-arminc-aarch64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads           | 2.54 sec                                                                 | 2.48 sec: 1.02x faster                                       |
| pprint_pformat        | 2.78 sec                                                                 | 2.72 sec: 1.02x faster                                       |
| sqlalchemy_imperative | 16.0 ms                                                                  | 15.6 ms: 1.02x faster                                        |
| sympy_sum             | 152 ms                                                                   | 149 ms: 1.02x faster                                         |
| bpe_tokeniser         | 5.70 sec                                                                 | 5.76 sec: 1.01x slower                                       |
| regex_effbot          | 3.91 ms                                                                  | 4.10 ms: 1.05x slower                                        |
| xml_etree_parse       | 179 ms                                                                   | 188 ms: 1.05x slower                                         |
| pathlib               | 21.5 ms                                                                  | 22.7 ms: 1.05x slower                                        |
| regex_dna             | 244 ms                                                                   | 262 ms: 1.07x slower                                         |
| Geometric mean        | (ref)                                                                    | 1.00x slower                                                 |

Benchmark hidden because not significant (87): telco, nqueens, gc_traversal, sqlglot_normalize, many_optionals, nbody, thrift, regex_compile, sympy_integrate, logging_simple, xml_etree_process, sqlglot_parse, async_tree_memoization_tg, pprint_safe_repr, go, crypto_pyaes, json_loads, scimark_monte_carlo, coverage, logging_format, async_tree_io_tg, json_dumps, sympy_expand, typing_runtime_protocols, k_core, json, html5lib, sqlglot_transpile, connected_components, scimark_sparse_mat_mult, scimark_fft, django_template, sqlalchemy_declarative, genshi_xml, hexiom, async_tree_cpu_io_mixed_tg, comprehensions, async_tree_memoization, logging_silent, async_tree_io, xml_etree_iterparse, deepcopy_memo, chaos, bench_thread_pool, pycparser, python_startup_no_site, async_tree_cpu_io_mixed, deepcopy, deltablue, async_tree_none, sympy_str, pidigits, docutils, spectral_norm, asyncio_websockets, shortest_path, unpickle_pure_python, python_startup, create_gc_cycles, coroutines, mako, raytrace, async_generators, 2to3, mdp, richards, sphinx, pyflate, async_tree_none_tg, generators, sqlglot_optimize, pylint, scimark_sor, fannkuch, richards_super, dulwich_log, float, meteor_contest, xml_etree_generate, deepcopy_reduce, pickle_pure_python, sqlite_synth, scimark_lu, genshi_text, subparsers, regex_v8, bench_mp_pool

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 95.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x