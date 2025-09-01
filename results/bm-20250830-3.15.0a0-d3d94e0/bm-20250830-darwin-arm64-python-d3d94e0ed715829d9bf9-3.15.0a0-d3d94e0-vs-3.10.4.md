# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.19x faster                                                  |
| docutils       | 1.74 sec                                               | 1.43 sec: 1.21x faster                                                |
| html5lib       | 43.5 ms                                                | 32.5 ms: 1.34x faster                                                 |
| sphinx         | 729 ms                                                 | 573 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.9 ms: 5.95x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 370 ms: 2.74x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 385 ms: 2.65x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.1 ms: 1.47x faster                                                 |
| nbody          | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.4 ms: 1.32x faster                                                 |
| regex_dna      | 175 ms                                                 | 137 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 5.67 ms: 1.46x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 216 us: 1.32x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 155 us: 1.28x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.41 sec: 1.22x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 39.5 ms: 1.13x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.3 ms: 1.03x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| json_loads           | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.8 ms: 1.05x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.03x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.04 ms: 1.22x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 32.6 ms: 1.08x faster                                                 |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.9 ms: 5.95x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 142 ms: 3.41x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 97.1 us: 3.36x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 370 ms: 2.74x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 385 ms: 2.65x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 197 ms: 2.44x faster                                                  |
| async_tree_none               | 391 ms                                                 | 172 ms: 2.27x faster                                                  |
| mdp                           | 1.65 sec                                               | 772 ms: 2.14x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.42 ms: 2.06x faster                                                 |
| go                            | 163 ms                                                 | 84.0 ms: 1.95x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| raytrace                      | 327 ms                                                 | 177 ms: 1.85x faster                                                  |
| chaos                         | 67.7 ms                                                | 38.8 ms: 1.75x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 83.1 ms: 1.68x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 21.2 us: 1.64x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.2 ms: 1.64x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 44.4 ms: 1.63x faster                                                 |
| logging_silent                | 117 ns                                                 | 71.9 ns: 1.63x faster                                                 |
| deepcopy                      | 276 us                                                 | 171 us: 1.62x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                  |
| richards                      | 52.3 ms                                                | 33.2 ms: 1.57x faster                                                 |
| subparsers                    | 39.8 ms                                                | 25.4 ms: 1.57x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 62.8 ms: 1.52x faster                                                 |
| pyflate                       | 448 ms                                                 | 301 ms: 1.49x faster                                                  |
| float                         | 72.4 ms                                                | 49.1 ms: 1.47x faster                                                 |
| comprehensions                | 17.3 us                                                | 11.7 us: 1.47x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 5.67 ms: 1.46x faster                                                 |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 51.6 ms: 1.42x faster                                                 |
| logging_format                | 5.03 us                                                | 3.55 us: 1.42x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.2 ms: 1.41x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.26 us: 1.41x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 73.8 ms: 1.39x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.53 ms: 1.38x faster                                                 |
| html5lib                      | 43.5 ms                                                | 32.5 ms: 1.34x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                |
| deepcopy_reduce               | 2.32 us                                                | 1.76 us: 1.32x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.4 ms: 1.32x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 216 us: 1.32x faster                                                  |
| generators                    | 31.7 ms                                                | 24.4 ms: 1.30x faster                                                 |
| pycparser                     | 887 ms                                                 | 687 ms: 1.29x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 155 us: 1.28x faster                                                  |
| sphinx                        | 729 ms                                                 | 573 ms: 1.27x faster                                                  |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.27x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.3 ms: 1.26x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.23x faster                                                 |
| thrift                        | 562 us                                                 | 458 us: 1.23x faster                                                  |
| mako                          | 9.81 ms                                                | 8.04 ms: 1.22x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.8 ms: 1.22x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.41 sec: 1.22x faster                                                |
| docutils                      | 1.74 sec                                               | 1.43 sec: 1.21x faster                                                |
| scimark_fft                   | 225 ms                                                 | 187 ms: 1.21x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.11 sec: 1.20x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 77.1 ms: 1.20x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 546 ms: 1.19x faster                                                  |
| 2to3                          | 201 ms                                                 | 170 ms: 1.19x faster                                                  |
| nbody                         | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| sympy_str                     | 166 ms                                                 | 146 ms: 1.14x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 39.5 ms: 1.13x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.1 ms: 1.11x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 493 us: 1.10x faster                                                  |
| fannkuch                      | 303 ms                                                 | 276 ms: 1.10x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.12 ms: 1.10x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.14 sec: 1.10x faster                                                |
| sympy_expand                  | 269 ms                                                 | 246 ms: 1.10x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 32.6 ms: 1.08x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 73.4 ms: 1.06x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.0 ms: 1.05x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.8 ms: 1.05x faster                                                 |
| connected_components          | 318 ms                                                 | 306 ms: 1.04x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.3 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                 |
| dask                          | 789 ms                                                 | 786 ms: 1.00x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| shortest_path                 | 328 ms                                                 | 334 ms: 1.02x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 55.6 ms: 1.03x slower                                                 |
| json_loads                    | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.61 us: 1.09x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 14.3 ms: 1.12x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.34 ms: 1.16x slower                                                 |
| coverage                      | 41.2 ms                                                | 47.8 ms: 1.16x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.16 ms: 1.17x slower                                                 |
| telco                         | 3.49 ms                                                | 4.16 ms: 1.19x slower                                                 |
| async_generators              | 233 ms                                                 | 279 ms: 1.20x slower                                                  |
| many_optionals                | 486 us                                                 | 594 us: 1.22x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 71.4 ms: 1.27x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.33x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250830-3.15.0a0-d3d94e0/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.331x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.18x