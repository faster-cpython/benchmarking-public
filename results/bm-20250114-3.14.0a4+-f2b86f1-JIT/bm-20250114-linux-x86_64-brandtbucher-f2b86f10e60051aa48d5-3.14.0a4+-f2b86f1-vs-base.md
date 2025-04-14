# Results vs. base

- fork: brandtbucher
- ref: f2b86f10e60051aa48d5
- machine: linux-x86_64
- commit hash: f2b86f1
- commit date: 2025-01-14
- overall geometric mean: 1.005x slower
- HPT reliability: 60.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg | 311 ms                                                                 | 308 ms: 1.01x faster                                                         |
| coroutines                | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                        |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_io, async_tree_memoization, async_generators, async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| float          | 68.8 ms                                                                | 71.2 ms: 1.03x slower                                                        |
| nbody          | 85.2 ms                                                                | 96.4 ms: 1.13x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 204 ms                                                                 | 196 ms: 1.04x faster                                                         |
| regex_effbot   | 3.06 ms                                                                | 2.96 ms: 1.03x faster                                                        |
| regex_v8       | 23.8 ms                                                                | 23.9 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads         | 1.85 sec                                                               | 1.84 sec: 1.01x faster                                                       |
| xml_etree_generate  | 77.7 ms                                                                | 78.2 ms: 1.01x slower                                                        |
| xml_etree_iterparse | 94.2 ms                                                                | 94.9 ms: 1.01x slower                                                        |
| pickle_pure_python  | 312 us                                                                 | 317 us: 1.02x slower                                                         |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): unpickle_pure_python, xml_etree_process, json_loads, json_dumps, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): genshi_text, genshi_xml, mako, django_template

All benchmarks:
===============

