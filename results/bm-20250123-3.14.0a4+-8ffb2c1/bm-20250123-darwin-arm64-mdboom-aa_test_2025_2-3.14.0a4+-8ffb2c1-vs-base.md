# Results vs. base

- fork: mdboom
- ref: aa_test_2025_2
- machine: darwin-arm64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.002x slower
- HPT reliability: 97.56%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 166 ms                                                                 | 195 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                                  | 1.04x slower                                                     |

Benchmark hidden because not significant (3): docutils, html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_generators              | 254 ms                                                                 | 250 ms: 1.01x faster                                             |
| asyncio_websockets            | 242 ms                                                                 | 242 ms: 1.00x faster                                             |
| coroutines                    | 16.0 ms                                                                | 16.0 ms: 1.00x slower                                            |
| async_tree_cpu_io_mixed_tg    | 409 ms                                                                 | 411 ms: 1.00x slower                                             |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 359 ms: 1.01x slower                                             |
| async_tree_eager              | 61.4 ms                                                                | 62.0 ms: 1.01x slower                                            |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (13): async_tree_eager_io, async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_tg, async_tree_eager_memoization, async_tree_memoization, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): nbody, float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 141 ms: 1.00x slower                                             |
| regex_v8       | 16.7 ms                                                                | 16.8 ms: 1.00x slower                                            |
| regex_effbot   | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|---------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads         | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                           |
| xml_etree_generate  | 53.8 ms                                                                | 53.2 ms: 1.01x faster                                            |
| xml_etree_process   | 41.1 ms                                                                | 41.0 ms: 1.00x faster                                            |
| json_loads          | 16.5 us                                                                | 16.6 us: 1.01x slower                                            |
| xml_etree_iterparse | 70.6 ms                                                                | 71.2 ms: 1.01x slower                                            |
| xml_etree_parse     | 98.0 ms                                                                | 102 ms: 1.04x slower                                             |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (3): json_dumps, unpickle_pure_python, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                                | 19.3 ms: 1.03x slower                                            |
| python_startup_no_site | 14.0 ms                                                                | 14.4 ms: 1.03x slower                                            |
| Geometric mean         | (ref)                                                                  | 1.03x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 7.18 ms                                                                | 6.99 ms: 1.03x faster                                            |
| django_template | 21.4 ms                                                                | 21.3 ms: 1.00x faster                                            |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                     | bm-20250121-darwin-arm64-python-f18b2264929c56360c86-3.14.0a4+-f18b226 | bm-20250123-darwin-arm64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako                          | 7.18 ms                                                                | 6.99 ms: 1.03x faster                                            |
| async_generators              | 254 ms                                                                 | 250 ms: 1.01x faster                                             |
| tomli_loads                   | 1.21 sec                                                               | 1.20 sec: 1.01x faster                                           |
| richards                      | 34.7 ms                                                                | 34.3 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult       | 2.72 ms                                                                | 2.69 ms: 1.01x faster                                            |
| xml_etree_generate            | 53.8 ms                                                                | 53.2 ms: 1.01x faster                                            |
| scimark_monte_carlo           | 50.1 ms                                                                | 49.7 ms: 1.01x faster                                            |
| json                          | 2.89 ms                                                                | 2.87 ms: 1.01x faster                                            |
| sympy_expand                  | 236 ms                                                                 | 235 ms: 1.01x faster                                             |
| richards_super                | 38.3 ms                                                                | 38.1 ms: 1.00x faster                                            |
| sqlite_synth                  | 1.54 us                                                                | 1.53 us: 1.00x faster                                            |
| thrift                        | 459 us                                                                 | 458 us: 1.00x faster                                             |
| django_template               | 21.4 ms                                                                | 21.3 ms: 1.00x faster                                            |
| xml_etree_process             | 41.1 ms                                                                | 41.0 ms: 1.00x faster                                            |
| generators                    | 22.5 ms                                                                | 22.4 ms: 1.00x faster                                            |
| raytrace                      | 204 ms                                                                 | 204 ms: 1.00x faster                                             |
| asyncio_websockets            | 242 ms                                                                 | 242 ms: 1.00x faster                                             |
| pyflate                       | 300 ms                                                                 | 300 ms: 1.00x slower                                             |
| coroutines                    | 16.0 ms                                                                | 16.0 ms: 1.00x slower                                            |
| pprint_pformat                | 928 ms                                                                 | 930 ms: 1.00x slower                                             |
| deepcopy                      | 148 us                                                                 | 149 us: 1.00x slower                                             |
| comprehensions                | 12.8 us                                                                | 12.9 us: 1.00x slower                                            |
| regex_dna                     | 141 ms                                                                 | 141 ms: 1.00x slower                                             |
| fannkuch                      | 245 ms                                                                 | 246 ms: 1.00x slower                                             |
| connected_components          | 296 ms                                                                 | 297 ms: 1.00x slower                                             |
| regex_v8                      | 16.7 ms                                                                | 16.8 ms: 1.00x slower                                            |
| async_tree_cpu_io_mixed_tg    | 409 ms                                                                 | 411 ms: 1.00x slower                                             |
| deepcopy_reduce               | 1.56 us                                                                | 1.57 us: 1.01x slower                                            |
| chaos                         | 39.2 ms                                                                | 39.5 ms: 1.01x slower                                            |
| bench_mp_pool                 | 60.2 ms                                                                | 60.5 ms: 1.01x slower                                            |
| async_tree_eager_cpu_io_mixed | 357 ms                                                                 | 359 ms: 1.01x slower                                             |
| regex_effbot                  | 2.25 ms                                                                | 2.27 ms: 1.01x slower                                            |
| typing_runtime_protocols      | 96.9 us                                                                | 97.6 us: 1.01x slower                                            |
| json_loads                    | 16.5 us                                                                | 16.6 us: 1.01x slower                                            |
| coverage                      | 45.8 ms                                                                | 46.2 ms: 1.01x slower                                            |
| deltablue                     | 2.70 ms                                                                | 2.72 ms: 1.01x slower                                            |
| xml_etree_iterparse           | 70.6 ms                                                                | 71.2 ms: 1.01x slower                                            |
| async_tree_eager              | 61.4 ms                                                                | 62.0 ms: 1.01x slower                                            |
| python_startup                | 18.8 ms                                                                | 19.3 ms: 1.03x slower                                            |
| python_startup_no_site        | 14.0 ms                                                                | 14.4 ms: 1.03x slower                                            |
| pathlib                       | 22.3 ms                                                                | 23.0 ms: 1.03x slower                                            |
| xml_etree_parse               | 98.0 ms                                                                | 102 ms: 1.04x slower                                             |
| 2to3                          | 166 ms                                                                 | 195 ms: 1.18x slower                                             |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                     |

Benchmark hidden because not significant (62): async_tree_eager_io, sympy_sum, k_core, shortest_path, sqlalchemy_declarative, genshi_text, pylint, async_tree_io, mdp, async_tree_io_tg, spectral_norm, regex_compile, sqlalchemy_imperative, json_dumps, async_tree_memoization_tg, crypto_pyaes, logging_format, sqlglot_transpile, sqlglot_parse, bpe_tokeniser, deepcopy_memo, logging_silent, dulwich_log, hexiom, nqueens, sqlglot_optimize, async_tree_none_tg, sqlglot_normalize, logging_simple, unpickle_pure_python, sympy_integrate, pickle_pure_python, genshi_xml, gc_traversal, dask, go, scimark_sor, docutils, meteor_contest, nbody, async_tree_eager_memoization_tg, float, pidigits, bench_thread_pool, scimark_fft, sympy_str, create_gc_cycles, subparsers, scimark_lu, async_tree_eager_cpu_io_mixed_tg, many_optionals, pprint_safe_repr, async_tree_cpu_io_mixed, async_tree_none, async_tree_eager_tg, pycparser, telco, html5lib, async_tree_eager_memoization, sphinx, async_tree_memoization, async_tree_eager_io_tg

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 97.56% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x