# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.041x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 170 ms: 1.10x faster                                                   |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                 |
| html5lib       | 36.6 ms                                                | 31.2 ms: 1.17x faster                                                  |
| sphinx         | 603 ms                                                 | 591 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                                   |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.6 ms: 1.10x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 44.3 ms: 1.08x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 254 ms: 1.06x faster                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                                   |
| async_tree_none                  | 215 ms                                                 | 206 ms: 1.04x faster                                                   |
| async_generators                 | 295 ms                                                 | 283 ms: 1.04x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 339 ms: 1.02x faster                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 480 ms: 1.07x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 221 ms: 1.12x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 590 ms: 1.16x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 629 ms: 1.27x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 684 ms: 1.33x slower                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 732 ms: 1.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 68.1 ms: 1.09x faster                                                  |
| float          | 56.0 ms                                                | 53.1 ms: 1.06x faster                                                  |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.32 ms: 1.13x faster                                                  |
| regex_compile  | 78.6 ms                                                | 71.9 ms: 1.09x faster                                                  |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| regex_v8       | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 164 us                                                 | 154 us: 1.07x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 54.5 ms: 1.05x faster                                                  |
| xml_etree_process    | 41.0 ms                                                | 39.5 ms: 1.04x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 208 us: 1.03x faster                                                   |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| xml_etree_parse      | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 73.6 ms                                                | 74.9 ms: 1.02x slower                                                  |
| json_dumps           | 6.52 ms                                                | 7.22 ms: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 13.4 ms: 1.08x faster                                                  |
| python_startup         | 18.9 ms                                                | 18.0 ms: 1.05x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.4 ms: 1.17x faster                                                  |
| genshi_xml      | 34.4 ms                                                | 31.0 ms: 1.11x faster                                                  |
| mako            | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| django_template | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.10x faster                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 153 us: 1.55x faster                                                   |
| deepcopy_memo                    | 27.4 us                                                | 18.3 us: 1.49x faster                                                  |
| generators                       | 31.5 ms                                                | 22.5 ms: 1.40x faster                                                  |
| go                               | 115 ms                                                 | 87.3 ms: 1.32x faster                                                  |
| deepcopy_reduce                  | 2.07 us                                                | 1.59 us: 1.30x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 240 ms: 1.20x faster                                                   |
| genshi_text                      | 16.9 ms                                                | 14.4 ms: 1.17x faster                                                  |
| html5lib                         | 36.6 ms                                                | 31.2 ms: 1.17x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.32 ms: 1.13x faster                                                  |
| coroutines                       | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| genshi_xml                       | 34.4 ms                                                | 31.0 ms: 1.11x faster                                                  |
| logging_simple                   | 3.60 us                                                | 3.25 us: 1.11x faster                                                  |
| pprint_safe_repr                 | 533 ms                                                 | 482 ms: 1.11x faster                                                   |
| pprint_pformat                   | 1.08 sec                                               | 981 ms: 1.10x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                   |
| async_tree_eager                 | 70.1 ms                                                | 63.6 ms: 1.10x faster                                                  |
| 2to3                             | 187 ms                                                 | 170 ms: 1.10x faster                                                   |
| regex_compile                    | 78.6 ms                                                | 71.9 ms: 1.09x faster                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 46.1 ms: 1.09x faster                                                  |
| regex_dna                        | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| logging_format                   | 3.89 us                                                | 3.57 us: 1.09x faster                                                  |
| hexiom                           | 4.86 ms                                                | 4.47 ms: 1.09x faster                                                  |
| nbody                            | 74.0 ms                                                | 68.1 ms: 1.09x faster                                                  |
| bench_thread_pool                | 505 us                                                 | 465 us: 1.09x faster                                                   |
| deltablue                        | 2.68 ms                                                | 2.47 ms: 1.08x faster                                                  |
| nqueens                          | 62.5 ms                                                | 57.9 ms: 1.08x faster                                                  |
| async_tree_eager_tg              | 47.8 ms                                                | 44.3 ms: 1.08x faster                                                  |
| python_startup_no_site           | 14.5 ms                                                | 13.4 ms: 1.08x faster                                                  |
| mako                             | 7.68 ms                                                | 7.13 ms: 1.08x faster                                                  |
| pycparser                        | 705 ms                                                 | 656 ms: 1.08x faster                                                   |
| regex_v8                         | 17.0 ms                                                | 15.8 ms: 1.07x faster                                                  |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                                   |
| fannkuch                         | 284 ms                                                 | 265 ms: 1.07x faster                                                   |
| unpickle_pure_python             | 164 us                                                 | 154 us: 1.07x faster                                                   |
| pathlib                          | 23.4 ms                                                | 21.9 ms: 1.07x faster                                                  |
| sqlglot_parse                    | 856 us                                                 | 803 us: 1.07x faster                                                   |
| raytrace                         | 181 ms                                                 | 170 ms: 1.07x faster                                                   |
| sqlglot_normalize                | 189 ms                                                 | 178 ms: 1.06x faster                                                   |
| spectral_norm                    | 76.3 ms                                                | 71.9 ms: 1.06x faster                                                  |
| sqlglot_optimize                 | 34.9 ms                                                | 33.0 ms: 1.06x faster                                                  |
| scimark_sor                      | 105 ms                                                 | 99.8 ms: 1.06x faster                                                  |
| float                            | 56.0 ms                                                | 53.1 ms: 1.06x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 254 ms: 1.06x faster                                                   |
| django_template                  | 22.2 ms                                                | 21.1 ms: 1.05x faster                                                  |
| chaos                            | 41.2 ms                                                | 39.1 ms: 1.05x faster                                                  |
| python_startup                   | 18.9 ms                                                | 18.0 ms: 1.05x faster                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 975 us: 1.05x faster                                                   |
| richards_super                   | 39.1 ms                                                | 37.4 ms: 1.05x faster                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 132 ms: 1.05x faster                                                   |
| xml_etree_generate               | 57.0 ms                                                | 54.5 ms: 1.05x faster                                                  |
| async_tree_none                  | 215 ms                                                 | 206 ms: 1.04x faster                                                   |
| sympy_expand                     | 246 ms                                                 | 236 ms: 1.04x faster                                                   |
| telco                            | 4.76 ms                                                | 4.57 ms: 1.04x faster                                                  |
| async_generators                 | 295 ms                                                 | 283 ms: 1.04x faster                                                   |
| richards                         | 35.2 ms                                                | 33.8 ms: 1.04x faster                                                  |
| pyflate                          | 351 ms                                                 | 338 ms: 1.04x faster                                                   |
| sympy_str                        | 145 ms                                                 | 140 ms: 1.04x faster                                                   |
| scimark_lu                       | 76.7 ms                                                | 73.9 ms: 1.04x faster                                                  |
| xml_etree_process                | 41.0 ms                                                | 39.5 ms: 1.04x faster                                                  |
| scimark_fft                      | 201 ms                                                 | 193 ms: 1.04x faster                                                   |
| typing_runtime_protocols         | 101 us                                                 | 97.6 us: 1.04x faster                                                  |
| coverage                         | 46.0 ms                                                | 44.4 ms: 1.04x faster                                                  |
| pickle_pure_python               | 214 us                                                 | 208 us: 1.03x faster                                                   |
| sympy_sum                        | 75.4 ms                                                | 73.0 ms: 1.03x faster                                                  |
| bench_mp_pool                    | 62.5 ms                                                | 60.7 ms: 1.03x faster                                                  |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.50 ms: 1.03x faster                                                  |
| bpe_tokeniser                    | 3.25 sec                                               | 3.17 sec: 1.03x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 364 ms: 1.02x faster                                                   |
| json                             | 3.03 ms                                                | 2.96 ms: 1.02x faster                                                  |
| logging_silent                   | 70.1 ns                                                | 68.5 ns: 1.02x faster                                                  |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 339 ms: 1.02x faster                                                   |
| tomli_loads                      | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                 |
| sphinx                           | 603 ms                                                 | 591 ms: 1.02x faster                                                   |
| meteor_contest                   | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| crypto_pyaes                     | 54.2 ms                                                | 53.6 ms: 1.01x faster                                                  |
| dulwich_log                      | 28.5 ms                                                | 28.3 ms: 1.01x faster                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 58.7 ms: 1.00x faster                                                  |
| shortest_path                    | 347 ms                                                 | 346 ms: 1.00x faster                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.98 ms: 1.00x faster                                                  |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                   |
| gc_traversal                     | 2.91 ms                                                | 2.92 ms: 1.00x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.00x slower                                                 |
| connected_components             | 319 ms                                                 | 321 ms: 1.01x slower                                                   |
| comprehensions                   | 12.3 us                                                | 12.4 us: 1.01x slower                                                  |
| mdp                              | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                  |
| xml_etree_iterparse              | 73.6 ms                                                | 74.9 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 469 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 480 ms: 1.07x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 7.22 ms: 1.11x slower                                                  |
| create_gc_cycles                 | 1.17 ms                                                | 1.30 ms: 1.12x slower                                                  |
| async_tree_none_tg               | 198 ms                                                 | 221 ms: 1.12x slower                                                   |
| async_tree_io                    | 507 ms                                                 | 590 ms: 1.16x slower                                                   |
| async_tree_io_tg                 | 497 ms                                                 | 629 ms: 1.27x slower                                                   |
| async_tree_eager_io              | 514 ms                                                 | 684 ms: 1.33x slower                                                   |
| k_core                           | 1.61 sec                                               | 2.30 sec: 1.43x slower                                                 |
| async_tree_eager_io_tg           | 477 ms                                                 | 732 ms: 1.53x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.041x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.02x