# Results vs. 3.10.4

- fork: mdboom
- ref: python_startup_time
- machine: darwin-arm64
- commit hash: 9fc1238
- commit date: 2025-04-25
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 220 ms: 1.09x slower                                                  |
| docutils       | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                |
| html5lib       | 43.5 ms                                                | 36.9 ms: 1.18x faster                                                 |
| sphinx         | 729 ms                                                 | 627 ms: 1.16x faster                                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.3 ms: 4.82x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 156 ms: 3.11x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 435 ms: 2.34x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 223 ms: 2.16x faster                                                  |
| async_tree_none               | 391 ms                                                 | 189 ms: 2.07x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.6 ms: 1.04x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 245 ms: 1.01x slower                                                  |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.86x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| nbody          | 92.5 ms                                                | 97.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                 |
| regex_compile  | 95.6 ms                                                | 85.6 ms: 1.12x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.28 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 249 us: 1.14x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| unpickle_pure_python | 198 us                                                 | 183 us: 1.08x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.88 ms: 1.05x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 107 ms: 1.03x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.4 ms: 1.03x slower                                                 |
| xml_etree_process    | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 61.5 ms: 1.14x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.9 ms: 1.01x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.07 ms: 1.08x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 37.2 ms: 1.06x slower                                                 |
| genshi_text     | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                 |
| django_template | 24.4 ms                                                | 26.2 ms: 1.08x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 81.3 ms: 4.82x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 156 ms: 3.11x faster                                                  |
| subparsers                    | 39.8 ms                                                | 13.9 ms: 2.87x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 115 us: 2.85x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 435 ms: 2.34x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 223 ms: 2.16x faster                                                  |
| async_tree_none               | 391 ms                                                 | 189 ms: 2.07x faster                                                  |
| mdp                           | 1.65 sec                                               | 877 ms: 1.88x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.93 ms: 1.70x faster                                                 |
| go                            | 163 ms                                                 | 105 ms: 1.55x faster                                                  |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 437 ms: 1.53x faster                                                  |
| deepcopy                      | 276 us                                                 | 181 us: 1.52x faster                                                  |
| logging_silent                | 117 ns                                                 | 78.3 ns: 1.50x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 23.4 us: 1.49x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 95.0 ms: 1.47x faster                                                 |
| chaos                         | 67.7 ms                                                | 46.5 ms: 1.46x faster                                                 |
| richards_super                | 61.0 ms                                                | 43.9 ms: 1.39x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 53.6 ms: 1.35x faster                                                 |
| richards                      | 52.3 ms                                                | 39.3 ms: 1.33x faster                                                 |
| pylint                        | 231 ms                                                 | 175 ms: 1.32x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.9 ms: 1.32x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                |
| pyflate                       | 448 ms                                                 | 347 ms: 1.29x faster                                                  |
| float                         | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 77.0 ms: 1.24x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 83.7 ms: 1.23x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.45 ms: 1.22x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.3 us: 1.21x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.21x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 61.1 ms: 1.20x faster                                                 |
| html5lib                      | 43.5 ms                                                | 36.9 ms: 1.18x faster                                                 |
| pycparser                     | 887 ms                                                 | 753 ms: 1.18x faster                                                  |
| sphinx                        | 729 ms                                                 | 627 ms: 1.16x faster                                                  |
| logging_format                | 5.03 us                                                | 4.38 us: 1.15x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.47 ms: 1.14x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 249 us: 1.14x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.06 us: 1.13x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 82.4 ms: 1.13x faster                                                 |
| sqlalchemy_declarative        | 75.7 ms                                                | 67.4 ms: 1.12x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                |
| regex_compile                 | 95.6 ms                                                | 85.6 ms: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.21 sec: 1.09x faster                                                |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.09x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 183 us: 1.08x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 598 ms: 1.08x faster                                                  |
| mako                          | 9.81 ms                                                | 9.07 ms: 1.08x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.20 ms: 1.07x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.2 ms: 1.06x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.88 ms: 1.05x faster                                                 |
| coroutines                    | 20.5 ms                                                | 19.6 ms: 1.04x faster                                                 |
| sympy_str                     | 166 ms                                                 | 159 ms: 1.04x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.03x faster                                                |
| regex_effbot                  | 2.34 ms                                                | 2.28 ms: 1.03x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 107 ms: 1.03x faster                                                  |
| connected_components          | 318 ms                                                 | 311 ms: 1.02x faster                                                  |
| json                          | 3.10 ms                                                | 3.06 ms: 1.01x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 77.5 ms: 1.00x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 268 ms: 1.00x faster                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| python_startup                | 19.6 ms                                                | 19.9 ms: 1.01x slower                                                 |
| asyncio_websockets            | 242 ms                                                 | 245 ms: 1.01x slower                                                  |
| many_optionals                | 486 us                                                 | 492 us: 1.01x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.4 ms: 1.03x slower                                                 |
| xml_etree_process             | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 561 us: 1.03x slower                                                  |
| shortest_path                 | 328 ms                                                 | 340 ms: 1.04x slower                                                  |
| nbody                         | 92.5 ms                                                | 97.4 ms: 1.05x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 37.2 ms: 1.06x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                 |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                 |
| django_template               | 24.4 ms                                                | 26.2 ms: 1.08x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                 |
| 2to3                          | 201 ms                                                 | 220 ms: 1.09x slower                                                  |
| fannkuch                      | 303 ms                                                 | 333 ms: 1.10x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 61.5 ms: 1.14x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                 |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 66.7 ms: 1.19x slower                                                 |
| coverage                      | 41.2 ms                                                | 50.0 ms: 1.21x slower                                                 |
| nqueens                       | 63.8 ms                                                | 78.5 ms: 1.23x slower                                                 |
| telco                         | 3.49 ms                                                | 4.91 ms: 1.41x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.21x faster                                                          |

Benchmark hidden because not significant (1): generators
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250425-3.14.0a7+-9fc1238/bm-20250425-darwin-arm64-mdboom-python_startup_time-3.14.0a7+-9fc1238.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.212x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.15x