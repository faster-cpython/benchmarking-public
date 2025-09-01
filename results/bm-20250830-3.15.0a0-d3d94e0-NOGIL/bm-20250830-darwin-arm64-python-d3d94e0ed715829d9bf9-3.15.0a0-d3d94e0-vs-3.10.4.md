# Results vs. 3.10.4

- fork: python
- ref: d3d94e0ed715829d9bf9
- machine: darwin-arm64
- commit hash: d3d94e0
- commit date: 2025-08-30
- overall geometric mean: 1.278x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.11x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                |
| html5lib       | 43.5 ms                                                | 32.6 ms: 1.33x faster                                                 |
| sphinx         | 729 ms                                                 | 594 ms: 1.23x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.7 ms: 5.18x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.32x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 320 ms: 3.18x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.58x faster                                                  |
| async_tree_none               | 391 ms                                                 | 155 ms: 2.53x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.68x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.12x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                 |
| nbody          | 92.5 ms                                                | 89.5 ms: 1.03x faster                                                 |
| pidigits       | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 19.1 ms                                                | 14.7 ms: 1.30x faster                                                 |
| regex_dna      | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| regex_compile  | 95.6 ms                                                | 79.5 ms: 1.20x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.17 ms: 1.08x faster                                                 |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 5.97 ms: 1.39x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 224 us: 1.27x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 164 us: 1.21x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 64.4 ms: 1.16x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 97.3 ms: 1.13x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.54 sec: 1.11x faster                                                |
| xml_etree_process    | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                 |
| json_loads           | 16.6 us                                                | 18.0 us: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.4 ms: 1.04x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.8 ms: 1.24x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 24.4 ms                                                | 24.4 ms: 1.00x slower                                                 |
| genshi_text     | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 37.3 ms: 1.06x slower                                                 |
| mako            | 9.81 ms                                                | 10.7 ms: 1.10x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.7 ms: 5.18x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.46x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 305 ms: 3.32x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 320 ms: 3.18x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 119 us: 2.75x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.58x faster                                                  |
| async_tree_none               | 391 ms                                                 | 155 ms: 2.53x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.29 ms: 2.10x faster                                                 |
| deltablue                     | 4.99 ms                                                | 2.51 ms: 1.99x faster                                                 |
| mdp                           | 1.65 sec                                               | 867 ms: 1.90x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 360 ms: 1.86x faster                                                  |
| go                            | 163 ms                                                 | 93.0 ms: 1.76x faster                                                 |
| raytrace                      | 327 ms                                                 | 194 ms: 1.68x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 399 ms: 1.68x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 86.5 ms: 1.62x faster                                                 |
| chaos                         | 67.7 ms                                                | 42.3 ms: 1.60x faster                                                 |
| float                         | 72.4 ms                                                | 47.7 ms: 1.52x faster                                                 |
| logging_silent                | 117 ns                                                 | 77.3 ns: 1.51x faster                                                 |
| create_gc_cycles              | 1.16 ms                                                | 773 us: 1.51x faster                                                  |
| deepcopy                      | 276 us                                                 | 186 us: 1.48x faster                                                  |
| richards_super                | 61.0 ms                                                | 41.1 ms: 1.48x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 23.4 us: 1.48x faster                                                 |
| subparsers                    | 39.8 ms                                                | 26.9 ms: 1.48x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 50.3 ms: 1.44x faster                                                 |
| richards                      | 52.3 ms                                                | 36.4 ms: 1.44x faster                                                 |
| pyflate                       | 448 ms                                                 | 314 ms: 1.43x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 5.97 ms: 1.39x faster                                                 |
| pylint                        | 231 ms                                                 | 167 ms: 1.39x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.8 ms: 1.38x faster                                                 |
| pycparser                     | 887 ms                                                 | 657 ms: 1.35x faster                                                  |
| html5lib                      | 43.5 ms                                                | 32.6 ms: 1.33x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 73.3 ms: 1.30x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 14.7 ms: 1.30x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.4 us: 1.29x faster                                                 |
| regex_dna                     | 175 ms                                                 | 137 ms: 1.28x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 224 us: 1.27x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 58.3 ms: 1.26x faster                                                 |
| generators                    | 31.7 ms                                                | 25.2 ms: 1.26x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.61 sec: 1.25x faster                                                |
| logging_simple                | 4.59 us                                                | 3.67 us: 1.25x faster                                                 |
| logging_format                | 5.03 us                                                | 4.05 us: 1.24x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.08 ms: 1.23x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                |
| coroutines                    | 20.5 ms                                                | 16.7 ms: 1.23x faster                                                 |
| sphinx                        | 729 ms                                                 | 594 ms: 1.23x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.91 us: 1.21x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 164 us: 1.21x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 84.8 ms: 1.21x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 79.5 ms: 1.20x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.13 sec: 1.18x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 555 ms: 1.17x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 64.4 ms: 1.16x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.6 ms: 1.13x faster                                                 |
| thrift                        | 562 us                                                 | 499 us: 1.13x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 97.3 ms: 1.13x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.9 ms: 1.12x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 82.5 ms: 1.12x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.54 sec: 1.11x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 3.12 sec: 1.10x faster                                                |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.10x faster                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.35 us: 1.09x faster                                                 |
| 2to3                          | 201 ms                                                 | 187 ms: 1.08x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.17 ms: 1.08x faster                                                 |
| sympy_str                     | 166 ms                                                 | 159 ms: 1.05x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.1 ms: 1.04x faster                                                 |
| nbody                         | 92.5 ms                                                | 89.5 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| fannkuch                      | 303 ms                                                 | 299 ms: 1.01x faster                                                  |
| pidigits                      | 280 ms                                                 | 280 ms: 1.00x faster                                                  |
| django_template               | 24.4 ms                                                | 24.4 ms: 1.00x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                  |
| dask                          | 789 ms                                                 | 796 ms: 1.01x slower                                                  |
| genshi_text                   | 17.7 ms                                                | 18.2 ms: 1.03x slower                                                 |
| nqueens                       | 63.8 ms                                                | 66.1 ms: 1.04x slower                                                 |
| connected_components          | 318 ms                                                 | 330 ms: 1.04x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.4 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.60 ms: 1.05x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 37.3 ms: 1.06x slower                                                 |
| shortest_path                 | 328 ms                                                 | 353 ms: 1.08x slower                                                  |
| xml_etree_generate            | 53.9 ms                                                | 58.5 ms: 1.09x slower                                                 |
| meteor_contest                | 77.8 ms                                                | 84.6 ms: 1.09x slower                                                 |
| json_loads                    | 16.6 us                                                | 18.0 us: 1.09x slower                                                 |
| mako                          | 9.81 ms                                                | 10.7 ms: 1.10x slower                                                 |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 15.8 ms: 1.24x slower                                                 |
| many_optionals                | 486 us                                                 | 612 us: 1.26x slower                                                  |
| telco                         | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 74.0 ms: 1.32x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 745 us: 1.37x slower                                                  |
| coverage                      | 41.2 ms                                                | 63.4 ms: 1.54x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.27x faster                                                          |
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250830-3.15.0a0-d3d94e0-NOGIL/bm-20250830-darwin-arm64-python-d3d94e0ed715829d9bf9-3.15.0a0-d3d94e0.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.278x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.11x

# Memory
- memory change: 1.35x