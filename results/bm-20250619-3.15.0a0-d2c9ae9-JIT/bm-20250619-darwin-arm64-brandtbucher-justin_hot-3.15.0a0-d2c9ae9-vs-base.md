# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.001x faster
- HPT reliability: 99.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| docutils       | 1.57 sec                                                              | 1.52 sec: 1.03x faster                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                      |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 367 ms: 1.00x faster                                              |
| async_tree_eager              | 71.7 ms                                                               | 71.9 ms: 1.00x slower                                             |
| coroutines                    | 19.2 ms                                                               | 19.3 ms: 1.00x slower                                             |
| async_generators              | 286 ms                                                                | 288 ms: 1.01x slower                                              |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (15): async_tree_none_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_io, async_tree_eager_io_tg, asyncio_websockets, async_tree_eager_io, async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 76.6 ms                                                               | 76.4 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                      |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                              |
| regex_v8       | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                             |
| regex_effbot   | 2.34 ms                                                               | 2.48 ms: 1.06x slower                                             |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| xml_etree_generate | 51.9 ms                                                               | 51.6 ms: 1.01x faster                                             |
| xml_etree_process  | 37.7 ms                                                               | 37.5 ms: 1.00x faster                                             |
| pickle_pure_python | 226 us                                                                | 227 us: 1.00x slower                                              |
| json_loads         | 16.5 us                                                               | 16.6 us: 1.00x slower                                             |
| tomli_loads        | 1.34 sec                                                              | 1.35 sec: 1.01x slower                                            |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (4): xml_etree_parse, json_dumps, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site | 15.6 ms                                                               | 14.4 ms: 1.09x faster                                             |
| python_startup         | 20.2 ms                                                               | 18.8 ms: 1.08x faster                                             |
| Geometric mean         | (ref)                                                                 | 1.08x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 25.3 ms                                                               | 25.2 ms: 1.00x faster                                             |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (3): genshi_xml, genshi_text, mako

All benchmarks:
===============

| Benchmark                     | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup_no_site        | 15.6 ms                                                               | 14.4 ms: 1.09x faster                                             |
| python_startup                | 20.2 ms                                                               | 18.8 ms: 1.08x faster                                             |
| docutils                      | 1.57 sec                                                              | 1.52 sec: 1.03x faster                                            |
| sqlite_synth                  | 1.62 us                                                               | 1.60 us: 1.01x faster                                             |
| pprint_pformat                | 1.20 sec                                                              | 1.19 sec: 1.01x faster                                            |
| sqlglot_v2_parse              | 893 us                                                                | 887 us: 1.01x faster                                              |
| xml_etree_generate            | 51.9 ms                                                               | 51.6 ms: 1.01x faster                                             |
| nqueens                       | 69.4 ms                                                               | 69.1 ms: 1.01x faster                                             |
| thrift                        | 472 us                                                                | 469 us: 1.00x faster                                              |
| sqlglot_v2_normalize          | 76.0 ms                                                               | 75.7 ms: 1.00x faster                                             |
| sympy_integrate               | 11.4 ms                                                               | 11.4 ms: 1.00x faster                                             |
| django_template               | 25.3 ms                                                               | 25.2 ms: 1.00x faster                                             |
| richards_super                | 42.2 ms                                                               | 42.0 ms: 1.00x faster                                             |
| crypto_pyaes                  | 58.0 ms                                                               | 57.8 ms: 1.00x faster                                             |
| xml_etree_process             | 37.7 ms                                                               | 37.5 ms: 1.00x faster                                             |
| nbody                         | 76.6 ms                                                               | 76.4 ms: 1.00x faster                                             |
| scimark_sor                   | 90.6 ms                                                               | 90.3 ms: 1.00x faster                                             |
| create_gc_cycles              | 1.36 ms                                                               | 1.36 ms: 1.00x faster                                             |
| sqlglot_v2_transpile          | 1.08 ms                                                               | 1.08 ms: 1.00x faster                                             |
| scimark_monte_carlo           | 53.5 ms                                                               | 53.3 ms: 1.00x faster                                             |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 367 ms: 1.00x faster                                              |
| 2to3                          | 185 ms                                                                | 185 ms: 1.00x faster                                              |
| spectral_norm                 | 74.3 ms                                                               | 74.4 ms: 1.00x slower                                             |
| connected_components          | 310 ms                                                                | 311 ms: 1.00x slower                                              |
| bpe_tokeniser                 | 3.10 sec                                                              | 3.11 sec: 1.00x slower                                            |
| async_tree_eager              | 71.7 ms                                                               | 71.9 ms: 1.00x slower                                             |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                              |
| coroutines                    | 19.2 ms                                                               | 19.3 ms: 1.00x slower                                             |
| dulwich_log                   | 26.7 ms                                                               | 26.9 ms: 1.00x slower                                             |
| pickle_pure_python            | 226 us                                                                | 227 us: 1.00x slower                                              |
| json_loads                    | 16.5 us                                                               | 16.6 us: 1.00x slower                                             |
| regex_v8                      | 16.2 ms                                                               | 16.3 ms: 1.01x slower                                             |
| async_generators              | 286 ms                                                                | 288 ms: 1.01x slower                                              |
| deepcopy_memo                 | 22.3 us                                                               | 22.5 us: 1.01x slower                                             |
| shortest_path                 | 339 ms                                                                | 341 ms: 1.01x slower                                              |
| tomli_loads                   | 1.34 sec                                                              | 1.35 sec: 1.01x slower                                            |
| scimark_lu                    | 84.3 ms                                                               | 85.2 ms: 1.01x slower                                             |
| logging_silent                | 344 ns                                                                | 348 ns: 1.01x slower                                              |
| fannkuch                      | 302 ms                                                                | 306 ms: 1.01x slower                                              |
| telco                         | 4.57 ms                                                               | 4.67 ms: 1.02x slower                                             |
| regex_effbot                  | 2.34 ms                                                               | 2.48 ms: 1.06x slower                                             |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (60): xml_etree_parse, many_optionals, async_tree_none_tg, pathlib, deepcopy_reduce, typing_runtime_protocols, html5lib, json_dumps, pylint, meteor_contest, async_tree_eager_tg, async_tree_eager_cpu_io_mixed_tg, sqlglot_v2_optimize, async_tree_memoization_tg, pycparser, async_tree_io_tg, comprehensions, async_tree_eager_memoization_tg, genshi_xml, async_tree_io, xml_etree_iterparse, dask, async_tree_eager_io_tg, regex_compile, asyncio_websockets, async_tree_eager_io, async_tree_none, async_tree_cpu_io_mixed_tg, unpickle_pure_python, chaos, gc_traversal, hexiom, generators, mdp, scimark_fft, k_core, genshi_text, deltablue, pidigits, go, sympy_expand, logging_format, scimark_sparse_mat_mult, async_tree_cpu_io_mixed, mako, richards, async_tree_memoization, raytrace, deepcopy, sphinx, sympy_sum, coverage, pprint_safe_repr, logging_simple, async_tree_eager_memoization, pyflate, subparsers, float, sympy_str, json

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 99.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x