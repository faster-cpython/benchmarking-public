# Results vs. 3.13.0

- fork: python
- ref: v3.13.0rc3
- machine: darwin-arm64
- commit hash: fae84c7
- commit date: 2024-10-01
- overall geometric mean: 1.00x slower
- HPT reliability: 61.67%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| chameleon      | 5.08 ms                                                | 5.10 ms: 1.00x slower                                        |
| docutils       | 1.44 sec                                               | 1.44 sec: 1.00x faster                                       |
| Geometric mean | (ref)                                                  | 1.01x slower                                                 |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_eager_tg              | 48.4 ms                                                | 48.0 ms: 1.01x faster                                        |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 346 ms: 1.01x faster                                         |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                         |
| async_tree_eager                 | 70.5 ms                                                | 70.7 ms: 1.00x slower                                        |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (16): asyncio_tcp, async_tree_eager_memoization_tg, async_tree_memoization_tg, asyncio_tcp_ssl, async_tree_eager_memoization, async_tree_cpu_io_mixed, async_tree_eager_cpu_io_mixed, async_tree_memoization, coroutines, async_tree_io_tg, async_tree_io, async_tree_eager_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_none, async_tree_eager_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 73.9 ms                                                | 74.2 ms: 1.00x slower                                        |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 78.5 ms                                                | 78.6 ms: 1.00x slower                                        |
| regex_effbot   | 2.63 ms                                                | 2.65 ms: 1.01x slower                                        |
| regex_dna      | 148 ms                                                 | 149 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|---------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_parse     | 109 ms                                                 | 108 ms: 1.01x faster                                         |
| json_dumps          | 6.56 ms                                                | 6.51 ms: 1.01x faster                                        |
| xml_etree_iterparse | 74.2 ms                                                | 73.8 ms: 1.01x faster                                        |
| pickle_pure_python  | 213 us                                                 | 213 us: 1.00x slower                                         |
| pickle_dict         | 18.2 us                                                | 18.2 us: 1.00x slower                                        |
| pickle              | 7.36 us                                                | 7.39 us: 1.00x slower                                        |
| xml_etree_process   | 40.9 ms                                                | 41.0 ms: 1.00x slower                                        |
| xml_etree_generate  | 56.6 ms                                                | 56.8 ms: 1.00x slower                                        |
| tomli_loads         | 1.56 sec                                               | 1.57 sec: 1.01x slower                                       |
| Geometric mean      | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (5): unpickle_list, json_loads, pickle_list, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 13.7 ms                                                | 13.7 ms: 1.00x slower                                        |
| python_startup         | 17.0 ms                                                | 17.1 ms: 1.00x slower                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 34.4 ms                                                | 34.2 ms: 1.00x faster                                        |
| django_template | 22.2 ms                                                | 22.2 ms: 1.00x faster                                        |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                 |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                        | bm-20241007-darwin-arm64-python-v3.13.0-3.13.0-60403a5 | bm-20241001-darwin-arm64-python-v3.13.0rc3-3.13.0rc3-fae84c7 |
|----------------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| comprehensions                   | 12.2 us                                                | 11.9 us: 1.03x faster                                        |
| nqueens                          | 62.9 ms                                                | 62.0 ms: 1.01x faster                                        |
| xml_etree_parse                  | 109 ms                                                 | 108 ms: 1.01x faster                                         |
| async_tree_eager_tg              | 48.4 ms                                                | 48.0 ms: 1.01x faster                                        |
| mdp                              | 1.50 sec                                               | 1.49 sec: 1.01x faster                                       |
| json_dumps                       | 6.56 ms                                                | 6.51 ms: 1.01x faster                                        |
| fannkuch                         | 282 ms                                                 | 280 ms: 1.01x faster                                         |
| thrift                           | 466 us                                                 | 462 us: 1.01x faster                                         |
| async_tree_eager_cpu_io_mixed_tg | 348 ms                                                 | 346 ms: 1.01x faster                                         |
| coverage                         | 46.1 ms                                                | 45.8 ms: 1.01x faster                                        |
| sqlite_synth                     | 1.54 us                                                | 1.54 us: 1.01x faster                                        |
| xml_etree_iterparse              | 74.2 ms                                                | 73.8 ms: 1.01x faster                                        |
| genshi_xml                       | 34.4 ms                                                | 34.2 ms: 1.00x faster                                        |
| sympy_integrate                  | 11.3 ms                                                | 11.3 ms: 1.00x faster                                        |
| telco                            | 4.80 ms                                                | 4.78 ms: 1.00x faster                                        |
| sympy_sum                        | 75.6 ms                                                | 75.3 ms: 1.00x faster                                        |
| docutils                         | 1.44 sec                                               | 1.44 sec: 1.00x faster                                       |
| scimark_monte_carlo              | 50.4 ms                                                | 50.2 ms: 1.00x faster                                        |
| sqlglot_normalize                | 189 ms                                                 | 188 ms: 1.00x faster                                         |
| hexiom                           | 4.85 ms                                                | 4.84 ms: 1.00x faster                                        |
| sympy_str                        | 145 ms                                                 | 145 ms: 1.00x faster                                         |
| sqlglot_optimize                 | 34.9 ms                                                | 34.8 ms: 1.00x faster                                        |
| dulwich_log                      | 28.7 ms                                                | 28.7 ms: 1.00x faster                                        |
| django_template                  | 22.2 ms                                                | 22.2 ms: 1.00x faster                                        |
| scimark_fft                      | 201 ms                                                 | 200 ms: 1.00x faster                                         |
| deltablue                        | 2.68 ms                                                | 2.68 ms: 1.00x faster                                        |
| bpe_tokeniser                    | 3.24 sec                                               | 3.24 sec: 1.00x faster                                       |
| scimark_sparse_mat_mult          | 2.99 ms                                                | 2.99 ms: 1.00x faster                                        |
| regex_compile                    | 78.5 ms                                                | 78.6 ms: 1.00x slower                                        |
| asyncio_websockets               | 241 ms                                                 | 242 ms: 1.00x slower                                         |
| pickle_pure_python               | 213 us                                                 | 213 us: 1.00x slower                                         |
| meteor_contest                   | 73.8 ms                                                | 73.9 ms: 1.00x slower                                        |
| pyflate                          | 351 ms                                                 | 352 ms: 1.00x slower                                         |
| pickle_dict                      | 18.2 us                                                | 18.2 us: 1.00x slower                                        |
| python_startup_no_site           | 13.7 ms                                                | 13.7 ms: 1.00x slower                                        |
| pickle                           | 7.36 us                                                | 7.39 us: 1.00x slower                                        |
| sqlglot_parse                    | 856 us                                                 | 860 us: 1.00x slower                                         |
| chameleon                        | 5.08 ms                                                | 5.10 ms: 1.00x slower                                        |
| xml_etree_process                | 40.9 ms                                                | 41.0 ms: 1.00x slower                                        |
| xml_etree_generate               | 56.6 ms                                                | 56.8 ms: 1.00x slower                                        |
| nbody                            | 73.9 ms                                                | 74.2 ms: 1.00x slower                                        |
| async_tree_eager                 | 70.5 ms                                                | 70.7 ms: 1.00x slower                                        |
| create_gc_cycles                 | 803 us                                                 | 807 us: 1.00x slower                                         |
| python_startup                   | 17.0 ms                                                | 17.1 ms: 1.00x slower                                        |
| tomli_loads                      | 1.56 sec                                               | 1.57 sec: 1.01x slower                                       |
| async_generators                 | 294 ms                                                 | 296 ms: 1.01x slower                                         |
| regex_effbot                     | 2.63 ms                                                | 2.65 ms: 1.01x slower                                        |
| pathlib                          | 22.8 ms                                                | 23.0 ms: 1.01x slower                                        |
| regex_dna                        | 148 ms                                                 | 149 ms: 1.01x slower                                         |
| pprint_pformat                   | 1.08 sec                                               | 1.09 sec: 1.01x slower                                       |
| mypy2                            | 396 ms                                                 | 495 ms: 1.25x slower                                         |
| Geometric mean                   | (ref)                                                  | 1.00x slower                                                 |

Benchmark hidden because not significant (60): asyncio_tcp, aiohttp, async_tree_eager_memoization_tg, unpickle_list, json_loads, async_tree_memoization_tg, pylint, spectral_norm, pycparser, genshi_text, deepcopy, 2to3, unpack_sequence, deepcopy_reduce, gc_traversal, logging_format, richards_super, pickle_list, asyncio_tcp_ssl, sqlglot_transpile, logging_silent, generators, async_tree_eager_memoization, crypto_pyaes, raytrace, richards, pprint_safe_repr, unpickle_pure_python, mako, sympy_expand, regex_v8, json, scimark_lu, html5lib, go, pidigits, scimark_sor, async_tree_cpu_io_mixed, chaos, float, async_tree_eager_cpu_io_mixed, async_tree_memoization, coroutines, async_tree_io_tg, logging_simple, bench_thread_pool, flaskblogging, deepcopy_memo, async_tree_io, unpickle, async_tree_eager_io, dask, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, async_tree_none_tg, bench_mp_pool, async_tree_none, async_tree_eager_io_tg, gunicorn, tornado_http

# HPT report

- Reliability score: 61.67% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x