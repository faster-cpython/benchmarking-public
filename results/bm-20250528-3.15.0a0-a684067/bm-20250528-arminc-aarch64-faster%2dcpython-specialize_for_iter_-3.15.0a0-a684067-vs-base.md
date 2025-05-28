# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: a684067
- commit date: 2025-05-28
- overall geometric mean: 1.002x slower
- HPT reliability: 68.47%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|--------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_generators   | 466 ms                                                                  | 450 ms: 1.03x faster                                                              |
| async_tree_none    | 393 ms                                                                  | 387 ms: 1.01x faster                                                              |
| async_tree_io_tg   | 914 ms                                                                  | 904 ms: 1.01x faster                                                              |
| async_tree_none_tg | 376 ms                                                                  | 372 ms: 1.01x faster                                                              |
| Geometric mean     | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

Benchmark hidden because not significant (4): regex_v8, regex_dna, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|---------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse | 142 ms                                                                  | 143 ms: 1.01x slower                                                              |
| json_dumps          | 13.6 ms                                                                 | 13.9 ms: 1.02x slower                                                             |
| Geometric mean      | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (7): xml_etree_process, xml_etree_generate, tomli_loads, json_loads, pickle_pure_python, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako           | 13.8 ms                                                                 | 14.0 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20250527-arminc-aarch64-python-f6f4e8a6622d55664179-3.15.0a0-f6f4e8a | bm-20250528-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-a684067 |
|--------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| bench_mp_pool            | 5.14 sec                                                                | 2.26 sec: 2.28x faster                                                            |
| async_generators         | 466 ms                                                                  | 450 ms: 1.03x faster                                                              |
| bpe_tokeniser            | 5.58 sec                                                                | 5.40 sec: 1.03x faster                                                            |
| pprint_safe_repr         | 1.00 sec                                                                | 985 ms: 1.02x faster                                                              |
| async_tree_none          | 393 ms                                                                  | 387 ms: 1.01x faster                                                              |
| pprint_pformat           | 2.04 sec                                                                | 2.02 sec: 1.01x faster                                                            |
| async_tree_io_tg         | 914 ms                                                                  | 904 ms: 1.01x faster                                                              |
| async_tree_none_tg       | 376 ms                                                                  | 372 ms: 1.01x faster                                                              |
| richards                 | 51.5 ms                                                                 | 51.1 ms: 1.01x faster                                                             |
| subparsers               | 28.3 ms                                                                 | 28.5 ms: 1.01x slower                                                             |
| xml_etree_iterparse      | 142 ms                                                                  | 143 ms: 1.01x slower                                                              |
| meteor_contest           | 111 ms                                                                  | 112 ms: 1.01x slower                                                              |
| logging_format           | 8.29 us                                                                 | 8.41 us: 1.01x slower                                                             |
| connected_components     | 554 ms                                                                  | 562 ms: 1.02x slower                                                              |
| mako                     | 13.8 ms                                                                 | 14.0 ms: 1.02x slower                                                             |
| json_dumps               | 13.6 ms                                                                 | 13.9 ms: 1.02x slower                                                             |
| create_gc_cycles         | 3.68 ms                                                                 | 3.78 ms: 1.03x slower                                                             |
| pyflate                  | 525 ms                                                                  | 541 ms: 1.03x slower                                                              |
| gc_traversal             | 6.72 ms                                                                 | 6.97 ms: 1.04x slower                                                             |
| pathlib                  | 22.0 ms                                                                 | 23.0 ms: 1.05x slower                                                             |
| mdp                      | 1.63 sec                                                                | 1.71 sec: 1.05x slower                                                            |
| typing_runtime_protocols | 191 us                                                                  | 202 us: 1.06x slower                                                              |
| Geometric mean           | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (72): sympy_sum, richards_super, crypto_pyaes, logging_silent, scimark_sor, xml_etree_process, chaos, scimark_sparse_mat_mult, nbody, sqlglot_v2_transpile, dulwich_log, genshi_xml, nqueens, go, async_tree_memoization_tg, sphinx, xml_etree_generate, fannkuch, sympy_expand, async_tree_memoization, regex_v8, sqlite_synth, async_tree_cpu_io_mixed, spectral_norm, telco, raytrace, many_optionals, coverage, asyncio_websockets, tomli_loads, generators, async_tree_cpu_io_mixed_tg, pylint, pidigits, deltablue, python_startup, regex_dna, logging_simple, genshi_text, shortest_path, json_loads, scimark_monte_carlo, python_startup_no_site, k_core, coroutines, deepcopy_reduce, docutils, sqlglot_v2_parse, async_tree_io, thrift, pycparser, float, deepcopy, sympy_integrate, django_template, deepcopy_memo, pickle_pure_python, scimark_fft, unpickle_pure_python, scimark_lu, html5lib, json, bench_thread_pool, hexiom, sqlglot_v2_optimize, regex_compile, 2to3, sqlglot_v2_normalize, xml_etree_parse, comprehensions, regex_effbot, sympy_str

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 68.47% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x