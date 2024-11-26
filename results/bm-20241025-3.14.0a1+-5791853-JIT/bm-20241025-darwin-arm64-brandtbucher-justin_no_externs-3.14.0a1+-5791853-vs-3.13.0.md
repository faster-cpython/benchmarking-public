# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.027x faster
- HPT reliability: 98.25%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| html5lib       | 36.6 ms                                                | 32.8 ms: 1.11x faster                                                     |
| sphinx         | 603 ms                                                 | 668 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.6 ms: 1.12x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 64.9 ms: 1.08x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.05x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 612 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, async_generators

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                     |
| nbody          | 74.0 ms                                                | 65.2 ms: 1.14x faster                                                     |
| Geometric mean | (ref)                                                  | 1.09x faster                                                              |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                     |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| regex_compile  | 78.6 ms                                                | 76.6 ms: 1.03x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.27 sec: 1.24x faster                                                    |
| unpickle_pure_python | 164 us                                                 | 133 us: 1.23x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 180 us: 1.19x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 35.2 ms: 1.16x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                | 49.7 ms: 1.15x faster                                                     |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                     |
| xml_etree_iterparse  | 73.6 ms                                                | 72.7 ms: 1.01x faster                                                     |
| json_dumps           | 6.52 ms                                                | 7.16 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 18.2 ms: 1.04x faster                                                     |
| python_startup_no_site | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.56 ms: 1.17x faster                                                     |
| django_template | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                     |
| genshi_text     | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 43.9 ms: 1.28x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                                     |
| deepcopy                         | 237 us                                                 | 156 us: 1.52x faster                                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.53 us: 1.35x faster                                                     |
| generators                       | 31.5 ms                                                | 24.9 ms: 1.27x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.27 sec: 1.24x faster                                                    |
| unpickle_pure_python             | 164 us                                                 | 133 us: 1.23x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                      |
| scimark_sor                      | 105 ms                                                 | 87.3 ms: 1.21x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 180 us: 1.19x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.7 ms: 1.18x faster                                                     |
| mako                             | 7.68 ms                                                | 6.56 ms: 1.17x faster                                                     |
| scimark_lu                       | 76.7 ms                                                | 65.6 ms: 1.17x faster                                                     |
| xml_etree_process                | 41.0 ms                                                | 35.2 ms: 1.16x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.13 us: 1.15x faster                                                     |
| float                            | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                     |
| xml_etree_generate               | 57.0 ms                                                | 49.7 ms: 1.15x faster                                                     |
| go                               | 115 ms                                                 | 101 ms: 1.14x faster                                                      |
| logging_format                   | 3.89 us                                                | 3.42 us: 1.14x faster                                                     |
| nbody                            | 74.0 ms                                                | 65.2 ms: 1.14x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.6 ms: 1.12x faster                                                     |
| html5lib                         | 36.6 ms                                                | 32.8 ms: 1.11x faster                                                     |
| thrift                           | 466 us                                                 | 422 us: 1.11x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| deltablue                        | 2.68 ms                                                | 2.46 ms: 1.09x faster                                                     |
| spectral_norm                    | 76.3 ms                                                | 70.1 ms: 1.09x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 46.5 ms: 1.08x faster                                                     |
| async_tree_eager                 | 70.1 ms                                                | 64.9 ms: 1.08x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 200 ms: 1.08x faster                                                      |
| json                             | 3.03 ms                                                | 2.85 ms: 1.06x faster                                                     |
| regex_effbot                     | 2.63 ms                                                | 2.47 ms: 1.06x faster                                                     |
| bench_thread_pool                | 505 us                                                 | 477 us: 1.06x faster                                                      |
| pyflate                          | 351 ms                                                 | 332 ms: 1.06x faster                                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                    |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.05x faster                                                      |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                      |
| coverage                         | 46.0 ms                                                | 44.0 ms: 1.05x faster                                                     |
| pathlib                          | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                     |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                                     |
| nqueens                          | 62.5 ms                                                | 60.1 ms: 1.04x faster                                                     |
| typing_runtime_protocols         | 101 us                                                 | 97.5 us: 1.04x faster                                                     |
| python_startup                   | 18.9 ms                                                | 18.2 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                     |
| regex_compile                    | 78.6 ms                                                | 76.6 ms: 1.03x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                      |
| pprint_safe_repr                 | 533 ms                                                 | 521 ms: 1.02x faster                                                      |
| pprint_pformat                   | 1.08 sec                                               | 1.06 sec: 1.02x faster                                                    |
| raytrace                         | 181 ms                                                 | 177 ms: 1.02x faster                                                      |
| richards_super                   | 39.1 ms                                                | 38.4 ms: 1.02x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| pycparser                        | 705 ms                                                 | 694 ms: 1.02x faster                                                      |
| richards                         | 35.2 ms                                                | 34.7 ms: 1.02x faster                                                     |
| python_startup_no_site           | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                     |
| 2to3                             | 187 ms                                                 | 185 ms: 1.01x faster                                                      |
| xml_etree_iterparse              | 73.6 ms                                                | 72.7 ms: 1.01x faster                                                     |
| bench_mp_pool                    | 62.5 ms                                                | 61.9 ms: 1.01x faster                                                     |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.64 ms: 1.01x faster                                                     |
| logging_silent                   | 70.1 ns                                                | 69.7 ns: 1.01x faster                                                     |
| fannkuch                         | 284 ms                                                 | 282 ms: 1.01x faster                                                      |
| sqlglot_normalize                | 189 ms                                                 | 190 ms: 1.00x slower                                                      |
| meteor_contest                   | 74.0 ms                                                | 75.1 ms: 1.01x slower                                                     |
| gc_traversal                     | 2.91 ms                                                | 2.96 ms: 1.02x slower                                                     |
| crypto_pyaes                     | 54.2 ms                                                | 55.2 ms: 1.02x slower                                                     |
| dulwich_log                      | 28.5 ms                                                | 29.1 ms: 1.02x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 253 ms: 1.03x slower                                                      |
| chaos                            | 41.2 ms                                                | 42.6 ms: 1.03x slower                                                     |
| sqlglot_parse                    | 856 us                                                 | 889 us: 1.04x slower                                                      |
| django_template                  | 22.2 ms                                                | 23.2 ms: 1.04x slower                                                     |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                    |
| genshi_text                      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                     |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 468 ms: 1.05x slower                                                      |
| sympy_str                        | 145 ms                                                 | 153 ms: 1.05x slower                                                      |
| hexiom                           | 4.86 ms                                                | 5.15 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.17 ms: 1.06x slower                                                     |
| sqlglot_transpile                | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                     |
| sqlalchemy_declarative           | 58.9 ms                                                | 62.5 ms: 1.06x slower                                                     |
| sympy_sum                        | 75.4 ms                                                | 81.0 ms: 1.07x slower                                                     |
| async_tree_none_tg               | 198 ms                                                 | 214 ms: 1.08x slower                                                      |
| sqlglot_optimize                 | 34.9 ms                                                | 38.0 ms: 1.09x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| json_dumps                       | 6.52 ms                                                | 7.16 ms: 1.10x slower                                                     |
| comprehensions                   | 12.3 us                                                | 13.6 us: 1.11x slower                                                     |
| sphinx                           | 603 ms                                                 | 668 ms: 1.11x slower                                                      |
| sympy_integrate                  | 11.3 ms                                                | 12.7 ms: 1.12x slower                                                     |
| create_gc_cycles                 | 1.17 ms                                                | 1.34 ms: 1.14x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 583 ms: 1.15x slower                                                      |
| pylint                           | 180 ms                                                 | 217 ms: 1.21x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 612 ms: 1.23x slower                                                      |
| genshi_xml                       | 34.4 ms                                                | 43.9 ms: 1.28x slower                                                     |
| async_tree_eager_io              | 514 ms                                                 | 667 ms: 1.30x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 715 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (6): tornado_http, async_tree_cpu_io_mixed, asyncio_websockets, async_generators, pidigits, xml_etree_parse
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.027x faster
# HPT report

- Reliability score: 98.25% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x