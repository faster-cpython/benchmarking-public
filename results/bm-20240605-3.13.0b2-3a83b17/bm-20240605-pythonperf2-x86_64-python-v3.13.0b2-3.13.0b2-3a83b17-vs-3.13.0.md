# Results vs. 3.13.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.00x faster
- HPT reliability: 75.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 291 ms: 1.00x slower                                             |
| chameleon      | 7.42 ms                                                      | 7.40 ms: 1.00x faster                                            |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                           |
| html5lib       | 71.9 ms                                                      | 74.7 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg | 461 ms                                                       | 421 ms: 1.10x faster                                             |
| async_tree_none           | 372 ms                                                       | 365 ms: 1.02x faster                                             |
| asyncio_tcp               | 380 ms                                                       | 378 ms: 1.01x faster                                             |
| async_generators          | 359 ms                                                       | 363 ms: 1.01x slower                                             |
| coroutines                | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                            |
| async_tree_io             | 847 ms                                                       | 873 ms: 1.03x slower                                             |
| asyncio_websockets        | 382 ms                                                       | 395 ms: 1.03x slower                                             |
| async_tree_io_tg          | 819 ms                                                       | 900 ms: 1.10x slower                                             |
| Geometric mean            | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, asyncio_tcp_ssl, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 80.2 ms: 1.02x faster                                            |
| pidigits       | 253 ms                                                       | 254 ms: 1.00x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| regex_effbot   | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                            |
| regex_dna      | 244 ms                                                       | 249 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                             |
| pickle_list          | 4.59 us                                                      | 4.44 us: 1.03x faster                                            |
| xml_etree_process    | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                            |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                            |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                             |
| xml_etree_generate   | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                            |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| unpickle_list        | 4.62 us                                                      | 4.70 us: 1.02x slower                                            |
| pickle_dict          | 32.1 us                                                      | 32.8 us: 1.02x slower                                            |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.02x slower                                             |
| unpickle             | 15.1 us                                                      | 15.7 us: 1.04x slower                                            |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| unpickle_pure_python | 214 us                                                       | 224 us: 1.05x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 8.85 ms: 1.01x faster                                            |
| python_startup         | 13.3 ms                                                      | 13.2 ms: 1.01x faster                                            |
| Geometric mean         | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                            |
| genshi_xml     | 57.3 ms                                                      | 58.1 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (2): mako, django_template

All benchmarks:
===============

