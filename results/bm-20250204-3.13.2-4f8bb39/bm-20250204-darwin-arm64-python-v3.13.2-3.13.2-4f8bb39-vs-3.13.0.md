# Results vs. 3.13.0

- fork: python
- ref: v3.13.2
- machine: darwin-arm64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.016x slower
- HPT reliability: 98.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 179 ms                                                 | 180 ms: 1.01x slower                                   |
| docutils       | 1.44 sec                                               | 1.44 sec: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (4): chameleon, html5lib, sphinx, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| async_generators                 | 294 ms                                                 | 262 ms: 1.12x faster                                   |
| async_tree_memoization_tg        | 288 ms                                                 | 278 ms: 1.03x faster                                   |
| coroutines                       | 20.0 ms                                                | 19.8 ms: 1.01x faster                                  |
| async_tree_none_tg               | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 462 ms: 1.01x slower                                   |
| async_tree_eager                 | 69.9 ms                                                | 70.6 ms: 1.01x slower                                  |
| async_tree_io_tg                 | 500 ms                                                 | 516 ms: 1.03x slower                                   |
| async_tree_eager_io_tg           | 479 ms                                                 | 510 ms: 1.07x slower                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 211 ms: 1.53x slower                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 159 ms: 3.35x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.10x slower                                           |

