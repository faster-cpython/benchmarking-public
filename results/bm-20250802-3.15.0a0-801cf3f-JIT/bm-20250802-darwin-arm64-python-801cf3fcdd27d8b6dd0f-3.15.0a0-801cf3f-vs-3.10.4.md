# Results vs. 3.10.4

- fork: python
- ref: 801cf3fcdd27d8b6dd0f
- machine: darwin-arm64
- commit hash: 801cf3f
- commit date: 2025-08-02
- overall geometric mean: 1.337x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| html5lib       | 43.5 ms                                                | 33.6 ms: 1.29x faster                                                 |
| sphinx         | 729 ms                                                 | 579 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.36x faster                                                  |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.03x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| nbody          | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.6 ms: 1.30x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.14 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                |
| pickle_pure_python   | 285 us                                                 | 210 us: 1.36x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.28 ms: 1.32x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 34.9 ms: 1.28x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 99.1 ms: 1.10x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 49.4 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                 |
| json_loads           | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.0 ms: 1.15x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 12.9 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.3 ms: 1.05x faster                                                 |
| django_template | 24.4 ms                                                | 23.4 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.4 ms: 5.99x faster                                                 |
| typing_runtime_protocols      | 326 us                                                 | 94.7 us: 3.44x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 366 ms: 2.77x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 204 ms: 2.36x faster                                                  |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                  |
| mdp                           | 1.65 sec                                               | 774 ms: 2.13x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.54 ms: 1.96x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                  |
| go                            | 163 ms                                                 | 88.2 ms: 1.85x faster                                                 |
| raytrace                      | 327 ms                                                 | 180 ms: 1.82x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.5 ms: 1.72x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 86.2 ms: 1.62x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 415 ms: 1.61x faster                                                  |
| richards_super                | 61.0 ms                                                | 38.0 ms: 1.60x faster                                                 |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.3 ms: 1.56x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 22.3 us: 1.56x faster                                                 |
| subparsers                    | 39.8 ms                                                | 25.6 ms: 1.55x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                  |
| pyflate                       | 448 ms                                                 | 293 ms: 1.53x faster                                                  |
| richards                      | 52.3 ms                                                | 34.3 ms: 1.53x faster                                                 |
| comprehensions                | 17.3 us                                                | 11.4 us: 1.52x faster                                                 |
| logging_silent                | 117 ns                                                 | 77.0 ns: 1.52x faster                                                 |
| mako                          | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 63.5 ms: 1.50x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.9 ms: 1.47x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 916 ms: 1.45x faster                                                  |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 457 ms: 1.42x faster                                                  |
| float                         | 72.4 ms                                                | 51.6 ms: 1.40x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                |
| dulwich_log                   | 35.6 ms                                                | 25.7 ms: 1.39x faster                                                 |
| logging_format                | 5.03 us                                                | 3.70 us: 1.36x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 210 us: 1.36x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 76.0 ms: 1.35x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.42 us: 1.34x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.67 ms: 1.34x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.28 ms: 1.32x faster                                                 |
| generators                    | 31.7 ms                                                | 24.4 ms: 1.30x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 73.6 ms: 1.30x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.79 us: 1.30x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.6 ms: 1.29x faster                                                 |
| nbody                         | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 34.9 ms: 1.28x faster                                                 |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.26x faster                                                |
| sphinx                        | 729 ms                                                 | 579 ms: 1.26x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| fannkuch                      | 303 ms                                                 | 246 ms: 1.23x faster                                                  |
| thrift                        | 562 us                                                 | 459 us: 1.22x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| pycparser                     | 887 ms                                                 | 736 ms: 1.21x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 77.4 ms: 1.20x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.0 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 2.92 sec: 1.18x faster                                                |
| 2to3                          | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 192 ms: 1.18x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.3 ms: 1.16x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.0 ms: 1.15x faster                                                 |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 99.1 ms: 1.10x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.14 ms: 1.09x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 49.4 ms: 1.09x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 504 us: 1.08x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 249 ms: 1.08x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 72.7 ms: 1.07x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.3 ms: 1.05x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.5 ms: 1.05x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                 |
| django_template               | 24.4 ms                                                | 23.4 ms: 1.04x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.9 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.39 ms: 1.01x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| connected_components          | 318 ms                                                 | 321 ms: 1.01x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 12.9 ms: 1.01x slower                                                 |
| dask                          | 789 ms                                                 | 797 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| shortest_path                 | 328 ms                                                 | 350 ms: 1.07x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.07x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| coverage                      | 41.2 ms                                                | 48.2 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 288 ms: 1.23x slower                                                  |
| many_optionals                | 486 us                                                 | 600 us: 1.23x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 70.2 ms: 1.25x slower                                                 |
| telco                         | 3.49 ms                                                | 4.40 ms: 1.26x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.33x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250802-3.15.0a0-801cf3f-JIT/bm-20250802-darwin-arm64-python-801cf3fcdd27d8b6dd0f-3.15.0a0-801cf3f.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.337x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x