# Results vs. 3.10.4

- fork: faster-cpython
- ref: fast_side_exits
- machine: darwin-arm64
- commit hash: 73832b2
- commit date: 2025-07-08
- overall geometric mean: 1.344x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 171 ms: 1.17x faster                                                       |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                     |
| html5lib       | 43.5 ms                                                | 31.6 ms: 1.38x faster                                                      |
| sphinx         | 729 ms                                                 | 583 ms: 1.25x faster                                                       |
| Geometric mean | (ref)                                                  | 1.25x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.6 ms: 6.16x faster                                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                       |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                       |
| async_tree_io                 | 1.02 sec                                               | 372 ms: 2.73x faster                                                       |
| async_tree_memoization        | 481 ms                                                 | 193 ms: 2.49x faster                                                       |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                                       |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                       |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.61x faster                                                       |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                      |
| async_generators              | 233 ms                                                 | 283 ms: 1.21x slower                                                       |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                               |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.8 ms: 1.45x faster                                                      |
| nbody          | 92.5 ms                                                | 75.6 ms: 1.22x faster                                                      |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                  | 1.21x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 71.3 ms: 1.34x faster                                                      |
| regex_dna      | 175 ms                                                 | 138 ms: 1.26x faster                                                       |
| regex_v8       | 19.1 ms                                                | 15.6 ms: 1.22x faster                                                      |
| Geometric mean | (ref)                                                  | 1.20x faster                                                               |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 135 us: 1.47x faster                                                       |
| tomli_loads          | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                     |
| pickle_pure_python   | 285 us                                                 | 210 us: 1.36x faster                                                       |
| json_dumps           | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                      |
| xml_etree_process    | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                      |
| xml_etree_parse      | 109 ms                                                 | 102 ms: 1.07x faster                                                       |
| xml_etree_generate   | 53.9 ms                                                | 50.8 ms: 1.06x faster                                                      |
| xml_etree_iterparse  | 74.5 ms                                                | 72.3 ms: 1.03x faster                                                      |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                      |
| Geometric mean       | (ref)                                                  | 1.20x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                      |
| python_startup_no_site | 12.8 ms                                                | 14.4 ms: 1.12x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.04x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.92 ms: 1.42x faster                                                      |
| genshi_text     | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                      |
| genshi_xml      | 35.1 ms                                                | 31.3 ms: 1.12x faster                                                      |
| django_template | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                      |
| Geometric mean  | (ref)                                                  | 1.21x faster                                                               |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2 |
|-------------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.6 ms: 6.16x faster                                                      |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                       |
| typing_runtime_protocols      | 326 us                                                 | 98.9 us: 3.30x faster                                                      |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.90x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 361 ms: 2.81x faster                                                       |
| async_tree_io                 | 1.02 sec                                               | 372 ms: 2.73x faster                                                       |
| async_tree_memoization        | 481 ms                                                 | 193 ms: 2.49x faster                                                       |
| async_tree_none               | 391 ms                                                 | 162 ms: 2.41x faster                                                       |
| mdp                           | 1.65 sec                                               | 756 ms: 2.18x faster                                                       |
| deltablue                     | 4.99 ms                                                | 2.62 ms: 1.91x faster                                                      |
| go                            | 163 ms                                                 | 87.3 ms: 1.87x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 358 ms: 1.87x faster                                                       |
| raytrace                      | 327 ms                                                 | 179 ms: 1.83x faster                                                       |
| deepcopy_memo                 | 34.7 us                                                | 19.6 us: 1.77x faster                                                      |
| deepcopy                      | 276 us                                                 | 156 us: 1.77x faster                                                       |
| chaos                         | 67.7 ms                                                | 39.3 ms: 1.72x faster                                                      |
| logging_silent                | 117 ns                                                 | 72.2 ns: 1.62x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.61x faster                                                       |
| scimark_monte_carlo           | 72.4 ms                                                | 45.9 ms: 1.58x faster                                                      |
| scimark_sor                   | 140 ms                                                 | 88.7 ms: 1.58x faster                                                      |
| pyflate                       | 448 ms                                                 | 288 ms: 1.55x faster                                                       |
| richards_super                | 61.0 ms                                                | 39.3 ms: 1.55x faster                                                      |
| richards                      | 52.3 ms                                                | 35.2 ms: 1.49x faster                                                      |
| unpickle_pure_python          | 198 us                                                 | 135 us: 1.47x faster                                                       |
| float                         | 72.4 ms                                                | 49.8 ms: 1.45x faster                                                      |
| spectral_norm                 | 95.3 ms                                                | 66.8 ms: 1.43x faster                                                      |
| mako                          | 9.81 ms                                                | 6.92 ms: 1.42x faster                                                      |
| pylint                        | 231 ms                                                 | 163 ms: 1.42x faster                                                       |
| dulwich_log                   | 35.6 ms                                                | 25.2 ms: 1.41x faster                                                      |
| comprehensions                | 17.3 us                                                | 12.4 us: 1.40x faster                                                      |
| tomli_loads                   | 1.72 sec                                               | 1.24 sec: 1.39x faster                                                     |
| deepcopy_reduce               | 2.32 us                                                | 1.68 us: 1.38x faster                                                      |
| html5lib                      | 43.5 ms                                                | 31.6 ms: 1.38x faster                                                      |
| pickle_pure_python            | 285 us                                                 | 210 us: 1.36x faster                                                       |
| logging_format                | 5.03 us                                                | 3.71 us: 1.36x faster                                                      |
| regex_compile                 | 95.6 ms                                                | 71.3 ms: 1.34x faster                                                      |
| logging_simple                | 4.59 us                                                | 3.44 us: 1.33x faster                                                      |
| k_core                        | 2.01 sec                                               | 1.52 sec: 1.33x faster                                                     |
| crypto_pyaes                  | 73.3 ms                                                | 55.6 ms: 1.32x faster                                                      |
| generators                    | 31.7 ms                                                | 24.2 ms: 1.31x faster                                                      |
| hexiom                        | 6.25 ms                                                | 4.77 ms: 1.31x faster                                                      |
| pycparser                     | 887 ms                                                 | 692 ms: 1.28x faster                                                       |
| thrift                        | 562 us                                                 | 441 us: 1.27x faster                                                       |
| json_dumps                    | 8.31 ms                                                | 6.55 ms: 1.27x faster                                                      |
| regex_dna                     | 175 ms                                                 | 138 ms: 1.26x faster                                                       |
| sphinx                        | 729 ms                                                 | 583 ms: 1.25x faster                                                       |
| xml_etree_process             | 44.6 ms                                                | 35.7 ms: 1.25x faster                                                      |
| scimark_lu                    | 103 ms                                                 | 82.2 ms: 1.25x faster                                                      |
| pprint_pformat                | 1.33 sec                                               | 1.08 sec: 1.23x faster                                                     |
| sympy_sum                     | 92.7 ms                                                | 75.7 ms: 1.22x faster                                                      |
| regex_v8                      | 19.1 ms                                                | 15.6 ms: 1.22x faster                                                      |
| nbody                         | 92.5 ms                                                | 75.6 ms: 1.22x faster                                                      |
| pprint_safe_repr              | 648 ms                                                 | 532 ms: 1.22x faster                                                       |
| coroutines                    | 20.5 ms                                                | 17.1 ms: 1.20x faster                                                      |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                     |
| genshi_text                   | 17.7 ms                                                | 14.9 ms: 1.19x faster                                                      |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.18x faster                                                      |
| 2to3                          | 201 ms                                                 | 171 ms: 1.17x faster                                                       |
| sympy_str                     | 166 ms                                                 | 144 ms: 1.15x faster                                                       |
| scimark_fft                   | 225 ms                                                 | 198 ms: 1.14x faster                                                       |
| genshi_xml                    | 35.1 ms                                                | 31.3 ms: 1.12x faster                                                      |
| bpe_tokeniser                 | 3.44 sec                                               | 3.07 sec: 1.12x faster                                                     |
| django_template               | 24.4 ms                                                | 21.9 ms: 1.11x faster                                                      |
| sympy_expand                  | 269 ms                                                 | 244 ms: 1.10x faster                                                       |
| pathlib                       | 25.7 ms                                                | 23.8 ms: 1.08x faster                                                      |
| xml_etree_parse               | 109 ms                                                 | 102 ms: 1.07x faster                                                       |
| json                          | 3.10 ms                                                | 2.89 ms: 1.07x faster                                                      |
| xml_etree_generate            | 53.9 ms                                                | 50.8 ms: 1.06x faster                                                      |
| python_startup                | 19.6 ms                                                | 18.9 ms: 1.04x faster                                                      |
| nqueens                       | 63.8 ms                                                | 61.5 ms: 1.04x faster                                                      |
| fannkuch                      | 303 ms                                                 | 292 ms: 1.03x faster                                                       |
| xml_etree_iterparse           | 74.5 ms                                                | 72.3 ms: 1.03x faster                                                      |
| dask                          | 789 ms                                                 | 769 ms: 1.03x faster                                                       |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                                       |
| many_optionals                | 486 us                                                 | 475 us: 1.02x faster                                                       |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                      |
| meteor_contest                | 77.8 ms                                                | 77.5 ms: 1.00x faster                                                      |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                       |
| shortest_path                 | 328 ms                                                 | 337 ms: 1.03x slower                                                       |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.55 ms: 1.04x slower                                                      |
| sqlite_synth                  | 1.48 us                                                | 1.58 us: 1.07x slower                                                      |
| python_startup_no_site        | 12.8 ms                                                | 14.4 ms: 1.12x slower                                                      |
| create_gc_cycles              | 1.16 ms                                                | 1.37 ms: 1.18x slower                                                      |
| coverage                      | 41.2 ms                                                | 48.5 ms: 1.18x slower                                                      |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                      |
| async_generators              | 233 ms                                                 | 283 ms: 1.21x slower                                                       |
| telco                         | 3.49 ms                                                | 4.60 ms: 1.32x slower                                                      |
| Geometric mean                | (ref)                                                  | 1.35x faster                                                               |

Benchmark hidden because not significant (2): asyncio_websockets, regex_effbot
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250708-3.15.0a0-73832b2-JIT/bm-20250708-darwin-arm64-faster%2dcpython-fast_side_exits-3.15.0a0-73832b2.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.344x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.18x