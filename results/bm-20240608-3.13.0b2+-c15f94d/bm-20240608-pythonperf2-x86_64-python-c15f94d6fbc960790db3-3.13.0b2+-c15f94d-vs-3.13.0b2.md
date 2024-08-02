# Results vs. 3.13.0b2

- fork: python
- ref: c15f94d6fbc960790db3
- machine: linux-x86_64
- commit hash: c15f94d
- commit date: 2024-06-08
- overall geometric mean: 1.00x slower
- HPT reliability: 97.87%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 291 ms: 1.00x faster                                                         |
| docutils       | 2.98 sec                                                         | 2.99 sec: 1.00x slower                                                       |
| html5lib       | 74.7 ms                                                          | 75.3 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|-------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 365 ms                                                           | 371 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed | 604 ms                                                           | 614 ms: 1.02x slower                                                         |
| Geometric mean          | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (6): async_tree_io_tg, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 80.8 ms: 1.01x slower                                                        |
| nbody          | 87.8 ms                                                          | 89.4 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 248 ms: 1.01x faster                                                         |
| regex_compile  | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| regex_v8       | 26.0 ms                                                          | 26.4 ms: 1.02x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.72 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                            | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_loads           | 25.0 us                                                          | 24.8 us: 1.01x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 85.2 ms: 1.01x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 102 ms: 1.01x faster                                                         |
| unpickle_pure_python | 224 us                                                           | 226 us: 1.01x slower                                                         |
| pickle_pure_python   | 307 us                                                           | 309 us: 1.01x slower                                                         |
| pickle_dict          | 32.8 us                                                          | 33.3 us: 1.02x slower                                                        |
| unpickle_list        | 4.70 us                                                          | 4.80 us: 1.02x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (5): tomli_loads, xml_etree_parse, pickle, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                 |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                        |
| genshi_text    | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240608-pythonperf2-x86_64-python-c15f94d6fbc960790db3-3.13.0b2+-c15f94d |
|--------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal             | 4.69 ms                                                          | 4.38 ms: 1.07x faster                                                        |
| genshi_xml               | 58.1 ms                                                          | 55.5 ms: 1.05x faster                                                        |
| genshi_text              | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.18 ms: 1.02x faster                                                        |
| json                     | 5.35 ms                                                          | 5.28 ms: 1.01x faster                                                        |
| richards_super           | 61.2 ms                                                          | 60.3 ms: 1.01x faster                                                        |
| logging_format           | 7.11 us                                                          | 7.02 us: 1.01x faster                                                        |
| scimark_sor              | 119 ms                                                           | 117 ms: 1.01x faster                                                         |
| json_loads               | 25.0 us                                                          | 24.8 us: 1.01x faster                                                        |
| asyncio_websockets       | 395 ms                                                           | 391 ms: 1.01x faster                                                         |
| go                       | 165 ms                                                           | 163 ms: 1.01x faster                                                         |
| sqlglot_normalize        | 120 ms                                                           | 119 ms: 1.01x faster                                                         |
| sqlglot_optimize         | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                        |
| xml_etree_process        | 59.7 ms                                                          | 59.3 ms: 1.01x faster                                                        |
| deepcopy_reduce          | 3.39 us                                                          | 3.37 us: 1.01x faster                                                        |
| xml_etree_generate       | 85.7 ms                                                          | 85.2 ms: 1.01x faster                                                        |
| xml_etree_iterparse      | 103 ms                                                           | 102 ms: 1.01x faster                                                         |
| regex_dna                | 249 ms                                                           | 248 ms: 1.01x faster                                                         |
| pprint_safe_repr         | 818 ms                                                           | 814 ms: 1.00x faster                                                         |
| generators               | 33.5 ms                                                          | 33.4 ms: 1.00x faster                                                        |
| 2to3                     | 291 ms                                                           | 291 ms: 1.00x faster                                                         |
| python_startup           | 13.2 ms                                                          | 13.2 ms: 1.00x faster                                                        |
| coroutines               | 22.0 ms                                                          | 22.0 ms: 1.00x slower                                                        |
| sympy_str                | 295 ms                                                           | 295 ms: 1.00x slower                                                         |
| sqlite_synth             | 2.80 us                                                          | 2.80 us: 1.00x slower                                                        |
| hexiom                   | 6.35 ms                                                          | 6.37 ms: 1.00x slower                                                        |
| docutils                 | 2.98 sec                                                         | 2.99 sec: 1.00x slower                                                       |
| crypto_pyaes             | 73.6 ms                                                          | 73.9 ms: 1.00x slower                                                        |
| scimark_lu               | 97.5 ms                                                          | 97.9 ms: 1.00x slower                                                        |
| nqueens                  | 88.4 ms                                                          | 88.8 ms: 1.00x slower                                                        |
| regex_compile            | 144 ms                                                           | 145 ms: 1.01x slower                                                         |
| pyflate                  | 482 ms                                                           | 484 ms: 1.01x slower                                                         |
| unpickle_pure_python     | 224 us                                                           | 226 us: 1.01x slower                                                         |
| pickle_pure_python       | 307 us                                                           | 309 us: 1.01x slower                                                         |
| comprehensions           | 17.0 us                                                          | 17.1 us: 1.01x slower                                                        |
| coverage                 | 83.5 ms                                                          | 84.1 ms: 1.01x slower                                                        |
| float                    | 80.2 ms                                                          | 80.8 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                        |
| html5lib                 | 74.7 ms                                                          | 75.3 ms: 1.01x slower                                                        |
| sympy_integrate          | 23.2 ms                                                          | 23.4 ms: 1.01x slower                                                        |
| pathlib                  | 17.1 ms                                                          | 17.3 ms: 1.01x slower                                                        |
| sqlglot_parse            | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                        |
| deepcopy                 | 377 us                                                           | 381 us: 1.01x slower                                                         |
| dask                     | 391 ms                                                           | 396 ms: 1.01x slower                                                         |
| chaos                    | 59.6 ms                                                          | 60.5 ms: 1.01x slower                                                        |
| fannkuch                 | 353 ms                                                           | 358 ms: 1.02x slower                                                         |
| deepcopy_memo            | 37.3 us                                                          | 37.8 us: 1.02x slower                                                        |
| async_tree_none          | 365 ms                                                           | 371 ms: 1.02x slower                                                         |
| pickle_dict              | 32.8 us                                                          | 33.3 us: 1.02x slower                                                        |
| typing_runtime_protocols | 171 us                                                           | 173 us: 1.02x slower                                                         |
| regex_v8                 | 26.0 ms                                                          | 26.4 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed  | 604 ms                                                           | 614 ms: 1.02x slower                                                         |
| thrift                   | 880 us                                                           | 894 us: 1.02x slower                                                         |
| create_gc_cycles         | 2.00 ms                                                          | 2.04 ms: 1.02x slower                                                        |
| nbody                    | 87.8 ms                                                          | 89.4 ms: 1.02x slower                                                        |
| async_generators         | 363 ms                                                           | 370 ms: 1.02x slower                                                         |
| unpickle_list            | 4.70 us                                                          | 4.80 us: 1.02x slower                                                        |
| json_dumps               | 10.8 ms                                                          | 11.1 ms: 1.03x slower                                                        |
| raytrace                 | 260 ms                                                           | 268 ms: 1.03x slower                                                         |
| mdp                      | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                                       |
| regex_effbot             | 3.40 ms                                                          | 3.72 ms: 1.09x slower                                                        |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (40): bench_mp_pool, scimark_fft, flaskblogging, tomli_loads, deltablue, gunicorn, mako, xml_etree_parse, dulwich_log, pickle, tornado_http, sympy_sum, pidigits, mypy2, spectral_norm, python_startup_no_site, pprint_pformat, asyncio_tcp_ssl, scimark_monte_carlo, meteor_contest, aiohttp, logging_silent, logging_simple, chameleon, asyncio_tcp, sympy_expand, richards, pylint, telco, pickle_list, unpickle, django_template, async_tree_io_tg, pycparser, bench_thread_pool, async_tree_memoization, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 97.87% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x