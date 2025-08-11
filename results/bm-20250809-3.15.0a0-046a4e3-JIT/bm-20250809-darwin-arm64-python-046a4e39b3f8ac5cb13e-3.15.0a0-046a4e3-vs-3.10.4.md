# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: darwin-arm64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| html5lib       | 43.5 ms                                                | 33.5 ms: 1.30x faster                                                 |
| sphinx         | 729 ms                                                 | 576 ms: 1.26x faster                                                  |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.4 ms: 6.08x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 376 ms: 2.70x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.35x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                  |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.05x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| nbody          | 92.5 ms                                                | 72.4 ms: 1.28x faster                                                 |
| pidigits       | 280 ms                                                 | 285 ms: 1.02x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.7 ms: 1.31x faster                                                 |
| regex_dna      | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| Geometric mean | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 128 us: 1.54x faster                                                  |
| json_dumps           | 8.31 ms                                                | 5.81 ms: 1.43x faster                                                 |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.38x faster                                                |
| pickle_pure_python   | 285 us                                                 | 209 us: 1.36x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 34.6 ms: 1.29x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 100 ms: 1.09x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 49.3 ms: 1.09x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 71.1 ms: 1.05x faster                                                 |
| json_loads           | 16.6 us                                                | 17.5 us: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.6 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.53 ms: 1.50x faster                                                 |
| genshi_text     | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| django_template | 24.4 ms                                                | 23.1 ms: 1.06x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.18x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.4 ms: 6.08x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.48x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 95.5 us: 3.41x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 376 ms: 2.70x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 377 ms: 2.70x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.35x faster                                                  |
| mdp                           | 1.65 sec                                               | 776 ms: 2.13x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.55 ms: 1.96x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                  |
| go                            | 163 ms                                                 | 87.4 ms: 1.87x faster                                                 |
| raytrace                      | 327 ms                                                 | 177 ms: 1.84x faster                                                  |
| chaos                         | 67.7 ms                                                | 39.2 ms: 1.73x faster                                                 |
| scimark_sor                   | 140 ms                                                 | 85.1 ms: 1.64x faster                                                 |
| richards_super                | 61.0 ms                                                | 37.5 ms: 1.63x faster                                                 |
| deepcopy_memo                 | 34.7 us                                                | 21.6 us: 1.61x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 419 ms: 1.60x faster                                                  |
| deepcopy                      | 276 us                                                 | 173 us: 1.59x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 45.6 ms: 1.59x faster                                                 |
| subparsers                    | 39.8 ms                                                | 25.4 ms: 1.57x faster                                                 |
| logging_silent                | 117 ns                                                 | 75.2 ns: 1.56x faster                                                 |
| pyflate                       | 448 ms                                                 | 289 ms: 1.55x faster                                                  |
| richards                      | 52.3 ms                                                | 33.8 ms: 1.55x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 128 us: 1.54x faster                                                  |
| comprehensions                | 17.3 us                                                | 11.4 us: 1.51x faster                                                 |
| mako                          | 9.81 ms                                                | 6.53 ms: 1.50x faster                                                 |
| spectral_norm                 | 95.3 ms                                                | 64.3 ms: 1.48x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 49.7 ms: 1.47x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 901 ms: 1.47x faster                                                  |
| pprint_safe_repr              | 648 ms                                                 | 448 ms: 1.45x faster                                                  |
| json_dumps                    | 8.31 ms                                                | 5.81 ms: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                  |
| float                         | 72.4 ms                                                | 51.1 ms: 1.42x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 25.4 ms: 1.40x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.38x faster                                                |
| logging_format                | 5.03 us                                                | 3.65 us: 1.38x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.37 us: 1.36x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 209 us: 1.36x faster                                                  |
| hexiom                        | 6.25 ms                                                | 4.65 ms: 1.34x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 77.1 ms: 1.33x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.7 ms: 1.31x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.30x faster                                                 |
| generators                    | 31.7 ms                                                | 24.4 ms: 1.30x faster                                                 |
| html5lib                      | 43.5 ms                                                | 33.5 ms: 1.30x faster                                                 |
| xml_etree_process             | 44.6 ms                                                | 34.6 ms: 1.29x faster                                                 |
| nbody                         | 92.5 ms                                                | 72.4 ms: 1.28x faster                                                 |
| sphinx                        | 729 ms                                                 | 576 ms: 1.26x faster                                                  |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.26x faster                                                  |
| pycparser                     | 887 ms                                                 | 703 ms: 1.26x faster                                                  |
| k_core                        | 2.01 sec                                               | 1.60 sec: 1.26x faster                                                |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                 |
| thrift                        | 562 us                                                 | 457 us: 1.23x faster                                                  |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.22x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 76.9 ms: 1.21x faster                                                 |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                |
| 2to3                          | 201 ms                                                 | 171 ms: 1.18x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 2.93 sec: 1.17x faster                                                |
| scimark_fft                   | 225 ms                                                 | 194 ms: 1.16x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 15.4 ms: 1.15x faster                                                 |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                 |
| bench_thread_pool             | 545 us                                                 | 498 us: 1.10x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 100 ms: 1.09x faster                                                  |
| xml_etree_generate            | 53.9 ms                                                | 49.3 ms: 1.09x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.0 ms: 1.09x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 71.7 ms: 1.08x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 248 ms: 1.08x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 33.0 ms: 1.06x faster                                                 |
| django_template               | 24.4 ms                                                | 23.1 ms: 1.06x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 71.1 ms: 1.05x faster                                                 |
| nqueens                       | 63.8 ms                                                | 62.2 ms: 1.03x faster                                                 |
| json                          | 3.10 ms                                                | 3.07 ms: 1.01x faster                                                 |
| dask                          | 789 ms                                                 | 797 ms: 1.01x slower                                                  |
| connected_components          | 318 ms                                                 | 322 ms: 1.01x slower                                                  |
| pidigits                      | 280 ms                                                 | 285 ms: 1.02x slower                                                  |
| json_loads                    | 16.6 us                                                | 17.5 us: 1.05x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.6 ms: 1.06x slower                                                 |
| shortest_path                 | 328 ms                                                 | 350 ms: 1.07x slower                                                  |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                 |
| coverage                      | 41.2 ms                                                | 48.0 ms: 1.16x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                                  |
| many_optionals                | 486 us                                                 | 598 us: 1.23x slower                                                  |
| telco                         | 3.49 ms                                                | 4.47 ms: 1.28x slower                                                 |
| bench_mp_pool                 | 56.0 ms                                                | 72.0 ms: 1.29x slower                                                 |
| Geometric mean                | (ref)                                                  | 1.33x faster                                                          |

Benchmark hidden because not significant (3): scimark_sparse_mat_mult, pathlib, asyncio_websockets
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (20) of results/bm-20250809-3.15.0a0-046a4e3-JIT/bm-20250809-darwin-arm64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.20x