# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.083x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 169 ms                                                                 | 186 ms: 1.10x slower                                                      |
| docutils       | 1.46 sec                                                               | 1.56 sec: 1.07x slower                                                    |
| html5lib       | 31.5 ms                                                                | 35.3 ms: 1.12x slower                                                     |
| sphinx         | 591 ms                                                                 | 636 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.09x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager_cpu_io_mixed_tg | 390 ms                                                                 | 402 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 410 ms                                                                 | 424 ms: 1.03x slower                                                      |
| async_generators                 | 261 ms                                                                 | 270 ms: 1.03x slower                                                      |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                 | 370 ms: 1.04x slower                                                      |
| async_tree_cpu_io_mixed          | 412 ms                                                                 | 432 ms: 1.05x slower                                                      |
| async_tree_eager_tg              | 134 ms                                                                 | 144 ms: 1.07x slower                                                      |
| async_tree_eager_memoization_tg  | 173 ms                                                                 | 187 ms: 1.08x slower                                                      |
| async_tree_eager_io_tg           | 381 ms                                                                 | 412 ms: 1.08x slower                                                      |
| async_tree_io_tg                 | 375 ms                                                                 | 406 ms: 1.08x slower                                                      |
| async_tree_eager_memoization     | 140 ms                                                                 | 153 ms: 1.09x slower                                                      |
| async_tree_none_tg               | 159 ms                                                                 | 173 ms: 1.09x slower                                                      |
| async_tree_memoization_tg        | 194 ms                                                                 | 213 ms: 1.09x slower                                                      |
| async_tree_io                    | 390 ms                                                                 | 430 ms: 1.10x slower                                                      |
| async_tree_eager_io              | 373 ms                                                                 | 414 ms: 1.11x slower                                                      |
| async_tree_none                  | 167 ms                                                                 | 186 ms: 1.11x slower                                                      |
| async_tree_memoization           | 198 ms                                                                 | 222 ms: 1.12x slower                                                      |
| coroutines                       | 17.3 ms                                                                | 19.5 ms: 1.13x slower                                                     |
| async_tree_eager                 | 65.0 ms                                                                | 75.0 ms: 1.16x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.08x slower                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 283 ms                                                                 | 284 ms: 1.00x slower                                                      |
| float          | 49.5 ms                                                                | 55.7 ms: 1.13x slower                                                     |
| nbody          | 75.7 ms                                                                | 86.0 ms: 1.14x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.09x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                                | 15.9 ms: 1.02x faster                                                     |
| regex_dna      | 141 ms                                                                 | 141 ms: 1.00x faster                                                      |
| regex_compile  | 73.2 ms                                                                | 85.2 ms: 1.16x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 17.7 us                                                                | 17.8 us: 1.01x slower                                                     |
| xml_etree_parse      | 104 ms                                                                 | 105 ms: 1.01x slower                                                      |
| json_dumps           | 7.43 ms                                                                | 7.72 ms: 1.04x slower                                                     |
| xml_etree_iterparse  | 73.6 ms                                                                | 77.5 ms: 1.05x slower                                                     |
| pickle_pure_python   | 220 us                                                                 | 241 us: 1.09x slower                                                      |
| xml_etree_generate   | 55.9 ms                                                                | 61.4 ms: 1.10x slower                                                     |
| unpickle_pure_python | 162 us                                                                 | 183 us: 1.13x slower                                                      |
| xml_etree_process    | 39.9 ms                                                                | 45.3 ms: 1.14x slower                                                     |
| tomli_loads          | 1.34 sec                                                               | 1.57 sec: 1.17x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.08x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 14.9 ms                                                                | 15.0 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 7.87 ms                                                                | 8.26 ms: 1.05x slower                                                     |
| django_template | 22.2 ms                                                                | 24.6 ms: 1.11x slower                                                     |
| genshi_xml      | 30.8 ms                                                                | 36.3 ms: 1.18x slower                                                     |
| genshi_text     | 14.9 ms                                                                | 17.9 ms: 1.20x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.13x slower                                                              |

All benchmarks:
===============

