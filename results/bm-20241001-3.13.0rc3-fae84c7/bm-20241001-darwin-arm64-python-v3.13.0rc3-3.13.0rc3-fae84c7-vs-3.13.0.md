# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: darwin-arm64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.025x faster
- HPT reliability: 60.25%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 187 ms                                                 | 178 ms: 1.06x faster                                         |
| chameleon      | 5.08 ms                                                | 5.10 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                     | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none               | 215 ms                                                 | 213 ms: 1.01x faster                                         |
| coroutines                    | 19.8 ms                                                | 19.8 ms: 1.00x slower                                        |
| async_tree_eager_tg           | 47.8 ms                                                | 48.0 ms: 1.00x slower                                        |
| async_tree_eager_cpu_io_mixed | 373 ms                                                 | 375 ms: 1.01x slower                                         |
| async_tree_memoization_tg     | 288 ms                                                 | 290 ms: 1.01x slower                                         |
| async_tree_eager              | 70.1 ms                                                | 70.7 ms: 1.01x slower                                        |
| Geometric mean                | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (13): async_tree_eager_cpu_io_mixed_tg, async_tree_eager_memoization_tg, asyncio_websockets, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_io, async_generators, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 74.0 ms                                                | 74.2 ms: 1.00x slower                                        |
| float          | 56.0 ms                                                | 56.3 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 17.0 ms                                                | 17.0 ms: 1.00x faster                                        |
| regex_effbot   | 2.63 ms                                                | 2.65 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): regex_dna, regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_loads           | 17.0 us                                                | 16.8 us: 1.01x faster                                        |
| pickle_pure_python   | 214 us                                                 | 213 us: 1.01x faster                                         |
| unpickle_pure_python | 164 us                                                 | 163 us: 1.00x faster                                         |
| json_dumps           | 6.52 ms                                                | 6.51 ms: 1.00x faster                                        |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (5): xml_etree_generate, tomli_loads, xml_etree_process, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 18.9 ms                                                | 17.1 ms: 1.11x faster                                        |
| python_startup_no_site | 14.5 ms                                                | 13.7 ms: 1.06x faster                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 34.2 ms: 1.00x faster                                        |
| django_template | 22.2 ms                                                | 22.2 ms: 1.00x faster                                        |
| genshi_text     | 16.9 ms                                                | 16.8 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                     | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| dask                          | 790 ms                                                 | 256 ms: 3.09x faster                                         |
| create_gc_cycles              | 1.17 ms                                                | 807 us: 1.45x faster                                         |
| mypy2                         | 701 ms                                                 | 495 ms: 1.42x faster                                         |
| bench_mp_pool                 | 62.5 ms                                                | 51.1 ms: 1.22x faster                                        |
| gc_traversal                  | 2.91 ms                                                | 2.48 ms: 1.17x faster                                        |
| python_startup                | 18.9 ms                                                | 17.1 ms: 1.11x faster                                        |
| python_startup_no_site        | 14.5 ms                                                | 13.7 ms: 1.06x faster                                        |
| 2to3                          | 187 ms                                                 | 178 ms: 1.06x faster                                         |
| comprehensions                | 12.3 us                                                | 11.9 us: 1.03x faster                                        |
| json                          | 3.03 ms                                                | 2.94 ms: 1.03x faster                                        |
| deepcopy                      | 237 us                                                 | 232 us: 1.02x faster                                         |
| pathlib                       | 23.4 ms                                                | 23.0 ms: 1.02x faster                                        |
| fannkuch                      | 284 ms                                                 | 280 ms: 1.01x faster                                         |
| async_tree_none               | 215 ms                                                 | 213 ms: 1.01x faster                                         |
| logging_format                | 3.89 us                                                | 3.85 us: 1.01x faster                                        |
| thrift                        | 466 us                                                 | 462 us: 1.01x faster                                         |
| nqueens                       | 62.5 ms                                                | 62.0 ms: 1.01x faster                                        |
| json_loads                    | 17.0 us                                                | 16.8 us: 1.01x faster                                        |
| logging_simple                | 3.60 us                                                | 3.58 us: 1.01x faster                                        |
| deepcopy_reduce               | 2.07 us                                                | 2.06 us: 1.01x faster                                        |
| hexiom                        | 4.86 ms                                                | 4.84 ms: 1.01x faster                                        |
| sqlglot_normalize             | 189 ms                                                 | 188 ms: 1.01x faster                                         |
| pickle_pure_python            | 214 us                                                 | 213 us: 1.01x faster                                         |
| unpickle_pure_python          | 164 us                                                 | 163 us: 1.00x faster                                         |
| pprint_safe_repr              | 533 ms                                                 | 531 ms: 1.00x faster                                         |
| genshi_xml                    | 34.4 ms                                                | 34.2 ms: 1.00x faster                                        |
| crypto_pyaes                  | 54.2 ms                                                | 54.0 ms: 1.00x faster                                        |
| logging_silent                | 70.1 ns                                                | 69.8 ns: 1.00x faster                                        |
| scimark_monte_carlo           | 50.4 ms                                                | 50.2 ms: 1.00x faster                                        |
| deepcopy_memo                 | 27.4 us                                                | 27.3 us: 1.00x faster                                        |
| django_template               | 22.2 ms                                                | 22.2 ms: 1.00x faster                                        |
| genshi_text                   | 16.9 ms                                                | 16.8 ms: 1.00x faster                                        |
| sqlglot_optimize              | 34.9 ms                                                | 34.8 ms: 1.00x faster                                        |
| json_dumps                    | 6.52 ms                                                | 6.51 ms: 1.00x faster                                        |
| sympy_integrate               | 11.3 ms                                                | 11.3 ms: 1.00x faster                                        |
| bpe_tokeniser                 | 3.25 sec                                               | 3.24 sec: 1.00x faster                                       |
| regex_v8                      | 17.0 ms                                                | 17.0 ms: 1.00x faster                                        |
| chaos                         | 41.2 ms                                                | 41.3 ms: 1.00x slower                                        |
| scimark_sparse_mat_mult       | 2.99 ms                                                | 2.99 ms: 1.00x slower                                        |
| coroutines                    | 19.8 ms                                                | 19.8 ms: 1.00x slower                                        |
| nbody                         | 74.0 ms                                                | 74.2 ms: 1.00x slower                                        |
| scimark_sor                   | 105 ms                                                 | 106 ms: 1.00x slower                                         |
| telco                         | 4.76 ms                                                | 4.78 ms: 1.00x slower                                        |
| chameleon                     | 5.08 ms                                                | 5.10 ms: 1.00x slower                                        |
| raytrace                      | 181 ms                                                 | 182 ms: 1.00x slower                                         |
| bench_thread_pool             | 505 us                                                 | 507 us: 1.00x slower                                         |
| sqlglot_parse                 | 856 us                                                 | 860 us: 1.00x slower                                         |
| float                         | 56.0 ms                                                | 56.3 ms: 1.00x slower                                        |
| async_tree_eager_tg           | 47.8 ms                                                | 48.0 ms: 1.00x slower                                        |
| dulwich_log                   | 28.5 ms                                                | 28.7 ms: 1.01x slower                                        |
| async_tree_eager_cpu_io_mixed | 373 ms                                                 | 375 ms: 1.01x slower                                         |
| richards                      | 35.2 ms                                                | 35.4 ms: 1.01x slower                                        |
| pprint_pformat                | 1.08 sec                                               | 1.09 sec: 1.01x slower                                       |
| regex_effbot                  | 2.63 ms                                                | 2.65 ms: 1.01x slower                                        |
| async_tree_memoization_tg     | 288 ms                                                 | 290 ms: 1.01x slower                                         |
| async_tree_eager              | 70.1 ms                                                | 70.7 ms: 1.01x slower                                        |
| spectral_norm                 | 76.3 ms                                                | 77.2 ms: 1.01x slower                                        |
| Geometric mean                | (ref)                                                  | 1.03x faster                                                 |

Benchmark hidden because not significant (42): mdp, coverage, sympy_str, async_tree_eager_cpu_io_mixed_tg, xml_etree_generate, sympy_sum, scimark_lu, pycparser, regex_dna, scimark_fft, tomli_loads, docutils, async_tree_eager_memoization_tg, regex_compile, meteor_contest, deltablue, go, generators, asyncio_websockets, async_tree_eager_io, richards_super, mako, sympy_expand, sqlglot_transpile, pidigits, xml_etree_process, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, pyflate, typing_runtime_protocols, async_tree_io, xml_etree_iterparse, async_generators, html5lib, pylint, async_tree_eager_memoization, xml_etree_parse, async_tree_eager_io_tg, async_tree_none_tg, async_tree_io_tg, async_tree_memoization, tornado_http
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20241001-3.13.0rc3-fae84c7/bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.025x faster
# HPT report

- Reliability score: 60.25% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.33x