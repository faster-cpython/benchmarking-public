# Results vs. base

- fork: diegorusso
- ref: fplt
- machine: linux-aarch64
- commit hash: 707b019
- commit date: 2025-01-22
- overall geometric mean: 1.004x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4+-a16ded1 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 3.20 sec                                                                 | 3.25 sec: 1.01x slower                                       |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, coroutines, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_none_tg, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4+-a16ded1 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|----------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 124 ms                                                                   | 132 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                                    | 1.03x slower                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_compile, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4+-a16ded1 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|--------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads        | 2.60 sec                                                                 | 2.64 sec: 1.02x slower                                       |
| pickle_pure_python | 410 us                                                                   | 430 us: 1.05x slower                                         |
| Geometric mean     | (ref)                                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (7): json_dumps, xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, json_loads, xml_etree_generate, xml_etree_process

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20250122-arminc-aarch64-python-a16ded10ad3952406280-3.14.0a4+-a16ded1 | bm-20250122-arminc-aarch64-diegorusso-fplt-3.14.0a4+-707b019 |
|------------------------|:------------------------------------------------------------------------:|:------------------------------------------------------------:|
| deepcopy_reduce        | 4.24 us                                                                  | 4.05 us: 1.05x faster                                        |
| sqlalchemy_declarative | 154 ms                                                                   | 152 ms: 1.02x faster                                         |
| docutils               | 3.20 sec                                                                 | 3.25 sec: 1.01x slower                                       |
| tomli_loads            | 2.60 sec                                                                 | 2.64 sec: 1.02x slower                                       |
| scimark_sor            | 154 ms                                                                   | 159 ms: 1.03x slower                                         |
| bpe_tokeniser          | 5.76 sec                                                                 | 5.94 sec: 1.03x slower                                       |
| pprint_pformat         | 2.59 sec                                                                 | 2.69 sec: 1.04x slower                                       |
| spectral_norm          | 138 ms                                                                   | 144 ms: 1.04x slower                                         |
| pickle_pure_python     | 410 us                                                                   | 430 us: 1.05x slower                                         |
| pprint_safe_repr       | 1.28 sec                                                                 | 1.35 sec: 1.06x slower                                       |
| scimark_fft            | 430 ms                                                                   | 457 ms: 1.06x slower                                         |
| nbody                  | 124 ms                                                                   | 132 ms: 1.06x slower                                         |
| telco                  | 9.54 ms                                                                  | 10.2 ms: 1.07x slower                                        |
| scimark_monte_carlo    | 87.4 ms                                                                  | 94.8 ms: 1.09x slower                                        |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                 |

Benchmark hidden because not significant (82): deepcopy, go, sympy_sum, sqlite_synth, sqlalchemy_imperative, json_dumps, many_optionals, typing_runtime_protocols, crypto_pyaes, deltablue, richards, bench_thread_pool, async_tree_memoization_tg, pathlib, 2to3, meteor_contest, async_tree_memoization, k_core, sympy_integrate, xml_etree_parse, nqueens, deepcopy_memo, logging_format, shortest_path, raytrace, regex_v8, async_tree_io_tg, python_startup, async_tree_cpu_io_mixed_tg, async_tree_none, gc_traversal, sympy_str, async_tree_io, coroutines, genshi_text, async_tree_cpu_io_mixed, generators, sympy_expand, genshi_xml, python_startup_no_site, asyncio_websockets, sqlglot_transpile, thrift, connected_components, chaos, comprehensions, dulwich_log, sphinx, json, xml_etree_iterparse, pyflate, richards_super, async_tree_none_tg, sqlglot_optimize, sqlglot_normalize, mdp, create_gc_cycles, logging_simple, fannkuch, bench_mp_pool, pidigits, hexiom, regex_compile, scimark_sparse_mat_mult, unpickle_pure_python, coverage, float, async_generators, json_loads, django_template, pycparser, subparsers, xml_etree_generate, pylint, logging_silent, html5lib, xml_etree_process, regex_dna, sqlglot_parse, regex_effbot, scimark_lu, mako

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x