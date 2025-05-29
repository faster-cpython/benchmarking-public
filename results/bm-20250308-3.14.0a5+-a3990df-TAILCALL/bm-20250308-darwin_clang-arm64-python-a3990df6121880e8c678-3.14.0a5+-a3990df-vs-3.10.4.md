# Results vs. 3.10.4

- fork: python
- ref: a3990df6121880e8c678
- machine: darwin-arm64
- commit hash: a3990df
- commit date: 2025-03-08
- overall geometric mean: 1.470x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 150 ms: 1.34x faster                                                   |
| docutils       | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| html5lib       | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| sphinx         | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| Geometric mean | (ref)                                                  | 1.37x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.7 ms: 7.04x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.68x faster                                                   |
| async_tree_eager_io           | 1.01 sec                                               | 331 ms: 3.06x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 182 ms: 2.64x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.62x faster                                                   |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 343 ms: 1.95x faster                                                   |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| async_generators              | 233 ms                                                 | 235 ms: 1.01x slower                                                   |
| Geometric mean                | (ref)                                                  | 2.24x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                  |
| nbody          | 92.5 ms                                                | 63.7 ms: 1.45x faster                                                  |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.34x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 62.1 ms: 1.54x faster                                                  |
| regex_dna      | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| regex_v8       | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                  |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 123 us: 1.62x faster                                                   |
| pickle_pure_python   | 285 us                                                 | 184 us: 1.55x faster                                                   |
| tomli_loads          | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 33.3 ms: 1.34x faster                                                  |
| json_dumps           | 8.31 ms                                                | 7.13 ms: 1.16x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| json_loads           | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                  |
| python_startup_no_site | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 12.5 ms: 1.42x faster                                                  |
| mako            | 9.81 ms                                                | 7.10 ms: 1.38x faster                                                  |
| genshi_xml      | 35.1 ms                                                | 26.7 ms: 1.31x faster                                                  |
| django_template | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.35x faster                                                           |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df |
|-------------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 55.7 ms: 7.04x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 83.4 us: 3.91x faster                                                  |
| async_tree_eager_memoization  | 483 ms                                                 | 131 ms: 3.68x faster                                                   |
| subparsers                    | 39.8 ms                                                | 11.3 ms: 3.52x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 331 ms: 3.06x faster                                                   |
| async_tree_io                 | 1.02 sec                                               | 343 ms: 2.96x faster                                                   |
| async_tree_memoization        | 481 ms                                                 | 182 ms: 2.64x faster                                                   |
| async_tree_none               | 391 ms                                                 | 149 ms: 2.62x faster                                                   |
| deltablue                     | 4.99 ms                                                | 2.05 ms: 2.44x faster                                                  |
| go                            | 163 ms                                                 | 70.5 ms: 2.32x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 16.3 us: 2.13x faster                                                  |
| raytrace                      | 327 ms                                                 | 161 ms: 2.03x faster                                                   |
| deepcopy                      | 276 us                                                 | 138 us: 1.99x faster                                                   |
| logging_silent                | 117 ns                                                 | 59.2 ns: 1.98x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 343 ms: 1.95x faster                                                   |
| richards_super                | 61.0 ms                                                | 31.4 ms: 1.94x faster                                                  |
| chaos                         | 67.7 ms                                                | 34.9 ms: 1.94x faster                                                  |
| sqlglot_parse                 | 1.35 ms                                                | 696 us: 1.94x faster                                                   |
| scimark_sor                   | 140 ms                                                 | 74.3 ms: 1.88x faster                                                  |
| richards                      | 52.3 ms                                                | 27.8 ms: 1.88x faster                                                  |
| sqlglot_transpile             | 1.56 ms                                                | 843 us: 1.85x faster                                                   |
| scimark_monte_carlo           | 72.4 ms                                                | 39.4 ms: 1.84x faster                                                  |
| comprehensions                | 17.3 us                                                | 9.76 us: 1.77x faster                                                  |
| generators                    | 31.7 ms                                                | 18.0 ms: 1.76x faster                                                  |
| hexiom                        | 6.25 ms                                                | 3.79 ms: 1.65x faster                                                  |
| float                         | 72.4 ms                                                | 44.0 ms: 1.65x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                                   |
| unpickle_pure_python          | 198 us                                                 | 123 us: 1.62x faster                                                   |
| deepcopy_reduce               | 2.32 us                                                | 1.47 us: 1.58x faster                                                  |
| logging_simple                | 4.59 us                                                | 2.95 us: 1.56x faster                                                  |
| pylint                        | 231 ms                                                 | 149 ms: 1.55x faster                                                   |
| logging_format                | 5.03 us                                                | 3.24 us: 1.55x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 184 us: 1.55x faster                                                   |
| dulwich_log                   | 35.6 ms                                                | 23.0 ms: 1.55x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 62.1 ms: 1.54x faster                                                  |
| pyflate                       | 448 ms                                                 | 295 ms: 1.52x faster                                                   |
| tomli_loads                   | 1.72 sec                                               | 1.14 sec: 1.51x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 882 ms: 1.51x faster                                                   |
| html5lib                      | 43.5 ms                                                | 29.0 ms: 1.50x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 49.3 ms: 1.49x faster                                                  |
| sqlalchemy_imperative         | 9.07 ms                                                | 6.10 ms: 1.49x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 69.2 ms: 1.48x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 443 ms: 1.46x faster                                                   |
| nbody                         | 92.5 ms                                                | 63.7 ms: 1.45x faster                                                  |
| pycparser                     | 887 ms                                                 | 617 ms: 1.44x faster                                                   |
| genshi_text                   | 17.7 ms                                                | 12.5 ms: 1.42x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 67.9 ms: 1.40x faster                                                  |
| sqlalchemy_declarative        | 75.7 ms                                                | 54.5 ms: 1.39x faster                                                  |
| mako                          | 9.81 ms                                                | 7.10 ms: 1.38x faster                                                  |
| thrift                        | 562 us                                                 | 407 us: 1.38x faster                                                   |
| coroutines                    | 20.5 ms                                                | 15.0 ms: 1.37x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.36x faster                                                 |
| sphinx                        | 729 ms                                                 | 540 ms: 1.35x faster                                                   |
| 2to3                          | 201 ms                                                 | 150 ms: 1.34x faster                                                   |
| sympy_sum                     | 92.7 ms                                                | 69.2 ms: 1.34x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 33.3 ms: 1.34x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 26.7 ms: 1.31x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 174 ms: 1.30x faster                                                   |
| sympy_integrate               | 13.2 ms                                                | 10.1 ms: 1.30x faster                                                  |
| sympy_str                     | 166 ms                                                 | 128 ms: 1.30x faster                                                   |
| django_template               | 24.4 ms                                                | 18.8 ms: 1.29x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.36 sec: 1.28x faster                                                 |
| nqueens                       | 63.8 ms                                                | 50.8 ms: 1.26x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 2.73 ms: 1.25x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 216 ms: 1.25x faster                                                   |
| sqlglot_optimize              | 37.2 ms                                                | 29.8 ms: 1.25x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.83 sec: 1.21x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.20x faster                                                   |
| bench_thread_pool             | 545 us                                                 | 454 us: 1.20x faster                                                   |
| fannkuch                      | 303 ms                                                 | 254 ms: 1.19x faster                                                   |
| sqlglot_normalize             | 192 ms                                                 | 163 ms: 1.18x faster                                                   |
| json_dumps                    | 8.31 ms                                                | 7.13 ms: 1.16x faster                                                  |
| many_optionals                | 486 us                                                 | 418 us: 1.16x faster                                                   |
| mdp                           | 1.65 sec                                               | 1.42 sec: 1.16x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.6 ms: 1.14x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 68.8 ms: 1.13x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 48.1 ms: 1.12x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.6 ms: 1.09x faster                                                  |
| connected_components          | 318 ms                                                 | 293 ms: 1.08x faster                                                   |
| xml_etree_iterparse           | 74.5 ms                                                | 68.8 ms: 1.08x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                   |
| json                          | 3.10 ms                                                | 3.00 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 767 ms: 1.03x faster                                                   |
| shortest_path                 | 328 ms                                                 | 320 ms: 1.02x faster                                                   |
| python_startup                | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x faster                                                   |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                   |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 235 ms: 1.01x slower                                                   |
| sqlite_synth                  | 1.48 us                                                | 1.50 us: 1.01x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 60.4 ms: 1.08x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.9 us: 1.08x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.26 ms: 1.08x slower                                                  |
| coverage                      | 41.2 ms                                                | 44.8 ms: 1.09x slower                                                  |
| gc_traversal                  | 2.71 ms                                                | 3.07 ms: 1.13x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                  |
| telco                         | 3.49 ms                                                | 4.38 ms: 1.25x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.47x faster                                                           |
Ignored benchmarks (4) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, tornado_http
Ignored benchmarks (16) of results/bm-20250308-3.14.0a5+-a3990df-CLANG/bm-20250308-darwin-arm64-python-a3990df6121880e8c678-3.14.0a5+-a3990df.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.470x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.13x