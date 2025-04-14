# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: clang_hot
- machine: darwin-arm64
- commit hash: 37fb620
- commit date: 2025-03-06
- overall geometric mean: 1.014x slower
- HPT reliability: 99.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 176 ms: 1.04x slower                                                  |
| docutils       | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.03x slower                                                          |

Benchmark hidden because not significant (2): html5lib, sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 398 ms: 1.69x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 401 ms: 1.68x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.53x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                  |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| coroutines                       | 19.7 ms                                                | 18.5 ms: 1.06x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 365 ms: 1.02x faster                                                  |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| async_tree_eager                 | 65.8 ms                                                | 68.2 ms: 1.04x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                                  |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| float          | 54.1 ms                                                | 54.6 ms: 1.01x slower                                                 |
| nbody          | 67.6 ms                                                | 91.7 ms: 1.36x slower                                                 |
| Geometric mean | (ref)                                                  | 1.11x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                 |
| regex_dna      | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| regex_compile  | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                 |
| regex_v8       | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 75.5 ms                                                | 74.8 ms: 1.01x faster                                                 |
| json_loads           | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| xml_etree_generate   | 55.4 ms                                                | 58.0 ms: 1.05x slower                                                 |
| tomli_loads          | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                |
| xml_etree_process    | 38.9 ms                                                | 42.9 ms: 1.10x slower                                                 |
| unpickle_pure_python | 145 us                                                 | 170 us: 1.17x slower                                                  |
| pickle_pure_python   | 197 us                                                 | 230 us: 1.17x slower                                                  |
| json_dumps           | 6.19 ms                                                | 7.59 ms: 1.23x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 13.2 ms                                                | 14.0 ms: 1.07x slower                                                 |
| python_startup         | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                 |
| genshi_text     | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                 |
| mako            | 7.44 ms                                                | 8.39 ms: 1.13x slower                                                 |
| django_template | 19.7 ms                                                | 24.2 ms: 1.23x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250306-darwin-arm64-Fidget%2dSpinner-clang_hot-3.14.0a5+-37fb620 |
|----------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.0 ms: 2.48x faster                                                 |
| async_tree_eager_io              | 666 ms                                                 | 394 ms: 1.69x faster                                                  |
| async_tree_io                    | 672 ms                                                 | 398 ms: 1.69x faster                                                  |
| async_tree_io_tg                 | 673 ms                                                 | 401 ms: 1.68x faster                                                  |
| async_tree_eager_io_tg           | 617 ms                                                 | 405 ms: 1.53x faster                                                  |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                  |
| async_tree_none_tg               | 255 ms                                                 | 172 ms: 1.49x faster                                                  |
| async_tree_none                  | 263 ms                                                 | 178 ms: 1.48x faster                                                  |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                  |
| deepcopy                         | 226 us                                                 | 168 us: 1.34x faster                                                  |
| deepcopy_memo                    | 26.0 us                                                | 20.9 us: 1.24x faster                                                 |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 428 ms: 1.23x faster                                                  |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 437 ms: 1.21x faster                                                  |
| deepcopy_reduce                  | 2.01 us                                                | 1.75 us: 1.15x faster                                                 |
| k_core                           | 1.72 sec                                               | 1.54 sec: 1.12x faster                                                |
| async_generators                 | 299 ms                                                 | 267 ms: 1.12x faster                                                  |
| async_tree_eager_memoization     | 168 ms                                                 | 150 ms: 1.12x faster                                                  |
| regex_effbot                     | 2.44 ms                                                | 2.27 ms: 1.07x faster                                                 |
| bench_mp_pool                    | 65.5 ms                                                | 61.2 ms: 1.07x faster                                                 |
| comprehensions                   | 14.0 us                                                | 13.1 us: 1.07x faster                                                 |
| coroutines                       | 19.7 ms                                                | 18.5 ms: 1.06x faster                                                 |
| pylint                           | 182 ms                                                 | 171 ms: 1.06x faster                                                  |
| xml_etree_parse                  | 108 ms                                                 | 104 ms: 1.04x faster                                                  |
| pathlib                          | 24.7 ms                                                | 23.8 ms: 1.04x faster                                                 |
| go                               | 98.5 ms                                                | 94.8 ms: 1.04x faster                                                 |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 365 ms: 1.02x faster                                                  |
| regex_dna                        | 143 ms                                                 | 141 ms: 1.01x faster                                                  |
| bpe_tokeniser                    | 3.28 sec                                               | 3.24 sec: 1.01x faster                                                |
| dask                             | 779 ms                                                 | 770 ms: 1.01x faster                                                  |
| xml_etree_iterparse              | 75.5 ms                                                | 74.8 ms: 1.01x faster                                                 |
| thrift                           | 468 us                                                 | 464 us: 1.01x faster                                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                                 |
| asyncio_websockets               | 243 ms                                                 | 242 ms: 1.00x faster                                                  |
| generators                       | 29.4 ms                                                | 29.3 ms: 1.00x faster                                                 |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                  |
| float                            | 54.1 ms                                                | 54.6 ms: 1.01x slower                                                 |
| logging_silent                   | 72.5 ns                                                | 73.2 ns: 1.01x slower                                                 |
| scimark_fft                      | 194 ms                                                 | 196 ms: 1.01x slower                                                  |
| sqlalchemy_declarative           | 61.9 ms                                                | 62.7 ms: 1.01x slower                                                 |
| regex_compile                    | 75.9 ms                                                | 77.9 ms: 1.03x slower                                                 |
| dulwich_log                      | 29.2 ms                                                | 30.0 ms: 1.03x slower                                                 |
| logging_simple                   | 3.60 us                                                | 3.71 us: 1.03x slower                                                 |
| shortest_path                    | 331 ms                                                 | 341 ms: 1.03x slower                                                  |
| docutils                         | 1.45 sec                                               | 1.50 sec: 1.03x slower                                                |
| logging_format                   | 3.90 us                                                | 4.04 us: 1.03x slower                                                 |
| async_tree_eager                 | 65.8 ms                                                | 68.2 ms: 1.04x slower                                                 |
| sympy_sum                        | 76.2 ms                                                | 79.2 ms: 1.04x slower                                                 |
| raytrace                         | 204 ms                                                 | 212 ms: 1.04x slower                                                  |
| json_loads                       | 17.0 us                                                | 17.7 us: 1.04x slower                                                 |
| pycparser                        | 673 ms                                                 | 702 ms: 1.04x slower                                                  |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.28 ms: 1.04x slower                                                 |
| mdp                              | 1.49 sec                                               | 1.56 sec: 1.04x slower                                                |
| 2to3                             | 168 ms                                                 | 176 ms: 1.04x slower                                                  |
| xml_etree_generate               | 55.4 ms                                                | 58.0 ms: 1.05x slower                                                 |
| connected_components             | 300 ms                                                 | 315 ms: 1.05x slower                                                  |
| tomli_loads                      | 1.36 sec                                               | 1.43 sec: 1.05x slower                                                |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                 |
| chaos                            | 41.6 ms                                                | 44.0 ms: 1.06x slower                                                 |
| sympy_str                        | 144 ms                                                 | 153 ms: 1.06x slower                                                  |
| python_startup_no_site           | 13.2 ms                                                | 14.0 ms: 1.07x slower                                                 |
| python_startup                   | 17.8 ms                                                | 19.0 ms: 1.07x slower                                                 |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.07 ms: 1.07x slower                                                 |
| deltablue                        | 2.57 ms                                                | 2.76 ms: 1.07x slower                                                 |
| sqlglot_optimize                 | 33.2 ms                                                | 35.9 ms: 1.08x slower                                                 |
| bench_thread_pool                | 483 us                                                 | 522 us: 1.08x slower                                                  |
| nqueens                          | 59.5 ms                                                | 65.0 ms: 1.09x slower                                                 |
| sqlglot_normalize                | 180 ms                                                 | 196 ms: 1.09x slower                                                  |
| sympy_expand                     | 233 ms                                                 | 256 ms: 1.09x slower                                                  |
| sqlglot_transpile                | 973 us                                                 | 1.07 ms: 1.10x slower                                                 |
| sqlglot_parse                    | 808 us                                                 | 890 us: 1.10x slower                                                  |
| sympy_integrate                  | 11.1 ms                                                | 12.2 ms: 1.10x slower                                                 |
| xml_etree_process                | 38.9 ms                                                | 42.9 ms: 1.10x slower                                                 |
| spectral_norm                    | 76.5 ms                                                | 84.4 ms: 1.10x slower                                                 |
| genshi_xml                       | 30.5 ms                                                | 33.8 ms: 1.11x slower                                                 |
| genshi_text                      | 14.7 ms                                                | 16.3 ms: 1.11x slower                                                 |
| scimark_sor                      | 85.8 ms                                                | 95.4 ms: 1.11x slower                                                 |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                 |
| typing_runtime_protocols         | 91.5 us                                                | 102 us: 1.11x slower                                                  |
| regex_v8                         | 15.1 ms                                                | 16.9 ms: 1.12x slower                                                 |
| scimark_monte_carlo              | 44.5 ms                                                | 49.9 ms: 1.12x slower                                                 |
| pprint_pformat                   | 986 ms                                                 | 1.11 sec: 1.12x slower                                                |
| meteor_contest                   | 69.1 ms                                                | 77.8 ms: 1.13x slower                                                 |
| mako                             | 7.44 ms                                                | 8.39 ms: 1.13x slower                                                 |
| pyflate                          | 311 ms                                                 | 351 ms: 1.13x slower                                                  |
| scimark_lu                       | 73.5 ms                                                | 83.1 ms: 1.13x slower                                                 |
| pprint_safe_repr                 | 483 ms                                                 | 549 ms: 1.13x slower                                                  |
| crypto_pyaes                     | 51.4 ms                                                | 59.2 ms: 1.15x slower                                                 |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                  |
| unpickle_pure_python             | 145 us                                                 | 170 us: 1.17x slower                                                  |
| many_optionals                   | 403 us                                                 | 470 us: 1.17x slower                                                  |
| pickle_pure_python               | 197 us                                                 | 230 us: 1.17x slower                                                  |
| fannkuch                         | 250 ms                                                 | 293 ms: 1.17x slower                                                  |
| hexiom                           | 4.38 ms                                                | 5.27 ms: 1.20x slower                                                 |
| telco                            | 3.92 ms                                                | 4.74 ms: 1.21x slower                                                 |
| json_dumps                       | 6.19 ms                                                | 7.59 ms: 1.23x slower                                                 |
| django_template                  | 19.7 ms                                                | 24.2 ms: 1.23x slower                                                 |
| coverage                         | 38.5 ms                                                | 47.3 ms: 1.23x slower                                                 |
| richards_super                   | 34.6 ms                                                | 42.9 ms: 1.24x slower                                                 |
| richards                         | 30.6 ms                                                | 39.9 ms: 1.30x slower                                                 |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 190 ms: 1.34x slower                                                  |
| nbody                            | 67.6 ms                                                | 91.7 ms: 1.36x slower                                                 |
| async_tree_eager_tg              | 46.9 ms                                                | 142 ms: 3.02x slower                                                  |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (3): html5lib, json, sphinx
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, tornado_http

- Geometric mean (including insignificant results): 1.014x slower

# HPT report

- Reliability score: 99.16% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.12x