# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 181 ms                                                 | 171 ms: 1.06x faster                                                             |
| docutils       | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                           |
| html5lib       | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                            |
| sphinx         | 600 ms                                                 | 576 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 289 ms                                                 | 192 ms: 1.51x faster                                                             |
| async_tree_eager_io              | 514 ms                                                 | 369 ms: 1.39x faster                                                             |
| async_tree_io                    | 510 ms                                                 | 376 ms: 1.36x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.34x faster                                                             |
| async_tree_io_tg                 | 499 ms                                                 | 374 ms: 1.33x faster                                                             |
| async_tree_none_tg               | 199 ms                                                 | 155 ms: 1.28x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.27x faster                                                             |
| async_tree_eager_io_tg           | 481 ms                                                 | 378 ms: 1.27x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| coroutines                       | 19.8 ms                                                | 17.7 ms: 1.12x faster                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 419 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 420 ms: 1.07x faster                                                             |
| async_tree_eager                 | 69.9 ms                                                | 67.1 ms: 1.04x faster                                                            |
| async_generators                 | 292 ms                                                 | 282 ms: 1.04x faster                                                             |
| async_tree_eager_tg              | 48.0 ms                                                | 46.5 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 342 ms: 1.01x faster                                                             |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                             |
| Geometric mean                   | (ref)                                                  | 1.17x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 63.7 ms: 1.16x faster                                                            |
| float          | 56.3 ms                                                | 50.5 ms: 1.12x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                            |
| regex_compile  | 78.6 ms                                                | 69.8 ms: 1.13x faster                                                            |
| regex_dna      | 148 ms                                                 | 136 ms: 1.09x faster                                                             |
| regex_v8       | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.56 sec                                               | 1.21 sec: 1.30x faster                                                           |
| unpickle_pure_python | 164 us                                                 | 127 us: 1.30x faster                                                             |
| xml_etree_process    | 41.0 ms                                                | 35.1 ms: 1.17x faster                                                            |
| xml_etree_generate   | 57.0 ms                                                | 49.0 ms: 1.16x faster                                                            |
| pickle_pure_python   | 214 us                                                 | 190 us: 1.13x faster                                                             |
| xml_etree_parse      | 107 ms                                                 | 102 ms: 1.05x faster                                                             |
| xml_etree_iterparse  | 74.1 ms                                                | 71.9 ms: 1.03x faster                                                            |
| json_loads           | 17.0 us                                                | 16.5 us: 1.03x faster                                                            |
| json_dumps           | 6.51 ms                                                | 7.16 ms: 1.10x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                | 21.6 ms: 1.05x slower                                                            |
| python_startup_no_site | 15.8 ms                                                | 16.6 ms: 1.05x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 7.70 ms                                                | 6.26 ms: 1.23x faster                                                            |
| genshi_text     | 16.9 ms                                                | 14.5 ms: 1.17x faster                                                            |
| genshi_xml      | 34.1 ms                                                | 30.7 ms: 1.11x faster                                                            |
| django_template | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                         | 234 us                                                 | 153 us: 1.53x faster                                                             |
| async_tree_memoization_tg        | 289 ms                                                 | 192 ms: 1.51x faster                                                             |
| deepcopy_memo                    | 27.3 us                                                | 18.3 us: 1.50x faster                                                            |
| async_tree_eager_io              | 514 ms                                                 | 369 ms: 1.39x faster                                                             |
| async_tree_io                    | 510 ms                                                 | 376 ms: 1.36x faster                                                             |
| generators                       | 31.5 ms                                                | 23.4 ms: 1.34x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 201 ms: 1.34x faster                                                             |
| async_tree_io_tg                 | 499 ms                                                 | 374 ms: 1.33x faster                                                             |
| tomli_loads                      | 1.56 sec                                               | 1.21 sec: 1.30x faster                                                           |
| unpickle_pure_python             | 164 us                                                 | 127 us: 1.30x faster                                                             |
| deepcopy_reduce                  | 2.08 us                                                | 1.61 us: 1.29x faster                                                            |
| regex_effbot                     | 2.62 ms                                                | 2.03 ms: 1.29x faster                                                            |
| go                               | 115 ms                                                 | 89.3 ms: 1.29x faster                                                            |
| async_tree_none_tg               | 199 ms                                                 | 155 ms: 1.28x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 167 ms: 1.27x faster                                                             |
| async_tree_eager_io_tg           | 481 ms                                                 | 378 ms: 1.27x faster                                                             |
| mako                             | 7.70 ms                                                | 6.26 ms: 1.23x faster                                                            |
| spectral_norm                    | 76.3 ms                                                | 63.0 ms: 1.21x faster                                                            |
| genshi_text                      | 16.9 ms                                                | 14.5 ms: 1.17x faster                                                            |
| xml_etree_process                | 41.0 ms                                                | 35.1 ms: 1.17x faster                                                            |
| scimark_fft                      | 200 ms                                                 | 172 ms: 1.17x faster                                                             |
| xml_etree_generate               | 57.0 ms                                                | 49.0 ms: 1.16x faster                                                            |
| nbody                            | 73.9 ms                                                | 63.7 ms: 1.16x faster                                                            |
| pyflate                          | 355 ms                                                 | 310 ms: 1.15x faster                                                             |
| async_tree_eager_memoization     | 168 ms                                                 | 147 ms: 1.14x faster                                                             |
| scimark_monte_carlo              | 50.6 ms                                                | 44.8 ms: 1.13x faster                                                            |
| regex_compile                    | 78.6 ms                                                | 69.8 ms: 1.13x faster                                                            |
| pickle_pure_python               | 214 us                                                 | 190 us: 1.13x faster                                                             |
| coroutines                       | 19.8 ms                                                | 17.7 ms: 1.12x faster                                                            |
| float                            | 56.3 ms                                                | 50.5 ms: 1.12x faster                                                            |
| genshi_xml                       | 34.1 ms                                                | 30.7 ms: 1.11x faster                                                            |
| html5lib                         | 36.6 ms                                                | 33.0 ms: 1.11x faster                                                            |
| pprint_pformat                   | 1.10 sec                                               | 991 ms: 1.11x faster                                                             |
| pylint                           | 179 ms                                                 | 162 ms: 1.11x faster                                                             |
| bpe_tokeniser                    | 3.25 sec                                               | 2.94 sec: 1.11x faster                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed          | 460 ms                                                 | 419 ms: 1.10x faster                                                             |
| pprint_safe_repr                 | 535 ms                                                 | 489 ms: 1.09x faster                                                             |
| regex_dna                        | 148 ms                                                 | 136 ms: 1.09x faster                                                             |
| scimark_sor                      | 106 ms                                                 | 97.3 ms: 1.09x faster                                                            |
| connected_components             | 320 ms                                                 | 295 ms: 1.08x faster                                                             |
| k_core                           | 1.62 sec                                               | 1.49 sec: 1.08x faster                                                           |
| thrift                           | 465 us                                                 | 435 us: 1.07x faster                                                             |
| shortest_path                    | 349 ms                                                 | 326 ms: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 420 ms: 1.07x faster                                                             |
| nqueens                          | 61.8 ms                                                | 57.8 ms: 1.07x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 15.9 ms: 1.07x faster                                                            |
| telco                            | 4.79 ms                                                | 4.51 ms: 1.06x faster                                                            |
| logging_simple                   | 3.59 us                                                | 3.39 us: 1.06x faster                                                            |
| 2to3                             | 181 ms                                                 | 171 ms: 1.06x faster                                                             |
| json                             | 3.06 ms                                                | 2.89 ms: 1.06x faster                                                            |
| fannkuch                         | 285 ms                                                 | 270 ms: 1.06x faster                                                             |
| hexiom                           | 4.83 ms                                                | 4.58 ms: 1.05x faster                                                            |
| logging_format                   | 3.90 us                                                | 3.70 us: 1.05x faster                                                            |
| richards_super                   | 39.2 ms                                                | 37.3 ms: 1.05x faster                                                            |
| xml_etree_parse                  | 107 ms                                                 | 102 ms: 1.05x faster                                                             |
| meteor_contest                   | 75.1 ms                                                | 71.7 ms: 1.05x faster                                                            |
| richards                         | 35.2 ms                                                | 33.6 ms: 1.05x faster                                                            |
| raytrace                         | 181 ms                                                 | 173 ms: 1.05x faster                                                             |
| deltablue                        | 2.67 ms                                                | 2.56 ms: 1.04x faster                                                            |
| sphinx                           | 600 ms                                                 | 576 ms: 1.04x faster                                                             |
| scimark_sparse_mat_mult          | 3.00 ms                                                | 2.88 ms: 1.04x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 67.1 ms: 1.04x faster                                                            |
| pycparser                        | 708 ms                                                 | 681 ms: 1.04x faster                                                             |
| async_generators                 | 292 ms                                                 | 282 ms: 1.04x faster                                                             |
| sqlglot_optimize                 | 34.8 ms                                                | 33.6 ms: 1.03x faster                                                            |
| pathlib                          | 23.3 ms                                                | 22.5 ms: 1.03x faster                                                            |
| async_tree_eager_tg              | 48.0 ms                                                | 46.5 ms: 1.03x faster                                                            |
| xml_etree_iterparse              | 74.1 ms                                                | 71.9 ms: 1.03x faster                                                            |
| coverage                         | 45.5 ms                                                | 44.2 ms: 1.03x faster                                                            |
| sqlglot_normalize                | 188 ms                                                 | 182 ms: 1.03x faster                                                             |
| json_loads                       | 17.0 us                                                | 16.5 us: 1.03x faster                                                            |
| scimark_lu                       | 76.7 ms                                                | 74.7 ms: 1.03x faster                                                            |
| chaos                            | 41.3 ms                                                | 40.2 ms: 1.03x faster                                                            |
| typing_runtime_protocols         | 103 us                                                 | 100 us: 1.02x faster                                                             |
| sympy_expand                     | 247 ms                                                 | 242 ms: 1.02x faster                                                             |
| sympy_sum                        | 75.1 ms                                                | 73.5 ms: 1.02x faster                                                            |
| bench_thread_pool                | 508 us                                                 | 497 us: 1.02x faster                                                             |
| bench_mp_pool                    | 64.9 ms                                                | 63.7 ms: 1.02x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 366 ms: 1.02x faster                                                             |
| sympy_str                        | 145 ms                                                 | 143 ms: 1.02x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 346 ms                                                 | 342 ms: 1.01x faster                                                             |
| crypto_pyaes                     | 54.4 ms                                                | 53.9 ms: 1.01x faster                                                            |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.01x faster                                                             |
| sqlite_synth                     | 1.56 us                                                | 1.55 us: 1.00x faster                                                            |
| mdp                              | 1.50 sec                                               | 1.50 sec: 1.00x slower                                                           |
| docutils                         | 1.44 sec                                               | 1.45 sec: 1.01x slower                                                           |
| sqlglot_parse                    | 859 us                                                 | 867 us: 1.01x slower                                                             |
| sqlglot_transpile                | 1.03 ms                                                | 1.04 ms: 1.01x slower                                                            |
| sqlalchemy_imperative            | 6.68 ms                                                | 6.79 ms: 1.02x slower                                                            |
| logging_silent                   | 70.1 ns                                                | 71.9 ns: 1.03x slower                                                            |
| django_template                  | 20.5 ms                                                | 21.1 ms: 1.03x slower                                                            |
| sympy_integrate                  | 11.3 ms                                                | 11.6 ms: 1.03x slower                                                            |
| dulwich_log                      | 28.6 ms                                                | 29.6 ms: 1.03x slower                                                            |
| python_startup                   | 20.6 ms                                                | 21.6 ms: 1.05x slower                                                            |
| gc_traversal                     | 2.93 ms                                                | 3.07 ms: 1.05x slower                                                            |
| python_startup_no_site           | 15.8 ms                                                | 16.6 ms: 1.05x slower                                                            |
| create_gc_cycles                 | 1.20 ms                                                | 1.26 ms: 1.06x slower                                                            |
| comprehensions                   | 12.0 us                                                | 13.0 us: 1.08x slower                                                            |
| json_dumps                       | 6.51 ms                                                | 7.16 ms: 1.10x slower                                                            |
| many_optionals                   | 324 us                                                 | 378 us: 1.17x slower                                                             |
| subparsers                       | 9.50 ms                                                | 12.4 ms: 1.30x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (2): pidigits, sqlalchemy_declarative
Ignored benchmarks (6) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, dask, djangocms, gevent_hub, gunicorn, tornado_http
Ignored benchmarks (1) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: mypy2

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.04x