Benchmark hidden because not significant (7): asyncio_websockets, async_tree_eager_cpu_io_mixed, async_tree_io, async_tree_none, async_tree_eager_io, async_tree_eager_memoization, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 73.6 ms                                                | 74.4 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.28 ms: 1.15x faster                                  |
| regex_dna      | 149 ms                                                 | 141 ms: 1.06x faster                                   |
| regex_compile  | 78.3 ms                                                | 78.9 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| unpickle_pure_python | 165 us                                                 | 164 us: 1.01x faster                                   |
| xml_etree_generate   | 57.1 ms                                                | 56.8 ms: 1.01x faster                                  |
| xml_etree_process    | 41.3 ms                                                | 41.5 ms: 1.00x slower                                  |
| json_dumps           | 6.47 ms                                                | 6.50 ms: 1.00x slower                                  |
| pickle_pure_python   | 215 us                                                 | 216 us: 1.00x slower                                   |
| Geometric mean       | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (3): xml_etree_iterparse, json_loads, tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 18.8 ms                                                | 18.4 ms: 1.02x faster                                  |
| python_startup_no_site | 13.7 ms                                                | 13.4 ms: 1.02x faster                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 7.75 ms                                                | 7.72 ms: 1.00x faster                                  |
| genshi_text     | 16.9 ms                                                | 16.9 ms: 1.00x faster                                  |
| django_template | 20.5 ms                                                | 20.6 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.00x faster                                           |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20250204-darwin-arm64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot                     | 2.63 ms                                                | 2.28 ms: 1.15x faster                                  |
| async_generators                 | 294 ms                                                 | 262 ms: 1.12x faster                                   |
| regex_dna                        | 149 ms                                                 | 141 ms: 1.06x faster                                   |
| bench_mp_pool                    | 64.7 ms                                                | 61.5 ms: 1.05x faster                                  |
| async_tree_memoization_tg        | 288 ms                                                 | 278 ms: 1.03x faster                                   |
| richards                         | 36.2 ms                                                | 35.3 ms: 1.02x faster                                  |
| python_startup                   | 18.8 ms                                                | 18.4 ms: 1.02x faster                                  |
| python_startup_no_site           | 13.7 ms                                                | 13.4 ms: 1.02x faster                                  |
| json                             | 3.04 ms                                                | 2.98 ms: 1.02x faster                                  |
| crypto_pyaes                     | 55.3 ms                                                | 54.4 ms: 1.02x faster                                  |
| pprint_pformat                   | 1.10 sec                                               | 1.08 sec: 1.02x faster                                 |
| generators                       | 31.9 ms                                                | 31.5 ms: 1.01x faster                                  |
| go                               | 117 ms                                                 | 115 ms: 1.01x faster                                   |
| coroutines                       | 20.0 ms                                                | 19.8 ms: 1.01x faster                                  |
| xml_etree_parse                  | 108 ms                                                 | 106 ms: 1.01x faster                                   |
| async_tree_none_tg               | 198 ms                                                 | 196 ms: 1.01x faster                                   |
| pprint_safe_repr                 | 541 ms                                                 | 535 ms: 1.01x faster                                   |
| deepcopy_reduce                  | 2.09 us                                                | 2.07 us: 1.01x faster                                  |
| sqlite_synth                     | 1.55 us                                                | 1.54 us: 1.01x faster                                  |
| logging_silent                   | 71.0 ns                                                | 70.3 ns: 1.01x faster                                  |
| sqlglot_transpile                | 1.04 ms                                                | 1.03 ms: 1.01x faster                                  |
| unpickle_pure_python             | 165 us                                                 | 164 us: 1.01x faster                                   |
| telco                            | 4.84 ms                                                | 4.81 ms: 1.01x faster                                  |
| docutils                         | 1.44 sec                                               | 1.44 sec: 1.01x faster                                 |
| deepcopy                         | 236 us                                                 | 235 us: 1.01x faster                                   |
| xml_etree_generate               | 57.1 ms                                                | 56.8 ms: 1.01x faster                                  |
| nqueens                          | 61.8 ms                                                | 61.5 ms: 1.01x faster                                  |
| mako                             | 7.75 ms                                                | 7.72 ms: 1.00x faster                                  |
| pycparser                        | 701 ms                                                 | 698 ms: 1.00x faster                                   |
| genshi_text                      | 16.9 ms                                                | 16.9 ms: 1.00x faster                                  |
| scimark_sor                      | 106 ms                                                 | 106 ms: 1.00x slower                                   |
| shortest_path                    | 345 ms                                                 | 347 ms: 1.00x slower                                   |
| fannkuch                         | 279 ms                                                 | 280 ms: 1.00x slower                                   |
| xml_etree_process                | 41.3 ms                                                | 41.5 ms: 1.00x slower                                  |
| json_dumps                       | 6.47 ms                                                | 6.50 ms: 1.00x slower                                  |
| mdp                              | 1.50 sec                                               | 1.51 sec: 1.00x slower                                 |
| spectral_norm                    | 76.5 ms                                                | 76.8 ms: 1.00x slower                                  |
| pickle_pure_python               | 215 us                                                 | 216 us: 1.00x slower                                   |
| deltablue                        | 2.65 ms                                                | 2.66 ms: 1.01x slower                                  |
| async_tree_cpu_io_mixed          | 459 ms                                                 | 462 ms: 1.01x slower                                   |
| create_gc_cycles                 | 1.19 ms                                                | 1.20 ms: 1.01x slower                                  |
| regex_compile                    | 78.3 ms                                                | 78.9 ms: 1.01x slower                                  |
| many_optionals                   | 409 us                                                 | 412 us: 1.01x slower                                   |
| django_template                  | 20.5 ms                                                | 20.6 ms: 1.01x slower                                  |
| 2to3                             | 179 ms                                                 | 180 ms: 1.01x slower                                   |
| scimark_monte_carlo              | 50.4 ms                                                | 50.8 ms: 1.01x slower                                  |
| dulwich_log                      | 28.7 ms                                                | 29.0 ms: 1.01x slower                                  |
| sqlglot_optimize                 | 34.7 ms                                                | 35.0 ms: 1.01x slower                                  |
| async_tree_eager                 | 69.9 ms                                                | 70.6 ms: 1.01x slower                                  |
| sympy_sum                        | 75.1 ms                                                | 75.8 ms: 1.01x slower                                  |
| scimark_lu                       | 75.9 ms                                                | 76.7 ms: 1.01x slower                                  |
| scimark_sparse_mat_mult          | 2.98 ms                                                | 3.02 ms: 1.01x slower                                  |
| nbody                            | 73.6 ms                                                | 74.4 ms: 1.01x slower                                  |
| scimark_fft                      | 200 ms                                                 | 202 ms: 1.01x slower                                   |
| logging_format                   | 3.85 us                                                | 3.91 us: 1.01x slower                                  |
| sqlglot_normalize                | 188 ms                                                 | 191 ms: 1.02x slower                                   |
| logging_simple                   | 3.56 us                                                | 3.62 us: 1.02x slower                                  |
| raytrace                         | 181 ms                                                 | 185 ms: 1.02x slower                                   |
| comprehensions                   | 12.0 us                                                | 12.3 us: 1.03x slower                                  |
| async_tree_io_tg                 | 500 ms                                                 | 516 ms: 1.03x slower                                   |
| chaos                            | 41.1 ms                                                | 42.5 ms: 1.03x slower                                  |
| async_tree_eager_io_tg           | 479 ms                                                 | 510 ms: 1.07x slower                                   |
| async_tree_cpu_io_mixed_tg       | 448 ms                                                 | 479 ms: 1.07x slower                                   |
| async_tree_eager_cpu_io_mixed_tg | 347 ms                                                 | 425 ms: 1.22x slower                                   |
| async_tree_eager_memoization_tg  | 138 ms                                                 | 211 ms: 1.53x slower                                   |
| async_tree_eager_tg              | 47.4 ms                                                | 159 ms: 3.35x slower                                   |
| Geometric mean                   | (ref)                                                  | 1.01x slower                                           |

Benchmark hidden because not significant (44): tornado_http, gunicorn, djangocms, html5lib, sphinx, gc_traversal, sqlalchemy_imperative, thrift, regex_v8, sympy_expand, sqlalchemy_declarative, coverage, xml_etree_iterparse, sqlglot_parse, meteor_contest, richards_super, chameleon, asyncio_websockets, sympy_integrate, pidigits, json_loads, genshi_xml, hexiom, dask, bpe_tokeniser, tomli_loads, pyflate, bench_thread_pool, float, deepcopy_memo, connected_components, gevent_hub, sympy_str, k_core, subparsers, async_tree_eager_cpu_io_mixed, pylint, typing_runtime_protocols, pathlib, async_tree_io, async_tree_none, async_tree_eager_io, async_tree_eager_memoization, async_tree_memoization

- Geometric mean (including insignificant results): 1.016x slower

# HPT report

- Reliability score: 98.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.09x