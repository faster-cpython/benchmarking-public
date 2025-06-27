# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.383x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 168 ms: 1.20x faster                                                            |
| docutils       | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                           |
| sphinx         | 729 ms                                                 | 574 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                  | 1.28x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 348 ms: 2.91x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 368 ms: 2.77x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.59x faster                                                            |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.50x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 410 ms: 1.63x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.1 ms: 1.28x faster                                                           |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.12x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                           |
| nbody          | 92.5 ms                                                | 74.3 ms: 1.24x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.24x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 66.6 ms: 1.43x faster                                                           |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                           |
| Geometric mean | (ref)                                                  | 1.20x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 133 us: 1.49x faster                                                            |
| tomli_loads          | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 200 us: 1.43x faster                                                            |
| json_dumps           | 8.31 ms                                                | 6.46 ms: 1.29x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 35.0 ms: 1.27x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 50.2 ms: 1.07x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                           |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.23x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.82 ms: 1.44x faster                                                           |
| genshi_text     | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 29.0 ms: 1.21x faster                                                           |
| django_template | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.28x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 61.3 ms: 6.39x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 138 ms: 3.51x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 95.2 us: 3.43x faster                                                           |
| subparsers                    | 39.8 ms                                                | 13.1 ms: 3.03x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 348 ms: 2.91x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 368 ms: 2.77x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 186 ms: 2.59x faster                                                            |
| async_tree_none               | 391 ms                                                 | 156 ms: 2.50x faster                                                            |
| mdp                           | 1.65 sec                                               | 732 ms: 2.25x faster                                                            |
| go                            | 163 ms                                                 | 77.9 ms: 2.10x faster                                                           |
| deltablue                     | 4.99 ms                                                | 2.49 ms: 2.00x faster                                                           |
| raytrace                      | 327 ms                                                 | 170 ms: 1.92x faster                                                            |
| deepcopy_memo                 | 34.7 us                                                | 18.3 us: 1.90x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 356 ms: 1.88x faster                                                            |
| deepcopy                      | 276 us                                                 | 149 us: 1.85x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 76.3 ms: 1.83x faster                                                           |
| chaos                         | 67.7 ms                                                | 37.0 ms: 1.83x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 42.3 ms: 1.71x faster                                                           |
| richards_super                | 61.0 ms                                                | 37.0 ms: 1.65x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 410 ms: 1.63x faster                                                            |
| pyflate                       | 448 ms                                                 | 277 ms: 1.62x faster                                                            |
| richards                      | 52.3 ms                                                | 32.5 ms: 1.61x faster                                                           |
| float                         | 72.4 ms                                                | 46.8 ms: 1.55x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 133 us: 1.49x faster                                                            |
| comprehensions                | 17.3 us                                                | 11.6 us: 1.49x faster                                                           |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 64.7 ms: 1.47x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 24.2 ms: 1.47x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.17 sec: 1.47x faster                                                          |
| pylint                        | 231 ms                                                 | 159 ms: 1.45x faster                                                            |
| mako                          | 9.81 ms                                                | 6.82 ms: 1.44x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 66.6 ms: 1.43x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.43x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 200 us: 1.43x faster                                                            |
| hexiom                        | 6.25 ms                                                | 4.49 ms: 1.39x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 74.0 ms: 1.39x faster                                                           |
| generators                    | 31.7 ms                                                | 23.1 ms: 1.37x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 55.0 ms: 1.33x faster                                                           |
| logging_format                | 5.03 us                                                | 3.79 us: 1.33x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.47 us: 1.32x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 13.5 ms: 1.31x faster                                                           |
| thrift                        | 562 us                                                 | 434 us: 1.30x faster                                                            |
| pycparser                     | 887 ms                                                 | 686 ms: 1.29x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 6.46 ms: 1.29x faster                                                           |
| coroutines                    | 20.5 ms                                                | 16.1 ms: 1.28x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 35.0 ms: 1.27x faster                                                           |
| sphinx                        | 729 ms                                                 | 574 ms: 1.27x faster                                                            |
| sympy_sum                     | 92.7 ms                                                | 73.3 ms: 1.26x faster                                                           |
| nbody                         | 92.5 ms                                                | 74.3 ms: 1.24x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 10.7 ms: 1.23x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| genshi_xml                    | 35.1 ms                                                | 29.0 ms: 1.21x faster                                                           |
| 2to3                          | 201 ms                                                 | 168 ms: 1.20x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.45 sec: 1.20x faster                                                          |
| sympy_str                     | 166 ms                                                 | 139 ms: 1.20x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                           |
| pathlib                       | 25.7 ms                                                | 21.9 ms: 1.17x faster                                                           |
| pprint_pformat                | 1.33 sec                                               | 1.14 sec: 1.16x faster                                                          |
| django_template               | 24.4 ms                                                | 21.0 ms: 1.16x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 568 ms: 1.14x faster                                                            |
| sympy_expand                  | 269 ms                                                 | 236 ms: 1.14x faster                                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.04 sec: 1.13x faster                                                          |
| scimark_fft                   | 225 ms                                                 | 201 ms: 1.12x faster                                                            |
| python_startup                | 19.6 ms                                                | 17.9 ms: 1.10x faster                                                           |
| nqueens                       | 63.8 ms                                                | 58.9 ms: 1.08x faster                                                           |
| json                          | 3.10 ms                                                | 2.88 ms: 1.08x faster                                                           |
| xml_etree_generate            | 53.9 ms                                                | 50.2 ms: 1.07x faster                                                           |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 70.8 ms: 1.05x faster                                                           |
| fannkuch                      | 303 ms                                                 | 290 ms: 1.04x faster                                                            |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                                            |
| connected_components          | 318 ms                                                 | 309 ms: 1.03x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 75.7 ms: 1.03x faster                                                           |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                            |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                           |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| shortest_path                 | 328 ms                                                 | 335 ms: 1.02x slower                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.55 ms: 1.04x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.4 ms: 1.05x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.57 us: 1.06x slower                                                           |
| coverage                      | 41.2 ms                                                | 47.0 ms: 1.14x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.18x slower                                                           |
| async_generators              | 233 ms                                                 | 276 ms: 1.18x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.35 ms: 1.24x slower                                                           |
| telco                         | 3.49 ms                                                | 4.62 ms: 1.33x slower                                                           |
| logging_silent                | 117 ns                                                 | 325 ns: 2.78x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.36x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250626-3.15.0a0-892a89d-JIT/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.383x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.19x