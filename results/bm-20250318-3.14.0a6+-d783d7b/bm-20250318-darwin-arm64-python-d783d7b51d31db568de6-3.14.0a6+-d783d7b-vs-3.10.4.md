# Results vs. 3.10.4

- fork: python
- ref: d783d7b51d31db568de6
- machine: darwin-arm64
- commit hash: d783d7b
- commit date: 2025-03-18
- overall geometric mean: 1.358x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 162 ms: 1.24x faster                                                   |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                  |
| sphinx         | 729 ms                                                 | 582 ms: 1.25x faster                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.2 ms: 6.40x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.80x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 411 ms: 1.63x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                  |
| async_generators              | 233 ms                                                 | 257 ms: 1.10x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                  |
| nbody          | 92.5 ms                                                | 72.9 ms: 1.27x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.8 ms: 1.39x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 205 us: 1.39x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.38x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 149 us: 1.33x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.30 ms: 1.14x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 71.7 ms: 1.04x faster                                                  |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.4 ms: 1.13x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.60 ms: 1.29x faster                                                  |
| genshi_text     | 17.7 ms                                                | 14.1 ms: 1.25x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                  |
| django_template | 24.4 ms                                                | 21.2 ms: 1.15x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.23x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.2 ms: 6.40x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 93.6 us: 3.48x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.2 ms: 3.27x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 363 ms: 2.80x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.39 ms: 2.09x faster                                                  |
| go                            | 163 ms                                                 | 82.2 ms: 1.99x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 18.4 us: 1.89x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                   |
| deepcopy                      | 276 us                                                 | 151 us: 1.82x faster                                                   |
| raytrace                      | 327 ms                                                 | 182 ms: 1.80x faster                                                   |
| logging_silent                | 117 ns                                                 | 66.2 ns: 1.77x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 79.1 ms: 1.77x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 43.3 ms: 1.67x faster                                                  |
| chaos                         | 67.7 ms                                                | 41.4 ms: 1.64x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 411 ms: 1.63x faster                                                   |
| richards_super                | 61.0 ms                                                | 37.6 ms: 1.62x faster                                                  |
| richards                      | 52.3 ms                                                | 33.4 ms: 1.56x faster                                                  |
| float                         | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.6 us: 1.50x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 24.6 ms: 1.44x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.44x faster                                                  |
| pylint                        | 231 ms                                                 | 163 ms: 1.41x faster                                                   |
| hexiom                        | 6.25 ms                                                | 4.44 ms: 1.41x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 948 ms: 1.40x faster                                                   |
| pyflate                       | 448 ms                                                 | 320 ms: 1.40x faster                                                   |
| logging_format                | 5.03 us                                                | 3.62 us: 1.39x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 68.8 ms: 1.39x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 205 us: 1.39x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 467 ms: 1.39x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.32 us: 1.38x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.38x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 74.6 ms: 1.37x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.60 ms: 1.37x faster                                                  |
| pycparser                     | 887 ms                                                 | 663 ms: 1.34x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 149 us: 1.33x faster                                                   |
| generators                    | 31.7 ms                                                | 24.2 ms: 1.31x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.30x faster                                                 |
| mako                          | 9.81 ms                                                | 7.60 ms: 1.29x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.9 ms: 1.29x faster                                                  |
| thrift                        | 562 us                                                 | 440 us: 1.28x faster                                                   |
| nbody                         | 92.5 ms                                                | 72.9 ms: 1.27x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 75.7 ms: 1.26x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 58.3 ms: 1.26x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 14.1 ms: 1.25x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                  |
| sphinx                        | 729 ms                                                 | 582 ms: 1.25x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 74.3 ms: 1.25x faster                                                  |
| 2to3                          | 201 ms                                                 | 162 ms: 1.24x faster                                                   |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 184 ms: 1.23x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 28.9 ms: 1.21x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                 |
| sympy_str                     | 166 ms                                                 | 142 ms: 1.17x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.96 ms: 1.15x faster                                                  |
| django_template               | 24.4 ms                                                | 21.2 ms: 1.15x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.14x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 236 ms: 1.14x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.30 ms: 1.14x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.4 ms: 1.13x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 490 us: 1.11x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.49 sec: 1.11x faster                                                 |
| fannkuch                      | 303 ms                                                 | 277 ms: 1.09x faster                                                   |
| many_optionals                | 486 us                                                 | 448 us: 1.09x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.20 sec: 1.07x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 73.0 ms: 1.07x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 71.7 ms: 1.04x faster                                                  |
| connected_components          | 318 ms                                                 | 308 ms: 1.04x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.13 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| shortest_path                 | 328 ms                                                 | 334 ms: 1.02x slower                                                   |
| nqueens                       | 63.8 ms                                                | 65.3 ms: 1.02x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.04x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.8 ms: 1.08x slower                                                  |
| async_generators              | 233 ms                                                 | 257 ms: 1.10x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.7 ms: 1.11x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.58 ms: 1.31x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_generate, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250318-3.14.0a6+-d783d7b/bm-20250318-darwin-arm64-python-d783d7b51d31db568de6-3.14.0a6+-d783d7b.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.358x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.15x