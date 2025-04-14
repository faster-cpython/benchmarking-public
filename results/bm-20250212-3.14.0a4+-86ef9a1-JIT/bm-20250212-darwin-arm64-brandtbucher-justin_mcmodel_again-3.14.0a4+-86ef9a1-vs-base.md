# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: darwin-arm64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.002x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 167 ms                                                                 | 166 ms: 1.01x faster                                                         |
| docutils       | 1.45 sec                                                               | 1.48 sec: 1.02x slower                                                       |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (19): async_tree_eager, async_tree_cpu_io_mixed, async_tree_eager_io_tg, asyncio_websockets, async_generators, async_tree_memoization_tg, coroutines, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_tg, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_eager_io, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 65.3 ms                                                                | 65.7 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 141 ms                                                                 | 141 ms: 1.00x slower                                                         |
| regex_compile  | 67.6 ms                                                                | 68.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.21 sec                                                               | 1.19 sec: 1.02x faster                                                       |
| xml_etree_process    | 35.8 ms                                                                | 35.6 ms: 1.01x faster                                                        |
| json_dumps           | 7.33 ms                                                                | 7.35 ms: 1.00x slower                                                        |
| xml_etree_generate   | 50.2 ms                                                                | 50.4 ms: 1.00x slower                                                        |
| json_loads           | 17.7 us                                                                | 17.8 us: 1.00x slower                                                        |
| pickle_pure_python   | 194 us                                                                 | 195 us: 1.01x slower                                                         |
| unpickle_pure_python | 130 us                                                                 | 131 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                        |
| python_startup_no_site | 14.9 ms                                                                | 14.8 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 6.45 ms                                                                | 6.49 ms: 1.01x slower                                                        |
| django_template | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark                | bm-20250209-darwin-arm64-python-f72977b2f4a29063ae30-3.14.0a4+-f72977b | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|--------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| scimark_sparse_mat_mult  | 2.92 ms                                                                | 2.83 ms: 1.03x faster                                                        |
| scimark_fft              | 173 ms                                                                 | 170 ms: 1.02x faster                                                         |
| spectral_norm            | 62.3 ms                                                                | 61.3 ms: 1.02x faster                                                        |
| tomli_loads              | 1.21 sec                                                               | 1.19 sec: 1.02x faster                                                       |
| telco                    | 4.52 ms                                                                | 4.45 ms: 1.02x faster                                                        |
| connected_components     | 304 ms                                                                 | 301 ms: 1.01x faster                                                         |
| typing_runtime_protocols | 95.5 us                                                                | 94.5 us: 1.01x faster                                                        |
| python_startup           | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                        |
| 2to3                     | 167 ms                                                                 | 166 ms: 1.01x faster                                                         |
| scimark_lu               | 73.8 ms                                                                | 73.3 ms: 1.01x faster                                                        |
| xml_etree_process        | 35.8 ms                                                                | 35.6 ms: 1.01x faster                                                        |
| python_startup_no_site   | 14.9 ms                                                                | 14.8 ms: 1.01x faster                                                        |
| logging_simple           | 3.14 us                                                                | 3.13 us: 1.00x faster                                                        |
| bpe_tokeniser            | 2.87 sec                                                               | 2.86 sec: 1.00x faster                                                       |
| logging_format           | 3.44 us                                                                | 3.43 us: 1.00x faster                                                        |
| nqueens                  | 61.5 ms                                                                | 61.3 ms: 1.00x faster                                                        |
| scimark_monte_carlo      | 42.5 ms                                                                | 42.4 ms: 1.00x faster                                                        |
| richards                 | 31.4 ms                                                                | 31.3 ms: 1.00x faster                                                        |
| scimark_sor              | 77.6 ms                                                                | 77.5 ms: 1.00x faster                                                        |
| generators               | 22.8 ms                                                                | 22.8 ms: 1.00x slower                                                        |
| regex_dna                | 141 ms                                                                 | 141 ms: 1.00x slower                                                         |
| pyflate                  | 284 ms                                                                 | 285 ms: 1.00x slower                                                         |
| raytrace                 | 171 ms                                                                 | 172 ms: 1.00x slower                                                         |
| crypto_pyaes             | 53.0 ms                                                                | 53.1 ms: 1.00x slower                                                        |
| bench_thread_pool        | 495 us                                                                 | 497 us: 1.00x slower                                                         |
| json_dumps               | 7.33 ms                                                                | 7.35 ms: 1.00x slower                                                        |
| xml_etree_generate       | 50.2 ms                                                                | 50.4 ms: 1.00x slower                                                        |
| gc_traversal             | 3.11 ms                                                                | 3.12 ms: 1.00x slower                                                        |
| sympy_expand             | 239 ms                                                                 | 240 ms: 1.00x slower                                                         |
| sqlglot_normalize        | 182 ms                                                                 | 183 ms: 1.00x slower                                                         |
| json_loads               | 17.7 us                                                                | 17.8 us: 1.00x slower                                                        |
| dulwich_log              | 28.0 ms                                                                | 28.1 ms: 1.00x slower                                                        |
| nbody                    | 65.3 ms                                                                | 65.7 ms: 1.01x slower                                                        |
| mdp                      | 1.52 sec                                                               | 1.53 sec: 1.01x slower                                                       |
| thrift                   | 435 us                                                                 | 438 us: 1.01x slower                                                         |
| mako                     | 6.45 ms                                                                | 6.49 ms: 1.01x slower                                                        |
| bench_mp_pool            | 60.6 ms                                                                | 61.0 ms: 1.01x slower                                                        |
| go                       | 80.3 ms                                                                | 80.8 ms: 1.01x slower                                                        |
| deepcopy                 | 149 us                                                                 | 150 us: 1.01x slower                                                         |
| fannkuch                 | 268 ms                                                                 | 270 ms: 1.01x slower                                                         |
| coverage                 | 45.9 ms                                                                | 46.2 ms: 1.01x slower                                                        |
| pickle_pure_python       | 194 us                                                                 | 195 us: 1.01x slower                                                         |
| sympy_integrate          | 11.4 ms                                                                | 11.5 ms: 1.01x slower                                                        |
| unpickle_pure_python     | 130 us                                                                 | 131 us: 1.01x slower                                                         |
| sqlalchemy_declarative   | 58.6 ms                                                                | 59.1 ms: 1.01x slower                                                        |
| sqlite_synth             | 1.54 us                                                                | 1.55 us: 1.01x slower                                                        |
| django_template          | 20.9 ms                                                                | 21.1 ms: 1.01x slower                                                        |
| sympy_sum                | 74.1 ms                                                                | 74.9 ms: 1.01x slower                                                        |
| sqlglot_optimize         | 33.2 ms                                                                | 33.5 ms: 1.01x slower                                                        |
| pycparser                | 679 ms                                                                 | 687 ms: 1.01x slower                                                         |
| sqlalchemy_imperative    | 6.60 ms                                                                | 6.68 ms: 1.01x slower                                                        |
| hexiom                   | 4.53 ms                                                                | 4.59 ms: 1.01x slower                                                        |
| regex_compile            | 67.6 ms                                                                | 68.5 ms: 1.01x slower                                                        |
| comprehensions           | 12.5 us                                                                | 12.7 us: 1.01x slower                                                        |
| sqlglot_transpile        | 994 us                                                                 | 1.01 ms: 1.01x slower                                                        |
| sqlglot_parse            | 827 us                                                                 | 840 us: 1.02x slower                                                         |
| many_optionals           | 444 us                                                                 | 452 us: 1.02x slower                                                         |
| docutils                 | 1.45 sec                                                               | 1.48 sec: 1.02x slower                                                       |
| pprint_safe_repr         | 524 ms                                                                 | 550 ms: 1.05x slower                                                         |
| pprint_pformat           | 1.04 sec                                                               | 1.11 sec: 1.06x slower                                                       |
| Geometric mean           | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (45): async_tree_eager, xml_etree_iterparse, deltablue, subparsers, deepcopy_reduce, sympy_str, genshi_xml, dask, async_tree_cpu_io_mixed, async_tree_eager_io_tg, asyncio_websockets, async_generators, regex_effbot, async_tree_memoization_tg, coroutines, create_gc_cycles, pidigits, deepcopy_memo, json, regex_v8, richards_super, html5lib, chaos, float, meteor_contest, shortest_path, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, k_core, async_tree_cpu_io_mixed_tg, genshi_text, async_tree_eager_tg, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_io_tg, async_tree_io, pathlib, async_tree_none_tg, async_tree_eager_io, logging_silent, async_tree_eager_memoization, sphinx, pylint, xml_etree_parse

- Geometric mean (including insignificant results): 1.002x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x