# Results vs. base

- fork: brandtbucher
- ref: nojit
- machine: linux-x86_64
- commit hash: f098037
- commit date: 2025-01-07
- overall geometric mean: 1.001x slower
- HPT reliability: 83.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 293 ms                                                                       | 290 ms: 1.01x faster                                                |
| docutils       | 2.98 sec                                                                     | 2.96 sec: 1.01x faster                                              |
| sphinx         | 1.15 sec                                                                     | 1.14 sec: 1.01x faster                                              |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                        |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_generators | 460 ms                                                                       | 467 ms: 1.01x slower                                                |
| Geometric mean   | (ref)                                                                        | 1.00x faster                                                        |

Benchmark hidden because not significant (10): async_tree_none, async_tree_cpu_io_mixed, asyncio_websockets, coroutines, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_memoization_tg, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 253 ms                                                                       | 255 ms: 1.01x slower                                                |
| nbody          | 93.7 ms                                                                      | 98.2 ms: 1.05x slower                                               |
| Geometric mean | (ref)                                                                        | 1.02x slower                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 235 ms                                                                       | 231 ms: 1.02x faster                                                |
| regex_compile  | 139 ms                                                                       | 138 ms: 1.01x faster                                                |
| regex_effbot   | 3.09 ms                                                                      | 3.17 ms: 1.03x slower                                               |
| regex_v8       | 24.9 ms                                                                      | 25.7 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                        | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark       | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|-----------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| xml_etree_parse | 135 ms                                                                       | 137 ms: 1.02x slower                                                |
| Geometric mean  | (ref)                                                                        | 1.00x slower                                                        |

