# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.211x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x slower
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 244 ms: 1.30x slower                                                   |
| docutils       | 1.44 sec                                               | 1.69 sec: 1.17x slower                                                 |
| html5lib       | 36.6 ms                                                | 49.7 ms: 1.36x slower                                                  |
| sphinx         | 603 ms                                                 | 713 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                  | 1.25x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 262 ms: 1.10x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 472 ms: 1.09x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 454 ms: 1.05x faster                                                   |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.01x faster                                                   |
| async_tree_io                    | 507 ms                                                 | 520 ms: 1.03x slower                                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.04x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 205 ms: 1.04x slower                                                   |
| coroutines                       | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 228 ms: 1.06x slower                                                   |
| async_tree_memoization           | 268 ms                                                 | 284 ms: 1.06x slower                                                   |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 487 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 396 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 370 ms: 1.07x slower                                                   |
| async_generators                 | 295 ms                                                 | 316 ms: 1.07x slower                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 181 ms: 1.08x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.15x slower                                                   |
| async_tree_eager                 | 70.1 ms                                                | 101 ms: 1.44x slower                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 74.1 ms: 1.55x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pidigits       | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| float          | 56.0 ms                                                | 90.9 ms: 1.62x slower                                                  |
| nbody          | 74.0 ms                                                | 134 ms: 1.81x slower                                                   |
| Geometric mean | (ref)                                                  | 1.43x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.42 ms: 1.09x faster                                                  |
| regex_dna      | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| regex_v8       | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| regex_compile  | 78.6 ms                                                | 116 ms: 1.48x slower                                                   |
| Geometric mean | (ref)                                                  | 1.05x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 107 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 73.6 ms                                                | 74.6 ms: 1.01x slower                                                  |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| xml_etree_generate   | 57.0 ms                                                | 64.7 ms: 1.14x slower                                                  |
| tomli_loads          | 1.57 sec                                               | 1.88 sec: 1.20x slower                                                 |
| xml_etree_process    | 41.0 ms                                                | 52.9 ms: 1.29x slower                                                  |
| json_dumps           | 6.52 ms                                                | 8.58 ms: 1.32x slower                                                  |
| unpickle_pure_python | 164 us                                                 | 256 us: 1.56x slower                                                   |
| pickle_pure_python   | 214 us                                                 | 347 us: 1.62x slower                                                   |
| Geometric mean       | (ref)                                                  | 1.21x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 20.6 ms: 1.09x slower                                                  |
| python_startup_no_site | 14.5 ms                                                | 16.0 ms: 1.11x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 47.4 ms: 1.38x slower                                                  |
| genshi_text     | 16.9 ms                                                | 23.5 ms: 1.39x slower                                                  |
| django_template | 22.2 ms                                                | 34.8 ms: 1.56x slower                                                  |
| mako            | 7.68 ms                                                | 13.4 ms: 1.75x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.51x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| gc_traversal                     | 2.91 ms                                                | 2.51 ms: 1.16x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 262 ms: 1.10x faster                                                   |
| async_tree_eager_io              | 514 ms                                                 | 472 ms: 1.09x faster                                                   |
| create_gc_cycles                 | 1.17 ms                                                | 1.08 ms: 1.09x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.42 ms: 1.09x faster                                                  |
| xml_etree_parse                  | 107 ms                                                 | 98.6 ms: 1.09x faster                                                  |
| regex_dna                        | 149 ms                                                 | 138 ms: 1.08x faster                                                   |
| async_tree_eager_io_tg           | 477 ms                                                 | 454 ms: 1.05x faster                                                   |
| deepcopy                         | 237 us                                                 | 230 us: 1.03x faster                                                   |
| generators                       | 31.5 ms                                                | 30.6 ms: 1.03x faster                                                  |
| regex_v8                         | 17.0 ms                                                | 16.6 ms: 1.02x faster                                                  |
| asyncio_websockets               | 242 ms                                                 | 238 ms: 1.01x faster                                                   |
| pidigits                         | 284 ms                                                 | 281 ms: 1.01x faster                                                   |
| xml_etree_iterparse              | 73.6 ms                                                | 74.6 ms: 1.01x slower                                                  |
| async_tree_io                    | 507 ms                                                 | 520 ms: 1.03x slower                                                   |
| pathlib                          | 23.4 ms                                                | 24.1 ms: 1.03x slower                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 464 ms: 1.04x slower                                                   |
| async_tree_none_tg               | 198 ms                                                 | 205 ms: 1.04x slower                                                   |
| json                             | 3.03 ms                                                | 3.16 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                  |
| coroutines                       | 19.8 ms                                                | 20.8 ms: 1.05x slower                                                  |
| async_tree_none                  | 215 ms                                                 | 228 ms: 1.06x slower                                                   |
| async_tree_memoization           | 268 ms                                                 | 284 ms: 1.06x slower                                                   |
| deepcopy_memo                    | 27.4 us                                                | 29.0 us: 1.06x slower                                                  |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 487 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 396 ms: 1.06x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 370 ms: 1.07x slower                                                   |
| async_generators                 | 295 ms                                                 | 316 ms: 1.07x slower                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 181 ms: 1.08x slower                                                   |
| python_startup                   | 18.9 ms                                                | 20.6 ms: 1.09x slower                                                  |
| python_startup_no_site           | 14.5 ms                                                | 16.0 ms: 1.11x slower                                                  |
| telco                            | 4.76 ms                                                | 5.30 ms: 1.11x slower                                                  |
| shortest_path                    | 347 ms                                                 | 388 ms: 1.12x slower                                                   |
| deepcopy_reduce                  | 2.07 us                                                | 2.32 us: 1.12x slower                                                  |
| nqueens                          | 62.5 ms                                                | 70.4 ms: 1.13x slower                                                  |
| xml_etree_generate               | 57.0 ms                                                | 64.7 ms: 1.14x slower                                                  |
| connected_components             | 319 ms                                                 | 364 ms: 1.14x slower                                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 159 ms: 1.15x slower                                                   |
| k_core                           | 1.61 sec                                               | 1.86 sec: 1.16x slower                                                 |
| pylint                           | 180 ms                                                 | 209 ms: 1.16x slower                                                   |
| scimark_fft                      | 201 ms                                                 | 233 ms: 1.16x slower                                                   |
| bench_mp_pool                    | 62.5 ms                                                | 72.9 ms: 1.17x slower                                                  |
| docutils                         | 1.44 sec                                               | 1.69 sec: 1.17x slower                                                 |
| coverage                         | 46.0 ms                                                | 54.1 ms: 1.18x slower                                                  |
| fannkuch                         | 284 ms                                                 | 334 ms: 1.18x slower                                                   |
| sphinx                           | 603 ms                                                 | 713 ms: 1.18x slower                                                   |
| bpe_tokeniser                    | 3.25 sec                                               | 3.85 sec: 1.18x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 87.9 ms: 1.19x slower                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.88 sec: 1.20x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.80 sec: 1.21x slower                                                 |
| pycparser                        | 705 ms                                                 | 909 ms: 1.29x slower                                                   |
| xml_etree_process                | 41.0 ms                                                | 52.9 ms: 1.29x slower                                                  |
| 2to3                             | 187 ms                                                 | 244 ms: 1.30x slower                                                   |
| json_dumps                       | 6.52 ms                                                | 8.58 ms: 1.32x slower                                                  |
| pyflate                          | 351 ms                                                 | 464 ms: 1.32x slower                                                   |
| spectral_norm                    | 76.3 ms                                                | 102 ms: 1.33x slower                                                   |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 3.99 ms: 1.34x slower                                                  |
| html5lib                         | 36.6 ms                                                | 49.7 ms: 1.36x slower                                                  |
| genshi_xml                       | 34.4 ms                                                | 47.4 ms: 1.38x slower                                                  |
| sqlglot_normalize                | 189 ms                                                 | 262 ms: 1.38x slower                                                   |
| dulwich_log                      | 28.5 ms                                                | 39.6 ms: 1.39x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 140 us: 1.39x slower                                                   |
| genshi_text                      | 16.9 ms                                                | 23.5 ms: 1.39x slower                                                  |
| sympy_integrate                  | 11.3 ms                                                | 15.8 ms: 1.40x slower                                                  |
| thrift                           | 466 us                                                 | 656 us: 1.41x slower                                                   |
| sqlglot_optimize                 | 34.9 ms                                                | 49.7 ms: 1.42x slower                                                  |
| crypto_pyaes                     | 54.2 ms                                                | 77.6 ms: 1.43x slower                                                  |
| scimark_sor                      | 105 ms                                                 | 151 ms: 1.43x slower                                                   |
| async_tree_eager                 | 70.1 ms                                                | 101 ms: 1.44x slower                                                   |
| pprint_safe_repr                 | 533 ms                                                 | 784 ms: 1.47x slower                                                   |
| regex_compile                    | 78.6 ms                                                | 116 ms: 1.48x slower                                                   |
| pprint_pformat                   | 1.08 sec                                               | 1.60 sec: 1.48x slower                                                 |
| sqlalchemy_imperative            | 6.69 ms                                                | 9.97 ms: 1.49x slower                                                  |
| scimark_monte_carlo              | 50.4 ms                                                | 76.3 ms: 1.51x slower                                                  |
| richards                         | 35.2 ms                                                | 53.3 ms: 1.51x slower                                                  |
| sqlalchemy_declarative           | 58.9 ms                                                | 89.8 ms: 1.52x slower                                                  |
| go                               | 115 ms                                                 | 177 ms: 1.54x slower                                                   |
| async_tree_eager_tg              | 47.8 ms                                                | 74.1 ms: 1.55x slower                                                  |
| hexiom                           | 4.86 ms                                                | 7.55 ms: 1.55x slower                                                  |
| sympy_str                        | 145 ms                                                 | 226 ms: 1.56x slower                                                   |
| unpickle_pure_python             | 164 us                                                 | 256 us: 1.56x slower                                                   |
| django_template                  | 22.2 ms                                                | 34.8 ms: 1.56x slower                                                  |
| comprehensions                   | 12.3 us                                                | 19.2 us: 1.57x slower                                                  |
| richards_super                   | 39.1 ms                                                | 62.2 ms: 1.59x slower                                                  |
| bench_thread_pool                | 505 us                                                 | 811 us: 1.61x slower                                                   |
| pickle_pure_python               | 214 us                                                 | 347 us: 1.62x slower                                                   |
| float                            | 56.0 ms                                                | 90.9 ms: 1.62x slower                                                  |
| logging_simple                   | 3.60 us                                                | 5.89 us: 1.63x slower                                                  |
| logging_format                   | 3.89 us                                                | 6.44 us: 1.65x slower                                                  |
| chaos                            | 41.2 ms                                                | 69.6 ms: 1.69x slower                                                  |
| sympy_expand                     | 246 ms                                                 | 417 ms: 1.69x slower                                                   |
| mako                             | 7.68 ms                                                | 13.4 ms: 1.75x slower                                                  |
| sqlglot_transpile                | 1.02 ms                                                | 1.84 ms: 1.80x slower                                                  |
| nbody                            | 74.0 ms                                                | 134 ms: 1.81x slower                                                   |
| sympy_sum                        | 75.4 ms                                                | 137 ms: 1.82x slower                                                   |
| scimark_lu                       | 76.7 ms                                                | 141 ms: 1.84x slower                                                   |
| logging_silent                   | 70.1 ns                                                | 130 ns: 1.85x slower                                                   |
| sqlglot_parse                    | 856 us                                                 | 1.61 ms: 1.88x slower                                                  |
| raytrace                         | 181 ms                                                 | 340 ms: 1.88x slower                                                   |
| deltablue                        | 2.68 ms                                                | 5.45 ms: 2.04x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.27x slower                                                           |

Benchmark hidden because not significant (1): async_tree_io_tg
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-NOGIL/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.211x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.17x
- 95% likely to have a slowdown of 1.16x
- 99% likely to have a slowdown of 1.14x

# Memory
- memory change: 1.15x