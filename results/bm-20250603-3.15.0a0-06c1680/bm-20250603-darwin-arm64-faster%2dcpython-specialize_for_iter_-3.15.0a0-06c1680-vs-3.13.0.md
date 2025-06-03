# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: darwin-arm64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.086x slower
- HPT reliability: 90.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 220 ms: 1.23x slower                                                            |
| docutils       | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                          |
| html5lib       | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                           |
| sphinx         | 602 ms                                                 | 612 ms: 1.02x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                            |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 185 ms: 1.15x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 436 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                            |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                           |
| async_tree_eager                 | 69.9 ms                                                | 73.4 ms: 1.05x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.34x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 59.3 ms: 1.06x slower                                                           |
| nbody          | 73.6 ms                                                | 85.1 ms: 1.16x slower                                                           |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.3 ms: 1.05x faster                                                           |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| regex_compile  | 78.3 ms                                                | 81.2 ms: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                          |
| xml_etree_parse      | 108 ms                                                 | 101 ms: 1.06x faster                                                            |
| json_loads           | 17.0 us                                                | 16.6 us: 1.03x faster                                                           |
| xml_etree_generate   | 57.1 ms                                                | 58.3 ms: 1.02x slower                                                           |
| xml_etree_process    | 41.3 ms                                                | 43.3 ms: 1.05x slower                                                           |
| json_dumps           | 6.47 ms                                                | 6.84 ms: 1.06x slower                                                           |
| unpickle_pure_python | 165 us                                                 | 179 us: 1.08x slower                                                            |
| pickle_pure_python   | 215 us                                                 | 241 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                           |
| python_startup_no_site | 13.7 ms                                                | 14.2 ms: 1.03x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                           |
| genshi_xml      | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                           |
| mako            | 7.75 ms                                                | 8.98 ms: 1.16x slower                                                           |
| django_template | 20.5 ms                                                | 25.0 ms: 1.22x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.12x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 828 ms: 1.81x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 209 ms: 1.38x faster                                                            |
| deepcopy                         | 236 us                                                 | 175 us: 1.35x faster                                                            |
| async_tree_eager_io              | 511 ms                                                 | 398 ms: 1.28x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 22.0 us: 1.24x faster                                                           |
| async_tree_memoization           | 268 ms                                                 | 216 ms: 1.24x faster                                                            |
| async_tree_io_tg                 | 500 ms                                                 | 408 ms: 1.23x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 417 ms: 1.22x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 406 ms: 1.18x faster                                                            |
| go                               | 117 ms                                                 | 100 ms: 1.16x faster                                                            |
| scimark_sor                      | 106 ms                                                 | 91.2 ms: 1.16x faster                                                           |
| async_tree_none_tg               | 198 ms                                                 | 172 ms: 1.15x faster                                                            |
| async_tree_none                  | 212 ms                                                 | 185 ms: 1.15x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.35 ms: 1.12x faster                                                           |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 153 ms: 1.10x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                          |
| dulwich_log                      | 28.7 ms                                                | 26.6 ms: 1.08x faster                                                           |
| html5lib                         | 36.7 ms                                                | 34.0 ms: 1.08x faster                                                           |
| async_generators                 | 294 ms                                                 | 275 ms: 1.07x faster                                                            |
| pylint                           | 180 ms                                                 | 169 ms: 1.07x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 101 ms: 1.06x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 436 ms: 1.05x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 426 ms: 1.05x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 16.3 ms: 1.05x faster                                                           |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                            |
| coroutines                       | 20.0 ms                                                | 19.3 ms: 1.04x faster                                                           |
| pyflate                          | 352 ms                                                 | 339 ms: 1.04x faster                                                            |
| k_core                           | 1.61 sec                                               | 1.55 sec: 1.04x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.6 us: 1.03x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 74.8 ms: 1.02x faster                                                           |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                                           |
| telco                            | 4.84 ms                                                | 4.78 ms: 1.01x faster                                                           |
| generators                       | 31.9 ms                                                | 31.6 ms: 1.01x faster                                                           |
| shortest_path                    | 345 ms                                                 | 342 ms: 1.01x faster                                                            |
| python_startup                   | 18.8 ms                                                | 18.7 ms: 1.01x faster                                                           |
| connected_components             | 319 ms                                                 | 317 ms: 1.01x faster                                                            |
| meteor_contest                   | 74.0 ms                                                | 74.9 ms: 1.01x slower                                                           |
| sphinx                           | 602 ms                                                 | 612 ms: 1.02x slower                                                            |
| xml_etree_generate               | 57.1 ms                                                | 58.3 ms: 1.02x slower                                                           |
| python_startup_no_site           | 13.7 ms                                                | 14.2 ms: 1.03x slower                                                           |
| pathlib                          | 23.2 ms                                                | 24.0 ms: 1.04x slower                                                           |
| regex_compile                    | 78.3 ms                                                | 81.2 ms: 1.04x slower                                                           |
| genshi_text                      | 16.9 ms                                                | 17.6 ms: 1.04x slower                                                           |
| scimark_fft                      | 200 ms                                                 | 208 ms: 1.04x slower                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.04x slower                                                           |
| hexiom                           | 4.87 ms                                                | 5.09 ms: 1.05x slower                                                           |
| richards                         | 36.2 ms                                                | 37.9 ms: 1.05x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.51 sec: 1.05x slower                                                          |
| xml_etree_process                | 41.3 ms                                                | 43.3 ms: 1.05x slower                                                           |
| async_tree_eager                 | 69.9 ms                                                | 73.4 ms: 1.05x slower                                                           |
| scimark_monte_carlo              | 50.4 ms                                                | 53.0 ms: 1.05x slower                                                           |
| sympy_expand                     | 248 ms                                                 | 260 ms: 1.05x slower                                                            |
| json_dumps                       | 6.47 ms                                                | 6.84 ms: 1.06x slower                                                           |
| genshi_xml                       | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                           |
| sympy_str                        | 146 ms                                                 | 155 ms: 1.06x slower                                                            |
| float                            | 55.8 ms                                                | 59.3 ms: 1.06x slower                                                           |
| pycparser                        | 701 ms                                                 | 745 ms: 1.06x slower                                                            |
| deltablue                        | 2.65 ms                                                | 2.81 ms: 1.06x slower                                                           |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.18 ms: 1.07x slower                                                           |
| richards_super                   | 39.2 ms                                                | 42.4 ms: 1.08x slower                                                           |
| unpickle_pure_python             | 165 us                                                 | 179 us: 1.08x slower                                                            |
| sympy_sum                        | 75.1 ms                                                | 81.5 ms: 1.09x slower                                                           |
| typing_runtime_protocols         | 101 us                                                 | 110 us: 1.09x slower                                                            |
| gc_traversal                     | 2.94 ms                                                | 3.23 ms: 1.10x slower                                                           |
| dask                             | 771 ms                                                 | 849 ms: 1.10x slower                                                            |
| crypto_pyaes                     | 55.3 ms                                                | 61.0 ms: 1.10x slower                                                           |
| comprehensions                   | 12.0 us                                                | 13.2 us: 1.11x slower                                                           |
| fannkuch                         | 279 ms                                                 | 310 ms: 1.11x slower                                                            |
| scimark_lu                       | 75.9 ms                                                | 84.7 ms: 1.12x slower                                                           |
| pickle_pure_python               | 215 us                                                 | 241 us: 1.12x slower                                                            |
| logging_format                   | 3.85 us                                                | 4.38 us: 1.14x slower                                                           |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                           |
| logging_simple                   | 3.56 us                                                | 4.06 us: 1.14x slower                                                           |
| pprint_pformat                   | 1.10 sec                                               | 1.26 sec: 1.15x slower                                                          |
| pprint_safe_repr                 | 541 ms                                                 | 621 ms: 1.15x slower                                                            |
| nqueens                          | 61.8 ms                                                | 71.1 ms: 1.15x slower                                                           |
| chaos                            | 41.1 ms                                                | 47.4 ms: 1.15x slower                                                           |
| nbody                            | 73.6 ms                                                | 85.1 ms: 1.16x slower                                                           |
| mako                             | 7.75 ms                                                | 8.98 ms: 1.16x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 403 ms: 1.16x slower                                                            |
| raytrace                         | 181 ms                                                 | 212 ms: 1.17x slower                                                            |
| django_template                  | 20.5 ms                                                | 25.0 ms: 1.22x slower                                                           |
| many_optionals                   | 409 us                                                 | 498 us: 1.22x slower                                                            |
| 2to3                             | 179 ms                                                 | 220 ms: 1.23x slower                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 184 ms: 1.34x slower                                                            |
| subparsers                       | 9.44 ms                                                | 15.1 ms: 1.60x slower                                                           |
| async_tree_eager_tg              | 47.4 ms                                                | 144 ms: 3.04x slower                                                            |
| logging_silent                   | 71.0 ns                                                | 347 ns: 4.88x slower                                                            |
| coverage                         | 46.2 ms                                                | 335 ms: 7.25x slower                                                            |
| thrift                           | 466 us                                                 | 44.1 ms: 94.68x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.11x slower                                                                    |

Benchmark hidden because not significant (6): bpe_tokeniser, async_tree_eager_cpu_io_mixed, pidigits, asyncio_websockets, sympy_integrate, xml_etree_iterparse
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-darwin-arm64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.086x slower

# HPT report

- Reliability score: 90.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x