| Benchmark                        | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8                         | 16.1 ms                                                                | 15.9 ms: 1.02x faster                                                     |
| gc_traversal                     | 3.11 ms                                                                | 3.10 ms: 1.00x faster                                                     |
| regex_dna                        | 141 ms                                                                 | 141 ms: 1.00x faster                                                      |
| pidigits                         | 283 ms                                                                 | 284 ms: 1.00x slower                                                      |
| python_startup_no_site           | 14.9 ms                                                                | 15.0 ms: 1.01x slower                                                     |
| sqlite_synth                     | 1.55 us                                                                | 1.56 us: 1.01x slower                                                     |
| json                             | 3.04 ms                                                                | 3.06 ms: 1.01x slower                                                     |
| json_loads                       | 17.7 us                                                                | 17.8 us: 1.01x slower                                                     |
| create_gc_cycles                 | 1.27 ms                                                                | 1.28 ms: 1.01x slower                                                     |
| bench_mp_pool                    | 61.2 ms                                                                | 61.8 ms: 1.01x slower                                                     |
| xml_etree_parse                  | 104 ms                                                                 | 105 ms: 1.01x slower                                                      |
| telco                            | 4.68 ms                                                                | 4.79 ms: 1.02x slower                                                     |
| pathlib                          | 23.8 ms                                                                | 24.4 ms: 1.02x slower                                                     |
| async_tree_eager_cpu_io_mixed_tg | 390 ms                                                                 | 402 ms: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg       | 410 ms                                                                 | 424 ms: 1.03x slower                                                      |
| meteor_contest                   | 75.7 ms                                                                | 78.2 ms: 1.03x slower                                                     |
| async_generators                 | 261 ms                                                                 | 270 ms: 1.03x slower                                                      |
| coverage                         | 46.4 ms                                                                | 48.1 ms: 1.04x slower                                                     |
| async_tree_eager_cpu_io_mixed    | 357 ms                                                                 | 370 ms: 1.04x slower                                                      |
| json_dumps                       | 7.43 ms                                                                | 7.72 ms: 1.04x slower                                                     |
| k_core                           | 1.54 sec                                                               | 1.61 sec: 1.05x slower                                                    |
| generators                       | 24.3 ms                                                                | 25.5 ms: 1.05x slower                                                     |
| async_tree_cpu_io_mixed          | 412 ms                                                                 | 432 ms: 1.05x slower                                                      |
| mako                             | 7.87 ms                                                                | 8.26 ms: 1.05x slower                                                     |
| bpe_tokeniser                    | 3.12 sec                                                               | 3.28 sec: 1.05x slower                                                    |
| xml_etree_iterparse              | 73.6 ms                                                                | 77.5 ms: 1.05x slower                                                     |
| connected_components             | 320 ms                                                                 | 339 ms: 1.06x slower                                                      |
| pylint                           | 166 ms                                                                 | 176 ms: 1.06x slower                                                      |
| crypto_pyaes                     | 57.5 ms                                                                | 61.1 ms: 1.06x slower                                                     |
| sympy_integrate                  | 11.4 ms                                                                | 12.1 ms: 1.06x slower                                                     |
| many_optionals                   | 456 us                                                                 | 485 us: 1.06x slower                                                      |
| shortest_path                    | 341 ms                                                                 | 364 ms: 1.07x slower                                                      |
| docutils                         | 1.46 sec                                                               | 1.56 sec: 1.07x slower                                                    |
| bench_thread_pool                | 505 us                                                                 | 540 us: 1.07x slower                                                      |
| subparsers                       | 12.6 ms                                                                | 13.5 ms: 1.07x slower                                                     |
| async_tree_eager_tg              | 134 ms                                                                 | 144 ms: 1.07x slower                                                      |
| sphinx                           | 591 ms                                                                 | 636 ms: 1.07x slower                                                      |
| dulwich_log                      | 25.3 ms                                                                | 27.2 ms: 1.08x slower                                                     |
| scimark_sparse_mat_mult          | 3.20 ms                                                                | 3.45 ms: 1.08x slower                                                     |
| async_tree_eager_memoization_tg  | 173 ms                                                                 | 187 ms: 1.08x slower                                                      |
| sqlalchemy_declarative           | 61.2 ms                                                                | 66.1 ms: 1.08x slower                                                     |
| sympy_sum                        | 77.6 ms                                                                | 83.9 ms: 1.08x slower                                                     |
| async_tree_eager_io_tg           | 381 ms                                                                 | 412 ms: 1.08x slower                                                      |
| logging_silent                   | 69.0 ns                                                                | 74.7 ns: 1.08x slower                                                     |
| async_tree_io_tg                 | 375 ms                                                                 | 406 ms: 1.08x slower                                                      |
| sympy_expand                     | 248 ms                                                                 | 271 ms: 1.09x slower                                                      |
| async_tree_eager_memoization     | 140 ms                                                                 | 153 ms: 1.09x slower                                                      |
| async_tree_none_tg               | 159 ms                                                                 | 173 ms: 1.09x slower                                                      |
| async_tree_memoization_tg        | 194 ms                                                                 | 213 ms: 1.09x slower                                                      |
| pickle_pure_python               | 220 us                                                                 | 241 us: 1.09x slower                                                      |
| sympy_str                        | 148 ms                                                                 | 162 ms: 1.10x slower                                                      |
| fannkuch                         | 284 ms                                                                 | 312 ms: 1.10x slower                                                      |
| xml_etree_generate               | 55.9 ms                                                                | 61.4 ms: 1.10x slower                                                     |
| sqlglot_v2_optimize              | 34.6 ms                                                                | 38.1 ms: 1.10x slower                                                     |
| 2to3                             | 169 ms                                                                 | 186 ms: 1.10x slower                                                      |
| scimark_lu                       | 81.4 ms                                                                | 89.7 ms: 1.10x slower                                                     |
| async_tree_io                    | 390 ms                                                                 | 430 ms: 1.10x slower                                                      |
| scimark_sor                      | 88.6 ms                                                                | 97.7 ms: 1.10x slower                                                     |
| pycparser                        | 682 ms                                                                 | 753 ms: 1.10x slower                                                      |
| richards                         | 36.5 ms                                                                | 40.4 ms: 1.11x slower                                                     |
| richards_super                   | 40.5 ms                                                                | 44.9 ms: 1.11x slower                                                     |
| sqlglot_v2_normalize             | 70.7 ms                                                                | 78.4 ms: 1.11x slower                                                     |
| async_tree_eager_io              | 373 ms                                                                 | 414 ms: 1.11x slower                                                      |
| django_template                  | 22.2 ms                                                                | 24.6 ms: 1.11x slower                                                     |
| async_tree_none                  | 167 ms                                                                 | 186 ms: 1.11x slower                                                      |
| scimark_fft                      | 194 ms                                                                 | 216 ms: 1.12x slower                                                      |
| async_tree_memoization           | 198 ms                                                                 | 222 ms: 1.12x slower                                                      |
| html5lib                         | 31.5 ms                                                                | 35.3 ms: 1.12x slower                                                     |
| pyflate                          | 318 ms                                                                 | 356 ms: 1.12x slower                                                      |
| deepcopy_reduce                  | 1.67 us                                                                | 1.88 us: 1.12x slower                                                     |
| float                            | 49.5 ms                                                                | 55.7 ms: 1.13x slower                                                     |
| coroutines                       | 17.3 ms                                                                | 19.5 ms: 1.13x slower                                                     |
| nqueens                          | 64.0 ms                                                                | 72.4 ms: 1.13x slower                                                     |
| unpickle_pure_python             | 162 us                                                                 | 183 us: 1.13x slower                                                      |
| deepcopy                         | 159 us                                                                 | 180 us: 1.13x slower                                                      |
| deltablue                        | 2.56 ms                                                                | 2.90 ms: 1.14x slower                                                     |
| nbody                            | 75.7 ms                                                                | 86.0 ms: 1.14x slower                                                     |
| xml_etree_process                | 39.9 ms                                                                | 45.3 ms: 1.14x slower                                                     |
| typing_runtime_protocols         | 98.3 us                                                                | 112 us: 1.14x slower                                                      |
| sqlalchemy_imperative            | 6.85 ms                                                                | 7.80 ms: 1.14x slower                                                     |
| raytrace                         | 179 ms                                                                 | 204 ms: 1.14x slower                                                      |
| pprint_pformat                   | 1.04 sec                                                               | 1.18 sec: 1.14x slower                                                    |
| pprint_safe_repr                 | 514 ms                                                                 | 587 ms: 1.14x slower                                                      |
| mdp                              | 785 ms                                                                 | 898 ms: 1.14x slower                                                      |
| async_tree_eager                 | 65.0 ms                                                                | 75.0 ms: 1.16x slower                                                     |
| hexiom                           | 4.84 ms                                                                | 5.60 ms: 1.16x slower                                                     |
| sqlglot_v2_transpile             | 1.01 ms                                                                | 1.17 ms: 1.16x slower                                                     |
| logging_format                   | 3.77 us                                                                | 4.38 us: 1.16x slower                                                     |
| comprehensions                   | 12.6 us                                                                | 14.6 us: 1.16x slower                                                     |
| regex_compile                    | 73.2 ms                                                                | 85.2 ms: 1.16x slower                                                     |
| tomli_loads                      | 1.34 sec                                                               | 1.57 sec: 1.17x slower                                                    |
| logging_simple                   | 3.45 us                                                                | 4.04 us: 1.17x slower                                                     |
| genshi_xml                       | 30.8 ms                                                                | 36.3 ms: 1.18x slower                                                     |
| spectral_norm                    | 71.5 ms                                                                | 84.6 ms: 1.18x slower                                                     |
| sqlglot_v2_parse                 | 836 us                                                                 | 989 us: 1.18x slower                                                      |
| go                               | 88.7 ms                                                                | 106 ms: 1.20x slower                                                      |
| genshi_text                      | 14.9 ms                                                                | 17.9 ms: 1.20x slower                                                     |
| chaos                            | 40.9 ms                                                                | 49.8 ms: 1.22x slower                                                     |
| scimark_monte_carlo              | 46.4 ms                                                                | 57.4 ms: 1.24x slower                                                     |
| deepcopy_memo                    | 19.3 us                                                                | 24.4 us: 1.27x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.09x slower                                                              |

Benchmark hidden because not significant (3): asyncio_websockets, python_startup, regex_effbot

- Geometric mean (including insignificant results): 1.083x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.07x
- 95% likely to have a slowdown of 1.07x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 0.99x