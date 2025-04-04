# Results vs. 3.10.4

- fork: faster-cpython
- ref: tos_caching_1
- machine: darwin-arm64
- commit hash: 492df4e
- commit date: 2025-04-04
- overall geometric mean: 1.218x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 186 ms: 1.08x faster                                                      |
| docutils       | 1.74 sec                                               | 1.56 sec: 1.11x faster                                                    |
| html5lib       | 43.5 ms                                                | 35.4 ms: 1.23x faster                                                     |
| sphinx         | 729 ms                                                 | 634 ms: 1.15x faster                                                      |
| Geometric mean | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.3 ms: 5.20x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                      |
| async_tree_eager_io           | 1.01 sec                                               | 413 ms: 2.45x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 430 ms: 2.37x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                      |
| async_tree_none               | 391 ms                                                 | 187 ms: 2.10x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                      |
| coroutines                    | 20.5 ms                                                | 19.6 ms: 1.05x faster                                                     |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                      |
| Geometric mean                | (ref)                                                  | 1.89x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 72.4 ms                                                | 55.7 ms: 1.30x faster                                                     |
| nbody          | 92.5 ms                                                | 85.9 ms: 1.08x faster                                                     |
| pidigits       | 280 ms                                                 | 284 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.11x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 175 ms                                                 | 140 ms: 1.25x faster                                                      |
| regex_v8       | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                     |
| regex_compile  | 95.6 ms                                                | 85.0 ms: 1.12x faster                                                     |
| regex_effbot   | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.15x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 285 us                                                 | 241 us: 1.18x faster                                                      |
| tomli_loads          | 1.72 sec                                               | 1.57 sec: 1.09x faster                                                    |
| unpickle_pure_python | 198 us                                                 | 184 us: 1.08x faster                                                      |
| json_dumps           | 8.31 ms                                                | 7.70 ms: 1.08x faster                                                     |
| xml_etree_parse      | 109 ms                                                 | 105 ms: 1.04x faster                                                      |
| xml_etree_process    | 44.6 ms                                                | 45.2 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 74.5 ms                                                | 77.7 ms: 1.04x slower                                                     |
| json_loads           | 16.6 us                                                | 17.8 us: 1.08x slower                                                     |
| xml_etree_generate   | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                     |
| python_startup_no_site | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 9.81 ms                                                | 8.23 ms: 1.19x faster                                                     |
| django_template | 24.4 ms                                                | 24.7 ms: 1.01x slower                                                     |
| genshi_text     | 17.7 ms                                                | 18.0 ms: 1.02x slower                                                     |
| genshi_xml      | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                              |

All benchmarks:
===============

