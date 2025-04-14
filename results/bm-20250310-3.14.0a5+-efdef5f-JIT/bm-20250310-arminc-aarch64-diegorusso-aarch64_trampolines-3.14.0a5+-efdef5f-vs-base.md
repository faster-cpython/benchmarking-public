# Results vs. base

- fork: diegorusso
- ref: aarch64_trampolines
- machine: linux-aarch64
- commit hash: efdef5f
- commit date: 2025-03-10
- overall geometric mean: 1.004x slower
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark              | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none_tg     | 373 ms                                                                   | 370 ms: 1.01x faster                                                        |
| async_tree_memoization | 468 ms                                                                   | 471 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                    | 1.00x slower                                                                |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_io_tg, asyncio_websockets, async_generators, async_tree_memoization_tg, coroutines

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 124 ms                                                                   | 123 ms: 1.00x faster                                                        |
| regex_v8       | 27.8 ms                                                                  | 28.2 ms: 1.01x slower                                                       |
| regex_effbot   | 3.79 ms                                                                  | 3.89 ms: 1.03x slower                                                       |
| regex_dna      | 237 ms                                                                   | 251 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                                    | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_parse      | 178 ms                                                                   | 177 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 142 ms                                                                   | 141 ms: 1.01x faster                                                        |
| tomli_loads          | 2.39 sec                                                                 | 2.45 sec: 1.02x slower                                                      |
| unpickle_pure_python | 269 us                                                                   | 282 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (5): json_dumps, json_loads, xml_etree_process, xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 15.8 ms                                                                  | 16.1 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|----------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako           | 13.4 ms                                                                  | 13.7 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                    | 1.01x faster                                                                |

Benchmark hidden because not significant (3): genshi_text, django_template, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20250309-arminc-aarch64-python-98fa4a49fecbac3c990a-3.14.0a5+-98fa4a4 | bm-20250310-arminc-aarch64-diegorusso-aarch64_trampolines-3.14.0a5+-efdef5f |
|------------------------|:------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| dulwich_log            | 55.8 ms                                                                  | 53.5 ms: 1.04x faster                                                       |
| pyflate                | 581 ms                                                                   | 566 ms: 1.03x faster                                                        |
| sqlalchemy_imperative  | 15.8 ms                                                                  | 15.5 ms: 1.01x faster                                                       |
| many_optionals         | 846 us                                                                   | 837 us: 1.01x faster                                                        |
| async_tree_none_tg     | 373 ms                                                                   | 370 ms: 1.01x faster                                                        |
| xml_etree_parse        | 178 ms                                                                   | 177 ms: 1.01x faster                                                        |
| sqlalchemy_declarative | 147 ms                                                                   | 146 ms: 1.01x faster                                                        |
| sympy_integrate        | 21.3 ms                                                                  | 21.2 ms: 1.01x faster                                                       |
| xml_etree_iterparse    | 142 ms                                                                   | 141 ms: 1.01x faster                                                        |
| sympy_str              | 271 ms                                                                   | 270 ms: 1.01x faster                                                        |
| regex_compile          | 124 ms                                                                   | 123 ms: 1.00x faster                                                        |
| sqlglot_v2_normalize   | 127 ms                                                                   | 128 ms: 1.00x slower                                                        |
| sqlglot_v2_parse       | 1.50 ms                                                                  | 1.51 ms: 1.01x slower                                                       |
| async_tree_memoization | 468 ms                                                                   | 471 ms: 1.01x slower                                                        |
| sqlite_synth           | 3.73 us                                                                  | 3.75 us: 1.01x slower                                                       |
| logging_simple         | 6.84 us                                                                  | 6.90 us: 1.01x slower                                                       |
| mdp                    | 3.28 sec                                                                 | 3.31 sec: 1.01x slower                                                      |
| logging_format         | 7.57 us                                                                  | 7.64 us: 1.01x slower                                                       |
| connected_components   | 547 ms                                                                   | 552 ms: 1.01x slower                                                        |
| regex_v8               | 27.8 ms                                                                  | 28.2 ms: 1.01x slower                                                       |
| pprint_pformat         | 2.52 sec                                                                 | 2.56 sec: 1.02x slower                                                      |
| python_startup         | 15.8 ms                                                                  | 16.1 ms: 1.02x slower                                                       |
| hexiom                 | 8.12 ms                                                                  | 8.25 ms: 1.02x slower                                                       |
| bpe_tokeniser          | 5.62 sec                                                                 | 5.73 sec: 1.02x slower                                                      |
| meteor_contest         | 119 ms                                                                   | 121 ms: 1.02x slower                                                        |
| json                   | 5.69 ms                                                                  | 5.81 ms: 1.02x slower                                                       |
| tomli_loads            | 2.39 sec                                                                 | 2.45 sec: 1.02x slower                                                      |
| mako                   | 13.4 ms                                                                  | 13.7 ms: 1.02x slower                                                       |
| subparsers             | 25.1 ms                                                                  | 25.7 ms: 1.02x slower                                                       |
| shortest_path          | 571 ms                                                                   | 585 ms: 1.03x slower                                                        |
| regex_effbot           | 3.79 ms                                                                  | 3.89 ms: 1.03x slower                                                       |
| unpickle_pure_python   | 269 us                                                                   | 282 us: 1.05x slower                                                        |
| scimark_monte_carlo    | 84.3 ms                                                                  | 88.8 ms: 1.05x slower                                                       |
| nqueens                | 102 ms                                                                   | 108 ms: 1.06x slower                                                        |
| regex_dna              | 237 ms                                                                   | 251 ms: 1.06x slower                                                        |
| spectral_norm          | 130 ms                                                                   | 138 ms: 1.06x slower                                                        |
| Geometric mean         | (ref)                                                                    | 1.01x slower                                                                |

Benchmark hidden because not significant (60): genshi_text, django_template, json_dumps, create_gc_cycles, crypto_pyaes, pprint_safe_repr, sympy_expand, async_tree_cpu_io_mixed, async_tree_none, scimark_lu, telco, logging_silent, async_tree_cpu_io_mixed_tg, genshi_xml, pylint, 2to3, sqlglot_v2_optimize, gc_traversal, async_tree_io, python_startup_no_site, scimark_sparse_mat_mult, chaos, sympy_sum, async_tree_io_tg, richards_super, json_loads, nbody, bench_thread_pool, float, html5lib, pycparser, docutils, xml_etree_process, k_core, pathlib, asyncio_websockets, typing_runtime_protocols, async_generators, scimark_sor, xml_etree_generate, coverage, sphinx, sqlglot_v2_transpile, go, async_tree_memoization_tg, raytrace, fannkuch, pickle_pure_python, pidigits, thrift, comprehensions, deepcopy_memo, generators, richards, deltablue, scimark_fft, coroutines, deepcopy, deepcopy_reduce, bench_mp_pool

- Geometric mean (including insignificant results): 1.004x slower

# HPT report

- Reliability score: 99.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x