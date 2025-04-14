# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.035x slower
- HPT reliability: 98.78%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| chameleon      | 7.49 ms                                                      | 7.66 ms: 1.02x slower                                            |
| docutils       | 2.81 sec                                                     | 3.03 sec: 1.08x slower                                           |
| html5lib       | 72.9 ms                                                      | 75.9 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 458 ms                                                       | 444 ms: 1.03x faster                                             |
| async_generators           | 364 ms                                                       | 367 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 586 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 619 ms: 1.04x slower                                             |
| async_tree_memoization     | 447 ms                                                       | 467 ms: 1.04x slower                                             |
| async_tree_io              | 832 ms                                                       | 870 ms: 1.05x slower                                             |
| async_tree_io_tg           | 823 ms                                                       | 889 ms: 1.08x slower                                             |
| Geometric mean             | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (4): asyncio_websockets, coroutines, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.6 ms                                                      | 81.1 ms: 1.01x faster                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                            |
| regex_dna      | 238 ms                                                       | 243 ms: 1.02x slower                                             |
| regex_v8       | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                            |
| regex_compile  | 143 ms                                                       | 147 ms: 1.03x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 318 us: 1.01x faster                                             |
| json_loads           | 24.7 us                                                      | 24.4 us: 1.01x faster                                            |
| json_dumps           | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                            |
| unpickle_pure_python | 216 us                                                       | 222 us: 1.03x slower                                             |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                             |
| xml_etree_generate   | 85.2 ms                                                      | 88.9 ms: 1.04x slower                                            |
| tomli_loads          | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 8.86 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.10x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text     | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                            |
| mako            | 10.3 ms                                                      | 10.5 ms: 1.02x slower                                            |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                      | 1.02 sec                                                     | 780 ms: 1.31x faster                                             |
| create_gc_cycles           | 2.65 ms                                                      | 2.02 ms: 1.31x faster                                            |
| python_startup             | 15.6 ms                                                      | 12.9 ms: 1.21x faster                                            |
| scimark_sor                | 125 ms                                                       | 117 ms: 1.07x faster                                             |
| fannkuch                   | 384 ms                                                       | 365 ms: 1.05x faster                                             |
| json                       | 5.62 ms                                                      | 5.36 ms: 1.05x faster                                            |
| go                         | 167 ms                                                       | 160 ms: 1.04x faster                                             |
| bench_thread_pool          | 929 us                                                       | 895 us: 1.04x faster                                             |
| genshi_text                | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                            |
| async_tree_memoization_tg  | 458 ms                                                       | 444 ms: 1.03x faster                                             |
| pyflate                    | 493 ms                                                       | 480 ms: 1.03x faster                                             |
| chaos                      | 60.6 ms                                                      | 59.4 ms: 1.02x faster                                            |
| generators                 | 33.9 ms                                                      | 33.3 ms: 1.02x faster                                            |
| hexiom                     | 6.47 ms                                                      | 6.37 ms: 1.02x faster                                            |
| nqueens                    | 92.3 ms                                                      | 91.1 ms: 1.01x faster                                            |
| pickle_pure_python         | 322 us                                                       | 318 us: 1.01x faster                                             |
| json_loads                 | 24.7 us                                                      | 24.4 us: 1.01x faster                                            |
| mdp                        | 2.53 sec                                                     | 2.50 sec: 1.01x faster                                           |
| coverage                   | 84.5 ms                                                      | 83.7 ms: 1.01x faster                                            |
| thrift                     | 918 us                                                       | 908 us: 1.01x faster                                             |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                            |
| 2to3                       | 293 ms                                                       | 290 ms: 1.01x faster                                             |
| crypto_pyaes               | 73.5 ms                                                      | 72.9 ms: 1.01x faster                                            |
| logging_silent             | 97.5 ns                                                      | 96.6 ns: 1.01x faster                                            |
| python_startup_no_site     | 8.93 ms                                                      | 8.86 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                            |
| pprint_pformat             | 1.70 sec                                                     | 1.69 sec: 1.01x faster                                           |
| float                      | 81.6 ms                                                      | 81.1 ms: 1.01x faster                                            |
| pprint_safe_repr           | 835 ms                                                       | 830 ms: 1.01x faster                                             |
| pathlib                    | 17.4 ms                                                      | 17.3 ms: 1.00x faster                                            |
| raytrace                   | 267 ms                                                       | 268 ms: 1.00x slower                                             |
| json_dumps                 | 10.8 ms                                                      | 10.9 ms: 1.01x slower                                            |
| async_generators           | 364 ms                                                       | 367 ms: 1.01x slower                                             |
| regex_effbot               | 3.51 ms                                                      | 3.56 ms: 1.01x slower                                            |
| richards_super             | 60.2 ms                                                      | 61.0 ms: 1.01x slower                                            |
| deepcopy_memo              | 38.9 us                                                      | 39.4 us: 1.01x slower                                            |
| sympy_expand               | 506 ms                                                       | 514 ms: 1.01x slower                                             |
| meteor_contest             | 130 ms                                                       | 132 ms: 1.01x slower                                             |
| sympy_integrate            | 23.4 ms                                                      | 23.8 ms: 1.02x slower                                            |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                            |
| mako                       | 10.3 ms                                                      | 10.5 ms: 1.02x slower                                            |
| deepcopy                   | 388 us                                                       | 395 us: 1.02x slower                                             |
| regex_dna                  | 238 ms                                                       | 243 ms: 1.02x slower                                             |
| sympy_str                  | 297 ms                                                       | 302 ms: 1.02x slower                                             |
| logging_format             | 6.95 us                                                      | 7.09 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 586 ms: 1.02x slower                                             |
| sqlglot_normalize          | 119 ms                                                       | 121 ms: 1.02x slower                                             |
| chameleon                  | 7.49 ms                                                      | 7.66 ms: 1.02x slower                                            |
| sympy_sum                  | 154 ms                                                       | 157 ms: 1.02x slower                                             |
| sqlglot_optimize           | 58.7 ms                                                      | 60.1 ms: 1.03x slower                                            |
| regex_v8                   | 24.9 ms                                                      | 25.6 ms: 1.03x slower                                            |
| unpickle_pure_python       | 216 us                                                       | 222 us: 1.03x slower                                             |
| richards                   | 52.5 ms                                                      | 54.0 ms: 1.03x slower                                            |
| xml_etree_iterparse        | 99.8 ms                                                      | 103 ms: 1.03x slower                                             |
| dulwich_log                | 65.5 ms                                                      | 67.6 ms: 1.03x slower                                            |
| regex_compile              | 143 ms                                                       | 147 ms: 1.03x slower                                             |
| logging_simple             | 6.28 us                                                      | 6.50 us: 1.04x slower                                            |
| scimark_lu                 | 97.4 ms                                                      | 101 ms: 1.04x slower                                             |
| async_tree_cpu_io_mixed    | 596 ms                                                       | 619 ms: 1.04x slower                                             |
| sqlglot_transpile          | 1.76 ms                                                      | 1.83 ms: 1.04x slower                                            |
| gc_traversal               | 4.48 ms                                                      | 4.66 ms: 1.04x slower                                            |
| html5lib                   | 72.9 ms                                                      | 75.9 ms: 1.04x slower                                            |
| xml_etree_generate         | 85.2 ms                                                      | 88.9 ms: 1.04x slower                                            |
| async_tree_memoization     | 447 ms                                                       | 467 ms: 1.04x slower                                             |
| async_tree_io              | 832 ms                                                       | 870 ms: 1.05x slower                                             |
| sqlglot_parse              | 1.37 ms                                                      | 1.44 ms: 1.05x slower                                            |
| tomli_loads                | 2.43 sec                                                     | 2.58 sec: 1.06x slower                                           |
| scimark_monte_carlo        | 65.2 ms                                                      | 69.5 ms: 1.07x slower                                            |
| docutils                   | 2.81 sec                                                     | 3.03 sec: 1.08x slower                                           |
| async_tree_io_tg           | 823 ms                                                       | 889 ms: 1.08x slower                                             |
| scimark_fft                | 298 ms                                                       | 328 ms: 1.10x slower                                             |
| telco                      | 8.77 ms                                                      | 175 ms: 19.91x slower                                            |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (17): nbody, typing_runtime_protocols, bench_mp_pool, pycparser, asyncio_websockets, genshi_xml, deepcopy_reduce, xml_etree_process, coroutines, pidigits, spectral_norm, deltablue, xml_etree_parse, async_tree_none, pylint, async_tree_none_tg, tornado_http
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.035x slower
# HPT report

- Reliability score: 98.78% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x