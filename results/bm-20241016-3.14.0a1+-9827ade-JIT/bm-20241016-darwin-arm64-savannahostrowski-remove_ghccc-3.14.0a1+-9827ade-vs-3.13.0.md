# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: darwin-arm64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.043x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 182 ms: 1.03x faster                                                      |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| html5lib       | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                     |
| sphinx         | 603 ms                                                 | 668 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 43.3 ms: 1.10x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 471 ms: 1.05x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 672 ms: 1.31x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 47.7 ms: 1.17x faster                                                     |
| nbody          | 74.0 ms                                                | 63.2 ms: 1.17x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 74.0 ms: 1.06x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| regex_effbot   | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.23 sec: 1.28x faster                                                    |
| unpickle_pure_python | 164 us                                                 | 132 us: 1.24x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 34.3 ms: 1.20x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                | 49.8 ms: 1.14x faster                                                     |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                     |
| json_dumps           | 6.52 ms                                                | 7.23 ms: 1.11x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 19.0 ms: 1.01x slower                                                     |
| python_startup_no_site | 14.5 ms                                                | 14.7 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.30 ms: 1.22x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                     |
| django_template | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.8 us: 1.63x faster                                                     |
| deepcopy                         | 237 us                                                 | 155 us: 1.52x faster                                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.53 us: 1.35x faster                                                     |
| scimark_sor                      | 105 ms                                                 | 82.4 ms: 1.28x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.23 sec: 1.28x faster                                                    |
| generators                       | 31.5 ms                                                | 25.2 ms: 1.25x faster                                                     |
| unpickle_pure_python             | 164 us                                                 | 132 us: 1.24x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 235 ms: 1.22x faster                                                      |
| mako                             | 7.68 ms                                                | 6.30 ms: 1.22x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                                      |
| xml_etree_process                | 41.0 ms                                                | 34.3 ms: 1.20x faster                                                     |
| go                               | 115 ms                                                 | 96.8 ms: 1.19x faster                                                     |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| float                            | 56.0 ms                                                | 47.7 ms: 1.17x faster                                                     |
| nbody                            | 74.0 ms                                                | 63.2 ms: 1.17x faster                                                     |
| scimark_lu                       | 76.7 ms                                                | 65.7 ms: 1.17x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.09 us: 1.17x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.37 us: 1.16x faster                                                     |
| xml_etree_generate               | 57.0 ms                                                | 49.8 ms: 1.14x faster                                                     |
| pprint_safe_repr                 | 533 ms                                                 | 470 ms: 1.13x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 961 ms: 1.13x faster                                                      |
| scimark_monte_carlo              | 50.4 ms                                                | 45.0 ms: 1.12x faster                                                     |
| spectral_norm                    | 76.3 ms                                                | 68.1 ms: 1.12x faster                                                     |
| deltablue                        | 2.68 ms                                                | 2.42 ms: 1.11x faster                                                     |
| pyflate                          | 351 ms                                                 | 318 ms: 1.10x faster                                                      |
| async_tree_eager_tg              | 47.8 ms                                                | 43.3 ms: 1.10x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 63.8 ms: 1.10x faster                                                     |
| thrift                           | 466 us                                                 | 426 us: 1.09x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 2.98 sec: 1.09x faster                                                    |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| scimark_fft                      | 201 ms                                                 | 185 ms: 1.08x faster                                                      |
| html5lib                         | 36.6 ms                                                | 33.8 ms: 1.08x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| raytrace                         | 181 ms                                                 | 169 ms: 1.07x faster                                                      |
| fannkuch                         | 284 ms                                                 | 265 ms: 1.07x faster                                                      |
| bench_thread_pool                | 505 us                                                 | 474 us: 1.06x faster                                                      |
| regex_compile                    | 78.6 ms                                                | 74.0 ms: 1.06x faster                                                     |
| typing_runtime_protocols         | 101 us                                                 | 95.3 us: 1.06x faster                                                     |
| json                             | 3.03 ms                                                | 2.87 ms: 1.06x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                      |
| pycparser                        | 705 ms                                                 | 673 ms: 1.05x faster                                                      |
| telco                            | 4.76 ms                                                | 4.55 ms: 1.05x faster                                                     |
| nqueens                          | 62.5 ms                                                | 59.9 ms: 1.04x faster                                                     |
| coverage                         | 46.0 ms                                                | 44.1 ms: 1.04x faster                                                     |
| pathlib                          | 23.4 ms                                                | 22.5 ms: 1.04x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 16.3 ms: 1.04x faster                                                     |
| 2to3                             | 187 ms                                                 | 182 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 337 ms: 1.03x faster                                                      |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 365 ms: 1.02x faster                                                      |
| richards_super                   | 39.1 ms                                                | 38.3 ms: 1.02x faster                                                     |
| crypto_pyaes                     | 54.2 ms                                                | 53.1 ms: 1.02x faster                                                     |
| richards                         | 35.2 ms                                                | 34.5 ms: 1.02x faster                                                     |
| sqlglot_normalize                | 189 ms                                                 | 186 ms: 1.02x faster                                                      |
| bench_mp_pool                    | 62.5 ms                                                | 61.7 ms: 1.01x faster                                                     |
| meteor_contest                   | 74.0 ms                                                | 73.1 ms: 1.01x faster                                                     |
| sqlglot_parse                    | 856 us                                                 | 849 us: 1.01x faster                                                      |
| regex_v8                         | 17.0 ms                                                | 16.9 ms: 1.01x faster                                                     |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.62 ms: 1.00x faster                                                     |
| python_startup                   | 18.9 ms                                                | 19.0 ms: 1.01x slower                                                     |
| logging_silent                   | 70.1 ns                                                | 70.7 ns: 1.01x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 249 ms: 1.01x slower                                                      |
| django_template                  | 22.2 ms                                                | 22.5 ms: 1.01x slower                                                     |
| gc_traversal                     | 2.91 ms                                                | 2.95 ms: 1.01x slower                                                     |
| python_startup_no_site           | 14.5 ms                                                | 14.7 ms: 1.01x slower                                                     |
| chaos                            | 41.2 ms                                                | 41.8 ms: 1.01x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.04 ms: 1.02x slower                                                     |
| hexiom                           | 4.86 ms                                                | 4.95 ms: 1.02x slower                                                     |
| sympy_str                        | 145 ms                                                 | 151 ms: 1.04x slower                                                      |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.11 ms: 1.04x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 471 ms: 1.05x slower                                                      |
| sympy_sum                        | 75.4 ms                                                | 79.2 ms: 1.05x slower                                                     |
| sqlglot_optimize                 | 34.9 ms                                                | 36.9 ms: 1.06x slower                                                     |
| comprehensions                   | 12.3 us                                                | 13.0 us: 1.06x slower                                                     |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| sympy_integrate                  | 11.3 ms                                                | 12.5 ms: 1.10x slower                                                     |
| sphinx                           | 603 ms                                                 | 668 ms: 1.11x slower                                                      |
| json_dumps                       | 6.52 ms                                                | 7.23 ms: 1.11x slower                                                     |
| genshi_xml                       | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                     |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.13x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 584 ms: 1.15x slower                                                      |
| pylint                           | 180 ms                                                 | 210 ms: 1.16x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 613 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 672 ms: 1.31x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (8): xml_etree_iterparse, async_tree_cpu_io_mixed, async_generators, asyncio_websockets, dulwich_log, regex_dna, xml_etree_parse, tornado_http
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-darwin-arm64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.043x faster
# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x