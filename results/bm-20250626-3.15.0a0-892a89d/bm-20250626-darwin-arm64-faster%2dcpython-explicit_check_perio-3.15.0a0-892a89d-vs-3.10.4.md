# Results vs. 3.10.4

- fork: faster-cpython
- ref: explicit_check_perio
- machine: darwin-arm64
- commit hash: 892a89d
- commit date: 2025-06-26
- overall geometric mean: 1.410x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 163 ms: 1.24x faster                                                            |
| docutils       | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                          |
| html5lib       | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                           |
| sphinx         | 729 ms                                                 | 568 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.5 ms: 6.48x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.54x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 365 ms: 2.79x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 185 ms: 2.59x faster                                                            |
| async_tree_none               | 391 ms                                                 | 157 ms: 2.49x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 354 ms: 1.89x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                           |
| async_generators              | 233 ms                                                 | 259 ms: 1.11x slower                                                            |
| Geometric mean                | (ref)                                                  | 2.14x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 47.0 ms: 1.54x faster                                                           |
| nbody          | 92.5 ms                                                | 68.6 ms: 1.35x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.27x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 65.9 ms: 1.45x faster                                                           |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_v8       | 19.1 ms                                                | 16.0 ms: 1.20x faster                                                           |
| Geometric mean | (ref)                                                  | 1.21x faster                                                                    |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 203 us: 1.40x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 144 us: 1.38x faster                                                            |
| json_dumps           | 8.31 ms                                                | 6.39 ms: 1.30x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 37.3 ms: 1.20x faster                                                           |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                            |
| xml_etree_iterparse  | 74.5 ms                                                | 70.7 ms: 1.05x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                           |
| json_loads           | 16.6 us                                                | 16.3 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.0 ms: 1.23x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 11.7 ms: 1.10x faster                                                           |
| Geometric mean         | (ref)                                                  | 1.16x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 17.7 ms                                                | 13.4 ms: 1.32x faster                                                           |
| mako            | 9.81 ms                                                | 7.64 ms: 1.28x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 28.6 ms: 1.23x faster                                                           |
| django_template | 24.4 ms                                                | 20.9 ms: 1.17x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.25x faster                                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 60.5 ms: 6.48x faster                                                           |
| typing_runtime_protocols      | 326 us                                                 | 90.9 us: 3.59x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 137 ms: 3.54x faster                                                            |
| subparsers                    | 39.8 ms                                                | 13.1 ms: 3.04x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 347 ms: 2.92x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 365 ms: 2.79x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 185 ms: 2.59x faster                                                            |
| async_tree_none               | 391 ms                                                 | 157 ms: 2.49x faster                                                            |
| mdp                           | 1.65 sec                                               | 725 ms: 2.28x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.34 ms: 2.13x faster                                                           |
| go                            | 163 ms                                                 | 77.1 ms: 2.12x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 17.8 us: 1.95x faster                                                           |
| raytrace                      | 327 ms                                                 | 169 ms: 1.93x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 354 ms: 1.89x faster                                                            |
| deepcopy                      | 276 us                                                 | 149 us: 1.86x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 76.1 ms: 1.84x faster                                                           |
| chaos                         | 67.7 ms                                                | 37.1 ms: 1.83x faster                                                           |
| richards_super                | 61.0 ms                                                | 35.5 ms: 1.72x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 42.3 ms: 1.71x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 409 ms: 1.63x faster                                                            |
| richards                      | 52.3 ms                                                | 32.3 ms: 1.62x faster                                                           |
| comprehensions                | 17.3 us                                                | 10.9 us: 1.59x faster                                                           |
| pyflate                       | 448 ms                                                 | 284 ms: 1.58x faster                                                            |
| float                         | 72.4 ms                                                | 47.0 ms: 1.54x faster                                                           |
| hexiom                        | 6.25 ms                                                | 4.15 ms: 1.50x faster                                                           |
| html5lib                      | 43.5 ms                                                | 29.4 ms: 1.48x faster                                                           |
| dulwich_log                   | 35.6 ms                                                | 24.1 ms: 1.47x faster                                                           |
| spectral_norm                 | 95.3 ms                                                | 64.7 ms: 1.47x faster                                                           |
| pylint                        | 231 ms                                                 | 157 ms: 1.47x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.19 sec: 1.45x faster                                                          |
| regex_compile                 | 95.6 ms                                                | 65.9 ms: 1.45x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.62 us: 1.44x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 203 us: 1.40x faster                                                            |
| k_core                        | 2.01 sec                                               | 1.44 sec: 1.39x faster                                                          |
| scimark_lu                    | 103 ms                                                 | 74.4 ms: 1.38x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 144 us: 1.38x faster                                                            |
| pycparser                     | 887 ms                                                 | 648 ms: 1.37x faster                                                            |
| generators                    | 31.7 ms                                                | 23.2 ms: 1.37x faster                                                           |
| crypto_pyaes                  | 73.3 ms                                                | 54.2 ms: 1.35x faster                                                           |
| nbody                         | 92.5 ms                                                | 68.6 ms: 1.35x faster                                                           |
| logging_format                | 5.03 us                                                | 3.78 us: 1.33x faster                                                           |
| genshi_text                   | 17.7 ms                                                | 13.4 ms: 1.32x faster                                                           |
| logging_simple                | 4.59 us                                                | 3.47 us: 1.32x faster                                                           |
| json_dumps                    | 8.31 ms                                                | 6.39 ms: 1.30x faster                                                           |
| thrift                        | 562 us                                                 | 435 us: 1.29x faster                                                            |
| mako                          | 9.81 ms                                                | 7.64 ms: 1.28x faster                                                           |
| sphinx                        | 729 ms                                                 | 568 ms: 1.28x faster                                                            |
| coroutines                    | 20.5 ms                                                | 16.0 ms: 1.28x faster                                                           |
| sympy_sum                     | 92.7 ms                                                | 72.9 ms: 1.27x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 179 ms: 1.26x faster                                                            |
| sympy_integrate               | 13.2 ms                                                | 10.5 ms: 1.26x faster                                                           |
| fannkuch                      | 303 ms                                                 | 241 ms: 1.26x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.07 sec: 1.24x faster                                                          |
| 2to3                          | 201 ms                                                 | 163 ms: 1.24x faster                                                            |
| docutils                      | 1.74 sec                                               | 1.41 sec: 1.23x faster                                                          |
| genshi_xml                    | 35.1 ms                                                | 28.6 ms: 1.23x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 528 ms: 1.23x faster                                                            |
| python_startup                | 19.6 ms                                                | 16.0 ms: 1.23x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| sympy_str                     | 166 ms                                                 | 137 ms: 1.21x faster                                                            |
| regex_v8                      | 19.1 ms                                                | 16.0 ms: 1.20x faster                                                           |
| xml_etree_process             | 44.6 ms                                                | 37.3 ms: 1.20x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 2.93 sec: 1.17x faster                                                          |
| django_template               | 24.4 ms                                                | 20.9 ms: 1.17x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 231 ms: 1.16x faster                                                            |
| pathlib                       | 25.7 ms                                                | 22.3 ms: 1.16x faster                                                           |
| nqueens                       | 63.8 ms                                                | 57.0 ms: 1.12x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 69.7 ms: 1.12x faster                                                           |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.09 ms: 1.11x faster                                                           |
| python_startup_no_site        | 12.8 ms                                                | 11.7 ms: 1.10x faster                                                           |
| json                          | 3.10 ms                                                | 2.87 ms: 1.08x faster                                                           |
| connected_components          | 318 ms                                                 | 295 ms: 1.08x faster                                                            |
| many_optionals                | 486 us                                                 | 452 us: 1.07x faster                                                            |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 70.7 ms: 1.05x faster                                                           |
| xml_etree_generate            | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                           |
| dask                          | 789 ms                                                 | 765 ms: 1.03x faster                                                            |
| shortest_path                 | 328 ms                                                 | 320 ms: 1.02x faster                                                            |
| json_loads                    | 16.6 us                                                | 16.3 us: 1.01x faster                                                           |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                           |
| async_generators              | 233 ms                                                 | 259 ms: 1.11x slower                                                            |
| coverage                      | 41.2 ms                                                | 47.5 ms: 1.15x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                           |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                           |
| telco                         | 3.49 ms                                                | 4.42 ms: 1.27x slower                                                           |
| logging_silent                | 117 ns                                                 | 321 ns: 2.75x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.39x faster                                                                    |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250626-3.15.0a0-892a89d/bm-20250626-darwin-arm64-faster%2dcpython-explicit_check_perio-3.15.0a0-892a89d.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.410x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.18x