# Results vs. base

- fork: brandtbucher
- ref: jit_off
- machine: darwin-arm64
- commit hash: 1f40ea4
- commit date: 2025-01-08
- overall geometric mean: 1.001x slower
- HPT reliability: 98.17%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| docutils       | 1.40 sec                                                               | 1.40 sec: 1.00x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| coroutines                    | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                           |
| async_tree_eager_tg           | 43.4 ms                                                                | 43.2 ms: 1.01x faster                                           |
| async_tree_eager              | 61.9 ms                                                                | 61.7 ms: 1.00x faster                                           |
| async_tree_io_tg              | 353 ms                                                                 | 352 ms: 1.00x faster                                            |
| async_tree_eager_cpu_io_mixed | 359 ms                                                                 | 359 ms: 1.00x slower                                            |
| Geometric mean                | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (14): async_tree_memoization_tg, async_tree_eager_io_tg, async_tree_io, async_tree_memoization, async_tree_none, async_tree_eager_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_generators, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, asyncio_websockets, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 68.2 ms                                                                | 70.0 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                                | 15.8 ms: 1.02x faster                                           |
| regex_effbot   | 2.08 ms                                                                | 2.05 ms: 1.02x faster                                           |
| regex_dna      | 137 ms                                                                 | 138 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| xml_etree_generate   | 52.3 ms                                                                | 52.4 ms: 1.00x slower                                           |
| json_dumps           | 7.25 ms                                                                | 7.28 ms: 1.00x slower                                           |
| pickle_pure_python   | 197 us                                                                 | 198 us: 1.01x slower                                            |
| unpickle_pure_python | 136 us                                                                 | 137 us: 1.01x slower                                            |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, json_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| django_template | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                           |
| genshi_text     | 13.5 ms                                                                | 13.5 ms: 1.00x slower                                           |
| mako            | 6.92 ms                                                                | 7.24 ms: 1.05x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20250106-darwin-arm64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250108-darwin-arm64-brandtbucher-jit_off-3.14.0a3+-1f40ea4 |
|-------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| gc_traversal                  | 3.23 ms                                                                | 3.16 ms: 1.02x faster                                           |
| regex_v8                      | 16.1 ms                                                                | 15.8 ms: 1.02x faster                                           |
| regex_effbot                  | 2.08 ms                                                                | 2.05 ms: 1.02x faster                                           |
| logging_silent                | 65.6 ns                                                                | 65.0 ns: 1.01x faster                                           |
| thrift                        | 435 us                                                                 | 432 us: 1.01x faster                                            |
| sqlite_synth                  | 1.53 us                                                                | 1.52 us: 1.01x faster                                           |
| coroutines                    | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                           |
| async_tree_eager_tg           | 43.4 ms                                                                | 43.2 ms: 1.01x faster                                           |
| mdp                           | 1.49 sec                                                               | 1.48 sec: 1.01x faster                                          |
| create_gc_cycles              | 1.28 ms                                                                | 1.28 ms: 1.01x faster                                           |
| scimark_sparse_mat_mult       | 2.67 ms                                                                | 2.65 ms: 1.01x faster                                           |
| django_template               | 21.0 ms                                                                | 20.9 ms: 1.00x faster                                           |
| sqlglot_transpile             | 930 us                                                                 | 926 us: 1.00x faster                                            |
| logging_format                | 3.47 us                                                                | 3.45 us: 1.00x faster                                           |
| async_tree_eager              | 61.9 ms                                                                | 61.7 ms: 1.00x faster                                           |
| async_tree_io_tg              | 353 ms                                                                 | 352 ms: 1.00x faster                                            |
| raytrace                      | 168 ms                                                                 | 168 ms: 1.00x slower                                            |
| async_tree_eager_cpu_io_mixed | 359 ms                                                                 | 359 ms: 1.00x slower                                            |
| scimark_fft                   | 171 ms                                                                 | 171 ms: 1.00x slower                                            |
| scimark_sor                   | 78.5 ms                                                                | 78.6 ms: 1.00x slower                                           |
| nqueens                       | 56.0 ms                                                                | 56.2 ms: 1.00x slower                                           |
| go                            | 78.1 ms                                                                | 78.3 ms: 1.00x slower                                           |
| docutils                      | 1.40 sec                                                               | 1.40 sec: 1.00x slower                                          |
| sympy_expand                  | 233 ms                                                                 | 234 ms: 1.00x slower                                            |
| meteor_contest                | 70.9 ms                                                                | 71.1 ms: 1.00x slower                                           |
| xml_etree_generate            | 52.3 ms                                                                | 52.4 ms: 1.00x slower                                           |
| json_dumps                    | 7.25 ms                                                                | 7.28 ms: 1.00x slower                                           |
| pprint_pformat                | 913 ms                                                                 | 916 ms: 1.00x slower                                            |
| bench_mp_pool                 | 60.4 ms                                                                | 60.6 ms: 1.00x slower                                           |
| richards                      | 31.5 ms                                                                | 31.6 ms: 1.00x slower                                           |
| spectral_norm                 | 61.4 ms                                                                | 61.6 ms: 1.00x slower                                           |
| genshi_text                   | 13.5 ms                                                                | 13.5 ms: 1.00x slower                                           |
| sympy_str                     | 138 ms                                                                 | 138 ms: 1.00x slower                                            |
| deepcopy                      | 148 us                                                                 | 149 us: 1.00x slower                                            |
| richards_super                | 35.1 ms                                                                | 35.3 ms: 1.00x slower                                           |
| chaos                         | 37.8 ms                                                                | 38.0 ms: 1.01x slower                                           |
| sqlalchemy_imperative         | 6.42 ms                                                                | 6.46 ms: 1.01x slower                                           |
| pickle_pure_python            | 197 us                                                                 | 198 us: 1.01x slower                                            |
| pprint_safe_repr              | 453 ms                                                                 | 455 ms: 1.01x slower                                            |
| sqlglot_normalize             | 178 ms                                                                 | 179 ms: 1.01x slower                                            |
| bench_thread_pool             | 472 us                                                                 | 475 us: 1.01x slower                                            |
| connected_components          | 295 ms                                                                 | 297 ms: 1.01x slower                                            |
| hexiom                        | 4.12 ms                                                                | 4.14 ms: 1.01x slower                                           |
| sympy_integrate               | 11.1 ms                                                                | 11.1 ms: 1.01x slower                                           |
| unpickle_pure_python          | 136 us                                                                 | 137 us: 1.01x slower                                            |
| sqlalchemy_declarative        | 57.9 ms                                                                | 58.3 ms: 1.01x slower                                           |
| regex_dna                     | 137 ms                                                                 | 138 ms: 1.01x slower                                            |
| scimark_lu                    | 71.9 ms                                                                | 72.6 ms: 1.01x slower                                           |
| generators                    | 22.0 ms                                                                | 22.3 ms: 1.01x slower                                           |
| sympy_sum                     | 72.5 ms                                                                | 73.5 ms: 1.01x slower                                           |
| comprehensions                | 12.2 us                                                                | 12.4 us: 1.02x slower                                           |
| pathlib                       | 22.0 ms                                                                | 22.4 ms: 1.02x slower                                           |
| nbody                         | 68.2 ms                                                                | 70.0 ms: 1.03x slower                                           |
| mako                          | 6.92 ms                                                                | 7.24 ms: 1.05x slower                                           |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (50): async_tree_memoization_tg, xml_etree_parse, subparsers, tomli_loads, async_tree_eager_io_tg, async_tree_io, async_tree_memoization, async_tree_none, deltablue, python_startup, async_tree_eager_io, async_tree_cpu_io_mixed, deepcopy_memo, async_tree_none_tg, many_optionals, async_generators, sqlglot_parse, pyflate, coverage, 2to3, json, regex_compile, bpe_tokeniser, json_loads, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, sqlglot_optimize, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization, xml_etree_process, pycparser, python_startup_no_site, asyncio_websockets, xml_etree_iterparse, pidigits, logging_simple, telco, float, crypto_pyaes, dulwich_log, deepcopy_reduce, k_core, shortest_path, genshi_xml, html5lib, pylint, typing_runtime_protocols, fannkuch, sphinx, async_tree_eager_memoization_tg

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 98.17% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x