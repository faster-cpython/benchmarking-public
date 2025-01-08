# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: darwin-arm64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x faster
- HPT reliability: 85.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 1.40 sec                                                               | 1.40 sec: 1.00x slower                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_eager_memoization_tg  | 123 ms                                                                 | 121 ms: 1.01x faster                                          |
| coroutines                       | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                 | 338 ms: 1.00x faster                                          |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                 | 359 ms: 1.00x faster                                          |
| async_tree_eager_tg              | 43.2 ms                                                                | 43.4 ms: 1.00x slower                                         |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (14): async_generators, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_io_tg, async_tree_eager, async_tree_eager_io, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_none_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 68.2 ms                                                                | 68.1 ms: 1.00x faster                                         |
| float          | 46.3 ms                                                                | 46.4 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                                | 15.7 ms: 1.03x faster                                         |
| regex_effbot   | 2.10 ms                                                                | 2.04 ms: 1.03x faster                                         |
| regex_dna      | 138 ms                                                                 | 135 ms: 1.02x faster                                          |
| regex_compile  | 66.6 ms                                                                | 66.8 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| xml_etree_process  | 38.0 ms                                                                | 38.1 ms: 1.00x slower                                         |
| xml_etree_generate | 52.2 ms                                                                | 52.4 ms: 1.00x slower                                         |
| json_loads         | 16.5 us                                                                | 16.5 us: 1.00x slower                                         |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (6): tomli_loads, json_dumps, unpickle_pure_python, pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                                | 13.7 ms: 1.00x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_xml      | 28.1 ms                                                                | 28.2 ms: 1.00x slower                                         |
| django_template | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                  |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                        | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-darwin-arm64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_v8                         | 16.2 ms                                                                | 15.7 ms: 1.03x faster                                         |
| regex_effbot                     | 2.10 ms                                                                | 2.04 ms: 1.03x faster                                         |
| regex_dna                        | 138 ms                                                                 | 135 ms: 1.02x faster                                          |
| fannkuch                         | 248 ms                                                                 | 244 ms: 1.02x faster                                          |
| pathlib                          | 22.6 ms                                                                | 22.3 ms: 1.01x faster                                         |
| scimark_monte_carlo              | 42.1 ms                                                                | 41.5 ms: 1.01x faster                                         |
| async_tree_eager_memoization_tg  | 123 ms                                                                 | 121 ms: 1.01x faster                                          |
| pprint_safe_repr                 | 457 ms                                                                 | 452 ms: 1.01x faster                                          |
| logging_silent                   | 65.5 ns                                                                | 64.8 ns: 1.01x faster                                         |
| subparsers                       | 11.9 ms                                                                | 11.8 ms: 1.01x faster                                         |
| coroutines                       | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                         |
| richards                         | 31.8 ms                                                                | 31.5 ms: 1.01x faster                                         |
| scimark_fft                      | 173 ms                                                                 | 171 ms: 1.01x faster                                          |
| json                             | 2.84 ms                                                                | 2.82 ms: 1.01x faster                                         |
| create_gc_cycles                 | 1.29 ms                                                                | 1.28 ms: 1.01x faster                                         |
| richards_super                   | 35.4 ms                                                                | 35.2 ms: 1.01x faster                                         |
| logging_simple                   | 3.15 us                                                                | 3.13 us: 1.01x faster                                         |
| scimark_sparse_mat_mult          | 2.67 ms                                                                | 2.65 ms: 1.00x faster                                         |
| scimark_sor                      | 78.9 ms                                                                | 78.5 ms: 1.00x faster                                         |
| sqlglot_transpile                | 932 us                                                                 | 927 us: 1.00x faster                                          |
| logging_format                   | 3.46 us                                                                | 3.44 us: 1.00x faster                                         |
| python_startup_no_site           | 13.7 ms                                                                | 13.7 ms: 1.00x faster                                         |
| meteor_contest                   | 70.9 ms                                                                | 70.6 ms: 1.00x faster                                         |
| gc_traversal                     | 3.24 ms                                                                | 3.22 ms: 1.00x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                 | 338 ms: 1.00x faster                                          |
| nbody                            | 68.2 ms                                                                | 68.1 ms: 1.00x faster                                         |
| async_tree_eager_cpu_io_mixed    | 359 ms                                                                 | 359 ms: 1.00x faster                                          |
| pprint_pformat                   | 914 ms                                                                 | 913 ms: 1.00x faster                                          |
| float                            | 46.3 ms                                                                | 46.4 ms: 1.00x slower                                         |
| xml_etree_process                | 38.0 ms                                                                | 38.1 ms: 1.00x slower                                         |
| raytrace                         | 168 ms                                                                 | 169 ms: 1.00x slower                                          |
| deepcopy                         | 149 us                                                                 | 149 us: 1.00x slower                                          |
| genshi_xml                       | 28.1 ms                                                                | 28.2 ms: 1.00x slower                                         |
| many_optionals                   | 437 us                                                                 | 439 us: 1.00x slower                                          |
| dulwich_log                      | 26.8 ms                                                                | 26.9 ms: 1.00x slower                                         |
| spectral_norm                    | 61.5 ms                                                                | 61.7 ms: 1.00x slower                                         |
| chaos                            | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                         |
| regex_compile                    | 66.6 ms                                                                | 66.8 ms: 1.00x slower                                         |
| connected_components             | 296 ms                                                                 | 297 ms: 1.00x slower                                          |
| xml_etree_generate               | 52.2 ms                                                                | 52.4 ms: 1.00x slower                                         |
| async_tree_eager_tg              | 43.2 ms                                                                | 43.4 ms: 1.00x slower                                         |
| sqlite_synth                     | 1.53 us                                                                | 1.53 us: 1.00x slower                                         |
| docutils                         | 1.40 sec                                                               | 1.40 sec: 1.00x slower                                        |
| hexiom                           | 4.12 ms                                                                | 4.14 ms: 1.00x slower                                         |
| json_loads                       | 16.5 us                                                                | 16.5 us: 1.00x slower                                         |
| sympy_integrate                  | 11.1 ms                                                                | 11.1 ms: 1.00x slower                                         |
| sympy_expand                     | 233 ms                                                                 | 234 ms: 1.00x slower                                          |
| sympy_str                        | 138 ms                                                                 | 138 ms: 1.01x slower                                          |
| bench_mp_pool                    | 60.5 ms                                                                | 60.9 ms: 1.01x slower                                         |
| bench_thread_pool                | 471 us                                                                 | 474 us: 1.01x slower                                          |
| shortest_path                    | 323 ms                                                                 | 325 ms: 1.01x slower                                          |
| django_template                  | 20.8 ms                                                                | 20.9 ms: 1.01x slower                                         |
| scimark_lu                       | 72.0 ms                                                                | 72.5 ms: 1.01x slower                                         |
| telco                            | 4.52 ms                                                                | 4.56 ms: 1.01x slower                                         |
| deepcopy_reduce                  | 1.54 us                                                                | 1.55 us: 1.01x slower                                         |
| thrift                           | 432 us                                                                 | 437 us: 1.01x slower                                          |
| nqueens                          | 55.6 ms                                                                | 56.2 ms: 1.01x slower                                         |
| sympy_sum                        | 72.5 ms                                                                | 73.5 ms: 1.01x slower                                         |
| generators                       | 21.8 ms                                                                | 22.1 ms: 1.01x slower                                         |
| comprehensions                   | 12.2 us                                                                | 12.4 us: 1.02x slower                                         |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (45): async_generators, deltablue, tomli_loads, pylint, python_startup, sqlglot_parse, deepcopy_memo, 2to3, pidigits, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager_io_tg, mdp, crypto_pyaes, async_tree_io_tg, sqlalchemy_imperative, json_dumps, async_tree_eager, unpickle_pure_python, sqlalchemy_declarative, async_tree_eager_io, genshi_text, sqlglot_normalize, async_tree_memoization, asyncio_websockets, go, async_tree_cpu_io_mixed_tg, pickle_pure_python, pyflate, async_tree_io, sqlglot_optimize, bpe_tokeniser, mypy2, coverage, xml_etree_iterparse, sphinx, mako, k_core, async_tree_none_tg, async_tree_none, typing_runtime_protocols, xml_etree_parse, html5lib, pycparser

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 85.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x