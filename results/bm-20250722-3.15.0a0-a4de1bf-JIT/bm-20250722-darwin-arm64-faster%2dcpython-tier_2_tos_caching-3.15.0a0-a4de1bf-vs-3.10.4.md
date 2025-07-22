# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.373x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.20x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 167 ms: 1.20x faster                                                          |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                        |
| html5lib       | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                         |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                                          |
| Geometric mean | (ref)                                                  | 1.25x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.2 ms: 6.21x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 193 ms: 2.49x faster                                                          |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.40x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                          |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                         |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                          |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 92.5 ms                                                | 60.3 ms: 1.54x faster                                                         |
| float          | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.29x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.6 ms: 1.34x faster                                                         |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                          |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                         |
| regex_effbot   | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 118 us: 1.68x faster                                                          |
| tomli_loads          | 1.72 sec                                               | 1.15 sec: 1.50x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 202 us: 1.41x faster                                                          |
| xml_etree_process    | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                         |
| json_dumps           | 8.31 ms                                                | 6.60 ms: 1.26x faster                                                         |
| xml_etree_generate   | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                         |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 72.2 ms: 1.03x faster                                                         |
| json_loads           | 16.6 us                                                | 16.9 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.24x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.5 ms: 1.19x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.44 ms: 1.52x faster                                                         |
| genshi_text     | 17.7 ms                                                | 15.2 ms: 1.17x faster                                                         |
| genshi_xml      | 35.1 ms                                                | 32.7 ms: 1.08x faster                                                         |
| django_template | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.2 ms: 6.21x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 95.9 us: 3.40x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 359 ms: 2.83x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 193 ms: 2.49x faster                                                          |
| async_tree_none               | 391 ms                                                 | 163 ms: 2.40x faster                                                          |
| mdp                           | 1.65 sec                                               | 745 ms: 2.22x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.42 ms: 2.06x faster                                                         |
| go                            | 163 ms                                                 | 85.4 ms: 1.91x faster                                                         |
| raytrace                      | 327 ms                                                 | 172 ms: 1.91x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 359 ms: 1.87x faster                                                          |
| chaos                         | 67.7 ms                                                | 38.3 ms: 1.77x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 118 us: 1.68x faster                                                          |
| scimark_sor                   | 140 ms                                                 | 83.8 ms: 1.67x faster                                                         |
| pyflate                       | 448 ms                                                 | 270 ms: 1.66x faster                                                          |
| spectral_norm                 | 95.3 ms                                                | 58.8 ms: 1.62x faster                                                         |
| scimark_monte_carlo           | 72.4 ms                                                | 44.7 ms: 1.62x faster                                                         |
| richards_super                | 61.0 ms                                                | 37.8 ms: 1.61x faster                                                         |
| deepcopy_memo                 | 34.7 us                                                | 21.6 us: 1.61x faster                                                         |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 417 ms: 1.60x faster                                                          |
| deepcopy                      | 276 us                                                 | 173 us: 1.60x faster                                                          |
| logging_silent                | 117 ns                                                 | 73.6 ns: 1.59x faster                                                         |
| subparsers                    | 39.8 ms                                                | 25.2 ms: 1.58x faster                                                         |
| richards                      | 52.3 ms                                                | 33.4 ms: 1.57x faster                                                         |
| comprehensions                | 17.3 us                                                | 11.2 us: 1.54x faster                                                         |
| nbody                         | 92.5 ms                                                | 60.3 ms: 1.54x faster                                                         |
| mako                          | 9.81 ms                                                | 6.44 ms: 1.52x faster                                                         |
| hexiom                        | 6.25 ms                                                | 4.15 ms: 1.50x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.15 sec: 1.50x faster                                                        |
| crypto_pyaes                  | 73.3 ms                                                | 49.2 ms: 1.49x faster                                                         |
| pprint_safe_repr              | 648 ms                                                 | 447 ms: 1.45x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 921 ms: 1.44x faster                                                          |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 25.1 ms: 1.42x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 202 us: 1.41x faster                                                          |
| float                         | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                         |
| logging_format                | 5.03 us                                                | 3.63 us: 1.38x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 74.2 ms: 1.38x faster                                                         |
| logging_simple                | 4.59 us                                                | 3.35 us: 1.37x faster                                                         |
| regex_compile                 | 95.6 ms                                                | 71.6 ms: 1.34x faster                                                         |
| xml_etree_process             | 44.6 ms                                                | 33.6 ms: 1.33x faster                                                         |
| html5lib                      | 43.5 ms                                                | 32.9 ms: 1.32x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.31x faster                                                        |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.30x faster                                                         |
| generators                    | 31.7 ms                                                | 24.3 ms: 1.30x faster                                                         |
| pycparser                     | 887 ms                                                 | 692 ms: 1.28x faster                                                          |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                                          |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                          |
| json_dumps                    | 8.31 ms                                                | 6.60 ms: 1.26x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 180 ms: 1.25x faster                                                          |
| fannkuch                      | 303 ms                                                 | 243 ms: 1.24x faster                                                          |
| coroutines                    | 20.5 ms                                                | 16.6 ms: 1.24x faster                                                         |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.23x faster                                                         |
| thrift                        | 562 us                                                 | 456 us: 1.23x faster                                                          |
| bpe_tokeniser                 | 3.44 sec                                               | 2.80 sec: 1.23x faster                                                        |
| sympy_sum                     | 92.7 ms                                                | 76.1 ms: 1.22x faster                                                         |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.21x faster                                                         |
| 2to3                          | 201 ms                                                 | 167 ms: 1.20x faster                                                          |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                        |
| python_startup                | 19.6 ms                                                | 16.5 ms: 1.19x faster                                                         |
| genshi_text                   | 17.7 ms                                                | 15.2 ms: 1.17x faster                                                         |
| sympy_str                     | 166 ms                                                 | 144 ms: 1.15x faster                                                          |
| pathlib                       | 25.7 ms                                                | 23.0 ms: 1.12x faster                                                         |
| xml_etree_generate            | 53.9 ms                                                | 48.2 ms: 1.12x faster                                                         |
| meteor_contest                | 77.8 ms                                                | 70.1 ms: 1.11x faster                                                         |
| sympy_expand                  | 269 ms                                                 | 245 ms: 1.10x faster                                                          |
| regex_effbot                  | 2.34 ms                                                | 2.13 ms: 1.10x faster                                                         |
| genshi_xml                    | 35.1 ms                                                | 32.7 ms: 1.08x faster                                                         |
| nqueens                       | 63.8 ms                                                | 59.6 ms: 1.07x faster                                                         |
| django_template               | 24.4 ms                                                | 23.0 ms: 1.06x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.28 ms: 1.04x faster                                                         |
| json                          | 3.10 ms                                                | 2.98 ms: 1.04x faster                                                         |
| python_startup_no_site        | 12.8 ms                                                | 12.4 ms: 1.03x faster                                                         |
| xml_etree_iterparse           | 74.5 ms                                                | 72.2 ms: 1.03x faster                                                         |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                          |
| connected_components          | 318 ms                                                 | 313 ms: 1.02x faster                                                          |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| json_loads                    | 16.6 us                                                | 16.9 us: 1.02x slower                                                         |
| shortest_path                 | 328 ms                                                 | 341 ms: 1.04x slower                                                          |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                         |
| coverage                      | 41.2 ms                                                | 47.1 ms: 1.14x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.21 ms: 1.19x slower                                                         |
| many_optionals                | 486 us                                                 | 595 us: 1.22x slower                                                          |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                          |
| telco                         | 3.49 ms                                                | 4.42 ms: 1.27x slower                                                         |
| Geometric mean                | (ref)                                                  | 1.37x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.373x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.20x