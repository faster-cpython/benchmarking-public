# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: 4cfabf5
- commit date: 2025-06-20
- overall geometric mean: 1.000x faster
- HPT reliability: 78.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators              | 289 ms                                                                | 287 ms: 1.01x faster                                              |
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 368 ms: 1.00x slower                                              |
| coroutines                    | 19.2 ms                                                               | 19.3 ms: 1.00x slower                                             |
| async_tree_eager              | 71.5 ms                                                               | 72.1 ms: 1.01x slower                                             |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (15): async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_eager_io, asyncio_websockets, async_tree_eager_tg, async_tree_none_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 284 ms                                                                | 283 ms: 1.00x faster                                              |
| nbody          | 76.7 ms                                                               | 77.0 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 79.6 ms                                                               | 79.5 ms: 1.00x faster                                             |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                              |
| regex_effbot   | 2.34 ms                                                               | 2.37 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python | 227 us                                                                | 226 us: 1.00x faster                                              |
| tomli_loads        | 1.36 sec                                                              | 1.37 sec: 1.01x slower                                            |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (7): xml_etree_parse, xml_etree_iterparse, unpickle_pure_python, xml_etree_process, json_dumps, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 14.3 ms                                                               | 14.2 ms: 1.01x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| genshi_xml      | 36.4 ms                                                               | 36.2 ms: 1.01x faster                                             |
| django_template | 25.4 ms                                                               | 25.2 ms: 1.01x faster                                             |
| mako            | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                             |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250620-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-4cfabf5 |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| pprint_pformat                | 1.20 sec                                                              | 1.18 sec: 1.02x faster                                            |
| meteor_contest                | 77.9 ms                                                               | 76.8 ms: 1.01x faster                                             |
| scimark_fft                   | 208 ms                                                                | 206 ms: 1.01x faster                                              |
| pprint_safe_repr              | 586 ms                                                                | 581 ms: 1.01x faster                                              |
| async_generators              | 289 ms                                                                | 287 ms: 1.01x faster                                              |
| scimark_sparse_mat_mult       | 3.57 ms                                                               | 3.54 ms: 1.01x faster                                             |
| genshi_xml                    | 36.4 ms                                                               | 36.2 ms: 1.01x faster                                             |
| django_template               | 25.4 ms                                                               | 25.2 ms: 1.01x faster                                             |
| sqlglot_v2_normalize          | 76.0 ms                                                               | 75.6 ms: 1.01x faster                                             |
| python_startup_no_site        | 14.3 ms                                                               | 14.2 ms: 1.01x faster                                             |
| sqlglot_v2_optimize           | 36.6 ms                                                               | 36.4 ms: 1.00x faster                                             |
| 2to3                          | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| sympy_integrate               | 11.4 ms                                                               | 11.4 ms: 1.00x faster                                             |
| pickle_pure_python            | 227 us                                                                | 226 us: 1.00x faster                                              |
| scimark_sor                   | 90.9 ms                                                               | 90.6 ms: 1.00x faster                                             |
| pidigits                      | 284 ms                                                                | 283 ms: 1.00x faster                                              |
| scimark_monte_carlo           | 53.5 ms                                                               | 53.4 ms: 1.00x faster                                             |
| regex_compile                 | 79.6 ms                                                               | 79.5 ms: 1.00x faster                                             |
| spectral_norm                 | 74.3 ms                                                               | 74.3 ms: 1.00x slower                                             |
| crypto_pyaes                  | 57.7 ms                                                               | 57.7 ms: 1.00x slower                                             |
| thrift                        | 472 us                                                                | 473 us: 1.00x slower                                              |
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 368 ms: 1.00x slower                                              |
| mako                          | 6.94 ms                                                               | 6.96 ms: 1.00x slower                                             |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                              |
| go                            | 99.7 ms                                                               | 100 ms: 1.00x slower                                              |
| coroutines                    | 19.2 ms                                                               | 19.3 ms: 1.00x slower                                             |
| nbody                         | 76.7 ms                                                               | 77.0 ms: 1.00x slower                                             |
| richards                      | 37.5 ms                                                               | 37.6 ms: 1.00x slower                                             |
| telco                         | 4.59 ms                                                               | 4.62 ms: 1.01x slower                                             |
| fannkuch                      | 305 ms                                                                | 307 ms: 1.01x slower                                              |
| sqlite_synth                  | 1.60 us                                                               | 1.61 us: 1.01x slower                                             |
| mdp                           | 823 ms                                                                | 828 ms: 1.01x slower                                              |
| tomli_loads                   | 1.36 sec                                                              | 1.37 sec: 1.01x slower                                            |
| scimark_lu                    | 84.2 ms                                                               | 84.9 ms: 1.01x slower                                             |
| async_tree_eager              | 71.5 ms                                                               | 72.1 ms: 1.01x slower                                             |
| logging_silent                | 339 ns                                                                | 342 ns: 1.01x slower                                              |
| regex_effbot                  | 2.34 ms                                                               | 2.37 ms: 1.01x slower                                             |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (64): pylint, xml_etree_parse, connected_components, sympy_str, xml_etree_iterparse, shortest_path, float, nqueens, genshi_text, dask, gc_traversal, unpickle_pure_python, logging_format, deepcopy_memo, xml_etree_process, json_dumps, many_optionals, create_gc_cycles, async_tree_eager_memoization_tg, pycparser, async_tree_memoization_tg, python_startup, raytrace, sqlglot_v2_parse, xml_etree_generate, sphinx, coverage, chaos, docutils, json, html5lib, async_tree_eager_io, asyncio_websockets, deepcopy_reduce, comprehensions, bpe_tokeniser, async_tree_eager_tg, pyflate, hexiom, async_tree_none_tg, sympy_expand, generators, async_tree_eager_io_tg, deltablue, async_tree_eager_cpu_io_mixed_tg, sqlglot_v2_transpile, richards_super, dulwich_log, async_tree_io_tg, typing_runtime_protocols, async_tree_cpu_io_mixed, k_core, deepcopy, regex_v8, json_loads, logging_simple, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io, sympy_sum, async_tree_eager_memoization, async_tree_none, subparsers, pathlib

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 78.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x