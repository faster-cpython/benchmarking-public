# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: darwin-arm64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.336x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 170 ms: 1.18x faster                                                  |
| docutils       | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| html5lib       | 43.5 ms                                                | 31.6 ms: 1.38x faster                                                 |
| sphinx         | 729 ms                                                 | 585 ms: 1.25x faster                                                  |
| Geometric mean | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.9 ms: 6.13x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                  |
| async_tree_eager_io           | 1.01 sec                                               | 365 ms: 2.78x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                  |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.62x faster                                                  |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                  |
| Geometric mean                | (ref)                                                  | 2.07x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 49.5 ms: 1.46x faster                                                 |
| nbody          | 92.5 ms                                                | 75.1 ms: 1.23x faster                                                 |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 72.0 ms: 1.33x faster                                                 |
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| regex_v8       | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                 |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| Geometric mean | (ref)                                                  | 1.17x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 219 us: 1.30x faster                                                  |
| tomli_loads          | 1.72 sec                                               | 1.36 sec: 1.27x faster                                                |
| json_dumps           | 8.31 ms                                                | 6.61 ms: 1.26x faster                                                 |
| unpickle_pure_python | 198 us                                                 | 161 us: 1.23x faster                                                  |
| xml_etree_process    | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                 |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| xml_etree_iterparse  | 74.5 ms                                                | 72.8 ms: 1.02x faster                                                 |
| json_loads           | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate   | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                 |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.1 ms: 1.09x faster                                                 |
| python_startup_no_site | 12.8 ms                                                | 13.5 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                 |
| genshi_text     | 17.7 ms                                                | 14.7 ms: 1.21x faster                                                 |
| genshi_xml      | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| django_template | 24.4 ms                                                | 22.0 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.17x faster                                                          |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 63.9 ms: 6.13x faster                                                 |
| async_tree_eager_memoization  | 483 ms                                                 | 140 ms: 3.45x faster                                                  |
| typing_runtime_protocols      | 326 us                                                 | 96.7 us: 3.37x faster                                                 |
| subparsers                    | 39.8 ms                                                | 13.7 ms: 2.92x faster                                                 |
| async_tree_eager_io           | 1.01 sec                                               | 365 ms: 2.78x faster                                                  |
| async_tree_io                 | 1.02 sec                                               | 380 ms: 2.68x faster                                                  |
| async_tree_memoization        | 481 ms                                                 | 195 ms: 2.47x faster                                                  |
| async_tree_none               | 391 ms                                                 | 164 ms: 2.38x faster                                                  |
| mdp                           | 1.65 sec                                               | 761 ms: 2.17x faster                                                  |
| deltablue                     | 4.99 ms                                                | 2.58 ms: 1.94x faster                                                 |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 357 ms: 1.87x faster                                                  |
| go                            | 163 ms                                                 | 87.5 ms: 1.87x faster                                                 |
| raytrace                      | 327 ms                                                 | 180 ms: 1.81x faster                                                  |
| deepcopy_memo                 | 34.7 us                                                | 19.3 us: 1.80x faster                                                 |
| deepcopy                      | 276 us                                                 | 156 us: 1.77x faster                                                  |
| chaos                         | 67.7 ms                                                | 40.2 ms: 1.68x faster                                                 |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 414 ms: 1.62x faster                                                  |
| scimark_sor                   | 140 ms                                                 | 88.4 ms: 1.58x faster                                                 |
| scimark_monte_carlo           | 72.4 ms                                                | 46.6 ms: 1.55x faster                                                 |
| richards_super                | 61.0 ms                                                | 40.2 ms: 1.51x faster                                                 |
| float                         | 72.4 ms                                                | 49.5 ms: 1.46x faster                                                 |
| richards                      | 52.3 ms                                                | 35.8 ms: 1.46x faster                                                 |
| comprehensions                | 17.3 us                                                | 12.0 us: 1.44x faster                                                 |
| dulwich_log                   | 35.6 ms                                                | 24.9 ms: 1.43x faster                                                 |
| pylint                        | 231 ms                                                 | 162 ms: 1.43x faster                                                  |
| pyflate                       | 448 ms                                                 | 319 ms: 1.40x faster                                                  |
| deepcopy_reduce               | 2.32 us                                                | 1.68 us: 1.38x faster                                                 |
| html5lib                      | 43.5 ms                                                | 31.6 ms: 1.38x faster                                                 |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                |
| spectral_norm                 | 95.3 ms                                                | 70.9 ms: 1.34x faster                                                 |
| hexiom                        | 6.25 ms                                                | 4.69 ms: 1.33x faster                                                 |
| regex_compile                 | 95.6 ms                                                | 72.0 ms: 1.33x faster                                                 |
| generators                    | 31.7 ms                                                | 24.0 ms: 1.32x faster                                                 |
| pycparser                     | 887 ms                                                 | 682 ms: 1.30x faster                                                  |
| pickle_pure_python            | 285 us                                                 | 219 us: 1.30x faster                                                  |
| crypto_pyaes                  | 73.3 ms                                                | 57.1 ms: 1.28x faster                                                 |
| tomli_loads                   | 1.72 sec                                               | 1.36 sec: 1.27x faster                                                |
| thrift                        | 562 us                                                 | 444 us: 1.27x faster                                                  |
| logging_format                | 5.03 us                                                | 3.97 us: 1.27x faster                                                 |
| json_dumps                    | 8.31 ms                                                | 6.61 ms: 1.26x faster                                                 |
| mako                          | 9.81 ms                                                | 7.81 ms: 1.26x faster                                                 |
| logging_simple                | 4.59 us                                                | 3.66 us: 1.25x faster                                                 |
| sphinx                        | 729 ms                                                 | 585 ms: 1.25x faster                                                  |
| nbody                         | 92.5 ms                                                | 75.1 ms: 1.23x faster                                                 |
| scimark_lu                    | 103 ms                                                 | 83.3 ms: 1.23x faster                                                 |
| unpickle_pure_python          | 198 us                                                 | 161 us: 1.23x faster                                                  |
| sympy_sum                     | 92.7 ms                                                | 75.6 ms: 1.22x faster                                                 |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                  |
| genshi_text                   | 17.7 ms                                                | 14.7 ms: 1.21x faster                                                 |
| coroutines                    | 20.5 ms                                                | 17.0 ms: 1.20x faster                                                 |
| docutils                      | 1.74 sec                                               | 1.46 sec: 1.19x faster                                                |
| sympy_integrate               | 13.2 ms                                                | 11.1 ms: 1.19x faster                                                 |
| regex_v8                      | 19.1 ms                                                | 16.1 ms: 1.19x faster                                                 |
| 2to3                          | 201 ms                                                 | 170 ms: 1.18x faster                                                  |
| pprint_pformat                | 1.33 sec                                               | 1.13 sec: 1.18x faster                                                |
| pprint_safe_repr              | 648 ms                                                 | 558 ms: 1.16x faster                                                  |
| sympy_str                     | 166 ms                                                 | 143 ms: 1.16x faster                                                  |
| scimark_fft                   | 225 ms                                                 | 196 ms: 1.15x faster                                                  |
| xml_etree_process             | 44.6 ms                                                | 38.9 ms: 1.15x faster                                                 |
| fannkuch                      | 303 ms                                                 | 267 ms: 1.13x faster                                                  |
| genshi_xml                    | 35.1 ms                                                | 31.2 ms: 1.13x faster                                                 |
| sympy_expand                  | 269 ms                                                 | 241 ms: 1.12x faster                                                  |
| bpe_tokeniser                 | 3.44 sec                                               | 3.09 sec: 1.11x faster                                                |
| django_template               | 24.4 ms                                                | 22.0 ms: 1.11x faster                                                 |
| python_startup                | 19.6 ms                                                | 18.1 ms: 1.09x faster                                                 |
| json                          | 3.10 ms                                                | 2.87 ms: 1.08x faster                                                 |
| pathlib                       | 25.7 ms                                                | 24.1 ms: 1.07x faster                                                 |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                  |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.23 ms: 1.06x faster                                                 |
| meteor_contest                | 77.8 ms                                                | 73.7 ms: 1.06x faster                                                 |
| many_optionals                | 486 us                                                 | 466 us: 1.04x faster                                                  |
| connected_components          | 318 ms                                                 | 307 ms: 1.04x faster                                                  |
| dask                          | 789 ms                                                 | 766 ms: 1.03x faster                                                  |
| nqueens                       | 63.8 ms                                                | 61.9 ms: 1.03x faster                                                 |
| xml_etree_iterparse           | 74.5 ms                                                | 72.8 ms: 1.02x faster                                                 |
| json_loads                    | 16.6 us                                                | 16.4 us: 1.01x faster                                                 |
| xml_etree_generate            | 53.9 ms                                                | 53.6 ms: 1.01x faster                                                 |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                  |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                 |
| python_startup_no_site        | 12.8 ms                                                | 13.5 ms: 1.06x slower                                                 |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                 |
| async_generators              | 233 ms                                                 | 263 ms: 1.13x slower                                                  |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                 |
| coverage                      | 41.2 ms                                                | 48.1 ms: 1.17x slower                                                 |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                 |
| telco                         | 3.49 ms                                                | 4.50 ms: 1.29x slower                                                 |
| logging_silent                | 117 ns                                                 | 331 ns: 2.82x slower                                                  |
| Geometric mean                | (ref)                                                  | 1.32x faster                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, shortest_path
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-darwin-arm64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.336x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: 1.17x