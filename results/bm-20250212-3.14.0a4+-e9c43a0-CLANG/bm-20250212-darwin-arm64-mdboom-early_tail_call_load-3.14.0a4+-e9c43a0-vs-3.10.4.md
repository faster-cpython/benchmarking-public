# Results vs. 3.10.4

- fork: mdboom
- ref: early_tail_call_load
- machine: darwin-arm64
- commit hash: e9c43a0
- commit date: 2025-02-12
- overall geometric mean: 1.479x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 152 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.35 sec: 1.29x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.7 ms: 1.51x faster                                                  |
| sphinx         | 729 ms                                                 | 537 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.4 ms: 6.72x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 134 ms: 3.60x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 340 ms: 2.99x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 348 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.1 ms: 1.36x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_generators              | 233 ms                                                 | 250 ms: 1.07x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.20x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.6 ms: 1.66x faster                                                  |
| nbody          | 92.5 ms                                                | 63.3 ms: 1.46x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| regex_dna      | 175 ms                                                 | 146 ms: 1.20x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.7 ms: 1.08x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 123 us: 1.61x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 182 us: 1.57x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.0 ms: 1.31x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.1 ms: 1.15x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.3 ms: 1.44x faster                                                  |
| mako            | 9.81 ms                                                | 7.05 ms: 1.39x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.3 ms: 1.34x faster                                                  |
| django_template | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.36x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.4 ms: 6.72x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 86.9 us: 3.75x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 134 ms: 3.60x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.53x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 340 ms: 2.99x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.04 ms: 2.45x faster                                                  |
| go                            | 163 ms                                                 | 70.5 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.3 us: 2.13x faster                                                  |
| raytrace                      | 327 ms                                                 | 155 ms: 2.11x faster                                                   |
| logging_silent                | 117 ns                                                 | 58.1 ns: 2.02x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 678 us: 1.99x faster                                                   |
| deepcopy                      | 276 us                                                 | 140 us: 1.97x faster                                                   |
| richards_super                | 61.0 ms                                                | 31.0 ms: 1.97x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.0 ms: 1.93x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 348 ms: 1.92x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 73.3 ms: 1.91x faster                                                  |
| richards                      | 52.3 ms                                                | 27.6 ms: 1.90x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 825 us: 1.89x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 39.0 ms: 1.86x faster                                                  |
| generators                    | 31.7 ms                                                | 17.2 ms: 1.85x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| float                         | 72.4 ms                                                | 43.6 ms: 1.66x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.5 us: 1.64x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.81 ms: 1.64x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 58.6 ms: 1.63x faster                                                  |
| pyflate                       | 448 ms                                                 | 276 ms: 1.62x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 123 us: 1.61x faster                                                   |
| logging_simple                | 4.59 us                                                | 2.90 us: 1.58x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 64.8 ms: 1.58x faster                                                  |
| pylint                        | 231 ms                                                 | 146 ms: 1.58x faster                                                   |
| logging_format                | 5.03 us                                                | 3.21 us: 1.57x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 46.8 ms: 1.57x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 182 us: 1.57x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.50 us: 1.55x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.0 ms: 1.54x faster                                                  |
| html5lib                      | 43.5 ms                                                | 28.7 ms: 1.51x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 879 ms: 1.51x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 436 ms: 1.49x faster                                                   |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.13 ms: 1.48x faster                                                  |
| nbody                         | 92.5 ms                                                | 63.3 ms: 1.46x faster                                                  |
| pycparser                     | 887 ms                                                 | 614 ms: 1.44x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.3 ms: 1.44x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 53.9 ms: 1.40x faster                                                  |
| mako                          | 9.81 ms                                                | 7.05 ms: 1.39x faster                                                  |
| thrift                        | 562 us                                                 | 409 us: 1.38x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.1 ms: 1.36x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                 |
| sphinx                        | 729 ms                                                 | 537 ms: 1.36x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 68.5 ms: 1.35x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.4 ms: 1.35x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.3 ms: 1.34x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 169 ms: 1.33x faster                                                   |
| 2to3                          | 201 ms                                                 | 152 ms: 1.33x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 34.0 ms: 1.31x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.31x faster                                                  |
| sympy_str                     | 166 ms                                                 | 128 ms: 1.29x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.35 sec: 1.29x faster                                                 |
| django_template               | 24.4 ms                                                | 19.0 ms: 1.28x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.67 ms: 1.28x faster                                                  |
| nqueens                       | 63.8 ms                                                | 50.6 ms: 1.26x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.75 sec: 1.25x faster                                                 |
| sqlglot_optimize              | 37.2 ms                                                | 29.8 ms: 1.25x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 216 ms: 1.25x faster                                                   |
| fannkuch                      | 303 ms                                                 | 247 ms: 1.23x faster                                                   |
| regex_dna                     | 175 ms                                                 | 146 ms: 1.20x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 456 us: 1.20x faster                                                   |
| many_optionals                | 486 us                                                 | 411 us: 1.18x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 164 ms: 1.18x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.1 ms: 1.17x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.16x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.1 ms: 1.15x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 68.4 ms: 1.14x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 17.7 ms: 1.08x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.0 ms: 1.08x faster                                                  |
| connected_components          | 318 ms                                                 | 297 ms: 1.07x faster                                                   |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 770 ms: 1.02x faster                                                   |
| shortest_path                 | 328 ms                                                 | 325 ms: 1.01x faster                                                   |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.36 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.50 us: 1.01x slower                                                  |
| async_generators              | 233 ms                                                 | 250 ms: 1.07x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.1 ms: 1.09x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                  |
| telco                         | 3.49 ms                                                | 4.42 ms: 1.27x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250212-3.14.0a4+-e9c43a0-CLANG/bm-20250212-darwin-arm64-mdboom-early_tail_call_load-3.14.0a4+-e9c43a0.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.479x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.12x