| Benchmark                 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|---------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mypy2                     | 1.05 sec                                                     | 764 ms: 1.37x faster                                             |
| raytrace                  | 289 ms                                                       | 260 ms: 1.11x faster                                             |
| async_tree_memoization_tg | 461 ms                                                       | 421 ms: 1.10x faster                                             |
| scimark_sor               | 126 ms                                                       | 119 ms: 1.06x faster                                             |
| deepcopy_memo             | 39.5 us                                                      | 37.3 us: 1.06x faster                                            |
| deepcopy                  | 397 us                                                       | 377 us: 1.05x faster                                             |
| deepcopy_reduce           | 3.54 us                                                      | 3.39 us: 1.04x faster                                            |
| pickle_pure_python        | 318 us                                                       | 307 us: 1.04x faster                                             |
| chaos                     | 61.7 ms                                                      | 59.6 ms: 1.03x faster                                            |
| fannkuch                  | 365 ms                                                       | 353 ms: 1.03x faster                                             |
| pickle_list               | 4.59 us                                                      | 4.44 us: 1.03x faster                                            |
| pycparser                 | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                           |
| genshi_text               | 26.6 ms                                                      | 25.9 ms: 1.03x faster                                            |
| mdp                       | 2.52 sec                                                     | 2.46 sec: 1.03x faster                                           |
| telco                     | 8.58 ms                                                      | 8.40 ms: 1.02x faster                                            |
| float                     | 81.9 ms                                                      | 80.2 ms: 1.02x faster                                            |
| pyflate                   | 492 ms                                                       | 482 ms: 1.02x faster                                             |
| typing_runtime_protocols  | 174 us                                                       | 171 us: 1.02x faster                                             |
| xml_etree_process         | 60.9 ms                                                      | 59.7 ms: 1.02x faster                                            |
| async_tree_none           | 372 ms                                                       | 365 ms: 1.02x faster                                             |
| comprehensions            | 17.3 us                                                      | 17.0 us: 1.02x faster                                            |
| pathlib                   | 17.4 ms                                                      | 17.1 ms: 1.02x faster                                            |
| json_dumps                | 11.0 ms                                                      | 10.8 ms: 1.02x faster                                            |
| logging_silent            | 97.7 ns                                                      | 96.3 ns: 1.01x faster                                            |
| python_startup_no_site    | 8.94 ms                                                      | 8.85 ms: 1.01x faster                                            |
| deltablue                 | 3.41 ms                                                      | 3.37 ms: 1.01x faster                                            |
| sqlglot_transpile         | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                            |
| python_startup            | 13.3 ms                                                      | 13.2 ms: 1.01x faster                                            |
| xml_etree_parse           | 145 ms                                                       | 144 ms: 1.01x faster                                             |
| sympy_expand              | 505 ms                                                       | 501 ms: 1.01x faster                                             |
| regex_v8                  | 26.2 ms                                                      | 26.0 ms: 1.01x faster                                            |
| sympy_integrate           | 23.3 ms                                                      | 23.2 ms: 1.01x faster                                            |
| asyncio_tcp               | 380 ms                                                       | 378 ms: 1.01x faster                                             |
| sympy_str                 | 296 ms                                                       | 295 ms: 1.00x faster                                             |
| chameleon                 | 7.42 ms                                                      | 7.40 ms: 1.00x faster                                            |
| meteor_contest            | 128 ms                                                       | 128 ms: 1.00x faster                                             |
| 2to3                      | 291 ms                                                       | 291 ms: 1.00x slower                                             |
| hexiom                    | 6.33 ms                                                      | 6.35 ms: 1.00x slower                                            |
| pidigits                  | 253 ms                                                       | 254 ms: 1.00x slower                                             |
| xml_etree_generate        | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                            |
| pprint_pformat            | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                           |
| sympy_sum                 | 154 ms                                                       | 155 ms: 1.01x slower                                             |
| pprint_safe_repr          | 812 ms                                                       | 818 ms: 1.01x slower                                             |
| pickle                    | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| bpe_tokeniser             | 5.10 sec                                                     | 5.14 sec: 1.01x slower                                           |
| sqlglot_parse             | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| scimark_monte_carlo       | 64.9 ms                                                      | 65.5 ms: 1.01x slower                                            |
| regex_effbot              | 3.37 ms                                                      | 3.40 ms: 1.01x slower                                            |
| async_generators          | 359 ms                                                       | 363 ms: 1.01x slower                                             |
| crypto_pyaes              | 72.8 ms                                                      | 73.6 ms: 1.01x slower                                            |
| genshi_xml                | 57.3 ms                                                      | 58.1 ms: 1.01x slower                                            |
| richards                  | 52.7 ms                                                      | 53.4 ms: 1.01x slower                                            |
| flaskblogging             | 4.62 ms                                                      | 4.68 ms: 1.01x slower                                            |
| sqlglot_normalize         | 118 ms                                                       | 120 ms: 1.02x slower                                             |
| unpickle_list             | 4.62 us                                                      | 4.70 us: 1.02x slower                                            |
| coroutines                | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                            |
| regex_dna                 | 244 ms                                                       | 249 ms: 1.02x slower                                             |
| richards_super            | 59.8 ms                                                      | 61.2 ms: 1.02x slower                                            |
| pickle_dict               | 32.1 us                                                      | 32.8 us: 1.02x slower                                            |
| json                      | 5.22 ms                                                      | 5.35 ms: 1.02x slower                                            |
| xml_etree_iterparse       | 100 ms                                                       | 103 ms: 1.02x slower                                             |
| dulwich_log               | 65.5 ms                                                      | 67.3 ms: 1.03x slower                                            |
| go                        | 160 ms                                                       | 165 ms: 1.03x slower                                             |
| coverage                  | 81.1 ms                                                      | 83.5 ms: 1.03x slower                                            |
| dask                      | 379 ms                                                       | 391 ms: 1.03x slower                                             |
| async_tree_io             | 847 ms                                                       | 873 ms: 1.03x slower                                             |
| asyncio_websockets        | 382 ms                                                       | 395 ms: 1.03x slower                                             |
| unpickle                  | 15.1 us                                                      | 15.7 us: 1.04x slower                                            |
| html5lib                  | 71.9 ms                                                      | 74.7 ms: 1.04x slower                                            |
| json_loads                | 24.0 us                                                      | 25.0 us: 1.04x slower                                            |
| unpickle_pure_python      | 214 us                                                       | 224 us: 1.05x slower                                             |
| bench_mp_pool             | 4.65 ms                                                      | 4.91 ms: 1.05x slower                                            |
| docutils                  | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                           |
| async_tree_io_tg          | 819 ms                                                       | 900 ms: 1.10x slower                                             |
| create_gc_cycles          | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                            |
| gc_traversal              | 4.11 ms                                                      | 4.69 ms: 1.14x slower                                            |
| Geometric mean            | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (26): pylint, scimark_fft, mako, scimark_lu, async_tree_cpu_io_mixed_tg, tornado_http, sqlglot_optimize, nbody, regex_compile, scimark_sparse_mat_mult, tomli_loads, spectral_norm, asyncio_tcp_ssl, logging_simple, generators, nqueens, async_tree_none_tg, django_template, thrift, sqlite_synth, aiohttp, logging_format, gunicorn, async_tree_cpu_io_mixed, bench_thread_pool, async_tree_memoization
Ignored benchmarks (1) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: unpack_sequence

# HPT report

- Reliability score: 75.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x