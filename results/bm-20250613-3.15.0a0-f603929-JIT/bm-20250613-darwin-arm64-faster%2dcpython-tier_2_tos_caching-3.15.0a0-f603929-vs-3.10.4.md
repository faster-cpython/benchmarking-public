# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: darwin-arm64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.174x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                        |
| html5lib       | 43.5 ms                                                | 34.0 ms: 1.28x faster                                                         |
| sphinx         | 729 ms                                                 | 616 ms: 1.18x faster                                                          |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.7 ms: 5.46x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.61x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.33x faster                                                          |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.21x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                          |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                         |
| async_generators              | 233 ms                                                 | 287 ms: 1.23x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.94x faster                                                                  |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.2 ms: 1.25x faster                                                         |
| nbody          | 92.5 ms                                                | 78.6 ms: 1.18x faster                                                         |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 143 ms: 1.22x faster                                                          |
| regex_compile  | 95.6 ms                                                | 79.4 ms: 1.20x faster                                                         |
| regex_v8       | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                  |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| unpickle_pure_python | 198 us                                                 | 138 us: 1.44x faster                                                          |
| tomli_loads          | 1.72 sec                                               | 1.31 sec: 1.31x faster                                                        |
| pickle_pure_python   | 285 us                                                 | 227 us: 1.25x faster                                                          |
| json_dumps           | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                         |
| xml_etree_process    | 44.6 ms                                                | 37.9 ms: 1.18x faster                                                         |
| xml_etree_parse      | 109 ms                                                 | 103 ms: 1.07x faster                                                          |
| xml_etree_generate   | 53.9 ms                                                | 52.0 ms: 1.04x faster                                                         |
| xml_etree_iterparse  | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                         |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                                  |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 16.1 ms: 1.22x faster                                                         |
| python_startup_no_site | 12.8 ms                                                | 11.9 ms: 1.08x faster                                                         |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 7.18 ms: 1.37x faster                                                         |
| genshi_text     | 17.7 ms                                                | 17.7 ms: 1.00x faster                                                         |
| genshi_xml      | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                         |
| django_template | 24.4 ms                                                | 25.4 ms: 1.04x slower                                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-------------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 71.7 ms: 5.46x faster                                                         |
| async_tree_eager_memoization  | 483 ms                                                 | 150 ms: 3.22x faster                                                          |
| typing_runtime_protocols      | 326 us                                                 | 106 us: 3.09x faster                                                          |
| subparsers                    | 39.8 ms                                                | 15.0 ms: 2.65x faster                                                         |
| async_tree_eager_io           | 1.01 sec                                               | 388 ms: 2.61x faster                                                          |
| async_tree_io                 | 1.02 sec                                               | 405 ms: 2.51x faster                                                          |
| async_tree_memoization        | 481 ms                                                 | 207 ms: 2.33x faster                                                          |
| async_tree_none               | 391 ms                                                 | 177 ms: 2.21x faster                                                          |
| mdp                           | 1.65 sec                                               | 819 ms: 2.02x faster                                                          |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 368 ms: 1.82x faster                                                          |
| deltablue                     | 4.99 ms                                                | 2.88 ms: 1.73x faster                                                         |
| go                            | 163 ms                                                 | 100 ms: 1.63x faster                                                          |
| deepcopy                      | 276 us                                                 | 175 us: 1.58x faster                                                          |
| deepcopy_memo                 | 34.7 us                                                | 22.4 us: 1.55x faster                                                         |
| raytrace                      | 327 ms                                                 | 211 ms: 1.55x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 431 ms: 1.55x faster                                                          |
| scimark_sor                   | 140 ms                                                 | 90.9 ms: 1.54x faster                                                         |
| richards_super                | 61.0 ms                                                | 42.0 ms: 1.45x faster                                                         |
| unpickle_pure_python          | 198 us                                                 | 138 us: 1.44x faster                                                          |
| chaos                         | 67.7 ms                                                | 47.9 ms: 1.41x faster                                                         |
| pyflate                       | 448 ms                                                 | 318 ms: 1.41x faster                                                          |
| richards                      | 52.3 ms                                                | 37.5 ms: 1.39x faster                                                         |
| k_core                        | 2.01 sec                                               | 1.45 sec: 1.39x faster                                                        |
| mako                          | 9.81 ms                                                | 7.18 ms: 1.37x faster                                                         |
| pylint                        | 231 ms                                                 | 169 ms: 1.36x faster                                                          |
| scimark_monte_carlo           | 72.4 ms                                                | 53.7 ms: 1.35x faster                                                         |
| crypto_pyaes                  | 73.3 ms                                                | 55.6 ms: 1.32x faster                                                         |
| tomli_loads                   | 1.72 sec                                               | 1.31 sec: 1.31x faster                                                        |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 27.4 ms: 1.30x faster                                                         |
| hexiom                        | 6.25 ms                                                | 4.84 ms: 1.29x faster                                                         |
| spectral_norm                 | 95.3 ms                                                | 74.4 ms: 1.28x faster                                                         |
| html5lib                      | 43.5 ms                                                | 34.0 ms: 1.28x faster                                                         |
| pickle_pure_python            | 285 us                                                 | 227 us: 1.25x faster                                                          |
| float                         | 72.4 ms                                                | 58.2 ms: 1.25x faster                                                         |
| deepcopy_reduce               | 2.32 us                                                | 1.90 us: 1.22x faster                                                         |
| regex_dna                     | 175 ms                                                 | 143 ms: 1.22x faster                                                          |
| python_startup                | 19.6 ms                                                | 16.1 ms: 1.22x faster                                                         |
| json_dumps                    | 8.31 ms                                                | 6.82 ms: 1.22x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 84.3 ms: 1.22x faster                                                         |
| regex_compile                 | 95.6 ms                                                | 79.4 ms: 1.20x faster                                                         |
| sphinx                        | 729 ms                                                 | 616 ms: 1.18x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 16.2 ms: 1.18x faster                                                         |
| pycparser                     | 887 ms                                                 | 752 ms: 1.18x faster                                                          |
| nbody                         | 92.5 ms                                                | 78.6 ms: 1.18x faster                                                         |
| xml_etree_process             | 44.6 ms                                                | 37.9 ms: 1.18x faster                                                         |
| sympy_integrate               | 13.2 ms                                                | 11.4 ms: 1.15x faster                                                         |
| docutils                      | 1.74 sec                                               | 1.52 sec: 1.15x faster                                                        |
| logging_format                | 5.03 us                                                | 4.40 us: 1.14x faster                                                         |
| sympy_sum                     | 92.7 ms                                                | 81.2 ms: 1.14x faster                                                         |
| logging_simple                | 4.59 us                                                | 4.10 us: 1.12x faster                                                         |
| scimark_fft                   | 225 ms                                                 | 204 ms: 1.11x faster                                                          |
| bpe_tokeniser                 | 3.44 sec                                               | 3.11 sec: 1.11x faster                                                        |
| python_startup_no_site        | 12.8 ms                                                | 11.9 ms: 1.08x faster                                                         |
| pprint_pformat                | 1.33 sec                                               | 1.24 sec: 1.07x faster                                                        |
| sympy_str                     | 166 ms                                                 | 155 ms: 1.07x faster                                                          |
| coroutines                    | 20.5 ms                                                | 19.2 ms: 1.07x faster                                                         |
| xml_etree_parse               | 109 ms                                                 | 103 ms: 1.07x faster                                                          |
| pprint_safe_repr              | 648 ms                                                 | 614 ms: 1.05x faster                                                          |
| json                          | 3.10 ms                                                | 2.95 ms: 1.05x faster                                                         |
| pathlib                       | 25.7 ms                                                | 24.6 ms: 1.05x faster                                                         |
| connected_components          | 318 ms                                                 | 305 ms: 1.04x faster                                                          |
| xml_etree_generate            | 53.9 ms                                                | 52.0 ms: 1.04x faster                                                         |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                          |
| sympy_expand                  | 269 ms                                                 | 265 ms: 1.02x faster                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 73.7 ms: 1.01x faster                                                         |
| meteor_contest                | 77.8 ms                                                | 77.1 ms: 1.01x faster                                                         |
| genshi_text                   | 17.7 ms                                                | 17.7 ms: 1.00x faster                                                         |
| shortest_path                 | 328 ms                                                 | 332 ms: 1.01x slower                                                          |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                          |
| genshi_xml                    | 35.1 ms                                                | 36.2 ms: 1.03x slower                                                         |
| django_template               | 24.4 ms                                                | 25.4 ms: 1.04x slower                                                         |
| fannkuch                      | 303 ms                                                 | 316 ms: 1.04x slower                                                          |
| many_optionals                | 486 us                                                 | 510 us: 1.05x slower                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.64 ms: 1.06x slower                                                         |
| sqlite_synth                  | 1.48 us                                                | 1.59 us: 1.08x slower                                                         |
| nqueens                       | 63.8 ms                                                | 69.4 ms: 1.09x slower                                                         |
| create_gc_cycles              | 1.16 ms                                                | 1.36 ms: 1.17x slower                                                         |
| gc_traversal                  | 2.71 ms                                                | 3.20 ms: 1.18x slower                                                         |
| async_generators              | 233 ms                                                 | 287 ms: 1.23x slower                                                          |
| telco                         | 3.49 ms                                                | 4.54 ms: 1.30x slower                                                         |
| logging_silent                | 117 ns                                                 | 346 ns: 2.95x slower                                                          |
| coverage                      | 41.2 ms                                                | 341 ms: 8.28x slower                                                          |
| thrift                        | 562 us                                                 | 43.8 ms: 77.94x slower                                                        |
| Geometric mean                | (ref)                                                  | 1.16x faster                                                                  |

Benchmark hidden because not significant (5): 2to3, generators, json_loads, regex_effbot, asyncio_websockets
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250613-3.15.0a0-f603929-JIT/bm-20250613-darwin-arm64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.174x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.19x