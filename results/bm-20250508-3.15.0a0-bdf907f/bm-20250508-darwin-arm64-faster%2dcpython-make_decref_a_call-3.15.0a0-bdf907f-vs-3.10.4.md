# Results vs. 3.10.4

- fork: faster-cpython
- ref: make_decref_a_call
- machine: darwin-arm64
- commit hash: bdf907f
- commit date: 2025-05-08
- overall geometric mean: 1.213x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 188 ms: 1.07x faster                                                          |
| docutils       | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                        |
| html5lib       | 43.5 ms                                                | 35.0 ms: 1.24x faster                                                         |
| sphinx         | 729 ms                                                 | 637 ms: 1.14x faster                                                          |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.6 ms: 5.12x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.15x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 427 ms: 2.38x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                          |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 439 ms: 1.52x faster                                                          |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x slower                                                          |
| async_generators              | 233 ms                                                 | 293 ms: 1.26x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.87x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.8 ms: 1.23x faster                                                         |
| nbody          | 92.5 ms                                                | 91.0 ms: 1.02x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 137 ms: 1.27x faster                                                          |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                         |
| regex_compile  | 95.6 ms                                                | 84.4 ms: 1.13x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                         |
| Geometric mean | (ref)                                                  | 1.16x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.49 sec: 1.15x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 249 us: 1.14x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 178 us: 1.11x faster                                                          |
| json_dumps           | 8.31 ms                                                | 8.43 ms: 1.01x slower                                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 76.8 ms: 1.03x slower                                                         |
| xml_etree_process    | 44.6 ms                                                | 46.3 ms: 1.04x slower                                                         |
| json_loads           | 16.6 us                                                | 18.6 us: 1.12x slower                                                         |
| xml_etree_generate   | 53.9 ms                                                | 62.8 ms: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.3 ms: 1.20x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 11.9 ms: 1.08x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.70 ms: 1.13x faster                                                         |
| genshi_text     | 17.7 ms                                                | 18.5 ms: 1.04x slower                                                         |
| django_template | 24.4 ms                                                | 26.1 ms: 1.07x slower                                                         |
| genshi_xml      | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.6 ms: 5.12x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.15x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 115 us: 2.84x faster                                                          |
| subparsers                    | 39.8 ms                                                | 14.8 ms: 2.70x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 409 ms: 2.48x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 427 ms: 2.38x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                          |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.11x faster                                                          |
| mdp                           | 1.65 sec                                               | 881 ms: 1.87x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.79 ms: 1.79x faster                                                         |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                          |
| raytrace                      | 327 ms                                                 | 208 ms: 1.57x faster                                                          |
| deepcopy_memo                 | 34.7 us                                                | 22.5 us: 1.54x faster                                                         |
| logging_silent                | 117 ns                                                 | 76.2 ns: 1.54x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 91.8 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 439 ms: 1.52x faster                                                          |
| deepcopy                      | 276 us                                                 | 183 us: 1.51x faster                                                          |
| chaos                         | 67.7 ms                                                | 47.1 ms: 1.44x faster                                                         |
| richards_super                | 61.0 ms                                                | 42.9 ms: 1.42x faster                                                         |
| richards                      | 52.3 ms                                                | 37.8 ms: 1.38x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 26.9 ms: 1.32x faster                                                         |
| pylint                        | 231 ms                                                 | 175 ms: 1.32x faster                                                          |
| k_core                        | 2.01 sec                                               | 1.57 sec: 1.28x faster                                                        |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.27x faster                                                          |
| html5lib                      | 43.5 ms                                                | 35.0 ms: 1.24x faster                                                         |
| float                         | 72.4 ms                                                | 58.8 ms: 1.23x faster                                                         |
| pyflate                       | 448 ms                                                 | 369 ms: 1.21x faster                                                          |
| comprehensions                | 17.3 us                                                | 14.3 us: 1.21x faster                                                         |
| hexiom                        | 6.25 ms                                                | 5.17 ms: 1.21x faster                                                         |
| python_startup                | 19.6 ms                                                | 16.3 ms: 1.20x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 80.1 ms: 1.19x faster                                                         |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.98 us: 1.17x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 62.6 ms: 1.17x faster                                                         |
| pycparser                     | 887 ms                                                 | 759 ms: 1.17x faster                                                          |
| logging_format                | 5.03 us                                                | 4.33 us: 1.16x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.49 sec: 1.15x faster                                                        |
| sphinx                        | 729 ms                                                 | 637 ms: 1.14x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 249 us: 1.14x faster                                                          |
| logging_simple                | 4.59 us                                                | 4.02 us: 1.14x faster                                                         |
| pprint_pformat                | 1.33 sec                                               | 1.17 sec: 1.14x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 84.4 ms: 1.13x faster                                                         |
| pprint_safe_repr              | 648 ms                                                 | 573 ms: 1.13x faster                                                          |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                         |
| mako                          | 9.81 ms                                                | 8.70 ms: 1.13x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 91.2 ms: 1.12x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 178 us: 1.11x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                        |
| thrift                        | 562 us                                                 | 509 us: 1.10x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 84.3 ms: 1.10x faster                                                         |
| pathlib                       | 25.7 ms                                                | 23.6 ms: 1.09x faster                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.16 ms: 1.08x faster                                                         |
| python_startup_no_site        | 12.8 ms                                                | 11.9 ms: 1.08x faster                                                         |
| 2to3                          | 201 ms                                                 | 188 ms: 1.07x faster                                                          |
| scimark_fft                   | 225 ms                                                 | 219 ms: 1.03x faster                                                          |
| sympy_str                     | 166 ms                                                 | 162 ms: 1.03x faster                                                          |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                          |
| nbody                         | 92.5 ms                                                | 91.0 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.37 ms: 1.01x faster                                                         |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                         |
| connected_components          | 318 ms                                                 | 315 ms: 1.01x faster                                                          |
| bench_thread_pool             | 545 us                                                 | 542 us: 1.01x faster                                                          |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                                         |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x slower                                                          |
| json                          | 3.10 ms                                                | 3.12 ms: 1.01x slower                                                         |
| bpe_tokeniser                 | 3.44 sec                                               | 3.47 sec: 1.01x slower                                                        |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| json_dumps                    | 8.31 ms                                                | 8.43 ms: 1.01x slower                                                         |
| xml_etree_iterparse           | 74.5 ms                                                | 76.8 ms: 1.03x slower                                                         |
| sympy_expand                  | 269 ms                                                 | 278 ms: 1.03x slower                                                          |
| many_optionals                | 486 us                                                 | 503 us: 1.04x slower                                                          |
| xml_etree_process             | 44.6 ms                                                | 46.3 ms: 1.04x slower                                                         |
| genshi_text                   | 17.7 ms                                                | 18.5 ms: 1.04x slower                                                         |
| shortest_path                 | 328 ms                                                 | 344 ms: 1.05x slower                                                          |
| fannkuch                      | 303 ms                                                 | 320 ms: 1.06x slower                                                          |
| meteor_contest                | 77.8 ms                                                | 82.5 ms: 1.06x slower                                                         |
| django_template               | 24.4 ms                                                | 26.1 ms: 1.07x slower                                                         |
| genshi_xml                    | 35.1 ms                                                | 37.6 ms: 1.07x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.66 us: 1.12x slower                                                         |
| json_loads                    | 16.6 us                                                | 18.6 us: 1.12x slower                                                         |
| nqueens                       | 63.8 ms                                                | 73.8 ms: 1.16x slower                                                         |
| xml_etree_generate            | 53.9 ms                                                | 62.8 ms: 1.16x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                                         |
| async_generators              | 233 ms                                                 | 293 ms: 1.26x slower                                                          |
| bench_mp_pool                 | 56.0 ms                                                | 70.6 ms: 1.26x slower                                                         |
| coverage                      | 41.2 ms                                                | 53.5 ms: 1.30x slower                                                         |
| telco                         | 3.49 ms                                                | 5.12 ms: 1.47x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.21x faster                                                                  |

Benchmark hidden because not significant (1): xml_etree_parse
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250508-3.15.0a0-bdf907f/bm-20250508-darwin-arm64-faster%2dcpython-make_decref_a_call-3.15.0a0-bdf907f.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.213x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.16x