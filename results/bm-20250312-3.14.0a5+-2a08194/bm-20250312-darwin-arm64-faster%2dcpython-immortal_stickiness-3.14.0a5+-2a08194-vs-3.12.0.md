# Results vs. 3.12.0

- fork: faster-cpython
- ref: immortal_stickiness
- machine: darwin-arm64
- commit hash: 2a08194
- commit date: 2025-03-12
- overall geometric mean: 1.018x faster
- HPT reliability: 73.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 170 ms: 1.01x slower                                                            |
| docutils       | 1.45 sec                                               | 1.49 sec: 1.02x slower                                                          |
| html5lib       | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                           |
| sphinx         | 613 ms                                                 | 596 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 384 ms: 1.75x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 386 ms: 1.72x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 399 ms: 1.68x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 391 ms: 1.58x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.56x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 422 ms: 1.25x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                            |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                           |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 362 ms: 1.03x faster                                                            |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 136 ms: 2.89x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.18x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 52.6 ms: 1.03x faster                                                           |
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| nbody          | 67.6 ms                                                | 81.0 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| regex_compile  | 75.9 ms                                                | 75.3 ms: 1.01x faster                                                           |
| regex_v8       | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                           |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 99.8 ms: 1.08x faster                                                           |
| xml_etree_iterparse  | 75.5 ms                                                | 73.8 ms: 1.02x faster                                                           |
| xml_etree_generate   | 55.4 ms                                                | 56.0 ms: 1.01x slower                                                           |
| tomli_loads          | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                          |
| xml_etree_process    | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                           |
| json_loads           | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                            |
| unpickle_pure_python | 145 us                                                 | 164 us: 1.13x slower                                                            |
| json_dumps           | 6.19 ms                                                | 7.50 ms: 1.21x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.05x slower                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                                    |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 31.7 ms: 1.04x slower                                                           |
| genshi_text     | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                           |
| mako            | 7.44 ms                                                | 7.96 ms: 1.07x slower                                                           |
| django_template | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.7 ms: 2.53x faster                                                           |
| async_tree_io_tg                 | 673 ms                                                 | 384 ms: 1.75x faster                                                            |
| async_tree_eager_io              | 666 ms                                                 | 386 ms: 1.72x faster                                                            |
| async_tree_io                    | 672 ms                                                 | 399 ms: 1.68x faster                                                            |
| async_tree_eager_io_tg           | 617 ms                                                 | 391 ms: 1.58x faster                                                            |
| async_tree_none_tg               | 255 ms                                                 | 164 ms: 1.56x faster                                                            |
| async_tree_memoization_tg        | 318 ms                                                 | 204 ms: 1.56x faster                                                            |
| async_tree_none                  | 263 ms                                                 | 172 ms: 1.53x faster                                                            |
| async_tree_memoization           | 310 ms                                                 | 208 ms: 1.49x faster                                                            |
| deepcopy                         | 226 us                                                 | 164 us: 1.37x faster                                                            |
| deepcopy_memo                    | 26.0 us                                                | 20.4 us: 1.27x faster                                                           |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 423 ms: 1.25x faster                                                            |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 422 ms: 1.25x faster                                                            |
| deepcopy_reduce                  | 2.01 us                                                | 1.70 us: 1.18x faster                                                           |
| generators                       | 29.4 ms                                                | 24.9 ms: 1.18x faster                                                           |
| dulwich_log                      | 29.2 ms                                                | 25.6 ms: 1.14x faster                                                           |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                            |
| coroutines                       | 19.7 ms                                                | 17.3 ms: 1.14x faster                                                           |
| async_generators                 | 299 ms                                                 | 264 ms: 1.13x faster                                                            |
| k_core                           | 1.72 sec                                               | 1.58 sec: 1.09x faster                                                          |
| comprehensions                   | 14.0 us                                                | 12.9 us: 1.09x faster                                                           |
| pylint                           | 182 ms                                                 | 168 ms: 1.08x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 99.8 ms: 1.08x faster                                                           |
| bench_mp_pool                    | 65.5 ms                                                | 60.9 ms: 1.08x faster                                                           |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                           |
| go                               | 98.5 ms                                                | 92.7 ms: 1.06x faster                                                           |
| raytrace                         | 204 ms                                                 | 192 ms: 1.06x faster                                                            |
| pathlib                          | 24.7 ms                                                | 23.5 ms: 1.05x faster                                                           |
| html5lib                         | 33.4 ms                                                | 32.3 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 362 ms: 1.03x faster                                                            |
| float                            | 54.1 ms                                                | 52.6 ms: 1.03x faster                                                           |
| sphinx                           | 613 ms                                                 | 596 ms: 1.03x faster                                                            |
| xml_etree_iterparse              | 75.5 ms                                                | 73.8 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.09 ms: 1.02x faster                                                           |
| thrift                           | 468 us                                                 | 459 us: 1.02x faster                                                            |
| sqlalchemy_declarative           | 61.9 ms                                                | 61.0 ms: 1.01x faster                                                           |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                            |
| regex_compile                    | 75.9 ms                                                | 75.3 ms: 1.01x faster                                                           |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.53 us: 1.01x faster                                                           |
| async_tree_eager                 | 65.8 ms                                                | 65.4 ms: 1.01x faster                                                           |
| scimark_fft                      | 194 ms                                                 | 193 ms: 1.01x faster                                                            |
| logging_simple                   | 3.60 us                                                | 3.62 us: 1.00x slower                                                           |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                            |
| bpe_tokeniser                    | 3.28 sec                                               | 3.30 sec: 1.01x slower                                                          |
| xml_etree_generate               | 55.4 ms                                                | 56.0 ms: 1.01x slower                                                           |
| logging_format                   | 3.90 us                                                | 3.94 us: 1.01x slower                                                           |
| logging_silent                   | 72.5 ns                                                | 73.3 ns: 1.01x slower                                                           |
| 2to3                             | 168 ms                                                 | 170 ms: 1.01x slower                                                            |
| sympy_sum                        | 76.2 ms                                                | 77.3 ms: 1.01x slower                                                           |
| docutils                         | 1.45 sec                                               | 1.49 sec: 1.02x slower                                                          |
| mdp                              | 1.49 sec                                               | 1.53 sec: 1.02x slower                                                          |
| scimark_sor                      | 85.8 ms                                                | 88.3 ms: 1.03x slower                                                           |
| sympy_str                        | 144 ms                                                 | 148 ms: 1.03x slower                                                            |
| tomli_loads                      | 1.36 sec                                               | 1.40 sec: 1.03x slower                                                          |
| pycparser                        | 673 ms                                                 | 695 ms: 1.03x slower                                                            |
| deltablue                        | 2.57 ms                                                | 2.65 ms: 1.03x slower                                                           |
| shortest_path                    | 331 ms                                                 | 343 ms: 1.04x slower                                                            |
| python_startup_no_site           | 13.2 ms                                                | 13.7 ms: 1.04x slower                                                           |
| genshi_xml                       | 30.5 ms                                                | 31.7 ms: 1.04x slower                                                           |
| genshi_text                      | 14.7 ms                                                | 15.3 ms: 1.04x slower                                                           |
| pprint_pformat                   | 986 ms                                                 | 1.03 sec: 1.04x slower                                                          |
| bench_thread_pool                | 483 us                                                 | 504 us: 1.04x slower                                                            |
| spectral_norm                    | 76.5 ms                                                | 79.9 ms: 1.05x slower                                                           |
| pprint_safe_repr                 | 483 ms                                                 | 506 ms: 1.05x slower                                                            |
| sqlalchemy_imperative            | 6.60 ms                                                | 6.92 ms: 1.05x slower                                                           |
| xml_etree_process                | 38.9 ms                                                | 40.9 ms: 1.05x slower                                                           |
| regex_v8                         | 15.1 ms                                                | 15.9 ms: 1.05x slower                                                           |
| json_loads                       | 17.0 us                                                | 18.0 us: 1.06x slower                                                           |
| connected_components             | 300 ms                                                 | 317 ms: 1.06x slower                                                            |
| scimark_monte_carlo              | 44.5 ms                                                | 47.1 ms: 1.06x slower                                                           |
| sympy_expand                     | 233 ms                                                 | 248 ms: 1.06x slower                                                            |
| json                             | 3.00 ms                                                | 3.19 ms: 1.06x slower                                                           |
| gc_traversal                     | 2.95 ms                                                | 3.14 ms: 1.07x slower                                                           |
| mako                             | 7.44 ms                                                | 7.96 ms: 1.07x slower                                                           |
| chaos                            | 41.6 ms                                                | 44.5 ms: 1.07x slower                                                           |
| scimark_lu                       | 73.5 ms                                                | 79.2 ms: 1.08x slower                                                           |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                           |
| typing_runtime_protocols         | 91.5 us                                                | 100.0 us: 1.09x slower                                                          |
| meteor_contest                   | 69.1 ms                                                | 76.4 ms: 1.11x slower                                                           |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                            |
| create_gc_cycles                 | 1.15 ms                                                | 1.29 ms: 1.12x slower                                                           |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                            |
| unpickle_pure_python             | 145 us                                                 | 164 us: 1.13x slower                                                            |
| hexiom                           | 4.38 ms                                                | 4.96 ms: 1.13x slower                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 397 ms: 1.14x slower                                                            |
| many_optionals                   | 403 us                                                 | 465 us: 1.16x slower                                                            |
| nqueens                          | 59.5 ms                                                | 68.8 ms: 1.16x slower                                                           |
| django_template                  | 19.7 ms                                                | 22.8 ms: 1.16x slower                                                           |
| crypto_pyaes                     | 51.4 ms                                                | 60.9 ms: 1.18x slower                                                           |
| telco                            | 3.92 ms                                                | 4.68 ms: 1.19x slower                                                           |
| nbody                            | 67.6 ms                                                | 81.0 ms: 1.20x slower                                                           |
| coverage                         | 38.5 ms                                                | 46.4 ms: 1.21x slower                                                           |
| richards_super                   | 34.6 ms                                                | 41.7 ms: 1.21x slower                                                           |
| json_dumps                       | 6.19 ms                                                | 7.50 ms: 1.21x slower                                                           |
| richards                         | 30.6 ms                                                | 37.2 ms: 1.22x slower                                                           |
| fannkuch                         | 250 ms                                                 | 308 ms: 1.23x slower                                                            |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 183 ms: 1.29x slower                                                            |
| async_tree_eager_tg              | 46.9 ms                                                | 136 ms: 2.89x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.02x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, python_startup
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250312-3.14.0a5+-2a08194/bm-20250312-darwin-arm64-faster%2dcpython-immortal_stickiness-3.14.0a5+-2a08194.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.018x faster

# HPT report

- Reliability score: 73.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.11x