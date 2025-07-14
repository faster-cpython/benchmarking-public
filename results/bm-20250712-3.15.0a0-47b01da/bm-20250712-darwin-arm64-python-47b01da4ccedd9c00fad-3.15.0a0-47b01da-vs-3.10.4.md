# Results vs. 3.10.4

- fork: python
- ref: 47b01da4ccedd9c00fad
- machine: darwin-arm64
- commit hash: 47b01da
- commit date: 2025-07-12
- overall geometric mean: 1.249x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| html5lib       | 43.5 ms                                                | 34.4 ms: 1.27x faster                                                 |
| sphinx         | 729 ms                                                 | 615 ms: 1.19x faster                                                  |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.6 ms: 5.11x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.24x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 396 ms: 2.56x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 410 ms: 2.48x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.25x faster                                                  |
| async_tree_none               | 391 ms                                                 | 179 ms: 2.19x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                  |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.92x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 56.7 ms: 1.28x faster                                                 |
| nbody          | 92.5 ms                                                | 85.7 ms: 1.08x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.11x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 147 ms: 1.19x faster                                                  |
| regex_compile  | 95.6 ms                                                | 81.2 ms: 1.18x faster                                                 |
| regex_v8       | 19.1 ms                                                | 16.5 ms: 1.16x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.12x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                  |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                  |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.05x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 43.2 ms: 1.03x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                          |

Benchmark hidden because not significant (2): json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.96 ms: 1.10x faster                                                 |
| genshi_text     | 17.7 ms                                                | 17.9 ms: 1.01x slower                                                 |
| django_template | 24.4 ms                                                | 24.8 ms: 1.02x slower                                                 |
| genshi_xml      | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 76.6 ms: 5.11x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 149 ms: 3.24x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 105 us: 3.11x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.1 ms: 2.64x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 396 ms: 2.56x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 410 ms: 2.48x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.25x faster                                                  |
| async_tree_none               | 391 ms                                                 | 179 ms: 2.19x faster                                                  |
| mdp                           | 1.65 sec                                               | 819 ms: 2.02x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.72 ms: 1.83x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 367 ms: 1.82x faster                                                  |
| go                            | 163 ms                                                 | 99.5 ms: 1.64x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                 |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 89.9 ms: 1.56x faster                                                 |
| raytrace                      | 327 ms                                                 | 210 ms: 1.56x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                  |
| logging_silent                | 117 ns                                                 | 77.2 ns: 1.52x faster                                                 |
| chaos                         | 67.7 ms                                                | 46.1 ms: 1.47x faster                                                 |
| richards_super                | 61.0 ms                                                | 41.7 ms: 1.46x faster                                                 |
| richards                      | 52.3 ms                                                | 37.4 ms: 1.40x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                |
| pylint                        | 231 ms                                                 | 169 ms: 1.37x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 53.2 ms: 1.36x faster                                                 |
| pyflate                       | 448 ms                                                 | 333 ms: 1.34x faster                                                  |
| spectral_norm                 | 95.3 ms                                                | 72.0 ms: 1.32x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 27.5 ms: 1.30x faster                                                 |
| float                         | 72.4 ms                                                | 56.7 ms: 1.28x faster                                                 |
| html5lib                      | 43.5 ms                                                | 34.4 ms: 1.27x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.89 us: 1.23x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.09 ms: 1.23x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 60.8 ms: 1.21x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.43 sec: 1.20x faster                                                |
| scimark_lu                    | 103 ms                                                 | 85.8 ms: 1.20x faster                                                 |
| pycparser                     | 887 ms                                                 | 742 ms: 1.20x faster                                                  |
| logging_format                | 5.03 us                                                | 4.21 us: 1.19x faster                                                 |
| regex_dna                     | 175 ms                                                 | 147 ms: 1.19x faster                                                  |
| thrift                        | 562 us                                                 | 473 us: 1.19x faster                                                  |
| sphinx                        | 729 ms                                                 | 615 ms: 1.19x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                  |
| regex_compile                 | 95.6 ms                                                | 81.2 ms: 1.18x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.92 us: 1.17x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 11.2 ms: 1.17x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.5 ms: 1.16x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 80.3 ms: 1.15x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                |
| pathlib                       | 25.7 ms                                                | 22.9 ms: 1.12x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.12x faster                                                  |
| python_startup                | 19.6 ms                                                | 17.7 ms: 1.11x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.11x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 586 ms: 1.11x faster                                                  |
| mako                          | 9.81 ms                                                | 8.96 ms: 1.10x faster                                                 |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                 |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                  |
| nbody                         | 92.5 ms                                                | 85.7 ms: 1.08x faster                                                 |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.08x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.23 sec: 1.07x faster                                                |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.21 ms: 1.06x faster                                                 |
| json                          | 3.10 ms                                                | 2.94 ms: 1.05x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.05x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 74.3 ms: 1.05x faster                                                 |
| connected_components          | 318 ms                                                 | 305 ms: 1.04x faster                                                  |
| fannkuch                      | 303 ms                                                 | 290 ms: 1.04x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 261 ms: 1.03x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 43.2 ms: 1.03x faster                                                 |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                  |
| generators                    | 31.7 ms                                                | 31.5 ms: 1.01x faster                                                 |
| genshi_text                   | 17.7 ms                                                | 17.9 ms: 1.01x slower                                                 |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| django_template               | 24.4 ms                                                | 24.8 ms: 1.02x slower                                                 |
| bench_thread_pool             | 545 us                                                 | 556 us: 1.02x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.39 ms: 1.02x slower                                                 |
| many_optionals                | 486 us                                                 | 501 us: 1.03x slower                                                  |
| python_startup_no_site        | 12.8 ms                                                | 13.2 ms: 1.03x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 36.4 ms: 1.04x slower                                                 |
| xml_etree_generate            | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                 |
| nqueens                       | 63.8 ms                                                | 70.4 ms: 1.10x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.63 us: 1.10x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 277 ms: 1.19x slower                                                  |
| coverage                      | 41.2 ms                                                | 49.7 ms: 1.21x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 70.2 ms: 1.25x slower                                                 |
| telco                         | 3.49 ms                                                | 4.74 ms: 1.36x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.25x faster                                                          |

Benchmark hidden because not significant (4): json_loads, asyncio_websockets, xml_etree_iterparse, shortest_path
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250712-3.15.0a0-47b01da/bm-20250712-darwin-arm64-python-47b01da4ccedd9c00fad-3.15.0a0-47b01da.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.249x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.17x