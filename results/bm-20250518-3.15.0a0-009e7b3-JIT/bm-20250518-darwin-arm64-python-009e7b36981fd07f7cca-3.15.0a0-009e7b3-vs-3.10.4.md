# Results vs. 3.10.4

- fork: python
- ref: 009e7b36981fd07f7cca
- machine: darwin-arm64
- commit hash: 009e7b3
- commit date: 2025-05-18
- overall geometric mean: 1.267x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| html5lib       | 43.5 ms                                                | 29.7 ms: 1.47x faster                                                 |
| sphinx         | 729 ms                                                 | 584 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.4 ms: 6.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.81x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 187 ms: 2.57x faster                                                  |
| async_tree_none               | 391 ms                                                 | 157 ms: 2.49x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                 |
| async_generators              | 233 ms                                                 | 281 ms: 1.21x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 45.9 ms: 1.58x faster                                                 |
| nbody          | 92.5 ms                                                | 72.9 ms: 1.27x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.26x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.17 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 136 us: 1.46x faster                                                  |
| pickle_pure_python   | 285 us                                                 | 200 us: 1.42x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.23 sec: 1.40x faster                                                |
| json_dumps           | 8.31 ms                                                | 6.64 ms: 1.25x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 36.0 ms: 1.24x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 99.7 ms: 1.10x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 51.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 71.2 ms: 1.05x faster                                                 |
| json_loads           | 16.6 us                                                | 18.1 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.83 ms: 1.44x faster                                                 |
| genshi_text     | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 29.2 ms: 1.20x faster                                                 |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.27x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 62.4 ms: 6.28x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 99.8 us: 3.27x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.4 ms: 2.97x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 360 ms: 2.81x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 374 ms: 2.72x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 187 ms: 2.57x faster                                                  |
| async_tree_none               | 391 ms                                                 | 157 ms: 2.49x faster                                                  |
| mdp                           | 1.65 sec                                               | 756 ms: 2.18x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.32 ms: 2.15x faster                                                 |
| go                            | 163 ms                                                 | 79.9 ms: 2.05x faster                                                 |
| raytrace                      | 327 ms                                                 | 171 ms: 1.91x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 18.5 us: 1.88x faster                                                 |
| deepcopy                      | 276 us                                                 | 151 us: 1.82x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 78.2 ms: 1.79x faster                                                 |
| chaos                         | 67.7 ms                                                | 37.9 ms: 1.79x faster                                                 |
| richards_super                | 61.0 ms                                                | 36.6 ms: 1.67x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 44.1 ms: 1.64x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 412 ms: 1.62x faster                                                  |
| richards                      | 52.3 ms                                                | 32.7 ms: 1.60x faster                                                 |
| float                         | 72.4 ms                                                | 45.9 ms: 1.58x faster                                                 |
| pyflate                       | 448 ms                                                 | 287 ms: 1.56x faster                                                  |
| html5lib                      | 43.5 ms                                                | 29.7 ms: 1.47x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 136 us: 1.46x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.31 ms: 1.45x faster                                                 |
| mako                          | 9.81 ms                                                | 6.83 ms: 1.44x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 24.8 ms: 1.43x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.43x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 200 us: 1.42x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 67.6 ms: 1.41x faster                                                 |
| pylint                        | 231 ms                                                 | 164 ms: 1.41x faster                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.23 sec: 1.40x faster                                                |
| comprehensions                | 17.3 us                                                | 12.6 us: 1.38x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 69.2 ms: 1.38x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 74.7 ms: 1.37x faster                                                 |
| generators                    | 31.7 ms                                                | 23.3 ms: 1.36x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 55.8 ms: 1.31x faster                                                 |
| logging_format                | 5.03 us                                                | 3.83 us: 1.31x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.02 sec: 1.30x faster                                                |
| logging_simple                | 4.59 us                                                | 3.53 us: 1.30x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 499 ms: 1.30x faster                                                  |
| pycparser                     | 887 ms                                                 | 683 ms: 1.30x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 13.8 ms: 1.28x faster                                                 |
| nbody                         | 92.5 ms                                                | 72.9 ms: 1.27x faster                                                 |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.4 ms: 1.25x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.61 sec: 1.25x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 74.1 ms: 1.25x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.64 ms: 1.25x faster                                                 |
| sphinx                        | 729 ms                                                 | 584 ms: 1.25x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 36.0 ms: 1.24x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.22x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 29.2 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| sympy_str                     | 166 ms                                                 | 140 ms: 1.19x faster                                                  |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 239 ms: 1.13x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.06 sec: 1.12x faster                                                |
| bench_thread_pool             | 545 us                                                 | 488 us: 1.12x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 99.7 ms: 1.10x faster                                                 |
| 2to3                          | 201 ms                                                 | 184 ms: 1.09x faster                                                  |
| python_startup                | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.17 ms: 1.08x faster                                                 |
| nqueens                       | 63.8 ms                                                | 59.4 ms: 1.07x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 51.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 71.2 ms: 1.05x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.8 ms: 1.04x faster                                                 |
| json                          | 3.10 ms                                                | 3.03 ms: 1.02x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 78.0 ms: 1.00x slower                                                 |
| connected_components          | 318 ms                                                 | 320 ms: 1.00x slower                                                  |
| fannkuch                      | 303 ms                                                 | 305 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| dask                          | 789 ms                                                 | 816 ms: 1.03x slower                                                  |
| shortest_path                 | 328 ms                                                 | 348 ms: 1.06x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.7 ms: 1.07x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.70 ms: 1.08x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.60 us: 1.08x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.1 us: 1.09x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.22 ms: 1.19x slower                                                 |
| async_generators              | 233 ms                                                 | 281 ms: 1.21x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 69.9 ms: 1.25x slower                                                 |
| telco                         | 3.49 ms                                                | 4.70 ms: 1.35x slower                                                 |
| logging_silent                | 117 ns                                                 | 324 ns: 2.77x slower                                                  |
| coverage                      | 41.2 ms                                                | 270 ms: 6.55x slower                                                  |
| thrift                        | 562 us                                                 | 43.4 ms: 77.13x slower                                                |
| Geometric mean                | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (3): scimark_fft, many_optionals, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250518-3.15.0a0-009e7b3-JIT/bm-20250518-darwin-arm64-python-009e7b36981fd07f7cca-3.15.0a0-009e7b3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.267x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x