# Results vs. base

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: linux-aarch64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.025x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|----------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| docutils       | 3.05 sec                                                                                                            | 3.19 sec: 1.05x slower                                                                                                  |
| html5lib       | 64.6 ms                                                                                                             | 71.4 ms: 1.11x slower                                                                                                   |
| Geometric mean | (ref)                                                                                                               | 1.05x slower                                                                                                            |

Benchmark hidden because not significant (2): 2to3, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| async_generators | 459 ms                                                                                                              | 491 ms: 1.07x slower                                                                                                    |
| Geometric mean   | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (12): asyncio_websockets, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_io_tg, asyncio_tcp_ssl, async_tree_cpu_io_mixed, asyncio_tcp, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_memoization, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, pidigits, nbody

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_effbot, regex_v8, regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

Benchmark hidden because not significant (14): xml_etree_generate, unpickle_list, xml_etree_process, tomli_loads, pickle_dict, pickle_list, json_dumps, xml_etree_iterparse, pickle, unpickle, json_loads, pickle_pure_python, xml_etree_parse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark               | results/bm-20250222-3.14.0a5+-5ec4bf8/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json | results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-arminc-aarch64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json |
|-------------------------|:-------------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| bench_mp_pool           | 7.33 sec                                                                                                            | 2.23 sec: 3.29x faster                                                                                                  |
| unpack_sequence         | 72.2 ns                                                                                                             | 62.8 ns: 1.15x faster                                                                                                   |
| k_core                  | 2.92 sec                                                                                                            | 2.97 sec: 1.02x slower                                                                                                  |
| bpe_tokeniser           | 5.77 sec                                                                                                            | 5.91 sec: 1.02x slower                                                                                                  |
| pyflate                 | 564 ms                                                                                                              | 584 ms: 1.04x slower                                                                                                    |
| sqlglot_normalize       | 128 ms                                                                                                              | 132 ms: 1.04x slower                                                                                                    |
| docutils                | 3.05 sec                                                                                                            | 3.19 sec: 1.05x slower                                                                                                  |
| meteor_contest          | 120 ms                                                                                                              | 127 ms: 1.06x slower                                                                                                    |
| sqlalchemy_imperative   | 15.2 ms                                                                                                             | 16.2 ms: 1.07x slower                                                                                                   |
| async_generators        | 459 ms                                                                                                              | 491 ms: 1.07x slower                                                                                                    |
| dulwich_log             | 60.3 ms                                                                                                             | 64.7 ms: 1.07x slower                                                                                                   |
| sympy_expand            | 474 ms                                                                                                              | 511 ms: 1.08x slower                                                                                                    |
| sqlglot_transpile       | 1.79 ms                                                                                                             | 1.93 ms: 1.08x slower                                                                                                   |
| nqueens                 | 104 ms                                                                                                              | 112 ms: 1.08x slower                                                                                                    |
| html5lib                | 64.6 ms                                                                                                             | 71.4 ms: 1.11x slower                                                                                                   |
| scimark_sparse_mat_mult | 6.32 ms                                                                                                             | 7.00 ms: 1.11x slower                                                                                                   |
| fannkuch                | 494 ms                                                                                                              | 549 ms: 1.11x slower                                                                                                    |
| pylint                  | 304 ms                                                                                                              | 338 ms: 1.11x slower                                                                                                    |
| sqlglot_parse           | 1.44 ms                                                                                                             | 1.61 ms: 1.12x slower                                                                                                   |
| hexiom                  | 7.49 ms                                                                                                             | 8.41 ms: 1.12x slower                                                                                                   |
| pycparser               | 1.30 sec                                                                                                            | 1.47 sec: 1.14x slower                                                                                                  |
| comprehensions          | 21.5 us                                                                                                             | 24.8 us: 1.16x slower                                                                                                   |
| go                      | 142 ms                                                                                                              | 165 ms: 1.16x slower                                                                                                    |
| crypto_pyaes            | 86.7 ms                                                                                                             | 102 ms: 1.18x slower                                                                                                    |
| pprint_safe_repr        | 978 ms                                                                                                              | 1.27 sec: 1.30x slower                                                                                                  |
| pprint_pformat          | 2.03 sec                                                                                                            | 2.66 sec: 1.31x slower                                                                                                  |
| Geometric mean          | (ref)                                                                                                               | 1.02x slower                                                                                                            |

Benchmark hidden because not significant (78): spectral_norm, sqlite_synth, gc_traversal, deepcopy_reduce, create_gc_cycles, regex_effbot, deepcopy_memo, json, xml_etree_generate, thrift, unpickle_list, scimark_sor, richards, generators, genshi_xml, deepcopy, xml_etree_process, tomli_loads, python_startup, pickle_dict, richards_super, logging_simple, python_startup_no_site, regex_v8, shortest_path, pickle_list, asyncio_websockets, json_dumps, raytrace, async_tree_none_tg, mdp, django_template, genshi_text, xml_etree_iterparse, async_tree_io, async_tree_memoization_tg, telco, bench_thread_pool, async_tree_io_tg, float, asyncio_tcp_ssl, logging_format, subparsers, pickle, regex_dna, async_tree_cpu_io_mixed, pathlib, scimark_fft, pidigits, connected_components, unpickle, asyncio_tcp, json_loads, async_tree_cpu_io_mixed_tg, mako, pickle_pure_python, sqlalchemy_declarative, sympy_str, xml_etree_parse, scimark_monte_carlo, sphinx, sqlglot_optimize, many_optionals, chaos, 2to3, async_tree_none, sympy_integrate, async_tree_memoization, scimark_lu, coverage, regex_compile, typing_runtime_protocols, sympy_sum, logging_silent, coroutines, unpickle_pure_python, nbody, deltablue

- Geometric mean (including insignificant results): 1.025x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.01x