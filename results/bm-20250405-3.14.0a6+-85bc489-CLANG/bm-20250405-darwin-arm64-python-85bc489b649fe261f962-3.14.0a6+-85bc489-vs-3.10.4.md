# Results vs. 3.10.4

- fork: python
- ref: 85bc489b649fe261f962
- machine: darwin-arm64
- commit hash: 85bc489
- commit date: 2025-04-05
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.1 ms: 1.50x faster                                                  |
| sphinx         | 729 ms                                                 | 549 ms: 1.33x faster                                                   |
| Geometric mean | (ref)                                                  | 1.35x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.0 ms: 7.00x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.72x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 336 ms: 3.02x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 177 ms: 2.71x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.63x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 396 ms: 1.69x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| async_generators              | 233 ms                                                 | 254 ms: 1.09x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 43.0 ms: 1.68x faster                                                  |
| nbody          | 92.5 ms                                                | 71.8 ms: 1.29x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.3 ms: 1.56x faster                                                  |
| regex_dna      | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.3 ms: 1.30x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.17 ms: 1.16x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 69.7 ms: 1.07x faster                                                  |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.6 ms: 1.40x faster                                                  |
| mako            | 9.81 ms                                                | 7.33 ms: 1.34x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| django_template | 24.4 ms                                                | 19.5 ms: 1.25x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.33x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.0 ms: 7.00x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 86.7 us: 3.76x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 130 ms: 3.72x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.4 ms: 3.49x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 336 ms: 3.02x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 338 ms: 3.00x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 177 ms: 2.71x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.63x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.06 ms: 2.42x faster                                                  |
| mdp                           | 1.65 sec                                               | 688 ms: 2.40x faster                                                   |
| go                            | 163 ms                                                 | 70.9 ms: 2.30x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.1 us: 2.15x faster                                                  |
| raytrace                      | 327 ms                                                 | 157 ms: 2.08x faster                                                   |
| logging_silent                | 117 ns                                                 | 57.4 ns: 2.04x faster                                                  |
| deepcopy                      | 276 us                                                 | 139 us: 1.99x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.94x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 73.2 ms: 1.91x faster                                                  |
| chaos                         | 67.7 ms                                                | 36.0 ms: 1.88x faster                                                  |
| richards_super                | 61.0 ms                                                | 33.0 ms: 1.85x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 39.6 ms: 1.83x faster                                                  |
| richards                      | 52.3 ms                                                | 29.3 ms: 1.78x faster                                                  |
| comprehensions                | 17.3 us                                                | 10.1 us: 1.72x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 396 ms: 1.69x faster                                                   |
| float                         | 72.4 ms                                                | 43.0 ms: 1.68x faster                                                  |
| generators                    | 31.7 ms                                                | 19.1 ms: 1.66x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.80 ms: 1.64x faster                                                  |
| pyflate                       | 448 ms                                                 | 274 ms: 1.64x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.48 us: 1.57x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.3 ms: 1.56x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.96 us: 1.55x faster                                                  |
| logging_format                | 5.03 us                                                | 3.25 us: 1.55x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| pylint                        | 231 ms                                                 | 151 ms: 1.53x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 23.6 ms: 1.51x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.1 ms: 1.50x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.4 ms: 1.48x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.4 ms: 1.48x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.15 ms: 1.47x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 919 ms: 1.44x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 66.7 ms: 1.43x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 453 ms: 1.43x faster                                                   |
| pycparser                     | 887 ms                                                 | 625 ms: 1.42x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.6 ms: 1.40x faster                                                  |
| coroutines                    | 20.5 ms                                                | 14.7 ms: 1.39x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 55.3 ms: 1.37x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.49 sec: 1.35x faster                                                 |
| mako                          | 9.81 ms                                                | 7.33 ms: 1.34x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 69.3 ms: 1.34x faster                                                  |
| 2to3                          | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| sphinx                        | 729 ms                                                 | 549 ms: 1.33x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 26.7 ms: 1.32x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.0 ms: 1.31x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 34.3 ms: 1.30x faster                                                  |
| nbody                         | 92.5 ms                                                | 71.8 ms: 1.29x faster                                                  |
| sympy_str                     | 166 ms                                                 | 130 ms: 1.28x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| django_template               | 24.4 ms                                                | 19.5 ms: 1.25x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 217 ms: 1.24x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.81 sec: 1.22x faster                                                 |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.21x faster                                                   |
| nqueens                       | 63.8 ms                                                | 53.3 ms: 1.20x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 457 us: 1.19x faster                                                   |
| regex_dna                     | 175 ms                                                 | 148 ms: 1.18x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 192 ms: 1.17x faster                                                   |
| many_optionals                | 486 us                                                 | 419 us: 1.16x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.17 ms: 1.16x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.9 ms: 1.13x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.12x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.5 ms: 1.11x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.1 ms: 1.11x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 69.7 ms: 1.07x faster                                                  |
| connected_components          | 318 ms                                                 | 299 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.21 ms: 1.06x faster                                                  |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                  |
| python_startup                | 19.6 ms                                                | 19.2 ms: 1.02x faster                                                  |
| shortest_path                 | 328 ms                                                 | 325 ms: 1.01x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.52 us: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.0 ms: 1.07x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.26 ms: 1.09x slower                                                  |
| async_generators              | 233 ms                                                 | 254 ms: 1.09x slower                                                   |
| coverage                      | 41.2 ms                                                | 45.4 ms: 1.10x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.08 ms: 1.14x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.8 ms: 1.16x slower                                                  |
| telco                         | 3.49 ms                                                | 4.49 ms: 1.29x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (20) of results/bm-20250405-3.14.0a6+-85bc489-CLANG/bm-20250405-darwin-arm64-python-85bc489b649fe261f962-3.14.0a6+-85bc489.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.13x