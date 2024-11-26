# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.013x faster
- HPT reliability: 81.65%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 293 ms                                                       | 291 ms: 1.00x faster                                             |
| chameleon      | 7.49 ms                                                      | 7.40 ms: 1.01x faster                                            |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                           |
| html5lib       | 72.9 ms                                                      | 74.7 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 458 ms                                                       | 421 ms: 1.09x faster                                             |
| async_tree_none           | 370 ms                                                       | 365 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 604 ms: 1.01x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                            |
| async_tree_memoization    | 447 ms                                                       | 460 ms: 1.03x slower                                             |
| async_tree_io             | 832 ms                                                       | 873 ms: 1.05x slower                                             |
| async_tree_io_tg          | 823 ms                                                       | 900 ms: 1.09x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_generators, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 92.1 ms                                                      | 87.8 ms: 1.05x faster                                            |
| float          | 81.6 ms                                                      | 80.2 ms: 1.02x faster                                            |
| pidigits       | 252 ms                                                       | 254 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                      | 3.40 ms: 1.03x faster                                            |
| regex_compile  | 143 ms                                                       | 144 ms: 1.01x slower                                             |
| regex_v8       | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| regex_dna      | 238 ms                                                       | 249 ms: 1.05x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 322 us                                                       | 307 us: 1.05x faster                                             |
| xml_etree_process    | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                            |
| tomli_loads          | 2.43 sec                                                     | 2.40 sec: 1.01x faster                                           |
| json_dumps           | 10.8 ms                                                      | 10.8 ms: 1.00x faster                                            |
| xml_etree_generate   | 85.2 ms                                                      | 85.7 ms: 1.01x slower                                            |
| json_loads           | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| xml_etree_iterparse  | 99.8 ms                                                      | 103 ms: 1.03x slower                                             |
| unpickle_pure_python | 216 us                                                       | 224 us: 1.04x slower                                             |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 15.6 ms                                                      | 13.2 ms: 1.18x faster                                            |
| python_startup_no_site | 8.93 ms                                                      | 8.85 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.09x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (3): genshi_xml, django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                     | 1.02 sec                                                     | 764 ms: 1.34x faster                                             |
| create_gc_cycles          | 2.65 ms                                                      | 2.00 ms: 1.32x faster                                            |
| python_startup            | 15.6 ms                                                      | 13.2 ms: 1.18x faster                                            |
| fannkuch                  | 384 ms                                                       | 353 ms: 1.09x faster                                             |
| async_tree_memoization_tg | 458 ms                                                       | 421 ms: 1.09x faster                                             |
| scimark_sor               | 125 ms                                                       | 119 ms: 1.05x faster                                             |
| json                      | 5.62 ms                                                      | 5.35 ms: 1.05x faster                                            |
| genshi_text               | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                            |
| nbody                     | 92.1 ms                                                      | 87.8 ms: 1.05x faster                                            |
| pycparser                 | 1.28 sec                                                     | 1.22 sec: 1.05x faster                                           |
| pickle_pure_python        | 322 us                                                       | 307 us: 1.05x faster                                             |
| telco                     | 8.77 ms                                                      | 8.40 ms: 1.04x faster                                            |
| nqueens                   | 92.3 ms                                                      | 88.4 ms: 1.04x faster                                            |
| thrift                    | 918 us                                                       | 880 us: 1.04x faster                                             |
| deepcopy_memo             | 38.9 us                                                      | 37.3 us: 1.04x faster                                            |
| regex_effbot              | 3.51 ms                                                      | 3.40 ms: 1.03x faster                                            |
| deepcopy_reduce           | 3.49 us                                                      | 3.39 us: 1.03x faster                                            |
| deepcopy                  | 388 us                                                       | 377 us: 1.03x faster                                             |
| typing_runtime_protocols  | 176 us                                                       | 171 us: 1.03x faster                                             |
| raytrace                  | 267 ms                                                       | 260 ms: 1.03x faster                                             |
| mdp                       | 2.53 sec                                                     | 2.46 sec: 1.03x faster                                           |
| pprint_pformat            | 1.70 sec                                                     | 1.66 sec: 1.02x faster                                           |
| bench_thread_pool         | 929 us                                                       | 908 us: 1.02x faster                                             |
| pyflate                   | 493 ms                                                       | 482 ms: 1.02x faster                                             |
| pprint_safe_repr          | 835 ms                                                       | 818 ms: 1.02x faster                                             |
| comprehensions            | 17.3 us                                                      | 17.0 us: 1.02x faster                                            |
| hexiom                    | 6.47 ms                                                      | 6.35 ms: 1.02x faster                                            |
| float                     | 81.6 ms                                                      | 80.2 ms: 1.02x faster                                            |
| pathlib                   | 17.4 ms                                                      | 17.1 ms: 1.02x faster                                            |
| meteor_contest            | 130 ms                                                       | 128 ms: 1.02x faster                                             |
| xml_etree_process         | 60.7 ms                                                      | 59.7 ms: 1.02x faster                                            |
| chaos                     | 60.6 ms                                                      | 59.6 ms: 1.02x faster                                            |
| async_tree_none           | 370 ms                                                       | 365 ms: 1.01x faster                                             |
| chameleon                 | 7.49 ms                                                      | 7.40 ms: 1.01x faster                                            |
| coverage                  | 84.5 ms                                                      | 83.5 ms: 1.01x faster                                            |
| tomli_loads               | 2.43 sec                                                     | 2.40 sec: 1.01x faster                                           |
| logging_silent            | 97.5 ns                                                      | 96.3 ns: 1.01x faster                                            |
| go                        | 167 ms                                                       | 165 ms: 1.01x faster                                             |
| generators                | 33.9 ms                                                      | 33.5 ms: 1.01x faster                                            |
| sympy_expand              | 506 ms                                                       | 501 ms: 1.01x faster                                             |
| sympy_integrate           | 23.4 ms                                                      | 23.2 ms: 1.01x faster                                            |
| python_startup_no_site    | 8.93 ms                                                      | 8.85 ms: 1.01x faster                                            |
| sympy_str                 | 297 ms                                                       | 295 ms: 1.01x faster                                             |
| json_dumps                | 10.8 ms                                                      | 10.8 ms: 1.00x faster                                            |
| 2to3                      | 293 ms                                                       | 291 ms: 1.00x faster                                             |
| scimark_monte_carlo       | 65.2 ms                                                      | 65.5 ms: 1.00x slower                                            |
| pidigits                  | 252 ms                                                       | 254 ms: 1.01x slower                                             |
| xml_etree_generate        | 85.2 ms                                                      | 85.7 ms: 1.01x slower                                            |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                             |
| bpe_tokeniser             | 5.09 sec                                                     | 5.14 sec: 1.01x slower                                           |
| regex_compile             | 143 ms                                                       | 144 ms: 1.01x slower                                             |
| sqlglot_normalize         | 119 ms                                                       | 120 ms: 1.01x slower                                             |
| json_loads                | 24.7 us                                                      | 25.0 us: 1.01x slower                                            |
| async_tree_cpu_io_mixed   | 596 ms                                                       | 604 ms: 1.01x slower                                             |
| sqlglot_optimize          | 58.7 ms                                                      | 59.5 ms: 1.02x slower                                            |
| scimark_sparse_mat_mult   | 4.21 ms                                                      | 4.28 ms: 1.02x slower                                            |
| richards_super            | 60.2 ms                                                      | 61.2 ms: 1.02x slower                                            |
| richards                  | 52.5 ms                                                      | 53.4 ms: 1.02x slower                                            |
| sqlglot_parse             | 1.37 ms                                                      | 1.39 ms: 1.02x slower                                            |
| coroutines                | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                            |
| logging_simple            | 6.28 us                                                      | 6.40 us: 1.02x slower                                            |
| logging_format            | 6.95 us                                                      | 7.11 us: 1.02x slower                                            |
| html5lib                  | 72.9 ms                                                      | 74.7 ms: 1.02x slower                                            |
| xml_etree_iterparse       | 99.8 ms                                                      | 103 ms: 1.03x slower                                             |
| dulwich_log               | 65.5 ms                                                      | 67.3 ms: 1.03x slower                                            |
| async_tree_memoization    | 447 ms                                                       | 460 ms: 1.03x slower                                             |
| unpickle_pure_python      | 216 us                                                       | 224 us: 1.04x slower                                             |
| regex_v8                  | 24.9 ms                                                      | 26.0 ms: 1.04x slower                                            |
| gc_traversal              | 4.48 ms                                                      | 4.69 ms: 1.05x slower                                            |
| regex_dna                 | 238 ms                                                       | 249 ms: 1.05x slower                                             |
| scimark_fft               | 298 ms                                                       | 312 ms: 1.05x slower                                             |
| async_tree_io             | 832 ms                                                       | 873 ms: 1.05x slower                                             |
| docutils                  | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                           |
| async_tree_io_tg          | 823 ms                                                       | 900 ms: 1.09x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (16): pylint, async_tree_none_tg, deltablue, async_tree_cpu_io_mixed_tg, async_generators, spectral_norm, asyncio_websockets, xml_etree_parse, genshi_xml, crypto_pyaes, scimark_lu, sqlglot_transpile, django_template, tornado_http, mako, bench_mp_pool
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: connected_components, gevent_hub, k_core, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.013x faster
# HPT report

- Reliability score: 81.65% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.91x