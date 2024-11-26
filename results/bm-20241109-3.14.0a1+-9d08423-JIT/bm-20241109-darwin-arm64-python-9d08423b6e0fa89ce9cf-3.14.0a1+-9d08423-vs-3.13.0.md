# Results vs. 3.13.0

- fork: python
- ref: 9d08423b6e0fa89ce9cf
- machine: darwin-arm64
- commit hash: 9d08423
- commit date: 2024-11-09
- overall geometric mean: 1.020x faster
- HPT reliability: 90.15%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| docutils       | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                 |
| html5lib       | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                  |
| sphinx         | 603 ms                                                 | 675 ms: 1.12x slower                                                   |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization_tg       | 288 ms                                                 | 242 ms: 1.19x faster                                                   |
| coroutines                      | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| async_tree_eager_memoization    | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| async_tree_memoization          | 268 ms                                                 | 254 ms: 1.06x faster                                                   |
| async_tree_eager_tg             | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| async_tree_eager                | 70.1 ms                                                | 66.8 ms: 1.05x faster                                                  |
| async_tree_none                 | 215 ms                                                 | 206 ms: 1.04x faster                                                   |
| async_tree_eager_memoization_tg | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed   | 373 ms                                                 | 370 ms: 1.01x faster                                                   |
| async_tree_cpu_io_mixed         | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| async_generators                | 295 ms                                                 | 306 ms: 1.04x slower                                                   |
| async_tree_none_tg              | 198 ms                                                 | 207 ms: 1.05x slower                                                   |
| async_tree_cpu_io_mixed_tg      | 448 ms                                                 | 482 ms: 1.08x slower                                                   |
| async_tree_io                   | 507 ms                                                 | 592 ms: 1.17x slower                                                   |
| async_tree_io_tg                | 497 ms                                                 | 627 ms: 1.26x slower                                                   |
| async_tree_eager_io             | 514 ms                                                 | 685 ms: 1.33x slower                                                   |
| async_tree_eager_io_tg          | 477 ms                                                 | 729 ms: 1.53x slower                                                   |
| Geometric mean                  | (ref)                                                  | 1.04x slower                                                           |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed_tg, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                  |
| float          | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                  |
| regex_dna      | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| regex_compile  | 78.6 ms                                                | 76.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                 |
| xml_etree_process    | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                  |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.16x faster                                                   |
| xml_etree_generate   | 57.0 ms                                                | 49.5 ms: 1.15x faster                                                  |
| pickle_pure_python   | 214 us                                                 | 194 us: 1.11x faster                                                   |
| json_loads           | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| xml_etree_parse      | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| xml_etree_iterparse  | 73.6 ms                                                | 72.8 ms: 1.01x faster                                                  |
| json_dumps           | 6.52 ms                                                | 7.10 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 14.5 ms                                                | 14.0 ms: 1.04x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.68 ms                                                | 6.24 ms: 1.23x faster                                                  |
| genshi_text     | 16.9 ms                                                | 17.3 ms: 1.03x slower                                                  |
| django_template | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| genshi_xml      | 34.4 ms                                                | 39.7 ms: 1.15x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                           |

All benchmarks:
===============

