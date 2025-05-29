# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: darwin-arm64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.476x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.38 sec: 1.26x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.1 ms: 1.50x faster                                                  |
| sphinx         | 729 ms                                                 | 553 ms: 1.32x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.6 ms: 6.93x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.68x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 339 ms: 2.99x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.68x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.60x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.68x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| async_generators              | 233 ms                                                 | 239 ms: 1.03x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.2 ms: 1.68x faster                                                  |
| nbody          | 92.5 ms                                                | 61.6 ms: 1.50x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.9 ms: 1.52x faster                                                  |
| regex_dna      | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.6 ms: 1.15x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 128 us: 1.55x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.8 ms: 1.28x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 98.3 ms: 1.11x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.9 ms: 1.10x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 69.9 ms: 1.07x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.9 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.7 ms: 1.39x faster                                                  |
| mako            | 9.81 ms                                                | 7.35 ms: 1.33x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.2 ms: 1.29x faster                                                  |
| django_template | 24.4 ms                                                | 19.4 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.6 ms: 6.93x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 87.0 us: 3.75x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.68x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.7 ms: 3.41x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 339 ms: 3.00x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 339 ms: 2.99x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 179 ms: 2.68x faster                                                   |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.60x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.08 ms: 2.40x faster                                                  |
| mdp                           | 1.65 sec                                               | 690 ms: 2.39x faster                                                   |
| go                            | 163 ms                                                 | 72.6 ms: 2.25x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.4 us: 2.11x faster                                                  |
| raytrace                      | 327 ms                                                 | 155 ms: 2.11x faster                                                   |
| logging_silent                | 117 ns                                                 | 56.9 ns: 2.06x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 71.8 ms: 1.95x faster                                                  |
| deepcopy                      | 276 us                                                 | 142 us: 1.95x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.3 ms: 1.92x faster                                                  |
| richards_super                | 61.0 ms                                                | 32.6 ms: 1.87x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 38.8 ms: 1.86x faster                                                  |
| richards                      | 52.3 ms                                                | 29.0 ms: 1.80x faster                                                  |
| generators                    | 31.7 ms                                                | 17.8 ms: 1.78x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.2 us: 1.70x faster                                                  |
| float                         | 72.4 ms                                                | 43.2 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.68x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.80 ms: 1.64x faster                                                  |
| pyflate                       | 448 ms                                                 | 276 ms: 1.62x faster                                                   |
| logging_simple                | 4.59 us                                                | 2.96 us: 1.55x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 66.1 ms: 1.55x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.50 us: 1.55x faster                                                  |
| logging_format                | 5.03 us                                                | 3.25 us: 1.55x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 128 us: 1.55x faster                                                   |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 62.6 ms: 1.52x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.9 ms: 1.52x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.5 ms: 1.51x faster                                                  |
| nbody                         | 92.5 ms                                                | 61.6 ms: 1.50x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.1 ms: 1.50x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 49.3 ms: 1.49x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.22 ms: 1.46x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 931 ms: 1.43x faster                                                   |
| pycparser                     | 887 ms                                                 | 627 ms: 1.42x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 466 ms: 1.39x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.7 ms: 1.39x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.0 ms: 1.38x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.50 sec: 1.34x faster                                                 |
| mako                          | 9.81 ms                                                | 7.35 ms: 1.33x faster                                                  |
| 2to3                          | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 69.8 ms: 1.33x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 9.94 ms: 1.32x faster                                                  |
| sphinx                        | 729 ms                                                 | 553 ms: 1.32x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 27.2 ms: 1.29x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.8 ms: 1.28x faster                                                  |
| sympy_str                     | 166 ms                                                 | 130 ms: 1.27x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.38 sec: 1.26x faster                                                 |
| django_template               | 24.4 ms                                                | 19.4 ms: 1.26x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 180 ms: 1.26x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.81 sec: 1.22x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 220 ms: 1.22x faster                                                   |
| nqueens                       | 63.8 ms                                                | 52.4 ms: 1.22x faster                                                  |
| fannkuch                      | 303 ms                                                 | 251 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.84 ms: 1.20x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 460 us: 1.19x faster                                                   |
| regex_dna                     | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 16.6 ms: 1.15x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                  |
| many_optionals                | 486 us                                                 | 429 us: 1.13x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.11x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 98.3 ms: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.2 ms: 1.11x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.9 ms: 1.10x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.9 ms: 1.07x faster                                                  |
| connected_components          | 318 ms                                                 | 300 ms: 1.06x faster                                                   |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.02x slower                                                  |
| async_generators              | 233 ms                                                 | 239 ms: 1.03x slower                                                   |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.6 ms: 1.08x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.7 ms: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.10 ms: 1.14x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.9 ms: 1.17x slower                                                  |
| telco                         | 3.49 ms                                                | 4.46 ms: 1.28x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (2): shortest_path, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (20) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-darwin-arm64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.476x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.32x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.14x