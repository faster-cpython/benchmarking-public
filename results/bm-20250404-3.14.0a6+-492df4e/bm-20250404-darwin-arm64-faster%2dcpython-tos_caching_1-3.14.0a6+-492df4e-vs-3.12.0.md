# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.041x slower
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 186 ms: 1.10x slower                                                      |
| docutils       | 1.45 sec                                               | 1.56 sec: 1.07x slower                                                    |
| html5lib       | 33.4 ms                                                | 35.4 ms: 1.06x slower                                                     |
| sphinx         | 613 ms                                                 | 634 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 413 ms: 1.61x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 430 ms: 1.56x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 411 ms: 1.50x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.47x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 187 ms: 1.41x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                                      |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                      |
| coroutines                       | 19.7 ms                                                | 19.6 ms: 1.01x faster                                                     |
| async_tree_eager                 | 65.8 ms                                                | 75.3 ms: 1.14x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                      |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 186 ms: 1.31x slower                                                      |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.13x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                      |
| float          | 54.1 ms                                                | 55.7 ms: 1.03x slower                                                     |
| nbody          | 67.6 ms                                                | 85.9 ms: 1.27x slower                                                     |
| Geometric mean | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                     |
| regex_dna      | 143 ms                                                 | 140 ms: 1.02x faster                                                      |
| regex_v8       | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                     |
| regex_compile  | 75.9 ms                                                | 85.0 ms: 1.12x slower                                                     |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| xml_etree_iterparse  | 75.5 ms                                                | 77.7 ms: 1.03x slower                                                     |
| json_loads           | 17.0 us                                                | 17.8 us: 1.05x slower                                                     |
| xml_etree_generate   | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                     |
| tomli_loads          | 1.36 sec                                               | 1.57 sec: 1.16x slower                                                    |
| xml_etree_process    | 38.9 ms                                                | 45.2 ms: 1.16x slower                                                     |
| pickle_pure_python   | 197 us                                                 | 241 us: 1.22x slower                                                      |
| json_dumps           | 6.19 ms                                                | 7.70 ms: 1.25x slower                                                     |
| unpickle_pure_python | 145 us                                                 | 184 us: 1.26x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                     |
| python_startup_no_site | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.23 ms: 1.11x slower                                                     |
| genshi_xml      | 30.5 ms                                                | 36.1 ms: 1.19x slower                                                     |
| genshi_text     | 14.7 ms                                                | 18.0 ms: 1.23x slower                                                     |
| django_template | 19.7 ms                                                | 24.7 ms: 1.25x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.19x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 13.6 ms: 2.36x faster                                                     |
| mdp                              | 1.49 sec                                               | 896 ms: 1.67x faster                                                      |
| async_tree_io_tg                 | 673 ms                                                 | 405 ms: 1.66x faster                                                      |
| async_tree_eager_io              | 666 ms                                                 | 413 ms: 1.61x faster                                                      |
| async_tree_io                    | 672 ms                                                 | 430 ms: 1.56x faster                                                      |
| async_tree_memoization_tg        | 318 ms                                                 | 212 ms: 1.50x faster                                                      |
| async_tree_eager_io_tg           | 617 ms                                                 | 411 ms: 1.50x faster                                                      |
| async_tree_none_tg               | 255 ms                                                 | 173 ms: 1.47x faster                                                      |
| async_tree_none                  | 263 ms                                                 | 187 ms: 1.41x faster                                                      |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                      |
| deepcopy                         | 226 us                                                 | 181 us: 1.25x faster                                                      |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 424 ms: 1.25x faster                                                      |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 434 ms: 1.21x faster                                                      |
| generators                       | 29.4 ms                                                | 25.4 ms: 1.16x faster                                                     |
| async_generators                 | 299 ms                                                 | 270 ms: 1.11x faster                                                      |
| async_tree_eager_memoization     | 168 ms                                                 | 152 ms: 1.10x faster                                                      |
| regex_effbot                     | 2.44 ms                                                | 2.24 ms: 1.09x faster                                                     |
| deepcopy_reduce                  | 2.01 us                                                | 1.88 us: 1.07x faster                                                     |
| dulwich_log                      | 29.2 ms                                                | 27.3 ms: 1.07x faster                                                     |
| k_core                           | 1.72 sec                                               | 1.61 sec: 1.07x faster                                                    |
| deepcopy_memo                    | 26.0 us                                                | 24.4 us: 1.07x faster                                                     |
| bench_mp_pool                    | 65.5 ms                                                | 61.7 ms: 1.06x faster                                                     |
| xml_etree_parse                  | 108 ms                                                 | 105 ms: 1.03x faster                                                      |
| regex_dna                        | 143 ms                                                 | 140 ms: 1.02x faster                                                      |
| async_tree_eager_cpu_io_mixed    | 374 ms                                                 | 370 ms: 1.01x faster                                                      |
| pathlib                          | 24.7 ms                                                | 24.5 ms: 1.01x faster                                                     |
| coroutines                       | 19.7 ms                                                | 19.6 ms: 1.01x faster                                                     |
| bpe_tokeniser                    | 3.28 sec                                               | 3.27 sec: 1.00x faster                                                    |
| raytrace                         | 204 ms                                                 | 204 ms: 1.00x faster                                                      |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                      |
| sqlite_synth                     | 1.55 us                                                | 1.56 us: 1.01x slower                                                     |
| json                             | 3.00 ms                                                | 3.07 ms: 1.02x slower                                                     |
| xml_etree_iterparse              | 75.5 ms                                                | 77.7 ms: 1.03x slower                                                     |
| float                            | 54.1 ms                                                | 55.7 ms: 1.03x slower                                                     |
| logging_silent                   | 72.5 ns                                                | 74.8 ns: 1.03x slower                                                     |
| sphinx                           | 613 ms                                                 | 634 ms: 1.03x slower                                                      |
| regex_v8                         | 15.1 ms                                                | 15.7 ms: 1.04x slower                                                     |
| json_loads                       | 17.0 us                                                | 17.8 us: 1.05x slower                                                     |
| comprehensions                   | 14.0 us                                                | 14.7 us: 1.05x slower                                                     |
| gc_traversal                     | 2.95 ms                                                | 3.11 ms: 1.06x slower                                                     |
| html5lib                         | 33.4 ms                                                | 35.4 ms: 1.06x slower                                                     |
| sqlalchemy_declarative           | 61.9 ms                                                | 66.1 ms: 1.07x slower                                                     |
| docutils                         | 1.45 sec                                               | 1.56 sec: 1.07x slower                                                    |
| go                               | 98.5 ms                                                | 106 ms: 1.08x slower                                                      |
| sympy_integrate                  | 11.1 ms                                                | 12.1 ms: 1.09x slower                                                     |
| python_startup                   | 17.8 ms                                                | 19.4 ms: 1.09x slower                                                     |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.45 ms: 1.10x slower                                                     |
| shortest_path                    | 331 ms                                                 | 363 ms: 1.10x slower                                                      |
| 2to3                             | 168 ms                                                 | 186 ms: 1.10x slower                                                      |
| sympy_sum                        | 76.2 ms                                                | 84.2 ms: 1.10x slower                                                     |
| mako                             | 7.44 ms                                                | 8.23 ms: 1.11x slower                                                     |
| spectral_norm                    | 76.5 ms                                                | 84.6 ms: 1.11x slower                                                     |
| xml_etree_generate               | 55.4 ms                                                | 61.4 ms: 1.11x slower                                                     |
| create_gc_cycles                 | 1.15 ms                                                | 1.28 ms: 1.11x slower                                                     |
| scimark_fft                      | 194 ms                                                 | 216 ms: 1.11x slower                                                      |
| logging_format                   | 3.90 us                                                | 4.36 us: 1.12x slower                                                     |
| bench_thread_pool                | 483 us                                                 | 540 us: 1.12x slower                                                      |
| logging_simple                   | 3.60 us                                                | 4.03 us: 1.12x slower                                                     |
| regex_compile                    | 75.9 ms                                                | 85.0 ms: 1.12x slower                                                     |
| pycparser                        | 673 ms                                                 | 755 ms: 1.12x slower                                                      |
| sympy_str                        | 144 ms                                                 | 162 ms: 1.12x slower                                                      |
| meteor_contest                   | 69.1 ms                                                | 78.0 ms: 1.13x slower                                                     |
| python_startup_no_site           | 13.2 ms                                                | 14.9 ms: 1.13x slower                                                     |
| deltablue                        | 2.57 ms                                                | 2.91 ms: 1.13x slower                                                     |
| connected_components             | 300 ms                                                 | 339 ms: 1.13x slower                                                      |
| scimark_sor                      | 85.8 ms                                                | 97.7 ms: 1.14x slower                                                     |
| pyflate                          | 311 ms                                                 | 356 ms: 1.14x slower                                                      |
| async_tree_eager                 | 65.8 ms                                                | 75.3 ms: 1.14x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 402 ms: 1.16x slower                                                      |
| tomli_loads                      | 1.36 sec                                               | 1.57 sec: 1.16x slower                                                    |
| sympy_expand                     | 233 ms                                                 | 271 ms: 1.16x slower                                                      |
| xml_etree_process                | 38.9 ms                                                | 45.2 ms: 1.16x slower                                                     |
| sqlalchemy_imperative            | 6.60 ms                                                | 7.77 ms: 1.18x slower                                                     |
| genshi_xml                       | 30.5 ms                                                | 36.1 ms: 1.19x slower                                                     |
| crypto_pyaes                     | 51.4 ms                                                | 61.3 ms: 1.19x slower                                                     |
| chaos                            | 41.6 ms                                                | 49.8 ms: 1.20x slower                                                     |
| pprint_pformat                   | 986 ms                                                 | 1.19 sec: 1.20x slower                                                    |
| many_optionals                   | 403 us                                                 | 486 us: 1.21x slower                                                      |
| pprint_safe_repr                 | 483 ms                                                 | 587 ms: 1.22x slower                                                      |
| typing_runtime_protocols         | 91.5 us                                                | 111 us: 1.22x slower                                                      |
| telco                            | 3.92 ms                                                | 4.77 ms: 1.22x slower                                                     |
| nqueens                          | 59.5 ms                                                | 72.5 ms: 1.22x slower                                                     |
| scimark_lu                       | 73.5 ms                                                | 89.5 ms: 1.22x slower                                                     |
| pickle_pure_python               | 197 us                                                 | 241 us: 1.22x slower                                                      |
| genshi_text                      | 14.7 ms                                                | 18.0 ms: 1.23x slower                                                     |
| json_dumps                       | 6.19 ms                                                | 7.70 ms: 1.25x slower                                                     |
| fannkuch                         | 250 ms                                                 | 312 ms: 1.25x slower                                                      |
| coverage                         | 38.5 ms                                                | 48.3 ms: 1.25x slower                                                     |
| django_template                  | 19.7 ms                                                | 24.7 ms: 1.25x slower                                                     |
| unpickle_pure_python             | 145 us                                                 | 184 us: 1.26x slower                                                      |
| nbody                            | 67.6 ms                                                | 85.9 ms: 1.27x slower                                                     |
| hexiom                           | 4.38 ms                                                | 5.60 ms: 1.28x slower                                                     |
| scimark_monte_carlo              | 44.5 ms                                                | 57.3 ms: 1.29x slower                                                     |
| richards_super                   | 34.6 ms                                                | 44.7 ms: 1.29x slower                                                     |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 186 ms: 1.31x slower                                                      |
| richards                         | 30.6 ms                                                | 40.5 ms: 1.32x slower                                                     |
| async_tree_eager_tg              | 46.9 ms                                                | 143 ms: 3.05x slower                                                      |
| Geometric mean                   | (ref)                                                  | 1.04x slower                                                              |

Benchmark hidden because not significant (2): pylint, asyncio_websockets
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, dask, djangocms, gevent_hub, gunicorn, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (4) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.59% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x