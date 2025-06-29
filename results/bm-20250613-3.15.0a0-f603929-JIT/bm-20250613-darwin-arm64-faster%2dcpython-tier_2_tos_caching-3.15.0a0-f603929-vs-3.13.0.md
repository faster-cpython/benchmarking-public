# Results vs. 3.13.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.065x slower
- HPT reliability: 50.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 201 ms: 1.12x slower                                                          |
| docutils       | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                        |
| html5lib       | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                         |
| sphinx         | 602 ms                                                 | 616 ms: 1.02x slower                                                          |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 405 ms: 1.25x faster                                                          |
| async_tree_eager_io_tg           | 479 ms                                                 | 396 ms: 1.21x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.20x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.07x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 423 ms: 1.06x faster                                                          |
| coroutines                       | 20.0 ms                                                | 19.2 ms: 1.04x faster                                                         |
| async_generators                 | 294 ms                                                 | 287 ms: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                          |
| async_tree_eager                 | 69.9 ms                                                | 71.7 ms: 1.03x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.29x slower                                                          |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.95x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 58.2 ms: 1.04x slower                                                         |
| nbody          | 73.6 ms                                                | 78.6 ms: 1.07x slower                                                         |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                  |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                         |
| regex_v8       | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                         |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                          |
| regex_compile  | 78.3 ms                                                | 79.4 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 138 us: 1.20x faster                                                          |
| tomli_loads          | 1.57 sec                                               | 1.31 sec: 1.19x faster                                                        |
| xml_etree_generate   | 57.1 ms                                                | 52.0 ms: 1.10x faster                                                         |
| xml_etree_process    | 41.3 ms                                                | 37.9 ms: 1.09x faster                                                         |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                          |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                         |
| json_dumps           | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                         |
| pickle_pure_python   | 215 us                                                 | 227 us: 1.06x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 16.1 ms: 1.17x faster                                                         |
| python_startup_no_site | 13.7 ms                                                | 11.9 ms: 1.16x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 7.18 ms: 1.08x faster                                                         |
| genshi_text     | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                         |
| genshi_xml      | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                         |
| django_template | 20.5 ms                                                | 25.4 ms: 1.24x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 819 ms: 1.83x faster                                                          |
| async_tree_memoization_tg        | 288 ms                                                 | 202 ms: 1.42x faster                                                          |
| deepcopy                         | 236 us                                                 | 175 us: 1.35x faster                                                          |
| async_tree_eager_io              | 511 ms                                                 | 388 ms: 1.32x faster                                                          |
| async_tree_memoization           | 268 ms                                                 | 207 ms: 1.29x faster                                                          |
| async_tree_io_tg                 | 500 ms                                                 | 395 ms: 1.27x faster                                                          |
| async_tree_io                    | 508 ms                                                 | 405 ms: 1.25x faster                                                          |
| deepcopy_memo                    | 27.4 us                                                | 22.4 us: 1.23x faster                                                         |
| async_tree_eager_io_tg           | 479 ms                                                 | 396 ms: 1.21x faster                                                          |
| unpickle_pure_python             | 165 us                                                 | 138 us: 1.20x faster                                                          |
| async_tree_none_tg               | 198 ms                                                 | 166 ms: 1.20x faster                                                          |
| async_tree_none                  | 212 ms                                                 | 177 ms: 1.19x faster                                                          |
| tomli_loads                      | 1.57 sec                                               | 1.31 sec: 1.19x faster                                                        |
| python_startup                   | 18.8 ms                                                | 16.1 ms: 1.17x faster                                                         |
| go                               | 117 ms                                                 | 100 ms: 1.17x faster                                                          |
| scimark_sor                      | 106 ms                                                 | 90.9 ms: 1.16x faster                                                         |
| python_startup_no_site           | 13.7 ms                                                | 11.9 ms: 1.16x faster                                                         |
| regex_effbot                     | 2.63 ms                                                | 2.33 ms: 1.13x faster                                                         |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                          |
| k_core                           | 1.61 sec                                               | 1.45 sec: 1.11x faster                                                        |
| pyflate                          | 352 ms                                                 | 318 ms: 1.11x faster                                                          |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                         |
| xml_etree_generate               | 57.1 ms                                                | 52.0 ms: 1.10x faster                                                         |
| xml_etree_process                | 41.3 ms                                                | 37.9 ms: 1.09x faster                                                         |
| mako                             | 7.75 ms                                                | 7.18 ms: 1.08x faster                                                         |
| html5lib                         | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                         |
| telco                            | 4.84 ms                                                | 4.54 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 431 ms: 1.07x faster                                                          |
| pylint                           | 180 ms                                                 | 169 ms: 1.06x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 423 ms: 1.06x faster                                                          |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                          |
| regex_v8                         | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                         |
| dulwich_log                      | 28.7 ms                                                | 27.4 ms: 1.05x faster                                                         |
| bpe_tokeniser                    | 3.26 sec                                               | 3.11 sec: 1.05x faster                                                        |
| connected_components             | 319 ms                                                 | 305 ms: 1.05x faster                                                          |
| shortest_path                    | 345 ms                                                 | 332 ms: 1.04x faster                                                          |
| coroutines                       | 20.0 ms                                                | 19.2 ms: 1.04x faster                                                         |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                          |
| json                             | 3.04 ms                                                | 2.95 ms: 1.03x faster                                                         |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                         |
| spectral_norm                    | 76.5 ms                                                | 74.4 ms: 1.03x faster                                                         |
| async_generators                 | 294 ms                                                 | 287 ms: 1.02x faster                                                          |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                          |
| generators                       | 31.9 ms                                                | 31.7 ms: 1.01x faster                                                         |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                         |
| hexiom                           | 4.87 ms                                                | 4.84 ms: 1.01x faster                                                         |
| dask                             | 771 ms                                                 | 768 ms: 1.00x faster                                                          |
| crypto_pyaes                     | 55.3 ms                                                | 55.6 ms: 1.01x slower                                                         |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.01x slower                                                         |
| regex_compile                    | 78.3 ms                                                | 79.4 ms: 1.01x slower                                                         |
| scimark_fft                      | 200 ms                                                 | 204 ms: 1.02x slower                                                          |
| sphinx                           | 602 ms                                                 | 616 ms: 1.02x slower                                                          |
| sqlite_synth                     | 1.55 us                                                | 1.59 us: 1.02x slower                                                         |
| async_tree_eager                 | 69.9 ms                                                | 71.7 ms: 1.03x slower                                                         |
| richards                         | 36.2 ms                                                | 37.5 ms: 1.04x slower                                                         |
| float                            | 55.8 ms                                                | 58.2 ms: 1.04x slower                                                         |
| meteor_contest                   | 74.0 ms                                                | 77.1 ms: 1.04x slower                                                         |
| genshi_text                      | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                         |
| typing_runtime_protocols         | 101 us                                                 | 106 us: 1.05x slower                                                          |
| docutils                         | 1.44 sec                                               | 1.52 sec: 1.05x slower                                                        |
| json_dumps                       | 6.47 ms                                                | 6.82 ms: 1.05x slower                                                         |
| pickle_pure_python               | 215 us                                                 | 227 us: 1.06x slower                                                          |
| pathlib                          | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                         |
| sympy_str                        | 146 ms                                                 | 155 ms: 1.06x slower                                                          |
| genshi_xml                       | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                         |
| scimark_monte_carlo              | 50.4 ms                                                | 53.7 ms: 1.06x slower                                                         |
| sympy_expand                     | 248 ms                                                 | 265 ms: 1.07x slower                                                          |
| nbody                            | 73.6 ms                                                | 78.6 ms: 1.07x slower                                                         |
| richards_super                   | 39.2 ms                                                | 42.0 ms: 1.07x slower                                                         |
| pycparser                        | 701 ms                                                 | 752 ms: 1.07x slower                                                          |
| sympy_sum                        | 75.1 ms                                                | 81.2 ms: 1.08x slower                                                         |
| deltablue                        | 2.65 ms                                                | 2.88 ms: 1.09x slower                                                         |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                         |
| comprehensions                   | 12.0 us                                                | 13.2 us: 1.11x slower                                                         |
| scimark_lu                       | 75.9 ms                                                | 84.3 ms: 1.11x slower                                                         |
| nqueens                          | 61.8 ms                                                | 69.4 ms: 1.12x slower                                                         |
| 2to3                             | 179 ms                                                 | 201 ms: 1.12x slower                                                          |
| pprint_pformat                   | 1.10 sec                                               | 1.24 sec: 1.12x slower                                                        |
| fannkuch                         | 279 ms                                                 | 316 ms: 1.13x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 614 ms: 1.14x slower                                                          |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                         |
| logging_format                   | 3.85 us                                                | 4.40 us: 1.14x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                          |
| logging_simple                   | 3.56 us                                                | 4.10 us: 1.15x slower                                                         |
| raytrace                         | 181 ms                                                 | 211 ms: 1.16x slower                                                          |
| chaos                            | 41.1 ms                                                | 47.9 ms: 1.17x slower                                                         |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.64 ms: 1.22x slower                                                         |
| django_template                  | 20.5 ms                                                | 25.4 ms: 1.24x slower                                                         |
| many_optionals                   | 409 us                                                 | 510 us: 1.25x slower                                                          |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 179 ms: 1.29x slower                                                          |
| subparsers                       | 9.44 ms                                                | 15.0 ms: 1.59x slower                                                         |
| async_tree_eager_tg              | 47.4 ms                                                | 140 ms: 2.95x slower                                                          |
| logging_silent                   | 71.0 ns                                                | 346 ns: 4.87x slower                                                          |
| coverage                         | 46.2 ms                                                | 341 ms: 7.38x slower                                                          |
| thrift                           | 466 us                                                 | 43.8 ms: 94.05x slower                                                        |
| Geometric mean                   | (ref)                                                  | 1.08x slower                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.065x slower

# HPT report

- Reliability score: 50.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x