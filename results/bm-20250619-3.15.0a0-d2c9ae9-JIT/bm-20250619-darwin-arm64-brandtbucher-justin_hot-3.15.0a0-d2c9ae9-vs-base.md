# Results vs. base

- fork: brandtbucher
- ref: justin_hot
- machine: darwin-arm64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.069x faster
- HPT reliability: 99.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 186 ms                                                | 185 ms: 1.00x faster                                              |
| Geometric mean | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| async_generators              | 294 ms                                                | 288 ms: 1.02x faster                                              |
| async_tree_eager_cpu_io_mixed | 368 ms                                                | 367 ms: 1.00x faster                                              |
| coroutines                    | 19.3 ms                                               | 19.3 ms: 1.00x slower                                             |
| Geometric mean                | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (16): async_tree_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_none_tg, async_tree_io_tg, async_tree_eager_io_tg, asyncio_websockets, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_io, async_tree_none, async_tree_memoization, async_tree_io, async_tree_eager_memoization, async_tree_eager

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| pidigits       | 283 ms                                                | 283 ms: 1.00x slower                                              |
| Geometric mean | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (2): float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 79.7 ms                                               | 79.6 ms: 1.00x faster                                             |
| regex_effbot   | 2.40 ms                                               | 2.48 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                 | 1.01x slower                                                      |

Benchmark hidden because not significant (2): regex_dna, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| tomli_loads        | 1.37 sec                                              | 1.35 sec: 1.01x faster                                            |
| xml_etree_process  | 37.7 ms                                               | 37.5 ms: 1.00x faster                                             |
| xml_etree_generate | 51.8 ms                                               | 51.6 ms: 1.00x faster                                             |
| json_dumps         | 6.81 ms                                               | 6.84 ms: 1.01x slower                                             |
| xml_etree_parse    | 101 ms                                                | 102 ms: 1.01x slower                                              |
| Geometric mean     | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (4): pickle_pure_python, unpickle_pure_python, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup | 18.9 ms                                               | 18.8 ms: 1.00x faster                                             |
| Geometric mean | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| django_template | 25.4 ms                                               | 25.2 ms: 1.01x faster                                             |
| Geometric mean  | (ref)                                                 | 1.00x faster                                                      |

Benchmark hidden because not significant (3): genshi_xml, mako, genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250610-darwin-arm64-python-main-3.15.0a0-0f866cb | bm-20250619-darwin-arm64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------------|:-----------------------------------------------------:|:-----------------------------------------------------------------:|
| thrift                        | 43.9 ms                                               | 469 us: 93.57x faster                                             |
| coverage                      | 336 ms                                                | 49.7 ms: 6.77x faster                                             |
| dask                          | 849 ms                                                | 771 ms: 1.10x faster                                              |
| async_generators              | 294 ms                                                | 288 ms: 1.02x faster                                              |
| dulwich_log                   | 27.3 ms                                               | 26.9 ms: 1.02x faster                                             |
| fannkuch                      | 310 ms                                                | 306 ms: 1.01x faster                                              |
| tomli_loads                   | 1.37 sec                                              | 1.35 sec: 1.01x faster                                            |
| django_template               | 25.4 ms                                               | 25.2 ms: 1.01x faster                                             |
| deepcopy_reduce               | 1.91 us                                               | 1.89 us: 1.01x faster                                             |
| create_gc_cycles              | 1.37 ms                                               | 1.36 ms: 1.01x faster                                             |
| deepcopy                      | 176 us                                                | 174 us: 1.01x faster                                              |
| sqlglot_v2_transpile          | 1.08 ms                                               | 1.08 ms: 1.01x faster                                             |
| sqlglot_v2_normalize          | 76.1 ms                                               | 75.7 ms: 1.01x faster                                             |
| hexiom                        | 5.03 ms                                               | 5.00 ms: 1.00x faster                                             |
| 2to3                          | 186 ms                                                | 185 ms: 1.00x faster                                              |
| meteor_contest                | 77.1 ms                                               | 76.8 ms: 1.00x faster                                             |
| xml_etree_process             | 37.7 ms                                               | 37.5 ms: 1.00x faster                                             |
| xml_etree_generate            | 51.8 ms                                               | 51.6 ms: 1.00x faster                                             |
| python_startup                | 18.9 ms                                               | 18.8 ms: 1.00x faster                                             |
| scimark_monte_carlo           | 53.5 ms                                               | 53.3 ms: 1.00x faster                                             |
| async_tree_eager_cpu_io_mixed | 368 ms                                                | 367 ms: 1.00x faster                                              |
| sympy_integrate               | 11.4 ms                                               | 11.4 ms: 1.00x faster                                             |
| sqlglot_v2_parse              | 889 us                                                | 887 us: 1.00x faster                                              |
| regex_compile                 | 79.7 ms                                               | 79.6 ms: 1.00x faster                                             |
| pidigits                      | 283 ms                                                | 283 ms: 1.00x slower                                              |
| connected_components          | 310 ms                                                | 311 ms: 1.00x slower                                              |
| generators                    | 31.6 ms                                               | 31.7 ms: 1.00x slower                                             |
| spectral_norm                 | 74.2 ms                                               | 74.4 ms: 1.00x slower                                             |
| raytrace                      | 211 ms                                                | 211 ms: 1.00x slower                                              |
| bpe_tokeniser                 | 3.10 sec                                              | 3.11 sec: 1.00x slower                                            |
| coroutines                    | 19.3 ms                                               | 19.3 ms: 1.00x slower                                             |
| deepcopy_memo                 | 22.4 us                                               | 22.5 us: 1.00x slower                                             |
| sympy_str                     | 155 ms                                                | 156 ms: 1.00x slower                                              |
| scimark_lu                    | 84.7 ms                                               | 85.2 ms: 1.01x slower                                             |
| json_dumps                    | 6.81 ms                                               | 6.84 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult       | 3.54 ms                                               | 3.56 ms: 1.01x slower                                             |
| xml_etree_parse               | 101 ms                                                | 102 ms: 1.01x slower                                              |
| regex_effbot                  | 2.40 ms                                               | 2.48 ms: 1.04x slower                                             |
| logging_silent                | 335 ns                                                | 348 ns: 1.04x slower                                              |
| Geometric mean                | (ref)                                                 | 1.07x faster                                                      |

Benchmark hidden because not significant (62): subparsers, pycparser, typing_runtime_protocols, deltablue, float, comprehensions, async_tree_memoization_tg, pathlib, genshi_xml, async_tree_eager_cpu_io_mixed_tg, pickle_pure_python, async_tree_none_tg, async_tree_io_tg, async_tree_eager_io_tg, chaos, scimark_fft, docutils, go, logging_format, pylint, mako, richards_super, regex_dna, html5lib, unpickle_pure_python, asyncio_websockets, async_tree_eager_tg, crypto_pyaes, async_tree_eager_memoization_tg, async_tree_cpu_io_mixed, gc_traversal, telco, sphinx, async_tree_cpu_io_mixed_tg, scimark_sor, async_tree_eager_io, async_tree_none, nbody, sympy_sum, nqueens, sqlglot_v2_optimize, logging_simple, k_core, async_tree_memoization, regex_v8, genshi_text, richards, async_tree_io, async_tree_eager_memoization, json_loads, many_optionals, mdp, python_startup_no_site, sqlite_synth, sympy_expand, async_tree_eager, pprint_pformat, pyflate, xml_etree_iterparse, shortest_path, pprint_safe_repr, json

- Geometric mean (including insignificant results): 1.069x faster

# HPT report

- Reliability score: 99.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x