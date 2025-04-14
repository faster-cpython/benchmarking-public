# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: darwin-arm64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.080x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 166 ms: 1.08x faster                                                         |
| docutils       | 1.44 sec                                               | 1.48 sec: 1.02x slower                                                       |
| html5lib       | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                        |
| sphinx         | 602 ms                                                 | 572 ms: 1.05x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 197 ms: 1.46x faster                                                         |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                         |
| async_tree_io_tg                 | 500 ms                                                 | 364 ms: 1.37x faster                                                         |
| async_tree_io                    | 508 ms                                                 | 373 ms: 1.36x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                         |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                         |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                         |
| coroutines                       | 20.0 ms                                                | 15.8 ms: 1.27x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.11x faster                                                         |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 418 ms: 1.07x faster                                                         |
| async_tree_eager                 | 69.9 ms                                                | 66.9 ms: 1.05x faster                                                        |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                         |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                        |
| nbody          | 73.6 ms                                                | 65.7 ms: 1.12x faster                                                        |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                        |
| regex_compile  | 78.3 ms                                                | 68.5 ms: 1.14x faster                                                        |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                         |
| regex_v8       | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                       |
| unpickle_pure_python | 165 us                                                 | 131 us: 1.26x faster                                                         |
| xml_etree_process    | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                        |
| xml_etree_generate   | 57.1 ms                                                | 50.4 ms: 1.13x faster                                                        |
| pickle_pure_python   | 215 us                                                 | 195 us: 1.10x faster                                                         |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.07x faster                                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 69.6 ms: 1.07x faster                                                        |
| json_loads           | 17.0 us                                                | 17.8 us: 1.04x slower                                                        |
| json_dumps           | 6.47 ms                                                | 7.35 ms: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                        |
| python_startup_no_site | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.6 ms: 1.25x faster                                                        |
| mako            | 7.75 ms                                                | 6.49 ms: 1.19x faster                                                        |
| genshi_xml      | 34.1 ms                                                | 29.1 ms: 1.17x faster                                                        |
| django_template | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                                 |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 150 us: 1.57x faster                                                         |
| deepcopy_memo                    | 27.4 us                                                | 18.3 us: 1.50x faster                                                        |
| async_tree_memoization_tg        | 288 ms                                                 | 197 ms: 1.46x faster                                                         |
| go                               | 117 ms                                                 | 80.8 ms: 1.45x faster                                                        |
| async_tree_eager_io              | 511 ms                                                 | 361 ms: 1.41x faster                                                         |
| generators                       | 31.9 ms                                                | 22.8 ms: 1.40x faster                                                        |
| async_tree_io_tg                 | 500 ms                                                 | 364 ms: 1.37x faster                                                         |
| scimark_sor                      | 106 ms                                                 | 77.5 ms: 1.36x faster                                                        |
| async_tree_io                    | 508 ms                                                 | 373 ms: 1.36x faster                                                         |
| async_tree_memoization           | 268 ms                                                 | 197 ms: 1.36x faster                                                         |
| deepcopy_reduce                  | 2.09 us                                                | 1.57 us: 1.33x faster                                                        |
| tomli_loads                      | 1.57 sec                                               | 1.19 sec: 1.32x faster                                                       |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 376 ms: 1.27x faster                                                         |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                         |
| coroutines                       | 20.0 ms                                                | 15.8 ms: 1.27x faster                                                        |
| unpickle_pure_python             | 165 us                                                 | 131 us: 1.26x faster                                                         |
| genshi_text                      | 16.9 ms                                                | 13.6 ms: 1.25x faster                                                        |
| spectral_norm                    | 76.5 ms                                                | 61.3 ms: 1.25x faster                                                        |
| html5lib                         | 36.7 ms                                                | 29.4 ms: 1.25x faster                                                        |
| pyflate                          | 352 ms                                                 | 285 ms: 1.24x faster                                                         |
| mako                             | 7.75 ms                                                | 6.49 ms: 1.19x faster                                                        |
| float                            | 55.8 ms                                                | 46.8 ms: 1.19x faster                                                        |
| scimark_monte_carlo              | 50.4 ms                                                | 42.4 ms: 1.19x faster                                                        |
| scimark_fft                      | 200 ms                                                 | 170 ms: 1.17x faster                                                         |
| genshi_xml                       | 34.1 ms                                                | 29.1 ms: 1.17x faster                                                        |
| xml_etree_process                | 41.3 ms                                                | 35.6 ms: 1.16x faster                                                        |
| richards                         | 36.2 ms                                                | 31.3 ms: 1.16x faster                                                        |
| regex_effbot                     | 2.63 ms                                                | 2.28 ms: 1.15x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 146 ms: 1.15x faster                                                         |
| regex_compile                    | 78.3 ms                                                | 68.5 ms: 1.14x faster                                                        |
| bpe_tokeniser                    | 3.26 sec                                               | 2.86 sec: 1.14x faster                                                       |
| logging_simple                   | 3.56 us                                                | 3.13 us: 1.14x faster                                                        |
| xml_etree_generate               | 57.1 ms                                                | 50.4 ms: 1.13x faster                                                        |
| deltablue                        | 2.65 ms                                                | 2.34 ms: 1.13x faster                                                        |
| logging_format                   | 3.85 us                                                | 3.43 us: 1.12x faster                                                        |
| richards_super                   | 39.2 ms                                                | 35.0 ms: 1.12x faster                                                        |
| nbody                            | 73.6 ms                                                | 65.7 ms: 1.12x faster                                                        |
| pylint                           | 180 ms                                                 | 161 ms: 1.12x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 416 ms: 1.11x faster                                                         |
| pickle_pure_python               | 215 us                                                 | 195 us: 1.10x faster                                                         |
| telco                            | 4.84 ms                                                | 4.45 ms: 1.09x faster                                                        |
| async_generators                 | 294 ms                                                 | 271 ms: 1.08x faster                                                         |
| 2to3                             | 179 ms                                                 | 166 ms: 1.08x faster                                                         |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 418 ms: 1.07x faster                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 69.6 ms: 1.07x faster                                                        |
| typing_runtime_protocols         | 101 us                                                 | 94.5 us: 1.07x faster                                                        |
| thrift                           | 466 us                                                 | 438 us: 1.06x faster                                                         |
| bench_mp_pool                    | 64.7 ms                                                | 61.0 ms: 1.06x faster                                                        |
| connected_components             | 319 ms                                                 | 301 ms: 1.06x faster                                                         |
| hexiom                           | 4.87 ms                                                | 4.59 ms: 1.06x faster                                                        |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                         |
| logging_silent                   | 71.0 ns                                                | 67.3 ns: 1.05x faster                                                        |
| raytrace                         | 181 ms                                                 | 172 ms: 1.05x faster                                                         |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.05x faster                                                       |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.83 ms: 1.05x faster                                                        |
| sphinx                           | 602 ms                                                 | 572 ms: 1.05x faster                                                         |
| chaos                            | 41.1 ms                                                | 39.2 ms: 1.05x faster                                                        |
| async_tree_eager                 | 69.9 ms                                                | 66.9 ms: 1.05x faster                                                        |
| shortest_path                    | 345 ms                                                 | 331 ms: 1.04x faster                                                         |
| crypto_pyaes                     | 55.3 ms                                                | 53.1 ms: 1.04x faster                                                        |
| scimark_lu                       | 75.9 ms                                                | 73.3 ms: 1.04x faster                                                        |
| fannkuch                         | 279 ms                                                 | 270 ms: 1.03x faster                                                         |
| sqlglot_optimize                 | 34.7 ms                                                | 33.5 ms: 1.03x faster                                                        |
| sympy_str                        | 146 ms                                                 | 141 ms: 1.03x faster                                                         |
| sympy_expand                     | 248 ms                                                 | 240 ms: 1.03x faster                                                         |
| sqlglot_transpile                | 1.04 ms                                                | 1.01 ms: 1.03x faster                                                        |
| sqlglot_normalize                | 188 ms                                                 | 183 ms: 1.03x faster                                                         |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 28.1 ms: 1.02x faster                                                        |
| pycparser                        | 701 ms                                                 | 687 ms: 1.02x faster                                                         |
| sqlglot_parse                    | 852 us                                                 | 840 us: 1.01x faster                                                         |
| bench_thread_pool                | 503 us                                                 | 497 us: 1.01x faster                                                         |
| json                             | 3.04 ms                                                | 3.01 ms: 1.01x faster                                                        |
| regex_v8                         | 17.0 ms                                                | 16.8 ms: 1.01x faster                                                        |
| nqueens                          | 61.8 ms                                                | 61.3 ms: 1.01x faster                                                        |
| dask                             | 771 ms                                                 | 766 ms: 1.01x faster                                                         |
| meteor_contest                   | 74.0 ms                                                | 73.5 ms: 1.01x faster                                                        |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                         |
| pprint_pformat                   | 1.10 sec                                               | 1.11 sec: 1.01x slower                                                       |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.02x slower                                                        |
| pprint_safe_repr                 | 541 ms                                                 | 550 ms: 1.02x slower                                                         |
| mdp                              | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                       |
| docutils                         | 1.44 sec                                               | 1.48 sec: 1.02x slower                                                       |
| django_template                  | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                        |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                        |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.04x slower                                                        |
| comprehensions                   | 12.0 us                                                | 12.7 us: 1.06x slower                                                        |
| gc_traversal                     | 2.94 ms                                                | 3.12 ms: 1.06x slower                                                        |
| create_gc_cycles                 | 1.19 ms                                                | 1.28 ms: 1.07x slower                                                        |
| python_startup_no_site           | 13.7 ms                                                | 14.8 ms: 1.08x slower                                                        |
| many_optionals                   | 409 us                                                 | 452 us: 1.11x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 393 ms: 1.13x slower                                                         |
| json_dumps                       | 6.47 ms                                                | 7.35 ms: 1.14x slower                                                        |
| subparsers                       | 9.44 ms                                                | 11.8 ms: 1.25x slower                                                        |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 132 ms: 2.78x slower                                                         |
| Geometric mean                   | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (7): sympy_sum, sqlalchemy_imperative, asyncio_websockets, coverage, sqlite_synth, sqlalchemy_declarative, pathlib
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.080x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x