| Benchmark                 | bm-20250114-linux-x86_64-python-f7ceb317aec498823555-3.14.0a4+-f7ceb31 | bm-20250114-linux-x86_64-brandtbucher-f2b86f10e60051aa48d5-3.14.0a4+-f2b86f1 |
|---------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal              | 4.93 ms                                                                | 4.55 ms: 1.08x faster                                                        |
| regex_dna                 | 204 ms                                                                 | 196 ms: 1.04x faster                                                         |
| regex_effbot              | 3.06 ms                                                                | 2.96 ms: 1.03x faster                                                        |
| sympy_sum                 | 157 ms                                                                 | 155 ms: 1.02x faster                                                         |
| sqlglot_normalize         | 110 ms                                                                 | 109 ms: 1.02x faster                                                         |
| connected_components      | 441 ms                                                                 | 434 ms: 1.02x faster                                                         |
| pprint_pformat            | 1.52 sec                                                               | 1.49 sec: 1.02x faster                                                       |
| generators                | 37.7 ms                                                                | 37.3 ms: 1.01x faster                                                        |
| scimark_lu                | 113 ms                                                                 | 112 ms: 1.01x faster                                                         |
| sqlglot_optimize          | 55.2 ms                                                                | 54.7 ms: 1.01x faster                                                        |
| richards                  | 43.8 ms                                                                | 43.4 ms: 1.01x faster                                                        |
| pyflate                   | 453 ms                                                                 | 449 ms: 1.01x faster                                                         |
| typing_runtime_protocols  | 168 us                                                                 | 167 us: 1.01x faster                                                         |
| sqlalchemy_imperative     | 16.9 ms                                                                | 16.8 ms: 1.01x faster                                                        |
| pidigits                  | 188 ms                                                                 | 186 ms: 1.01x faster                                                         |
| async_tree_memoization_tg | 311 ms                                                                 | 308 ms: 1.01x faster                                                         |
| tomli_loads               | 1.85 sec                                                               | 1.84 sec: 1.01x faster                                                       |
| sqlglot_transpile         | 1.60 ms                                                                | 1.59 ms: 1.01x faster                                                        |
| sympy_expand              | 475 ms                                                                 | 472 ms: 1.01x faster                                                         |
| bench_mp_pool             | 81.1 ms                                                                | 80.7 ms: 1.01x faster                                                        |
| many_optionals            | 975 us                                                                 | 970 us: 1.01x faster                                                         |
| create_gc_cycles          | 2.45 ms                                                                | 2.44 ms: 1.00x faster                                                        |
| shortest_path             | 481 ms                                                                 | 478 ms: 1.00x faster                                                         |
| sympy_str                 | 281 ms                                                                 | 280 ms: 1.00x faster                                                         |
| python_startup            | 12.9 ms                                                                | 12.8 ms: 1.00x faster                                                        |
| 2to3                      | 260 ms                                                                 | 261 ms: 1.00x slower                                                         |
| sqlalchemy_declarative    | 132 ms                                                                 | 132 ms: 1.00x slower                                                         |
| go                        | 134 ms                                                                 | 135 ms: 1.01x slower                                                         |
| bpe_tokeniser             | 4.40 sec                                                               | 4.42 sec: 1.01x slower                                                       |
| deltablue                 | 3.25 ms                                                                | 3.26 ms: 1.01x slower                                                        |
| xml_etree_generate        | 77.7 ms                                                                | 78.2 ms: 1.01x slower                                                        |
| regex_v8                  | 23.8 ms                                                                | 23.9 ms: 1.01x slower                                                        |
| xml_etree_iterparse       | 94.2 ms                                                                | 94.9 ms: 1.01x slower                                                        |
| mdp                       | 2.57 sec                                                               | 2.59 sec: 1.01x slower                                                       |
| deepcopy_memo             | 29.7 us                                                                | 30.0 us: 1.01x slower                                                        |
| scimark_monte_carlo       | 62.2 ms                                                                | 62.8 ms: 1.01x slower                                                        |
| nqueens                   | 90.1 ms                                                                | 90.9 ms: 1.01x slower                                                        |
| meteor_contest            | 108 ms                                                                 | 109 ms: 1.01x slower                                                         |
| logging_format            | 6.31 us                                                                | 6.38 us: 1.01x slower                                                        |
| logging_silent            | 109 ns                                                                 | 110 ns: 1.01x slower                                                         |
| fannkuch                  | 383 ms                                                                 | 388 ms: 1.01x slower                                                         |
| coverage                  | 90.7 ms                                                                | 91.8 ms: 1.01x slower                                                        |
| subparsers                | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                                        |
| deepcopy                  | 267 us                                                                 | 271 us: 1.01x slower                                                         |
| pickle_pure_python        | 312 us                                                                 | 317 us: 1.02x slower                                                         |
| coroutines                | 23.8 ms                                                                | 24.2 ms: 1.02x slower                                                        |
| chaos                     | 61.1 ms                                                                | 62.8 ms: 1.03x slower                                                        |
| raytrace                  | 289 ms                                                                 | 298 ms: 1.03x slower                                                         |
| float                     | 68.8 ms                                                                | 71.2 ms: 1.03x slower                                                        |
| crypto_pyaes              | 67.6 ms                                                                | 70.7 ms: 1.05x slower                                                        |
| scimark_sor               | 112 ms                                                                 | 118 ms: 1.05x slower                                                         |
| scimark_fft               | 314 ms                                                                 | 333 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult   | 4.44 ms                                                                | 4.78 ms: 1.08x slower                                                        |
| nbody                     | 85.2 ms                                                                | 96.4 ms: 1.13x slower                                                        |
| spectral_norm             | 102 ms                                                                 | 120 ms: 1.18x slower                                                         |
| Geometric mean            | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (41): unpickle_pure_python, genshi_text, telco, async_tree_io, xml_etree_process, k_core, regex_compile, json, genshi_xml, async_tree_memoization, richards_super, async_generators, pprint_safe_repr, json_loads, pylint, async_tree_cpu_io_mixed, async_tree_none_tg, sympy_integrate, docutils, python_startup_no_site, comprehensions, bench_thread_pool, json_dumps, sqlglot_parse, asyncio_websockets, pycparser, async_tree_io_tg, mako, sphinx, django_template, xml_etree_parse, hexiom, async_tree_none, async_tree_cpu_io_mixed_tg, html5lib, dulwich_log, thrift, logging_simple, sqlite_synth, pathlib, deepcopy_reduce

- Geometric mean (including insignificant results): 1.005x slower

# HPT report

- Reliability score: 60.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x