# Results vs. 3.12.0

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.045x slower
- HPT reliability: 99.93%
- HPT 99th percentile: 1.01x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 168 ms                                                 | 190 ms: 1.13x slower                                                          |
| docutils       | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                        |
| html5lib       | 33.4 ms                                                | 34.8 ms: 1.04x slower                                                         |
| sphinx         | 613 ms                                                 | 635 ms: 1.04x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager_io              | 666 ms                                                 | 409 ms: 1.63x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 421 ms: 1.60x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 426 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 416 ms: 1.49x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 217 ms: 1.47x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 188 ms: 1.40x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 442 ms: 1.19x faster                                                          |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| async_generators                 | 299 ms                                                 | 292 ms: 1.02x faster                                                          |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| async_tree_eager                 | 65.8 ms                                                | 77.0 ms: 1.17x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.33x slower                                                          |
| async_tree_eager_tg              | 46.9 ms                                                | 146 ms: 3.12x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (2): async_tree_eager_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| float          | 54.1 ms                                                | 59.4 ms: 1.10x slower                                                         |
| nbody          | 67.6 ms                                                | 89.0 ms: 1.32x slower                                                         |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 2.44 ms                                                | 2.18 ms: 1.12x faster                                                         |
| regex_dna      | 143 ms                                                 | 138 ms: 1.03x faster                                                          |
| regex_v8       | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| regex_compile  | 75.9 ms                                                | 84.4 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 75.5 ms                                                | 76.8 ms: 1.02x slower                                                         |
| json_loads           | 17.0 us                                                | 18.5 us: 1.09x slower                                                         |
| tomli_loads          | 1.36 sec                                               | 1.49 sec: 1.10x slower                                                        |
| xml_etree_generate   | 55.4 ms                                                | 62.9 ms: 1.13x slower                                                         |
| xml_etree_process    | 38.9 ms                                                | 46.2 ms: 1.19x slower                                                         |
| json_dumps           | 6.19 ms                                                | 7.38 ms: 1.19x slower                                                         |
| unpickle_pure_python | 145 us                                                 | 179 us: 1.23x slower                                                          |
| pickle_pure_python   | 197 us                                                 | 244 us: 1.24x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                         |
| python_startup_no_site | 13.2 ms                                                | 14.3 ms: 1.09x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 7.44 ms                                                | 8.74 ms: 1.17x slower                                                         |
| genshi_xml      | 30.5 ms                                                | 37.6 ms: 1.23x slower                                                         |
| genshi_text     | 14.7 ms                                                | 18.4 ms: 1.26x slower                                                         |
| django_template | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.25x slower                                                                  |

All benchmarks:
===============

