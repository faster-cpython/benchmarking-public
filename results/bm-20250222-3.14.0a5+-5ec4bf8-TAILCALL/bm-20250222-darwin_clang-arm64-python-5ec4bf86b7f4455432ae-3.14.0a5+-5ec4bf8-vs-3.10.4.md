# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.473x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.29x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| docutils       | 1.74 sec                                               | 1.35 sec: 1.29x faster                                                 |
| html5lib       | 43.5 ms                                                | 28.7 ms: 1.51x faster                                                  |
| sphinx         | 729 ms                                                 | 537 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.8 ms: 6.90x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.65x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.03x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.63x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.95x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| async_generators              | 233 ms                                                 | 234 ms: 1.00x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                  |
| nbody          | 92.5 ms                                                | 63.9 ms: 1.45x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 61.5 ms: 1.55x faster                                                  |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.8 ms: 1.08x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 124 us: 1.60x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 183 us: 1.55x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 98.2 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                  |
| json_loads           | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.25x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.9 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| mako            | 9.81 ms                                                | 7.06 ms: 1.39x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.9 ms: 1.31x faster                                                  |
| django_template | 24.4 ms                                                | 18.7 ms: 1.30x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 56.8 ms: 6.90x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 83.4 us: 3.91x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 132 ms: 3.65x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.52x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 335 ms: 3.03x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 338 ms: 3.01x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 181 ms: 2.66x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.63x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.03 ms: 2.46x faster                                                  |
| go                            | 163 ms                                                 | 70.3 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.4 us: 2.11x faster                                                  |
| logging_silent                | 117 ns                                                 | 57.1 ns: 2.05x faster                                                  |
| raytrace                      | 327 ms                                                 | 161 ms: 2.03x faster                                                   |
| deepcopy                      | 276 us                                                 | 139 us: 1.98x faster                                                   |
| richards_super                | 61.0 ms                                                | 30.9 ms: 1.97x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 694 us: 1.95x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 344 ms: 1.95x faster                                                   |
| chaos                         | 67.7 ms                                                | 34.9 ms: 1.94x faster                                                  |
| richards                      | 52.3 ms                                                | 27.4 ms: 1.91x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 74.4 ms: 1.88x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 842 us: 1.85x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 39.7 ms: 1.82x faster                                                  |
| generators                    | 31.7 ms                                                | 17.7 ms: 1.79x faster                                                  |
| comprehensions                | 17.3 us                                                | 9.76 us: 1.77x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 400 ms: 1.67x faster                                                   |
| hexiom                        | 6.25 ms                                                | 3.76 ms: 1.66x faster                                                  |
| float                         | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 124 us: 1.60x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.47 us: 1.58x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.94 us: 1.56x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 61.5 ms: 1.55x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                   |
| pickle_pure_python            | 285 us                                                 | 183 us: 1.55x faster                                                   |
| logging_format                | 5.03 us                                                | 3.25 us: 1.55x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 867 ms: 1.53x faster                                                   |
| pyflate                       | 448 ms                                                 | 294 ms: 1.52x faster                                                   |
| html5lib                      | 43.5 ms                                                | 28.7 ms: 1.51x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.05 ms: 1.50x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 433 ms: 1.50x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 49.3 ms: 1.49x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.9 ms: 1.47x faster                                                  |
| nbody                         | 92.5 ms                                                | 63.9 ms: 1.45x faster                                                  |
| pycparser                     | 887 ms                                                 | 614 ms: 1.44x faster                                                   |
| spectral_norm                 | 95.3 ms                                                | 67.6 ms: 1.41x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 12.6 ms: 1.41x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.0 ms: 1.40x faster                                                  |
| mako                          | 9.81 ms                                                | 7.06 ms: 1.39x faster                                                  |
| thrift                        | 562 us                                                 | 410 us: 1.37x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                 |
| sphinx                        | 729 ms                                                 | 537 ms: 1.36x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 26.4 ms: 1.35x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 68.9 ms: 1.34x faster                                                  |
| 2to3                          | 201 ms                                                 | 151 ms: 1.33x faster                                                   |
| xml_etree_process             | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.9 ms: 1.31x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.31x faster                                                  |
| sympy_str                     | 166 ms                                                 | 127 ms: 1.31x faster                                                   |
| django_template               | 24.4 ms                                                | 18.7 ms: 1.30x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 174 ms: 1.30x faster                                                   |
| docutils                      | 1.74 sec                                               | 1.35 sec: 1.29x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 214 ms: 1.26x faster                                                   |
| nqueens                       | 63.8 ms                                                | 51.0 ms: 1.25x faster                                                  |
| sqlglot_optimize              | 37.2 ms                                                | 29.7 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.75 ms: 1.24x faster                                                  |
| fannkuch                      | 303 ms                                                 | 246 ms: 1.23x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.83 sec: 1.21x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 454 us: 1.20x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 163 ms: 1.18x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.09 ms: 1.17x faster                                                  |
| many_optionals                | 486 us                                                 | 418 us: 1.16x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.42 sec: 1.16x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.14x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 98.2 ms: 1.12x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 70.1 ms: 1.11x faster                                                  |
| connected_components          | 318 ms                                                 | 294 ms: 1.08x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 68.9 ms: 1.08x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.8 ms: 1.08x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.5 ms: 1.06x faster                                                  |
| json                          | 3.10 ms                                                | 3.02 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| shortest_path                 | 328 ms                                                 | 321 ms: 1.02x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 234 ms: 1.00x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.51 us: 1.02x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 59.4 ms: 1.06x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.7 us: 1.07x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.25 ms: 1.07x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.9 ms: 1.08x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.8 ms: 1.09x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.06 ms: 1.13x slower                                                  |
| telco                         | 3.49 ms                                                | 4.41 ms: 1.26x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250222-3.14.0a5+-5ec4bf8-CLANG/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.473x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.29x

# Memory
- memory change: 1.12x