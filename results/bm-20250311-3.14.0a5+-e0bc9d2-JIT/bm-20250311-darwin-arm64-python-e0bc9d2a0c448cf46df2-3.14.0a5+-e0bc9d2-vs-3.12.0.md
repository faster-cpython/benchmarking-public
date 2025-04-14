# Results vs. 3.12.0

- fork: python
- ref: e0bc9d2a0c448cf46df2
- machine: darwin-arm64
- commit hash: e0bc9d2
- commit date: 2025-03-11
- overall geometric mean: 1.008x faster
- HPT reliability: 86.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 176 ms: 1.05x slower                                                   |
| docutils       | 1.45 sec                                               | 1.54 sec: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 391 ms: 1.72x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 403 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 399 ms: 1.55x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.53x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 212 ms: 1.47x faster                                                   |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 435 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                                   |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                                  |
| async_generators                 | 299 ms                                                 | 290 ms: 1.03x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                   |
| async_tree_eager                 | 65.8 ms                                                | 67.9 ms: 1.03x slower                                                  |
| asyncio_websockets               | 243 ms                                                 | 251 ms: 1.03x slower                                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 410 ms: 1.18x slower                                                   |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 186 ms: 1.31x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 138 ms: 2.94x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 54.1 ms                                                | 47.3 ms: 1.14x faster                                                  |
| pidigits       | 283 ms                                                 | 293 ms: 1.04x slower                                                   |
| nbody          | 67.6 ms                                                | 72.0 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.33 ms: 1.05x faster                                                  |
| regex_dna      | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| regex_compile  | 75.9 ms                                                | 77.3 ms: 1.02x slower                                                  |
| regex_v8       | 15.1 ms                                                | 16.5 ms: 1.09x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| xml_etree_generate   | 55.4 ms                                                | 53.3 ms: 1.04x faster                                                  |
| tomli_loads          | 1.36 sec                                               | 1.31 sec: 1.04x faster                                                 |
| xml_etree_process    | 38.9 ms                                                | 37.8 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 73.9 ms: 1.02x faster                                                  |
| unpickle_pure_python | 145 us                                                 | 148 us: 1.02x slower                                                   |
| json_loads           | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 221 us: 1.12x slower                                                   |
| json_dumps           | 6.19 ms                                                | 7.47 ms: 1.21x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 17.9 ms: 1.01x slower                                                  |
| python_startup_no_site | 13.2 ms                                                | 13.5 ms: 1.02x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 6.94 ms: 1.07x faster                                                  |
| genshi_xml      | 30.5 ms                                                | 32.8 ms: 1.08x slower                                                  |
| genshi_text     | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                  |
| django_template | 19.7 ms                                                | 23.6 ms: 1.20x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                           |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2 |
|----------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 12.9 ms: 2.49x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 391 ms: 1.72x faster                                                   |
| async_tree_eager_io              | 666 ms                                                 | 389 ms: 1.71x faster                                                   |
| async_tree_io                    | 672 ms                                                 | 403 ms: 1.67x faster                                                   |
| async_tree_eager_io_tg           | 617 ms                                                 | 399 ms: 1.55x faster                                                   |
| async_tree_memoization_tg        | 318 ms                                                 | 207 ms: 1.53x faster                                                   |
| async_tree_none_tg               | 255 ms                                                 | 167 ms: 1.53x faster                                                   |
| async_tree_none                  | 263 ms                                                 | 175 ms: 1.51x faster                                                   |
| async_tree_memoization           | 310 ms                                                 | 212 ms: 1.47x faster                                                   |
| deepcopy                         | 226 us                                                 | 168 us: 1.34x faster                                                   |
| deepcopy_memo                    | 26.0 us                                                | 21.4 us: 1.22x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 435 ms: 1.21x faster                                                   |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 438 ms: 1.20x faster                                                   |
| spectral_norm                    | 76.5 ms                                                | 66.6 ms: 1.15x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.76 us: 1.14x faster                                                  |
| float                            | 54.1 ms                                                | 47.3 ms: 1.14x faster                                                  |
| generators                       | 29.4 ms                                                | 25.8 ms: 1.14x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                   |
| deltablue                        | 2.57 ms                                                | 2.33 ms: 1.10x faster                                                  |
| coroutines                       | 19.7 ms                                                | 17.9 ms: 1.10x faster                                                  |
| dulwich_log                      | 29.2 ms                                                | 26.7 ms: 1.09x faster                                                  |
| k_core                           | 1.72 sec                                               | 1.58 sec: 1.09x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.0 us: 1.08x faster                                                  |
| mako                             | 7.44 ms                                                | 6.94 ms: 1.07x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 102 ms: 1.05x faster                                                   |
| pylint                           | 182 ms                                                 | 173 ms: 1.05x faster                                                   |
| regex_effbot                     | 2.44 ms                                                | 2.33 ms: 1.05x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.6 ms: 1.05x faster                                                  |
| xml_etree_generate               | 55.4 ms                                                | 53.3 ms: 1.04x faster                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.31 sec: 1.04x faster                                                 |
| bpe_tokeniser                    | 3.28 sec                                               | 3.17 sec: 1.04x faster                                                 |
| async_generators                 | 299 ms                                                 | 290 ms: 1.03x faster                                                   |
| xml_etree_process                | 38.9 ms                                                | 37.8 ms: 1.03x faster                                                  |
| bench_mp_pool                    | 65.5 ms                                                | 63.9 ms: 1.02x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 73.9 ms: 1.02x faster                                                  |
| raytrace                         | 204 ms                                                 | 200 ms: 1.02x faster                                                   |
| dask                             | 779 ms                                                 | 768 ms: 1.01x faster                                                   |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 372 ms: 1.01x faster                                                   |
| thrift                           | 468 us                                                 | 471 us: 1.01x slower                                                   |
| python_startup                   | 17.8 ms                                                | 17.9 ms: 1.01x slower                                                  |
| regex_dna                        | 143 ms                                                 | 145 ms: 1.02x slower                                                   |
| unpickle_pure_python             | 145 us                                                 | 148 us: 1.02x slower                                                   |
| regex_compile                    | 75.9 ms                                                | 77.3 ms: 1.02x slower                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 63.1 ms: 1.02x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 13.5 ms: 1.02x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.23 ms: 1.03x slower                                                  |
| logging_silent                   | 72.5 ns                                                | 74.5 ns: 1.03x slower                                                  |
| shortest_path                    | 331 ms                                                 | 340 ms: 1.03x slower                                                   |
| mdp                              | 1.49 sec                                               | 1.54 sec: 1.03x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 67.9 ms: 1.03x slower                                                  |
| asyncio_websockets               | 243 ms                                                 | 251 ms: 1.03x slower                                                   |
| logging_simple                   | 3.60 us                                                | 3.73 us: 1.03x slower                                                  |
| connected_components             | 300 ms                                                 | 310 ms: 1.03x slower                                                   |
| scimark_fft                      | 194 ms                                                 | 201 ms: 1.03x slower                                                   |
| pidigits                         | 283 ms                                                 | 293 ms: 1.04x slower                                                   |
| sympy_sum                        | 76.2 ms                                                | 79.0 ms: 1.04x slower                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.61 us: 1.04x slower                                                  |
| logging_format                   | 3.90 us                                                | 4.07 us: 1.04x slower                                                  |
| 2to3                             | 168 ms                                                 | 176 ms: 1.05x slower                                                   |
| json                             | 3.00 ms                                                | 3.14 ms: 1.05x slower                                                  |
| sympy_str                        | 144 ms                                                 | 152 ms: 1.06x slower                                                   |
| docutils                         | 1.45 sec                                               | 1.54 sec: 1.06x slower                                                 |
| nbody                            | 67.6 ms                                                | 72.0 ms: 1.07x slower                                                  |
| richards_super                   | 34.6 ms                                                | 36.9 ms: 1.07x slower                                                  |
| go                               | 98.5 ms                                                | 105 ms: 1.07x slower                                                   |
| bench_thread_pool                | 483 us                                                 | 516 us: 1.07x slower                                                   |
| scimark_sor                      | 85.8 ms                                                | 91.7 ms: 1.07x slower                                                  |
| json_loads                       | 17.0 us                                                | 18.2 us: 1.07x slower                                                  |
| pyflate                          | 311 ms                                                 | 333 ms: 1.07x slower                                                   |
| genshi_xml                       | 30.5 ms                                                | 32.8 ms: 1.08x slower                                                  |
| genshi_text                      | 14.7 ms                                                | 15.9 ms: 1.08x slower                                                  |
| chaos                            | 41.6 ms                                                | 45.5 ms: 1.09x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.5 ms: 1.09x slower                                                  |
| scimark_monte_carlo              | 44.5 ms                                                | 48.6 ms: 1.09x slower                                                  |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.23 ms: 1.10x slower                                                  |
| gc_traversal                     | 2.95 ms                                                | 3.23 ms: 1.10x slower                                                  |
| richards                         | 30.6 ms                                                | 33.6 ms: 1.10x slower                                                  |
| pycparser                        | 673 ms                                                 | 741 ms: 1.10x slower                                                   |
| scimark_lu                       | 73.5 ms                                                | 81.1 ms: 1.10x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 258 ms: 1.11x slower                                                   |
| typing_runtime_protocols         | 91.5 us                                                | 101 us: 1.11x slower                                                   |
| sympy_integrate                  | 11.1 ms                                                | 12.4 ms: 1.12x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 221 us: 1.12x slower                                                   |
| pprint_pformat                   | 986 ms                                                 | 1.10 sec: 1.12x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 544 ms: 1.13x slower                                                   |
| meteor_contest                   | 69.1 ms                                                | 79.4 ms: 1.15x slower                                                  |
| nqueens                          | 59.5 ms                                                | 68.8 ms: 1.16x slower                                                  |
| create_gc_cycles                 | 1.15 ms                                                | 1.33 ms: 1.16x slower                                                  |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 410 ms: 1.18x slower                                                   |
| hexiom                           | 4.38 ms                                                | 5.19 ms: 1.19x slower                                                  |
| django_template                  | 19.7 ms                                                | 23.6 ms: 1.20x slower                                                  |
| json_dumps                       | 6.19 ms                                                | 7.47 ms: 1.21x slower                                                  |
| many_optionals                   | 403 us                                                 | 488 us: 1.21x slower                                                   |
| telco                            | 3.92 ms                                                | 4.76 ms: 1.22x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 62.7 ms: 1.22x slower                                                  |
| fannkuch                         | 250 ms                                                 | 308 ms: 1.23x slower                                                   |
| coverage                         | 38.5 ms                                                | 48.3 ms: 1.25x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 186 ms: 1.31x slower                                                   |
| async_tree_eager_tg              | 46.9 ms                                                | 138 ms: 2.94x slower                                                   |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): html5lib, sphinx
Ignored benchmarks (9) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250311-3.14.0a5+-e0bc9d2-JIT/bm-20250311-darwin-arm64-python-e0bc9d2a0c448cf46df2-3.14.0a5+-e0bc9d2.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.008x faster

# HPT report

- Reliability score: 86.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x