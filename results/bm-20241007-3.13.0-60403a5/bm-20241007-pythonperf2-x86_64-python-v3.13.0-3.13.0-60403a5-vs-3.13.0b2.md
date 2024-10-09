# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.00x slower
- HPT reliability: 68.76%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 291 ms: 1.00x faster                                         |
| chameleon      | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                        |
| docutils       | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                       |
| html5lib       | 74.7 ms                                                          | 71.9 ms: 1.04x faster                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 819 ms: 1.10x faster                                         |
| async_tree_io             | 873 ms                                                           | 847 ms: 1.03x faster                                         |
| async_tree_none           | 365 ms                                                           | 372 ms: 1.02x slower                                         |
| async_tree_memoization_tg | 421 ms                                                           | 461 ms: 1.10x slower                                         |
| Geometric mean            | (ref)                                                            | 1.00x faster                                                 |

Benchmark hidden because not significant (4): async_tree_memoization, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                         |
| float          | 80.2 ms                                                          | 81.9 ms: 1.02x slower                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 244 ms: 1.02x faster                                         |
| regex_effbot   | 3.40 ms                                                          | 3.37 ms: 1.01x faster                                        |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                         |
| json_loads           | 25.0 us                                                          | 24.0 us: 1.04x faster                                        |
| unpickle             | 15.7 us                                                          | 15.1 us: 1.04x faster                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                         |
| pickle_dict          | 32.8 us                                                          | 32.1 us: 1.02x faster                                        |
| unpickle_list        | 4.70 us                                                          | 4.62 us: 1.02x faster                                        |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                        |
| xml_etree_generate   | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                        |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                         |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                        |
| xml_etree_process    | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                        |
| pickle_list          | 4.44 us                                                          | 4.59 us: 1.03x slower                                        |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.04x slower                                         |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                        |
| python_startup_no_site | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                        |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 57.3 ms: 1.01x faster                                        |
| genshi_text    | 25.9 ms                                                          | 26.6 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                 |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal              | 4.69 ms                                                          | 4.11 ms: 1.14x faster                                        |
| create_gc_cycles          | 2.00 ms                                                          | 1.76 ms: 1.14x faster                                        |
| async_tree_io_tg          | 900 ms                                                           | 819 ms: 1.10x faster                                         |
| docutils                  | 2.98 sec                                                         | 2.81 sec: 1.06x faster                                       |
| bench_mp_pool             | 4.91 ms                                                          | 4.65 ms: 1.05x faster                                        |
| unpickle_pure_python      | 224 us                                                           | 214 us: 1.05x faster                                         |
| json_loads                | 25.0 us                                                          | 24.0 us: 1.04x faster                                        |
| html5lib                  | 74.7 ms                                                          | 71.9 ms: 1.04x faster                                        |
| unpickle                  | 15.7 us                                                          | 15.1 us: 1.04x faster                                        |
| asyncio_websockets        | 395 ms                                                           | 382 ms: 1.03x faster                                         |
| async_tree_io             | 873 ms                                                           | 847 ms: 1.03x faster                                         |
| dask                      | 391 ms                                                           | 379 ms: 1.03x faster                                         |
| coverage                  | 83.5 ms                                                          | 81.1 ms: 1.03x faster                                        |
| go                        | 165 ms                                                           | 160 ms: 1.03x faster                                         |
| dulwich_log               | 67.3 ms                                                          | 65.5 ms: 1.03x faster                                        |
| xml_etree_iterparse       | 103 ms                                                           | 100 ms: 1.02x faster                                         |
| json                      | 5.35 ms                                                          | 5.22 ms: 1.02x faster                                        |
| pickle_dict               | 32.8 us                                                          | 32.1 us: 1.02x faster                                        |
| richards_super            | 61.2 ms                                                          | 59.8 ms: 1.02x faster                                        |
| regex_dna                 | 249 ms                                                           | 244 ms: 1.02x faster                                         |
| coroutines                | 22.0 ms                                                          | 21.6 ms: 1.02x faster                                        |
| unpickle_list             | 4.70 us                                                          | 4.62 us: 1.02x faster                                        |
| sqlglot_normalize         | 120 ms                                                           | 118 ms: 1.02x faster                                         |
| flaskblogging             | 4.68 ms                                                          | 4.62 ms: 1.01x faster                                        |
| richards                  | 53.4 ms                                                          | 52.7 ms: 1.01x faster                                        |
| genshi_xml                | 58.1 ms                                                          | 57.3 ms: 1.01x faster                                        |
| crypto_pyaes              | 73.6 ms                                                          | 72.8 ms: 1.01x faster                                        |
| async_generators          | 363 ms                                                           | 359 ms: 1.01x faster                                         |
| regex_effbot              | 3.40 ms                                                          | 3.37 ms: 1.01x faster                                        |
| scimark_monte_carlo       | 65.5 ms                                                          | 64.9 ms: 1.01x faster                                        |
| sqlglot_parse             | 1.39 ms                                                          | 1.38 ms: 1.01x faster                                        |
| bpe_tokeniser             | 5.14 sec                                                         | 5.10 sec: 1.01x faster                                       |
| pickle                    | 10.6 us                                                          | 10.5 us: 1.01x faster                                        |
| pprint_safe_repr          | 818 ms                                                           | 812 ms: 1.01x faster                                         |
| sympy_sum                 | 155 ms                                                           | 154 ms: 1.01x faster                                         |
| pprint_pformat            | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                       |
| xml_etree_generate        | 85.7 ms                                                          | 85.3 ms: 1.00x faster                                        |
| pidigits                  | 254 ms                                                           | 253 ms: 1.00x faster                                         |
| hexiom                    | 6.35 ms                                                          | 6.33 ms: 1.00x faster                                        |
| 2to3                      | 291 ms                                                           | 291 ms: 1.00x faster                                         |
| meteor_contest            | 128 ms                                                           | 128 ms: 1.00x slower                                         |
| chameleon                 | 7.40 ms                                                          | 7.42 ms: 1.00x slower                                        |
| sympy_str                 | 295 ms                                                           | 296 ms: 1.00x slower                                         |
| asyncio_tcp               | 378 ms                                                           | 380 ms: 1.01x slower                                         |
| sympy_integrate           | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                        |
| regex_v8                  | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                        |
| sympy_expand              | 501 ms                                                           | 505 ms: 1.01x slower                                         |
| xml_etree_parse           | 144 ms                                                           | 145 ms: 1.01x slower                                         |
| python_startup            | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                        |
| sqlglot_transpile         | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                        |
| deltablue                 | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                        |
| python_startup_no_site    | 8.85 ms                                                          | 8.94 ms: 1.01x slower                                        |
| logging_silent            | 96.3 ns                                                          | 97.7 ns: 1.01x slower                                        |
| json_dumps                | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                        |
| pathlib                   | 17.1 ms                                                          | 17.4 ms: 1.02x slower                                        |
| comprehensions            | 17.0 us                                                          | 17.3 us: 1.02x slower                                        |
| async_tree_none           | 365 ms                                                           | 372 ms: 1.02x slower                                         |
| xml_etree_process         | 59.7 ms                                                          | 60.9 ms: 1.02x slower                                        |
| typing_runtime_protocols  | 171 us                                                           | 174 us: 1.02x slower                                         |
| pyflate                   | 482 ms                                                           | 492 ms: 1.02x slower                                         |
| float                     | 80.2 ms                                                          | 81.9 ms: 1.02x slower                                        |
| telco                     | 8.40 ms                                                          | 8.58 ms: 1.02x slower                                        |
| mdp                       | 2.46 sec                                                         | 2.52 sec: 1.03x slower                                       |
| genshi_text               | 25.9 ms                                                          | 26.6 ms: 1.03x slower                                        |
| pycparser                 | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                       |
| pickle_list               | 4.44 us                                                          | 4.59 us: 1.03x slower                                        |
| fannkuch                  | 353 ms                                                           | 365 ms: 1.03x slower                                         |
| chaos                     | 59.6 ms                                                          | 61.7 ms: 1.03x slower                                        |
| pickle_pure_python        | 307 us                                                           | 318 us: 1.04x slower                                         |
| deepcopy_reduce           | 3.39 us                                                          | 3.54 us: 1.04x slower                                        |
| deepcopy                  | 377 us                                                           | 397 us: 1.05x slower                                         |
| deepcopy_memo             | 37.3 us                                                          | 39.5 us: 1.06x slower                                        |
| scimark_sor               | 119 ms                                                           | 126 ms: 1.06x slower                                         |
| async_tree_memoization_tg | 421 ms                                                           | 461 ms: 1.10x slower                                         |
| raytrace                  | 260 ms                                                           | 289 ms: 1.11x slower                                         |
| mypy2                     | 764 ms                                                           | 1.05 sec: 1.37x slower                                       |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                 |

Benchmark hidden because not significant (26): async_tree_memoization, bench_thread_pool, async_tree_cpu_io_mixed, gunicorn, logging_format, aiohttp, sqlite_synth, thrift, django_template, async_tree_none_tg, nqueens, generators, logging_simple, asyncio_tcp_ssl, spectral_norm, tomli_loads, scimark_sparse_mat_mult, regex_compile, nbody, sqlglot_optimize, tornado_http, async_tree_cpu_io_mixed_tg, scimark_lu, mako, scimark_fft, pylint
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 68.76% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x