# Results vs. base

- fork: brandtbucher
- ref: warmup_side_4096
- machine: linux-aarch64
- commit hash: a8a4ed3
- commit date: 2024-11-22
- overall geometric mean: 1.014x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 348 ms                                                                   | 315 ms: 1.10x faster                                                       |
| docutils       | 3.52 sec                                                                 | 3.24 sec: 1.09x faster                                                     |
| sphinx         | 1.36 sec                                                                 | 1.30 sec: 1.05x faster                                                     |
| Geometric mean | (ref)                                                                    | 1.06x faster                                                               |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed, async_tree_io, async_tree_none_tg, asyncio_websockets, coroutines, async_tree_none, async_tree_io_tg, async_generators, async_tree_memoization, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|----------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 158 ms                                                                   | 141 ms: 1.13x faster                                                       |
| Geometric mean | (ref)                                                                    | 1.02x faster                                                               |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (9): xml_etree_iterparse, pickle_pure_python, json_loads, xml_etree_generate, tomli_loads, xml_etree_process, json_dumps, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark              | bm-20241122-arminc-aarch64-python-615abb99a4538520f380-3.14.0a2+-615abb9 | bm-20241122-arminc-aarch64-brandtbucher-warmup_side_4096-3.14.0a2+-a8a4ed3 |
|------------------------|:------------------------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile          | 158 ms                                                                   | 141 ms: 1.13x faster                                                       |
| 2to3                   | 348 ms                                                                   | 315 ms: 1.10x faster                                                       |
| go                     | 201 ms                                                                   | 183 ms: 1.10x faster                                                       |
| sympy_sum              | 175 ms                                                                   | 159 ms: 1.10x faster                                                       |
| sqlalchemy_imperative  | 18.5 ms                                                                  | 16.9 ms: 1.10x faster                                                      |
| fannkuch               | 539 ms                                                                   | 494 ms: 1.09x faster                                                       |
| docutils               | 3.52 sec                                                                 | 3.24 sec: 1.09x faster                                                     |
| sqlalchemy_declarative | 161 ms                                                                   | 148 ms: 1.09x faster                                                       |
| hexiom                 | 9.99 ms                                                                  | 9.22 ms: 1.08x faster                                                      |
| richards_super         | 62.9 ms                                                                  | 59.2 ms: 1.06x faster                                                      |
| sympy_str              | 319 ms                                                                   | 300 ms: 1.06x faster                                                       |
| pylint                 | 338 ms                                                                   | 318 ms: 1.06x faster                                                       |
| dulwich_log            | 78.5 ms                                                                  | 74.1 ms: 1.06x faster                                                      |
| sympy_expand           | 545 ms                                                                   | 516 ms: 1.06x faster                                                       |
| pycparser              | 1.53 sec                                                                 | 1.46 sec: 1.05x faster                                                     |
| sphinx                 | 1.36 sec                                                                 | 1.30 sec: 1.05x faster                                                     |
| djangocms              | 67.4 us                                                                  | 65.7 us: 1.03x faster                                                      |
| bpe_tokeniser          | 6.03 sec                                                                 | 5.89 sec: 1.02x faster                                                     |
| sqlglot_normalize      | 144 ms                                                                   | 141 ms: 1.02x faster                                                       |
| bench_mp_pool          | 1.47 sec                                                                 | 2.26 sec: 1.54x slower                                                     |
| Geometric mean         | (ref)                                                                    | 1.01x faster                                                               |

Benchmark hidden because not significant (77): sqlglot_optimize, crypto_pyaes, deepcopy_reduce, scimark_monte_carlo, typing_runtime_protocols, sqlglot_transpile, deepcopy_memo, deltablue, xml_etree_iterparse, sqlglot_parse, subparsers, pathlib, sympy_integrate, many_optionals, gc_traversal, scimark_lu, deepcopy, chaos, async_tree_cpu_io_mixed, pickle_pure_python, genshi_text, richards, pyflate, html5lib, scimark_sor, genshi_xml, logging_format, json_loads, pprint_pformat, spectral_norm, xml_etree_generate, tomli_loads, async_tree_io, django_template, pidigits, async_tree_none_tg, xml_etree_process, python_startup_no_site, asyncio_websockets, k_core, coroutines, python_startup, async_tree_none, async_tree_io_tg, async_generators, raytrace, connected_components, mdp, async_tree_memoization, async_tree_memoization_tg, shortest_path, regex_dna, json_dumps, scimark_sparse_mat_mult, nqueens, create_gc_cycles, nbody, json, scimark_fft, thrift, float, telco, regex_effbot, mako, comprehensions, logging_silent, regex_v8, async_tree_cpu_io_mixed_tg, pprint_safe_repr, bench_thread_pool, coverage, sqlite_synth, meteor_contest, logging_simple, xml_etree_parse, generators, unpickle_pure_python

- Geometric mean (including insignificant results): 1.014x faster
# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x