# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: darwin-arm64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.124x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 192 ms: 1.05x faster                                                  |
| docutils       | 1.74 sec                                               | 1.63 sec: 1.07x faster                                                |
| html5lib       | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 658 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.6 ms: 5.39x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.61x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 402 ms: 2.53x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 206 ms: 2.34x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 394 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 452 ms: 1.48x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.3 ms: 1.12x faster                                                 |
| async_generators              | 233 ms                                                 | 326 ms: 1.40x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.91x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| nbody          | 92.5 ms                                                | 77.6 ms: 1.19x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 76.2 ms: 1.25x faster                                                 |
| regex_dna      | 175 ms                                                 | 147 ms: 1.19x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.7 ms: 1.08x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 150 us: 1.32x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| json_dumps           | 8.31 ms                                                | 8.05 ms: 1.03x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 111 ms: 1.01x slower                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.9 ms: 1.03x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 64.0 ms: 1.19x slower                                                 |
| json_loads           | 16.6 us                                                | 22.9 us: 1.38x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.5 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.15 ms: 1.20x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.8 ms: 1.12x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                 |
| django_template | 24.4 ms                                                | 25.6 ms: 1.05x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.6 ms: 5.39x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 123 us: 2.66x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.61x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 402 ms: 2.53x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.1 ms: 2.48x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 206 ms: 2.34x faster                                                  |
| async_tree_none               | 391 ms                                                 | 173 ms: 2.26x faster                                                  |
| go                            | 163 ms                                                 | 79.5 ms: 2.05x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.69 ms: 1.86x faster                                                 |
| mdp                           | 1.65 sec                                               | 891 ms: 1.85x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.3 us: 1.80x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 394 ms: 1.70x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 89.0 ms: 1.57x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.1 ms: 1.57x faster                                                 |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                  |
| chaos                         | 67.7 ms                                                | 45.0 ms: 1.51x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.0 ms: 1.49x faster                                                 |
| deepcopy                      | 276 us                                                 | 186 us: 1.48x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 452 ms: 1.48x faster                                                  |
| pyflate                       | 448 ms                                                 | 310 ms: 1.44x faster                                                  |
| richards                      | 52.3 ms                                                | 36.3 ms: 1.44x faster                                                 |
| float                         | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| generators                    | 31.7 ms                                                | 23.1 ms: 1.37x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.68 ms: 1.34x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 150 us: 1.32x faster                                                  |
| html5lib                      | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.5 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.4 us: 1.29x faster                                                 |
| pylint                        | 231 ms                                                 | 179 ms: 1.29x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.27x faster                                                |
| regex_compile                 | 95.6 ms                                                | 76.2 ms: 1.25x faster                                                 |
| mako                          | 9.81 ms                                                | 8.15 ms: 1.20x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 61.0 ms: 1.20x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                |
| nbody                         | 92.5 ms                                                | 77.6 ms: 1.19x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 80.3 ms: 1.19x faster                                                 |
| regex_dna                     | 175 ms                                                 | 147 ms: 1.19x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.98 us: 1.17x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 87.5 ms: 1.17x faster                                                 |
| logging_format                | 5.03 us                                                | 4.39 us: 1.15x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.06 us: 1.13x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.8 ms: 1.12x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.3 ms: 1.12x faster                                                 |
| pycparser                     | 887 ms                                                 | 797 ms: 1.11x faster                                                  |
| sphinx                        | 729 ms                                                 | 658 ms: 1.11x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.7 ms: 1.08x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 86.0 ms: 1.08x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.63 sec: 1.07x faster                                                |
| pathlib                       | 25.7 ms                                                | 24.3 ms: 1.06x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.22 ms: 1.05x faster                                                 |
| 2to3                          | 201 ms                                                 | 192 ms: 1.05x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.05 ms: 1.03x faster                                                 |
| python_startup                | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                 |
| connected_components          | 318 ms                                                 | 316 ms: 1.01x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 543 us: 1.00x faster                                                  |
| sympy_str                     | 166 ms                                                 | 168 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| xml_etree_parse               | 109 ms                                                 | 111 ms: 1.01x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.9 ms: 1.03x slower                                                 |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                  |
| django_template               | 24.4 ms                                                | 25.6 ms: 1.05x slower                                                 |
| pprint_safe_repr              | 648 ms                                                 | 690 ms: 1.06x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 82.8 ms: 1.06x slower                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.42 sec: 1.07x slower                                                |
| nqueens                       | 63.8 ms                                                | 68.3 ms: 1.07x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 291 ms: 1.08x slower                                                  |
| dask                          | 789 ms                                                 | 854 ms: 1.08x slower                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.76 sec: 1.09x slower                                                |
| many_optionals                | 486 us                                                 | 533 us: 1.10x slower                                                  |
| scimark_fft                   | 225 ms                                                 | 248 ms: 1.10x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.5 ms: 1.13x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| fannkuch                      | 303 ms                                                 | 357 ms: 1.18x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 64.0 ms: 1.19x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.39 ms: 1.20x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.20 ms: 1.23x slower                                                 |
| json                          | 3.10 ms                                                | 3.85 ms: 1.24x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.92 us: 1.30x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 75.2 ms: 1.34x slower                                                 |
| json_loads                    | 16.6 us                                                | 22.9 us: 1.38x slower                                                 |
| async_generators              | 233 ms                                                 | 326 ms: 1.40x slower                                                  |
| telco                         | 3.49 ms                                                | 5.63 ms: 1.61x slower                                                 |
| logging_silent                | 117 ns                                                 | 414 ns: 3.54x slower                                                  |
| coverage                      | 41.2 ms                                                | 306 ms: 7.43x slower                                                  |
| thrift                        | 562 us                                                 | 44.1 ms: 78.49x slower                                                |
| Geometric mean                | (ref)                                                  | 1.11x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-darwin-arm64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.16x