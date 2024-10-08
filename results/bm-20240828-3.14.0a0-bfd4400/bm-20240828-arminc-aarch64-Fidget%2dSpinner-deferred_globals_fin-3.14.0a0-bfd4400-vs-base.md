# Results vs. base

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-aarch64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.00x faster
- HPT reliability: 99.70%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| asyncio_tcp     | 581 ms                                                                  | 562 ms: 1.03x faster                                                              |
| asyncio_tcp_ssl | 2.23 sec                                                                | 2.18 sec: 1.02x faster                                                            |
| Geometric mean  | (ref)                                                                   | 1.01x faster                                                                      |

Benchmark hidden because not significant (11): async_tree_io, asyncio_websockets, async_tree_cpu_io_mixed, coroutines, async_tree_io_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_generators, async_tree_memoization_tg, async_tree_none, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 92.5 ms                                                                 | 94.6 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                                      |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 247 ms                                                                  | 253 ms: 1.03x slower                                                              |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 255 us                                                                  | 250 us: 1.02x faster                                                              |
| pickle_pure_python   | 357 us                                                                  | 351 us: 1.02x faster                                                              |
| Geometric mean       | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (7): json_dumps, json_loads, xml_etree_process, xml_etree_iterparse, tomli_loads, xml_etree_generate, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.1 ms                                                                 | 12.9 ms: 1.01x faster                                                             |
| python_startup_no_site | 8.78 ms                                                                 | 8.75 ms: 1.00x faster                                                             |
| Geometric mean         | (ref)                                                                   | 1.01x faster                                                                      |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, genshi_text, mako

All benchmarks:
===============

| Benchmark                | bm-20240815-arminc-aarch64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c | bm-20240828-arminc-aarch64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|--------------------------|:-----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| gc_traversal             | 5.05 ms                                                                 | 4.85 ms: 1.04x faster                                                             |
| asyncio_tcp              | 581 ms                                                                  | 562 ms: 1.03x faster                                                              |
| richards_super           | 60.6 ms                                                                 | 58.6 ms: 1.03x faster                                                             |
| pprint_pformat           | 1.93 sec                                                                | 1.88 sec: 1.03x faster                                                            |
| hexiom                   | 7.07 ms                                                                 | 6.91 ms: 1.02x faster                                                             |
| thrift                   | 975 us                                                                  | 956 us: 1.02x faster                                                              |
| pprint_safe_repr         | 934 ms                                                                  | 916 ms: 1.02x faster                                                              |
| asyncio_tcp_ssl          | 2.23 sec                                                                | 2.18 sec: 1.02x faster                                                            |
| pathlib                  | 21.5 ms                                                                 | 21.1 ms: 1.02x faster                                                             |
| unpickle_pure_python     | 255 us                                                                  | 250 us: 1.02x faster                                                              |
| pickle_pure_python       | 357 us                                                                  | 351 us: 1.02x faster                                                              |
| richards                 | 53.4 ms                                                                 | 52.5 ms: 1.02x faster                                                             |
| typing_runtime_protocols | 201 us                                                                  | 198 us: 1.02x faster                                                              |
| python_startup           | 13.1 ms                                                                 | 12.9 ms: 1.01x faster                                                             |
| python_startup_no_site   | 8.78 ms                                                                 | 8.75 ms: 1.00x faster                                                             |
| mdp                      | 3.31 sec                                                                | 3.33 sec: 1.00x slower                                                            |
| nqueens                  | 99.2 ms                                                                 | 100 ms: 1.01x slower                                                              |
| telco                    | 9.88 ms                                                                 | 10.1 ms: 1.02x slower                                                             |
| fannkuch                 | 463 ms                                                                  | 471 ms: 1.02x slower                                                              |
| bpe_tokeniser            | 5.83 sec                                                                | 5.94 sec: 1.02x slower                                                            |
| pyflate                  | 566 ms                                                                  | 579 ms: 1.02x slower                                                              |
| float                    | 92.5 ms                                                                 | 94.6 ms: 1.02x slower                                                             |
| regex_dna                | 247 ms                                                                  | 253 ms: 1.03x slower                                                              |
| Geometric mean           | (ref)                                                                   | 1.00x faster                                                                      |

Benchmark hidden because not significant (66): html5lib, async_tree_io, tornado_http, sympy_sum, sqlglot_normalize, json_dumps, regex_v8, sqlglot_transpile, deepcopy_memo, scimark_sor, asyncio_websockets, genshi_xml, async_tree_cpu_io_mixed, crypto_pyaes, nbody, comprehensions, 2to3, coroutines, meteor_contest, bench_mp_pool, raytrace, async_tree_io_tg, django_template, pycparser, go, sympy_integrate, pylint, logging_silent, deepcopy, scimark_monte_carlo, sympy_str, create_gc_cycles, chaos, spectral_norm, scimark_fft, json, async_tree_none_tg, async_tree_cpu_io_mixed_tg, scimark_lu, async_generators, generators, regex_compile, json_loads, async_tree_memoization_tg, xml_etree_process, pidigits, regex_effbot, bench_thread_pool, scimark_sparse_mat_mult, xml_etree_iterparse, sympy_expand, tomli_loads, logging_format, genshi_text, logging_simple, docutils, sqlglot_optimize, async_tree_none, coverage, deepcopy_reduce, async_tree_memoization, deltablue, sqlglot_parse, xml_etree_generate, xml_etree_parse, mako

# HPT report

- Reliability score: 99.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x