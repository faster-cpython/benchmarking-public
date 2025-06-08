# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.139x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 217 ms: 1.08x slower                                                  |
| docutils       | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| html5lib       | 43.5 ms                                                | 33.4 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 651 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.0 ms: 5.52x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.28x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.62x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 399 ms: 2.55x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.36x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 455 ms: 1.47x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.3 ms: 1.12x faster                                                 |
| async_generators              | 233 ms                                                 | 314 ms: 1.35x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| nbody          | 92.5 ms                                                | 77.4 ms: 1.20x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.5 ms: 1.28x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.3 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 158 us: 1.26x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.39 sec: 1.24x faster                                                |
| json_dumps           | 8.31 ms                                                | 8.13 ms: 1.02x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 76.5 ms: 1.03x slower                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.03x slower                                                  |
| xml_etree_generate   | 53.9 ms                                                | 64.9 ms: 1.20x slower                                                 |
| json_loads           | 16.6 us                                                | 22.9 us: 1.38x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.27 ms: 1.19x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.6 ms: 1.14x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.2 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 25.7 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.0 ms: 5.52x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 147 ms: 3.28x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 121 us: 2.69x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.62x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 399 ms: 2.55x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.1 ms: 2.48x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.36x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| go                            | 163 ms                                                 | 77.5 ms: 2.11x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.61 ms: 1.91x faster                                                 |
| mdp                           | 1.65 sec                                               | 889 ms: 1.86x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.4 us: 1.79x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.3 ms: 1.56x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 89.8 ms: 1.56x faster                                                 |
| raytrace                      | 327 ms                                                 | 210 ms: 1.56x faster                                                  |
| chaos                         | 67.7 ms                                                | 44.4 ms: 1.53x faster                                                 |
| richards_super                | 61.0 ms                                                | 40.7 ms: 1.50x faster                                                 |
| deepcopy                      | 276 us                                                 | 187 us: 1.47x faster                                                  |
| pyflate                       | 448 ms                                                 | 305 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 455 ms: 1.47x faster                                                  |
| richards                      | 52.3 ms                                                | 36.1 ms: 1.45x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.45x faster                                                 |
| float                         | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.56 ms: 1.37x faster                                                 |
| generators                    | 31.7 ms                                                | 23.2 ms: 1.37x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.1 ms: 1.31x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.54 sec: 1.31x faster                                                |
| pylint                        | 231 ms                                                 | 177 ms: 1.31x faster                                                  |
| html5lib                      | 43.5 ms                                                | 33.4 ms: 1.31x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 74.5 ms: 1.28x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 158 us: 1.26x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.39 sec: 1.24x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 60.7 ms: 1.21x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| nbody                         | 92.5 ms                                                | 77.4 ms: 1.20x faster                                                 |
| pycparser                     | 887 ms                                                 | 745 ms: 1.19x faster                                                  |
| mako                          | 9.81 ms                                                | 8.27 ms: 1.19x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 81.0 ms: 1.18x faster                                                 |
| logging_format                | 5.03 us                                                | 4.28 us: 1.18x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 87.6 ms: 1.17x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.99 us: 1.17x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.94 us: 1.16x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.6 ms: 1.14x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.3 ms: 1.12x faster                                                 |
| sphinx                        | 729 ms                                                 | 651 ms: 1.12x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.8 ms: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.20 sec: 1.11x faster                                                |
| regex_v8                      | 19.1 ms                                                | 17.3 ms: 1.10x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 589 ms: 1.10x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 85.2 ms: 1.09x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.3 ms: 1.06x faster                                                 |
| connected_components          | 318 ms                                                 | 301 ms: 1.06x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 33.2 ms: 1.06x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.13 ms: 1.02x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 76.3 ms: 1.02x faster                                                 |
| python_startup                | 19.6 ms                                                | 19.3 ms: 1.02x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 539 us: 1.01x faster                                                  |
| sympy_str                     | 166 ms                                                 | 165 ms: 1.01x faster                                                  |
| shortest_path                 | 328 ms                                                 | 329 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| fannkuch                      | 303 ms                                                 | 310 ms: 1.02x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.5 ms: 1.03x slower                                                 |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.03x slower                                                  |
| django_template               | 24.4 ms                                                | 25.7 ms: 1.06x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 286 ms: 1.06x slower                                                  |
| nqueens                       | 63.8 ms                                                | 67.9 ms: 1.06x slower                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.66 sec: 1.06x slower                                                |
| many_optionals                | 486 us                                                 | 524 us: 1.08x slower                                                  |
| 2to3                          | 201 ms                                                 | 217 ms: 1.08x slower                                                  |
| dask                          | 789 ms                                                 | 853 ms: 1.08x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                 |
| scimark_fft                   | 225 ms                                                 | 262 ms: 1.16x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.03 ms: 1.18x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 64.9 ms: 1.20x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.42 ms: 1.22x slower                                                 |
| json                          | 3.10 ms                                                | 3.84 ms: 1.24x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.90 us: 1.29x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 75.4 ms: 1.35x slower                                                 |
| async_generators              | 233 ms                                                 | 314 ms: 1.35x slower                                                  |
| json_loads                    | 16.6 us                                                | 22.9 us: 1.38x slower                                                 |
| telco                         | 3.49 ms                                                | 5.55 ms: 1.59x slower                                                 |
| logging_silent                | 117 ns                                                 | 421 ns: 3.59x slower                                                  |
| coverage                      | 41.2 ms                                                | 306 ms: 7.43x slower                                                  |
| thrift                        | 562 us                                                 | 44.1 ms: 78.49x slower                                                |
| Geometric mean                | (ref)                                                  | 1.12x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.139x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.14x