# Results vs. base

- fork: mdboom
- ref: aa_test_2025
- machine: darwin-arm64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.001x faster
- HPT reliability: 98.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 189 ms                                                                 | 189 ms: 1.00x slower                                           |
| sphinx         | 614 ms                                                                 | 624 ms: 1.02x slower                                           |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                   |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none_tg              | 137 ms                                                                 | 136 ms: 1.01x faster                                           |
| async_tree_none                 | 161 ms                                                                 | 160 ms: 1.01x faster                                           |
| async_tree_memoization_tg       | 177 ms                                                                 | 176 ms: 1.00x faster                                           |
| async_tree_eager_memoization_tg | 162 ms                                                                 | 161 ms: 1.00x faster                                           |
| async_tree_eager_tg             | 120 ms                                                                 | 119 ms: 1.00x faster                                           |
| async_generators                | 262 ms                                                                 | 261 ms: 1.00x faster                                           |
| asyncio_websockets              | 238 ms                                                                 | 237 ms: 1.00x faster                                           |
| async_tree_cpu_io_mixed         | 407 ms                                                                 | 409 ms: 1.00x slower                                           |
| Geometric mean                  | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (11): async_tree_memoization, async_tree_eager, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_io_tg, coroutines, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, async_tree_eager_io

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): float, nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_effbot   | 2.09 ms                                                                | 2.08 ms: 1.01x faster                                          |
| regex_v8       | 15.6 ms                                                                | 15.6 ms: 1.00x faster                                          |
| regex_compile  | 77.0 ms                                                                | 76.9 ms: 1.00x faster                                          |
| regex_dna      | 137 ms                                                                 | 137 ms: 1.00x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark         | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse   | 100 ms                                                                 | 95.6 ms: 1.05x faster                                          |
| json_dumps        | 8.01 ms                                                                | 7.94 ms: 1.01x faster                                          |
| xml_etree_process | 45.8 ms                                                                | 45.6 ms: 1.00x faster                                          |
| json_loads        | 17.7 us                                                                | 17.8 us: 1.00x slower                                          |
| Geometric mean    | (ref)                                                                  | 1.01x faster                                                   |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_pure_python, unpickle_pure_python, xml_etree_generate, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                          |
| python_startup         | 20.6 ms                                                                | 20.5 ms: 1.01x faster                                          |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| genshi_xml      | 33.4 ms                                                                | 33.2 ms: 1.01x faster                                          |
| django_template | 24.7 ms                                                                | 24.5 ms: 1.01x faster                                          |
| mako            | 9.95 ms                                                                | 9.97 ms: 1.00x slower                                          |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                       | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250121-darwin-arm64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|---------------------------------|:----------------------------------------------------------------------:|:--------------------------------------------------------------:|
| xml_etree_parse                 | 100 ms                                                                 | 95.6 ms: 1.05x faster                                          |
| sqlalchemy_declarative          | 67.8 ms                                                                | 67.2 ms: 1.01x faster                                          |
| json_dumps                      | 8.01 ms                                                                | 7.94 ms: 1.01x faster                                          |
| python_startup_no_site          | 15.9 ms                                                                | 15.8 ms: 1.01x faster                                          |
| genshi_xml                      | 33.4 ms                                                                | 33.2 ms: 1.01x faster                                          |
| django_template                 | 24.7 ms                                                                | 24.5 ms: 1.01x faster                                          |
| scimark_sor                     | 97.6 ms                                                                | 97.0 ms: 1.01x faster                                          |
| raytrace                        | 249 ms                                                                 | 247 ms: 1.01x faster                                           |
| async_tree_none_tg              | 137 ms                                                                 | 136 ms: 1.01x faster                                           |
| async_tree_none                 | 161 ms                                                                 | 160 ms: 1.01x faster                                           |
| python_startup                  | 20.6 ms                                                                | 20.5 ms: 1.01x faster                                          |
| dulwich_log                     | 29.7 ms                                                                | 29.6 ms: 1.01x faster                                          |
| thrift                          | 520 us                                                                 | 517 us: 1.01x faster                                           |
| regex_effbot                    | 2.09 ms                                                                | 2.08 ms: 1.01x faster                                          |
| xml_etree_process               | 45.8 ms                                                                | 45.6 ms: 1.00x faster                                          |
| async_tree_memoization_tg       | 177 ms                                                                 | 176 ms: 1.00x faster                                           |
| deepcopy_memo                   | 21.7 us                                                                | 21.6 us: 1.00x faster                                          |
| async_tree_eager_memoization_tg | 162 ms                                                                 | 161 ms: 1.00x faster                                           |
| sympy_integrate                 | 12.4 ms                                                                | 12.3 ms: 1.00x faster                                          |
| telco                           | 4.97 ms                                                                | 4.96 ms: 1.00x faster                                          |
| regex_v8                        | 15.6 ms                                                                | 15.6 ms: 1.00x faster                                          |
| async_tree_eager_tg             | 120 ms                                                                 | 119 ms: 1.00x faster                                           |
| deltablue                       | 3.42 ms                                                                | 3.41 ms: 1.00x faster                                          |
| sqlglot_normalize               | 189 ms                                                                 | 188 ms: 1.00x faster                                           |
| regex_compile                   | 77.0 ms                                                                | 76.9 ms: 1.00x faster                                          |
| regex_dna                       | 137 ms                                                                 | 137 ms: 1.00x faster                                           |
| bpe_tokeniser                   | 3.04 sec                                                               | 3.03 sec: 1.00x faster                                         |
| async_generators                | 262 ms                                                                 | 261 ms: 1.00x faster                                           |
| chaos                           | 46.2 ms                                                                | 46.1 ms: 1.00x faster                                          |
| asyncio_websockets              | 238 ms                                                                 | 237 ms: 1.00x faster                                           |
| spectral_norm                   | 74.1 ms                                                                | 74.2 ms: 1.00x slower                                          |
| pprint_safe_repr                | 544 ms                                                                 | 545 ms: 1.00x slower                                           |
| mako                            | 9.95 ms                                                                | 9.97 ms: 1.00x slower                                          |
| fannkuch                        | 284 ms                                                                 | 285 ms: 1.00x slower                                           |
| richards                        | 39.3 ms                                                                | 39.5 ms: 1.00x slower                                          |
| async_tree_cpu_io_mixed         | 407 ms                                                                 | 409 ms: 1.00x slower                                           |
| logging_simple                  | 3.80 us                                                                | 3.82 us: 1.00x slower                                          |
| json_loads                      | 17.7 us                                                                | 17.8 us: 1.00x slower                                          |
| logging_silent                  | 92.7 ns                                                                | 93.0 ns: 1.00x slower                                          |
| 2to3                            | 189 ms                                                                 | 189 ms: 1.00x slower                                           |
| connected_components            | 325 ms                                                                 | 327 ms: 1.00x slower                                           |
| coverage                        | 51.9 ms                                                                | 52.2 ms: 1.01x slower                                          |
| logging_format                  | 4.19 us                                                                | 4.21 us: 1.01x slower                                          |
| sqlglot_optimize                | 35.0 ms                                                                | 35.2 ms: 1.01x slower                                          |
| typing_runtime_protocols        | 116 us                                                                 | 117 us: 1.01x slower                                           |
| sphinx                          | 614 ms                                                                 | 624 ms: 1.02x slower                                           |
| Geometric mean                  | (ref)                                                                  | 1.00x faster                                                   |

Benchmark hidden because not significant (58): xml_etree_iterparse, pycparser, sqlalchemy_imperative, bench_thread_pool, pickle_pure_python, crypto_pyaes, docutils, generators, async_tree_memoization, json, hexiom, bench_mp_pool, async_tree_eager, sqlite_synth, sqlglot_transpile, float, richards_super, create_gc_cycles, genshi_text, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, deepcopy, async_tree_io, unpickle_pure_python, gc_traversal, mdp, async_tree_io_tg, xml_etree_generate, meteor_contest, coroutines, scimark_fft, async_tree_eager_cpu_io_mixed_tg, html5lib, scimark_lu, nqueens, pyflate, comprehensions, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization, nbody, go, pidigits, async_tree_eager_io, pprint_pformat, scimark_sparse_mat_mult, many_optionals, subparsers, shortest_path, k_core, sympy_expand, sympy_str, deepcopy_reduce, pylint, tomli_loads, sympy_sum, scimark_monte_carlo, sqlglot_parse, pathlib

- Geometric mean (including insignificant results): 1.001x faster

# HPT report

- Reliability score: 98.06% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x