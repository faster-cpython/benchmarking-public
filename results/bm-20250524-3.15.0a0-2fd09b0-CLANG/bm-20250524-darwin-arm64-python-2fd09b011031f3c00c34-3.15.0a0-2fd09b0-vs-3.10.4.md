# Results vs. 3.10.4

- fork: python
- ref: 2fd09b011031f3c00c34
- machine: darwin-arm64
- commit hash: 2fd09b0
- commit date: 2025-05-24
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 157 ms: 1.28x faster                                                  |
| docutils       | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                |
| html5lib       | 43.5 ms                                                | 30.8 ms: 1.41x faster                                                 |
| sphinx         | 729 ms                                                 | 551 ms: 1.32x faster                                                  |
| Geometric mean | (ref)                                                  | 1.32x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.2 ms: 6.85x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.62x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 342 ms: 2.97x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 178 ms: 2.70x faster                                                  |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                  |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.20x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                 |
| nbody          | 92.5 ms                                                | 73.0 ms: 1.27x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.4 ms: 1.56x faster                                                 |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| regex_dna      | 175 ms                                                 | 144 ms: 1.21x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.27x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 130 us: 1.53x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 188 us: 1.52x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.18 sec: 1.45x faster                                                |
| json_dumps           | 8.31 ms                                                | 6.08 ms: 1.37x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.9 ms: 1.28x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 70.5 ms: 1.06x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| json_loads           | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.0 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.8 ms: 1.38x faster                                                 |
| mako            | 9.81 ms                                                | 7.20 ms: 1.36x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 27.1 ms: 1.30x faster                                                 |
| django_template | 24.4 ms                                                | 19.5 ms: 1.25x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.32x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 57.2 ms: 6.85x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 88.9 us: 3.67x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.62x faster                                                  |
| subparsers                    | 39.8 ms                                                | 13.0 ms: 3.07x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.02x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 342 ms: 2.97x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 178 ms: 2.70x faster                                                  |
| async_tree_none               | 391 ms                                                 | 150 ms: 2.61x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.07 ms: 2.41x faster                                                 |
| mdp                           | 1.65 sec                                               | 700 ms: 2.36x faster                                                  |
| go                            | 163 ms                                                 | 71.5 ms: 2.29x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 16.5 us: 2.10x faster                                                 |
| raytrace                      | 327 ms                                                 | 160 ms: 2.04x faster                                                  |
| deepcopy                      | 276 us                                                 | 145 us: 1.91x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 351 ms: 1.91x faster                                                  |
| chaos                         | 67.7 ms                                                | 35.9 ms: 1.89x faster                                                 |
| richards_super                | 61.0 ms                                                | 32.9 ms: 1.85x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 75.9 ms: 1.84x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 39.9 ms: 1.82x faster                                                 |
| richards                      | 52.3 ms                                                | 29.2 ms: 1.79x faster                                                 |
| generators                    | 31.7 ms                                                | 18.9 ms: 1.68x faster                                                 |
| hexiom                        | 6.25 ms                                                | 3.75 ms: 1.67x faster                                                 |
| comprehensions                | 17.3 us                                                | 10.4 us: 1.66x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 405 ms: 1.65x faster                                                  |
| float                         | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                 |
| pyflate                       | 448 ms                                                 | 276 ms: 1.62x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.4 ms: 1.56x faster                                                 |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 130 us: 1.53x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 188 us: 1.52x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.7 ms: 1.50x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.57 us: 1.48x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.8 ms: 1.47x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 69.7 ms: 1.47x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.18 sec: 1.45x faster                                                |
| pycparser                     | 887 ms                                                 | 621 ms: 1.43x faster                                                  |
| html5lib                      | 43.5 ms                                                | 30.8 ms: 1.41x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.26 us: 1.41x faster                                                 |
| logging_format                | 5.03 us                                                | 3.58 us: 1.41x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 68.4 ms: 1.39x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 12.8 ms: 1.38x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 969 ms: 1.37x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 6.08 ms: 1.37x faster                                                 |
| mako                          | 9.81 ms                                                | 7.20 ms: 1.36x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 479 ms: 1.35x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 69.1 ms: 1.34x faster                                                 |
| coroutines                    | 20.5 ms                                                | 15.3 ms: 1.34x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                |
| sphinx                        | 729 ms                                                 | 551 ms: 1.32x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.0 ms: 1.31x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 27.1 ms: 1.30x faster                                                 |
| 2to3                          | 201 ms                                                 | 157 ms: 1.28x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.9 ms: 1.28x faster                                                 |
| sympy_str                     | 166 ms                                                 | 130 ms: 1.28x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.37 sec: 1.27x faster                                                |
| nbody                         | 92.5 ms                                                | 73.0 ms: 1.27x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| django_template               | 24.4 ms                                                | 19.5 ms: 1.25x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 221 ms: 1.22x faster                                                  |
| regex_dna                     | 175 ms                                                 | 144 ms: 1.21x faster                                                  |
| fannkuch                      | 303 ms                                                 | 250 ms: 1.21x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.92 sec: 1.18x faster                                                |
| nqueens                       | 63.8 ms                                                | 55.2 ms: 1.16x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 472 us: 1.15x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                  |
| many_optionals                | 486 us                                                 | 439 us: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.8 ms: 1.10x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.2 ms: 1.06x faster                                                 |
| connected_components          | 318 ms                                                 | 301 ms: 1.06x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 70.5 ms: 1.06x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.24 ms: 1.05x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 104 ms: 1.05x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.0 ms: 1.04x faster                                                 |
| json                          | 3.10 ms                                                | 3.06 ms: 1.02x faster                                                 |
| shortest_path                 | 328 ms                                                 | 327 ms: 1.00x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| dask                          | 789 ms                                                 | 798 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.4 us: 1.11x slower                                                 |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.6 ms: 1.14x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.34 ms: 1.15x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 69.6 ms: 1.24x slower                                                 |
| telco                         | 3.49 ms                                                | 4.45 ms: 1.28x slower                                                 |
| logging_silent                | 117 ns                                                 | 292 ns: 2.50x slower                                                  |
| coverage                      | 41.2 ms                                                | 235 ms: 5.71x slower                                                  |
| thrift                        | 562 us                                                 | 43.1 ms: 76.66x slower                                                |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250524-3.15.0a0-2fd09b0-CLANG/bm-20250524-darwin-arm64-python-2fd09b011031f3c00c34-3.15.0a0-2fd09b0.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.17x