# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: darwin-arm64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.002x slower
- HPT reliability: 97.50%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 166 ms                                                                 | 197 ms: 1.18x slower                                           |
| docutils       | 1.45 sec                                                               | 1.52 sec: 1.05x slower                                         |
| Geometric mean | (ref)                                                                  | 1.06x slower                                                   |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_generators              | 254 ms                                                                 | 250 ms: 1.01x faster                                           |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 358 ms: 1.00x slower                                           |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (17): async_tree_io_tg, async_tree_eager_io_tg, async_tree_eager_io, async_tree_eager, async_tree_none_tg, async_tree_eager_tg, asyncio_websockets, async_tree_eager_memoization, coroutines, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 68.4 ms                                                                | 68.6 ms: 1.00x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 141 ms: 1.00x slower                                           |
| regex_v8       | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                          |
| regex_effbot   | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| tomli_loads          | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                         |
| xml_etree_generate   | 53.8 ms                                                                | 53.4 ms: 1.01x faster                                          |
| unpickle_pure_python | 147 us                                                                 | 147 us: 1.00x faster                                           |
| xml_etree_iterparse  | 70.6 ms                                                                | 71.1 ms: 1.01x slower                                          |
| xml_etree_parse      | 98.0 ms                                                                | 102 ms: 1.05x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (4): xml_etree_process, pickle_pure_python, json_dumps, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 14.0 ms                                                                | 13.9 ms: 1.01x faster                                          |
| python_startup         | 18.8 ms                                                                | 18.7 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_xml, django_template, mako, genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_generators              | 254 ms                                                                 | 250 ms: 1.01x faster                                           |
| python_startup_no_site        | 14.0 ms                                                                | 13.9 ms: 1.01x faster                                          |
| richards                      | 34.7 ms                                                                | 34.2 ms: 1.01x faster                                          |
| tomli_loads                   | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                         |
| scimark_sparse_mat_mult       | 2.72 ms                                                                | 2.69 ms: 1.01x faster                                          |
| sympy_integrate               | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                          |
| python_startup                | 18.8 ms                                                                | 18.7 ms: 1.01x faster                                          |
| json                          | 2.89 ms                                                                | 2.87 ms: 1.01x faster                                          |
| richards_super                | 38.3 ms                                                                | 38.0 ms: 1.01x faster                                          |
| xml_etree_generate            | 53.8 ms                                                                | 53.4 ms: 1.01x faster                                          |
| scimark_monte_carlo           | 50.1 ms                                                                | 49.8 ms: 1.01x faster                                          |
| sympy_str                     | 140 ms                                                                 | 139 ms: 1.00x faster                                           |
| sqlalchemy_imperative         | 6.78 ms                                                                | 6.74 ms: 1.00x faster                                          |
| thrift                        | 459 us                                                                 | 457 us: 1.00x faster                                           |
| sympy_expand                  | 236 ms                                                                 | 235 ms: 1.00x faster                                           |
| sqlglot_transpile             | 1.01 ms                                                                | 1.01 ms: 1.00x faster                                          |
| unpickle_pure_python          | 147 us                                                                 | 147 us: 1.00x faster                                           |
| gc_traversal                  | 3.11 ms                                                                | 3.10 ms: 1.00x faster                                          |
| many_optionals                | 446 us                                                                 | 444 us: 1.00x faster                                           |
| spectral_norm                 | 60.9 ms                                                                | 60.7 ms: 1.00x faster                                          |
| raytrace                      | 204 ms                                                                 | 204 ms: 1.00x faster                                           |
| pyflate                       | 300 ms                                                                 | 300 ms: 1.00x slower                                           |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 358 ms: 1.00x slower                                           |
| create_gc_cycles              | 1.28 ms                                                                | 1.28 ms: 1.00x slower                                          |
| deepcopy_reduce               | 1.56 us                                                                | 1.57 us: 1.00x slower                                          |
| sqlite_synth                  | 1.54 us                                                                | 1.55 us: 1.00x slower                                          |
| nbody                         | 68.4 ms                                                                | 68.6 ms: 1.00x slower                                          |
| regex_dna                     | 141 ms                                                                 | 141 ms: 1.00x slower                                           |
| scimark_sor                   | 85.2 ms                                                                | 85.6 ms: 1.00x slower                                          |
| chaos                         | 39.2 ms                                                                | 39.4 ms: 1.01x slower                                          |
| fannkuch                      | 245 ms                                                                 | 247 ms: 1.01x slower                                           |
| regex_v8                      | 16.7 ms                                                                | 16.8 ms: 1.01x slower                                          |
| pprint_safe_repr              | 460 ms                                                                 | 464 ms: 1.01x slower                                           |
| xml_etree_iterparse           | 70.6 ms                                                                | 71.1 ms: 1.01x slower                                          |
| regex_effbot                  | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                          |
| pathlib                       | 22.3 ms                                                                | 23.1 ms: 1.03x slower                                          |
| xml_etree_parse               | 98.0 ms                                                                | 102 ms: 1.05x slower                                           |
| docutils                      | 1.45 sec                                                               | 1.52 sec: 1.05x slower                                         |
| 2to3                          | 166 ms                                                                 | 197 ms: 1.18x slower                                           |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (66): shortest_path, sympy_sum, async_tree_io_tg, sqlglot_parse, scimark_fft, genshi_xml, async_tree_eager_io_tg, logging_format, k_core, deepcopy, sqlglot_normalize, bench_thread_pool, django_template, mdp, sqlglot_optimize, telco, nqueens, scimark_lu, async_tree_eager_io, xml_etree_process, go, logging_simple, regex_compile, async_tree_eager, async_tree_none_tg, bench_mp_pool, float, subparsers, pickle_pure_python, async_tree_eager_tg, asyncio_websockets, async_tree_eager_memoization, typing_runtime_protocols, coroutines, pidigits, json_dumps, bpe_tokeniser, generators, json_loads, crypto_pyaes, connected_components, async_tree_memoization_tg, dask, dulwich_log, hexiom, deepcopy_memo, pprint_pformat, async_tree_io, meteor_contest, sqlalchemy_declarative, mako, async_tree_cpu_io_mixed_tg, comprehensions, async_tree_cpu_io_mixed, async_tree_memoization, deltablue, async_tree_eager_cpu_io_mixed_tg, genshi_text, logging_silent, async_tree_eager_memoization_tg, async_tree_none, html5lib, pylint, coverage, pycparser, sphinx

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.50% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x