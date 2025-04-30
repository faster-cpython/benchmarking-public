# Results vs. 3.10.4

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: darwin-arm64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.212x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 190 ms: 1.06x faster                                                   |
| docutils       | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                 |
| html5lib       | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                  |
| sphinx         | 729 ms                                                 | 632 ms: 1.15x faster                                                   |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 78.1 ms: 5.02x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.13x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 229 ms: 2.10x faster                                                   |
| async_tree_none               | 391 ms                                                 | 191 ms: 2.04x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 375 ms: 1.78x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                   |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.86x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.5 ms: 1.24x faster                                                  |
| nbody          | 92.5 ms                                                | 93.6 ms: 1.01x slower                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.20x faster                                                  |
| regex_compile  | 95.6 ms                                                | 86.5 ms: 1.10x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 253 us: 1.12x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 186 us: 1.07x faster                                                   |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                                   |
| json_dumps           | 8.31 ms                                                | 8.13 ms: 1.02x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.1 ms: 1.02x slower                                                  |
| xml_etree_process    | 44.6 ms                                                | 45.7 ms: 1.03x slower                                                  |
| json_loads           | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 62.0 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.16 ms: 1.07x faster                                                  |
| genshi_text     | 17.7 ms                                                | 18.5 ms: 1.04x slower                                                  |
| genshi_xml      | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                  |
| django_template | 24.4 ms                                                | 26.2 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 78.1 ms: 5.02x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 154 ms: 3.13x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 112 us: 2.92x faster                                                   |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.91x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 424 ms: 2.40x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 229 ms: 2.10x faster                                                   |
| async_tree_none               | 391 ms                                                 | 191 ms: 2.04x faster                                                   |
| mdp                           | 1.65 sec                                               | 872 ms: 1.89x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 375 ms: 1.78x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.86 ms: 1.74x faster                                                  |
| raytrace                      | 327 ms                                                 | 206 ms: 1.59x faster                                                   |
| go                            | 163 ms                                                 | 105 ms: 1.55x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 95.0 ms: 1.47x faster                                                  |
| deepcopy                      | 276 us                                                 | 188 us: 1.47x faster                                                   |
| logging_silent                | 117 ns                                                 | 79.9 ns: 1.47x faster                                                  |
| chaos                         | 67.7 ms                                                | 46.7 ms: 1.45x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 24.0 us: 1.44x faster                                                  |
| richards_super                | 61.0 ms                                                | 44.0 ms: 1.39x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 54.0 ms: 1.34x faster                                                  |
| richards                      | 52.3 ms                                                | 39.5 ms: 1.32x faster                                                  |
| pylint                        | 231 ms                                                 | 175 ms: 1.32x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 27.3 ms: 1.30x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.29x faster                                                 |
| pyflate                       | 448 ms                                                 | 351 ms: 1.27x faster                                                   |
| html5lib                      | 43.5 ms                                                | 35.1 ms: 1.24x faster                                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| float                         | 72.4 ms                                                | 58.5 ms: 1.24x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 83.0 ms: 1.24x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 78.2 ms: 1.22x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.46 ms: 1.21x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.20x faster                                                  |
| comprehensions                | 17.3 us                                                | 14.5 us: 1.19x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 62.0 ms: 1.18x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.97 us: 1.18x faster                                                  |
| pycparser                     | 887 ms                                                 | 758 ms: 1.17x faster                                                   |
| logging_format                | 5.03 us                                                | 4.30 us: 1.17x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.98 us: 1.16x faster                                                  |
| sphinx                        | 729 ms                                                 | 632 ms: 1.15x faster                                                   |
| hexiom                        | 6.25 ms                                                | 5.46 ms: 1.14x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 66.5 ms: 1.14x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.17 sec: 1.13x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.52 sec: 1.13x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 253 us: 1.12x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 579 ms: 1.12x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 83.2 ms: 1.11x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 86.5 ms: 1.10x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 210 ms: 1.07x faster                                                   |
| mako                          | 9.81 ms                                                | 9.16 ms: 1.07x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 186 us: 1.07x faster                                                   |
| 2to3                          | 201 ms                                                 | 190 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.25 ms: 1.05x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| sympy_str                     | 166 ms                                                 | 160 ms: 1.04x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 106 ms: 1.03x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.36 sec: 1.02x faster                                                 |
| connected_components          | 318 ms                                                 | 311 ms: 1.02x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 8.13 ms: 1.02x faster                                                  |
| generators                    | 31.7 ms                                                | 31.4 ms: 1.01x faster                                                  |
| pathlib                       | 25.7 ms                                                | 25.5 ms: 1.01x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 77.9 ms: 1.00x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                   |
| nbody                         | 92.5 ms                                                | 93.6 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| bench_thread_pool             | 545 us                                                 | 553 us: 1.01x slower                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 76.1 ms: 1.02x slower                                                  |
| many_optionals                | 486 us                                                 | 497 us: 1.02x slower                                                   |
| xml_etree_process             | 44.6 ms                                                | 45.7 ms: 1.03x slower                                                  |
| json                          | 3.10 ms                                                | 3.18 ms: 1.03x slower                                                  |
| shortest_path                 | 328 ms                                                 | 339 ms: 1.03x slower                                                   |
| genshi_text                   | 17.7 ms                                                | 18.5 ms: 1.04x slower                                                  |
| fannkuch                      | 303 ms                                                 | 318 ms: 1.05x slower                                                   |
| genshi_xml                    | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                  |
| django_template               | 24.4 ms                                                | 26.2 ms: 1.08x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.61 us: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| json_loads                    | 16.6 us                                                | 18.6 us: 1.12x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 62.0 ms: 1.15x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                  |
| nqueens                       | 63.8 ms                                                | 75.3 ms: 1.18x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 66.9 ms: 1.19x slower                                                  |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                   |
| coverage                      | 41.2 ms                                                | 50.4 ms: 1.22x slower                                                  |
| telco                         | 3.49 ms                                                | 4.97 ms: 1.43x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, python_startup
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-darwin-arm64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.212x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.14x