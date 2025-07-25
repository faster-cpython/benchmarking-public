# Results vs. 3.10.4

- fork: faster-cpython
- ref: check_periodic_at_en
- machine: darwin-arm64
- commit hash: 021fc09
- commit date: 2025-07-25
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.18x faster                                                            |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| html5lib       | 43.5 ms                                                | 33.5 ms: 1.30x faster                                                           |
| sphinx         | 729 ms                                                 | 576 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.6 ms: 6.07x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.78x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                                            |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.35x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                           |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.05x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                           |
| nbody          | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                           |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 73.3 ms: 1.30x faster                                                           |
| regex_dna      | 175 ms                                                 | 138 ms: 1.27x faster                                                            |
| regex_v8       | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.15 ms: 1.09x faster                                                           |
| Geometric mean | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 129 us: 1.54x faster                                                            |
| tomli_loads          | 1.72 sec                                               | 1.23 sec: 1.40x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 209 us: 1.36x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 34.5 ms: 1.29x faster                                                           |
| json_dumps           | 8.31 ms                                                | 6.69 ms: 1.24x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 97.5 ms: 1.12x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 70.9 ms: 1.05x faster                                                           |
| json_loads           | 16.6 us                                                | 17.4 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.22x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.0 ms: 1.16x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                           |
| genshi_text     | 17.7 ms                                                | 15.7 ms: 1.13x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                           |
| django_template | 24.4 ms                                                | 23.3 ms: 1.05x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 64.6 ms: 6.07x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 139 ms: 3.47x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 95.8 us: 3.40x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 364 ms: 2.78x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 379 ms: 2.69x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 196 ms: 2.45x faster                                                            |
| async_tree_none               | 391 ms                                                 | 166 ms: 2.35x faster                                                            |
| mdp                           | 1.65 sec                                               | 772 ms: 2.14x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.54 ms: 1.96x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                            |
| raytrace                      | 327 ms                                                 | 177 ms: 1.85x faster                                                            |
| go                            | 163 ms                                                 | 89.1 ms: 1.83x faster                                                           |
| chaos                         | 67.7 ms                                                | 39.6 ms: 1.71x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 84.2 ms: 1.66x faster                                                           |
| richards_super                | 61.0 ms                                                | 37.5 ms: 1.62x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 420 ms: 1.59x faster                                                            |
| deepcopy                      | 276 us                                                 | 174 us: 1.58x faster                                                            |
| logging_silent                | 117 ns                                                 | 74.2 ns: 1.58x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 22.0 us: 1.58x faster                                                           |
| subparsers                    | 39.8 ms                                                | 25.4 ms: 1.57x faster                                                           |
| pyflate                       | 448 ms                                                 | 288 ms: 1.56x faster                                                            |
| richards                      | 52.3 ms                                                | 33.8 ms: 1.55x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 129 us: 1.54x faster                                                            |
| comprehensions                | 17.3 us                                                | 11.3 us: 1.53x faster                                                           |
| mako                          | 9.81 ms                                                | 6.46 ms: 1.52x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 64.2 ms: 1.48x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 49.0 ms: 1.48x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 49.8 ms: 1.47x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 913 ms: 1.46x faster                                                            |
| pprint_safe_repr              | 648 ms                                                 | 450 ms: 1.44x faster                                                            |
| pylint                        | 231 ms                                                 | 161 ms: 1.43x faster                                                            |
| float                         | 72.4 ms                                                | 51.5 ms: 1.41x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.23 sec: 1.40x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 25.5 ms: 1.40x faster                                                           |
| logging_format                | 5.03 us                                                | 3.69 us: 1.36x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 209 us: 1.36x faster                                                            |
| hexiom                        | 6.25 ms                                                | 4.62 ms: 1.35x faster                                                           |
| logging_simple                | 4.59 us                                                | 3.41 us: 1.35x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 76.1 ms: 1.35x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.78 us: 1.30x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 73.3 ms: 1.30x faster                                                           |
| html5lib                      | 43.5 ms                                                | 33.5 ms: 1.30x faster                                                           |
| generators                    | 31.7 ms                                                | 24.5 ms: 1.29x faster                                                           |
| nbody                         | 92.5 ms                                                | 71.6 ms: 1.29x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 34.5 ms: 1.29x faster                                                           |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.27x faster                                                            |
| sphinx                        | 729 ms                                                 | 576 ms: 1.27x faster                                                            |
| pycparser                     | 887 ms                                                 | 702 ms: 1.26x faster                                                            |
| k_core                        | 2.01 sec                                               | 1.60 sec: 1.26x faster                                                          |
| coroutines                    | 20.5 ms                                                | 16.5 ms: 1.24x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 6.69 ms: 1.24x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 15.5 ms: 1.24x faster                                                           |
| thrift                        | 562 us                                                 | 457 us: 1.23x faster                                                            |
| fannkuch                      | 303 ms                                                 | 249 ms: 1.22x faster                                                            |
| sympy_integrate               | 13.2 ms                                                | 10.9 ms: 1.20x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 77.2 ms: 1.20x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| scimark_fft                   | 225 ms                                                 | 191 ms: 1.18x faster                                                            |
| 2to3                          | 201 ms                                                 | 171 ms: 1.18x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 2.92 sec: 1.18x faster                                                          |
| python_startup                | 19.6 ms                                                | 17.0 ms: 1.16x faster                                                           |
| sympy_str                     | 166 ms                                                 | 147 ms: 1.13x faster                                                            |
| genshi_text                   | 17.7 ms                                                | 15.7 ms: 1.13x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 97.5 ms: 1.12x faster                                                           |
| pathlib                       | 25.7 ms                                                | 23.4 ms: 1.10x faster                                                           |
| xml_etree_generate            | 53.9 ms                                                | 49.2 ms: 1.10x faster                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.15 ms: 1.09x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 249 ms: 1.08x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 73.9 ms: 1.05x faster                                                           |
| xml_etree_iterparse           | 74.5 ms                                                | 70.9 ms: 1.05x faster                                                           |
| genshi_xml                    | 35.1 ms                                                | 33.5 ms: 1.05x faster                                                           |
| django_template               | 24.4 ms                                                | 23.3 ms: 1.05x faster                                                           |
| nqueens                       | 63.8 ms                                                | 62.2 ms: 1.03x faster                                                           |
| json                          | 3.10 ms                                                | 3.04 ms: 1.02x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.37 ms: 1.01x faster                                                           |
| python_startup_no_site        | 12.8 ms                                                | 12.7 ms: 1.01x faster                                                           |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                            |
| connected_components          | 318 ms                                                 | 323 ms: 1.01x slower                                                            |
| dask                          | 789 ms                                                 | 801 ms: 1.02x slower                                                            |
| json_loads                    | 16.6 us                                                | 17.4 us: 1.05x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                           |
| shortest_path                 | 328 ms                                                 | 351 ms: 1.07x slower                                                            |
| coverage                      | 41.2 ms                                                | 47.5 ms: 1.15x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                           |
| many_optionals                | 486 us                                                 | 595 us: 1.23x slower                                                            |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                            |
| telco                         | 3.49 ms                                                | 4.40 ms: 1.26x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250725-3.15.0a0-021fc09-JIT/bm-20250725-darwin-arm64-faster%2dcpython-check_periodic_at_en-3.15.0a0-021fc09.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.345x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.19x