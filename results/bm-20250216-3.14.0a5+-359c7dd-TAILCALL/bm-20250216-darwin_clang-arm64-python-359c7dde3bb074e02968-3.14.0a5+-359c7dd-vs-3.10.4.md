# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: darwin-arm64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.466x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 153 ms: 1.31x faster                                                   |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                  |
| sphinx         | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                  | 1.36x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.9 ms: 6.65x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.97x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 344 ms: 2.95x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.57x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 349 ms: 1.92x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 401 ms: 1.67x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.37x faster                                                  |
| async_generators              | 233 ms                                                 | 252 ms: 1.08x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.20x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.4 ms: 1.63x faster                                                  |
| nbody          | 92.5 ms                                                | 62.8 ms: 1.47x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.7 ms: 1.55x faster                                                  |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 124 us: 1.60x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 186 us: 1.53x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| xml_etree_iterparse  | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                  |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| mako            | 9.81 ms                                                | 7.14 ms: 1.37x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.7 ms: 1.31x faster                                                  |
| django_template | 24.4 ms                                                | 18.8 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 58.9 ms: 6.65x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 85.3 us: 3.82x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 135 ms: 3.58x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.53x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.97x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 344 ms: 2.95x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 183 ms: 2.63x faster                                                   |
| async_tree_none               | 391 ms                                                 | 152 ms: 2.57x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.05 ms: 2.43x faster                                                  |
| go                            | 163 ms                                                 | 70.6 ms: 2.31x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.6 us: 2.09x faster                                                  |
| logging_silent                | 117 ns                                                 | 57.5 ns: 2.04x faster                                                  |
| raytrace                      | 327 ms                                                 | 163 ms: 2.01x faster                                                   |
| deepcopy                      | 276 us                                                 | 139 us: 1.98x faster                                                   |
| richards_super                | 61.0 ms                                                | 31.2 ms: 1.95x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 698 us: 1.93x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 349 ms: 1.92x faster                                                   |
| chaos                         | 67.7 ms                                                | 35.5 ms: 1.91x faster                                                  |
| richards                      | 52.3 ms                                                | 27.6 ms: 1.89x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 74.4 ms: 1.88x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 846 us: 1.84x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 39.5 ms: 1.83x faster                                                  |
| generators                    | 31.7 ms                                                | 17.7 ms: 1.79x faster                                                  |
| comprehensions                | 17.3 us                                                | 9.74 us: 1.78x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 401 ms: 1.67x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.79 ms: 1.65x faster                                                  |
| float                         | 72.4 ms                                                | 44.4 ms: 1.63x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 124 us: 1.60x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.48 us: 1.56x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.95 us: 1.56x faster                                                  |
| logging_format                | 5.03 us                                                | 3.23 us: 1.56x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                   |
| regex_compile                 | 95.6 ms                                                | 61.7 ms: 1.55x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 186 us: 1.53x faster                                                   |
| pyflate                       | 448 ms                                                 | 295 ms: 1.52x faster                                                   |
| pprint_pformat                | 1.33 sec                                               | 874 ms: 1.52x faster                                                   |
| html5lib                      | 43.5 ms                                                | 28.9 ms: 1.51x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.15 sec: 1.49x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.07 ms: 1.49x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 435 ms: 1.49x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 49.5 ms: 1.48x faster                                                  |
| nbody                         | 92.5 ms                                                | 62.8 ms: 1.47x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 71.0 ms: 1.45x faster                                                  |
| pycparser                     | 887 ms                                                 | 615 ms: 1.44x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 67.9 ms: 1.40x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.1 ms: 1.40x faster                                                  |
| thrift                        | 562 us                                                 | 408 us: 1.38x faster                                                   |
| coroutines                    | 20.5 ms                                                | 14.9 ms: 1.37x faster                                                  |
| mako                          | 9.81 ms                                                | 7.14 ms: 1.37x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                 |
| sphinx                        | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 69.0 ms: 1.34x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 26.5 ms: 1.34x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.7 ms: 1.31x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 172 ms: 1.31x faster                                                   |
| 2to3                          | 201 ms                                                 | 153 ms: 1.31x faster                                                   |
| django_template               | 24.4 ms                                                | 18.8 ms: 1.30x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.2 ms: 1.29x faster                                                  |
| sympy_str                     | 166 ms                                                 | 129 ms: 1.29x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.73 ms: 1.25x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 29.8 ms: 1.25x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 216 ms: 1.24x faster                                                   |
| nqueens                       | 63.8 ms                                                | 51.3 ms: 1.24x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.83 sec: 1.21x faster                                                 |
| fannkuch                      | 303 ms                                                 | 250 ms: 1.21x faster                                                   |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 455 us: 1.20x faster                                                   |
| many_optionals                | 486 us                                                 | 414 us: 1.17x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 164 ms: 1.17x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.2 ms: 1.16x faster                                                  |
| mdp                           | 1.65 sec                                               | 1.43 sec: 1.15x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.7 ms: 1.10x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                  |
| connected_components          | 318 ms                                                 | 296 ms: 1.07x faster                                                   |
| dask                          | 789 ms                                                 | 770 ms: 1.03x faster                                                   |
| json                          | 3.10 ms                                                | 3.03 ms: 1.03x faster                                                  |
| shortest_path                 | 328 ms                                                 | 323 ms: 1.02x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.50 us: 1.01x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 58.1 ms: 1.04x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| async_generators              | 233 ms                                                 | 252 ms: 1.08x slower                                                   |
| coverage                      | 41.2 ms                                                | 44.6 ms: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.07 ms: 1.13x slower                                                  |
| telco                         | 3.49 ms                                                | 4.52 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.46x faster                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250216-3.14.0a5+-359c7dd-CLANG/bm-20250216-darwin-arm64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.466x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.12x