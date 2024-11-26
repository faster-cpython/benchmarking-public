# Results vs. 3.13.0

- fork: python
- ref: v3.13.0a4
- machine: windows-amd64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.005x faster
- HPT reliability: 95.10%
- HPT 99th percentile: 1.00x slower
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 221 ms                                                      | 214 ms: 1.03x faster                                            |
| chameleon      | 4.82 ms                                                     | 5.01 ms: 1.04x slower                                           |
| docutils       | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| html5lib       | 38.9 ms                                                     | 36.9 ms: 1.06x faster                                           |
| tornado_http   | 93.0 ms                                                     | 84.3 ms: 1.10x faster                                           |
| Geometric mean | (ref)                                                       | 1.03x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                            |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 453 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 472 ms: 1.25x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 274 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 732 ms: 1.40x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 758 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.22x slower                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 49.9 ms                                                     | 51.0 ms: 1.02x slower                                           |
| nbody          | 68.4 ms                                                     | 73.2 ms: 1.07x slower                                           |
| Geometric mean | (ref)                                                       | 1.03x slower                                                    |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_v8       | 21.4 ms                                                     | 14.4 ms: 1.49x faster                                           |
| regex_compile  | 80.5 ms                                                     | 77.8 ms: 1.03x faster                                           |
| regex_effbot   | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                           |
| regex_dna      | 115 ms                                                      | 115 ms: 1.00x faster                                            |
| Geometric mean | (ref)                                                       | 1.12x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| json_loads           | 15.1 us                                                     | 13.7 us: 1.11x faster                                           |
| json_dumps           | 5.92 ms                                                     | 5.58 ms: 1.06x faster                                           |
| unpickle_pure_python | 133 us                                                      | 129 us: 1.03x faster                                            |
| pickle_pure_python   | 190 us                                                      | 186 us: 1.02x faster                                            |
| xml_etree_parse      | 93.6 ms                                                     | 92.2 ms: 1.02x faster                                           |
| xml_etree_generate   | 54.0 ms                                                     | 54.5 ms: 1.01x slower                                           |
| tomli_loads          | 1.39 sec                                                    | 1.43 sec: 1.02x slower                                          |
| xml_etree_iterparse  | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                           |
| Geometric mean       | (ref)                                                       | 1.02x faster                                                    |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 25.4 ms                                                     | 20.2 ms: 1.26x faster                                           |
| python_startup_no_site | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                           |
| Geometric mean         | (ref)                                                       | 1.13x faster                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako           | 6.35 ms                                                     | 6.29 ms: 1.01x faster                                           |
| genshi_text    | 15.6 ms                                                     | 16.0 ms: 1.03x slower                                           |
| Geometric mean | (ref)                                                       | 1.00x slower                                                    |

