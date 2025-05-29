# Results vs. base

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.011x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 152 ms                                                                 | 149 ms: 1.01x faster                                                      |
| docutils       | 1.37 sec                                                               | 1.36 sec: 1.00x faster                                                    |
| html5lib       | 29.0 ms                                                                | 28.1 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| coroutines                       | 14.8 ms                                                                | 14.2 ms: 1.05x faster                                                     |
| async_tree_eager                 | 56.1 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 344 ms                                                                 | 343 ms: 1.00x faster                                                      |
| async_tree_eager_cpu_io_mixed_tg | 376 ms                                                                 | 379 ms: 1.01x slower                                                      |
| async_generators                 | 240 ms                                                                 | 249 ms: 1.04x slower                                                      |
| Geometric mean                   | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (14): async_tree_none, async_tree_eager_memoization, async_tree_io, async_tree_cpu_io_mixed, asyncio_websockets, async_tree_cpu_io_mixed_tg, async_tree_memoization, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_eager_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 42.8 ms                                                                | 41.0 ms: 1.05x faster                                                     |
| nbody          | 71.8 ms                                                                | 69.0 ms: 1.04x faster                                                     |
| pidigits       | 280 ms                                                                 | 280 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 148 ms                                                                 | 148 ms: 1.00x faster                                                      |
| regex_v8       | 16.7 ms                                                                | 16.7 ms: 1.00x faster                                                     |
| regex_effbot   | 2.37 ms                                                                | 2.39 ms: 1.01x slower                                                     |
| regex_compile  | 61.7 ms                                                                | 63.9 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 186 us                                                                 | 180 us: 1.03x faster                                                      |
| xml_etree_iterparse  | 70.4 ms                                                                | 68.8 ms: 1.02x faster                                                     |
| tomli_loads          | 1.15 sec                                                               | 1.14 sec: 1.02x faster                                                    |
| xml_etree_parse      | 105 ms                                                                 | 104 ms: 1.02x faster                                                      |
| unpickle_pure_python | 130 us                                                                 | 128 us: 1.01x faster                                                      |
| json_dumps           | 7.18 ms                                                                | 7.15 ms: 1.00x faster                                                     |
| xml_etree_process    | 34.5 ms                                                                | 35.4 ms: 1.03x slower                                                     |
| xml_etree_generate   | 48.7 ms                                                                | 50.9 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.1 ms                                                                | 19.2 ms: 1.00x slower                                                     |
| python_startup_no_site | 14.8 ms                                                                | 14.9 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 19.3 ms                                                                | 18.8 ms: 1.02x faster                                                     |
| mako            | 7.32 ms                                                                | 8.36 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20250403-darwin-arm64-python-275056a7fdcbe36aaac4-3.14.0a6+-275056a | bm-20250408-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| crypto_pyaes                     | 49.4 ms                                                                | 44.8 ms: 1.10x faster                                                     |
| go                               | 70.8 ms                                                                | 66.0 ms: 1.07x faster                                                     |
| chaos                            | 35.5 ms                                                                | 33.1 ms: 1.07x faster                                                     |
| generators                       | 19.2 ms                                                                | 17.9 ms: 1.07x faster                                                     |
| deltablue                        | 2.05 ms                                                                | 1.92 ms: 1.07x faster                                                     |
| scimark_monte_carlo              | 39.4 ms                                                                | 36.9 ms: 1.07x faster                                                     |
| pyflate                          | 273 ms                                                                 | 257 ms: 1.06x faster                                                      |
| spectral_norm                    | 66.9 ms                                                                | 63.0 ms: 1.06x faster                                                     |
| scimark_fft                      | 194 ms                                                                 | 183 ms: 1.06x faster                                                      |
| logging_silent                   | 57.5 ns                                                                | 54.4 ns: 1.06x faster                                                     |
| sympy_integrate                  | 10.2 ms                                                                | 9.67 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult          | 3.20 ms                                                                | 3.05 ms: 1.05x faster                                                     |
| raytrace                         | 157 ms                                                                 | 150 ms: 1.05x faster                                                      |
| nqueens                          | 52.8 ms                                                                | 50.4 ms: 1.05x faster                                                     |
| float                            | 42.8 ms                                                                | 41.0 ms: 1.05x faster                                                     |
| coroutines                       | 14.8 ms                                                                | 14.2 ms: 1.05x faster                                                     |
| nbody                            | 71.8 ms                                                                | 69.0 ms: 1.04x faster                                                     |
| fannkuch                         | 249 ms                                                                 | 240 ms: 1.04x faster                                                      |
| richards_super                   | 33.0 ms                                                                | 31.9 ms: 1.04x faster                                                     |
| pickle_pure_python               | 186 us                                                                 | 180 us: 1.03x faster                                                      |
| scimark_sor                      | 75.1 ms                                                                | 72.7 ms: 1.03x faster                                                     |
| hexiom                           | 3.80 ms                                                                | 3.68 ms: 1.03x faster                                                     |
| comprehensions                   | 10.1 us                                                                | 9.78 us: 1.03x faster                                                     |
| html5lib                         | 29.0 ms                                                                | 28.1 ms: 1.03x faster                                                     |
| bpe_tokeniser                    | 2.80 sec                                                               | 2.72 sec: 1.03x faster                                                    |
| sqlglot_v2_parse                 | 691 us                                                                 | 672 us: 1.03x faster                                                      |
| sqlglot_v2_transpile             | 839 us                                                                 | 817 us: 1.03x faster                                                      |
| mdp                              | 691 ms                                                                 | 675 ms: 1.02x faster                                                      |
| django_template                  | 19.3 ms                                                                | 18.8 ms: 1.02x faster                                                     |
| xml_etree_iterparse              | 70.4 ms                                                                | 68.8 ms: 1.02x faster                                                     |
| richards                         | 29.3 ms                                                                | 28.7 ms: 1.02x faster                                                     |
| dulwich_log                      | 23.5 ms                                                                | 23.1 ms: 1.02x faster                                                     |
| pycparser                        | 625 ms                                                                 | 613 ms: 1.02x faster                                                      |
| sympy_str                        | 131 ms                                                                 | 128 ms: 1.02x faster                                                      |
| meteor_contest                   | 70.1 ms                                                                | 68.8 ms: 1.02x faster                                                     |
| sqlalchemy_declarative           | 55.4 ms                                                                | 54.4 ms: 1.02x faster                                                     |
| tomli_loads                      | 1.15 sec                                                               | 1.14 sec: 1.02x faster                                                    |
| xml_etree_parse                  | 105 ms                                                                 | 104 ms: 1.02x faster                                                      |
| async_tree_eager                 | 56.1 ms                                                                | 55.3 ms: 1.01x faster                                                     |
| sympy_expand                     | 220 ms                                                                 | 217 ms: 1.01x faster                                                      |
| 2to3                             | 152 ms                                                                 | 149 ms: 1.01x faster                                                      |
| unpickle_pure_python             | 130 us                                                                 | 128 us: 1.01x faster                                                      |
| sqlalchemy_imperative            | 6.21 ms                                                                | 6.13 ms: 1.01x faster                                                     |
| subparsers                       | 11.6 ms                                                                | 11.4 ms: 1.01x faster                                                     |
| coverage                         | 45.0 ms                                                                | 44.6 ms: 1.01x faster                                                     |
| many_optionals                   | 420 us                                                                 | 417 us: 1.01x faster                                                      |
| docutils                         | 1.37 sec                                                               | 1.36 sec: 1.00x faster                                                    |
| json_dumps                       | 7.18 ms                                                                | 7.15 ms: 1.00x faster                                                     |
| bench_mp_pool                    | 60.1 ms                                                                | 59.8 ms: 1.00x faster                                                     |
| async_tree_eager_cpu_io_mixed    | 344 ms                                                                 | 343 ms: 1.00x faster                                                      |
| scimark_lu                       | 69.4 ms                                                                | 69.2 ms: 1.00x faster                                                     |
| sqlglot_v2_optimize              | 30.6 ms                                                                | 30.5 ms: 1.00x faster                                                     |
| regex_dna                        | 148 ms                                                                 | 148 ms: 1.00x faster                                                      |
| regex_v8                         | 16.7 ms                                                                | 16.7 ms: 1.00x faster                                                     |
| pidigits                         | 280 ms                                                                 | 280 ms: 1.00x faster                                                      |
| create_gc_cycles                 | 1.27 ms                                                                | 1.27 ms: 1.00x slower                                                     |
| bench_thread_pool                | 462 us                                                                 | 464 us: 1.00x slower                                                      |
| python_startup                   | 19.1 ms                                                                | 19.2 ms: 1.00x slower                                                     |
| gc_traversal                     | 3.08 ms                                                                | 3.10 ms: 1.00x slower                                                     |
| pprint_safe_repr                 | 467 ms                                                                 | 469 ms: 1.01x slower                                                      |
| python_startup_no_site           | 14.8 ms                                                                | 14.9 ms: 1.01x slower                                                     |
| telco                            | 4.51 ms                                                                | 4.53 ms: 1.01x slower                                                     |
| connected_components             | 300 ms                                                                 | 302 ms: 1.01x slower                                                      |
| pathlib                          | 23.1 ms                                                                | 23.2 ms: 1.01x slower                                                     |
| shortest_path                    | 325 ms                                                                 | 328 ms: 1.01x slower                                                      |
| async_tree_eager_cpu_io_mixed_tg | 376 ms                                                                 | 379 ms: 1.01x slower                                                      |
| pprint_pformat                   | 939 ms                                                                 | 946 ms: 1.01x slower                                                      |
| regex_effbot                     | 2.37 ms                                                                | 2.39 ms: 1.01x slower                                                     |
| sqlglot_v2_normalize             | 61.9 ms                                                                | 62.6 ms: 1.01x slower                                                     |
| typing_runtime_protocols         | 86.3 us                                                                | 87.3 us: 1.01x slower                                                     |
| deepcopy                         | 142 us                                                                 | 144 us: 1.01x slower                                                      |
| xml_etree_process                | 34.5 ms                                                                | 35.4 ms: 1.03x slower                                                     |
| regex_compile                    | 61.7 ms                                                                | 63.9 ms: 1.03x slower                                                     |
| async_generators                 | 240 ms                                                                 | 249 ms: 1.04x slower                                                      |
| xml_etree_generate               | 48.7 ms                                                                | 50.9 ms: 1.05x slower                                                     |
| mako                             | 7.32 ms                                                                | 8.36 ms: 1.14x slower                                                     |
| deepcopy_memo                    | 16.1 us                                                                | 18.5 us: 1.15x slower                                                     |
| Geometric mean                   | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (26): pylint, k_core, async_tree_none, async_tree_eager_memoization, async_tree_io, async_tree_cpu_io_mixed, sphinx, sympy_sum, logging_simple, logging_format, genshi_text, genshi_xml, asyncio_websockets, async_tree_cpu_io_mixed_tg, json_loads, async_tree_memoization, sqlite_synth, deepcopy_reduce, async_tree_io_tg, async_tree_eager_memoization_tg, async_tree_eager_io_tg, async_tree_eager_tg, async_tree_none_tg, async_tree_memoization_tg, json, async_tree_eager_io

- Geometric mean (including insignificant results): 1.011x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x