Benchmark hidden because not significant (8): unpickle_pure_python, xml_etree_process, xml_etree_generate, json_dumps, json_loads, xml_etree_iterparse, tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (4): django_template, mako, genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20250106-pythonperf2-x86_64-python-7363476b6405e3d288a6-3.14.0a3+-7363476 | bm-20250107-pythonperf2-x86_64-brandtbucher-nojit-3.14.0a3+-f098037 |
|--------------------------|:----------------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators               | 41.3 ms                                                                      | 39.9 ms: 1.03x faster                                               |
| scimark_sor              | 101 ms                                                                       | 98.7 ms: 1.02x faster                                               |
| scimark_lu               | 96.6 ms                                                                      | 94.7 ms: 1.02x faster                                               |
| thrift                   | 895 us                                                                       | 879 us: 1.02x faster                                                |
| regex_dna                | 235 ms                                                                       | 231 ms: 1.02x faster                                                |
| pycparser                | 1.28 sec                                                                     | 1.26 sec: 1.01x faster                                              |
| 2to3                     | 293 ms                                                                       | 290 ms: 1.01x faster                                                |
| subparsers               | 23.4 ms                                                                      | 23.2 ms: 1.01x faster                                               |
| mdp                      | 2.61 sec                                                                     | 2.58 sec: 1.01x faster                                              |
| sphinx                   | 1.15 sec                                                                     | 1.14 sec: 1.01x faster                                              |
| sympy_expand             | 526 ms                                                                       | 520 ms: 1.01x faster                                                |
| connected_components     | 407 ms                                                                       | 403 ms: 1.01x faster                                                |
| sqlalchemy_declarative   | 148 ms                                                                       | 146 ms: 1.01x faster                                                |
| logging_simple           | 6.69 us                                                                      | 6.63 us: 1.01x faster                                               |
| sqlglot_parse            | 1.37 ms                                                                      | 1.36 ms: 1.01x faster                                               |
| meteor_contest           | 133 ms                                                                       | 132 ms: 1.01x faster                                                |
| typing_runtime_protocols | 181 us                                                                       | 180 us: 1.01x faster                                                |
| many_optionals           | 1.06 ms                                                                      | 1.05 ms: 1.01x faster                                               |
| sympy_str                | 307 ms                                                                       | 305 ms: 1.01x faster                                                |
| regex_compile            | 139 ms                                                                       | 138 ms: 1.01x faster                                                |
| docutils                 | 2.98 sec                                                                     | 2.96 sec: 1.01x faster                                              |
| crypto_pyaes             | 74.9 ms                                                                      | 74.5 ms: 1.01x faster                                               |
| sqlglot_optimize         | 61.6 ms                                                                      | 61.4 ms: 1.00x faster                                               |
| shortest_path            | 439 ms                                                                       | 438 ms: 1.00x faster                                                |
| deltablue                | 3.49 ms                                                                      | 3.51 ms: 1.00x slower                                               |
| logging_silent           | 100 ns                                                                       | 101 ns: 1.00x slower                                                |
| sqlite_synth             | 2.80 us                                                                      | 2.82 us: 1.01x slower                                               |
| pathlib                  | 16.4 ms                                                                      | 16.5 ms: 1.01x slower                                               |
| bpe_tokeniser            | 4.70 sec                                                                     | 4.73 sec: 1.01x slower                                              |
| hexiom                   | 7.37 ms                                                                      | 7.42 ms: 1.01x slower                                               |
| deepcopy_reduce          | 2.96 us                                                                      | 2.98 us: 1.01x slower                                               |
| pidigits                 | 253 ms                                                                       | 255 ms: 1.01x slower                                                |
| comprehensions           | 19.1 us                                                                      | 19.3 us: 1.01x slower                                               |
| deepcopy                 | 296 us                                                                       | 299 us: 1.01x slower                                                |
| coverage                 | 78.4 ms                                                                      | 79.4 ms: 1.01x slower                                               |
| async_generators         | 460 ms                                                                       | 467 ms: 1.01x slower                                                |
| xml_etree_parse          | 135 ms                                                                       | 137 ms: 1.02x slower                                                |
| go                       | 142 ms                                                                       | 145 ms: 1.02x slower                                                |
| pyflate                  | 453 ms                                                                       | 463 ms: 1.02x slower                                                |
| pprint_pformat           | 1.60 sec                                                                     | 1.64 sec: 1.02x slower                                              |
| scimark_sparse_mat_mult  | 4.78 ms                                                                      | 4.88 ms: 1.02x slower                                               |
| fannkuch                 | 374 ms                                                                       | 382 ms: 1.02x slower                                                |
| pprint_safe_repr         | 788 ms                                                                       | 807 ms: 1.02x slower                                                |
| raytrace                 | 326 ms                                                                       | 334 ms: 1.02x slower                                                |
| scimark_fft              | 292 ms                                                                       | 300 ms: 1.03x slower                                                |
| regex_effbot             | 3.09 ms                                                                      | 3.17 ms: 1.03x slower                                               |
| nqueens                  | 99.2 ms                                                                      | 102 ms: 1.03x slower                                                |
| regex_v8                 | 24.9 ms                                                                      | 25.7 ms: 1.04x slower                                               |
| nbody                    | 93.7 ms                                                                      | 98.2 ms: 1.05x slower                                               |
| Geometric mean           | (ref)                                                                        | 1.00x slower                                                        |

Benchmark hidden because not significant (48): bench_mp_pool, async_tree_none, mypy2, pylint, async_tree_cpu_io_mixed, k_core, html5lib, asyncio_websockets, telco, sqlglot_transpile, scimark_monte_carlo, unpickle_pure_python, django_template, xml_etree_process, sqlalchemy_imperative, dulwich_log, coroutines, sympy_integrate, deepcopy_memo, async_tree_cpu_io_mixed_tg, mako, xml_etree_generate, async_tree_memoization, create_gc_cycles, json_dumps, json, json_loads, float, async_tree_none_tg, sqlglot_normalize, logging_format, python_startup_no_site, richards_super, xml_etree_iterparse, python_startup, spectral_norm, gc_traversal, tomli_loads, async_tree_io, genshi_text, richards, sympy_sum, pickle_pure_python, async_tree_memoization_tg, bench_thread_pool, async_tree_io_tg, chaos, genshi_xml

- Geometric mean (including insignificant results): 1.001x slower

# HPT report

- Reliability score: 83.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x