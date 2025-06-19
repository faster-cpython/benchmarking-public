# Results vs. base

- fork: mdboom
- ref: faster_pprint_merge_
- machine: linux-x86_64
- commit hash: 28d3287
- commit date: 2025-06-18
- overall geometric mean: 1.001x faster
- HPT reliability: 92.46%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (11): async_generators, async_tree_memoization_tg, asyncio_websockets, async_tree_io_tg, async_tree_memoization, async_tree_cpu_io_mixed, coroutines, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): regex_dna, regex_effbot, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 259 us                                                                | 256 us: 1.01x faster                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (8): xml_etree_process, json_loads, xml_etree_parse, xml_etree_generate, json_dumps, pickle_pure_python, tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.40 ms                                                               | 7.39 ms: 1.00x faster                                                 |
| python_startup         | 13.2 ms                                                               | 13.2 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 40.8 ms                                                               | 41.0 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (3): genshi_text, mako, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python   | 259 us                                                                | 256 us: 1.01x faster                                                  |
| sympy_expand           | 541 ms                                                                | 535 ms: 1.01x faster                                                  |
| telco                  | 9.52 ms                                                               | 9.42 ms: 1.01x faster                                                 |
| regex_v8               | 24.2 ms                                                               | 23.9 ms: 1.01x faster                                                 |
| pprint_safe_repr       | 993 ms                                                                | 987 ms: 1.01x faster                                                  |
| richards_super         | 62.2 ms                                                               | 61.8 ms: 1.01x faster                                                 |
| spectral_norm          | 113 ms                                                                | 113 ms: 1.01x faster                                                  |
| pyflate                | 465 ms                                                                | 464 ms: 1.00x faster                                                  |
| dulwich_log            | 63.8 ms                                                               | 63.6 ms: 1.00x faster                                                 |
| thrift                 | 956 us                                                                | 954 us: 1.00x faster                                                  |
| fannkuch               | 479 ms                                                                | 478 ms: 1.00x faster                                                  |
| pprint_pformat         | 2.01 sec                                                              | 2.00 sec: 1.00x faster                                                |
| bpe_tokeniser          | 5.32 sec                                                              | 5.30 sec: 1.00x faster                                                |
| hexiom                 | 6.65 ms                                                               | 6.64 ms: 1.00x faster                                                 |
| python_startup_no_site | 7.40 ms                                                               | 7.39 ms: 1.00x faster                                                 |
| python_startup         | 13.2 ms                                                               | 13.2 ms: 1.00x faster                                                 |
| django_template        | 40.8 ms                                                               | 41.0 ms: 1.01x slower                                                 |
| connected_components   | 490 ms                                                                | 493 ms: 1.01x slower                                                  |
| scimark_monte_carlo    | 76.4 ms                                                               | 76.8 ms: 1.01x slower                                                 |
| nqueens                | 98.2 ms                                                               | 98.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (73): djangocms, genshi_text, sqlglot_v2_optimize, scimark_sparse_mat_mult, xml_etree_process, json_loads, logging_format, deltablue, chaos, sphinx, async_generators, deepcopy_memo, sqlglot_v2_normalize, xml_etree_parse, mdp, scimark_sor, subparsers, async_tree_memoization_tg, xml_etree_generate, go, regex_dna, pycparser, sqlglot_v2_transpile, shortest_path, sympy_sum, docutils, json_dumps, asyncio_websockets, async_tree_io_tg, coverage, many_optionals, async_tree_memoization, async_tree_cpu_io_mixed, pylint, sqlglot_v2_parse, regex_effbot, generators, pathlib, coroutines, nbody, gc_traversal, async_tree_io, logging_simple, raytrace, pidigits, crypto_pyaes, create_gc_cycles, 2to3, pickle_pure_python, meteor_contest, sympy_integrate, tomli_loads, async_tree_cpu_io_mixed_tg, html5lib, deepcopy, mako, genshi_xml, sympy_str, scimark_fft, async_tree_none, xml_etree_iterparse, float, typing_runtime_protocols, scimark_lu, deepcopy_reduce, comprehensions, async_tree_none_tg, regex_compile, logging_silent, json, sqlite_synth, k_core, richards
Ignored benchmarks (10) of results/bm-20250617-3.15.0a0-fba5dde/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 92.46% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x