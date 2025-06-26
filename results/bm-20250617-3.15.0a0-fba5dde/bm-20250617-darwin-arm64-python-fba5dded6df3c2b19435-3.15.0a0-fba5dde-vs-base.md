# Results vs. base

- fork: python
- ref: fba5dded6df3c2b19435
- machine: darwin-arm64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.001x faster
- HPT reliability: 86.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 72.7 ms                                                               | 72.9 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 369 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed       | 432 ms                                                                | 434 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 425 ms: 1.01x slower                                                  |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (15): async_tree_eager_memoization_tg, async_generators, async_tree_io_tg, async_tree_eager_io_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_eager_memoization, coroutines, async_tree_eager_tg, async_tree_none_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                                | 290 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): regex_v8, regex_compile, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse   | 104 ms                                                                | 103 ms: 1.01x faster                                                  |
| tomli_loads       | 1.46 sec                                                              | 1.45 sec: 1.01x faster                                                |
| xml_etree_process | 42.9 ms                                                               | 43.0 ms: 1.00x slower                                                 |
| Geometric mean    | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, xml_etree_generate, json_dumps, json_loads, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                               | 13.0 ms: 1.06x faster                                                 |
| python_startup         | 18.3 ms                                                               | 17.4 ms: 1.05x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.06x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 9.01 ms                                                               | 9.04 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (3): genshi_xml, django_template, genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250617-darwin-arm64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site        | 13.8 ms                                                               | 13.0 ms: 1.06x faster                                                 |
| python_startup                | 18.3 ms                                                               | 17.4 ms: 1.05x faster                                                 |
| xml_etree_parse               | 104 ms                                                                | 103 ms: 1.01x faster                                                  |
| bpe_tokeniser                 | 3.26 sec                                                              | 3.23 sec: 1.01x faster                                                |
| scimark_sparse_mat_mult       | 3.20 ms                                                               | 3.18 ms: 1.01x faster                                                 |
| sympy_sum                     | 81.4 ms                                                               | 80.9 ms: 1.01x faster                                                 |
| tomli_loads                   | 1.46 sec                                                              | 1.45 sec: 1.01x faster                                                |
| nqueens                       | 70.4 ms                                                               | 70.2 ms: 1.00x faster                                                 |
| sqlglot_v2_parse              | 991 us                                                                | 988 us: 1.00x faster                                                  |
| scimark_fft                   | 204 ms                                                                | 203 ms: 1.00x faster                                                  |
| logging_silent                | 343 ns                                                                | 342 ns: 1.00x faster                                                  |
| go                            | 99.3 ms                                                               | 99.1 ms: 1.00x faster                                                 |
| comprehensions                | 13.1 us                                                               | 13.1 us: 1.00x faster                                                 |
| pyflate                       | 333 ms                                                                | 333 ms: 1.00x faster                                                  |
| chaos                         | 47.2 ms                                                               | 47.3 ms: 1.00x slower                                                 |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                                  |
| xml_etree_process             | 42.9 ms                                                               | 43.0 ms: 1.00x slower                                                 |
| mako                          | 9.01 ms                                                               | 9.04 ms: 1.00x slower                                                 |
| pprint_pformat                | 1.26 sec                                                              | 1.27 sec: 1.00x slower                                                |
| async_tree_eager              | 72.7 ms                                                               | 72.9 ms: 1.00x slower                                                 |
| sqlglot_v2_normalize          | 76.3 ms                                                               | 76.5 ms: 1.00x slower                                                 |
| richards_super                | 41.5 ms                                                               | 41.7 ms: 1.00x slower                                                 |
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 369 ms: 1.00x slower                                                  |
| async_tree_cpu_io_mixed       | 432 ms                                                                | 434 ms: 1.01x slower                                                  |
| meteor_contest                | 74.1 ms                                                               | 74.6 ms: 1.01x slower                                                 |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 425 ms: 1.01x slower                                                  |
| deepcopy_memo                 | 21.7 us                                                               | 21.9 us: 1.01x slower                                                 |
| scimark_monte_carlo           | 52.5 ms                                                               | 53.0 ms: 1.01x slower                                                 |
| pprint_safe_repr              | 622 ms                                                                | 629 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.61 us                                                               | 1.63 us: 1.01x slower                                                 |
| pidigits                      | 284 ms                                                                | 290 ms: 1.02x slower                                                  |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (70): json, async_tree_eager_memoization_tg, coverage, genshi_xml, k_core, float, xml_etree_iterparse, sympy_expand, xml_etree_generate, async_generators, regex_v8, crypto_pyaes, async_tree_io_tg, sympy_str, django_template, typing_runtime_protocols, dulwich_log, fannkuch, regex_compile, spectral_norm, dask, logging_simple, async_tree_eager_io_tg, create_gc_cycles, genshi_text, scimark_lu, scimark_sor, sphinx, sympy_integrate, hexiom, connected_components, deepcopy_reduce, deltablue, async_tree_memoization_tg, telco, pylint, gc_traversal, nbody, sqlglot_v2_transpile, raytrace, generators, asyncio_websockets, shortest_path, async_tree_eager_memoization, json_dumps, coroutines, docutils, regex_effbot, deepcopy, json_loads, many_optionals, richards, 2to3, mdp, logging_format, pycparser, unpickle_pure_python, thrift, async_tree_eager_tg, async_tree_none_tg, html5lib, pickle_pure_python, async_tree_io, sqlglot_v2_optimize, subparsers, async_tree_memoization, async_tree_none, async_tree_eager_io, async_tree_eager_cpu_io_mixed_tg, pathlib

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 86.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x