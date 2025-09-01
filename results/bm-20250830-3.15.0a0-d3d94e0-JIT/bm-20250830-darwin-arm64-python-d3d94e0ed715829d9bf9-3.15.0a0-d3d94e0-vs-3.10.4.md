# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                |
| html5lib       | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                 |
| sphinx         | 729 ms                                                 | 576 ms: 1.27x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.0 ms: 6.03x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.78x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.04x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 50.6 ms: 1.43x faster                                                 |
| nbody          | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.7 ms: 1.31x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.14 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                  |
| json_dumps           | 8.31 ms                                                | 5.77 ms: 1.44x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.25 sec: 1.38x faster                                                |
| pickle_pure_python   | 285 us                                                 | 206 us: 1.38x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 34.7 ms: 1.29x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 49.4 ms: 1.09x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 71.9 ms: 1.04x faster                                                 |
| json_loads           | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.50 ms: 1.51x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.5 ms: 1.14x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.3 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 23.3 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 65.0 ms: 6.03x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.43x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 96.5 us: 3.38x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.78x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 378 ms: 2.69x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 170 ms: 2.30x faster                                                  |
| mdp                           | 1.65 sec                                               | 779 ms: 2.12x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.53 ms: 1.97x faster                                                 |
| raytrace                      | 327 ms                                                 | 175 ms: 1.87x faster                                                  |
| go                            | 163 ms                                                 | 87.6 ms: 1.86x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 363 ms: 1.84x faster                                                  |
| chaos                         | 67.7 ms                                                | 38.9 ms: 1.74x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 83.7 ms: 1.67x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.4 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                  |
| logging_silent                | 117 ns                                                 | 73.3 ns: 1.60x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 21.8 us: 1.60x faster                                                 |
| deepcopy                      | 276 us                                                 | 174 us: 1.58x faster                                                  |
| pyflate                       | 448 ms                                                 | 285 ms: 1.57x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 46.2 ms: 1.57x faster                                                 |
| richards                      | 52.3 ms                                                | 33.5 ms: 1.56x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.4 us: 1.52x faster                                                 |
| subparsers                    | 39.8 ms                                                | 26.3 ms: 1.52x faster                                                 |
| mako                          | 9.81 ms                                                | 6.50 ms: 1.51x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 63.8 ms: 1.49x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.6 ms: 1.48x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 900 ms: 1.48x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 449 ms: 1.44x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 5.77 ms: 1.44x faster                                                 |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                  |
| float                         | 72.4 ms                                                | 50.6 ms: 1.43x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.3 ms: 1.41x faster                                                 |
| logging_format                | 5.03 us                                                | 3.58 us: 1.40x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.31 us: 1.39x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.25 sec: 1.38x faster                                                |
| pickle_pure_python            | 285 us                                                 | 206 us: 1.38x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 75.6 ms: 1.36x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.61 ms: 1.35x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.7 ms: 1.31x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.2 ms: 1.31x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.80 us: 1.29x faster                                                 |
| nbody                         | 92.5 ms                                                | 71.7 ms: 1.29x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 34.7 ms: 1.29x faster                                                 |
| generators                    | 31.7 ms                                                | 24.7 ms: 1.28x faster                                                 |
| pycparser                     | 887 ms                                                 | 695 ms: 1.28x faster                                                  |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                  |
| sphinx                        | 729 ms                                                 | 576 ms: 1.27x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.59 sec: 1.26x faster                                                |
| regex_v8                      | 19.1 ms                                                | 15.3 ms: 1.25x faster                                                 |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                 |
| thrift                        | 562 us                                                 | 458 us: 1.23x faster                                                  |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.22x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 76.7 ms: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.44 sec: 1.20x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 2.92 sec: 1.18x faster                                                |
| scimark_fft                   | 225 ms                                                 | 192 ms: 1.17x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.5 ms: 1.14x faster                                                 |
| sympy_str                     | 166 ms                                                 | 145 ms: 1.14x faster                                                  |
| pathlib                       | 25.7 ms                                                | 23.2 ms: 1.11x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 493 us: 1.11x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 49.4 ms: 1.09x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.14 ms: 1.09x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.09x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 101 ms: 1.08x faster                                                  |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 72.7 ms: 1.07x faster                                                 |
| genshi_xml                    | 35.1 ms                                                | 33.3 ms: 1.06x faster                                                 |
| django_template               | 24.4 ms                                                | 23.3 ms: 1.04x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 71.9 ms: 1.04x faster                                                 |
| nqueens                       | 63.8 ms                                                | 62.3 ms: 1.02x faster                                                 |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                 |
| dask                          | 789 ms                                                 | 785 ms: 1.01x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.41 ms: 1.00x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 243 ms: 1.00x slower                                                  |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| connected_components          | 318 ms                                                 | 322 ms: 1.01x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.4 us: 1.05x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.57 us: 1.06x slower                                                 |
| shortest_path                 | 328 ms                                                 | 351 ms: 1.07x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 14.4 ms: 1.13x slower                                                 |
| telco                         | 3.49 ms                                                | 3.95 ms: 1.13x slower                                                 |
| coverage                      | 41.2 ms                                                | 47.5 ms: 1.15x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.34 ms: 1.15x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.17 ms: 1.17x slower                                                 |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| many_optionals                | 486 us                                                 | 615 us: 1.27x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 71.7 ms: 1.28x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.34x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250830-3.15.0a0-d3d94e0-JIT/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x