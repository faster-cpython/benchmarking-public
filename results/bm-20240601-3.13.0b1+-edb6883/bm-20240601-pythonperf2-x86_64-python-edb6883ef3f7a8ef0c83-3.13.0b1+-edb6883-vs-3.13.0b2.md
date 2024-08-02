# Results vs. 3.13.0b2

- fork: python
- ref: edb6883ef3f7a8ef0c83
- machine: linux-x86_64
- commit hash: edb6883
- commit date: 2024-06-01
- overall geometric mean: 1.00x slower
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 293 ms: 1.01x slower                                                         |
| chameleon      | 7.40 ms                                                          | 7.46 ms: 1.01x slower                                                        |
| html5lib       | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                 |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.2 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                        |
| regex_compile  | 144 ms                                                           | 144 ms: 1.00x faster                                                         |
| regex_dna      | 249 ms                                                           | 251 ms: 1.01x slower                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict        | 32.8 us                                                          | 31.1 us: 1.06x faster                                                        |
| unpickle           | 15.7 us                                                          | 15.2 us: 1.03x faster                                                        |
| pickle             | 10.6 us                                                          | 10.4 us: 1.02x faster                                                        |
| json_loads         | 25.0 us                                                          | 24.8 us: 1.01x faster                                                        |
| json_dumps         | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| xml_etree_parse    | 144 ms                                                           | 144 ms: 1.00x slower                                                         |
| pickle_pure_python | 307 us                                                           | 310 us: 1.01x slower                                                         |
| xml_etree_generate | 85.7 ms                                                          | 86.7 ms: 1.01x slower                                                        |
| xml_etree_process  | 59.7 ms                                                          | 60.5 ms: 1.01x slower                                                        |
| unpickle_list      | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| Geometric mean     | (ref)                                                            | 1.01x faster                                                                 |

