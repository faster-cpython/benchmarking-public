# Results vs. base

- fork: zooba
- ref: gh_91349
- machine: darwin-arm64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.001x faster
- HPT reliability: 71.71%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| docutils       | 1.45 sec                                                               | 1.44 sec: 1.00x faster                                    |
| Geometric mean | (ref)                                                                  | 1.00x faster                                              |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| asyncio_websockets | 242 ms                                                                 | 242 ms: 1.00x slower                                      |
| async_tree_eager   | 61.2 ms                                                                | 61.4 ms: 1.00x slower                                     |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                              |

Benchmark hidden because not significant (17): async_tree_eager_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, async_tree_eager_memoization, async_tree_io, async_tree_eager_io, async_tree_memoization_tg, async_tree_memoization, async_tree_io_tg, async_tree_eager_tg, coroutines, async_generators, async_tree_none_tg, async_tree_eager_io_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| nbody          | 72.9 ms                                                                | 72.9 ms: 1.00x slower                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                              |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| regex_effbot   | 2.27 ms                                                                | 2.24 ms: 1.01x faster                                     |
| regex_v8       | 15.9 ms                                                                | 15.7 ms: 1.01x faster                                     |
| regex_dna      | 141 ms                                                                 | 140 ms: 1.00x faster                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| pickle_pure_python | 205 us                                                                 | 203 us: 1.01x faster                                      |
| tomli_loads        | 1.24 sec                                                               | 1.24 sec: 1.01x faster                                    |
| xml_etree_process  | 38.9 ms                                                                | 39.1 ms: 1.00x slower                                     |
| xml_etree_generate | 53.7 ms                                                                | 54.0 ms: 1.00x slower                                     |
| json_loads         | 17.9 us                                                                | 18.0 us: 1.01x slower                                     |
| json_dumps         | 7.30 ms                                                                | 7.36 ms: 1.01x slower                                     |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                              |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                                | 12.7 ms: 1.03x faster                                     |
| python_startup         | 17.4 ms                                                                | 17.0 ms: 1.02x faster                                     |
| Geometric mean         | (ref)                                                                  | 1.03x faster                                              |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| genshi_text    | 14.1 ms                                                                | 14.2 ms: 1.01x slower                                     |
| genshi_xml     | 28.9 ms                                                                | 29.2 ms: 1.01x slower                                     |
| Geometric mean | (ref)                                                                  | 1.00x slower                                              |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b | bm-20250319-darwin-arm64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------:|
| python_startup_no_site   | 13.2 ms                                                                | 12.7 ms: 1.03x faster                                     |
| python_startup           | 17.4 ms                                                                | 17.0 ms: 1.02x faster                                     |
| regex_effbot             | 2.27 ms                                                                | 2.24 ms: 1.01x faster                                     |
| pickle_pure_python       | 205 us                                                                 | 203 us: 1.01x faster                                      |
| regex_v8                 | 15.9 ms                                                                | 15.7 ms: 1.01x faster                                     |
| pathlib                  | 23.8 ms                                                                | 23.7 ms: 1.01x faster                                     |
| tomli_loads              | 1.24 sec                                                               | 1.24 sec: 1.01x faster                                    |
| scimark_sparse_mat_mult  | 2.96 ms                                                                | 2.95 ms: 1.01x faster                                     |
| mdp                      | 1.49 sec                                                               | 1.48 sec: 1.01x faster                                    |
| sqlite_synth             | 1.55 us                                                                | 1.54 us: 1.00x faster                                     |
| scimark_lu               | 74.6 ms                                                                | 74.4 ms: 1.00x faster                                     |
| regex_dna                | 141 ms                                                                 | 140 ms: 1.00x faster                                      |
| scimark_sor              | 79.1 ms                                                                | 78.9 ms: 1.00x faster                                     |
| telco                    | 4.58 ms                                                                | 4.57 ms: 1.00x faster                                     |
| nqueens                  | 65.3 ms                                                                | 65.0 ms: 1.00x faster                                     |
| dulwich_log              | 24.6 ms                                                                | 24.6 ms: 1.00x faster                                     |
| docutils                 | 1.45 sec                                                               | 1.44 sec: 1.00x faster                                    |
| pyflate                  | 320 ms                                                                 | 320 ms: 1.00x faster                                      |
| go                       | 82.2 ms                                                                | 82.1 ms: 1.00x faster                                     |
| scimark_monte_carlo      | 43.3 ms                                                                | 43.2 ms: 1.00x faster                                     |
| bpe_tokeniser            | 3.20 sec                                                               | 3.20 sec: 1.00x faster                                    |
| spectral_norm            | 75.7 ms                                                                | 75.7 ms: 1.00x faster                                     |
| nbody                    | 72.9 ms                                                                | 72.9 ms: 1.00x slower                                     |
| hexiom                   | 4.44 ms                                                                | 4.44 ms: 1.00x slower                                     |
| asyncio_websockets       | 242 ms                                                                 | 242 ms: 1.00x slower                                      |
| crypto_pyaes             | 58.3 ms                                                                | 58.4 ms: 1.00x slower                                     |
| comprehensions           | 11.6 us                                                                | 11.6 us: 1.00x slower                                     |
| sqlalchemy_declarative   | 58.9 ms                                                                | 59.0 ms: 1.00x slower                                     |
| connected_components     | 308 ms                                                                 | 308 ms: 1.00x slower                                      |
| async_tree_eager         | 61.2 ms                                                                | 61.4 ms: 1.00x slower                                     |
| xml_etree_process        | 38.9 ms                                                                | 39.1 ms: 1.00x slower                                     |
| gc_traversal             | 3.11 ms                                                                | 3.12 ms: 1.00x slower                                     |
| thrift                   | 440 us                                                                 | 442 us: 1.00x slower                                      |
| create_gc_cycles         | 1.29 ms                                                                | 1.29 ms: 1.00x slower                                     |
| xml_etree_generate       | 53.7 ms                                                                | 54.0 ms: 1.00x slower                                     |
| sympy_integrate          | 11.5 ms                                                                | 11.6 ms: 1.00x slower                                     |
| json_loads               | 17.9 us                                                                | 18.0 us: 1.01x slower                                     |
| fannkuch                 | 277 ms                                                                 | 279 ms: 1.01x slower                                      |
| genshi_text              | 14.1 ms                                                                | 14.2 ms: 1.01x slower                                     |
| typing_runtime_protocols | 93.6 us                                                                | 94.2 us: 1.01x slower                                     |
| json_dumps               | 7.30 ms                                                                | 7.36 ms: 1.01x slower                                     |
| genshi_xml               | 28.9 ms                                                                | 29.2 ms: 1.01x slower                                     |
| json                     | 3.13 ms                                                                | 3.16 ms: 1.01x slower                                     |
| meteor_contest           | 73.0 ms                                                                | 73.8 ms: 1.01x slower                                     |
| logging_silent           | 66.2 ns                                                                | 66.9 ns: 1.01x slower                                     |
| Geometric mean           | (ref)                                                                  | 1.00x faster                                              |

Benchmark hidden because not significant (60): bench_mp_pool, subparsers, pylint, many_optionals, richards, sympy_str, sqlglot_v2_parse, xml_etree_parse, regex_compile, sphinx, scimark_fft, sqlglot_v2_optimize, deepcopy_memo, chaos, logging_simple, pidigits, float, async_tree_eager_memoization_tg, sympy_expand, dask, deepcopy, k_core, sqlglot_v2_normalize, pprint_pformat, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed, unpickle_pure_python, async_tree_eager_memoization, mako, shortest_path, async_tree_io, sqlglot_v2_transpile, django_template, async_tree_eager_io, raytrace, logging_format, async_tree_memoization_tg, html5lib, async_tree_memoization, 2to3, generators, xml_etree_iterparse, async_tree_io_tg, richards_super, pycparser, bench_thread_pool, deepcopy_reduce, sympy_sum, async_tree_eager_tg, sqlalchemy_imperative, coroutines, pprint_safe_repr, async_generators, coverage, async_tree_none_tg, async_tree_eager_io_tg, async_tree_none, deltablue

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 71.71% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x