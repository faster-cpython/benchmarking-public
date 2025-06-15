# Results vs. base

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 9b65402
- commit date: 2025-06-13
- overall geometric mean: 1.000x slower
- HPT reliability: 75.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 186 ms                                                                | 213 ms: 1.15x slower                                                            |
| docutils       | 1.51 sec                                                              | 1.51 sec: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                                    |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                    | 19.3 ms                                                               | 19.3 ms: 1.00x faster                                                           |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 369 ms: 1.00x slower                                                            |
| async_tree_eager              | 73.0 ms                                                               | 73.4 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 425 ms: 1.01x slower                                                            |
| async_tree_cpu_io_mixed       | 433 ms                                                                | 436 ms: 1.01x slower                                                            |
| async_generators              | 273 ms                                                                | 279 ms: 1.02x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (13): async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_tg, asyncio_websockets, async_tree_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_memoization, async_tree_eager_io, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 84.7 ms                                                               | 85.1 ms: 1.01x slower                                                           |
| float          | 57.7 ms                                                               | 58.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 81.4 ms                                                               | 81.2 ms: 1.00x faster                                                           |
| regex_effbot   | 2.34 ms                                                               | 2.34 ms: 1.00x faster                                                           |
| regex_dna      | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| regex_v8       | 16.1 ms                                                               | 16.2 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads        | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                                          |
| json_dumps         | 6.83 ms                                                               | 6.78 ms: 1.01x faster                                                           |
| xml_etree_generate | 58.1 ms                                                               | 58.5 ms: 1.01x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, xml_etree_process, pickle_pure_python, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 17.5 ms                                                               | 17.4 ms: 1.01x faster                                                           |
| python_startup_no_site | 13.1 ms                                                               | 13.0 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.01x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako           | 9.19 ms                                                               | 8.99 ms: 1.02x faster                                                           |
| genshi_xml     | 36.5 ms                                                               | 36.3 ms: 1.00x faster                                                           |
| genshi_text    | 17.6 ms                                                               | 17.7 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                     | bm-20250613-darwin-arm64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d | bm-20250613-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-9b65402 |
|-------------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| logging_simple                | 4.19 us                                                               | 4.05 us: 1.03x faster                                                           |
| logging_format                | 4.44 us                                                               | 4.34 us: 1.02x faster                                                           |
| mako                          | 9.19 ms                                                               | 8.99 ms: 1.02x faster                                                           |
| pathlib                       | 24.7 ms                                                               | 24.3 ms: 1.02x faster                                                           |
| chaos                         | 48.4 ms                                                               | 47.5 ms: 1.02x faster                                                           |
| connected_components          | 308 ms                                                                | 303 ms: 1.02x faster                                                            |
| typing_runtime_protocols      | 110 us                                                                | 109 us: 1.01x faster                                                            |
| logging_silent                | 347 ns                                                                | 343 ns: 1.01x faster                                                            |
| sqlglot_v2_normalize          | 76.7 ms                                                               | 75.9 ms: 1.01x faster                                                           |
| hexiom                        | 5.10 ms                                                               | 5.06 ms: 1.01x faster                                                           |
| tomli_loads                   | 1.45 sec                                                              | 1.44 sec: 1.01x faster                                                          |
| python_startup                | 17.5 ms                                                               | 17.4 ms: 1.01x faster                                                           |
| json_dumps                    | 6.83 ms                                                               | 6.78 ms: 1.01x faster                                                           |
| scimark_sparse_mat_mult       | 3.17 ms                                                               | 3.15 ms: 1.01x faster                                                           |
| python_startup_no_site        | 13.1 ms                                                               | 13.0 ms: 1.01x faster                                                           |
| dulwich_log                   | 26.8 ms                                                               | 26.6 ms: 1.01x faster                                                           |
| sqlglot_v2_optimize           | 36.6 ms                                                               | 36.3 ms: 1.01x faster                                                           |
| crypto_pyaes                  | 61.4 ms                                                               | 61.1 ms: 1.01x faster                                                           |
| deltablue                     | 2.81 ms                                                               | 2.80 ms: 1.00x faster                                                           |
| scimark_lu                    | 84.3 ms                                                               | 84.0 ms: 1.00x faster                                                           |
| meteor_contest                | 74.5 ms                                                               | 74.2 ms: 1.00x faster                                                           |
| mdp                           | 829 ms                                                                | 826 ms: 1.00x faster                                                            |
| deepcopy_reduce               | 1.90 us                                                               | 1.90 us: 1.00x faster                                                           |
| genshi_xml                    | 36.5 ms                                                               | 36.3 ms: 1.00x faster                                                           |
| docutils                      | 1.51 sec                                                              | 1.51 sec: 1.00x faster                                                          |
| go                            | 100 ms                                                                | 100 ms: 1.00x faster                                                            |
| coroutines                    | 19.3 ms                                                               | 19.3 ms: 1.00x faster                                                           |
| regex_compile                 | 81.4 ms                                                               | 81.2 ms: 1.00x faster                                                           |
| regex_effbot                  | 2.34 ms                                                               | 2.34 ms: 1.00x faster                                                           |
| fannkuch                      | 310 ms                                                                | 309 ms: 1.00x faster                                                            |
| shortest_path                 | 328 ms                                                                | 327 ms: 1.00x faster                                                            |
| sympy_expand                  | 261 ms                                                                | 260 ms: 1.00x faster                                                            |
| bpe_tokeniser                 | 3.28 sec                                                              | 3.27 sec: 1.00x faster                                                          |
| scimark_fft                   | 206 ms                                                                | 206 ms: 1.00x slower                                                            |
| pprint_pformat                | 1.27 sec                                                              | 1.27 sec: 1.00x slower                                                          |
| sqlite_synth                  | 1.61 us                                                               | 1.62 us: 1.00x slower                                                           |
| genshi_text                   | 17.6 ms                                                               | 17.7 ms: 1.00x slower                                                           |
| async_tree_eager_cpu_io_mixed | 368 ms                                                                | 369 ms: 1.00x slower                                                            |
| generators                    | 31.5 ms                                                               | 31.6 ms: 1.00x slower                                                           |
| scimark_sor                   | 90.9 ms                                                               | 91.1 ms: 1.00x slower                                                           |
| create_gc_cycles              | 1.35 ms                                                               | 1.35 ms: 1.00x slower                                                           |
| regex_dna                     | 143 ms                                                                | 143 ms: 1.00x slower                                                            |
| pyflate                       | 336 ms                                                                | 338 ms: 1.00x slower                                                            |
| pprint_safe_repr              | 623 ms                                                                | 626 ms: 1.00x slower                                                            |
| regex_v8                      | 16.1 ms                                                               | 16.2 ms: 1.00x slower                                                           |
| nqueens                       | 71.2 ms                                                               | 71.5 ms: 1.00x slower                                                           |
| many_optionals                | 494 us                                                                | 497 us: 1.00x slower                                                            |
| nbody                         | 84.7 ms                                                               | 85.1 ms: 1.01x slower                                                           |
| async_tree_eager              | 73.0 ms                                                               | 73.4 ms: 1.01x slower                                                           |
| xml_etree_generate            | 58.1 ms                                                               | 58.5 ms: 1.01x slower                                                           |
| async_tree_cpu_io_mixed_tg    | 422 ms                                                                | 425 ms: 1.01x slower                                                            |
| deepcopy_memo                 | 21.8 us                                                               | 22.0 us: 1.01x slower                                                           |
| comprehensions                | 13.1 us                                                               | 13.2 us: 1.01x slower                                                           |
| async_tree_cpu_io_mixed       | 433 ms                                                                | 436 ms: 1.01x slower                                                            |
| json                          | 2.94 ms                                                               | 2.96 ms: 1.01x slower                                                           |
| float                         | 57.7 ms                                                               | 58.7 ms: 1.02x slower                                                           |
| async_generators              | 273 ms                                                                | 279 ms: 1.02x slower                                                            |
| 2to3                          | 186 ms                                                                | 213 ms: 1.15x slower                                                            |
| Geometric mean                | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (43): async_tree_eager_memoization_tg, xml_etree_parse, sphinx, async_tree_eager_io_tg, pylint, telco, richards_super, async_tree_eager_tg, coverage, deepcopy, gc_traversal, dask, unpickle_pure_python, pidigits, xml_etree_iterparse, spectral_norm, pycparser, xml_etree_process, sqlglot_v2_transpile, sympy_integrate, richards, thrift, sympy_str, sqlglot_v2_parse, raytrace, asyncio_websockets, pickle_pure_python, async_tree_io_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_io, django_template, json_loads, sympy_sum, html5lib, scimark_monte_carlo, async_tree_memoization_tg, subparsers, async_tree_none_tg, async_tree_eager_memoization, k_core, async_tree_eager_io, async_tree_none

- Geometric mean (including insignificant results): 1.000x slower

# HPT report

- Reliability score: 75.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x