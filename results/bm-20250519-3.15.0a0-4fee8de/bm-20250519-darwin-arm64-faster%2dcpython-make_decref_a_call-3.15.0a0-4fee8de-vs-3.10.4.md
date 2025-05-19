# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: 4fee8de
- commit date: 2025-05-19
- overall geometric mean: 1.209x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 190 ms: 1.06x faster                                                          |
| docutils       | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                        |
| html5lib       | 43.5 ms                                                | 34.8 ms: 1.25x faster                                                         |
| sphinx         | 729 ms                                                 | 635 ms: 1.15x faster                                                          |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.0 ms: 5.09x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 426 ms: 2.39x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                          |
| async_tree_none               | 391 ms                                                 | 188 ms: 2.08x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 442 ms: 1.51x faster                                                          |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                          |
| async_generators              | 233 ms                                                 | 292 ms: 1.25x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.86x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 59.4 ms: 1.22x faster                                                         |
| nbody          | 92.5 ms                                                | 89.0 ms: 1.04x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                          |
| regex_v8       | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| regex_compile  | 95.6 ms                                                | 84.4 ms: 1.13x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.18 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 244 us: 1.16x faster                                                          |
| tomli_loads          | 1.72 sec                                               | 1.49 sec: 1.16x faster                                                        |
| json_dumps           | 8.31 ms                                                | 7.38 ms: 1.12x faster                                                         |
| unpickle_pure_python | 198 us                                                 | 179 us: 1.11x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 76.8 ms: 1.03x slower                                                         |
| xml_etree_process    | 44.6 ms                                                | 46.2 ms: 1.03x slower                                                         |
| json_loads           | 16.6 us                                                | 18.5 us: 1.12x slower                                                         |
| xml_etree_generate   | 53.9 ms                                                | 62.9 ms: 1.17x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.8 ms: 1.05x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.74 ms: 1.12x faster                                                         |
| genshi_text     | 17.7 ms                                                | 18.4 ms: 1.04x slower                                                         |
| genshi_xml      | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                         |
| django_template | 24.4 ms                                                | 26.2 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 77.0 ms: 5.09x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.14x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 114 us: 2.86x faster                                                          |
| subparsers                    | 39.8 ms                                                | 15.4 ms: 2.59x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 426 ms: 2.39x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                          |
| async_tree_none               | 391 ms                                                 | 188 ms: 2.08x faster                                                          |
| mdp                           | 1.65 sec                                               | 879 ms: 1.88x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.79 ms: 1.79x faster                                                         |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                          |
| raytrace                      | 327 ms                                                 | 207 ms: 1.58x faster                                                          |
| deepcopy_memo                 | 34.7 us                                                | 22.5 us: 1.54x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 91.3 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 442 ms: 1.51x faster                                                          |
| deepcopy                      | 276 us                                                 | 185 us: 1.49x faster                                                          |
| richards_super                | 61.0 ms                                                | 42.2 ms: 1.44x faster                                                         |
| chaos                         | 67.7 ms                                                | 47.1 ms: 1.44x faster                                                         |
| richards                      | 52.3 ms                                                | 37.4 ms: 1.40x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 52.3 ms: 1.38x faster                                                         |
| pylint                        | 231 ms                                                 | 176 ms: 1.32x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 27.1 ms: 1.31x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.57 sec: 1.28x faster                                                        |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                          |
| html5lib                      | 43.5 ms                                                | 34.8 ms: 1.25x faster                                                         |
| float                         | 72.4 ms                                                | 59.4 ms: 1.22x faster                                                         |
| comprehensions                | 17.3 us                                                | 14.2 us: 1.21x faster                                                         |
| pyflate                       | 448 ms                                                 | 369 ms: 1.21x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 15.8 ms: 1.21x faster                                                         |
| hexiom                        | 6.25 ms                                                | 5.18 ms: 1.21x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 79.4 ms: 1.20x faster                                                         |
| pycparser                     | 887 ms                                                 | 752 ms: 1.18x faster                                                          |
| deepcopy_reduce               | 2.32 us                                                | 1.98 us: 1.17x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 62.7 ms: 1.17x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 244 us: 1.16x faster                                                          |
| scimark_lu                    | 103 ms                                                 | 88.6 ms: 1.16x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.49 sec: 1.16x faster                                                        |
| sphinx                        | 729 ms                                                 | 635 ms: 1.15x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 1.17 sec: 1.14x faster                                                        |
| pprint_safe_repr              | 648 ms                                                 | 570 ms: 1.14x faster                                                          |
| regex_compile                 | 95.6 ms                                                | 84.4 ms: 1.13x faster                                                         |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                         |
| json_dumps                    | 8.31 ms                                                | 7.38 ms: 1.12x faster                                                         |
| mako                          | 9.81 ms                                                | 8.74 ms: 1.12x faster                                                         |
| thrift                        | 562 us                                                 | 505 us: 1.11x faster                                                          |
| unpickle_pure_python          | 198 us                                                 | 179 us: 1.11x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                        |
| sympy_sum                     | 92.7 ms                                                | 84.2 ms: 1.10x faster                                                         |
| logging_format                | 5.03 us                                                | 4.58 us: 1.10x faster                                                         |
| logging_simple                | 4.59 us                                                | 4.26 us: 1.08x faster                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.18 ms: 1.07x faster                                                         |
| 2to3                          | 201 ms                                                 | 190 ms: 1.06x faster                                                          |
| pathlib                       | 25.7 ms                                                | 24.4 ms: 1.05x faster                                                         |
| python_startup                | 19.6 ms                                                | 18.8 ms: 1.05x faster                                                         |
| nbody                         | 92.5 ms                                                | 89.0 ms: 1.04x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 218 ms: 1.04x faster                                                          |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                          |
| sympy_str                     | 166 ms                                                 | 162 ms: 1.02x faster                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.35 ms: 1.02x faster                                                         |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| bench_thread_pool             | 545 us                                                 | 539 us: 1.01x faster                                                          |
| generators                    | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                         |
| connected_components          | 318 ms                                                 | 316 ms: 1.01x faster                                                          |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                          |
| bpe_tokeniser                 | 3.44 sec                                               | 3.47 sec: 1.01x slower                                                        |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| sympy_expand                  | 269 ms                                                 | 277 ms: 1.03x slower                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 76.8 ms: 1.03x slower                                                         |
| xml_etree_process             | 44.6 ms                                                | 46.2 ms: 1.03x slower                                                         |
| genshi_text                   | 17.7 ms                                                | 18.4 ms: 1.04x slower                                                         |
| many_optionals                | 486 us                                                 | 508 us: 1.05x slower                                                          |
| shortest_path                 | 328 ms                                                 | 344 ms: 1.05x slower                                                          |
| fannkuch                      | 303 ms                                                 | 320 ms: 1.06x slower                                                          |
| meteor_contest                | 77.8 ms                                                | 82.8 ms: 1.06x slower                                                         |
| genshi_xml                    | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                         |
| django_template               | 24.4 ms                                                | 26.2 ms: 1.07x slower                                                         |
| json_loads                    | 16.6 us                                                | 18.5 us: 1.12x slower                                                         |
| python_startup_no_site        | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.66 us: 1.12x slower                                                         |
| nqueens                       | 63.8 ms                                                | 73.7 ms: 1.15x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 62.9 ms: 1.17x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                         |
| async_generators              | 233 ms                                                 | 292 ms: 1.25x slower                                                          |
| bench_mp_pool                 | 56.0 ms                                                | 71.8 ms: 1.28x slower                                                         |
| coverage                      | 41.2 ms                                                | 54.0 ms: 1.31x slower                                                         |
| telco                         | 3.49 ms                                                | 5.19 ms: 1.49x slower                                                         |
| logging_silent                | 117 ns                                                 | 359 ns: 3.06x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.18x faster                                                                  |

Benchmark hidden because not significant (2): xml_etree_parse, json
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250519-3.15.0a0-4fee8de/bm-20250519-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-4fee8de.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.209x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.16x