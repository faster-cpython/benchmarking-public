# Results vs. 3.13.0

- fork: brandtbucher
- ref: justin_no_externs
- machine: darwin-arm64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.031x faster
- HPT reliability: 99.51%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| html5lib       | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| sphinx         | 603 ms                                                 | 666 ms: 1.11x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.8 ms: 1.12x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                      |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 64.2 ms: 1.09x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                      |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.06x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                      |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 470 ms: 1.05x slower                                                      |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                                      |
| async_tree_eager_io              | 514 ms                                                 | 666 ms: 1.30x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.6 ms: 1.15x faster                                                     |
| nbody          | 74.0 ms                                                | 65.0 ms: 1.14x faster                                                     |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 149 ms                                                 | 144 ms: 1.04x faster                                                      |
| regex_effbot   | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                     |
| regex_compile  | 78.6 ms                                                | 76.6 ms: 1.03x faster                                                     |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.27 sec: 1.24x faster                                                    |
| unpickle_pure_python | 164 us                                                 | 133 us: 1.23x faster                                                      |
| pickle_pure_python   | 214 us                                                 | 179 us: 1.20x faster                                                      |
| xml_etree_process    | 41.0 ms                                                | 34.6 ms: 1.18x faster                                                     |
| xml_etree_generate   | 57.0 ms                                                | 49.6 ms: 1.15x faster                                                     |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                     |
| xml_etree_parse      | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| xml_etree_iterparse  | 73.6 ms                                                | 72.6 ms: 1.01x faster                                                     |
| json_dumps           | 6.52 ms                                                | 7.16 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 18.1 ms: 1.04x faster                                                     |
| python_startup_no_site | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.58 ms: 1.17x faster                                                     |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                     |
| django_template | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                     |
| genshi_xml      | 34.4 ms                                                | 44.1 ms: 1.28x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241025-darwin-arm64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo                    | 27.4 us                                                | 16.7 us: 1.64x faster                                                     |
| deepcopy                         | 237 us                                                 | 156 us: 1.51x faster                                                      |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.36x faster                                                     |
| generators                       | 31.5 ms                                                | 24.9 ms: 1.26x faster                                                     |
| tomli_loads                      | 1.57 sec                                               | 1.27 sec: 1.24x faster                                                    |
| unpickle_pure_python             | 164 us                                                 | 133 us: 1.23x faster                                                      |
| async_tree_memoization_tg        | 288 ms                                                 | 234 ms: 1.23x faster                                                      |
| scimark_sor                      | 105 ms                                                 | 86.8 ms: 1.21x faster                                                     |
| scimark_lu                       | 76.7 ms                                                | 64.1 ms: 1.20x faster                                                     |
| pickle_pure_python               | 214 us                                                 | 179 us: 1.20x faster                                                      |
| coroutines                       | 19.8 ms                                                | 16.5 ms: 1.20x faster                                                     |
| xml_etree_process                | 41.0 ms                                                | 34.6 ms: 1.18x faster                                                     |
| mako                             | 7.68 ms                                                | 6.58 ms: 1.17x faster                                                     |
| logging_simple                   | 3.60 us                                                | 3.11 us: 1.16x faster                                                     |
| float                            | 56.0 ms                                                | 48.6 ms: 1.15x faster                                                     |
| xml_etree_generate               | 57.0 ms                                                | 49.6 ms: 1.15x faster                                                     |
| nbody                            | 74.0 ms                                                | 65.0 ms: 1.14x faster                                                     |
| logging_format                   | 3.89 us                                                | 3.42 us: 1.14x faster                                                     |
| go                               | 115 ms                                                 | 102 ms: 1.13x faster                                                      |
| html5lib                         | 36.6 ms                                                | 32.6 ms: 1.12x faster                                                     |
| async_tree_eager_tg              | 47.8 ms                                                | 42.8 ms: 1.12x faster                                                     |
| thrift                           | 466 us                                                 | 423 us: 1.10x faster                                                      |
| deltablue                        | 2.68 ms                                                | 2.43 ms: 1.10x faster                                                     |
| scimark_monte_carlo              | 50.4 ms                                                | 45.8 ms: 1.10x faster                                                     |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                      |
| spectral_norm                    | 76.3 ms                                                | 69.6 ms: 1.09x faster                                                     |
| async_tree_memoization           | 268 ms                                                 | 246 ms: 1.09x faster                                                      |
| async_tree_eager                 | 70.1 ms                                                | 64.2 ms: 1.09x faster                                                     |
| async_tree_none                  | 215 ms                                                 | 199 ms: 1.08x faster                                                      |
| bpe_tokeniser                    | 3.25 sec                                               | 3.03 sec: 1.07x faster                                                    |
| bench_thread_pool                | 505 us                                                 | 471 us: 1.07x faster                                                      |
| pyflate                          | 351 ms                                                 | 330 ms: 1.06x faster                                                      |
| json                             | 3.03 ms                                                | 2.86 ms: 1.06x faster                                                     |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 131 ms: 1.06x faster                                                      |
| fannkuch                         | 284 ms                                                 | 269 ms: 1.06x faster                                                      |
| nqueens                          | 62.5 ms                                                | 59.4 ms: 1.05x faster                                                     |
| raytrace                         | 181 ms                                                 | 172 ms: 1.05x faster                                                      |
| coverage                         | 46.0 ms                                                | 44.0 ms: 1.05x faster                                                     |
| python_startup                   | 18.9 ms                                                | 18.1 ms: 1.04x faster                                                     |
| scimark_fft                      | 201 ms                                                 | 192 ms: 1.04x faster                                                      |
| pprint_safe_repr                 | 533 ms                                                 | 511 ms: 1.04x faster                                                      |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                                     |
| pprint_pformat                   | 1.08 sec                                               | 1.04 sec: 1.04x faster                                                    |
| typing_runtime_protocols         | 101 us                                                 | 97.6 us: 1.04x faster                                                     |
| regex_dna                        | 149 ms                                                 | 144 ms: 1.04x faster                                                      |
| pathlib                          | 23.4 ms                                                | 22.6 ms: 1.04x faster                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                      |
| regex_effbot                     | 2.63 ms                                                | 2.56 ms: 1.03x faster                                                     |
| regex_compile                    | 78.6 ms                                                | 76.6 ms: 1.03x faster                                                     |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.56 ms: 1.02x faster                                                     |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                                     |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                     |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                     |
| xml_etree_parse                  | 107 ms                                                 | 105 ms: 1.02x faster                                                      |
| richards_super                   | 39.1 ms                                                | 38.4 ms: 1.02x faster                                                     |
| pycparser                        | 705 ms                                                 | 693 ms: 1.02x faster                                                      |
| bench_mp_pool                    | 62.5 ms                                                | 61.6 ms: 1.02x faster                                                     |
| python_startup_no_site           | 14.5 ms                                                | 14.3 ms: 1.01x faster                                                     |
| xml_etree_iterparse              | 73.6 ms                                                | 72.6 ms: 1.01x faster                                                     |
| richards                         | 35.2 ms                                                | 34.8 ms: 1.01x faster                                                     |
| async_generators                 | 295 ms                                                 | 292 ms: 1.01x faster                                                      |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                      |
| sqlglot_normalize                | 189 ms                                                 | 190 ms: 1.01x slower                                                      |
| meteor_contest                   | 74.0 ms                                                | 74.6 ms: 1.01x slower                                                     |
| gc_traversal                     | 2.91 ms                                                | 2.94 ms: 1.01x slower                                                     |
| crypto_pyaes                     | 54.2 ms                                                | 54.9 ms: 1.01x slower                                                     |
| sympy_expand                     | 246 ms                                                 | 250 ms: 1.02x slower                                                      |
| dulwich_log                      | 28.5 ms                                                | 29.2 ms: 1.03x slower                                                     |
| chaos                            | 41.2 ms                                                | 42.3 ms: 1.03x slower                                                     |
| sqlglot_parse                    | 856 us                                                 | 888 us: 1.04x slower                                                      |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.05x slower                                                    |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 470 ms: 1.05x slower                                                      |
| sqlalchemy_declarative           | 58.9 ms                                                | 61.9 ms: 1.05x slower                                                     |
| sympy_str                        | 145 ms                                                 | 154 ms: 1.06x slower                                                      |
| sqlglot_transpile                | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                     |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.17 ms: 1.06x slower                                                     |
| hexiom                           | 4.86 ms                                                | 5.17 ms: 1.06x slower                                                     |
| sympy_sum                        | 75.4 ms                                                | 80.4 ms: 1.07x slower                                                     |
| async_tree_none_tg               | 198 ms                                                 | 213 ms: 1.08x slower                                                      |
| django_template                  | 22.2 ms                                                | 24.1 ms: 1.08x slower                                                     |
| sqlglot_optimize                 | 34.9 ms                                                | 38.0 ms: 1.09x slower                                                     |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                    |
| json_dumps                       | 6.52 ms                                                | 7.16 ms: 1.10x slower                                                     |
| comprehensions                   | 12.3 us                                                | 13.5 us: 1.10x slower                                                     |
| sphinx                           | 603 ms                                                 | 666 ms: 1.11x slower                                                      |
| sympy_integrate                  | 11.3 ms                                                | 12.7 ms: 1.12x slower                                                     |
| create_gc_cycles                 | 1.17 ms                                                | 1.32 ms: 1.13x slower                                                     |
| async_tree_io                    | 507 ms                                                 | 582 ms: 1.15x slower                                                      |
| pylint                           | 180 ms                                                 | 215 ms: 1.20x slower                                                      |
| async_tree_io_tg                 | 497 ms                                                 | 611 ms: 1.23x slower                                                      |
| genshi_xml                       | 34.4 ms                                                | 44.1 ms: 1.28x slower                                                     |
| async_tree_eager_io              | 514 ms                                                 | 666 ms: 1.30x slower                                                      |
| async_tree_eager_io_tg           | 477 ms                                                 | 714 ms: 1.50x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (5): tornado_http, 2to3, async_tree_cpu_io_mixed, asyncio_websockets, logging_silent
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path

- Geometric mean (including insignificant results): 1.031x faster
# HPT report

- Reliability score: 99.51% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x