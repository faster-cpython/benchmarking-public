# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.000x faster
- HPT reliability: 91.39%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| docutils       | 1.43 sec                                                               | 1.43 sec: 1.00x faster                                           |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (3): 2to3, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_generators                 | 262 ms                                                                 | 260 ms: 1.01x faster                                             |
| async_tree_eager_memoization     | 152 ms                                                                 | 151 ms: 1.00x faster                                             |
| coroutines                       | 17.0 ms                                                                | 17.0 ms: 1.00x slower                                            |
| async_tree_io                    | 343 ms                                                                 | 343 ms: 1.00x slower                                             |
| async_tree_eager_cpu_io_mixed_tg | 367 ms                                                                 | 368 ms: 1.00x slower                                             |
| async_tree_cpu_io_mixed          | 407 ms                                                                 | 409 ms: 1.00x slower                                             |
| async_tree_eager_tg              | 120 ms                                                                 | 120 ms: 1.01x slower                                             |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (12): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager, async_tree_eager_memoization_tg, async_tree_memoization, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, async_tree_io_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 87.3 ms                                                                | 87.6 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 15.6 ms                                                                | 15.5 ms: 1.01x faster                                            |
| regex_dna      | 137 ms                                                                 | 137 ms: 1.00x faster                                             |
| regex_effbot   | 2.09 ms                                                                | 2.08 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| json_dumps           | 8.01 ms                                                                | 7.96 ms: 1.01x faster                                            |
| xml_etree_process    | 45.8 ms                                                                | 45.6 ms: 1.01x faster                                            |
| pickle_pure_python   | 225 us                                                                 | 224 us: 1.00x faster                                             |
| unpickle_pure_python | 162 us                                                                 | 162 us: 1.00x slower                                             |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (5): xml_etree_parse, tomli_loads, xml_etree_iterparse, xml_etree_generate, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                            |
| python_startup_no_site | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                            |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_xml     | 33.4 ms                                                                | 33.1 ms: 1.01x faster                                            |
| mako           | 9.95 ms                                                                | 9.98 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                        | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| coverage                         | 51.9 ms                                                                | 51.3 ms: 1.01x faster                                            |
| telco                            | 4.97 ms                                                                | 4.92 ms: 1.01x faster                                            |
| regex_v8                         | 15.6 ms                                                                | 15.5 ms: 1.01x faster                                            |
| async_generators                 | 262 ms                                                                 | 260 ms: 1.01x faster                                             |
| scimark_sor                      | 97.6 ms                                                                | 96.8 ms: 1.01x faster                                            |
| generators                       | 24.0 ms                                                                | 23.8 ms: 1.01x faster                                            |
| genshi_xml                       | 33.4 ms                                                                | 33.1 ms: 1.01x faster                                            |
| sqlalchemy_declarative           | 67.8 ms                                                                | 67.4 ms: 1.01x faster                                            |
| json_dumps                       | 8.01 ms                                                                | 7.96 ms: 1.01x faster                                            |
| sympy_integrate                  | 12.4 ms                                                                | 12.3 ms: 1.01x faster                                            |
| xml_etree_process                | 45.8 ms                                                                | 45.6 ms: 1.01x faster                                            |
| pprint_pformat                   | 1.11 sec                                                               | 1.10 sec: 1.00x faster                                           |
| pprint_safe_repr                 | 544 ms                                                                 | 541 ms: 1.00x faster                                             |
| pickle_pure_python               | 225 us                                                                 | 224 us: 1.00x faster                                             |
| regex_dna                        | 137 ms                                                                 | 137 ms: 1.00x faster                                             |
| docutils                         | 1.43 sec                                                               | 1.43 sec: 1.00x faster                                           |
| crypto_pyaes                     | 61.8 ms                                                                | 61.5 ms: 1.00x faster                                            |
| dulwich_log                      | 29.7 ms                                                                | 29.6 ms: 1.00x faster                                            |
| bpe_tokeniser                    | 3.04 sec                                                               | 3.03 sec: 1.00x faster                                           |
| async_tree_eager_memoization     | 152 ms                                                                 | 151 ms: 1.00x faster                                             |
| regex_effbot                     | 2.09 ms                                                                | 2.08 ms: 1.00x faster                                            |
| logging_format                   | 4.19 us                                                                | 4.18 us: 1.00x faster                                            |
| richards_super                   | 44.3 ms                                                                | 44.2 ms: 1.00x faster                                            |
| thrift                           | 520 us                                                                 | 519 us: 1.00x faster                                             |
| logging_silent                   | 92.7 ns                                                                | 92.6 ns: 1.00x faster                                            |
| spectral_norm                    | 74.1 ms                                                                | 74.2 ms: 1.00x slower                                            |
| richards                         | 39.3 ms                                                                | 39.4 ms: 1.00x slower                                            |
| coroutines                       | 17.0 ms                                                                | 17.0 ms: 1.00x slower                                            |
| unpickle_pure_python             | 162 us                                                                 | 162 us: 1.00x slower                                             |
| async_tree_io                    | 343 ms                                                                 | 343 ms: 1.00x slower                                             |
| deepcopy_memo                    | 21.7 us                                                                | 21.8 us: 1.00x slower                                            |
| go                               | 104 ms                                                                 | 104 ms: 1.00x slower                                             |
| scimark_lu                       | 98.9 ms                                                                | 99.1 ms: 1.00x slower                                            |
| async_tree_eager_cpu_io_mixed_tg | 367 ms                                                                 | 368 ms: 1.00x slower                                             |
| fannkuch                         | 284 ms                                                                 | 285 ms: 1.00x slower                                             |
| nbody                            | 87.3 ms                                                                | 87.6 ms: 1.00x slower                                            |
| deepcopy                         | 173 us                                                                 | 173 us: 1.00x slower                                             |
| mako                             | 9.95 ms                                                                | 9.98 ms: 1.00x slower                                            |
| async_tree_cpu_io_mixed          | 407 ms                                                                 | 409 ms: 1.00x slower                                             |
| create_gc_cycles                 | 818 us                                                                 | 821 us: 1.00x slower                                             |
| scimark_fft                      | 210 ms                                                                 | 211 ms: 1.00x slower                                             |
| python_startup                   | 20.6 ms                                                                | 20.7 ms: 1.00x slower                                            |
| async_tree_eager_tg              | 120 ms                                                                 | 120 ms: 1.01x slower                                             |
| meteor_contest                   | 78.9 ms                                                                | 79.4 ms: 1.01x slower                                            |
| python_startup_no_site           | 15.9 ms                                                                | 16.1 ms: 1.01x slower                                            |
| sqlglot_optimize                 | 35.0 ms                                                                | 35.4 ms: 1.01x slower                                            |
| sqlglot_normalize                | 189 ms                                                                 | 191 ms: 1.01x slower                                             |
| sqlglot_transpile                | 1.18 ms                                                                | 1.19 ms: 1.01x slower                                            |
| sqlalchemy_imperative            | 7.65 ms                                                                | 7.78 ms: 1.02x slower                                            |
| sqlglot_parse                    | 989 us                                                                 | 1.01 ms: 1.02x slower                                            |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                     |

Benchmark hidden because not significant (54): xml_etree_parse, bench_thread_pool, tomli_loads, async_tree_none, pycparser, json, xml_etree_iterparse, pyflate, many_optionals, async_tree_none_tg, deltablue, genshi_text, comprehensions, async_tree_memoization_tg, hexiom, sympy_expand, django_template, subparsers, raytrace, sympy_sum, nqueens, async_tree_eager, k_core, 2to3, async_tree_eager_memoization_tg, xml_etree_generate, pylint, deepcopy_reduce, json_loads, html5lib, pidigits, async_tree_memoization, float, mdp, sphinx, asyncio_websockets, regex_compile, gc_traversal, shortest_path, scimark_monte_carlo, async_tree_cpu_io_mixed_tg, chaos, async_tree_eager_io_tg, async_tree_eager_cpu_io_mixed, logging_simple, scimark_sparse_mat_mult, async_tree_io_tg, sympy_str, async_tree_eager_io, sqlite_synth, typing_runtime_protocols, connected_components, pathlib, bench_mp_pool

- Geometric mean (including insignificant results): 1.000x faster

# HPT report

- Reliability score: 91.39% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x