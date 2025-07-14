# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.170x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 210 ms: 1.04x slower                                                  |
| docutils       | 1.74 sec                                               | 1.54 sec: 1.13x faster                                                |
| html5lib       | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| sphinx         | 729 ms                                                 | 641 ms: 1.14x faster                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 88.7 ms: 4.42x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 156 ms: 3.09x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 366 ms: 2.78x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                  |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.20x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                  |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                 |
| async_generators              | 233 ms                                                 | 298 ms: 1.28x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                 |
| pidigits       | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| nbody          | 92.5 ms                                                | 98.8 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 133 ms: 1.31x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.0 ms: 1.27x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.12 ms: 1.10x faster                                                 |
| regex_compile  | 95.6 ms                                                | 93.2 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 68.7 ms: 1.08x faster                                                 |
| pickle_pure_python   | 285 us                                                 | 265 us: 1.07x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 201 us: 1.01x slower                                                  |
| tomli_loads          | 1.72 sec                                               | 1.76 sec: 1.03x slower                                                |
| json_loads           | 16.6 us                                                | 17.8 us: 1.07x slower                                                 |
| xml_etree_process    | 44.6 ms                                                | 49.1 ms: 1.10x slower                                                 |
| xml_etree_generate   | 53.9 ms                                                | 65.2 ms: 1.21x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 35.1 ms                                                | 40.6 ms: 1.15x slower                                                 |
| genshi_text     | 17.7 ms                                                | 20.6 ms: 1.16x slower                                                 |
| mako            | 9.81 ms                                                | 11.7 ms: 1.20x slower                                                 |
| django_template | 24.4 ms                                                | 29.3 ms: 1.20x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.18x slower                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 88.7 ms: 4.42x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 156 ms: 3.09x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 366 ms: 2.78x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 122 us: 2.67x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.9 ms: 2.51x faster                                                 |
| async_tree_memoization        | 481 ms                                                 | 209 ms: 2.30x faster                                                  |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.20x faster                                                  |
| gc_traversal                  | 2.71 ms                                                | 1.46 ms: 1.85x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 374 ms: 1.79x faster                                                  |
| mdp                           | 1.65 sec                                               | 942 ms: 1.75x faster                                                  |
| deltablue                     | 4.99 ms                                                | 3.06 ms: 1.63x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 418 ms: 1.60x faster                                                  |
| raytrace                      | 327 ms                                                 | 230 ms: 1.42x faster                                                  |
| create_gc_cycles              | 1.16 ms                                                | 821 us: 1.42x faster                                                  |
| go                            | 163 ms                                                 | 117 ms: 1.40x faster                                                  |
| logging_silent                | 117 ns                                                 | 84.4 ns: 1.39x faster                                                 |
| float                         | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 104 ms: 1.34x faster                                                  |
| deepcopy                      | 276 us                                                 | 207 us: 1.33x faster                                                  |
| chaos                         | 67.7 ms                                                | 51.3 ms: 1.32x faster                                                 |
| regex_dna                     | 175 ms                                                 | 133 ms: 1.31x faster                                                  |
| pylint                        | 231 ms                                                 | 178 ms: 1.30x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.55 sec: 1.29x faster                                                |
| regex_v8                      | 19.1 ms                                                | 15.0 ms: 1.27x faster                                                 |
| richards                      | 52.3 ms                                                | 41.3 ms: 1.27x faster                                                 |
| richards_super                | 61.0 ms                                                | 48.2 ms: 1.26x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 28.4 ms: 1.25x faster                                                 |
| html5lib                      | 43.5 ms                                                | 35.2 ms: 1.24x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 28.2 us: 1.23x faster                                                 |
| comprehensions                | 17.3 us                                                | 14.3 us: 1.21x faster                                                 |
| pycparser                     | 887 ms                                                 | 733 ms: 1.21x faster                                                  |
| pyflate                       | 448 ms                                                 | 371 ms: 1.21x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 7.21 ms: 1.15x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 63.7 ms: 1.14x faster                                                 |
| sphinx                        | 729 ms                                                 | 641 ms: 1.14x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.54 sec: 1.13x faster                                                |
| deepcopy_reduce               | 2.32 us                                                | 2.10 us: 1.10x faster                                                 |
| pathlib                       | 25.7 ms                                                | 23.3 ms: 1.10x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.12 ms: 1.10x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 86.6 ms: 1.10x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 68.7 ms: 1.08x faster                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.37 us: 1.08x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 265 us: 1.07x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 68.4 ms: 1.07x faster                                                 |
| thrift                        | 562 us                                                 | 527 us: 1.07x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 12.5 ms: 1.05x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 87.9 ms: 1.05x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.95 ms: 1.05x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.28 sec: 1.04x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 625 ms: 1.04x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 93.2 ms: 1.03x faster                                                 |
| logging_format                | 5.03 us                                                | 4.91 us: 1.02x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.36 sec: 1.02x faster                                                |
| logging_simple                | 4.59 us                                                | 4.50 us: 1.02x faster                                                 |
| asyncio_websockets            | 242 ms                                                 | 238 ms: 1.02x faster                                                  |
| json                          | 3.10 ms                                                | 3.05 ms: 1.02x faster                                                 |
| dask                          | 789 ms                                                 | 780 ms: 1.01x faster                                                  |
| coroutines                    | 20.5 ms                                                | 20.3 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 281 ms: 1.00x slower                                                  |
| connected_components          | 318 ms                                                 | 320 ms: 1.01x slower                                                  |
| generators                    | 31.7 ms                                                | 32.0 ms: 1.01x slower                                                 |
| unpickle_pure_python          | 198 us                                                 | 201 us: 1.01x slower                                                  |
| tomli_loads                   | 1.72 sec                                               | 1.76 sec: 1.03x slower                                                |
| scimark_fft                   | 225 ms                                                 | 232 ms: 1.03x slower                                                  |
| scimark_lu                    | 103 ms                                                 | 106 ms: 1.03x slower                                                  |
| sympy_str                     | 166 ms                                                 | 172 ms: 1.04x slower                                                  |
| 2to3                          | 201 ms                                                 | 210 ms: 1.04x slower                                                  |
| shortest_path                 | 328 ms                                                 | 346 ms: 1.06x slower                                                  |
| nbody                         | 92.5 ms                                                | 98.8 ms: 1.07x slower                                                 |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.07x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.67 ms: 1.08x slower                                                 |
| many_optionals                | 486 us                                                 | 525 us: 1.08x slower                                                  |
| meteor_contest                | 77.8 ms                                                | 84.5 ms: 1.09x slower                                                 |
| sympy_expand                  | 269 ms                                                 | 296 ms: 1.10x slower                                                  |
| xml_etree_process             | 44.6 ms                                                | 49.1 ms: 1.10x slower                                                 |
| fannkuch                      | 303 ms                                                 | 333 ms: 1.10x slower                                                  |
| genshi_xml                    | 35.1 ms                                                | 40.6 ms: 1.15x slower                                                 |
| genshi_text                   | 17.7 ms                                                | 20.6 ms: 1.16x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 15.0 ms: 1.17x slower                                                 |
| mako                          | 9.81 ms                                                | 11.7 ms: 1.20x slower                                                 |
| django_template               | 24.4 ms                                                | 29.3 ms: 1.20x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 65.2 ms: 1.21x slower                                                 |
| async_generators              | 233 ms                                                 | 298 ms: 1.28x slower                                                  |
| nqueens                       | 63.8 ms                                                | 82.1 ms: 1.29x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 73.5 ms: 1.31x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 776 us: 1.42x slower                                                  |
| telco                         | 3.49 ms                                                | 5.25 ms: 1.51x slower                                                 |
| coverage                      | 41.2 ms                                                | 66.7 ms: 1.62x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.17x faster                                                          |

Benchmark hidden because not significant (1): python_startup
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250712-3.15.0a0-47b01da-NOGIL/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.170x faster

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.34x