# Results vs. base

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.002x slower
- HPT reliability: 99.40%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 175 ms                                                                 | 176 ms: 1.01x slower                                                  |
| docutils       | 1.50 sec                                                               | 1.50 sec: 1.00x slower                                                |
| sphinx         | 607 ms                                                                 | 643 ms: 1.06x slower                                                  |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_generators | 269 ms                                                                 | 267 ms: 1.01x faster                                                  |
| async_tree_io_tg | 402 ms                                                                 | 401 ms: 1.00x faster                                                  |
| Geometric mean   | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (17): async_tree_eager_memoization, async_tree_eager_cpu_io_mixed, async_tree_memoization_tg, async_tree_eager, async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_eager_cpu_io_mixed_tg, async_tree_memoization, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_none, async_tree_eager_memoization_tg, async_tree_io, async_tree_eager_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                                | 91.7 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 78.1 ms                                                                | 77.9 ms: 1.00x faster                                                 |
| regex_dna      | 140 ms                                                                 | 141 ms: 1.00x slower                                                  |
| regex_v8       | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                 |
| regex_effbot   | 2.24 ms                                                                | 2.27 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads        | 1.44 sec                                                               | 1.43 sec: 1.01x faster                                                |
| pickle_pure_python | 231 us                                                                 | 230 us: 1.00x faster                                                  |
| json_dumps         | 7.52 ms                                                                | 7.59 ms: 1.01x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (6): xml_etree_parse, unpickle_pure_python, json_loads, xml_etree_generate, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                                | 19.0 ms: 1.00x faster                                                 |
| python_startup_no_site | 14.1 ms                                                                | 14.0 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 24.3 ms                                                                | 24.2 ms: 1.01x faster                                                 |
| genshi_text     | 16.2 ms                                                                | 16.3 ms: 1.00x slower                                                 |
| genshi_xml      | 33.6 ms                                                                | 33.8 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20250305-darwin-arm64-python-d7bb7c781771650a4edc-3.14.0a5+-d7bb7c7 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| sympy_sum                | 80.1 ms                                                                | 79.2 ms: 1.01x faster                                                 |
| nbody                    | 92.5 ms                                                                | 91.7 ms: 1.01x faster                                                 |
| deltablue                | 2.78 ms                                                                | 2.76 ms: 1.01x faster                                                 |
| tomli_loads              | 1.44 sec                                                               | 1.43 sec: 1.01x faster                                                |
| async_generators         | 269 ms                                                                 | 267 ms: 1.01x faster                                                  |
| sqlite_synth             | 1.55 us                                                                | 1.54 us: 1.01x faster                                                 |
| meteor_contest           | 78.3 ms                                                                | 77.8 ms: 1.01x faster                                                 |
| django_template          | 24.3 ms                                                                | 24.2 ms: 1.01x faster                                                 |
| logging_silent           | 73.6 ns                                                                | 73.2 ns: 1.00x faster                                                 |
| sympy_integrate          | 12.3 ms                                                                | 12.2 ms: 1.00x faster                                                 |
| python_startup           | 19.1 ms                                                                | 19.0 ms: 1.00x faster                                                 |
| async_tree_io_tg         | 402 ms                                                                 | 401 ms: 1.00x faster                                                  |
| telco                    | 4.76 ms                                                                | 4.74 ms: 1.00x faster                                                 |
| go                       | 95.1 ms                                                                | 94.8 ms: 1.00x faster                                                 |
| regex_compile            | 78.1 ms                                                                | 77.9 ms: 1.00x faster                                                 |
| python_startup_no_site   | 14.1 ms                                                                | 14.0 ms: 1.00x faster                                                 |
| chaos                    | 44.1 ms                                                                | 44.0 ms: 1.00x faster                                                 |
| pprint_pformat           | 1.11 sec                                                               | 1.11 sec: 1.00x faster                                                |
| sqlglot_transpile        | 1.07 ms                                                                | 1.07 ms: 1.00x faster                                                 |
| logging_format           | 4.04 us                                                                | 4.04 us: 1.00x faster                                                 |
| pickle_pure_python       | 231 us                                                                 | 230 us: 1.00x faster                                                  |
| logging_simple           | 3.72 us                                                                | 3.71 us: 1.00x faster                                                 |
| hexiom                   | 5.26 ms                                                                | 5.27 ms: 1.00x slower                                                 |
| bpe_tokeniser            | 3.24 sec                                                               | 3.24 sec: 1.00x slower                                                |
| richards_super           | 42.8 ms                                                                | 42.9 ms: 1.00x slower                                                 |
| sqlglot_normalize        | 196 ms                                                                 | 196 ms: 1.00x slower                                                  |
| raytrace                 | 212 ms                                                                 | 212 ms: 1.00x slower                                                  |
| deepcopy                 | 168 us                                                                 | 168 us: 1.00x slower                                                  |
| mdp                      | 1.55 sec                                                               | 1.56 sec: 1.00x slower                                                |
| docutils                 | 1.50 sec                                                               | 1.50 sec: 1.00x slower                                                |
| deepcopy_memo            | 20.9 us                                                                | 20.9 us: 1.00x slower                                                 |
| genshi_text              | 16.2 ms                                                                | 16.3 ms: 1.00x slower                                                 |
| sqlglot_optimize         | 35.7 ms                                                                | 35.9 ms: 1.00x slower                                                 |
| crypto_pyaes             | 59.0 ms                                                                | 59.2 ms: 1.00x slower                                                 |
| regex_dna                | 140 ms                                                                 | 141 ms: 1.00x slower                                                  |
| pprint_safe_repr         | 546 ms                                                                 | 549 ms: 1.00x slower                                                  |
| 2to3                     | 175 ms                                                                 | 176 ms: 1.01x slower                                                  |
| create_gc_cycles         | 1.27 ms                                                                | 1.28 ms: 1.01x slower                                                 |
| typing_runtime_protocols | 101 us                                                                 | 102 us: 1.01x slower                                                  |
| genshi_xml               | 33.6 ms                                                                | 33.8 ms: 1.01x slower                                                 |
| json_dumps               | 7.52 ms                                                                | 7.59 ms: 1.01x slower                                                 |
| generators               | 29.0 ms                                                                | 29.3 ms: 1.01x slower                                                 |
| regex_v8                 | 16.7 ms                                                                | 16.9 ms: 1.01x slower                                                 |
| regex_effbot             | 2.24 ms                                                                | 2.27 ms: 1.01x slower                                                 |
| scimark_sor              | 92.7 ms                                                                | 95.4 ms: 1.03x slower                                                 |
| sphinx                   | 607 ms                                                                 | 643 ms: 1.06x slower                                                  |
| scimark_sparse_mat_mult  | 3.06 ms                                                                | 3.28 ms: 1.07x slower                                                 |
| spectral_norm            | 77.8 ms                                                                | 84.4 ms: 1.09x slower                                                 |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (57): deepcopy_reduce, xml_etree_parse, subparsers, pycparser, async_tree_eager_memoization, unpickle_pure_python, bench_mp_pool, async_tree_eager_cpu_io_mixed, json_loads, xml_etree_generate, async_tree_memoization_tg, bench_thread_pool, scimark_lu, sqlalchemy_imperative, async_tree_eager, async_tree_cpu_io_mixed, nqueens, asyncio_websockets, coroutines, async_tree_eager_cpu_io_mixed_tg, richards, pidigits, json, pyflate, sqlalchemy_declarative, async_tree_memoization, scimark_fft, async_tree_eager_io, async_tree_cpu_io_mixed_tg, mako, async_tree_eager_io_tg, comprehensions, async_tree_none, fannkuch, k_core, connected_components, sympy_expand, shortest_path, async_tree_eager_memoization_tg, xml_etree_process, scimark_monte_carlo, dulwich_log, async_tree_io, sympy_str, dask, thrift, async_tree_eager_tg, async_tree_none_tg, sqlglot_parse, xml_etree_iterparse, coverage, html5lib, gc_traversal, pylint, pathlib, many_optionals, float

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 99.40% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x