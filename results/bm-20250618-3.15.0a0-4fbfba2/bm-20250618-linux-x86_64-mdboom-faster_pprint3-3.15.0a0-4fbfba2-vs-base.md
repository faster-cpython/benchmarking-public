# Results vs. base

- fork: mdboom
- ref: faster_pprint3
- machine: linux-x86_64
- commit hash: 4fbfba2
- commit date: 2025-06-18
- overall geometric mean: 1.002x faster
- HPT reliability: 74.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_none, async_tree_cpu_io_mixed, async_generators, asyncio_websockets, async_tree_io, async_tree_memoization, coroutines, async_tree_none_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                               | 24.0 ms: 1.01x faster                                           |
| regex_compile  | 144 ms                                                                | 144 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 259 us                                                                | 257 us: 1.01x faster                                            |
| pickle_pure_python   | 374 us                                                                | 376 us: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                    |

Benchmark hidden because not significant (7): tomli_loads, xml_etree_generate, xml_etree_process, json_loads, xml_etree_iterparse, xml_etree_parse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 7.40 ms                                                               | 7.42 ms: 1.00x slower                                           |
| python_startup         | 13.2 ms                                                               | 13.2 ms: 1.00x slower                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, mako, genshi_xml, django_template

All benchmarks:
===============

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint3-3.15.0a0-4fbfba2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pprint_safe_repr       | 993 ms                                                                | 898 ms: 1.11x faster                                            |
| pprint_pformat         | 2.01 sec                                                              | 1.82 sec: 1.11x faster                                          |
| regex_v8               | 24.2 ms                                                               | 24.0 ms: 1.01x faster                                           |
| sqlite_synth           | 3.18 us                                                               | 3.16 us: 1.01x faster                                           |
| unpickle_pure_python   | 259 us                                                                | 257 us: 1.01x faster                                            |
| dulwich_log            | 63.8 ms                                                               | 63.5 ms: 1.00x faster                                           |
| chaos                  | 68.8 ms                                                               | 68.6 ms: 1.00x faster                                           |
| richards               | 54.3 ms                                                               | 54.2 ms: 1.00x faster                                           |
| sqlglot_v2_normalize   | 128 ms                                                                | 128 ms: 1.00x faster                                            |
| fannkuch               | 479 ms                                                                | 479 ms: 1.00x faster                                            |
| regex_compile          | 144 ms                                                                | 144 ms: 1.00x faster                                            |
| gc_traversal           | 5.14 ms                                                               | 5.14 ms: 1.00x slower                                           |
| python_startup_no_site | 7.40 ms                                                               | 7.42 ms: 1.00x slower                                           |
| python_startup         | 13.2 ms                                                               | 13.2 ms: 1.00x slower                                           |
| deepcopy               | 315 us                                                                | 316 us: 1.00x slower                                            |
| nqueens                | 98.2 ms                                                               | 98.6 ms: 1.00x slower                                           |
| scimark_lu             | 133 ms                                                                | 133 ms: 1.00x slower                                            |
| pickle_pure_python     | 374 us                                                                | 376 us: 1.01x slower                                            |
| connected_components   | 490 ms                                                                | 492 ms: 1.01x slower                                            |
| sympy_sum              | 166 ms                                                                | 167 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                    |

Benchmark hidden because not significant (73): scimark_sparse_mat_mult, sympy_expand, tomli_loads, logging_format, spectral_norm, richards_super, scimark_sor, async_tree_cpu_io_mixed_tg, pyflate, generators, deepcopy_memo, sqlglot_v2_parse, sphinx, subparsers, logging_silent, meteor_contest, crypto_pyaes, async_tree_memoization_tg, typing_runtime_protocols, logging_simple, scimark_fft, hexiom, genshi_text, xml_etree_generate, html5lib, async_tree_none, pycparser, async_tree_cpu_io_mixed, mdp, pylint, regex_effbot, nbody, shortest_path, deltablue, pidigits, comprehensions, sqlglot_v2_optimize, regex_dna, xml_etree_process, thrift, async_generators, asyncio_websockets, async_tree_io, mako, genshi_xml, 2to3, docutils, go, sympy_integrate, async_tree_memoization, bpe_tokeniser, pathlib, float, raytrace, many_optionals, sqlglot_v2_transpile, sympy_str, json, create_gc_cycles, json_loads, django_template, xml_etree_iterparse, xml_etree_parse, json_dumps, deepcopy_reduce, telco, coroutines, async_tree_none_tg, scimark_monte_carlo, async_tree_io_tg, k_core, coverage, djangocms
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.002x faster

# HPT report

- Reliability score: 74.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x