| Benchmark                        | bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| subparsers                       | 32.1 ms                                                | 15.4 ms: 2.09x faster                                                         |
| mdp                              | 1.49 sec                                               | 879 ms: 1.70x faster                                                          |
| async_tree_eager_io              | 666 ms                                                 | 409 ms: 1.63x faster                                                          |
| async_tree_io_tg                 | 673 ms                                                 | 421 ms: 1.60x faster                                                          |
| async_tree_io                    | 672 ms                                                 | 426 ms: 1.58x faster                                                          |
| async_tree_eager_io_tg           | 617 ms                                                 | 416 ms: 1.49x faster                                                          |
| async_tree_memoization_tg        | 318 ms                                                 | 217 ms: 1.47x faster                                                          |
| async_tree_none_tg               | 255 ms                                                 | 176 ms: 1.45x faster                                                          |
| async_tree_none                  | 263 ms                                                 | 188 ms: 1.40x faster                                                          |
| async_tree_memoization           | 310 ms                                                 | 222 ms: 1.40x faster                                                          |
| async_tree_cpu_io_mixed_tg       | 528 ms                                                 | 429 ms: 1.23x faster                                                          |
| deepcopy                         | 226 us                                                 | 185 us: 1.22x faster                                                          |
| async_tree_cpu_io_mixed          | 527 ms                                                 | 442 ms: 1.19x faster                                                          |
| deepcopy_memo                    | 26.0 us                                                | 22.5 us: 1.15x faster                                                         |
| regex_effbot                     | 2.44 ms                                                | 2.18 ms: 1.12x faster                                                         |
| k_core                           | 1.72 sec                                               | 1.57 sec: 1.10x faster                                                        |
| async_tree_eager_memoization     | 168 ms                                                 | 154 ms: 1.09x faster                                                          |
| dulwich_log                      | 29.2 ms                                                | 27.1 ms: 1.08x faster                                                         |
| regex_dna                        | 143 ms                                                 | 138 ms: 1.03x faster                                                          |
| async_generators                 | 299 ms                                                 | 292 ms: 1.02x faster                                                          |
| deepcopy_reduce                  | 2.01 us                                                | 1.98 us: 1.02x faster                                                         |
| pathlib                          | 24.7 ms                                                | 24.4 ms: 1.01x faster                                                         |
| dask                             | 779 ms                                                 | 772 ms: 1.01x faster                                                          |
| pidigits                         | 283 ms                                                 | 284 ms: 1.00x slower                                                          |
| raytrace                         | 204 ms                                                 | 207 ms: 1.02x slower                                                          |
| go                               | 98.5 ms                                                | 100 ms: 1.02x slower                                                          |
| xml_etree_iterparse              | 75.5 ms                                                | 76.8 ms: 1.02x slower                                                         |
| comprehensions                   | 14.0 us                                                | 14.2 us: 1.02x slower                                                         |
| coroutines                       | 19.7 ms                                                | 20.3 ms: 1.03x slower                                                         |
| sphinx                           | 613 ms                                                 | 635 ms: 1.04x slower                                                          |
| json                             | 3.00 ms                                                | 3.11 ms: 1.04x slower                                                         |
| spectral_norm                    | 76.5 ms                                                | 79.4 ms: 1.04x slower                                                         |
| shortest_path                    | 331 ms                                                 | 344 ms: 1.04x slower                                                          |
| html5lib                         | 33.4 ms                                                | 34.8 ms: 1.04x slower                                                         |
| regex_v8                         | 15.1 ms                                                | 15.8 ms: 1.05x slower                                                         |
| sympy_integrate                  | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                         |
| connected_components             | 300 ms                                                 | 316 ms: 1.05x slower                                                          |
| bpe_tokeniser                    | 3.28 sec                                               | 3.47 sec: 1.06x slower                                                        |
| python_startup                   | 17.8 ms                                                | 18.8 ms: 1.06x slower                                                         |
| scimark_sor                      | 85.8 ms                                                | 91.3 ms: 1.06x slower                                                         |
| scimark_sparse_mat_mult          | 3.14 ms                                                | 3.35 ms: 1.07x slower                                                         |
| generators                       | 29.4 ms                                                | 31.4 ms: 1.07x slower                                                         |
| sqlite_synth                     | 1.55 us                                                | 1.66 us: 1.07x slower                                                         |
| thrift                           | 468 us                                                 | 505 us: 1.08x slower                                                          |
| docutils                         | 1.45 sec                                               | 1.57 sec: 1.08x slower                                                        |
| deltablue                        | 2.57 ms                                                | 2.79 ms: 1.09x slower                                                         |
| python_startup_no_site           | 13.2 ms                                                | 14.3 ms: 1.09x slower                                                         |
| json_loads                       | 17.0 us                                                | 18.5 us: 1.09x slower                                                         |
| gc_traversal                     | 2.95 ms                                                | 3.22 ms: 1.09x slower                                                         |
| tomli_loads                      | 1.36 sec                                               | 1.49 sec: 1.10x slower                                                        |
| bench_mp_pool                    | 65.5 ms                                                | 71.8 ms: 1.10x slower                                                         |
| float                            | 54.1 ms                                                | 59.4 ms: 1.10x slower                                                         |
| sympy_sum                        | 76.2 ms                                                | 84.2 ms: 1.10x slower                                                         |
| regex_compile                    | 75.9 ms                                                | 84.4 ms: 1.11x slower                                                         |
| pycparser                        | 673 ms                                                 | 752 ms: 1.12x slower                                                          |
| bench_thread_pool                | 483 us                                                 | 539 us: 1.12x slower                                                          |
| scimark_fft                      | 194 ms                                                 | 218 ms: 1.12x slower                                                          |
| 2to3                             | 168 ms                                                 | 190 ms: 1.13x slower                                                          |
| sympy_str                        | 144 ms                                                 | 162 ms: 1.13x slower                                                          |
| chaos                            | 41.6 ms                                                | 47.1 ms: 1.13x slower                                                         |
| xml_etree_generate               | 55.4 ms                                                | 62.9 ms: 1.13x slower                                                         |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 405 ms: 1.17x slower                                                          |
| async_tree_eager                 | 65.8 ms                                                | 77.0 ms: 1.17x slower                                                         |
| mako                             | 7.44 ms                                                | 8.74 ms: 1.17x slower                                                         |
| logging_format                   | 3.90 us                                                | 4.58 us: 1.17x slower                                                         |
| scimark_monte_carlo              | 44.5 ms                                                | 52.3 ms: 1.18x slower                                                         |
| pprint_safe_repr                 | 483 ms                                                 | 570 ms: 1.18x slower                                                          |
| logging_simple                   | 3.60 us                                                | 4.26 us: 1.18x slower                                                         |
| pprint_pformat                   | 986 ms                                                 | 1.17 sec: 1.18x slower                                                        |
| create_gc_cycles                 | 1.15 ms                                                | 1.36 ms: 1.18x slower                                                         |
| hexiom                           | 4.38 ms                                                | 5.18 ms: 1.18x slower                                                         |
| sympy_expand                     | 233 ms                                                 | 277 ms: 1.19x slower                                                          |
| xml_etree_process                | 38.9 ms                                                | 46.2 ms: 1.19x slower                                                         |
| pyflate                          | 311 ms                                                 | 369 ms: 1.19x slower                                                          |
| json_dumps                       | 6.19 ms                                                | 7.38 ms: 1.19x slower                                                         |
| meteor_contest                   | 69.1 ms                                                | 82.8 ms: 1.20x slower                                                         |
| scimark_lu                       | 73.5 ms                                                | 88.6 ms: 1.21x slower                                                         |
| crypto_pyaes                     | 51.4 ms                                                | 62.7 ms: 1.22x slower                                                         |
| richards_super                   | 34.6 ms                                                | 42.2 ms: 1.22x slower                                                         |
| richards                         | 30.6 ms                                                | 37.4 ms: 1.22x slower                                                         |
| unpickle_pure_python             | 145 us                                                 | 179 us: 1.23x slower                                                          |
| genshi_xml                       | 30.5 ms                                                | 37.6 ms: 1.23x slower                                                         |
| nqueens                          | 59.5 ms                                                | 73.7 ms: 1.24x slower                                                         |
| pickle_pure_python               | 197 us                                                 | 244 us: 1.24x slower                                                          |
| typing_runtime_protocols         | 91.5 us                                                | 114 us: 1.25x slower                                                          |
| genshi_text                      | 14.7 ms                                                | 18.4 ms: 1.26x slower                                                         |
| many_optionals                   | 403 us                                                 | 508 us: 1.26x slower                                                          |
| fannkuch                         | 250 ms                                                 | 320 ms: 1.28x slower                                                          |
| nbody                            | 67.6 ms                                                | 89.0 ms: 1.32x slower                                                         |
| telco                            | 3.92 ms                                                | 5.19 ms: 1.32x slower                                                         |
| django_template                  | 19.7 ms                                                | 26.2 ms: 1.33x slower                                                         |
| async_tree_eager_memoization_tg  | 142 ms                                                 | 189 ms: 1.33x slower                                                          |
| coverage                         | 38.5 ms                                                | 54.0 ms: 1.40x slower                                                         |
| async_tree_eager_tg              | 46.9 ms                                                | 146 ms: 3.12x slower                                                          |
| logging_silent                   | 72.5 ns                                                | 359 ns: 4.95x slower                                                          |
| Geometric mean                   | (ref)                                                  | 1.06x slower                                                                  |

Benchmark hidden because not significant (4): pylint, async_tree_eager_cpu_io_mixed, asyncio_websockets, xml_etree_parse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-darwin-arm64-python-v3.12.0-3.12.0-0fb18b0.json: chameleon, djangocms, gevent_hub, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (4) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.045x slower

# HPT report

- Reliability score: 99.93% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 1.11x