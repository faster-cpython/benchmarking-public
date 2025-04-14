# Results vs. 3.10.4

- fork: python
- ref: 5ec4bf86b7f4455432ae
- machine: darwin-arm64
- commit hash: 5ec4bf8
- commit date: 2025-02-22
- overall geometric mean: 1.371x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 166 ms: 1.21x faster                                                   |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                  |
| sphinx         | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| Geometric mean | (ref)                                                  | 1.28x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.8 ms: 6.24x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                  |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.08x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.4 ms: 1.53x faster                                                  |
| nbody          | 92.5 ms                                                | 64.6 ms: 1.43x faster                                                  |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| Geometric mean | (ref)                                                  | 1.29x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.9 ms: 1.39x faster                                                  |
| regex_dna      | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| regex_v8       | 19.1 ms                                                | 16.7 ms: 1.15x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 197 us: 1.45x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 35.8 ms: 1.25x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.23 ms: 1.15x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| xml_etree_generate   | 53.9 ms                                                | 50.8 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                  |
| json_loads           | 16.6 us                                                | 17.6 us: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.3 ms: 1.08x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                  |
| genshi_text     | 17.7 ms                                                | 13.9 ms: 1.27x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 29.2 ms: 1.21x faster                                                  |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8 |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.8 ms: 6.24x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 92.2 us: 3.53x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.42x faster                                                   |
| subparsers                    | 39.8 ms                                                | 12.0 ms: 3.31x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 371 ms: 2.74x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.46x faster                                                   |
| async_tree_none               | 391 ms                                                 | 161 ms: 2.43x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.37 ms: 2.10x faster                                                  |
| go                            | 163 ms                                                 | 81.0 ms: 2.02x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 18.2 us: 1.91x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                   |
| raytrace                      | 327 ms                                                 | 178 ms: 1.84x faster                                                   |
| deepcopy                      | 276 us                                                 | 151 us: 1.83x faster                                                   |
| logging_silent                | 117 ns                                                 | 65.1 ns: 1.80x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 79.8 ms: 1.75x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.2 ms: 1.73x faster                                                  |
| richards_super                | 61.0 ms                                                | 36.3 ms: 1.68x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 43.3 ms: 1.67x faster                                                  |
| richards                      | 52.3 ms                                                | 32.1 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                   |
| sqlglot_parse                 | 1.35 ms                                                | 861 us: 1.57x faster                                                   |
| float                         | 72.4 ms                                                | 47.4 ms: 1.53x faster                                                  |
| mako                          | 9.81 ms                                                | 6.47 ms: 1.52x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 1.03 ms: 1.52x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.4 us: 1.51x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.57 us: 1.48x faster                                                  |
| pyflate                       | 448 ms                                                 | 307 ms: 1.46x faster                                                   |
| html5lib                      | 43.5 ms                                                | 29.8 ms: 1.46x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 197 us: 1.45x faster                                                   |
| nbody                         | 92.5 ms                                                | 64.6 ms: 1.43x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.20 sec: 1.43x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.37 ms: 1.43x faster                                                  |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                   |
| logging_format                | 5.03 us                                                | 3.54 us: 1.42x faster                                                  |
| logging_simple                | 4.59 us                                                | 3.23 us: 1.42x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 73.2 ms: 1.40x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 68.9 ms: 1.39x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 977 ms: 1.36x faster                                                   |
| generators                    | 31.7 ms                                                | 23.3 ms: 1.36x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.67 ms: 1.36x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 71.2 ms: 1.34x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 488 ms: 1.33x faster                                                   |
| crypto_pyaes                  | 73.3 ms                                                | 55.3 ms: 1.32x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                 |
| pycparser                     | 887 ms                                                 | 674 ms: 1.32x faster                                                   |
| sqlalchemy_declarative        | 75.7 ms                                                | 58.7 ms: 1.29x faster                                                  |
| thrift                        | 562 us                                                 | 437 us: 1.29x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 13.9 ms: 1.27x faster                                                  |
| sphinx                        | 729 ms                                                 | 575 ms: 1.27x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 28.1 ms: 1.27x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 73.7 ms: 1.26x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.8 ms: 1.25x faster                                                  |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.24x faster                                                   |
| scimark_fft                   | 225 ms                                                 | 182 ms: 1.24x faster                                                   |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                  |
| 2to3                          | 201 ms                                                 | 166 ms: 1.21x faster                                                   |
| genshi_xml                    | 35.1 ms                                                | 29.2 ms: 1.21x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                 |
| sympy_str                     | 166 ms                                                 | 141 ms: 1.18x faster                                                   |
| bpe_tokeniser                 | 3.44 sec                                               | 2.94 sec: 1.17x faster                                                 |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.16x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.96 ms: 1.15x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.7 ms: 1.15x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.23 ms: 1.15x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 239 ms: 1.13x faster                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 33.1 ms: 1.12x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 490 us: 1.11x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.51 sec: 1.10x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.5 ms: 1.10x faster                                                  |
| nqueens                       | 63.8 ms                                                | 58.4 ms: 1.09x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.3 ms: 1.08x faster                                                  |
| fannkuch                      | 303 ms                                                 | 282 ms: 1.07x faster                                                   |
| many_optionals                | 486 us                                                 | 453 us: 1.07x faster                                                   |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 180 ms: 1.07x faster                                                   |
| xml_etree_generate            | 53.9 ms                                                | 50.8 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 301 ms: 1.06x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 74.8 ms: 1.04x faster                                                  |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.27 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                   |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                   |
| shortest_path                 | 328 ms                                                 | 338 ms: 1.03x slower                                                   |
| python_startup_no_site        | 12.8 ms                                                | 13.3 ms: 1.04x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.55 us: 1.05x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.6 us: 1.06x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.8 ms: 1.09x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.27 ms: 1.09x slower                                                  |
| coverage                      | 41.2 ms                                                | 46.0 ms: 1.12x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.09 ms: 1.14x slower                                                  |
| async_generators              | 233 ms                                                 | 271 ms: 1.16x slower                                                   |
| telco                         | 3.49 ms                                                | 4.52 ms: 1.30x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                           |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250222-3.14.0a5+-5ec4bf8-JIT/bm-20250222-darwin-arm64-python-5ec4bf86b7f4455432ae-3.14.0a5+-5ec4bf8.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.371x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.15x