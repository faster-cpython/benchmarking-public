# Results vs. 3.13.0

- fork: faster-cpython
- ref: more_robust_immortal
- machine: darwin-arm64
- commit hash: 94f8fd0
- commit date: 2024-10-10
- overall geometric mean: 1.095x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 0.63x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 160 ms: 1.17x faster                                                            |
| docutils       | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                          |
| html5lib       | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                    |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                                            |
| async_tree_eager                 | 70.1 ms                                                | 59.7 ms: 1.17x faster                                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                                           |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                            |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.07x faster                                                            |
| async_generators                 | 295 ms                                                 | 276 ms: 1.07x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                            |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                            |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                            |
| async_tree_io_tg                 | 497 ms                                                 | 562 ms: 1.13x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.01x faster                                                                    |

Benchmark hidden because not significant (3): async_tree_none_tg, async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                           |
| nbody          | 74.0 ms                                                | 65.4 ms: 1.13x faster                                                           |
| pidigits       | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                           |
| regex_v8       | 17.0 ms                                                | 16.7 ms: 1.01x faster                                                           |
| regex_dna      | 149 ms                                                 | 148 ms: 1.01x faster                                                            |
| regex_effbot   | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                           |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pickle_pure_python   | 214 us                                                 | 184 us: 1.17x faster                                                            |
| unpickle_pure_python | 164 us                                                 | 142 us: 1.16x faster                                                            |
| xml_etree_process    | 41.0 ms                                                | 37.4 ms: 1.09x faster                                                           |
| xml_etree_generate   | 57.0 ms                                                | 52.1 ms: 1.09x faster                                                           |
| tomli_loads          | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| json_dumps           | 6.52 ms                                                | 6.22 ms: 1.05x faster                                                           |
| json_loads           | 17.0 us                                                | 16.7 us: 1.01x faster                                                           |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup | 18.9 ms                                                | 17.0 ms: 1.11x faster                                                           |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_text     | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| genshi_xml      | 34.4 ms                                                | 29.8 ms: 1.15x faster                                                           |
| django_template | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                           |
| mako            | 7.68 ms                                                | 6.97 ms: 1.10x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.15x faster                                                                    |

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0 |
|----------------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| deepcopy                         | 237 us                                                 | 147 us: 1.61x faster                                                            |
| deepcopy_memo                    | 27.4 us                                                | 17.1 us: 1.60x faster                                                           |
| generators                       | 31.5 ms                                                | 20.3 ms: 1.55x faster                                                           |
| go                               | 115 ms                                                 | 81.6 ms: 1.41x faster                                                           |
| deepcopy_reduce                  | 2.07 us                                                | 1.52 us: 1.36x faster                                                           |
| create_gc_cycles                 | 1.17 ms                                                | 918 us: 1.27x faster                                                            |
| bench_mp_pool                    | 62.5 ms                                                | 49.3 ms: 1.27x faster                                                           |
| genshi_text                      | 16.9 ms                                                | 13.7 ms: 1.23x faster                                                           |
| deltablue                        | 2.68 ms                                                | 2.23 ms: 1.20x faster                                                           |
| coroutines                       | 19.8 ms                                                | 16.6 ms: 1.19x faster                                                           |
| raytrace                         | 181 ms                                                 | 153 ms: 1.18x faster                                                            |
| logging_simple                   | 3.60 us                                                | 3.05 us: 1.18x faster                                                           |
| async_tree_memoization_tg        | 288 ms                                                 | 245 ms: 1.18x faster                                                            |
| hexiom                           | 4.86 ms                                                | 4.14 ms: 1.17x faster                                                           |
| 2to3                             | 187 ms                                                 | 160 ms: 1.17x faster                                                            |
| async_tree_eager                 | 70.1 ms                                                | 59.7 ms: 1.17x faster                                                           |
| gc_traversal                     | 2.91 ms                                                | 2.49 ms: 1.17x faster                                                           |
| pickle_pure_python               | 214 us                                                 | 184 us: 1.17x faster                                                            |
| pprint_safe_repr                 | 533 ms                                                 | 457 ms: 1.17x faster                                                            |
| logging_format                   | 3.89 us                                                | 3.34 us: 1.17x faster                                                           |
| sqlglot_parse                    | 856 us                                                 | 737 us: 1.16x faster                                                            |
| regex_compile                    | 78.6 ms                                                | 67.8 ms: 1.16x faster                                                           |
| logging_silent                   | 70.1 ns                                                | 60.5 ns: 1.16x faster                                                           |
| unpickle_pure_python             | 164 us                                                 | 142 us: 1.16x faster                                                            |
| genshi_xml                       | 34.4 ms                                                | 29.8 ms: 1.15x faster                                                           |
| pprint_pformat                   | 1.08 sec                                               | 940 ms: 1.15x faster                                                            |
| nqueens                          | 62.5 ms                                                | 54.4 ms: 1.15x faster                                                           |
| async_tree_eager_tg              | 47.8 ms                                                | 41.7 ms: 1.15x faster                                                           |
| float                            | 56.0 ms                                                | 48.9 ms: 1.15x faster                                                           |
| scimark_lu                       | 76.7 ms                                                | 66.9 ms: 1.15x faster                                                           |
| html5lib                         | 36.6 ms                                                | 32.0 ms: 1.14x faster                                                           |
| sqlglot_transpile                | 1.02 ms                                                | 896 us: 1.14x faster                                                            |
| richards_super                   | 39.1 ms                                                | 34.4 ms: 1.14x faster                                                           |
| sqlglot_normalize                | 189 ms                                                 | 166 ms: 1.14x faster                                                            |
| scimark_monte_carlo              | 50.4 ms                                                | 44.4 ms: 1.13x faster                                                           |
| chaos                            | 41.2 ms                                                | 36.3 ms: 1.13x faster                                                           |
| nbody                            | 74.0 ms                                                | 65.4 ms: 1.13x faster                                                           |
| richards                         | 35.2 ms                                                | 31.2 ms: 1.13x faster                                                           |
| sqlglot_optimize                 | 34.9 ms                                                | 30.9 ms: 1.13x faster                                                           |
| thrift                           | 466 us                                                 | 416 us: 1.12x faster                                                            |
| async_tree_none                  | 215 ms                                                 | 192 ms: 1.12x faster                                                            |
| django_template                  | 22.2 ms                                                | 19.9 ms: 1.12x faster                                                           |
| comprehensions                   | 12.3 us                                                | 11.0 us: 1.11x faster                                                           |
| python_startup                   | 18.9 ms                                                | 17.0 ms: 1.11x faster                                                           |
| bench_thread_pool                | 505 us                                                 | 455 us: 1.11x faster                                                            |
| scimark_sor                      | 105 ms                                                 | 95.1 ms: 1.11x faster                                                           |
| pycparser                        | 705 ms                                                 | 639 ms: 1.10x faster                                                            |
| mako                             | 7.68 ms                                                | 6.97 ms: 1.10x faster                                                           |
| xml_etree_process                | 41.0 ms                                                | 37.4 ms: 1.09x faster                                                           |
| xml_etree_generate               | 57.0 ms                                                | 52.1 ms: 1.09x faster                                                           |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 126 ms: 1.09x faster                                                            |
| sympy_expand                     | 246 ms                                                 | 226 ms: 1.09x faster                                                            |
| sympy_str                        | 145 ms                                                 | 134 ms: 1.09x faster                                                            |
| typing_runtime_protocols         | 101 us                                                 | 93.1 us: 1.09x faster                                                           |
| spectral_norm                    | 76.3 ms                                                | 70.2 ms: 1.09x faster                                                           |
| sympy_sum                        | 75.4 ms                                                | 69.7 ms: 1.08x faster                                                           |
| fannkuch                         | 284 ms                                                 | 262 ms: 1.08x faster                                                            |
| pyflate                          | 351 ms                                                 | 326 ms: 1.08x faster                                                            |
| async_tree_eager_memoization     | 168 ms                                                 | 158 ms: 1.07x faster                                                            |
| async_generators                 | 295 ms                                                 | 276 ms: 1.07x faster                                                            |
| async_tree_memoization           | 268 ms                                                 | 251 ms: 1.07x faster                                                            |
| pathlib                          | 23.4 ms                                                | 21.9 ms: 1.07x faster                                                           |
| crypto_pyaes                     | 54.2 ms                                                | 51.2 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.82 ms: 1.06x faster                                                           |
| json                             | 3.03 ms                                                | 2.87 ms: 1.06x faster                                                           |
| bpe_tokeniser                    | 3.25 sec                                               | 3.07 sec: 1.06x faster                                                          |
| scimark_fft                      | 201 ms                                                 | 191 ms: 1.05x faster                                                            |
| tomli_loads                      | 1.57 sec                                               | 1.49 sec: 1.05x faster                                                          |
| json_dumps                       | 6.52 ms                                                | 6.22 ms: 1.05x faster                                                           |
| meteor_contest                   | 74.0 ms                                                | 70.5 ms: 1.05x faster                                                           |
| coverage                         | 46.0 ms                                                | 43.9 ms: 1.05x faster                                                           |
| dulwich_log                      | 28.5 ms                                                | 27.4 ms: 1.04x faster                                                           |
| sympy_integrate                  | 11.3 ms                                                | 10.9 ms: 1.03x faster                                                           |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 336 ms: 1.03x faster                                                            |
| async_tree_eager_cpu_io_mixed    | 373 ms                                                 | 361 ms: 1.03x faster                                                            |
| docutils                         | 1.44 sec                                               | 1.40 sec: 1.03x faster                                                          |
| telco                            | 4.76 ms                                                | 4.64 ms: 1.03x faster                                                           |
| mdp                              | 1.49 sec                                               | 1.46 sec: 1.03x faster                                                          |
| json_loads                       | 17.0 us                                                | 16.7 us: 1.01x faster                                                           |
| regex_v8                         | 17.0 ms                                                | 16.7 ms: 1.01x faster                                                           |
| regex_dna                        | 149 ms                                                 | 148 ms: 1.01x faster                                                            |
| pidigits                         | 284 ms                                                 | 283 ms: 1.00x faster                                                            |
| regex_effbot                     | 2.63 ms                                                | 2.63 ms: 1.00x slower                                                           |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 458 ms: 1.02x slower                                                            |
| async_tree_io_tg                 | 497 ms                                                 | 562 ms: 1.13x slower                                                            |
| async_tree_io                    | 507 ms                                                 | 593 ms: 1.17x slower                                                            |
| async_tree_eager_io              | 514 ms                                                 | 675 ms: 1.31x slower                                                            |
| async_tree_eager_io_tg           | 477 ms                                                 | 712 ms: 1.49x slower                                                            |
| Geometric mean                   | (ref)                                                  | 1.10x faster                                                                    |

Benchmark hidden because not significant (8): python_startup_no_site, async_tree_none_tg, pylint, xml_etree_iterparse, async_tree_cpu_io_mixed, tornado_http, asyncio_websockets, xml_etree_parse
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dask, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241010-3.14.0a0-94f8fd0/bm-20241010-darwin-arm64-faster%2dcpython-more_robust_immortal-3.14.0a0-94f8fd0.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.095x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 0.63x