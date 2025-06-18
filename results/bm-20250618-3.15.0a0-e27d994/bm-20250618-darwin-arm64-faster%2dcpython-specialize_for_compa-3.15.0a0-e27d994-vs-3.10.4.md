# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_compa
- machine: darwin-arm64
- commit hash: e27d994
- commit date: 2025-06-18
- overall geometric mean: 1.249x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                            |
| docutils       | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                          |
| html5lib       | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                           |
| sphinx         | 729 ms                                                 | 615 ms: 1.18x faster                                                            |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.8 ms: 5.38x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                            |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.46x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                            |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                           |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.93x faster                                                                    |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                           |
| nbody          | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                           |
| pidigits       | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| regex_compile  | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                           |
| regex_v8       | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                           |
| regex_effbot   | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 8.31 ms                                                | 6.81 ms: 1.22x faster                                                           |
| tomli_loads          | 1.72 sec                                               | 1.45 sec: 1.18x faster                                                          |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                            |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                            |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.06x faster                                                            |
| xml_etree_process    | 44.6 ms                                                | 43.3 ms: 1.03x faster                                                           |
| xml_etree_iterparse  | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                           |
| xml_etree_generate   | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.4 ms: 1.07x faster                                                           |
| python_startup_no_site | 12.8 ms                                                | 13.8 ms: 1.08x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.96 ms: 1.09x faster                                                           |
| genshi_xml      | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                           |
| django_template | 24.4 ms                                                | 25.1 ms: 1.03x slower                                                           |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994 |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 72.8 ms: 5.38x faster                                                           |
| async_tree_eager_memoization  | 483 ms                                                 | 151 ms: 3.21x faster                                                            |
| typing_runtime_protocols      | 326 us                                                 | 110 us: 2.96x faster                                                            |
| subparsers                    | 39.8 ms                                                | 14.8 ms: 2.69x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 392 ms: 2.59x faster                                                            |
| async_tree_io                 | 1.02 sec                                               | 413 ms: 2.46x faster                                                            |
| async_tree_memoization        | 481 ms                                                 | 214 ms: 2.24x faster                                                            |
| async_tree_none               | 391 ms                                                 | 182 ms: 2.15x faster                                                            |
| mdp                           | 1.65 sec                                               | 834 ms: 1.98x faster                                                            |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                            |
| deltablue                     | 4.99 ms                                                | 2.80 ms: 1.78x faster                                                           |
| go                            | 163 ms                                                 | 99.3 ms: 1.65x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 21.8 us: 1.59x faster                                                           |
| deepcopy                      | 276 us                                                 | 175 us: 1.57x faster                                                            |
| scimark_sor                   | 140 ms                                                 | 89.7 ms: 1.56x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 432 ms: 1.55x faster                                                            |
| raytrace                      | 327 ms                                                 | 212 ms: 1.54x faster                                                            |
| richards_super                | 61.0 ms                                                | 41.6 ms: 1.46x faster                                                           |
| chaos                         | 67.7 ms                                                | 47.1 ms: 1.44x faster                                                           |
| richards                      | 52.3 ms                                                | 37.2 ms: 1.41x faster                                                           |
| pylint                        | 231 ms                                                 | 168 ms: 1.38x faster                                                            |
| scimark_monte_carlo           | 72.4 ms                                                | 52.7 ms: 1.37x faster                                                           |
| k_core                        | 2.01 sec                                               | 1.47 sec: 1.37x faster                                                          |
| dulwich_log                   | 35.6 ms                                                | 26.3 ms: 1.35x faster                                                           |
| pyflate                       | 448 ms                                                 | 332 ms: 1.35x faster                                                            |
| spectral_norm                 | 95.3 ms                                                | 72.0 ms: 1.32x faster                                                           |
| comprehensions                | 17.3 us                                                | 13.1 us: 1.32x faster                                                           |
| html5lib                      | 43.5 ms                                                | 34.2 ms: 1.27x faster                                                           |
| float                         | 72.4 ms                                                | 57.9 ms: 1.25x faster                                                           |
| deepcopy_reduce               | 2.32 us                                                | 1.89 us: 1.23x faster                                                           |
| hexiom                        | 6.25 ms                                                | 5.09 ms: 1.23x faster                                                           |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                            |
| json_dumps                    | 8.31 ms                                                | 6.81 ms: 1.22x faster                                                           |
| scimark_lu                    | 103 ms                                                 | 84.6 ms: 1.21x faster                                                           |
| thrift                        | 562 us                                                 | 468 us: 1.20x faster                                                            |
| crypto_pyaes                  | 73.3 ms                                                | 61.1 ms: 1.20x faster                                                           |
| pycparser                     | 887 ms                                                 | 739 ms: 1.20x faster                                                            |
| sphinx                        | 729 ms                                                 | 615 ms: 1.18x faster                                                            |
| tomli_loads                   | 1.72 sec                                               | 1.45 sec: 1.18x faster                                                          |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                            |
| regex_compile                 | 95.6 ms                                                | 81.1 ms: 1.18x faster                                                           |
| regex_v8                      | 19.1 ms                                                | 16.3 ms: 1.18x faster                                                           |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                           |
| logging_format                | 5.03 us                                                | 4.35 us: 1.16x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.51 sec: 1.15x faster                                                          |
| sympy_sum                     | 92.7 ms                                                | 81.3 ms: 1.14x faster                                                           |
| pathlib                       | 25.7 ms                                                | 22.8 ms: 1.13x faster                                                           |
| logging_simple                | 4.59 us                                                | 4.07 us: 1.13x faster                                                           |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                            |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.12x faster                                                            |
| mako                          | 9.81 ms                                                | 8.96 ms: 1.09x faster                                                           |
| coroutines                    | 20.5 ms                                                | 18.9 ms: 1.09x faster                                                           |
| nbody                         | 92.5 ms                                                | 85.2 ms: 1.09x faster                                                           |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                            |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.18 ms: 1.08x faster                                                           |
| sympy_str                     | 166 ms                                                 | 154 ms: 1.07x faster                                                            |
| python_startup                | 19.6 ms                                                | 18.4 ms: 1.07x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.24 sec: 1.06x faster                                                          |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.06x faster                                                            |
| pprint_pformat                | 1.33 sec                                               | 1.27 sec: 1.05x faster                                                          |
| json                          | 3.10 ms                                                | 2.97 ms: 1.04x faster                                                           |
| connected_components          | 318 ms                                                 | 306 ms: 1.04x faster                                                            |
| meteor_contest                | 77.8 ms                                                | 74.9 ms: 1.04x faster                                                           |
| pprint_safe_repr              | 648 ms                                                 | 627 ms: 1.03x faster                                                            |
| xml_etree_process             | 44.6 ms                                                | 43.3 ms: 1.03x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 262 ms: 1.03x faster                                                            |
| dask                          | 789 ms                                                 | 771 ms: 1.02x faster                                                            |
| xml_etree_iterparse           | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                           |
| generators                    | 31.7 ms                                                | 31.6 ms: 1.00x faster                                                           |
| fannkuch                      | 303 ms                                                 | 304 ms: 1.01x slower                                                            |
| pidigits                      | 280 ms                                                 | 283 ms: 1.01x slower                                                            |
| many_optionals                | 486 us                                                 | 493 us: 1.02x slower                                                            |
| regex_effbot                  | 2.34 ms                                                | 2.37 ms: 1.02x slower                                                           |
| genshi_xml                    | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                           |
| django_template               | 24.4 ms                                                | 25.1 ms: 1.03x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.8 ms: 1.08x slower                                                           |
| xml_etree_generate            | 53.9 ms                                                | 58.6 ms: 1.09x slower                                                           |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.09x slower                                                           |
| nqueens                       | 63.8 ms                                                | 70.2 ms: 1.10x slower                                                           |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                           |
| async_generators              | 233 ms                                                 | 273 ms: 1.17x slower                                                            |
| gc_traversal                  | 2.71 ms                                                | 3.18 ms: 1.18x slower                                                           |
| coverage                      | 41.2 ms                                                | 49.3 ms: 1.20x slower                                                           |
| telco                         | 3.49 ms                                                | 4.75 ms: 1.36x slower                                                           |
| logging_silent                | 117 ns                                                 | 340 ns: 2.91x slower                                                            |
| Geometric mean                | (ref)                                                  | 1.23x faster                                                                    |

Benchmark hidden because not significant (4): json_loads, asyncio_websockets, genshi_text, shortest_path
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250618-3.15.0a0-e27d994/bm-20250618-darwin-arm64-faster%2dcpython-specialize_for_compa-3.15.0a0-e27d994.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.249x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.17x