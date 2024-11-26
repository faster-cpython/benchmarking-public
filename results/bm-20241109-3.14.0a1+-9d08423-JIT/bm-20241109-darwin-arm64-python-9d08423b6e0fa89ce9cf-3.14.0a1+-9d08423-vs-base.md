# Results vs. base

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.019x slower
- HPT reliability: 99.54%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 170 ms                                                                                                            | 212 ms: 1.25x slower                                                                                                  |
| docutils       | 1.45 sec                                                                                                          | 1.58 sec: 1.10x slower                                                                                                |
| html5lib       | 31.2 ms                                                                                                           | 33.0 ms: 1.06x slower                                                                                                 |
| sphinx         | 591 ms                                                                                                            | 675 ms: 1.14x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.13x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_none_tg               | 221 ms                                                                                                            | 207 ms: 1.07x faster                                                                                                  |
| async_tree_eager_io_tg           | 732 ms                                                                                                            | 729 ms: 1.01x faster                                                                                                  |
| async_tree_io_tg                 | 629 ms                                                                                                            | 627 ms: 1.00x faster                                                                                                  |
| coroutines                       | 17.5 ms                                                                                                           | 17.5 ms: 1.00x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                            | 370 ms: 1.02x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                                                            | 346 ms: 1.02x slower                                                                                                  |
| async_tree_eager_tg              | 44.3 ms                                                                                                           | 45.4 ms: 1.03x slower                                                                                                 |
| async_tree_eager_memoization     | 153 ms                                                                                                            | 157 ms: 1.03x slower                                                                                                  |
| async_tree_eager                 | 63.6 ms                                                                                                           | 66.8 ms: 1.05x slower                                                                                                 |
| async_generators                 | 283 ms                                                                                                            | 306 ms: 1.08x slower                                                                                                  |
| Geometric mean                   | (ref)                                                                                                             | 1.01x slower                                                                                                          |

