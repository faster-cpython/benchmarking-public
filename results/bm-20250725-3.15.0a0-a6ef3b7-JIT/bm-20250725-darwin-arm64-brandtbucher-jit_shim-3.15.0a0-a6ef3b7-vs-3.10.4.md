# Results vs. 3.10.4

- fork: brandtbucher
- ref: jit_shim
- machine: darwin-arm64
- commit hash: a6ef3b7
- commit date: 2025-07-25
- overall geometric mean: 1.190x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 202 ms: 1.00x slower                                            |
| docutils       | 1.74 sec                                               | 1.82 sec: 1.05x slower                                          |
| html5lib       | 43.5 ms                                                | 38.1 ms: 1.14x faster                                           |
| sphinx         | 729 ms                                                 | 690 ms: 1.06x faster                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.4 ms: 5.49x faster                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                            |
| async_tree_eager_io           | 1.01 sec                                               | 418 ms: 2.43x faster                                            |
| async_tree_io                 | 1.02 sec                                               | 433 ms: 2.35x faster                                            |
| async_tree_memoization        | 481 ms                                                 | 224 ms: 2.15x faster                                            |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.10x faster                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 394 ms: 1.70x faster                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 466 ms: 1.44x faster                                            |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                           |
| asyncio_websockets            | 242 ms                                                 | 273 ms: 1.13x slower                                            |
| async_generators              | 233 ms                                                 | 316 ms: 1.35x slower                                            |
| Geometric mean                | (ref)                                                  | 1.84x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.7 ms: 1.30x faster                                           |
| nbody          | 92.5 ms                                                | 78.9 ms: 1.17x faster                                           |
| pidigits       | 280 ms                                                 | 310 ms: 1.11x slower                                            |
| Geometric mean | (ref)                                                  | 1.11x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 95.6 ms                                                | 82.1 ms: 1.16x faster                                           |
| regex_dna      | 175 ms                                                 | 152 ms: 1.15x faster                                            |
| regex_v8       | 19.1 ms                                                | 17.0 ms: 1.13x faster                                           |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.00x slower                                           |
| Geometric mean | (ref)                                                  | 1.11x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 143 us: 1.38x faster                                            |
| tomli_loads          | 1.72 sec                                               | 1.39 sec: 1.24x faster                                          |
| pickle_pure_python   | 285 us                                                 | 233 us: 1.22x faster                                            |
| json_dumps           | 8.31 ms                                                | 7.25 ms: 1.15x faster                                           |
| xml_etree_process    | 44.6 ms                                                | 39.3 ms: 1.13x faster                                           |
| xml_etree_generate   | 53.9 ms                                                | 56.0 ms: 1.04x slower                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 82.3 ms: 1.11x slower                                           |
| json_loads           | 16.6 us                                                | 19.2 us: 1.16x slower                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.5 ms: 1.06x faster                                           |
| python_startup_no_site | 12.8 ms                                                | 14.0 ms: 1.10x slower                                           |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.15 ms: 1.37x faster                                           |
| genshi_text     | 17.7 ms                                                | 16.6 ms: 1.07x faster                                           |
| genshi_xml      | 35.1 ms                                                | 36.3 ms: 1.03x slower                                           |
| django_template | 24.4 ms                                                | 25.7 ms: 1.05x slower                                           |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                    |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7 |
|-------------------------------|:------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.4 ms: 5.49x faster                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.19x faster                                            |
| typing_runtime_protocols      | 326 us                                                 | 105 us: 3.11x faster                                            |
| async_tree_eager_io           | 1.01 sec                                               | 418 ms: 2.43x faster                                            |
| async_tree_io                 | 1.02 sec                                               | 433 ms: 2.35x faster                                            |
| async_tree_memoization        | 481 ms                                                 | 224 ms: 2.15x faster                                            |
| async_tree_none               | 391 ms                                                 | 186 ms: 2.10x faster                                            |
| deltablue                     | 4.99 ms                                                | 2.79 ms: 1.79x faster                                           |
| mdp                           | 1.65 sec                                               | 925 ms: 1.78x faster                                            |
| go                            | 163 ms                                                 | 95.8 ms: 1.71x faster                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 394 ms: 1.70x faster                                            |
| raytrace                      | 327 ms                                                 | 193 ms: 1.69x faster                                            |
| chaos                         | 67.7 ms                                                | 42.7 ms: 1.58x faster                                           |
| scimark_sor                   | 140 ms                                                 | 92.0 ms: 1.52x faster                                           |
| richards_super                | 61.0 ms                                                | 41.0 ms: 1.49x faster                                           |
| deepcopy_memo                 | 34.7 us                                                | 23.5 us: 1.48x faster                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 49.1 ms: 1.47x faster                                           |
| logging_silent                | 117 ns                                                 | 80.3 ns: 1.46x faster                                           |
| deepcopy                      | 276 us                                                 | 190 us: 1.45x faster                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 466 ms: 1.44x faster                                            |
| richards                      | 52.3 ms                                                | 36.7 ms: 1.43x faster                                           |
| comprehensions                | 17.3 us                                                | 12.5 us: 1.39x faster                                           |
| spectral_norm                 | 95.3 ms                                                | 68.8 ms: 1.38x faster                                           |
| unpickle_pure_python          | 198 us                                                 | 143 us: 1.38x faster                                            |
| mako                          | 9.81 ms                                                | 7.15 ms: 1.37x faster                                           |
| subparsers                    | 39.8 ms                                                | 29.3 ms: 1.36x faster                                           |
| crypto_pyaes                  | 73.3 ms                                                | 55.4 ms: 1.32x faster                                           |
| pprint_pformat                | 1.33 sec                                               | 1.01 sec: 1.31x faster                                          |
| pyflate                       | 448 ms                                                 | 342 ms: 1.31x faster                                            |
| pprint_safe_repr              | 648 ms                                                 | 498 ms: 1.30x faster                                            |
| float                         | 72.4 ms                                                | 55.7 ms: 1.30x faster                                           |
| scimark_lu                    | 103 ms                                                 | 81.2 ms: 1.26x faster                                           |
| logging_format                | 5.03 us                                                | 4.06 us: 1.24x faster                                           |
| tomli_loads                   | 1.72 sec                                               | 1.39 sec: 1.24x faster                                          |
| logging_simple                | 4.59 us                                                | 3.73 us: 1.23x faster                                           |
| pickle_pure_python            | 285 us                                                 | 233 us: 1.22x faster                                            |
| hexiom                        | 6.25 ms                                                | 5.14 ms: 1.22x faster                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.96 us: 1.19x faster                                           |
| dulwich_log                   | 35.6 ms                                                | 30.1 ms: 1.18x faster                                           |
| generators                    | 31.7 ms                                                | 26.8 ms: 1.18x faster                                           |
| pylint                        | 231 ms                                                 | 196 ms: 1.18x faster                                            |
| nbody                         | 92.5 ms                                                | 78.9 ms: 1.17x faster                                           |
| regex_compile                 | 95.6 ms                                                | 82.1 ms: 1.16x faster                                           |
| regex_dna                     | 175 ms                                                 | 152 ms: 1.15x faster                                            |
| json_dumps                    | 8.31 ms                                                | 7.25 ms: 1.15x faster                                           |
| html5lib                      | 43.5 ms                                                | 38.1 ms: 1.14x faster                                           |
| coroutines                    | 20.5 ms                                                | 18.0 ms: 1.14x faster                                           |
| xml_etree_process             | 44.6 ms                                                | 39.3 ms: 1.13x faster                                           |
| regex_v8                      | 19.1 ms                                                | 17.0 ms: 1.13x faster                                           |
| thrift                        | 562 us                                                 | 508 us: 1.11x faster                                            |
| fannkuch                      | 303 ms                                                 | 274 ms: 1.10x faster                                            |
| scimark_fft                   | 225 ms                                                 | 208 ms: 1.08x faster                                            |
| genshi_text                   | 17.7 ms                                                | 16.6 ms: 1.07x faster                                           |
| python_startup                | 19.6 ms                                                | 18.5 ms: 1.06x faster                                           |
| sphinx                        | 729 ms                                                 | 690 ms: 1.06x faster                                            |
| pycparser                     | 887 ms                                                 | 856 ms: 1.04x faster                                            |
| bpe_tokeniser                 | 3.44 sec                                               | 3.32 sec: 1.03x faster                                          |
| pathlib                       | 25.7 ms                                                | 25.1 ms: 1.03x faster                                           |
| sympy_sum                     | 92.7 ms                                                | 91.1 ms: 1.02x faster                                           |
| 2to3                          | 201 ms                                                 | 202 ms: 1.00x slower                                            |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.00x slower                                           |
| sympy_integrate               | 13.2 ms                                                | 13.5 ms: 1.02x slower                                           |
| genshi_xml                    | 35.1 ms                                                | 36.3 ms: 1.03x slower                                           |
| sympy_str                     | 166 ms                                                 | 172 ms: 1.04x slower                                            |
| xml_etree_generate            | 53.9 ms                                                | 56.0 ms: 1.04x slower                                           |
| docutils                      | 1.74 sec                                               | 1.82 sec: 1.05x slower                                          |
| nqueens                       | 63.8 ms                                                | 67.1 ms: 1.05x slower                                           |
| django_template               | 24.4 ms                                                | 25.7 ms: 1.05x slower                                           |
| sympy_expand                  | 269 ms                                                 | 285 ms: 1.06x slower                                            |
| meteor_contest                | 77.8 ms                                                | 83.5 ms: 1.07x slower                                           |
| k_core                        | 2.01 sec                                               | 2.18 sec: 1.08x slower                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.72 ms: 1.09x slower                                           |
| json                          | 3.10 ms                                                | 3.40 ms: 1.10x slower                                           |
| python_startup_no_site        | 12.8 ms                                                | 14.0 ms: 1.10x slower                                           |
| pidigits                      | 280 ms                                                 | 310 ms: 1.11x slower                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 82.3 ms: 1.11x slower                                           |
| asyncio_websockets            | 242 ms                                                 | 273 ms: 1.13x slower                                            |
| json_loads                    | 16.6 us                                                | 19.2 us: 1.16x slower                                           |
| sqlite_synth                  | 1.48 us                                                | 1.75 us: 1.18x slower                                           |
| coverage                      | 41.2 ms                                                | 51.3 ms: 1.25x slower                                           |
| connected_components          | 318 ms                                                 | 419 ms: 1.32x slower                                            |
| async_generators              | 233 ms                                                 | 316 ms: 1.35x slower                                            |
| shortest_path                 | 328 ms                                                 | 452 ms: 1.38x slower                                            |
| telco                         | 3.49 ms                                                | 4.84 ms: 1.39x slower                                           |
| many_optionals                | 486 us                                                 | 713 us: 1.47x slower                                            |
| gc_traversal                  | 2.71 ms                                                | 4.62 ms: 1.71x slower                                           |
| create_gc_cycles              | 1.16 ms                                                | 2.14 ms: 1.83x slower                                           |
| Geometric mean                | (ref)                                                  | 1.19x faster                                                    |

Benchmark hidden because not significant (2): dask, xml_etree_parse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250725-3.15.0a0-a6ef3b7-JIT/bm-20250725-darwin-arm64-brandtbucher-jit_shim-3.15.0a0-a6ef3b7.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.190x faster

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.25x