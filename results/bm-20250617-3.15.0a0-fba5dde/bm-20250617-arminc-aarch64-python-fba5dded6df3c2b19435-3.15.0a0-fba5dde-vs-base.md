# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-aarch64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.001x slower
- HPT reliability: 93.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg | 482 ms                                                                  | 472 ms: 1.02x faster                                                    |
| coroutines                | 30.0 ms                                                                 | 29.4 ms: 1.02x faster                                                   |
| async_tree_io             | 910 ms                                                                  | 897 ms: 1.01x faster                                                    |
| async_tree_none_tg        | 388 ms                                                                  | 383 ms: 1.01x faster                                                    |
| Geometric mean            | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (7): async_tree_io_tg, asyncio_websockets, async_generators, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 120 ms                                                                  | 119 ms: 1.00x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                  | 223 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse | 141 ms                                                                  | 142 ms: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (8): json_dumps, json_loads, pickle_pure_python, unpickle_pure_python, tomli_loads, xml_etree_process, xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 8.60 ms                                                                 | 8.54 ms: 1.01x faster                                                   |
| Geometric mean         | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako           | 14.0 ms                                                                 | 13.8 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20250617-arminc-aarch64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-arminc-aarch64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|---------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| connected_components      | 569 ms                                                                  | 555 ms: 1.02x faster                                                    |
| async_tree_memoization_tg | 482 ms                                                                  | 472 ms: 1.02x faster                                                    |
| coroutines                | 30.0 ms                                                                 | 29.4 ms: 1.02x faster                                                   |
| async_tree_io             | 910 ms                                                                  | 897 ms: 1.01x faster                                                    |
| mako                      | 14.0 ms                                                                 | 13.8 ms: 1.01x faster                                                   |
| async_tree_none_tg        | 388 ms                                                                  | 383 ms: 1.01x faster                                                    |
| python_startup_no_site    | 8.60 ms                                                                 | 8.54 ms: 1.01x faster                                                   |
| nbody                     | 120 ms                                                                  | 119 ms: 1.00x faster                                                    |
| sqlglot_v2_normalize      | 123 ms                                                                  | 124 ms: 1.01x slower                                                    |
| regex_dna                 | 221 ms                                                                  | 223 ms: 1.01x slower                                                    |
| xml_etree_iterparse       | 141 ms                                                                  | 142 ms: 1.01x slower                                                    |
| hexiom                    | 6.77 ms                                                                 | 6.86 ms: 1.01x slower                                                   |
| mdp                       | 1.66 sec                                                                | 1.68 sec: 1.02x slower                                                  |
| create_gc_cycles          | 3.69 ms                                                                 | 3.84 ms: 1.04x slower                                                   |
| gc_traversal              | 6.71 ms                                                                 | 7.00 ms: 1.04x slower                                                   |
| many_optionals            | 740 us                                                                  | 772 us: 1.04x slower                                                    |
| dulwich_log               | 50.8 ms                                                                 | 54.4 ms: 1.07x slower                                                   |
| Geometric mean            | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (76): regex_v8, sqlglot_v2_transpile, json_dumps, deepcopy_memo, chaos, thrift, genshi_xml, async_tree_io_tg, asyncio_websockets, async_generators, nqueens, sqlglot_v2_parse, pylint, sympy_str, json_loads, pickle_pure_python, k_core, fannkuch, typing_runtime_protocols, crypto_pyaes, pathlib, telco, scimark_monte_carlo, logging_format, scimark_fft, django_template, shortest_path, subparsers, unpickle_pure_python, tomli_loads, richards_super, pprint_pformat, async_tree_none, json, richards, logging_simple, djangocms, xml_etree_process, coverage, float, scimark_lu, bpe_tokeniser, 2to3, pycparser, spectral_norm, regex_compile, meteor_contest, deltablue, sqlite_synth, sphinx, generators, async_tree_memoization, scimark_sor, comprehensions, python_startup, xml_etree_parse, sympy_expand, html5lib, async_tree_cpu_io_mixed, docutils, pidigits, async_tree_cpu_io_mixed_tg, raytrace, pprint_safe_repr, deepcopy, pyflate, xml_etree_generate, sympy_sum, logging_silent, genshi_text, sympy_integrate, go, sqlglot_v2_optimize, scimark_sparse_mat_mult, regex_effbot, deepcopy_reduce

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 93.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x