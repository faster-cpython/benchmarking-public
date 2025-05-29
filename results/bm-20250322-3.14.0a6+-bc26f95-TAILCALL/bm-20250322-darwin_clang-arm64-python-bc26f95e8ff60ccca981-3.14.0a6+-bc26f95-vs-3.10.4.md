# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.435x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 152 ms: 1.32x faster                                                   |
| docutils       | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.6 ms: 1.47x faster                                                  |
| sphinx         | 729 ms                                                 | 556 ms: 1.31x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.8 ms: 6.90x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.64x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 342 ms: 2.97x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.57x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.6 ms: 1.40x faster                                                  |
| async_generators              | 233 ms                                                 | 255 ms: 1.10x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.21x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.3 ms: 1.63x faster                                                  |
| nbody          | 92.5 ms                                                | 64.8 ms: 1.43x faster                                                  |
| pidigits       | 280 ms                                                 | 279 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.33x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 64.0 ms: 1.49x faster                                                  |
| regex_dna      | 175 ms                                                 | 149 ms: 1.17x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.13x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.42 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| unpickle_pure_python | 198 us                                                 | 130 us: 1.52x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.18 sec: 1.46x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.4 ms: 1.30x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 98.5 ms: 1.11x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 49.7 ms: 1.09x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 69.8 ms: 1.07x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.3 ms: 1.07x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 13.0 ms: 1.37x faster                                                  |
| mako            | 9.81 ms                                                | 7.31 ms: 1.34x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 27.8 ms: 1.26x faster                                                  |
| django_template | 24.4 ms                                                | 19.4 ms: 1.26x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.31x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.8 ms: 6.90x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 88.2 us: 3.70x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 133 ms: 3.64x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.6 ms: 3.42x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 342 ms: 2.97x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 345 ms: 2.94x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.57x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.10 ms: 2.38x faster                                                  |
| go                            | 163 ms                                                 | 73.6 ms: 2.22x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.5 us: 2.11x faster                                                  |
| logging_silent                | 117 ns                                                 | 57.2 ns: 2.05x faster                                                  |
| raytrace                      | 327 ms                                                 | 165 ms: 1.99x faster                                                   |
| deepcopy                      | 276 us                                                 | 141 us: 1.96x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 71.9 ms: 1.95x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 345 ms: 1.94x faster                                                   |
| richards_super                | 61.0 ms                                                | 32.9 ms: 1.85x faster                                                  |
| chaos                         | 67.7 ms                                                | 36.9 ms: 1.83x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 40.1 ms: 1.81x faster                                                  |
| richards                      | 52.3 ms                                                | 29.7 ms: 1.76x faster                                                  |
| generators                    | 31.7 ms                                                | 18.3 ms: 1.73x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.2 us: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| float                         | 72.4 ms                                                | 44.3 ms: 1.63x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.91 ms: 1.60x faster                                                  |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 130 us: 1.52x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.53 us: 1.51x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 23.6 ms: 1.51x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.07 us: 1.50x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 64.0 ms: 1.49x faster                                                  |
| logging_format                | 5.03 us                                                | 3.38 us: 1.49x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 901 ms: 1.47x faster                                                   |
| html5lib                      | 43.5 ms                                                | 29.6 ms: 1.47x faster                                                  |
| pyflate                       | 448 ms                                                 | 306 ms: 1.46x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.18 sec: 1.46x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.21 ms: 1.46x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 446 ms: 1.45x faster                                                   |
| scimark_lu                    | 103 ms                                                 | 71.1 ms: 1.44x faster                                                  |
| nbody                         | 92.5 ms                                                | 64.8 ms: 1.43x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.6 ms: 1.40x faster                                                  |
| pycparser                     | 887 ms                                                 | 633 ms: 1.40x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 13.0 ms: 1.37x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.5 ms: 1.36x faster                                                  |
| thrift                        | 562 us                                                 | 415 us: 1.36x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 54.2 ms: 1.35x faster                                                  |
| mako                          | 9.81 ms                                                | 7.31 ms: 1.34x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                 |
| 2to3                          | 201 ms                                                 | 152 ms: 1.32x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 70.2 ms: 1.32x faster                                                  |
| sphinx                        | 729 ms                                                 | 556 ms: 1.31x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 34.4 ms: 1.30x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.3 ms: 1.28x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 74.4 ms: 1.28x faster                                                  |
| sympy_str                     | 166 ms                                                 | 131 ms: 1.27x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 27.8 ms: 1.26x faster                                                  |
| django_template               | 24.4 ms                                                | 19.4 ms: 1.26x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.39 sec: 1.25x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 182 ms: 1.24x faster                                                   |
| sympy_expand                  | 269 ms                                                 | 220 ms: 1.22x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 461 us: 1.18x faster                                                   |
| regex_dna                     | 175 ms                                                 | 149 ms: 1.17x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.93 ms: 1.17x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.16x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                  |
| many_optionals                | 486 us                                                 | 428 us: 1.14x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 3.03 sec: 1.13x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.13x faster                                                  |
| fannkuch                      | 303 ms                                                 | 270 ms: 1.12x faster                                                   |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 98.5 ms: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.3 ms: 1.11x faster                                                  |
| nqueens                       | 63.8 ms                                                | 57.9 ms: 1.10x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 49.7 ms: 1.09x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.3 ms: 1.07x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 69.8 ms: 1.07x faster                                                  |
| connected_components          | 318 ms                                                 | 300 ms: 1.06x faster                                                   |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                  |
| shortest_path                 | 328 ms                                                 | 326 ms: 1.01x faster                                                   |
| pidigits                      | 280 ms                                                 | 279 ms: 1.00x faster                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.51 us: 1.02x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.42 ms: 1.04x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.8 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.8 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 255 ms: 1.10x slower                                                   |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.1 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.43x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250322-3.14.0a6+-bc26f95-CLANG/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.435x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.14x