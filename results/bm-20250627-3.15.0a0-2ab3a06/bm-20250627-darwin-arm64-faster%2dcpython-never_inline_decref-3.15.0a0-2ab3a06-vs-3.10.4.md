# Results vs. 3.10.4

- fork: faster-cpython
- ref: never_inline_decref
- machine: darwin-arm64
- commit hash: 2ab3a06
- commit date: 2025-06-27
- overall geometric mean: 1.237x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 191 ms: 1.05x faster                                                           |
| docutils       | 1.74 sec                                               | 1.53 sec: 1.13x faster                                                         |
| html5lib       | 43.5 ms                                                | 36.4 ms: 1.20x faster                                                          |
| sphinx         | 729 ms                                                 | 617 ms: 1.18x faster                                                           |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.7 ms: 5.32x faster                                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                           |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                                           |
| async_tree_io                 | 1.02 sec                                               | 412 ms: 2.47x faster                                                           |
| async_tree_memoization        | 481 ms                                                 | 218 ms: 2.20x faster                                                           |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.18x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                           |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                           |
| coroutines                    | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                          |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                                           |
| Geometric mean                | (ref)                                                  | 1.91x faster                                                                   |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 58.2 ms: 1.24x faster                                                          |
| nbody          | 92.5 ms                                                | 85.4 ms: 1.08x faster                                                          |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 139 ms: 1.26x faster                                                           |
| regex_v8       | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                          |
| regex_compile  | 95.6 ms                                                | 81.8 ms: 1.17x faster                                                          |
| regex_effbot   | 2.34 ms                                                | 2.35 ms: 1.00x slower                                                          |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                         |
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                           |
| json_dumps           | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                          |
| unpickle_pure_python | 198 us                                                 | 177 us: 1.12x faster                                                           |
| xml_etree_process    | 44.6 ms                                                | 45.3 ms: 1.02x slower                                                          |
| xml_etree_iterparse  | 74.5 ms                                                | 76.2 ms: 1.02x slower                                                          |
| json_loads           | 16.6 us                                                | 17.1 us: 1.03x slower                                                          |
| xml_etree_generate   | 53.9 ms                                                | 62.1 ms: 1.15x slower                                                          |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                   |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 18.1 ms: 1.09x faster                                                          |
| python_startup_no_site | 12.8 ms                                                | 13.6 ms: 1.06x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 9.21 ms: 1.07x faster                                                          |
| django_template | 24.4 ms                                                | 25.0 ms: 1.02x slower                                                          |
| genshi_text     | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                          |
| genshi_xml      | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                          |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                                   |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 73.7 ms: 5.32x faster                                                          |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.18x faster                                                           |
| typing_runtime_protocols      | 326 us                                                 | 105 us: 3.09x faster                                                           |
| subparsers                    | 39.8 ms                                                | 14.8 ms: 2.69x faster                                                          |
| async_tree_eager_io           | 1.01 sec                                               | 393 ms: 2.58x faster                                                           |
| async_tree_io                 | 1.02 sec                                               | 412 ms: 2.47x faster                                                           |
| async_tree_memoization        | 481 ms                                                 | 218 ms: 2.20x faster                                                           |
| async_tree_none               | 391 ms                                                 | 180 ms: 2.18x faster                                                           |
| mdp                           | 1.65 sec                                               | 848 ms: 1.95x faster                                                           |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 372 ms: 1.80x faster                                                           |
| deltablue                     | 4.99 ms                                                | 2.81 ms: 1.77x faster                                                          |
| raytrace                      | 327 ms                                                 | 206 ms: 1.58x faster                                                           |
| scimark_sor                   | 140 ms                                                 | 90.3 ms: 1.55x faster                                                          |
| go                            | 163 ms                                                 | 106 ms: 1.55x faster                                                           |
| deepcopy_memo                 | 34.7 us                                                | 22.8 us: 1.53x faster                                                          |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 438 ms: 1.53x faster                                                           |
| logging_silent                | 117 ns                                                 | 78.7 ns: 1.49x faster                                                          |
| chaos                         | 67.7 ms                                                | 45.7 ms: 1.48x faster                                                          |
| deepcopy                      | 276 us                                                 | 187 us: 1.48x faster                                                           |
| richards_super                | 61.0 ms                                                | 42.0 ms: 1.45x faster                                                          |
| richards                      | 52.3 ms                                                | 37.3 ms: 1.40x faster                                                          |
| pylint                        | 231 ms                                                 | 168 ms: 1.37x faster                                                           |
| scimark_monte_carlo           | 72.4 ms                                                | 53.0 ms: 1.37x faster                                                          |
| k_core                        | 2.01 sec                                               | 1.48 sec: 1.36x faster                                                         |
| dulwich_log                   | 35.6 ms                                                | 26.6 ms: 1.34x faster                                                          |
| spectral_norm                 | 95.3 ms                                                | 72.7 ms: 1.31x faster                                                          |
| comprehensions                | 17.3 us                                                | 13.2 us: 1.31x faster                                                          |
| regex_dna                     | 175 ms                                                 | 139 ms: 1.26x faster                                                           |
| pyflate                       | 448 ms                                                 | 357 ms: 1.25x faster                                                           |
| float                         | 72.4 ms                                                | 58.2 ms: 1.24x faster                                                          |
| logging_format                | 5.03 us                                                | 4.12 us: 1.22x faster                                                          |
| hexiom                        | 6.25 ms                                                | 5.14 ms: 1.22x faster                                                          |
| deepcopy_reduce               | 2.32 us                                                | 1.92 us: 1.21x faster                                                          |
| regex_v8                      | 19.1 ms                                                | 15.9 ms: 1.21x faster                                                          |
| logging_simple                | 4.59 us                                                | 3.82 us: 1.20x faster                                                          |
| crypto_pyaes                  | 73.3 ms                                                | 60.9 ms: 1.20x faster                                                          |
| thrift                        | 562 us                                                 | 470 us: 1.20x faster                                                           |
| html5lib                      | 43.5 ms                                                | 36.4 ms: 1.20x faster                                                          |
| pycparser                     | 887 ms                                                 | 743 ms: 1.19x faster                                                           |
| tomli_loads                   | 1.72 sec                                               | 1.45 sec: 1.19x faster                                                         |
| scimark_lu                    | 103 ms                                                 | 86.5 ms: 1.19x faster                                                          |
| sphinx                        | 729 ms                                                 | 617 ms: 1.18x faster                                                           |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                           |
| regex_compile                 | 95.6 ms                                                | 81.8 ms: 1.17x faster                                                          |
| json_dumps                    | 8.31 ms                                                | 7.12 ms: 1.17x faster                                                          |
| pprint_pformat                | 1.33 sec                                               | 1.14 sec: 1.16x faster                                                         |
| sympy_integrate               | 13.2 ms                                                | 11.3 ms: 1.16x faster                                                          |
| pprint_safe_repr              | 648 ms                                                 | 561 ms: 1.16x faster                                                           |
| docutils                      | 1.74 sec                                               | 1.53 sec: 1.13x faster                                                         |
| sympy_sum                     | 92.7 ms                                                | 82.1 ms: 1.13x faster                                                          |
| unpickle_pure_python          | 198 us                                                 | 177 us: 1.12x faster                                                           |
| scimark_fft                   | 225 ms                                                 | 202 ms: 1.11x faster                                                           |
| python_startup                | 19.6 ms                                                | 18.1 ms: 1.09x faster                                                          |
| nbody                         | 92.5 ms                                                | 85.4 ms: 1.08x faster                                                          |
| coroutines                    | 20.5 ms                                                | 19.0 ms: 1.08x faster                                                          |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.20 ms: 1.07x faster                                                          |
| mako                          | 9.81 ms                                                | 9.21 ms: 1.07x faster                                                          |
| connected_components          | 318 ms                                                 | 302 ms: 1.06x faster                                                           |
| 2to3                          | 201 ms                                                 | 191 ms: 1.05x faster                                                           |
| sympy_str                     | 166 ms                                                 | 157 ms: 1.05x faster                                                           |
| bpe_tokeniser                 | 3.44 sec                                               | 3.30 sec: 1.04x faster                                                         |
| pathlib                       | 25.7 ms                                                | 24.8 ms: 1.04x faster                                                          |
| json                          | 3.10 ms                                                | 2.99 ms: 1.04x faster                                                          |
| dask                          | 789 ms                                                 | 768 ms: 1.03x faster                                                           |
| sympy_expand                  | 269 ms                                                 | 266 ms: 1.01x faster                                                           |
| meteor_contest                | 77.8 ms                                                | 77.2 ms: 1.01x faster                                                          |
| shortest_path                 | 328 ms                                                 | 329 ms: 1.00x slower                                                           |
| regex_effbot                  | 2.34 ms                                                | 2.35 ms: 1.00x slower                                                          |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                           |
| many_optionals                | 486 us                                                 | 493 us: 1.02x slower                                                           |
| xml_etree_process             | 44.6 ms                                                | 45.3 ms: 1.02x slower                                                          |
| xml_etree_iterparse           | 74.5 ms                                                | 76.2 ms: 1.02x slower                                                          |
| django_template               | 24.4 ms                                                | 25.0 ms: 1.02x slower                                                          |
| json_loads                    | 16.6 us                                                | 17.1 us: 1.03x slower                                                          |
| genshi_text                   | 17.7 ms                                                | 18.8 ms: 1.06x slower                                                          |
| fannkuch                      | 303 ms                                                 | 321 ms: 1.06x slower                                                           |
| python_startup_no_site        | 12.8 ms                                                | 13.6 ms: 1.06x slower                                                          |
| genshi_xml                    | 35.1 ms                                                | 37.5 ms: 1.07x slower                                                          |
| sqlite_synth                  | 1.48 us                                                | 1.62 us: 1.09x slower                                                          |
| xml_etree_generate            | 53.9 ms                                                | 62.1 ms: 1.15x slower                                                          |
| create_gc_cycles              | 1.16 ms                                                | 1.35 ms: 1.16x slower                                                          |
| nqueens                       | 63.8 ms                                                | 74.3 ms: 1.16x slower                                                          |
| gc_traversal                  | 2.71 ms                                                | 3.19 ms: 1.18x slower                                                          |
| async_generators              | 233 ms                                                 | 285 ms: 1.22x slower                                                           |
| coverage                      | 41.2 ms                                                | 53.2 ms: 1.29x slower                                                          |
| telco                         | 3.49 ms                                                | 5.04 ms: 1.44x slower                                                          |
| Geometric mean                | (ref)                                                  | 1.24x faster                                                                   |

Benchmark hidden because not significant (3): generators, asyncio_websockets, xml_etree_parse
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: bench_mp_pool, bench_thread_pool, chameleon, djangocms, gevent_hub, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (12) of results/bm-20250627-3.15.0a0-2ab3a06/bm-20250627-darwin-arm64-faster%2dcpython-never_inline_decref-3.15.0a0-2ab3a06.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.237x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.12x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.17x