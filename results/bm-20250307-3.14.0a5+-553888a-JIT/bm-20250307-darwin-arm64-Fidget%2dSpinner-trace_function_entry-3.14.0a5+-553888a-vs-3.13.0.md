# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: darwin-arm64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.067x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 165 ms: 1.08x faster                                                             |
| html5lib       | 36.7 ms                                                | 29.7 ms: 1.23x faster                                                            |
| sphinx         | 602 ms                                                 | 578 ms: 1.04x faster                                                             |
| Geometric mean | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_memoization_tg        | 288 ms                                                 | 198 ms: 1.46x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                             |
| async_tree_io                    | 508 ms                                                 | 366 ms: 1.39x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                             |
| async_tree_memoization           | 268 ms                                                 | 203 ms: 1.32x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                             |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                             |
| coroutines                       | 20.0 ms                                                | 16.8 ms: 1.19x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                             |
| async_generators                 | 294 ms                                                 | 255 ms: 1.15x faster                                                             |
| async_tree_eager                 | 69.9 ms                                                | 62.1 ms: 1.13x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                             |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                             |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                             |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                             |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 55.8 ms                                                | 47.9 ms: 1.16x faster                                                            |
| nbody          | 73.6 ms                                                | 67.7 ms: 1.09x faster                                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                            |
| regex_compile  | 78.3 ms                                                | 71.0 ms: 1.10x faster                                                            |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                                             |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 1.57 sec                                               | 1.29 sec: 1.21x faster                                                           |
| unpickle_pure_python | 165 us                                                 | 142 us: 1.17x faster                                                             |
| xml_etree_process    | 41.3 ms                                                | 37.2 ms: 1.11x faster                                                            |
| xml_etree_generate   | 57.1 ms                                                | 52.2 ms: 1.09x faster                                                            |
| xml_etree_parse      | 108 ms                                                 | 103 ms: 1.05x faster                                                             |
| xml_etree_iterparse  | 74.2 ms                                                | 71.1 ms: 1.04x faster                                                            |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                            |
| json_dumps           | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                            |
| python_startup_no_site | 13.7 ms                                                | 15.1 ms: 1.10x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                            |
| mako            | 7.75 ms                                                | 6.66 ms: 1.16x faster                                                            |
| genshi_xml      | 34.1 ms                                                | 29.6 ms: 1.15x faster                                                            |
| django_template | 20.5 ms                                                | 21.3 ms: 1.04x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                     |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250307-darwin-arm64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| deepcopy                         | 236 us                                                 | 152 us: 1.55x faster                                                             |
| deepcopy_memo                    | 27.4 us                                                | 18.7 us: 1.47x faster                                                            |
| async_tree_memoization_tg        | 288 ms                                                 | 198 ms: 1.46x faster                                                             |
| async_tree_eager_io              | 511 ms                                                 | 362 ms: 1.41x faster                                                             |
| go                               | 117 ms                                                 | 83.1 ms: 1.40x faster                                                            |
| async_tree_io                    | 508 ms                                                 | 366 ms: 1.39x faster                                                             |
| async_tree_io_tg                 | 500 ms                                                 | 366 ms: 1.37x faster                                                             |
| generators                       | 31.9 ms                                                | 23.8 ms: 1.34x faster                                                            |
| deepcopy_reduce                  | 2.09 us                                                | 1.58 us: 1.32x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 203 ms: 1.32x faster                                                             |
| async_tree_none                  | 212 ms                                                 | 161 ms: 1.31x faster                                                             |
| scimark_sor                      | 106 ms                                                 | 80.9 ms: 1.31x faster                                                            |
| async_tree_eager_io_tg           | 479 ms                                                 | 374 ms: 1.28x faster                                                             |
| async_tree_none_tg               | 198 ms                                                 | 156 ms: 1.27x faster                                                             |
| html5lib                         | 36.7 ms                                                | 29.7 ms: 1.23x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.29 sec: 1.21x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 14.1 ms: 1.20x faster                                                            |
| coroutines                       | 20.0 ms                                                | 16.8 ms: 1.19x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 141 ms: 1.19x faster                                                             |
| regex_effbot                     | 2.63 ms                                                | 2.24 ms: 1.17x faster                                                            |
| unpickle_pure_python             | 165 us                                                 | 142 us: 1.17x faster                                                             |
| mako                             | 7.75 ms                                                | 6.66 ms: 1.16x faster                                                            |
| float                            | 55.8 ms                                                | 47.9 ms: 1.16x faster                                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 43.5 ms: 1.16x faster                                                            |
| async_generators                 | 294 ms                                                 | 255 ms: 1.15x faster                                                             |
| genshi_xml                       | 34.1 ms                                                | 29.6 ms: 1.15x faster                                                            |
| async_tree_eager                 | 69.9 ms                                                | 62.1 ms: 1.13x faster                                                            |
| pyflate                          | 352 ms                                                 | 313 ms: 1.12x faster                                                             |
| xml_etree_process                | 41.3 ms                                                | 37.2 ms: 1.11x faster                                                            |
| logging_simple                   | 3.56 us                                                | 3.22 us: 1.11x faster                                                            |
| regex_compile                    | 78.3 ms                                                | 71.0 ms: 1.10x faster                                                            |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 417 ms: 1.10x faster                                                             |
| richards                         | 36.2 ms                                                | 32.8 ms: 1.10x faster                                                            |
| pylint                           | 180 ms                                                 | 164 ms: 1.10x faster                                                             |
| xml_etree_generate               | 57.1 ms                                                | 52.2 ms: 1.09x faster                                                            |
| deltablue                        | 2.65 ms                                                | 2.42 ms: 1.09x faster                                                            |
| logging_format                   | 3.85 us                                                | 3.53 us: 1.09x faster                                                            |
| hexiom                           | 4.87 ms                                                | 4.47 ms: 1.09x faster                                                            |
| bpe_tokeniser                    | 3.26 sec                                               | 3.00 sec: 1.09x faster                                                           |
| nbody                            | 73.6 ms                                                | 67.7 ms: 1.09x faster                                                            |
| 2to3                             | 179 ms                                                 | 165 ms: 1.08x faster                                                             |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 417 ms: 1.07x faster                                                             |
| thrift                           | 466 us                                                 | 435 us: 1.07x faster                                                             |
| typing_runtime_protocols         | 101 us                                                 | 94.5 us: 1.07x faster                                                            |
| scimark_fft                      | 200 ms                                                 | 187 ms: 1.07x faster                                                             |
| connected_components             | 319 ms                                                 | 299 ms: 1.06x faster                                                             |
| telco                            | 4.84 ms                                                | 4.55 ms: 1.06x faster                                                            |
| k_core                           | 1.61 sec                                               | 1.52 sec: 1.06x faster                                                           |
| spectral_norm                    | 76.5 ms                                                | 72.2 ms: 1.06x faster                                                            |
| bench_mp_pool                    | 64.7 ms                                                | 61.2 ms: 1.06x faster                                                            |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                                             |
| richards_super                   | 39.2 ms                                                | 37.2 ms: 1.05x faster                                                            |
| shortest_path                    | 345 ms                                                 | 329 ms: 1.05x faster                                                             |
| logging_silent                   | 71.0 ns                                                | 67.7 ns: 1.05x faster                                                            |
| xml_etree_parse                  | 108 ms                                                 | 103 ms: 1.05x faster                                                             |
| xml_etree_iterparse              | 74.2 ms                                                | 71.1 ms: 1.04x faster                                                            |
| sphinx                           | 602 ms                                                 | 578 ms: 1.04x faster                                                             |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 359 ms: 1.04x faster                                                             |
| chaos                            | 41.1 ms                                                | 39.6 ms: 1.04x faster                                                            |
| pycparser                        | 701 ms                                                 | 678 ms: 1.03x faster                                                             |
| nqueens                          | 61.8 ms                                                | 60.1 ms: 1.03x faster                                                            |
| sympy_str                        | 146 ms                                                 | 142 ms: 1.03x faster                                                             |
| sympy_expand                     | 248 ms                                                 | 241 ms: 1.03x faster                                                             |
| scimark_lu                       | 75.9 ms                                                | 74.3 ms: 1.02x faster                                                            |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.02x faster                                                            |
| comprehensions                   | 12.0 us                                                | 11.8 us: 1.02x faster                                                            |
| bench_thread_pool                | 503 us                                                 | 496 us: 1.01x faster                                                             |
| sympy_sum                        | 75.1 ms                                                | 74.2 ms: 1.01x faster                                                            |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                            |
| dask                             | 771 ms                                                 | 767 ms: 1.01x faster                                                             |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.00x faster                                                           |
| asyncio_websockets               | 242 ms                                                 | 242 ms: 1.00x faster                                                             |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 2.97 ms: 1.00x faster                                                            |
| sqlalchemy_declarative           | 59.0 ms                                                | 59.2 ms: 1.00x slower                                                            |
| raytrace                         | 181 ms                                                 | 183 ms: 1.01x slower                                                             |
| sqlalchemy_imperative            | 6.69 ms                                                | 6.76 ms: 1.01x slower                                                            |
| crypto_pyaes                     | 55.3 ms                                                | 56.0 ms: 1.01x slower                                                            |
| sympy_integrate                  | 11.3 ms                                                | 11.5 ms: 1.01x slower                                                            |
| sqlglot_transpile                | 1.04 ms                                                | 1.07 ms: 1.03x slower                                                            |
| django_template                  | 20.5 ms                                                | 21.3 ms: 1.04x slower                                                            |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                            |
| python_startup                   | 18.8 ms                                                | 19.6 ms: 1.04x slower                                                            |
| gc_traversal                     | 2.94 ms                                                | 3.09 ms: 1.05x slower                                                            |
| sqlglot_parse                    | 852 us                                                 | 900 us: 1.06x slower                                                             |
| create_gc_cycles                 | 1.19 ms                                                | 1.27 ms: 1.06x slower                                                            |
| fannkuch                         | 279 ms                                                 | 305 ms: 1.10x slower                                                             |
| python_startup_no_site           | 13.7 ms                                                | 15.1 ms: 1.10x slower                                                            |
| many_optionals                   | 409 us                                                 | 456 us: 1.12x slower                                                             |
| json_dumps                       | 6.47 ms                                                | 7.29 ms: 1.13x slower                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 392 ms: 1.13x slower                                                             |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 175 ms: 1.27x slower                                                             |
| subparsers                       | 9.44 ms                                                | 12.2 ms: 1.29x slower                                                            |
| async_tree_eager_tg              | 47.4 ms                                                | 131 ms: 2.76x slower                                                             |
| Geometric mean                   | (ref)                                                  | 1.07x faster                                                                     |

Benchmark hidden because not significant (7): json, pickle_pure_python, pidigits, meteor_contest, dulwich_log, coverage, pathlib
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, djangocms, docutils, gevent_hub, gunicorn, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.09x