Benchmark hidden because not significant (9): async_tree_memoization, asyncio_websockets, async_tree_none, async_tree_eager_io, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| float          | 53.1 ms                                                                                                           | 48.8 ms: 1.09x faster                                                                                                 |
| nbody          | 68.1 ms                                                                                                           | 63.5 ms: 1.07x faster                                                                                                 |
| pidigits       | 283 ms                                                                                                            | 283 ms: 1.00x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                             | 1.05x faster                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 2.32 ms                                                                                                           | 2.33 ms: 1.00x slower                                                                                                 |
| regex_dna      | 137 ms                                                                                                            | 137 ms: 1.01x slower                                                                                                  |
| regex_v8       | 15.8 ms                                                                                                           | 15.9 ms: 1.01x slower                                                                                                 |
| regex_compile  | 71.9 ms                                                                                                           | 76.7 ms: 1.07x slower                                                                                                 |
| Geometric mean | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads          | 1.54 sec                                                                                                          | 1.25 sec: 1.23x faster                                                                                                |
| xml_etree_process    | 39.5 ms                                                                                                           | 35.3 ms: 1.12x faster                                                                                                 |
| xml_etree_generate   | 54.5 ms                                                                                                           | 49.5 ms: 1.10x faster                                                                                                 |
| unpickle_pure_python | 154 us                                                                                                            | 142 us: 1.09x faster                                                                                                  |
| pickle_pure_python   | 208 us                                                                                                            | 194 us: 1.07x faster                                                                                                  |
| xml_etree_iterparse  | 74.9 ms                                                                                                           | 72.8 ms: 1.03x faster                                                                                                 |
| json_dumps           | 7.22 ms                                                                                                           | 7.10 ms: 1.02x faster                                                                                                 |
| Geometric mean       | (ref)                                                                                                             | 1.07x faster                                                                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup_no_site | 13.4 ms                                                                                                           | 14.0 ms: 1.04x slower                                                                                                 |
| python_startup         | 18.0 ms                                                                                                           | 18.8 ms: 1.05x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                             | 1.04x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| mako            | 7.13 ms                                                                                                           | 6.24 ms: 1.14x faster                                                                                                 |
| django_template | 21.1 ms                                                                                                           | 23.5 ms: 1.12x slower                                                                                                 |
| genshi_text     | 14.4 ms                                                                                                           | 17.3 ms: 1.21x slower                                                                                                 |
| genshi_xml      | 31.0 ms                                                                                                           | 39.7 ms: 1.28x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                             | 1.11x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                        | results/bm-20241109-3.14.0a1+-9d08423/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json | results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json |
|----------------------------------|:-----------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| tomli_loads                      | 1.54 sec                                                                                                          | 1.25 sec: 1.23x faster                                                                                                |
| scimark_sor                      | 99.8 ms                                                                                                           | 87.0 ms: 1.15x faster                                                                                                 |
| mako                             | 7.13 ms                                                                                                           | 6.24 ms: 1.14x faster                                                                                                 |
| xml_etree_process                | 39.5 ms                                                                                                           | 35.3 ms: 1.12x faster                                                                                                 |
| xml_etree_generate               | 54.5 ms                                                                                                           | 49.5 ms: 1.10x faster                                                                                                 |
| float                            | 53.1 ms                                                                                                           | 48.8 ms: 1.09x faster                                                                                                 |
| unpickle_pure_python             | 154 us                                                                                                            | 142 us: 1.09x faster                                                                                                  |
| connected_components             | 321 ms                                                                                                            | 298 ms: 1.08x faster                                                                                                  |
| scimark_lu                       | 73.9 ms                                                                                                           | 68.7 ms: 1.07x faster                                                                                                 |
| nbody                            | 68.1 ms                                                                                                           | 63.5 ms: 1.07x faster                                                                                                 |
| pickle_pure_python               | 208 us                                                                                                            | 194 us: 1.07x faster                                                                                                  |
| async_tree_none_tg               | 221 ms                                                                                                            | 207 ms: 1.07x faster                                                                                                  |
| bpe_tokeniser                    | 3.17 sec                                                                                                          | 2.98 sec: 1.06x faster                                                                                                |
| shortest_path                    | 346 ms                                                                                                            | 329 ms: 1.05x faster                                                                                                  |
| scimark_fft                      | 193 ms                                                                                                            | 185 ms: 1.04x faster                                                                                                  |
| deepcopy_memo                    | 18.3 us                                                                                                           | 17.6 us: 1.04x faster                                                                                                 |
| pyflate                          | 338 ms                                                                                                            | 327 ms: 1.04x faster                                                                                                  |
| fannkuch                         | 265 ms                                                                                                            | 257 ms: 1.03x faster                                                                                                  |
| telco                            | 4.57 ms                                                                                                           | 4.43 ms: 1.03x faster                                                                                                 |
| deepcopy_reduce                  | 1.59 us                                                                                                           | 1.54 us: 1.03x faster                                                                                                 |
| spectral_norm                    | 71.9 ms                                                                                                           | 69.8 ms: 1.03x faster                                                                                                 |
| xml_etree_iterparse              | 74.9 ms                                                                                                           | 72.8 ms: 1.03x faster                                                                                                 |
| k_core                           | 2.30 sec                                                                                                          | 2.24 sec: 1.03x faster                                                                                                |
| scimark_monte_carlo              | 46.1 ms                                                                                                           | 45.0 ms: 1.02x faster                                                                                                 |
| json                             | 2.96 ms                                                                                                           | 2.91 ms: 1.02x faster                                                                                                 |
| json_dumps                       | 7.22 ms                                                                                                           | 7.10 ms: 1.02x faster                                                                                                 |
| async_tree_eager_io_tg           | 732 ms                                                                                                            | 729 ms: 1.01x faster                                                                                                  |
| async_tree_io_tg                 | 629 ms                                                                                                            | 627 ms: 1.00x faster                                                                                                  |
| pidigits                         | 283 ms                                                                                                            | 283 ms: 1.00x slower                                                                                                  |
| coroutines                       | 17.5 ms                                                                                                           | 17.5 ms: 1.00x slower                                                                                                 |
| richards                         | 33.8 ms                                                                                                           | 34.0 ms: 1.00x slower                                                                                                 |
| regex_effbot                     | 2.32 ms                                                                                                           | 2.33 ms: 1.00x slower                                                                                                 |
| coverage                         | 44.4 ms                                                                                                           | 44.6 ms: 1.00x slower                                                                                                 |
| regex_dna                        | 137 ms                                                                                                            | 137 ms: 1.01x slower                                                                                                  |
| regex_v8                         | 15.8 ms                                                                                                           | 15.9 ms: 1.01x slower                                                                                                 |
| pprint_safe_repr                 | 482 ms                                                                                                            | 487 ms: 1.01x slower                                                                                                  |
| logging_format                   | 3.57 us                                                                                                           | 3.61 us: 1.01x slower                                                                                                 |
| richards_super                   | 37.4 ms                                                                                                           | 37.8 ms: 1.01x slower                                                                                                 |
| logging_simple                   | 3.25 us                                                                                                           | 3.29 us: 1.01x slower                                                                                                 |
| sqlite_synth                     | 1.52 us                                                                                                           | 1.54 us: 1.01x slower                                                                                                 |
| create_gc_cycles                 | 1.30 ms                                                                                                           | 1.32 ms: 1.01x slower                                                                                                 |
| crypto_pyaes                     | 53.6 ms                                                                                                           | 54.5 ms: 1.02x slower                                                                                                 |
| async_tree_eager_cpu_io_mixed    | 364 ms                                                                                                            | 370 ms: 1.02x slower                                                                                                  |
| thrift                           | 435 us                                                                                                            | 442 us: 1.02x slower                                                                                                  |
| async_tree_eager_cpu_io_mixed_tg | 339 ms                                                                                                            | 346 ms: 1.02x slower                                                                                                  |
| pathlib                          | 21.9 ms                                                                                                           | 22.4 ms: 1.02x slower                                                                                                 |
| dulwich_log                      | 28.3 ms                                                                                                           | 29.0 ms: 1.03x slower                                                                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                                                                           | 3.06 ms: 1.03x slower                                                                                                 |
| async_tree_eager_tg              | 44.3 ms                                                                                                           | 45.4 ms: 1.03x slower                                                                                                 |
| async_tree_eager_memoization     | 153 ms                                                                                                            | 157 ms: 1.03x slower                                                                                                  |
| deepcopy                         | 153 us                                                                                                            | 157 us: 1.03x slower                                                                                                  |
| typing_runtime_protocols         | 97.6 us                                                                                                           | 101 us: 1.03x slower                                                                                                  |
| sqlalchemy_imperative            | 6.50 ms                                                                                                           | 6.71 ms: 1.03x slower                                                                                                 |
| pprint_pformat                   | 981 ms                                                                                                            | 1.02 sec: 1.04x slower                                                                                                |
| pycparser                        | 656 ms                                                                                                            | 680 ms: 1.04x slower                                                                                                  |
| python_startup_no_site           | 13.4 ms                                                                                                           | 14.0 ms: 1.04x slower                                                                                                 |
| python_startup                   | 18.0 ms                                                                                                           | 18.8 ms: 1.05x slower                                                                                                 |
| mdp                              | 1.51 sec                                                                                                          | 1.58 sec: 1.05x slower                                                                                                |
| bench_thread_pool                | 465 us                                                                                                            | 488 us: 1.05x slower                                                                                                  |
| async_tree_eager                 | 63.6 ms                                                                                                           | 66.8 ms: 1.05x slower                                                                                                 |
| deltablue                        | 2.47 ms                                                                                                           | 2.61 ms: 1.06x slower                                                                                                 |
| html5lib                         | 31.2 ms                                                                                                           | 33.0 ms: 1.06x slower                                                                                                 |
| bench_mp_pool                    | 60.7 ms                                                                                                           | 64.2 ms: 1.06x slower                                                                                                 |
| nqueens                          | 57.9 ms                                                                                                           | 61.7 ms: 1.07x slower                                                                                                 |
| regex_compile                    | 71.9 ms                                                                                                           | 76.7 ms: 1.07x slower                                                                                                 |
| logging_silent                   | 68.5 ns                                                                                                           | 73.5 ns: 1.07x slower                                                                                                 |
| sqlalchemy_declarative           | 58.7 ms                                                                                                           | 63.2 ms: 1.08x slower                                                                                                 |
| async_generators                 | 283 ms                                                                                                            | 306 ms: 1.08x slower                                                                                                  |
| raytrace                         | 170 ms                                                                                                            | 184 ms: 1.08x slower                                                                                                  |
| sqlglot_normalize                | 178 ms                                                                                                            | 193 ms: 1.08x slower                                                                                                  |
| sympy_expand                     | 236 ms                                                                                                            | 256 ms: 1.09x slower                                                                                                  |
| comprehensions                   | 12.4 us                                                                                                           | 13.5 us: 1.09x slower                                                                                                 |
| docutils                         | 1.45 sec                                                                                                          | 1.58 sec: 1.10x slower                                                                                                |
| sqlglot_parse                    | 803 us                                                                                                            | 882 us: 1.10x slower                                                                                                  |
| sympy_str                        | 140 ms                                                                                                            | 155 ms: 1.11x slower                                                                                                  |
| sympy_sum                        | 73.0 ms                                                                                                           | 80.9 ms: 1.11x slower                                                                                                 |
| sqlglot_transpile                | 975 us                                                                                                            | 1.08 ms: 1.11x slower                                                                                                 |
| chaos                            | 39.1 ms                                                                                                           | 43.5 ms: 1.11x slower                                                                                                 |
| django_template                  | 21.1 ms                                                                                                           | 23.5 ms: 1.12x slower                                                                                                 |
| sympy_integrate                  | 11.5 ms                                                                                                           | 12.8 ms: 1.12x slower                                                                                                 |
| hexiom                           | 4.47 ms                                                                                                           | 5.05 ms: 1.13x slower                                                                                                 |
| sphinx                           | 591 ms                                                                                                            | 675 ms: 1.14x slower                                                                                                  |
| go                               | 87.3 ms                                                                                                           | 101 ms: 1.15x slower                                                                                                  |
| sqlglot_optimize                 | 33.0 ms                                                                                                           | 38.1 ms: 1.15x slower                                                                                                 |
| generators                       | 22.5 ms                                                                                                           | 26.9 ms: 1.19x slower                                                                                                 |
| genshi_text                      | 14.4 ms                                                                                                           | 17.3 ms: 1.21x slower                                                                                                 |
| 2to3                             | 170 ms                                                                                                            | 212 ms: 1.25x slower                                                                                                  |
| genshi_xml                       | 31.0 ms                                                                                                           | 39.7 ms: 1.28x slower                                                                                                 |
| Geometric mean                   | (ref)                                                                                                             | 1.02x slower                                                                                                          |

Benchmark hidden because not significant (14): pylint, xml_etree_parse, async_tree_memoization, meteor_contest, asyncio_websockets, async_tree_none, gc_traversal, async_tree_eager_io, json_loads, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_eager_memoization_tg

- Geometric mean (including insignificant results): 1.019x slower
# HPT report

- Reliability score: 99.54% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.08x