Benchmark hidden because not significant (2): genshi_xml, django_template

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 | bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| create_gc_cycles           | 1.26 ms                                                     | 743 us: 1.69x faster                                            |
| mypy2                      | 679 ms                                                      | 416 ms: 1.63x faster                                            |
| typing_runtime_protocols   | 105 us                                                      | 71.0 us: 1.49x faster                                           |
| regex_v8                   | 21.4 ms                                                     | 14.4 ms: 1.49x faster                                           |
| gc_traversal               | 1.97 ms                                                     | 1.50 ms: 1.31x faster                                           |
| bench_mp_pool              | 86.4 ms                                                     | 66.4 ms: 1.30x faster                                           |
| python_startup             | 25.4 ms                                                     | 20.2 ms: 1.26x faster                                           |
| json_loads                 | 15.1 us                                                     | 13.7 us: 1.11x faster                                           |
| tornado_http               | 93.0 ms                                                     | 84.3 ms: 1.10x faster                                           |
| json                       | 3.19 ms                                                     | 2.91 ms: 1.10x faster                                           |
| thrift                     | 8.80 ms                                                     | 8.18 ms: 1.07x faster                                           |
| sympy_expand               | 291 ms                                                      | 274 ms: 1.06x faster                                            |
| spectral_norm              | 62.8 ms                                                     | 59.0 ms: 1.06x faster                                           |
| crypto_pyaes               | 45.4 ms                                                     | 42.8 ms: 1.06x faster                                           |
| json_dumps                 | 5.92 ms                                                     | 5.58 ms: 1.06x faster                                           |
| sympy_str                  | 169 ms                                                      | 160 ms: 1.06x faster                                            |
| html5lib                   | 38.9 ms                                                     | 36.9 ms: 1.06x faster                                           |
| sympy_sum                  | 86.9 ms                                                     | 83.5 ms: 1.04x faster                                           |
| mdp                        | 1.39 sec                                                    | 1.34 sec: 1.04x faster                                          |
| regex_compile              | 80.5 ms                                                     | 77.8 ms: 1.03x faster                                           |
| unpickle_pure_python       | 133 us                                                      | 129 us: 1.03x faster                                            |
| 2to3                       | 221 ms                                                      | 214 ms: 1.03x faster                                            |
| go                         | 87.0 ms                                                     | 84.4 ms: 1.03x faster                                           |
| pickle_pure_python         | 190 us                                                      | 186 us: 1.02x faster                                            |
| hexiom                     | 3.89 ms                                                     | 3.82 ms: 1.02x faster                                           |
| python_startup_no_site     | 18.1 ms                                                     | 17.8 ms: 1.02x faster                                           |
| meteor_contest             | 73.5 ms                                                     | 72.2 ms: 1.02x faster                                           |
| docutils                   | 1.57 sec                                                    | 1.55 sec: 1.02x faster                                          |
| xml_etree_parse            | 93.6 ms                                                     | 92.2 ms: 1.02x faster                                           |
| deepcopy_memo              | 23.3 us                                                     | 23.0 us: 1.01x faster                                           |
| fannkuch                   | 253 ms                                                      | 250 ms: 1.01x faster                                            |
| telco                      | 4.79 ms                                                     | 4.73 ms: 1.01x faster                                           |
| mako                       | 6.35 ms                                                     | 6.29 ms: 1.01x faster                                           |
| sympy_integrate            | 12.5 ms                                                     | 12.4 ms: 1.01x faster                                           |
| regex_effbot               | 1.58 ms                                                     | 1.56 ms: 1.01x faster                                           |
| regex_dna                  | 115 ms                                                      | 115 ms: 1.00x faster                                            |
| sqlglot_normalize          | 175 ms                                                      | 176 ms: 1.01x slower                                            |
| pyflate                    | 283 ms                                                      | 285 ms: 1.01x slower                                            |
| xml_etree_generate         | 54.0 ms                                                     | 54.5 ms: 1.01x slower                                           |
| dulwich_log                | 40.8 ms                                                     | 41.3 ms: 1.01x slower                                           |
| pprint_safe_repr           | 494 ms                                                      | 500 ms: 1.01x slower                                            |
| sqlglot_optimize           | 32.9 ms                                                     | 33.4 ms: 1.01x slower                                           |
| scimark_sparse_mat_mult    | 2.46 ms                                                     | 2.49 ms: 1.01x slower                                           |
| float                      | 49.9 ms                                                     | 51.0 ms: 1.02x slower                                           |
| scimark_sor                | 76.2 ms                                                     | 77.9 ms: 1.02x slower                                           |
| pprint_pformat             | 999 ms                                                      | 1.02 sec: 1.02x slower                                          |
| chaos                      | 38.5 ms                                                     | 39.5 ms: 1.02x slower                                           |
| tomli_loads                | 1.39 sec                                                    | 1.43 sec: 1.02x slower                                          |
| richards_super             | 30.9 ms                                                     | 31.6 ms: 1.02x slower                                           |
| richards                   | 27.3 ms                                                     | 28.0 ms: 1.03x slower                                           |
| genshi_text                | 15.6 ms                                                     | 16.0 ms: 1.03x slower                                           |
| nqueens                    | 56.7 ms                                                     | 58.2 ms: 1.03x slower                                           |
| sqlglot_transpile          | 956 us                                                      | 983 us: 1.03x slower                                            |
| raytrace                   | 160 ms                                                      | 165 ms: 1.03x slower                                            |
| deepcopy                   | 226 us                                                      | 233 us: 1.03x slower                                            |
| async_generators           | 223 ms                                                      | 230 ms: 1.03x slower                                            |
| logging_simple             | 5.96 us                                                     | 6.15 us: 1.03x slower                                           |
| deltablue                  | 1.92 ms                                                     | 1.98 ms: 1.03x slower                                           |
| coroutines                 | 12.8 ms                                                     | 13.2 ms: 1.04x slower                                           |
| chameleon                  | 4.82 ms                                                     | 5.01 ms: 1.04x slower                                           |
| coverage                   | 45.6 ms                                                     | 47.3 ms: 1.04x slower                                           |
| scimark_lu                 | 53.0 ms                                                     | 55.0 ms: 1.04x slower                                           |
| scimark_fft                | 172 ms                                                      | 179 ms: 1.04x slower                                            |
| logging_silent             | 54.6 ns                                                     | 57.3 ns: 1.05x slower                                           |
| comprehensions             | 10.3 us                                                     | 10.8 us: 1.05x slower                                           |
| logging_format             | 6.26 us                                                     | 6.57 us: 1.05x slower                                           |
| xml_etree_iterparse        | 61.8 ms                                                     | 65.1 ms: 1.05x slower                                           |
| generators                 | 19.5 ms                                                     | 20.8 ms: 1.07x slower                                           |
| nbody                      | 68.4 ms                                                     | 73.2 ms: 1.07x slower                                           |
| pycparser                  | 683 ms                                                      | 754 ms: 1.10x slower                                            |
| async_tree_none            | 226 ms                                                      | 266 ms: 1.18x slower                                            |
| async_tree_cpu_io_mixed    | 383 ms                                                      | 453 ms: 1.18x slower                                            |
| async_tree_memoization_tg  | 288 ms                                                      | 349 ms: 1.21x slower                                            |
| async_tree_memoization     | 276 ms                                                      | 340 ms: 1.23x slower                                            |
| async_tree_cpu_io_mixed_tg | 377 ms                                                      | 472 ms: 1.25x slower                                            |
| async_tree_none_tg         | 209 ms                                                      | 274 ms: 1.31x slower                                            |
| async_tree_io              | 521 ms                                                      | 732 ms: 1.40x slower                                            |
| async_tree_io_tg           | 518 ms                                                      | 758 ms: 1.46x slower                                            |
| Geometric mean             | (ref)                                                       | 1.01x faster                                                    |

Benchmark hidden because not significant (10): bench_thread_pool, pylint, genshi_xml, deepcopy_reduce, sqlglot_parse, scimark_monte_carlo, pathlib, pidigits, xml_etree_process, django_template
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: asyncio_websockets, bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf1-amd64-python-v3.13.0a4-3.13.0a4-9d34f60.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, flaskblogging, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.005x faster
# HPT report

- Reliability score: 95.10% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: unknown