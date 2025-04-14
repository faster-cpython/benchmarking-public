# Results vs. 3.13.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.019x faster
- HPT reliability: 95.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 170 ms: 1.05x faster                                                            |
| docutils       | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                          |
| html5lib       | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 386 ms: 1.32x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 384 ms: 1.30x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 399 ms: 1.27x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 391 ms: 1.23x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                            |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.15x faster                                                            |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 422 ms: 1.09x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 423 ms: 1.06x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.33x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 136 ms: 2.86x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.06x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 52.6 ms: 1.06x faster                                                           |
| nbody          | 73.6 ms                                                | 81.0 ms: 1.10x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                           |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                           |
| regex_dna      | 149 ms                                                 | 141 ms: 1.05x faster                                                            |
| regex_compile  | 78.3 ms                                                | 75.3 ms: 1.04x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 99.8 ms: 1.08x faster                                                           |
| xml_etree_generate   | 57.1 ms                                                | 56.0 ms: 1.02x faster                                                           |
| xml_etree_process    | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                           |
| xml_etree_iterparse  | 74.2 ms                                                | 73.8 ms: 1.01x faster                                                           |
| unpickle_pure_python | 165 us                                                 | 164 us: 1.01x faster                                                            |
| pickle_pure_python   | 215 us                                                 | 221 us: 1.03x slower                                                            |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| json_dumps           | 6.47 ms                                                | 7.50 ms: 1.16x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 17.8 ms: 1.05x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 13.7 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 15.3 ms: 1.11x faster                                                           |
| genshi_xml      | 34.1 ms                                                | 31.7 ms: 1.07x faster                                                           |
| mako            | 7.75 ms                                                | 7.96 ms: 1.03x slower                                                           |
| django_template | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 164 us: 1.44x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 204 ms: 1.41x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 20.4 us: 1.34x faster                                                           |
| async_tree_eager_io              | 511 ms                                                 | 386 ms: 1.32x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 384 ms: 1.30x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                            |
| generators                       | 31.9 ms                                                | 24.9 ms: 1.28x faster                                                           |
| async_tree_io                    | 508 ms                                                 | 399 ms: 1.27x faster                                                            |
| go                               | 117 ms                                                 | 92.7 ms: 1.26x faster                                                           |
| deepcopy_reduce                  | 2.09 us                                                | 1.70 us: 1.23x faster                                                           |
| async_tree_none                  | 212 ms                                                 | 172 ms: 1.23x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 391 ms: 1.23x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 164 ms: 1.21x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 88.3 ms: 1.20x faster                                                           |
| regex_effbot                     | 2.63 ms                                                | 2.27 ms: 1.16x faster                                                           |
| coroutines                       | 20.0 ms                                                | 17.3 ms: 1.16x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.15x faster                                                            |
| html5lib                         | 36.7 ms                                                | 32.3 ms: 1.14x faster                                                           |
| dulwich_log                      | 28.7 ms                                                | 25.6 ms: 1.12x faster                                                           |
| tomli_loads                      | 1.57 sec                                               | 1.40 sec: 1.12x faster                                                          |
| async_generators                 | 294 ms                                                 | 264 ms: 1.11x faster                                                            |
| genshi_text                      | 16.9 ms                                                | 15.3 ms: 1.11x faster                                                           |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 422 ms: 1.09x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 99.8 ms: 1.08x faster                                                           |
| genshi_xml                       | 34.1 ms                                                | 31.7 ms: 1.07x faster                                                           |
| pylint                           | 180 ms                                                 | 168 ms: 1.07x faster                                                            |
| pprint_pformat                   | 1.10 sec                                               | 1.03 sec: 1.07x faster                                                          |
| scimark_monte_carlo              | 50.4 ms                                                | 47.1 ms: 1.07x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 65.4 ms: 1.07x faster                                                           |
| pprint_safe_repr                 | 541 ms                                                 | 506 ms: 1.07x faster                                                            |
| bench_mp_pool                    | 64.7 ms                                                | 60.9 ms: 1.06x faster                                                           |
| float                            | 55.8 ms                                                | 52.6 ms: 1.06x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 423 ms: 1.06x faster                                                            |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.05x faster                                                            |
| python_startup                   | 18.8 ms                                                | 17.8 ms: 1.05x faster                                                           |
| 2to3                             | 179 ms                                                 | 170 ms: 1.05x faster                                                            |
| regex_compile                    | 78.3 ms                                                | 75.3 ms: 1.04x faster                                                           |
| telco                            | 4.84 ms                                                | 4.68 ms: 1.03x faster                                                           |
| scimark_fft                      | 200 ms                                                 | 193 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 362 ms: 1.03x faster                                                            |
| xml_etree_generate               | 57.1 ms                                                | 56.0 ms: 1.02x faster                                                           |
| k_core                           | 1.61 sec                                               | 1.58 sec: 1.02x faster                                                          |
| thrift                           | 466 us                                                 | 459 us: 1.01x faster                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                           |
| xml_etree_process                | 41.3 ms                                                | 40.9 ms: 1.01x faster                                                           |
| shortest_path                    | 345 ms                                                 | 343 ms: 1.01x faster                                                            |
| typing_runtime_protocols         | 101 us                                                 | 100.0 us: 1.01x faster                                                          |
| xml_etree_iterparse              | 74.2 ms                                                | 73.8 ms: 1.01x faster                                                           |
| unpickle_pure_python             | 165 us                                                 | 164 us: 1.01x faster                                                            |
| python_startup_no_site           | 13.7 ms                                                | 13.7 ms: 1.00x faster                                                           |
| connected_components             | 319 ms                                                 | 317 ms: 1.00x faster                                                            |
| pyflate                          | 352 ms                                                 | 351 ms: 1.00x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.65 ms: 1.00x slower                                                           |
| coverage                         | 46.2 ms                                                | 46.4 ms: 1.00x slower                                                           |
| bpe_tokeniser                    | 3.26 sec                                               | 3.30 sec: 1.01x slower                                                          |
| pathlib                          | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                           |
| sympy_str                        | 146 ms                                                 | 148 ms: 1.02x slower                                                            |
| logging_simple                   | 3.56 us                                                | 3.62 us: 1.02x slower                                                           |
| mdp                              | 1.50 sec                                               | 1.53 sec: 1.02x slower                                                          |
| hexiom                           | 4.87 ms                                                | 4.96 ms: 1.02x slower                                                           |
| logging_format                   | 3.85 us                                                | 3.94 us: 1.02x slower                                                           |
| mako                             | 7.75 ms                                                | 7.96 ms: 1.03x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.49 sec: 1.03x slower                                                          |
| richards                         | 36.2 ms                                                | 37.2 ms: 1.03x slower                                                           |
| sympy_sum                        | 75.1 ms                                                | 77.3 ms: 1.03x slower                                                           |
| pickle_pure_python               | 215 us                                                 | 221 us: 1.03x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 73.3 ns: 1.03x slower                                                           |
| meteor_contest                   | 74.0 ms                                                | 76.4 ms: 1.03x slower                                                           |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.92 ms: 1.03x slower                                                           |
| sqlalchemy_declarative           | 59.0 ms                                                | 61.0 ms: 1.03x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.09 ms: 1.04x slower                                                           |
| scimark_lu                       | 75.9 ms                                                | 79.2 ms: 1.04x slower                                                           |
| spectral_norm                    | 76.5 ms                                                | 79.9 ms: 1.05x slower                                                           |
| json                             | 3.04 ms                                                | 3.19 ms: 1.05x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| raytrace                         | 181 ms                                                 | 192 ms: 1.06x slower                                                            |
| richards_super                   | 39.2 ms                                                | 41.7 ms: 1.06x slower                                                           |
| sympy_integrate                  | 11.3 ms                                                | 12.1 ms: 1.07x slower                                                           |
| gc_traversal                     | 2.94 ms                                                | 3.14 ms: 1.07x slower                                                           |
| comprehensions                   | 12.0 us                                                | 12.9 us: 1.08x slower                                                           |
| chaos                            | 41.1 ms                                                | 44.5 ms: 1.08x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.29 ms: 1.08x slower                                                           |
| nbody                            | 73.6 ms                                                | 81.0 ms: 1.10x slower                                                           |
| crypto_pyaes                     | 55.3 ms                                                | 60.9 ms: 1.10x slower                                                           |
| fannkuch                         | 279 ms                                                 | 308 ms: 1.11x slower                                                            |
| nqueens                          | 61.8 ms                                                | 68.8 ms: 1.11x slower                                                           |
| django_template                  | 20.5 ms                                                | 22.8 ms: 1.11x slower                                                           |
| many_optionals                   | 409 us                                                 | 465 us: 1.14x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                            |
| json_dumps                       | 6.47 ms                                                | 7.50 ms: 1.16x slower                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 183 ms: 1.33x slower                                                            |
| subparsers                       | 9.44 ms                                                | 12.7 ms: 1.34x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 136 ms: 2.86x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (7): sphinx, pycparser, asyncio_websockets, sympy_expand, dask, pidigits, bench_thread_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.019x faster

# HPT report

- Reliability score: 95.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x