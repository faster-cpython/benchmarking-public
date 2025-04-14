# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_mcmodel_again
- machine: darwin-arm64
- commit hash: 86ef9a1
- commit date: 2025-02-12
- overall geometric mean: 1.371x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 166 ms: 1.21x faster                                                         |
| docutils       | 1.74 sec                                               | 1.48 sec: 1.18x faster                                                       |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                        |
| sphinx         | 729 ms                                                 | 572 ms: 1.27x faster                                                         |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 66.9 ms: 5.86x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 146 ms: 3.31x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 373 ms: 2.73x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                         |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 364 ms: 1.84x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                         |
| coroutines                    | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                        |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                         |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                        |
| nbody          | 92.5 ms                                                | 65.7 ms: 1.41x faster                                                        |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.5 ms: 1.40x faster                                                        |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                         |
| regex_v8       | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                        |
| regex_effbot   | 2.34 ms                                                | 2.28 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 131 us: 1.51x faster                                                         |
| pickle_pure_python   | 285 us                                                 | 195 us: 1.46x faster                                                         |
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                       |
| xml_etree_process    | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                        |
| json_dumps           | 8.31 ms                                                | 7.35 ms: 1.13x faster                                                        |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.09x faster                                                         |
| xml_etree_generate   | 53.9 ms                                                | 50.4 ms: 1.07x faster                                                        |
| xml_etree_iterparse  | 74.5 ms                                                | 69.6 ms: 1.07x faster                                                        |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                 |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.49 ms: 1.51x faster                                                        |
| genshi_text     | 17.7 ms                                                | 13.6 ms: 1.31x faster                                                        |
| genshi_xml      | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                        |
| django_template | 24.4 ms                                                | 21.1 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 66.9 ms: 5.86x faster                                                        |
| typing_runtime_protocols      | 326 us                                                 | 94.5 us: 3.45x faster                                                        |
| subparsers                    | 39.8 ms                                                | 11.8 ms: 3.36x faster                                                        |
| async_tree_eager_memoization  | 483 ms                                                 | 146 ms: 3.31x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                         |
| async_tree_io                 | 1.02 sec                                               | 373 ms: 2.73x faster                                                         |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                         |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                         |
| deltablue                     | 4.99 ms                                                | 2.34 ms: 2.13x faster                                                        |
| go                            | 163 ms                                                 | 80.8 ms: 2.02x faster                                                        |
| deepcopy_memo                 | 34.7 us                                                | 18.3 us: 1.90x faster                                                        |
| raytrace                      | 327 ms                                                 | 172 ms: 1.90x faster                                                         |
| deepcopy                      | 276 us                                                 | 150 us: 1.84x faster                                                         |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 364 ms: 1.84x faster                                                         |
| scimark_sor                   | 140 ms                                                 | 77.5 ms: 1.81x faster                                                        |
| richards_super                | 61.0 ms                                                | 35.0 ms: 1.74x faster                                                        |
| logging_silent                | 117 ns                                                 | 67.3 ns: 1.74x faster                                                        |
| chaos                         | 67.7 ms                                                | 39.2 ms: 1.73x faster                                                        |
| scimark_monte_carlo           | 72.4 ms                                                | 42.4 ms: 1.71x faster                                                        |
| richards                      | 52.3 ms                                                | 31.3 ms: 1.67x faster                                                        |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                         |
| sqlglot_parse                 | 1.35 ms                                                | 840 us: 1.61x faster                                                         |
| pyflate                       | 448 ms                                                 | 285 ms: 1.57x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 61.3 ms: 1.55x faster                                                        |
| sqlglot_transpile             | 1.56 ms                                                | 1.01 ms: 1.55x faster                                                        |
| float                         | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                        |
| unpickle_pure_python          | 198 us                                                 | 131 us: 1.51x faster                                                         |
| mako                          | 9.81 ms                                                | 6.49 ms: 1.51x faster                                                        |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                        |
| deepcopy_reduce               | 2.32 us                                                | 1.57 us: 1.48x faster                                                        |
| logging_format                | 5.03 us                                                | 3.43 us: 1.47x faster                                                        |
| logging_simple                | 4.59 us                                                | 3.13 us: 1.47x faster                                                        |
| pickle_pure_python            | 285 us                                                 | 195 us: 1.46x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                       |
| pylint                        | 231 ms                                                 | 161 ms: 1.44x faster                                                         |
| nbody                         | 92.5 ms                                                | 65.7 ms: 1.41x faster                                                        |
| scimark_lu                    | 103 ms                                                 | 73.3 ms: 1.40x faster                                                        |
| regex_compile                 | 95.6 ms                                                | 68.5 ms: 1.40x faster                                                        |
| generators                    | 31.7 ms                                                | 22.8 ms: 1.39x faster                                                        |
| crypto_pyaes                  | 73.3 ms                                                | 53.1 ms: 1.38x faster                                                        |
| comprehensions                | 17.3 us                                                | 12.7 us: 1.37x faster                                                        |
| hexiom                        | 6.25 ms                                                | 4.59 ms: 1.36x faster                                                        |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.68 ms: 1.36x faster                                                        |
| scimark_fft                   | 225 ms                                                 | 170 ms: 1.32x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                       |
| genshi_text                   | 17.7 ms                                                | 13.6 ms: 1.31x faster                                                        |
| coroutines                    | 20.5 ms                                                | 15.8 ms: 1.30x faster                                                        |
| pycparser                     | 887 ms                                                 | 687 ms: 1.29x faster                                                         |
| thrift                        | 562 us                                                 | 438 us: 1.28x faster                                                         |
| sqlalchemy_declarative        | 75.7 ms                                                | 59.1 ms: 1.28x faster                                                        |
| sphinx                        | 729 ms                                                 | 572 ms: 1.27x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 28.1 ms: 1.27x faster                                                        |
| xml_etree_process             | 44.6 ms                                                | 35.6 ms: 1.25x faster                                                        |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                         |
| sympy_sum                     | 92.7 ms                                                | 74.9 ms: 1.24x faster                                                        |
| 2to3                          | 201 ms                                                 | 166 ms: 1.21x faster                                                         |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.83 ms: 1.21x faster                                                        |
| genshi_xml                    | 35.1 ms                                                | 29.1 ms: 1.21x faster                                                        |
| bpe_tokeniser                 | 3.44 sec                                               | 2.86 sec: 1.20x faster                                                       |
| pprint_pformat                | 1.33 sec                                               | 1.11 sec: 1.19x faster                                                       |
| pprint_safe_repr              | 648 ms                                                 | 550 ms: 1.18x faster                                                         |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                         |
| docutils                      | 1.74 sec                                               | 1.48 sec: 1.18x faster                                                       |
| django_template               | 24.4 ms                                                | 21.1 ms: 1.15x faster                                                        |
| sympy_integrate               | 13.2 ms                                                | 11.5 ms: 1.15x faster                                                        |
| regex_v8                      | 19.1 ms                                                | 16.8 ms: 1.14x faster                                                        |
| json_dumps                    | 8.31 ms                                                | 7.35 ms: 1.13x faster                                                        |
| fannkuch                      | 303 ms                                                 | 270 ms: 1.12x faster                                                         |
| sympy_expand                  | 269 ms                                                 | 240 ms: 1.12x faster                                                         |
| sqlglot_optimize              | 37.2 ms                                                | 33.5 ms: 1.11x faster                                                        |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                        |
| bench_thread_pool             | 545 us                                                 | 497 us: 1.10x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.09x faster                                                         |
| mdp                           | 1.65 sec                                               | 1.53 sec: 1.08x faster                                                       |
| many_optionals                | 486 us                                                 | 452 us: 1.07x faster                                                         |
| xml_etree_generate            | 53.9 ms                                                | 50.4 ms: 1.07x faster                                                        |
| xml_etree_iterparse           | 74.5 ms                                                | 69.6 ms: 1.07x faster                                                        |
| connected_components          | 318 ms                                                 | 301 ms: 1.06x faster                                                         |
| meteor_contest                | 77.8 ms                                                | 73.5 ms: 1.06x faster                                                        |
| sqlglot_normalize             | 192 ms                                                 | 183 ms: 1.05x faster                                                         |
| nqueens                       | 63.8 ms                                                | 61.3 ms: 1.04x faster                                                        |
| json                          | 3.10 ms                                                | 3.01 ms: 1.03x faster                                                        |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                         |
| regex_effbot                  | 2.34 ms                                                | 2.28 ms: 1.02x faster                                                        |
| shortest_path                 | 328 ms                                                 | 331 ms: 1.01x slower                                                         |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                        |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                        |
| bench_mp_pool                 | 56.0 ms                                                | 61.0 ms: 1.09x slower                                                        |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                        |
| coverage                      | 41.2 ms                                                | 46.2 ms: 1.12x slower                                                        |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                        |
| python_startup_no_site        | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                        |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                         |
| telco                         | 3.49 ms                                                | 4.45 ms: 1.28x slower                                                        |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                                 |

Benchmark hidden because not significant (2): python_startup, asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (8) of results/bm-20250212-3.14.0a4+-86ef9a1-JIT/bm-20250212-darwin-arm64-brandtbucher-justin_mcmodel_again-3.14.0a4+-86ef9a1.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

- Geometric mean (including insignificant results): 1.371x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.15x