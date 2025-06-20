# Results vs. 3.10.4

- fork: python
- ref: 0f866cbfefd797b4dae2
- machine: darwin-arm64
- commit hash: 0f866cb
- commit date: 2025-06-10
- overall geometric mean: 1.260x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| docutils       | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| html5lib       | 43.5 ms                                                | 34.1 ms: 1.28x faster                                                 |
| sphinx         | 729 ms                                                 | 617 ms: 1.18x faster                                                  |
| Geometric mean | (ref)                                                  | 1.16x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.7 ms: 5.47x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 387 ms: 2.62x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 406 ms: 2.50x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.32x faster                                                  |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 427 ms: 1.56x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                 |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| nbody          | 92.5 ms                                                | 76.6 ms: 1.21x faster                                                 |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_compile  | 95.6 ms                                                | 79.7 ms: 1.20x faster                                                 |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                  | 1.15x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 138 us: 1.44x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.34 sec: 1.28x faster                                                |
| pickle_pure_python   | 285 us                                                 | 226 us: 1.26x faster                                                  |
| json_dumps           | 8.31 ms                                                | 6.86 ms: 1.21x faster                                                 |
| xml_etree_process    | 44.6 ms                                                | 37.7 ms: 1.18x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| xml_etree_generate   | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                 |
| xml_etree_iterparse  | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                          |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 20.2 ms: 1.03x slower                                                 |
| python_startup_no_site | 12.8 ms                                                | 15.6 ms: 1.22x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 6.94 ms: 1.41x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                 |
| django_template | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.7 ms: 5.47x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 104 us: 3.13x faster                                                  |
| subparsers                    | 39.8 ms                                                | 15.0 ms: 2.66x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 387 ms: 2.62x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 406 ms: 2.50x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 208 ms: 2.32x faster                                                  |
| async_tree_none               | 391 ms                                                 | 178 ms: 2.20x faster                                                  |
| mdp                           | 1.65 sec                                               | 826 ms: 2.00x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.89 ms: 1.72x faster                                                 |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                  |
| deepcopy                      | 276 us                                                 | 174 us: 1.58x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 427 ms: 1.56x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 22.3 us: 1.56x faster                                                 |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 90.6 ms: 1.54x faster                                                 |
| richards_super                | 61.0 ms                                                | 42.2 ms: 1.45x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 138 us: 1.44x faster                                                  |
| chaos                         | 67.7 ms                                                | 47.9 ms: 1.41x faster                                                 |
| mako                          | 9.81 ms                                                | 6.94 ms: 1.41x faster                                                 |
| pyflate                       | 448 ms                                                 | 321 ms: 1.40x faster                                                  |
| richards                      | 52.3 ms                                                | 37.6 ms: 1.39x faster                                                 |
| pylint                        | 231 ms                                                 | 170 ms: 1.36x faster                                                  |
| scimark_monte_carlo           | 72.4 ms                                                | 53.5 ms: 1.35x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 26.7 ms: 1.33x faster                                                 |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.53 sec: 1.32x faster                                                |
| spectral_norm                 | 95.3 ms                                                | 74.3 ms: 1.28x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.34 sec: 1.28x faster                                                |
| html5lib                      | 43.5 ms                                                | 34.1 ms: 1.28x faster                                                 |
| crypto_pyaes                  | 73.3 ms                                                | 58.0 ms: 1.26x faster                                                 |
| pickle_pure_python            | 285 us                                                 | 226 us: 1.26x faster                                                  |
| float                         | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                 |
| hexiom                        | 6.25 ms                                                | 5.01 ms: 1.25x faster                                                 |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| scimark_lu                    | 103 ms                                                 | 84.3 ms: 1.22x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.86 ms: 1.21x faster                                                 |
| nbody                         | 92.5 ms                                                | 76.6 ms: 1.21x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 79.7 ms: 1.20x faster                                                 |
| thrift                        | 562 us                                                 | 472 us: 1.19x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 37.7 ms: 1.18x faster                                                 |
| sphinx                        | 729 ms                                                 | 617 ms: 1.18x faster                                                  |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                 |
| pycparser                     | 887 ms                                                 | 753 ms: 1.18x faster                                                  |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.15x faster                                                 |
| sympy_sum                     | 92.7 ms                                                | 80.9 ms: 1.15x faster                                                 |
| logging_format                | 5.03 us                                                | 4.40 us: 1.14x faster                                                 |
| pathlib                       | 25.7 ms                                                | 22.9 ms: 1.12x faster                                                 |
| logging_simple                | 4.59 us                                                | 4.10 us: 1.12x faster                                                 |
| pprint_pformat                | 1.33 sec                                               | 1.20 sec: 1.11x faster                                                |
| bpe_tokeniser                 | 3.44 sec                                               | 3.10 sec: 1.11x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 585 ms: 1.11x faster                                                  |
| docutils                      | 1.74 sec                                               | 1.57 sec: 1.11x faster                                                |
| scimark_fft                   | 225 ms                                                 | 206 ms: 1.09x faster                                                  |
| 2to3                          | 201 ms                                                 | 185 ms: 1.09x faster                                                  |
| sympy_str                     | 166 ms                                                 | 155 ms: 1.07x faster                                                  |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                  |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                 |
| json                          | 3.10 ms                                                | 2.93 ms: 1.06x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 51.9 ms: 1.04x faster                                                 |
| connected_components          | 318 ms                                                 | 310 ms: 1.03x faster                                                  |
| dask                          | 789 ms                                                 | 772 ms: 1.02x faster                                                  |
| sympy_expand                  | 269 ms                                                 | 265 ms: 1.02x faster                                                  |
| meteor_contest                | 77.8 ms                                                | 77.0 ms: 1.01x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                 |
| regex_effbot                  | 2.34 ms                                                | 2.34 ms: 1.00x slower                                                 |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                  |
| python_startup                | 19.6 ms                                                | 20.2 ms: 1.03x slower                                                 |
| genshi_xml                    | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                 |
| shortest_path                 | 328 ms                                                 | 339 ms: 1.03x slower                                                  |
| django_template               | 24.4 ms                                                | 25.3 ms: 1.04x slower                                                 |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.56 ms: 1.04x slower                                                 |
| many_optionals                | 486 us                                                 | 508 us: 1.05x slower                                                  |
| nqueens                       | 63.8 ms                                                | 69.4 ms: 1.09x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.09x slower                                                 |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                 |
| coverage                      | 41.2 ms                                                | 49.6 ms: 1.20x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 15.6 ms: 1.22x slower                                                 |
| async_generators              | 233 ms                                                 | 286 ms: 1.23x slower                                                  |
| telco                         | 3.49 ms                                                | 4.57 ms: 1.31x slower                                                 |
| logging_silent                | 117 ns                                                 | 344 ns: 2.94x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.24x faster                                                          |

Benchmark hidden because not significant (5): json_loads, genshi_text, fannkuch, generators, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250610-3.15.0a0-0f866cb-JIT/bm-20250610-darwin-arm64-python-0f866cbfefd797b4dae2-3.15.0a0-0f866cb.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.260x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.19x