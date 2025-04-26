# Results vs. base

- fork: mdboom
- ref: python_startup_time
- machine: darwin-arm64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.002x slower
- HPT reliability: 64.56%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 187 ms                                                                 | 220 ms: 1.17x slower                                                  |
| docutils       | 1.55 sec                                                               | 1.55 sec: 1.00x faster                                                |
| html5lib       | 35.0 ms                                                                | 36.9 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.05x slower                                                          |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_tg           | 150 ms                                                                 | 146 ms: 1.03x faster                                                  |
| async_tree_memoization        | 227 ms                                                                 | 223 ms: 1.02x faster                                                  |
| async_tree_none_tg            | 178 ms                                                                 | 176 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed       | 441 ms                                                                 | 437 ms: 1.01x faster                                                  |
| async_tree_eager_memoization  | 157 ms                                                                 | 156 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed | 374 ms                                                                 | 372 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed_tg    | 424 ms                                                                 | 427 ms: 1.01x slower                                                  |
| asyncio_websockets            | 243 ms                                                                 | 245 ms: 1.01x slower                                                  |
| async_tree_none               | 186 ms                                                                 | 189 ms: 1.02x slower                                                  |
| async_tree_memoization_tg     | 211 ms                                                                 | 215 ms: 1.02x slower                                                  |
| async_tree_io                 | 426 ms                                                                 | 435 ms: 1.02x slower                                                  |
| async_tree_eager              | 76.8 ms                                                                | 81.3 ms: 1.06x slower                                                 |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (7): async_tree_eager_io_tg, async_tree_io_tg, coroutines, async_tree_eager_io, async_tree_eager_memoization_tg, async_generators, async_tree_eager_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 284 ms                                                                 | 284 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 145 ms                                                                 | 140 ms: 1.04x faster                                                  |
| regex_effbot   | 2.34 ms                                                                | 2.28 ms: 1.03x faster                                                 |
| regex_v8       | 16.2 ms                                                                | 15.9 ms: 1.02x faster                                                 |
| regex_compile  | 85.5 ms                                                                | 85.6 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|--------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_generate | 61.7 ms                                                                | 61.5 ms: 1.00x faster                                                 |
| pickle_pure_python | 250 us                                                                 | 249 us: 1.00x faster                                                  |
| json_dumps         | 7.76 ms                                                                | 7.88 ms: 1.02x slower                                                 |
| Geometric mean     | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (6): xml_etree_iterparse, unpickle_pure_python, xml_etree_process, json_loads, tomli_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                                | 15.0 ms: 1.03x faster                                                 |
| python_startup         | 20.1 ms                                                                | 19.9 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                                  | 1.02x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 37.5 ms                                                                | 37.2 ms: 1.01x faster                                                 |
| mako            | 9.14 ms                                                                | 9.07 ms: 1.01x faster                                                 |
| django_template | 26.3 ms                                                                | 26.2 ms: 1.00x faster                                                 |
| genshi_text     | 18.5 ms                                                                | 18.8 ms: 1.01x slower                                                 |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_safe_repr              | 635 ms                                                                 | 598 ms: 1.06x faster                                                  |
| richards                      | 41.6 ms                                                                | 39.3 ms: 1.06x faster                                                 |
| pprint_pformat                | 1.28 sec                                                               | 1.21 sec: 1.06x faster                                                |
| dulwich_log                   | 28.0 ms                                                                | 26.9 ms: 1.04x faster                                                 |
| regex_dna                     | 145 ms                                                                 | 140 ms: 1.04x faster                                                  |
| python_startup_no_site        | 15.5 ms                                                                | 15.0 ms: 1.03x faster                                                 |
| regex_effbot                  | 2.34 ms                                                                | 2.28 ms: 1.03x faster                                                 |
| async_tree_eager_tg           | 150 ms                                                                 | 146 ms: 1.03x faster                                                  |
| regex_v8                      | 16.2 ms                                                                | 15.9 ms: 1.02x faster                                                 |
| async_tree_memoization        | 227 ms                                                                 | 223 ms: 1.02x faster                                                  |
| python_startup                | 20.1 ms                                                                | 19.9 ms: 1.01x faster                                                 |
| async_tree_none_tg            | 178 ms                                                                 | 176 ms: 1.01x faster                                                  |
| raytrace                      | 215 ms                                                                 | 212 ms: 1.01x faster                                                  |
| json                          | 3.10 ms                                                                | 3.06 ms: 1.01x faster                                                 |
| sqlalchemy_imperative         | 7.53 ms                                                                | 7.45 ms: 1.01x faster                                                 |
| sympy_expand                  | 271 ms                                                                 | 268 ms: 1.01x faster                                                  |
| async_tree_cpu_io_mixed       | 441 ms                                                                 | 437 ms: 1.01x faster                                                  |
| async_tree_eager_memoization  | 157 ms                                                                 | 156 ms: 1.01x faster                                                  |
| genshi_xml                    | 37.5 ms                                                                | 37.2 ms: 1.01x faster                                                 |
| mako                          | 9.14 ms                                                                | 9.07 ms: 1.01x faster                                                 |
| async_tree_eager_cpu_io_mixed | 374 ms                                                                 | 372 ms: 1.01x faster                                                  |
| sympy_str                     | 160 ms                                                                 | 159 ms: 1.01x faster                                                  |
| sqlglot_v2_normalize          | 77.9 ms                                                                | 77.6 ms: 1.00x faster                                                 |
| xml_etree_generate            | 61.7 ms                                                                | 61.5 ms: 1.00x faster                                                 |
| docutils                      | 1.55 sec                                                               | 1.55 sec: 1.00x faster                                                |
| richards_super                | 44.1 ms                                                                | 43.9 ms: 1.00x faster                                                 |
| pickle_pure_python            | 250 us                                                                 | 249 us: 1.00x faster                                                  |
| sympy_integrate               | 11.7 ms                                                                | 11.6 ms: 1.00x faster                                                 |
| django_template               | 26.3 ms                                                                | 26.2 ms: 1.00x faster                                                 |
| hexiom                        | 5.48 ms                                                                | 5.47 ms: 1.00x faster                                                 |
| pyflate                       | 347 ms                                                                 | 347 ms: 1.00x faster                                                  |
| pidigits                      | 284 ms                                                                 | 284 ms: 1.00x faster                                                  |
| regex_compile                 | 85.5 ms                                                                | 85.6 ms: 1.00x slower                                                 |
| connected_components          | 310 ms                                                                 | 311 ms: 1.00x slower                                                  |
| meteor_contest                | 77.3 ms                                                                | 77.5 ms: 1.00x slower                                                 |
| go                            | 105 ms                                                                 | 105 ms: 1.00x slower                                                  |
| scimark_fft                   | 206 ms                                                                 | 206 ms: 1.00x slower                                                  |
| sqlglot_v2_optimize           | 37.9 ms                                                                | 38.0 ms: 1.00x slower                                                 |
| scimark_sor                   | 94.5 ms                                                                | 95.0 ms: 1.00x slower                                                 |
| generators                    | 31.5 ms                                                                | 31.7 ms: 1.00x slower                                                 |
| shortest_path                 | 339 ms                                                                 | 340 ms: 1.01x slower                                                  |
| subparsers                    | 13.8 ms                                                                | 13.9 ms: 1.01x slower                                                 |
| bpe_tokeniser                 | 3.30 sec                                                               | 3.32 sec: 1.01x slower                                                |
| async_tree_cpu_io_mixed_tg    | 424 ms                                                                 | 427 ms: 1.01x slower                                                  |
| scimark_lu                    | 83.0 ms                                                                | 83.7 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult       | 3.18 ms                                                                | 3.20 ms: 1.01x slower                                                 |
| pathlib                       | 24.0 ms                                                                | 24.2 ms: 1.01x slower                                                 |
| asyncio_websockets            | 243 ms                                                                 | 245 ms: 1.01x slower                                                  |
| sqlglot_v2_parse              | 976 us                                                                 | 986 us: 1.01x slower                                                  |
| coverage                      | 49.4 ms                                                                | 50.0 ms: 1.01x slower                                                 |
| scimark_monte_carlo           | 52.9 ms                                                                | 53.6 ms: 1.01x slower                                                 |
| genshi_text                   | 18.5 ms                                                                | 18.8 ms: 1.01x slower                                                 |
| telco                         | 4.84 ms                                                                | 4.91 ms: 1.01x slower                                                 |
| sqlite_synth                  | 1.58 us                                                                | 1.60 us: 1.01x slower                                                 |
| bench_thread_pool             | 553 us                                                                 | 561 us: 1.02x slower                                                  |
| deltablue                     | 2.88 ms                                                                | 2.93 ms: 1.02x slower                                                 |
| async_tree_none               | 186 ms                                                                 | 189 ms: 1.02x slower                                                  |
| json_dumps                    | 7.76 ms                                                                | 7.88 ms: 1.02x slower                                                 |
| async_tree_memoization_tg     | 211 ms                                                                 | 215 ms: 1.02x slower                                                  |
| async_tree_io                 | 426 ms                                                                 | 435 ms: 1.02x slower                                                  |
| sqlalchemy_declarative        | 66.1 ms                                                                | 67.4 ms: 1.02x slower                                                 |
| sqlglot_v2_transpile          | 1.17 ms                                                                | 1.20 ms: 1.03x slower                                                 |
| typing_runtime_protocols      | 110 us                                                                 | 115 us: 1.04x slower                                                  |
| fannkuch                      | 321 ms                                                                 | 333 ms: 1.04x slower                                                  |
| nqueens                       | 75.2 ms                                                                | 78.5 ms: 1.04x slower                                                 |
| html5lib                      | 35.0 ms                                                                | 36.9 ms: 1.05x slower                                                 |
| async_tree_eager              | 76.8 ms                                                                | 81.3 ms: 1.06x slower                                                 |
| 2to3                          | 187 ms                                                                 | 220 ms: 1.17x slower                                                  |
| Geometric mean                | (ref)                                                                  | 1.00x slower                                                          |

Benchmark hidden because not significant (35): async_tree_eager_io_tg, many_optionals, pycparser, async_tree_io_tg, sphinx, k_core, pylint, sympy_sum, deepcopy, logging_silent, gc_traversal, coroutines, spectral_norm, logging_format, comprehensions, xml_etree_iterparse, deepcopy_reduce, mdp, deepcopy_memo, unpickle_pure_python, chaos, async_tree_eager_io, xml_etree_process, create_gc_cycles, crypto_pyaes, async_tree_eager_memoization_tg, nbody, logging_simple, async_generators, json_loads, bench_mp_pool, async_tree_eager_cpu_io_mixed_tg, tomli_loads, float, xml_etree_parse

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 64.56% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x