Benchmark hidden because not significant (4): pickle_list, tomli_loads, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.85 ms                                                          | 8.79 ms: 1.01x faster                                                        |
| python_startup         | 13.2 ms                                                          | 13.1 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 56.7 ms: 1.02x faster                                                        |
| django_template | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                        |
| mako            | 10.4 ms                                                          | 10.7 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240601-pythonperf2-x86_64-python-edb6883ef3f7a8ef0c83-3.13.0b1+-edb6883 |
|--------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict              | 32.8 us                                                          | 31.1 us: 1.06x faster                                                        |
| gc_traversal             | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                        |
| scimark_sor              | 119 ms                                                           | 114 ms: 1.04x faster                                                         |
| unpickle                 | 15.7 us                                                          | 15.2 us: 1.03x faster                                                        |
| go                       | 165 ms                                                           | 160 ms: 1.03x faster                                                         |
| scimark_fft              | 312 ms                                                           | 304 ms: 1.03x faster                                                         |
| genshi_xml               | 58.1 ms                                                          | 56.7 ms: 1.02x faster                                                        |
| json                     | 5.35 ms                                                          | 5.23 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                                        |
| regex_v8                 | 26.0 ms                                                          | 25.5 ms: 1.02x faster                                                        |
| logging_format           | 7.11 us                                                          | 6.97 us: 1.02x faster                                                        |
| pickle                   | 10.6 us                                                          | 10.4 us: 1.02x faster                                                        |
| asyncio_websockets       | 395 ms                                                           | 388 ms: 1.02x faster                                                         |
| thrift                   | 880 us                                                           | 867 us: 1.01x faster                                                         |
| float                    | 80.2 ms                                                          | 79.2 ms: 1.01x faster                                                        |
| html5lib                 | 74.7 ms                                                          | 73.7 ms: 1.01x faster                                                        |
| crypto_pyaes             | 73.6 ms                                                          | 72.7 ms: 1.01x faster                                                        |
| json_loads               | 25.0 us                                                          | 24.8 us: 1.01x faster                                                        |
| async_generators         | 363 ms                                                           | 359 ms: 1.01x faster                                                         |
| json_dumps               | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| python_startup_no_site   | 8.85 ms                                                          | 8.79 ms: 1.01x faster                                                        |
| spectral_norm            | 97.3 ms                                                          | 96.8 ms: 1.01x faster                                                        |
| python_startup           | 13.2 ms                                                          | 13.1 ms: 1.01x faster                                                        |
| regex_compile            | 144 ms                                                           | 144 ms: 1.00x faster                                                         |
| sqlglot_optimize         | 59.5 ms                                                          | 59.4 ms: 1.00x faster                                                        |
| dulwich_log              | 67.3 ms                                                          | 67.5 ms: 1.00x slower                                                        |
| xml_etree_parse          | 144 ms                                                           | 144 ms: 1.00x slower                                                         |
| richards_super           | 61.2 ms                                                          | 61.5 ms: 1.01x slower                                                        |
| 2to3                     | 291 ms                                                           | 293 ms: 1.01x slower                                                         |
| sqlite_synth             | 2.80 us                                                          | 2.82 us: 1.01x slower                                                        |
| regex_dna                | 249 ms                                                           | 251 ms: 1.01x slower                                                         |
| sympy_str                | 295 ms                                                           | 297 ms: 1.01x slower                                                         |
| fannkuch                 | 353 ms                                                           | 355 ms: 1.01x slower                                                         |
| sqlglot_normalize        | 120 ms                                                           | 121 ms: 1.01x slower                                                         |
| deepcopy                 | 377 us                                                           | 380 us: 1.01x slower                                                         |
| chameleon                | 7.40 ms                                                          | 7.46 ms: 1.01x slower                                                        |
| sqlglot_transpile        | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                        |
| pickle_pure_python       | 307 us                                                           | 310 us: 1.01x slower                                                         |
| deepcopy_reduce          | 3.39 us                                                          | 3.42 us: 1.01x slower                                                        |
| meteor_contest           | 128 ms                                                           | 129 ms: 1.01x slower                                                         |
| scimark_monte_carlo      | 65.5 ms                                                          | 66.2 ms: 1.01x slower                                                        |
| pprint_safe_repr         | 818 ms                                                           | 826 ms: 1.01x slower                                                         |
| xml_etree_generate       | 85.7 ms                                                          | 86.7 ms: 1.01x slower                                                        |
| sympy_expand             | 501 ms                                                           | 506 ms: 1.01x slower                                                         |
| sqlglot_parse            | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                        |
| django_template          | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                        |
| sympy_integrate          | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                                        |
| logging_silent           | 96.3 ns                                                          | 97.5 ns: 1.01x slower                                                        |
| xml_etree_process        | 59.7 ms                                                          | 60.5 ms: 1.01x slower                                                        |
| pathlib                  | 17.1 ms                                                          | 17.4 ms: 1.01x slower                                                        |
| pprint_pformat           | 1.66 sec                                                         | 1.69 sec: 1.02x slower                                                       |
| chaos                    | 59.6 ms                                                          | 60.7 ms: 1.02x slower                                                        |
| typing_runtime_protocols | 171 us                                                           | 174 us: 1.02x slower                                                         |
| raytrace                 | 260 ms                                                           | 265 ms: 1.02x slower                                                         |
| unpickle_list            | 4.70 us                                                          | 4.79 us: 1.02x slower                                                        |
| telco                    | 8.40 ms                                                          | 8.58 ms: 1.02x slower                                                        |
| generators               | 33.5 ms                                                          | 34.3 ms: 1.02x slower                                                        |
| mdp                      | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                       |
| mako                     | 10.4 ms                                                          | 10.7 ms: 1.03x slower                                                        |
| nqueens                  | 88.4 ms                                                          | 91.1 ms: 1.03x slower                                                        |
| hexiom                   | 6.35 ms                                                          | 6.55 ms: 1.03x slower                                                        |
| richards                 | 53.4 ms                                                          | 55.3 ms: 1.03x slower                                                        |
| pycparser                | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                       |
| coverage                 | 83.5 ms                                                          | 86.7 ms: 1.04x slower                                                        |
| regex_effbot             | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                        |
| Geometric mean           | (ref)                                                            | 1.00x slower                                                                 |

Benchmark hidden because not significant (36): bench_mp_pool, nbody, create_gc_cycles, bench_thread_pool, aiohttp, deltablue, pickle_list, tomli_loads, logging_simple, tornado_http, xml_etree_iterparse, pidigits, unpickle_pure_python, scimark_lu, asyncio_tcp, pyflate, genshi_text, docutils, deepcopy_memo, asyncio_tcp_ssl, sympy_sum, coroutines, flaskblogging, comprehensions, gunicorn, dask, async_tree_io_tg, mypy2, async_tree_none, pylint, async_tree_memoization, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 99.91% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x