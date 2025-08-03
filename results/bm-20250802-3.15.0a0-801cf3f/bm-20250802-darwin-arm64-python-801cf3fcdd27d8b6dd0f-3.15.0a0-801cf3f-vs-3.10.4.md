# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.324x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 173 ms: 1.17x faster                                                  |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| html5lib       | 43.5 ms                                                | 33.1 ms: 1.32x faster                                                 |
| sphinx         | 729 ms                                                 | 582 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.9 ms: 6.04x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.49x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 382 ms: 2.66x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                                  |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 50.1 ms: 1.44x faster                                                 |
| nbody          | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.18x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 74.0 ms: 1.29x faster                                                 |
| regex_dna      | 175 ms                                                 | 139 ms: 1.26x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.15 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 216 us: 1.32x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 156 us: 1.27x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.63 ms: 1.25x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 39.7 ms: 1.12x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                 |
| json_loads           | 16.6 us                                                | 17.0 us: 1.03x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.9 ms: 1.16x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                 |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.09 ms: 1.21x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                 |
| django_template | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.9 ms: 6.04x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.49x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 96.8 us: 3.37x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 382 ms: 2.66x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                                  |
| async_tree_none               | 391 ms                                                 | 167 ms: 2.34x faster                                                  |
| mdp                           | 1.65 sec                                               | 774 ms: 2.13x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.39 ms: 2.09x faster                                                 |
| go                            | 163 ms                                                 | 85.7 ms: 1.91x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.88x faster                                                  |
| raytrace                      | 327 ms                                                 | 175 ms: 1.87x faster                                                  |
| chaos                         | 67.7 ms                                                | 38.7 ms: 1.75x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 84.3 ms: 1.66x faster                                                 |
| logging_silent                | 117 ns                                                 | 71.5 ns: 1.64x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.7 ms: 1.62x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 45.2 ms: 1.60x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                  |
| deepcopy                      | 276 us                                                 | 173 us: 1.59x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 21.9 us: 1.59x faster                                                 |
| subparsers                    | 39.8 ms                                                | 25.5 ms: 1.56x faster                                                 |
| richards                      | 52.3 ms                                                | 33.6 ms: 1.56x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 62.6 ms: 1.52x faster                                                 |
| pyflate                       | 448 ms                                                 | 306 ms: 1.47x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.9 us: 1.45x faster                                                 |
| float                         | 72.4 ms                                                | 50.1 ms: 1.44x faster                                                 |
| pylint                        | 231 ms                                                 | 162 ms: 1.42x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.2 ms: 1.41x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 52.1 ms: 1.41x faster                                                 |
| logging_format                | 5.03 us                                                | 3.64 us: 1.38x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.34 us: 1.38x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.58 ms: 1.36x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 76.4 ms: 1.34x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 216 us: 1.32x faster                                                  |
| html5lib                      | 43.5 ms                                                | 33.1 ms: 1.32x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.31x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.31x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 74.0 ms: 1.29x faster                                                 |
| pycparser                     | 887 ms                                                 | 692 ms: 1.28x faster                                                  |
| unpickle_pure_python          | 198 us                                                 | 156 us: 1.27x faster                                                  |
| thrift                        | 562 us                                                 | 447 us: 1.26x faster                                                  |
| regex_dna                     | 175 ms                                                 | 139 ms: 1.26x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 6.63 ms: 1.25x faster                                                 |
| sphinx                        | 729 ms                                                 | 582 ms: 1.25x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 529 ms: 1.22x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                                 |
| mako                          | 9.81 ms                                                | 8.09 ms: 1.21x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 187 ms: 1.20x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| sympy_sum                     | 92.7 ms                                                | 77.6 ms: 1.19x faster                                                 |
| 2to3                          | 201 ms                                                 | 173 ms: 1.17x faster                                                  |
| python_startup                | 19.6 ms                                                | 16.9 ms: 1.16x faster                                                 |
| nbody                         | 92.5 ms                                                | 80.0 ms: 1.16x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.51 sec: 1.14x faster                                                |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 39.7 ms: 1.12x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.12 ms: 1.10x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.14 sec: 1.09x faster                                                |
| sympy_expand                  | 269 ms                                                 | 247 ms: 1.09x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.15 ms: 1.08x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 505 us: 1.08x faster                                                  |
| django_template               | 24.4 ms                                                | 22.8 ms: 1.07x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.1 ms: 1.07x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| fannkuch                      | 303 ms                                                 | 286 ms: 1.06x faster                                                  |
| connected_components          | 318 ms                                                 | 306 ms: 1.04x faster                                                  |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.5 ms: 1.04x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 75.0 ms: 1.04x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 71.8 ms: 1.04x faster                                                 |
| python_startup_no_site        | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| dask                          | 789 ms                                                 | 797 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| shortest_path                 | 328 ms                                                 | 337 ms: 1.03x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.0 us: 1.03x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 56.0 ms: 1.04x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                 |
| coverage                      | 41.2 ms                                                | 46.1 ms: 1.12x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.17 ms: 1.17x slower                                                 |
| async_generators              | 233 ms                                                 | 275 ms: 1.18x slower                                                  |
| many_optionals                | 486 us                                                 | 591 us: 1.22x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 69.6 ms: 1.24x slower                                                 |
| telco                         | 3.49 ms                                                | 4.60 ms: 1.32x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250802-3.15.0a0-801cf3f/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.324x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.17x