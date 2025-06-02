# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.140x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 221 ms: 1.10x slower                                                  |
| docutils       | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| html5lib       | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 651 ms: 1.12x faster                                                  |
| Geometric mean | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.4 ms: 5.57x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.57x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 402 ms: 2.53x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.34x faster                                                  |
| async_tree_none               | 391 ms                                                 | 174 ms: 2.25x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 454 ms: 1.47x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.13x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 316 ms: 1.35x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.2 ms: 1.41x faster                                                 |
| nbody          | 92.5 ms                                                | 77.6 ms: 1.19x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.3 ms: 1.29x faster                                                 |
| regex_dna      | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| regex_v8       | 19.1 ms                                                | 17.3 ms: 1.10x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 222 us: 1.28x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 156 us: 1.27x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                |
| json_dumps           | 8.31 ms                                                | 8.07 ms: 1.03x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 76.7 ms: 1.03x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 65.1 ms: 1.21x slower                                                 |
| json_loads           | 16.6 us                                                | 22.6 us: 1.37x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.23 ms: 1.19x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.6 ms: 1.13x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.1 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 70.4 ms: 5.57x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 148 ms: 3.26x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 119 us: 2.75x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 394 ms: 2.57x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 402 ms: 2.53x faster                                                  |
| subparsers                    | 39.8 ms                                                | 16.0 ms: 2.49x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 205 ms: 2.34x faster                                                  |
| async_tree_none               | 391 ms                                                 | 174 ms: 2.25x faster                                                  |
| go                            | 163 ms                                                 | 77.4 ms: 2.11x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.60 ms: 1.92x faster                                                 |
| mdp                           | 1.65 sec                                               | 880 ms: 1.88x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.3 us: 1.80x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 391 ms: 1.71x faster                                                  |
| raytrace                      | 327 ms                                                 | 210 ms: 1.56x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 89.9 ms: 1.56x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.7 ms: 1.55x faster                                                 |
| chaos                         | 67.7 ms                                                | 43.8 ms: 1.55x faster                                                 |
| richards_super                | 61.0 ms                                                | 40.5 ms: 1.50x faster                                                 |
| deepcopy                      | 276 us                                                 | 185 us: 1.49x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 454 ms: 1.47x faster                                                  |
| pyflate                       | 448 ms                                                 | 306 ms: 1.46x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.9 us: 1.45x faster                                                 |
| richards                      | 52.3 ms                                                | 36.0 ms: 1.45x faster                                                 |
| float                         | 72.4 ms                                                | 51.2 ms: 1.41x faster                                                 |
| generators                    | 31.7 ms                                                | 23.0 ms: 1.38x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.60 ms: 1.36x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.1 ms: 1.31x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.3 ms: 1.31x faster                                                 |
| pylint                        | 231 ms                                                 | 178 ms: 1.30x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 74.3 ms: 1.29x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 222 us: 1.28x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 156 us: 1.27x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.62 sec: 1.24x faster                                                |
| tomli_loads                   | 1.72 sec                                               | 1.40 sec: 1.23x faster                                                |
| crypto_pyaes                  | 73.3 ms                                                | 60.3 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 145 ms: 1.21x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 79.2 ms: 1.20x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 85.9 ms: 1.19x faster                                                 |
| nbody                         | 92.5 ms                                                | 77.6 ms: 1.19x faster                                                 |
| pycparser                     | 887 ms                                                 | 744 ms: 1.19x faster                                                  |
| mako                          | 9.81 ms                                                | 8.23 ms: 1.19x faster                                                 |
| logging_format                | 5.03 us                                                | 4.33 us: 1.16x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 2.00 us: 1.16x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.97 us: 1.16x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.6 ms: 1.13x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.1 ms: 1.13x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.7 ms: 1.12x faster                                                 |
| sphinx                        | 729 ms                                                 | 651 ms: 1.12x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.12x faster                                                |
| regex_v8                      | 19.1 ms                                                | 17.3 ms: 1.10x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 587 ms: 1.10x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.59 sec: 1.09x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 85.1 ms: 1.09x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.2 ms: 1.08x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.19 ms: 1.07x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.1 ms: 1.06x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 8.07 ms: 1.03x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 75.9 ms: 1.02x faster                                                 |
| connected_components          | 318 ms                                                 | 312 ms: 1.02x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 535 us: 1.02x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.9 ms: 1.02x faster                                                 |
| pathlib                       | 25.7 ms                                                | 25.3 ms: 1.02x faster                                                 |
| sympy_str                     | 166 ms                                                 | 163 ms: 1.01x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 242 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| xml_etree_parse               | 109 ms                                                 | 112 ms: 1.02x slower                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 76.7 ms: 1.03x slower                                                 |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                  |
| fannkuch                      | 303 ms                                                 | 314 ms: 1.04x slower                                                  |
| django_template               | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 285 ms: 1.06x slower                                                  |
| nqueens                       | 63.8 ms                                                | 67.8 ms: 1.06x slower                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.67 sec: 1.07x slower                                                |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                 |
| many_optionals                | 486 us                                                 | 523 us: 1.08x slower                                                  |
| dask                          | 789 ms                                                 | 857 ms: 1.08x slower                                                  |
| 2to3                          | 201 ms                                                 | 221 ms: 1.10x slower                                                  |
| scimark_fft                   | 225 ms                                                 | 263 ms: 1.17x slower                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 4.03 ms: 1.18x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.23 ms: 1.19x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.40 ms: 1.20x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 65.1 ms: 1.21x slower                                                 |
| json                          | 3.10 ms                                                | 3.83 ms: 1.23x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.90 us: 1.28x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 74.8 ms: 1.33x slower                                                 |
| async_generators              | 233 ms                                                 | 316 ms: 1.35x slower                                                  |
| json_loads                    | 16.6 us                                                | 22.6 us: 1.37x slower                                                 |
| telco                         | 3.49 ms                                                | 5.55 ms: 1.59x slower                                                 |
| logging_silent                | 117 ns                                                 | 420 ns: 3.58x slower                                                  |
| coverage                      | 41.2 ms                                                | 302 ms: 7.32x slower                                                  |
| thrift                        | 562 us                                                 | 44.2 ms: 78.67x slower                                                |
| Geometric mean                | (ref)                                                  | 1.12x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.140x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.14x