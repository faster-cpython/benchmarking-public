# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.539x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 226 ms: 1.12x slower                                                  |
| docutils       | 1.74 sec                                               | 1.67 sec: 1.04x faster                                                |
| html5lib       | 43.5 ms                                                | 33.4 ms: 1.30x faster                                                 |
| sphinx         | 729 ms                                                 | 659 ms: 1.11x faster                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 406 ms: 2.51x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                  |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 395 ms: 1.70x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 454 ms: 1.47x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 331 ms: 1.42x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.89x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.2 ms: 1.47x faster                                                 |
| nbody          | 92.5 ms                                                | 77.9 ms: 1.19x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 68.1 ms: 1.40x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.21 ms: 1.06x faster                                                 |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 151 us: 1.31x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 221 us: 1.28x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| json_dumps           | 8.31 ms                                                | 8.02 ms: 1.04x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 77.5 ms: 1.04x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 63.9 ms: 1.18x slower                                                 |
| json_loads           | 16.6 us                                                | 22.6 us: 1.37x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.8 ms: 1.11x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.24 ms: 1.19x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.7 ms: 1.04x faster                                                 |
| django_template | 24.4 ms                                                | 25.8 ms: 1.06x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat                | 1.33 sec                                               | 1.01 us: 1312171.79x faster                                           |
| pprint_safe_repr              | 648 ms                                                 | 590 ns: 1097273.62x faster                                            |
| async_tree_eager              | 392 ms                                                 | 73.6 ms: 5.33x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 123 us: 2.64x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.58x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 406 ms: 2.51x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.0 ms: 2.49x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.31x faster                                                  |
| async_tree_none               | 391 ms                                                 | 175 ms: 2.24x faster                                                  |
| go                            | 163 ms                                                 | 79.7 ms: 2.05x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.68 ms: 1.86x faster                                                 |
| mdp                           | 1.65 sec                                               | 891 ms: 1.85x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.5 us: 1.78x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 395 ms: 1.70x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 45.8 ms: 1.58x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 89.3 ms: 1.57x faster                                                 |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                  |
| chaos                         | 67.7 ms                                                | 45.1 ms: 1.50x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.0 ms: 1.49x faster                                                 |
| deepcopy                      | 276 us                                                 | 187 us: 1.47x faster                                                  |
| float                         | 72.4 ms                                                | 49.2 ms: 1.47x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 454 ms: 1.47x faster                                                  |
| pyflate                       | 448 ms                                                 | 311 ms: 1.44x faster                                                  |
| richards                      | 52.3 ms                                                | 36.4 ms: 1.44x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 68.1 ms: 1.40x faster                                                 |
| generators                    | 31.7 ms                                                | 23.4 ms: 1.36x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.69 ms: 1.33x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 151 us: 1.31x faster                                                  |
| html5lib                      | 43.5 ms                                                | 33.4 ms: 1.30x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.5 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 221 us: 1.28x faster                                                  |
| comprehensions                | 17.3 us                                                | 13.5 us: 1.28x faster                                                 |
| pylint                        | 231 ms                                                 | 181 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.68 sec: 1.20x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 61.2 ms: 1.20x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.44 sec: 1.20x faster                                                |
| mako                          | 9.81 ms                                                | 8.24 ms: 1.19x faster                                                 |
| nbody                         | 92.5 ms                                                | 77.9 ms: 1.19x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 81.0 ms: 1.18x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 87.3 ms: 1.18x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.99 us: 1.17x faster                                                 |
| logging_format                | 5.03 us                                                | 4.38 us: 1.15x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.04 us: 1.14x faster                                                 |
| pycparser                     | 887 ms                                                 | 791 ms: 1.12x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.9 ms: 1.12x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.8 ms: 1.11x faster                                                 |
| sphinx                        | 729 ms                                                 | 659 ms: 1.11x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 17.4 ms: 1.10x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 86.0 ms: 1.08x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.21 ms: 1.06x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.7 ms: 1.04x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.67 sec: 1.04x faster                                                |
| xml_etree_process             | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.02 ms: 1.04x faster                                                 |
| pathlib                       | 25.7 ms                                                | 25.2 ms: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| sympy_str                     | 166 ms                                                 | 167 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| connected_components          | 318 ms                                                 | 328 ms: 1.03x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 77.5 ms: 1.04x slower                                                 |
| meteor_contest                | 77.8 ms                                                | 81.8 ms: 1.05x slower                                                 |
| django_template               | 24.4 ms                                                | 25.8 ms: 1.06x slower                                                 |
| nqueens                       | 63.8 ms                                                | 68.7 ms: 1.08x slower                                                 |
| dask                          | 789 ms                                                 | 853 ms: 1.08x slower                                                  |
| shortest_path                 | 328 ms                                                 | 355 ms: 1.08x slower                                                  |
| sympy_expand                  | 269 ms                                                 | 292 ms: 1.08x slower                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.76 sec: 1.09x slower                                                |
| scimark_fft                   | 225 ms                                                 | 248 ms: 1.10x slower                                                  |
| many_optionals                | 486 us                                                 | 535 us: 1.10x slower                                                  |
| 2to3                          | 201 ms                                                 | 226 ms: 1.12x slower                                                  |
| fannkuch                      | 303 ms                                                 | 358 ms: 1.18x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 63.9 ms: 1.18x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.23 ms: 1.19x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.40 ms: 1.20x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.21 ms: 1.23x slower                                                 |
| json                          | 3.10 ms                                                | 3.84 ms: 1.24x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.94 us: 1.31x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 74.8 ms: 1.33x slower                                                 |
| json_loads                    | 16.6 us                                                | 22.6 us: 1.37x slower                                                 |
| async_generators              | 233 ms                                                 | 331 ms: 1.42x slower                                                  |
| telco                         | 3.49 ms                                                | 5.56 ms: 1.59x slower                                                 |
| logging_silent                | 117 ns                                                 | 411 ns: 3.51x slower                                                  |
| coverage                      | 41.2 ms                                                | 308 ms: 7.48x slower                                                  |
| thrift                        | 562 us                                                 | 44.3 ms: 78.71x slower                                                |
| Geometric mean                | (ref)                                                  | 1.51x faster                                                          |

Benchmark hidden because not significant (1): bench_thread_pool
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.539x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.09x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.15x