| Benchmark                       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423 |
|---------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| deepcopy_memo                   | 27.4 us                                                | 17.6 us: 1.56x faster                                                  |
| deepcopy                        | 237 us                                                 | 157 us: 1.50x faster                                                   |
| deepcopy_reduce                 | 2.07 us                                                | 1.54 us: 1.35x faster                                                  |
| tomli_loads                     | 1.57 sec                                               | 1.25 sec: 1.25x faster                                                 |
| mako                            | 7.68 ms                                                | 6.24 ms: 1.23x faster                                                  |
| scimark_sor                     | 105 ms                                                 | 87.0 ms: 1.21x faster                                                  |
| async_tree_memoization_tg       | 288 ms                                                 | 242 ms: 1.19x faster                                                   |
| generators                      | 31.5 ms                                                | 26.9 ms: 1.17x faster                                                  |
| nbody                           | 74.0 ms                                                | 63.5 ms: 1.17x faster                                                  |
| xml_etree_process               | 41.0 ms                                                | 35.3 ms: 1.16x faster                                                  |
| unpickle_pure_python            | 164 us                                                 | 142 us: 1.16x faster                                                   |
| xml_etree_generate              | 57.0 ms                                                | 49.5 ms: 1.15x faster                                                  |
| float                           | 56.0 ms                                                | 48.8 ms: 1.15x faster                                                  |
| go                              | 115 ms                                                 | 101 ms: 1.14x faster                                                   |
| coroutines                      | 19.8 ms                                                | 17.5 ms: 1.13x faster                                                  |
| regex_effbot                    | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                  |
| scimark_monte_carlo             | 50.4 ms                                                | 45.0 ms: 1.12x faster                                                  |
| scimark_lu                      | 76.7 ms                                                | 68.7 ms: 1.12x faster                                                  |
| pickle_pure_python              | 214 us                                                 | 194 us: 1.11x faster                                                   |
| html5lib                        | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                  |
| fannkuch                        | 284 ms                                                 | 257 ms: 1.11x faster                                                   |
| logging_simple                  | 3.60 us                                                | 3.29 us: 1.09x faster                                                  |
| pprint_safe_repr                | 533 ms                                                 | 487 ms: 1.09x faster                                                   |
| spectral_norm                   | 76.3 ms                                                | 69.8 ms: 1.09x faster                                                  |
| bpe_tokeniser                   | 3.25 sec                                               | 2.98 sec: 1.09x faster                                                 |
| regex_dna                       | 149 ms                                                 | 137 ms: 1.09x faster                                                   |
| scimark_fft                     | 201 ms                                                 | 185 ms: 1.08x faster                                                   |
| logging_format                  | 3.89 us                                                | 3.61 us: 1.08x faster                                                  |
| pyflate                         | 351 ms                                                 | 327 ms: 1.08x faster                                                   |
| telco                           | 4.76 ms                                                | 4.43 ms: 1.08x faster                                                  |
| async_tree_eager_memoization    | 168 ms                                                 | 157 ms: 1.07x faster                                                   |
| connected_components            | 319 ms                                                 | 298 ms: 1.07x faster                                                   |
| regex_v8                        | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                  |
| pprint_pformat                  | 1.08 sec                                               | 1.02 sec: 1.07x faster                                                 |
| async_tree_memoization          | 268 ms                                                 | 254 ms: 1.06x faster                                                   |
| shortest_path                   | 347 ms                                                 | 329 ms: 1.06x faster                                                   |
| thrift                          | 466 us                                                 | 442 us: 1.05x faster                                                   |
| async_tree_eager_tg             | 47.8 ms                                                | 45.4 ms: 1.05x faster                                                  |
| async_tree_eager                | 70.1 ms                                                | 66.8 ms: 1.05x faster                                                  |
| async_tree_none                 | 215 ms                                                 | 206 ms: 1.04x faster                                                   |
| json                            | 3.03 ms                                                | 2.91 ms: 1.04x faster                                                  |
| pathlib                         | 23.4 ms                                                | 22.4 ms: 1.04x faster                                                  |
| pycparser                       | 705 ms                                                 | 680 ms: 1.04x faster                                                   |
| python_startup_no_site          | 14.5 ms                                                | 14.0 ms: 1.04x faster                                                  |
| richards                        | 35.2 ms                                                | 34.0 ms: 1.04x faster                                                  |
| richards_super                  | 39.1 ms                                                | 37.8 ms: 1.03x faster                                                  |
| bench_thread_pool               | 505 us                                                 | 488 us: 1.03x faster                                                   |
| async_tree_eager_memoization_tg | 138 ms                                                 | 134 ms: 1.03x faster                                                   |
| coverage                        | 46.0 ms                                                | 44.6 ms: 1.03x faster                                                  |
| regex_compile                   | 78.6 ms                                                | 76.7 ms: 1.03x faster                                                  |
| deltablue                       | 2.68 ms                                                | 2.61 ms: 1.02x faster                                                  |
| json_loads                      | 17.0 us                                                | 16.6 us: 1.02x faster                                                  |
| meteor_contest                  | 74.0 ms                                                | 72.8 ms: 1.02x faster                                                  |
| nqueens                         | 62.5 ms                                                | 61.7 ms: 1.01x faster                                                  |
| xml_etree_parse                 | 107 ms                                                 | 106 ms: 1.01x faster                                                   |
| xml_etree_iterparse             | 73.6 ms                                                | 72.8 ms: 1.01x faster                                                  |
| async_tree_eager_cpu_io_mixed   | 373 ms                                                 | 370 ms: 1.01x faster                                                   |
| sqlalchemy_imperative           | 6.69 ms                                                | 6.71 ms: 1.00x slower                                                  |
| crypto_pyaes                    | 54.2 ms                                                | 54.5 ms: 1.01x slower                                                  |
| gc_traversal                    | 2.91 ms                                                | 2.93 ms: 1.01x slower                                                  |
| dulwich_log                     | 28.5 ms                                                | 29.0 ms: 1.02x slower                                                  |
| raytrace                        | 181 ms                                                 | 184 ms: 1.02x slower                                                   |
| sqlglot_normalize               | 189 ms                                                 | 193 ms: 1.02x slower                                                   |
| scimark_sparse_mat_mult         | 2.99 ms                                                | 3.06 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed         | 460 ms                                                 | 472 ms: 1.03x slower                                                   |
| bench_mp_pool                   | 62.5 ms                                                | 64.2 ms: 1.03x slower                                                  |
| genshi_text                     | 16.9 ms                                                | 17.3 ms: 1.03x slower                                                  |
| sqlglot_parse                   | 856 us                                                 | 882 us: 1.03x slower                                                   |
| async_generators                | 295 ms                                                 | 306 ms: 1.04x slower                                                   |
| hexiom                          | 4.86 ms                                                | 5.05 ms: 1.04x slower                                                  |
| sympy_expand                    | 246 ms                                                 | 256 ms: 1.04x slower                                                   |
| async_tree_none_tg              | 198 ms                                                 | 207 ms: 1.05x slower                                                   |
| logging_silent                  | 70.1 ns                                                | 73.5 ns: 1.05x slower                                                  |
| chaos                           | 41.2 ms                                                | 43.5 ms: 1.05x slower                                                  |
| django_template                 | 22.2 ms                                                | 23.5 ms: 1.06x slower                                                  |
| sqlglot_transpile               | 1.02 ms                                                | 1.08 ms: 1.06x slower                                                  |
| mdp                             | 1.49 sec                                               | 1.58 sec: 1.06x slower                                                 |
| sympy_str                       | 145 ms                                                 | 155 ms: 1.06x slower                                                   |
| sqlalchemy_declarative          | 58.9 ms                                                | 63.2 ms: 1.07x slower                                                  |
| sympy_sum                       | 75.4 ms                                                | 80.9 ms: 1.07x slower                                                  |
| async_tree_cpu_io_mixed_tg      | 448 ms                                                 | 482 ms: 1.08x slower                                                   |
| json_dumps                      | 6.52 ms                                                | 7.10 ms: 1.09x slower                                                  |
| sqlglot_optimize                | 34.9 ms                                                | 38.1 ms: 1.09x slower                                                  |
| docutils                        | 1.44 sec                                               | 1.58 sec: 1.10x slower                                                 |
| comprehensions                  | 12.3 us                                                | 13.5 us: 1.10x slower                                                  |
| sphinx                          | 603 ms                                                 | 675 ms: 1.12x slower                                                   |
| create_gc_cycles                | 1.17 ms                                                | 1.32 ms: 1.13x slower                                                  |
| 2to3                            | 187 ms                                                 | 212 ms: 1.13x slower                                                   |
| sympy_integrate                 | 11.3 ms                                                | 12.8 ms: 1.13x slower                                                  |
| genshi_xml                      | 34.4 ms                                                | 39.7 ms: 1.15x slower                                                  |
| async_tree_io                   | 507 ms                                                 | 592 ms: 1.17x slower                                                   |
| async_tree_io_tg                | 497 ms                                                 | 627 ms: 1.26x slower                                                   |
| async_tree_eager_io             | 514 ms                                                 | 685 ms: 1.33x slower                                                   |
| k_core                          | 1.61 sec                                               | 2.24 sec: 1.39x slower                                                 |
| async_tree_eager_io_tg          | 477 ms                                                 | 729 ms: 1.53x slower                                                   |
| Geometric mean                  | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (6): typing_runtime_protocols, python_startup, async_tree_eager_cpu_io_mixed_tg, asyncio_websockets, pidigits, pylint
Ignored benchmarks (5) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241109-3.14.0a1+-9d08423-JIT/bm-20241109-darwin-arm64-python-9d08423b6e0fa89ce9cf-3.14.0a1+-9d08423.json: sqlite_synth

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 90.15% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.11x