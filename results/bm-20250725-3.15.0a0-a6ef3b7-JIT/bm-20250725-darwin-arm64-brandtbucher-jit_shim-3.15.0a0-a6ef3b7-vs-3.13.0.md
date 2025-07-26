# Results vs. 3.13.0

- fork: brandtbucher
- ref: jit_shim
- machine: darwin-arm64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.060x slower
- HPT reliability: 99.43%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 202 ms: 1.13x slower                                            |
| docutils       | 1.44 sec                                               | 1.82 sec: 1.26x slower                                          |
| html5lib       | 36.7 ms                                                | 38.1 ms: 1.04x slower                                           |
| sphinx         | 602 ms                                                 | 690 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                  | 1.14x slower                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 219 ms: 1.31x faster                                            |
| async_tree_eager_io              | 511 ms                                                 | 418 ms: 1.22x faster                                            |
| async_tree_memoization           | 268 ms                                                 | 224 ms: 1.20x faster                                            |
| async_tree_io                    | 508 ms                                                 | 433 ms: 1.17x faster                                            |
| async_tree_io_tg                 | 500 ms                                                 | 431 ms: 1.16x faster                                            |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 432 ms: 1.11x faster                                            |
| async_tree_none_tg               | 198 ms                                                 | 181 ms: 1.10x faster                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 466 ms: 1.01x slower                                            |
| async_tree_eager                 | 69.9 ms                                                | 71.4 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                            |
| async_generators                 | 294 ms                                                 | 316 ms: 1.08x slower                                            |
| asyncio_websockets               | 242 ms                                                 | 273 ms: 1.12x slower                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 435 ms: 1.25x slower                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 198 ms: 1.43x slower                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 148 ms: 3.13x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.03x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| nbody          | 73.6 ms                                                | 78.9 ms: 1.07x slower                                           |
| pidigits       | 284 ms                                                 | 310 ms: 1.09x slower                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                    |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.35 ms: 1.12x faster                                           |
| regex_dna      | 149 ms                                                 | 152 ms: 1.02x slower                                            |
| regex_compile  | 78.3 ms                                                | 82.1 ms: 1.05x slower                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                    |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 143 us: 1.15x faster                                            |
| tomli_loads          | 1.57 sec                                               | 1.39 sec: 1.13x faster                                          |
| xml_etree_process    | 41.3 ms                                                | 39.3 ms: 1.05x faster                                           |
| xml_etree_generate   | 57.1 ms                                                | 56.0 ms: 1.02x faster                                           |
| xml_etree_parse      | 108 ms                                                 | 110 ms: 1.02x slower                                            |
| pickle_pure_python   | 215 us                                                 | 233 us: 1.08x slower                                            |
| xml_etree_iterparse  | 74.2 ms                                                | 82.3 ms: 1.11x slower                                           |
| json_dumps           | 6.47 ms                                                | 7.25 ms: 1.12x slower                                           |
| json_loads           | 17.0 us                                                | 19.2 us: 1.13x slower                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.5 ms: 1.01x faster                                           |
| python_startup_no_site | 13.7 ms                                                | 14.0 ms: 1.02x slower                                           |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 7.15 ms: 1.08x faster                                           |
| genshi_text     | 16.9 ms                                                | 16.6 ms: 1.02x faster                                           |
| genshi_xml      | 34.1 ms                                                | 36.3 ms: 1.07x slower                                           |
| django_template | 20.5 ms                                                | 25.7 ms: 1.25x slower                                           |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 925 ms: 1.62x faster                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 219 ms: 1.31x faster                                            |
| deepcopy                         | 236 us                                                 | 190 us: 1.24x faster                                            |
| async_tree_eager_io              | 511 ms                                                 | 418 ms: 1.22x faster                                            |
| go                               | 117 ms                                                 | 95.8 ms: 1.22x faster                                           |
| async_tree_memoization           | 268 ms                                                 | 224 ms: 1.20x faster                                            |
| generators                       | 31.9 ms                                                | 26.8 ms: 1.19x faster                                           |
| async_tree_io                    | 508 ms                                                 | 433 ms: 1.17x faster                                            |
| deepcopy_memo                    | 27.4 us                                                | 23.5 us: 1.16x faster                                           |
| async_tree_io_tg                 | 500 ms                                                 | 431 ms: 1.16x faster                                            |
| unpickle_pure_python             | 165 us                                                 | 143 us: 1.15x faster                                            |
| scimark_sor                      | 106 ms                                                 | 92.0 ms: 1.15x faster                                           |
| async_tree_none                  | 212 ms                                                 | 186 ms: 1.14x faster                                            |
| tomli_loads                      | 1.57 sec                                               | 1.39 sec: 1.13x faster                                          |
| regex_effbot                     | 2.63 ms                                                | 2.35 ms: 1.12x faster                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 151 ms: 1.11x faster                                            |
| spectral_norm                    | 76.5 ms                                                | 68.8 ms: 1.11x faster                                           |
| coroutines                       | 20.0 ms                                                | 18.0 ms: 1.11x faster                                           |
| async_tree_eager_io_tg           | 479 ms                                                 | 432 ms: 1.11x faster                                            |
| async_tree_none_tg               | 198 ms                                                 | 181 ms: 1.10x faster                                            |
| pprint_pformat                   | 1.10 sec                                               | 1.01 sec: 1.09x faster                                          |
| pprint_safe_repr                 | 541 ms                                                 | 498 ms: 1.08x faster                                            |
| mako                             | 7.75 ms                                                | 7.15 ms: 1.08x faster                                           |
| deepcopy_reduce                  | 2.09 us                                                | 1.96 us: 1.07x faster                                           |
| xml_etree_process                | 41.3 ms                                                | 39.3 ms: 1.05x faster                                           |
| pyflate                          | 352 ms                                                 | 342 ms: 1.03x faster                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 49.1 ms: 1.03x faster                                           |
| xml_etree_generate               | 57.1 ms                                                | 56.0 ms: 1.02x faster                                           |
| genshi_text                      | 16.9 ms                                                | 16.6 ms: 1.02x faster                                           |
| fannkuch                         | 279 ms                                                 | 274 ms: 1.02x faster                                            |
| python_startup                   | 18.8 ms                                                | 18.5 ms: 1.01x faster                                           |
| richards                         | 36.2 ms                                                | 36.7 ms: 1.01x slower                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 466 ms: 1.01x slower                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 3.32 sec: 1.02x slower                                          |
| regex_dna                        | 149 ms                                                 | 152 ms: 1.02x slower                                            |
| dask                             | 771 ms                                                 | 787 ms: 1.02x slower                                            |
| xml_etree_parse                  | 108 ms                                                 | 110 ms: 1.02x slower                                            |
| async_tree_eager                 | 69.9 ms                                                | 71.4 ms: 1.02x slower                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                            |
| python_startup_no_site           | 13.7 ms                                                | 14.0 ms: 1.02x slower                                           |
| html5lib                         | 36.7 ms                                                | 38.1 ms: 1.04x slower                                           |
| chaos                            | 41.1 ms                                                | 42.7 ms: 1.04x slower                                           |
| comprehensions                   | 12.0 us                                                | 12.5 us: 1.04x slower                                           |
| typing_runtime_protocols         | 101 us                                                 | 105 us: 1.04x slower                                            |
| scimark_fft                      | 200 ms                                                 | 208 ms: 1.04x slower                                            |
| richards_super                   | 39.2 ms                                                | 41.0 ms: 1.05x slower                                           |
| dulwich_log                      | 28.7 ms                                                | 30.1 ms: 1.05x slower                                           |
| regex_compile                    | 78.3 ms                                                | 82.1 ms: 1.05x slower                                           |
| logging_simple                   | 3.56 us                                                | 3.73 us: 1.05x slower                                           |
| logging_format                   | 3.85 us                                                | 4.06 us: 1.05x slower                                           |
| deltablue                        | 2.65 ms                                                | 2.79 ms: 1.05x slower                                           |
| hexiom                           | 4.87 ms                                                | 5.14 ms: 1.06x slower                                           |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 394 ms: 1.06x slower                                            |
| genshi_xml                       | 34.1 ms                                                | 36.3 ms: 1.07x slower                                           |
| raytrace                         | 181 ms                                                 | 193 ms: 1.07x slower                                            |
| scimark_lu                       | 75.9 ms                                                | 81.2 ms: 1.07x slower                                           |
| nbody                            | 73.6 ms                                                | 78.9 ms: 1.07x slower                                           |
| async_generators                 | 294 ms                                                 | 316 ms: 1.08x slower                                            |
| pathlib                          | 23.2 ms                                                | 25.1 ms: 1.08x slower                                           |
| pickle_pure_python               | 215 us                                                 | 233 us: 1.08x slower                                            |
| nqueens                          | 61.8 ms                                                | 67.1 ms: 1.08x slower                                           |
| pylint                           | 180 ms                                                 | 196 ms: 1.09x slower                                            |
| thrift                           | 466 us                                                 | 508 us: 1.09x slower                                            |
| pidigits                         | 284 ms                                                 | 310 ms: 1.09x slower                                            |
| xml_etree_iterparse              | 74.2 ms                                                | 82.3 ms: 1.11x slower                                           |
| coverage                         | 46.2 ms                                                | 51.3 ms: 1.11x slower                                           |
| json                             | 3.04 ms                                                | 3.40 ms: 1.12x slower                                           |
| json_dumps                       | 6.47 ms                                                | 7.25 ms: 1.12x slower                                           |
| asyncio_websockets               | 242 ms                                                 | 273 ms: 1.12x slower                                            |
| sqlite_synth                     | 1.55 us                                                | 1.75 us: 1.12x slower                                           |
| json_loads                       | 17.0 us                                                | 19.2 us: 1.13x slower                                           |
| meteor_contest                   | 74.0 ms                                                | 83.5 ms: 1.13x slower                                           |
| 2to3                             | 179 ms                                                 | 202 ms: 1.13x slower                                            |
| logging_silent                   | 71.0 ns                                                | 80.3 ns: 1.13x slower                                           |
| sphinx                           | 602 ms                                                 | 690 ms: 1.15x slower                                            |
| sympy_expand                     | 248 ms                                                 | 285 ms: 1.15x slower                                            |
| sympy_str                        | 146 ms                                                 | 172 ms: 1.18x slower                                            |
| sympy_integrate                  | 11.3 ms                                                | 13.5 ms: 1.19x slower                                           |
| sympy_sum                        | 75.1 ms                                                | 91.1 ms: 1.21x slower                                           |
| pycparser                        | 701 ms                                                 | 856 ms: 1.22x slower                                            |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.72 ms: 1.25x slower                                           |
| django_template                  | 20.5 ms                                                | 25.7 ms: 1.25x slower                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 435 ms: 1.25x slower                                            |
| docutils                         | 1.44 sec                                               | 1.82 sec: 1.26x slower                                          |
| shortest_path                    | 345 ms                                                 | 452 ms: 1.31x slower                                            |
| connected_components             | 319 ms                                                 | 419 ms: 1.31x slower                                            |
| k_core                           | 1.61 sec                                               | 2.18 sec: 1.35x slower                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 198 ms: 1.43x slower                                            |
| gc_traversal                     | 2.94 ms                                                | 4.62 ms: 1.57x slower                                           |
| many_optionals                   | 409 us                                                 | 713 us: 1.74x slower                                            |
| create_gc_cycles                 | 1.19 ms                                                | 2.14 ms: 1.79x slower                                           |
| subparsers                       | 9.44 ms                                                | 29.3 ms: 3.11x slower                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 148 ms: 3.13x slower                                            |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                    |

Benchmark hidden because not significant (4): float, regex_v8, telco, crypto_pyaes
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.060x slower

# HPT report

- Reliability score: 99.43% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.17x