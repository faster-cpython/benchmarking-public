# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.340x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 174 ms: 1.16x faster                                                  |
| docutils       | 1.74 sec                                               | 1.47 sec: 1.18x faster                                                |
| html5lib       | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| sphinx         | 729 ms                                                 | 586 ms: 1.24x faster                                                  |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.6 ms: 6.07x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.44x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.39x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| async_generators              | 233 ms                                                 | 281 ms: 1.20x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.06x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 48.2 ms: 1.50x faster                                                 |
| nbody          | 92.5 ms                                                | 75.8 ms: 1.22x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.22x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.3 ms: 1.34x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.44 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.19x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 134 us: 1.48x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                |
| pickle_pure_python   | 285 us                                                 | 210 us: 1.35x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                 |
| json_dumps           | 8.31 ms                                                | 6.67 ms: 1.24x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 50.7 ms: 1.06x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 72.4 ms: 1.03x faster                                                 |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.5 ms: 1.13x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.01 ms: 1.40x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| django_template | 24.4 ms                                                | 21.7 ms: 1.12x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.20x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.6 ms: 6.07x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 141 ms: 3.44x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 98.4 us: 3.31x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.8 ms: 2.89x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 362 ms: 2.80x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.39x faster                                                  |
| mdp                           | 1.65 sec                                               | 757 ms: 2.18x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.67 ms: 1.87x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.86x faster                                                  |
| raytrace                      | 327 ms                                                 | 179 ms: 1.83x faster                                                  |
| go                            | 163 ms                                                 | 91.3 ms: 1.79x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 19.5 us: 1.78x faster                                                 |
| deepcopy                      | 276 us                                                 | 156 us: 1.76x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.4 ms: 1.72x faster                                                 |
| logging_silent                | 117 ns                                                 | 72.3 ns: 1.62x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 416 ms: 1.61x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 88.7 ms: 1.58x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.0 ms: 1.58x faster                                                 |
| pyflate                       | 448 ms                                                 | 289 ms: 1.55x faster                                                  |
| float                         | 72.4 ms                                                | 48.2 ms: 1.50x faster                                                 |
| richards_super                | 61.0 ms                                                | 40.9 ms: 1.49x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 134 us: 1.48x faster                                                  |
| richards                      | 52.3 ms                                                | 35.9 ms: 1.46x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.1 us: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                  |
| dulwich_log                   | 35.6 ms                                                | 25.2 ms: 1.41x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 68.0 ms: 1.40x faster                                                 |
| mako                          | 9.81 ms                                                | 7.01 ms: 1.40x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.67 us: 1.39x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                |
| html5lib                      | 43.5 ms                                                | 31.5 ms: 1.38x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 210 us: 1.35x faster                                                  |
| logging_format                | 5.03 us                                                | 3.72 us: 1.35x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.42 us: 1.34x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 71.3 ms: 1.34x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.32x faster                                                |
| generators                    | 31.7 ms                                                | 24.1 ms: 1.32x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 55.9 ms: 1.31x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.79 ms: 1.30x faster                                                 |
| thrift                        | 562 us                                                 | 444 us: 1.27x faster                                                  |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| pycparser                     | 887 ms                                                 | 705 ms: 1.26x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.67 ms: 1.24x faster                                                 |
| sphinx                        | 729 ms                                                 | 586 ms: 1.24x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 75.3 ms: 1.23x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 83.9 ms: 1.22x faster                                                 |
| nbody                         | 92.5 ms                                                | 75.8 ms: 1.22x faster                                                 |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.21x faster                                                 |
| pprint_safe_repr              | 648 ms                                                 | 541 ms: 1.20x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.11 sec: 1.19x faster                                                |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.18x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.47 sec: 1.18x faster                                                |
| 2to3                          | 201 ms                                                 | 174 ms: 1.16x faster                                                  |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                  |
| pathlib                       | 25.7 ms                                                | 22.5 ms: 1.15x faster                                                 |
| scimark_fft                   | 225 ms                                                 | 198 ms: 1.14x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| python_startup                | 19.6 ms                                                | 17.5 ms: 1.13x faster                                                 |
| django_template               | 24.4 ms                                                | 21.7 ms: 1.12x faster                                                 |
| bpe_tokeniser                 | 3.44 sec                                               | 3.10 sec: 1.11x faster                                                |
| sympy_expand                  | 269 ms                                                 | 244 ms: 1.10x faster                                                  |
| json                          | 3.10 ms                                                | 2.89 ms: 1.08x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                  |
| bench_thread_pool             | 545 us                                                 | 508 us: 1.07x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 50.7 ms: 1.06x faster                                                 |
| nqueens                       | 63.8 ms                                                | 61.9 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                  |
| xml_etree_iterparse           | 74.5 ms                                                | 72.4 ms: 1.03x faster                                                 |
| connected_components          | 318 ms                                                 | 311 ms: 1.02x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 76.3 ms: 1.02x faster                                                 |
| many_optionals                | 486 us                                                 | 478 us: 1.02x faster                                                  |
| fannkuch                      | 303 ms                                                 | 299 ms: 1.01x faster                                                  |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| shortest_path                 | 328 ms                                                 | 336 ms: 1.02x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.52 ms: 1.03x slower                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.44 ms: 1.04x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                 |
| coverage                      | 41.2 ms                                                | 48.2 ms: 1.17x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.18x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 281 ms: 1.20x slower                                                  |
| bench_mp_pool                 | 56.0 ms                                                | 69.5 ms: 1.24x slower                                                 |
| telco                         | 3.49 ms                                                | 4.56 ms: 1.31x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.33x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250712-3.15.0a0-47b01da-JIT/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.340x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.19x