| Benchmark                     | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e |
|-------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_eager              | 392 ms                                                 | 75.3 ms: 5.20x faster                                                     |
| async_tree_eager_memoization  | 483 ms                                                 | 152 ms: 3.17x faster                                                      |
| typing_runtime_protocols      | 326 us                                                 | 111 us: 2.93x faster                                                      |
| subparsers                    | 39.8 ms                                                | 13.6 ms: 2.92x faster                                                     |
| async_tree_eager_io           | 1.01 sec                                               | 413 ms: 2.45x faster                                                      |
| async_tree_io                 | 1.02 sec                                               | 430 ms: 2.37x faster                                                      |
| async_tree_memoization        | 481 ms                                                 | 222 ms: 2.17x faster                                                      |
| async_tree_none               | 391 ms                                                 | 187 ms: 2.10x faster                                                      |
| mdp                           | 1.65 sec                                               | 896 ms: 1.84x faster                                                      |
| async_tree_eager_cpu_io_mixed | 669 ms                                                 | 370 ms: 1.81x faster                                                      |
| deltablue                     | 4.99 ms                                                | 2.91 ms: 1.72x faster                                                     |
| raytrace                      | 327 ms                                                 | 204 ms: 1.61x faster                                                      |
| logging_silent                | 117 ns                                                 | 74.8 ns: 1.57x faster                                                     |
| go                            | 163 ms                                                 | 106 ms: 1.54x faster                                                      |
| async_tree_cpu_io_mixed       | 668 ms                                                 | 434 ms: 1.54x faster                                                      |
| deepcopy                      | 276 us                                                 | 181 us: 1.53x faster                                                      |
| scimark_sor                   | 140 ms                                                 | 97.7 ms: 1.43x faster                                                     |
| deepcopy_memo                 | 34.7 us                                                | 24.4 us: 1.42x faster                                                     |
| richards_super                | 61.0 ms                                                | 44.7 ms: 1.36x faster                                                     |
| chaos                         | 67.7 ms                                                | 49.8 ms: 1.36x faster                                                     |
| pylint                        | 231 ms                                                 | 177 ms: 1.31x faster                                                      |
| dulwich_log                   | 35.6 ms                                                | 27.3 ms: 1.30x faster                                                     |
| float                         | 72.4 ms                                                | 55.7 ms: 1.30x faster                                                     |
| richards                      | 52.3 ms                                                | 40.5 ms: 1.29x faster                                                     |
| scimark_monte_carlo           | 72.4 ms                                                | 57.3 ms: 1.26x faster                                                     |
| pyflate                       | 448 ms                                                 | 356 ms: 1.26x faster                                                      |
| generators                    | 31.7 ms                                                | 25.4 ms: 1.25x faster                                                     |
| k_core                        | 2.01 sec                                               | 1.61 sec: 1.25x faster                                                    |
| regex_dna                     | 175 ms                                                 | 140 ms: 1.25x faster                                                      |
| deepcopy_reduce               | 2.32 us                                                | 1.88 us: 1.24x faster                                                     |
| html5lib                      | 43.5 ms                                                | 35.4 ms: 1.23x faster                                                     |
| regex_v8                      | 19.1 ms                                                | 15.7 ms: 1.22x faster                                                     |
| crypto_pyaes                  | 73.3 ms                                                | 61.3 ms: 1.20x faster                                                     |
| mako                          | 9.81 ms                                                | 8.23 ms: 1.19x faster                                                     |
| pickle_pure_python            | 285 us                                                 | 241 us: 1.18x faster                                                      |
| comprehensions                | 17.3 us                                                | 14.7 us: 1.18x faster                                                     |
| pycparser                     | 887 ms                                                 | 755 ms: 1.17x faster                                                      |
| sqlalchemy_imperative         | 9.07 ms                                                | 7.77 ms: 1.17x faster                                                     |
| logging_format                | 5.03 us                                                | 4.36 us: 1.15x faster                                                     |
| sphinx                        | 729 ms                                                 | 634 ms: 1.15x faster                                                      |
| scimark_lu                    | 103 ms                                                 | 89.5 ms: 1.15x faster                                                     |
| sqlalchemy_declarative        | 75.7 ms                                                | 66.1 ms: 1.15x faster                                                     |
| logging_simple                | 4.59 us                                                | 4.03 us: 1.14x faster                                                     |
| spectral_norm                 | 95.3 ms                                                | 84.6 ms: 1.13x faster                                                     |
| regex_compile                 | 95.6 ms                                                | 85.0 ms: 1.12x faster                                                     |
| pprint_pformat                | 1.33 sec                                               | 1.19 sec: 1.12x faster                                                    |
| hexiom                        | 6.25 ms                                                | 5.60 ms: 1.11x faster                                                     |
| docutils                      | 1.74 sec                                               | 1.56 sec: 1.11x faster                                                    |
| pprint_safe_repr              | 648 ms                                                 | 587 ms: 1.10x faster                                                      |
| sympy_sum                     | 92.7 ms                                                | 84.2 ms: 1.10x faster                                                     |
| tomli_loads                   | 1.72 sec                                               | 1.57 sec: 1.09x faster                                                    |
| sympy_integrate               | 13.2 ms                                                | 12.1 ms: 1.09x faster                                                     |
| 2to3                          | 201 ms                                                 | 186 ms: 1.08x faster                                                      |
| unpickle_pure_python          | 198 us                                                 | 184 us: 1.08x faster                                                      |
| json_dumps                    | 8.31 ms                                                | 7.70 ms: 1.08x faster                                                     |
| nbody                         | 92.5 ms                                                | 85.9 ms: 1.08x faster                                                     |
| pathlib                       | 25.7 ms                                                | 24.5 ms: 1.05x faster                                                     |
| bpe_tokeniser                 | 3.44 sec                                               | 3.27 sec: 1.05x faster                                                    |
| coroutines                    | 20.5 ms                                                | 19.6 ms: 1.05x faster                                                     |
| scimark_fft                   | 225 ms                                                 | 216 ms: 1.04x faster                                                      |
| xml_etree_parse               | 109 ms                                                 | 105 ms: 1.04x faster                                                      |
| regex_effbot                  | 2.34 ms                                                | 2.24 ms: 1.04x faster                                                     |
| sympy_str                     | 166 ms                                                 | 162 ms: 1.03x faster                                                      |
| python_startup                | 19.6 ms                                                | 19.4 ms: 1.01x faster                                                     |
| json                          | 3.10 ms                                                | 3.07 ms: 1.01x faster                                                     |
| bench_thread_pool             | 545 us                                                 | 540 us: 1.01x faster                                                      |
| meteor_contest                | 77.8 ms                                                | 78.0 ms: 1.00x slower                                                     |
| sympy_expand                  | 269 ms                                                 | 271 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult       | 3.42 ms                                                | 3.45 ms: 1.01x slower                                                     |
| pidigits                      | 280 ms                                                 | 284 ms: 1.01x slower                                                      |
| xml_etree_process             | 44.6 ms                                                | 45.2 ms: 1.01x slower                                                     |
| django_template               | 24.4 ms                                                | 24.7 ms: 1.01x slower                                                     |
| genshi_text                   | 17.7 ms                                                | 18.0 ms: 1.02x slower                                                     |
| genshi_xml                    | 35.1 ms                                                | 36.1 ms: 1.03x slower                                                     |
| fannkuch                      | 303 ms                                                 | 312 ms: 1.03x slower                                                      |
| xml_etree_iterparse           | 74.5 ms                                                | 77.7 ms: 1.04x slower                                                     |
| sqlite_synth                  | 1.48 us                                                | 1.56 us: 1.06x slower                                                     |
| connected_components          | 318 ms                                                 | 339 ms: 1.07x slower                                                      |
| json_loads                    | 16.6 us                                                | 17.8 us: 1.08x slower                                                     |
| create_gc_cycles              | 1.16 ms                                                | 1.28 ms: 1.10x slower                                                     |
| bench_mp_pool                 | 56.0 ms                                                | 61.7 ms: 1.10x slower                                                     |
| shortest_path                 | 328 ms                                                 | 363 ms: 1.11x slower                                                      |
| nqueens                       | 63.8 ms                                                | 72.5 ms: 1.14x slower                                                     |
| xml_etree_generate            | 53.9 ms                                                | 61.4 ms: 1.14x slower                                                     |
| gc_traversal                  | 2.71 ms                                                | 3.11 ms: 1.15x slower                                                     |
| async_generators              | 233 ms                                                 | 270 ms: 1.16x slower                                                      |
| python_startup_no_site        | 12.8 ms                                                | 14.9 ms: 1.16x slower                                                     |
| coverage                      | 41.2 ms                                                | 48.3 ms: 1.17x slower                                                     |
| telco                         | 3.49 ms                                                | 4.77 ms: 1.37x slower                                                     |
| Geometric mean                | (ref)                                                  | 1.22x faster                                                              |

Benchmark hidden because not significant (2): asyncio_websockets, many_optionals
Ignored benchmarks (10) of results/bm-20220323-3.10.4-9d38120/bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120.json: chameleon, dask, djangocms, gevent_hub, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (12) of results/bm-20250404-3.14.0a6+-492df4e/bm-20250404-darwin-arm64-faster%2dcpython-tos_caching_1-3.14.0a6+-492df4e.json: async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io_tg, async_tree_eager_memoization_tg, async_tree_eager_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile

- Geometric mean (including insignificant results): 1.218x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.14x