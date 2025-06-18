# Results vs. base

- fork: faster-cpython
- ref: specialize_for_compa
- machine: darwin-arm64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.000x slower
- HPT reliability: 89.93%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 368 ms: 1.00x slower                                                            |
| async_tree_eager              | 72.7 ms                                                               | 72.8 ms: 1.00x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (17): async_tree_eager_memoization_tg, async_tree_memoization_tg, async_tree_eager_io_tg, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, coroutines, async_tree_none, async_tree_eager_memoization, async_tree_io_tg, async_tree_eager_io, async_tree_memoization, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_eager_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 84.8 ms                                                               | 85.2 ms: 1.00x slower                                                           |
| float          | 57.6 ms                                                               | 57.9 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.37 ms                                                               | 2.37 ms: 1.00x slower                                                           |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): regex_v8, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|---------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_iterparse | 74.2 ms                                                               | 73.7 ms: 1.01x faster                                                           |
| tomli_loads         | 1.46 sec                                                              | 1.45 sec: 1.00x faster                                                          |
| xml_etree_generate  | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                                           |
| xml_etree_process   | 42.9 ms                                                               | 43.3 ms: 1.01x slower                                                           |
| Geometric mean      | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (5): xml_etree_parse, json_dumps, pickle_pure_python, unpickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.8 ms                                                               | 13.8 ms: 1.00x slower                                                           |
| python_startup         | 18.3 ms                                                               | 18.4 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.01 ms                                                               | 8.96 ms: 1.01x faster                                                           |
| genshi_text    | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                     | bm-20250617-darwin-arm64-python-8dd8b5c2f0785675b928-3.15.0a0-8dd8b5c | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| spectral_norm                 | 74.8 ms                                                               | 72.0 ms: 1.04x faster                                                           |
| scimark_fft                   | 204 ms                                                                | 202 ms: 1.01x faster                                                            |
| logging_silent                | 343 ns                                                                | 340 ns: 1.01x faster                                                            |
| scimark_sparse_mat_mult       | 3.20 ms                                                               | 3.18 ms: 1.01x faster                                                           |
| bpe_tokeniser                 | 3.26 sec                                                              | 3.24 sec: 1.01x faster                                                          |
| xml_etree_iterparse           | 74.2 ms                                                               | 73.7 ms: 1.01x faster                                                           |
| sqlglot_v2_parse              | 991 us                                                                | 985 us: 1.01x faster                                                            |
| crypto_pyaes                  | 61.4 ms                                                               | 61.1 ms: 1.01x faster                                                           |
| mako                          | 9.01 ms                                                               | 8.96 ms: 1.01x faster                                                           |
| pyflate                       | 333 ms                                                                | 332 ms: 1.01x faster                                                            |
| tomli_loads                   | 1.46 sec                                                              | 1.45 sec: 1.00x faster                                                          |
| dulwich_log                   | 26.4 ms                                                               | 26.3 ms: 1.00x faster                                                           |
| telco                         | 4.77 ms                                                               | 4.75 ms: 1.00x faster                                                           |
| chaos                         | 47.2 ms                                                               | 47.1 ms: 1.00x faster                                                           |
| sqlglot_v2_transpile          | 1.17 ms                                                               | 1.17 ms: 1.00x faster                                                           |
| nqueens                       | 70.4 ms                                                               | 70.2 ms: 1.00x faster                                                           |
| sympy_expand                  | 262 ms                                                                | 262 ms: 1.00x faster                                                            |
| regex_effbot                  | 2.37 ms                                                               | 2.37 ms: 1.00x slower                                                           |
| python_startup_no_site        | 13.8 ms                                                               | 13.8 ms: 1.00x slower                                                           |
| hexiom                        | 5.08 ms                                                               | 5.09 ms: 1.00x slower                                                           |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| richards                      | 37.1 ms                                                               | 37.2 ms: 1.00x slower                                                           |
| async_tree_eager_cpu_io_mixed | 367 ms                                                                | 368 ms: 1.00x slower                                                            |
| logging_format                | 4.34 us                                                               | 4.35 us: 1.00x slower                                                           |
| async_tree_eager              | 72.7 ms                                                               | 72.8 ms: 1.00x slower                                                           |
| genshi_text                   | 17.7 ms                                                               | 17.8 ms: 1.00x slower                                                           |
| scimark_lu                    | 84.4 ms                                                               | 84.6 ms: 1.00x slower                                                           |
| generators                    | 31.5 ms                                                               | 31.6 ms: 1.00x slower                                                           |
| deepcopy                      | 175 us                                                                | 175 us: 1.00x slower                                                            |
| raytrace                      | 212 ms                                                                | 212 ms: 1.00x slower                                                            |
| richards_super                | 41.5 ms                                                               | 41.6 ms: 1.00x slower                                                           |
| pprint_pformat                | 1.26 sec                                                              | 1.27 sec: 1.00x slower                                                          |
| scimark_monte_carlo           | 52.5 ms                                                               | 52.7 ms: 1.00x slower                                                           |
| deepcopy_memo                 | 21.7 us                                                               | 21.8 us: 1.00x slower                                                           |
| coverage                      | 49.1 ms                                                               | 49.3 ms: 1.00x slower                                                           |
| python_startup                | 18.3 ms                                                               | 18.4 ms: 1.00x slower                                                           |
| sqlglot_v2_normalize          | 76.3 ms                                                               | 76.6 ms: 1.00x slower                                                           |
| create_gc_cycles              | 1.35 ms                                                               | 1.36 ms: 1.00x slower                                                           |
| nbody                         | 84.8 ms                                                               | 85.2 ms: 1.00x slower                                                           |
| scimark_sor                   | 89.2 ms                                                               | 89.7 ms: 1.01x slower                                                           |
| sqlite_synth                  | 1.61 us                                                               | 1.62 us: 1.01x slower                                                           |
| shortest_path                 | 327 ms                                                                | 329 ms: 1.01x slower                                                            |
| float                         | 57.6 ms                                                               | 57.9 ms: 1.01x slower                                                           |
| xml_etree_generate            | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                                           |
| pprint_safe_repr              | 622 ms                                                                | 627 ms: 1.01x slower                                                            |
| xml_etree_process             | 42.9 ms                                                               | 43.3 ms: 1.01x slower                                                           |
| meteor_contest                | 74.1 ms                                                               | 74.9 ms: 1.01x slower                                                           |
| connected_components          | 303 ms                                                                | 306 ms: 1.01x slower                                                            |
| mdp                           | 825 ms                                                                | 834 ms: 1.01x slower                                                            |
| json                          | 2.93 ms                                                               | 2.97 ms: 1.01x slower                                                           |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (51): xml_etree_parse, async_tree_eager_memoization_tg, gc_traversal, genshi_xml, async_tree_memoization_tg, deepcopy_reduce, sympy_str, regex_v8, fannkuch, sympy_sum, django_template, json_dumps, regex_compile, comprehensions, pickle_pure_python, deltablue, pidigits, docutils, async_tree_eager_io_tg, go, pylint, sphinx, unpickle_pure_python, json_loads, asyncio_websockets, thrift, sqlglot_v2_optimize, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, dask, coroutines, async_tree_none, async_tree_eager_memoization, async_tree_io_tg, 2to3, async_tree_eager_io, async_tree_memoization, async_generators, async_tree_cpu_io_mixed_tg, async_tree_io, k_core, many_optionals, pycparser, async_tree_eager_tg, sympy_integrate, html5lib, subparsers, async_tree_none_tg, typing_runtime_protocols, logging_simple, pathlib

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 89.93% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x