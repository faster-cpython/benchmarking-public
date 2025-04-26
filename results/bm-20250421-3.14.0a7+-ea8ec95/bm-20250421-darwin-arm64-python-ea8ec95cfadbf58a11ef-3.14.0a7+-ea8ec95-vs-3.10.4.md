# Results vs. 3.10.4

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: darwin-arm64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.214x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.07x faster                                                   |
| docutils       | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                 |
| html5lib       | 43.5 ms                                                | 35.0 ms: 1.24x faster                                                  |
| sphinx         | 729 ms                                                 | 629 ms: 1.16x faster                                                   |
| Geometric mean | (ref)                                                  | 1.15x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.8 ms: 5.10x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 426 ms: 2.39x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 227 ms: 2.12x faster                                                   |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.10x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                   |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                   |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                   |
| Geometric mean                | (ref)                                                  | 1.87x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| nbody          | 92.5 ms                                                | 97.3 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                  |
| regex_compile  | 95.6 ms                                                | 85.5 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 250 us: 1.14x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 183 us: 1.08x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.76 ms: 1.07x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 106 ms: 1.03x faster                                                   |
| xml_etree_process    | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.4 ms: 1.03x slower                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 61.7 ms: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.1 ms: 1.03x slower                                                  |
| python_startup_no_site | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.14 ms: 1.07x faster                                                  |
| genshi_text     | 17.7 ms                                                | 18.5 ms: 1.05x slower                                                  |
| genshi_xml      | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                  |
| django_template | 24.4 ms                                                | 26.3 ms: 1.08x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.8 ms: 5.10x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 157 ms: 3.08x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 110 us: 2.95x faster                                                   |
| subparsers                    | 39.8 ms                                                | 13.8 ms: 2.89x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 410 ms: 2.47x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 426 ms: 2.39x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 227 ms: 2.12x faster                                                   |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.10x faster                                                   |
| mdp                           | 1.65 sec                                               | 878 ms: 1.88x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.88 ms: 1.73x faster                                                  |
| go                            | 163 ms                                                 | 105 ms: 1.56x faster                                                   |
| raytrace                      | 327 ms                                                 | 215 ms: 1.52x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 441 ms: 1.52x faster                                                   |
| deepcopy                      | 276 us                                                 | 182 us: 1.52x faster                                                   |
| logging_silent                | 117 ns                                                 | 78.4 ns: 1.49x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 23.4 us: 1.49x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 94.5 ms: 1.48x faster                                                  |
| chaos                         | 67.7 ms                                                | 46.5 ms: 1.46x faster                                                  |
| richards_super                | 61.0 ms                                                | 44.1 ms: 1.38x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 52.9 ms: 1.37x faster                                                  |
| pylint                        | 231 ms                                                 | 175 ms: 1.32x faster                                                   |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.30x faster                                                 |
| pyflate                       | 448 ms                                                 | 347 ms: 1.29x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 28.0 ms: 1.27x faster                                                  |
| float                         | 72.4 ms                                                | 57.5 ms: 1.26x faster                                                  |
| richards                      | 52.3 ms                                                | 41.6 ms: 1.26x faster                                                  |
| html5lib                      | 43.5 ms                                                | 35.0 ms: 1.24x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 77.1 ms: 1.24x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 83.0 ms: 1.24x faster                                                  |
| comprehensions                | 17.3 us                                                | 14.3 us: 1.21x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.93 us: 1.21x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.53 ms: 1.20x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 61.0 ms: 1.20x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                  |
| pycparser                     | 887 ms                                                 | 757 ms: 1.17x faster                                                   |
| sphinx                        | 729 ms                                                 | 629 ms: 1.16x faster                                                   |
| logging_format                | 5.03 us                                                | 4.38 us: 1.15x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 66.1 ms: 1.15x faster                                                  |
| hexiom                        | 6.25 ms                                                | 5.48 ms: 1.14x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 250 us: 1.14x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.06 us: 1.13x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.13x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 82.6 ms: 1.12x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 85.5 ms: 1.12x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.55 sec: 1.12x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.10x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 183 us: 1.08x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.18 ms: 1.08x faster                                                  |
| 2to3                          | 201 ms                                                 | 187 ms: 1.07x faster                                                   |
| mako                          | 9.81 ms                                                | 9.14 ms: 1.07x faster                                                  |
| pathlib                       | 25.7 ms                                                | 24.0 ms: 1.07x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.76 ms: 1.07x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.7 ms: 1.04x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.30 sec: 1.04x faster                                                 |
| sympy_str                     | 166 ms                                                 | 160 ms: 1.04x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 1.28 sec: 1.03x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 106 ms: 1.03x faster                                                   |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 635 ms: 1.02x faster                                                   |
| meteor_contest                | 77.8 ms                                                | 77.3 ms: 1.01x faster                                                  |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                   |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                   |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| bench_thread_pool             | 545 us                                                 | 553 us: 1.01x slower                                                   |
| many_optionals                | 486 us                                                 | 494 us: 1.02x slower                                                   |
| python_startup                | 19.6 ms                                                | 20.1 ms: 1.03x slower                                                  |
| xml_etree_process             | 44.6 ms                                                | 45.8 ms: 1.03x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.4 ms: 1.03x slower                                                  |
| shortest_path                 | 328 ms                                                 | 339 ms: 1.03x slower                                                   |
| genshi_text                   | 17.7 ms                                                | 18.5 ms: 1.05x slower                                                  |
| nbody                         | 92.5 ms                                                | 97.3 ms: 1.05x slower                                                  |
| fannkuch                      | 303 ms                                                 | 321 ms: 1.06x slower                                                   |
| genshi_xml                    | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                  |
| django_template               | 24.4 ms                                                | 26.3 ms: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 61.7 ms: 1.15x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                  |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                   |
| nqueens                       | 63.8 ms                                                | 75.2 ms: 1.18x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 66.5 ms: 1.19x slower                                                  |
| coverage                      | 41.2 ms                                                | 49.4 ms: 1.20x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.5 ms: 1.21x slower                                                  |
| telco                         | 3.49 ms                                                | 4.84 ms: 1.39x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.21x faster                                                           |

Benchmark hidden because not significant (2): json, regex_effbot
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-darwin-arm64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.214x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x