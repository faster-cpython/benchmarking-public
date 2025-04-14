# Results vs. base

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 490cf8d
- commit date: 2025-03-12
- overall geometric mean: 1.000x faster
- HPT reliability: 69.85%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| sphinx         | 612 ms                                                                 | 601 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): 2to3, docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines       | 17.6 ms                                                                | 17.6 ms: 1.00x faster                                                           |
| async_generators | 263 ms                                                                 | 265 ms: 1.01x slower                                                            |
| Geometric mean   | (ref)                                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_eager_tg, asyncio_websockets, async_tree_memoization, async_tree_io, async_tree_eager_io, async_tree_memoization_tg, async_tree_eager, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 80.1 ms                                                                | 80.1 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 141 ms: 1.00x faster                                                            |
| regex_effbot   | 2.27 ms                                                                | 2.27 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads    | 1.33 sec                                                               | 1.32 sec: 1.01x faster                                                          |
| json_dumps     | 7.47 ms                                                                | 7.50 ms: 1.00x slower                                                           |
| json_loads     | 17.9 us                                                                | 18.0 us: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (6): xml_etree_generate, xml_etree_process, pickle_pure_python, xml_etree_iterparse, unpickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 17.6 ms                                                                | 17.7 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 8.17 ms                                                                | 8.11 ms: 1.01x faster                                                           |
| genshi_xml      | 32.6 ms                                                                | 32.5 ms: 1.00x faster                                                           |
| django_template | 23.0 ms                                                                | 23.0 ms: 1.00x faster                                                           |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250312-darwin-arm64-python-155c44b9015089eacc6e-3.14.0a5+-155c44b | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-490cf8d |
|--------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| sphinx                   | 612 ms                                                                 | 601 ms: 1.02x faster                                                            |
| many_optionals           | 472 us                                                                 | 466 us: 1.01x faster                                                            |
| scimark_lu               | 78.8 ms                                                                | 77.9 ms: 1.01x faster                                                           |
| mako                     | 8.17 ms                                                                | 8.11 ms: 1.01x faster                                                           |
| tomli_loads              | 1.33 sec                                                               | 1.32 sec: 1.01x faster                                                          |
| chaos                    | 43.9 ms                                                                | 43.7 ms: 1.01x faster                                                           |
| bench_mp_pool            | 60.6 ms                                                                | 60.4 ms: 1.00x faster                                                           |
| deepcopy                 | 166 us                                                                 | 166 us: 1.00x faster                                                            |
| genshi_xml               | 32.6 ms                                                                | 32.5 ms: 1.00x faster                                                           |
| logging_simple           | 3.60 us                                                                | 3.59 us: 1.00x faster                                                           |
| scimark_sor              | 87.8 ms                                                                | 87.5 ms: 1.00x faster                                                           |
| sqlglot_v2_transpile     | 1.06 ms                                                                | 1.06 ms: 1.00x faster                                                           |
| logging_silent           | 73.2 ns                                                                | 73.0 ns: 1.00x faster                                                           |
| coroutines               | 17.6 ms                                                                | 17.6 ms: 1.00x faster                                                           |
| spectral_norm            | 70.4 ms                                                                | 70.2 ms: 1.00x faster                                                           |
| django_template          | 23.0 ms                                                                | 23.0 ms: 1.00x faster                                                           |
| regex_dna                | 141 ms                                                                 | 141 ms: 1.00x faster                                                            |
| regex_effbot             | 2.27 ms                                                                | 2.27 ms: 1.00x slower                                                           |
| hexiom                   | 5.05 ms                                                                | 5.05 ms: 1.00x slower                                                           |
| nbody                    | 80.1 ms                                                                | 80.1 ms: 1.00x slower                                                           |
| scimark_sparse_mat_mult  | 3.05 ms                                                                | 3.05 ms: 1.00x slower                                                           |
| richards_super           | 40.2 ms                                                                | 40.2 ms: 1.00x slower                                                           |
| meteor_contest           | 75.4 ms                                                                | 75.6 ms: 1.00x slower                                                           |
| comprehensions           | 12.9 us                                                                | 13.0 us: 1.00x slower                                                           |
| sympy_expand             | 250 ms                                                                 | 251 ms: 1.00x slower                                                            |
| sqlglot_v2_optimize      | 34.9 ms                                                                | 35.0 ms: 1.00x slower                                                           |
| sqlglot_v2_normalize     | 71.6 ms                                                                | 71.8 ms: 1.00x slower                                                           |
| json_dumps               | 7.47 ms                                                                | 7.50 ms: 1.00x slower                                                           |
| nqueens                  | 66.1 ms                                                                | 66.4 ms: 1.00x slower                                                           |
| python_startup           | 17.6 ms                                                                | 17.7 ms: 1.00x slower                                                           |
| pyflate                  | 325 ms                                                                 | 327 ms: 1.01x slower                                                            |
| json_loads               | 17.9 us                                                                | 18.0 us: 1.01x slower                                                           |
| typing_runtime_protocols | 100 us                                                                 | 101 us: 1.01x slower                                                            |
| async_generators         | 263 ms                                                                 | 265 ms: 1.01x slower                                                            |
| fannkuch                 | 294 ms                                                                 | 296 ms: 1.01x slower                                                            |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                                                    |

Benchmark hidden because not significant (70): json, dask, sqlalchemy_imperative, pprint_safe_repr, async_tree_eager_memoization, sympy_str, docutils, generators, regex_compile, gc_traversal, logging_format, create_gc_cycles, mdp, async_tree_io_tg, deepcopy_memo, 2to3, pycparser, crypto_pyaes, pprint_pformat, float, sqlglot_v2_parse, thrift, async_tree_eager_io_tg, richards, go, sympy_sum, raytrace, pidigits, async_tree_eager_memoization_tg, async_tree_none_tg, async_tree_eager_tg, bpe_tokeniser, python_startup_no_site, asyncio_websockets, async_tree_memoization, connected_components, async_tree_io, dulwich_log, sqlalchemy_declarative, genshi_text, xml_etree_generate, scimark_monte_carlo, async_tree_eager_io, scimark_fft, xml_etree_process, pickle_pure_python, async_tree_memoization_tg, async_tree_eager, regex_v8, telco, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, deltablue, html5lib, xml_etree_iterparse, k_core, async_tree_eager_cpu_io_mixed, shortest_path, async_tree_cpu_io_mixed_tg, sqlite_synth, sympy_integrate, bench_thread_pool, unpickle_pure_python, deepcopy_reduce, subparsers, async_tree_none, xml_etree_parse, pathlib, coverage, pylint

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 69.85% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x