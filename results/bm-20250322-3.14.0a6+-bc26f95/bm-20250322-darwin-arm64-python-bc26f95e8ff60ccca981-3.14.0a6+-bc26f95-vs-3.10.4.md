# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: darwin-arm64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.290x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 203 ms: 1.01x slower                                                   |
| docutils       | 1.74 sec                                               | 1.48 sec: 1.18x faster                                                 |
| html5lib       | 43.5 ms                                                | 32.6 ms: 1.33x faster                                                  |
| sphinx         | 729 ms                                                 | 596 ms: 1.22x faster                                                   |
| Geometric mean | (ref)                                                  | 1.18x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.7 ms: 5.97x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 143 ms: 3.37x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 397 ms: 2.57x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.34x faster                                                   |
| async_tree_none               | 391 ms                                                 | 171 ms: 2.28x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                   |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.19x faster                                                  |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.01x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 52.7 ms: 1.37x faster                                                  |
| nbody          | 92.5 ms                                                | 81.1 ms: 1.14x faster                                                  |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.16x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.9 ms: 1.28x faster                                                  |
| regex_dna      | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 221 us: 1.29x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 165 us: 1.20x faster                                                   |
| json_dumps           | 8.31 ms                                                | 7.48 ms: 1.11x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                  |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.83 ms: 1.25x faster                                                  |
| genshi_text     | 17.7 ms                                                | 15.6 ms: 1.14x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 32.2 ms: 1.09x faster                                                  |
| django_template | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.14x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.7 ms: 5.97x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 143 ms: 3.37x faster                                                   |
| typing_runtime_protocols      | 326 us                                                 | 100.0 us: 3.26x faster                                                 |
| subparsers                    | 39.8 ms                                                | 12.7 ms: 3.14x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 397 ms: 2.57x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.34x faster                                                   |
| async_tree_none               | 391 ms                                                 | 171 ms: 2.28x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.63 ms: 1.89x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| go                            | 163 ms                                                 | 92.7 ms: 1.76x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 20.4 us: 1.70x faster                                                  |
| deepcopy                      | 276 us                                                 | 162 us: 1.70x faster                                                   |
| raytrace                      | 327 ms                                                 | 192 ms: 1.70x faster                                                   |
| logging_silent                | 117 ns                                                 | 70.4 ns: 1.66x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 87.8 ms: 1.59x faster                                                  |
| chaos                         | 67.7 ms                                                | 43.8 ms: 1.55x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 47.0 ms: 1.54x faster                                                  |
| richards_super                | 61.0 ms                                                | 41.6 ms: 1.46x faster                                                  |
| richards                      | 52.3 ms                                                | 37.4 ms: 1.40x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.6 ms: 1.39x faster                                                  |
| pylint                        | 231 ms                                                 | 167 ms: 1.38x faster                                                   |
| float                         | 72.4 ms                                                | 52.7 ms: 1.37x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.73 us: 1.35x faster                                                  |
| comprehensions                | 17.3 us                                                | 12.9 us: 1.34x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.6 ms: 1.33x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.84 ms: 1.33x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 78.9 ms: 1.30x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.02 sec: 1.30x faster                                                 |
| logging_format                | 5.03 us                                                | 3.90 us: 1.29x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.29x faster                                                   |
| pprint_safe_repr              | 648 ms                                                 | 506 ms: 1.28x faster                                                   |
| pyflate                       | 448 ms                                                 | 350 ms: 1.28x faster                                                   |
| logging_simple                | 4.59 us                                                | 3.59 us: 1.28x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 74.9 ms: 1.28x faster                                                  |
| pycparser                     | 887 ms                                                 | 696 ms: 1.27x faster                                                   |
| generators                    | 31.7 ms                                                | 25.1 ms: 1.26x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.60 sec: 1.26x faster                                                 |
| mako                          | 9.81 ms                                                | 7.83 ms: 1.25x faster                                                  |
| hexiom                        | 6.25 ms                                                | 5.01 ms: 1.25x faster                                                  |
| regex_dna                     | 175 ms                                                 | 141 ms: 1.24x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 61.1 ms: 1.24x faster                                                  |
| thrift                        | 562 us                                                 | 455 us: 1.24x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                 |
| sphinx                        | 729 ms                                                 | 596 ms: 1.22x faster                                                   |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 60.6 ms: 1.21x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 165 us: 1.20x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 79.5 ms: 1.20x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 77.3 ms: 1.20x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.3 ms: 1.19x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.48 sec: 1.18x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 194 ms: 1.16x faster                                                   |
| nbody                         | 92.5 ms                                                | 81.1 ms: 1.14x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.6 ms: 1.14x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                  |
| sympy_str                     | 166 ms                                                 | 148 ms: 1.12x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.48 ms: 1.11x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.10 ms: 1.10x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 40.9 ms: 1.09x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 32.2 ms: 1.09x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.09x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.52 sec: 1.08x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 506 us: 1.08x faster                                                   |
| django_template               | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                  |
| pathlib                       | 25.7 ms                                                | 24.1 ms: 1.07x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.30 sec: 1.04x faster                                                 |
| many_optionals                | 486 us                                                 | 471 us: 1.03x faster                                                   |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 73.5 ms: 1.01x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 76.9 ms: 1.01x faster                                                  |
| connected_components          | 318 ms                                                 | 316 ms: 1.01x faster                                                   |
| fannkuch                      | 303 ms                                                 | 303 ms: 1.00x slower                                                   |
| 2to3                          | 201 ms                                                 | 203 ms: 1.01x slower                                                   |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                   |
| json                          | 3.10 ms                                                | 3.14 ms: 1.01x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.54 us: 1.04x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 56.2 ms: 1.04x slower                                                  |
| shortest_path                 | 328 ms                                                 | 342 ms: 1.04x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| nqueens                       | 63.8 ms                                                | 69.2 ms: 1.08x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.7 ms: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.29 ms: 1.11x slower                                                  |
| coverage                      | 41.2 ms                                                | 45.9 ms: 1.11x slower                                                  |
| async_generators              | 233 ms                                                 | 264 ms: 1.13x slower                                                   |
| gc_traversal                  | 2.71 ms                                                | 3.12 ms: 1.15x slower                                                  |
| telco                         | 3.49 ms                                                | 4.63 ms: 1.33x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.29x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250322-3.14.0a6+-bc26f95/bm-20250322-darwin-arm64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.290x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.15x