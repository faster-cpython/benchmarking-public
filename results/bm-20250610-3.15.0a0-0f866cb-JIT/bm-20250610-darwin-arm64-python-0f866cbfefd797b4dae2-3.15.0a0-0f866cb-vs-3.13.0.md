# Results vs. 3.13.0

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: darwin-arm64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.003x slower
- HPT reliability: 51.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 185 ms: 1.04x slower                                                  |
| docutils       | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| html5lib       | 36.7 ms                                                | 34.1 ms: 1.08x faster                                                 |
| sphinx         | 602 ms                                                 | 617 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 387 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 406 ms: 1.25x faster                                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 427 ms: 1.08x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.2 ms: 1.04x faster                                                 |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| async_tree_eager                 | 69.9 ms                                                | 71.7 ms: 1.02x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                  |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                 |
| nbody          | 73.6 ms                                                | 76.6 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| regex_v8       | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                 |
| regex_dna      | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| regex_compile  | 78.3 ms                                                | 79.7 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 165 us                                                 | 138 us: 1.20x faster                                                  |
| tomli_loads          | 1.57 sec                                               | 1.34 sec: 1.17x faster                                                |
| xml_etree_generate   | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                 |
| xml_etree_process    | 41.3 ms                                                | 37.7 ms: 1.10x faster                                                 |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| xml_etree_iterparse  | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| pickle_pure_python   | 215 us                                                 | 226 us: 1.05x slower                                                  |
| json_dumps           | 6.47 ms                                                | 6.86 ms: 1.06x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 20.2 ms: 1.08x slower                                                 |
| python_startup_no_site | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 7.75 ms                                                | 6.94 ms: 1.12x faster                                                 |
| genshi_text     | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                 |
| genshi_xml      | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| django_template | 20.5 ms                                                | 25.3 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                              | 1.50 sec                                               | 826 ms: 1.82x faster                                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 203 ms: 1.41x faster                                                  |
| deepcopy                         | 236 us                                                 | 174 us: 1.35x faster                                                  |
| async_tree_eager_io              | 511 ms                                                 | 387 ms: 1.32x faster                                                  |
| async_tree_memoization           | 268 ms                                                 | 208 ms: 1.29x faster                                                  |
| async_tree_io_tg                 | 500 ms                                                 | 397 ms: 1.26x faster                                                  |
| async_tree_io                    | 508 ms                                                 | 406 ms: 1.25x faster                                                  |
| deepcopy_memo                    | 27.4 us                                                | 22.3 us: 1.23x faster                                                 |
| async_tree_eager_io_tg           | 479 ms                                                 | 397 ms: 1.21x faster                                                  |
| unpickle_pure_python             | 165 us                                                 | 138 us: 1.20x faster                                                  |
| async_tree_none_tg               | 198 ms                                                 | 167 ms: 1.19x faster                                                  |
| async_tree_none                  | 212 ms                                                 | 178 ms: 1.19x faster                                                  |
| tomli_loads                      | 1.57 sec                                               | 1.34 sec: 1.17x faster                                                |
| scimark_sor                      | 106 ms                                                 | 90.6 ms: 1.17x faster                                                 |
| go                               | 117 ms                                                 | 100 ms: 1.17x faster                                                  |
| regex_effbot                     | 2.63 ms                                                | 2.34 ms: 1.12x faster                                                 |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| mako                             | 7.75 ms                                                | 6.94 ms: 1.12x faster                                                 |
| deepcopy_reduce                  | 2.09 us                                                | 1.90 us: 1.10x faster                                                 |
| xml_etree_generate               | 57.1 ms                                                | 51.9 ms: 1.10x faster                                                 |
| pyflate                          | 352 ms                                                 | 321 ms: 1.10x faster                                                  |
| xml_etree_process                | 41.3 ms                                                | 37.7 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 427 ms: 1.08x faster                                                  |
| html5lib                         | 36.7 ms                                                | 34.1 ms: 1.08x faster                                                 |
| dulwich_log                      | 28.7 ms                                                | 26.7 ms: 1.07x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 422 ms: 1.06x faster                                                  |
| pylint                           | 180 ms                                                 | 170 ms: 1.06x faster                                                  |
| telco                            | 4.84 ms                                                | 4.57 ms: 1.06x faster                                                 |
| k_core                           | 1.61 sec                                               | 1.53 sec: 1.06x faster                                                |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                  |
| bpe_tokeniser                    | 3.26 sec                                               | 3.10 sec: 1.05x faster                                                |
| regex_v8                         | 17.0 ms                                                | 16.2 ms: 1.05x faster                                                 |
| regex_dna                        | 149 ms                                                 | 143 ms: 1.04x faster                                                  |
| coroutines                       | 20.0 ms                                                | 19.2 ms: 1.04x faster                                                 |
| json                             | 3.04 ms                                                | 2.93 ms: 1.04x faster                                                 |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                 |
| spectral_norm                    | 76.5 ms                                                | 74.3 ms: 1.03x faster                                                 |
| connected_components             | 319 ms                                                 | 310 ms: 1.03x faster                                                  |
| async_generators                 | 294 ms                                                 | 286 ms: 1.03x faster                                                  |
| shortest_path                    | 345 ms                                                 | 339 ms: 1.02x faster                                                  |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 368 ms: 1.01x faster                                                  |
| pathlib                          | 23.2 ms                                                | 22.9 ms: 1.01x faster                                                 |
| xml_etree_iterparse              | 74.2 ms                                                | 73.7 ms: 1.01x faster                                                 |
| generators                       | 31.9 ms                                                | 31.7 ms: 1.01x faster                                                 |
| sympy_integrate                  | 11.3 ms                                                | 11.4 ms: 1.01x slower                                                 |
| thrift                           | 466 us                                                 | 472 us: 1.01x slower                                                  |
| regex_compile                    | 78.3 ms                                                | 79.7 ms: 1.02x slower                                                 |
| sphinx                           | 602 ms                                                 | 617 ms: 1.02x slower                                                  |
| async_tree_eager                 | 69.9 ms                                                | 71.7 ms: 1.02x slower                                                 |
| hexiom                           | 4.87 ms                                                | 5.01 ms: 1.03x slower                                                 |
| scimark_fft                      | 200 ms                                                 | 206 ms: 1.03x slower                                                  |
| typing_runtime_protocols         | 101 us                                                 | 104 us: 1.04x slower                                                  |
| 2to3                             | 179 ms                                                 | 185 ms: 1.04x slower                                                  |
| float                            | 55.8 ms                                                | 57.9 ms: 1.04x slower                                                 |
| richards                         | 36.2 ms                                                | 37.6 ms: 1.04x slower                                                 |
| meteor_contest                   | 74.0 ms                                                | 77.0 ms: 1.04x slower                                                 |
| sqlite_synth                     | 1.55 us                                                | 1.62 us: 1.04x slower                                                 |
| nbody                            | 73.6 ms                                                | 76.6 ms: 1.04x slower                                                 |
| genshi_text                      | 16.9 ms                                                | 17.7 ms: 1.04x slower                                                 |
| crypto_pyaes                     | 55.3 ms                                                | 58.0 ms: 1.05x slower                                                 |
| pickle_pure_python               | 215 us                                                 | 226 us: 1.05x slower                                                  |
| json_dumps                       | 6.47 ms                                                | 6.86 ms: 1.06x slower                                                 |
| scimark_monte_carlo              | 50.4 ms                                                | 53.5 ms: 1.06x slower                                                 |
| genshi_xml                       | 34.1 ms                                                | 36.2 ms: 1.06x slower                                                 |
| sympy_str                        | 146 ms                                                 | 155 ms: 1.06x slower                                                  |
| sympy_expand                     | 248 ms                                                 | 265 ms: 1.07x slower                                                  |
| coverage                         | 46.2 ms                                                | 49.6 ms: 1.07x slower                                                 |
| pycparser                        | 701 ms                                                 | 753 ms: 1.07x slower                                                  |
| richards_super                   | 39.2 ms                                                | 42.2 ms: 1.07x slower                                                 |
| python_startup                   | 18.8 ms                                                | 20.2 ms: 1.08x slower                                                 |
| sympy_sum                        | 75.1 ms                                                | 80.9 ms: 1.08x slower                                                 |
| fannkuch                         | 279 ms                                                 | 302 ms: 1.08x slower                                                  |
| pprint_safe_repr                 | 541 ms                                                 | 585 ms: 1.08x slower                                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.20 sec: 1.09x slower                                                |
| docutils                         | 1.44 sec                                               | 1.57 sec: 1.09x slower                                                |
| gc_traversal                     | 2.94 ms                                                | 3.20 ms: 1.09x slower                                                 |
| deltablue                        | 2.65 ms                                                | 2.89 ms: 1.09x slower                                                 |
| comprehensions                   | 12.0 us                                                | 13.1 us: 1.10x slower                                                 |
| scimark_lu                       | 75.9 ms                                                | 84.3 ms: 1.11x slower                                                 |
| nqueens                          | 61.8 ms                                                | 69.4 ms: 1.12x slower                                                 |
| python_startup_no_site           | 13.7 ms                                                | 15.6 ms: 1.14x slower                                                 |
| create_gc_cycles                 | 1.19 ms                                                | 1.36 ms: 1.14x slower                                                 |
| logging_format                   | 3.85 us                                                | 4.40 us: 1.14x slower                                                 |
| logging_simple                   | 3.56 us                                                | 4.10 us: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 400 ms: 1.15x slower                                                  |
| raytrace                         | 181 ms                                                 | 211 ms: 1.16x slower                                                  |
| chaos                            | 41.1 ms                                                | 47.9 ms: 1.17x slower                                                 |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.56 ms: 1.19x slower                                                 |
| django_template                  | 20.5 ms                                                | 25.3 ms: 1.23x slower                                                 |
| many_optionals                   | 409 us                                                 | 508 us: 1.24x slower                                                  |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 180 ms: 1.30x slower                                                  |
| subparsers                       | 9.44 ms                                                | 15.0 ms: 1.58x slower                                                 |
| async_tree_eager_tg              | 47.4 ms                                                | 141 ms: 2.97x slower                                                  |
| logging_silent                   | 71.0 ns                                                | 344 ns: 4.84x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.02x slower                                                          |

Benchmark hidden because not significant (3): asyncio_websockets, pidigits, dask
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.003x slower

# HPT report

- Reliability score: 51.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x