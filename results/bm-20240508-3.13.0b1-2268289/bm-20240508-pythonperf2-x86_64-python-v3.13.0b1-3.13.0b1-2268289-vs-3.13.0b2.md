# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 290 ms: 1.01x faster                                             |
| chameleon      | 7.40 ms                                                          | 7.66 ms: 1.04x slower                                            |
| docutils       | 2.98 sec                                                         | 3.03 sec: 1.01x slower                                           |
| html5lib       | 74.7 ms                                                          | 75.9 ms: 1.02x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none           | 365 ms                                                           | 371 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 619 ms: 1.02x slower                                             |
| async_tree_memoization_tg | 421 ms                                                           | 444 ms: 1.06x slower                                             |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                     |

Benchmark hidden because not significant (5): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                             |
| float          | 80.2 ms                                                          | 81.1 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 243 ms: 1.03x faster                                             |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                            |
| regex_compile  | 144 ms                                                           | 147 ms: 1.02x slower                                             |
| regex_effbot   | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.8 us                                                          | 31.2 us: 1.05x faster                                            |
| json_loads           | 25.0 us                                                          | 24.4 us: 1.02x faster                                            |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                            |
| unpickle             | 15.7 us                                                          | 15.5 us: 1.01x faster                                            |
| unpickle_pure_python | 224 us                                                           | 222 us: 1.01x faster                                             |
| pickle_list          | 4.44 us                                                          | 4.49 us: 1.01x slower                                            |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                            |
| unpickle_list        | 4.70 us                                                          | 4.75 us: 1.01x slower                                            |
| xml_etree_process    | 59.7 ms                                                          | 60.6 ms: 1.01x slower                                            |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.03x slower                                             |
| xml_etree_generate   | 85.7 ms                                                          | 88.9 ms: 1.04x slower                                            |
| tomli_loads          | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                           |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 8.86 ms: 1.00x slower                                            |
| Geometric mean         | (ref)                                                            | 1.01x faster                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                            |
| genshi_text     | 25.9 ms                                                          | 26.2 ms: 1.01x slower                                            |
| django_template | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                            |
| Geometric mean  | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|---------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict               | 32.8 us                                                          | 31.2 us: 1.05x faster                                            |
| go                        | 165 ms                                                           | 160 ms: 1.03x faster                                             |
| regex_dna                 | 249 ms                                                           | 243 ms: 1.03x faster                                             |
| json_loads                | 25.0 us                                                          | 24.4 us: 1.02x faster                                            |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.19 ms: 1.02x faster                                            |
| pickle                    | 10.6 us                                                          | 10.4 us: 1.02x faster                                            |
| coroutines                | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                            |
| python_startup            | 13.2 ms                                                          | 12.9 ms: 1.02x faster                                            |
| regex_v8                  | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                            |
| scimark_sor               | 119 ms                                                           | 117 ms: 1.02x faster                                             |
| unpickle                  | 15.7 us                                                          | 15.5 us: 1.01x faster                                            |
| unpickle_pure_python      | 224 us                                                           | 222 us: 1.01x faster                                             |
| crypto_pyaes              | 73.6 ms                                                          | 72.9 ms: 1.01x faster                                            |
| generators                | 33.5 ms                                                          | 33.3 ms: 1.01x faster                                            |
| pidigits                  | 254 ms                                                           | 252 ms: 1.01x faster                                             |
| 2to3                      | 291 ms                                                           | 290 ms: 1.01x faster                                             |
| gc_traversal              | 4.69 ms                                                          | 4.66 ms: 1.00x faster                                            |
| chaos                     | 59.6 ms                                                          | 59.4 ms: 1.00x faster                                            |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                           |
| pyflate                   | 482 ms                                                           | 480 ms: 1.00x faster                                             |
| python_startup_no_site    | 8.85 ms                                                          | 8.86 ms: 1.00x slower                                            |
| spectral_norm             | 97.3 ms                                                          | 97.5 ms: 1.00x slower                                            |
| hexiom                    | 6.35 ms                                                          | 6.37 ms: 1.00x slower                                            |
| logging_silent            | 96.3 ns                                                          | 96.6 ns: 1.00x slower                                            |
| dulwich_log               | 67.3 ms                                                          | 67.6 ms: 1.00x slower                                            |
| asyncio_tcp               | 378 ms                                                           | 380 ms: 1.01x slower                                             |
| sqlglot_normalize         | 120 ms                                                           | 121 ms: 1.01x slower                                             |
| comprehensions            | 17.0 us                                                          | 17.1 us: 1.01x slower                                            |
| sqlglot_optimize          | 59.5 ms                                                          | 60.1 ms: 1.01x slower                                            |
| richards                  | 53.4 ms                                                          | 54.0 ms: 1.01x slower                                            |
| pickle_list               | 4.44 us                                                          | 4.49 us: 1.01x slower                                            |
| mako                      | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                            |
| async_generators          | 363 ms                                                           | 367 ms: 1.01x slower                                             |
| json_dumps                | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                            |
| float                     | 80.2 ms                                                          | 81.1 ms: 1.01x slower                                            |
| unpickle_list             | 4.70 us                                                          | 4.75 us: 1.01x slower                                            |
| pathlib                   | 17.1 ms                                                          | 17.3 ms: 1.01x slower                                            |
| genshi_text               | 25.9 ms                                                          | 26.2 ms: 1.01x slower                                            |
| django_template           | 39.0 ms                                                          | 39.5 ms: 1.01x slower                                            |
| sqlite_synth              | 2.80 us                                                          | 2.83 us: 1.01x slower                                            |
| dask                      | 391 ms                                                           | 396 ms: 1.01x slower                                             |
| sympy_sum                 | 155 ms                                                           | 157 ms: 1.01x slower                                             |
| xml_etree_process         | 59.7 ms                                                          | 60.6 ms: 1.01x slower                                            |
| docutils                  | 2.98 sec                                                         | 3.03 sec: 1.01x slower                                           |
| flaskblogging             | 4.68 ms                                                          | 4.75 ms: 1.01x slower                                            |
| logging_simple            | 6.40 us                                                          | 6.50 us: 1.02x slower                                            |
| mdp                       | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                           |
| pprint_safe_repr          | 818 ms                                                           | 830 ms: 1.02x slower                                             |
| async_tree_none           | 365 ms                                                           | 371 ms: 1.02x slower                                             |
| html5lib                  | 74.7 ms                                                          | 75.9 ms: 1.02x slower                                            |
| pprint_pformat            | 1.66 sec                                                         | 1.69 sec: 1.02x slower                                           |
| mypy2                     | 764 ms                                                           | 780 ms: 1.02x slower                                             |
| typing_runtime_protocols  | 171 us                                                           | 174 us: 1.02x slower                                             |
| regex_compile             | 144 ms                                                           | 147 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 619 ms: 1.02x slower                                             |
| sympy_str                 | 295 ms                                                           | 302 ms: 1.02x slower                                             |
| sympy_integrate           | 23.2 ms                                                          | 23.8 ms: 1.03x slower                                            |
| sympy_expand              | 501 ms                                                           | 514 ms: 1.03x slower                                             |
| deepcopy_reduce           | 3.39 us                                                          | 3.48 us: 1.03x slower                                            |
| raytrace                  | 260 ms                                                           | 268 ms: 1.03x slower                                             |
| nqueens                   | 88.4 ms                                                          | 91.1 ms: 1.03x slower                                            |
| meteor_contest            | 128 ms                                                           | 132 ms: 1.03x slower                                             |
| thrift                    | 880 us                                                           | 908 us: 1.03x slower                                             |
| pickle_pure_python        | 307 us                                                           | 318 us: 1.03x slower                                             |
| fannkuch                  | 353 ms                                                           | 365 ms: 1.03x slower                                             |
| chameleon                 | 7.40 ms                                                          | 7.66 ms: 1.04x slower                                            |
| sqlglot_parse             | 1.39 ms                                                          | 1.44 ms: 1.04x slower                                            |
| scimark_lu                | 97.5 ms                                                          | 101 ms: 1.04x slower                                             |
| xml_etree_generate        | 85.7 ms                                                          | 88.9 ms: 1.04x slower                                            |
| sqlglot_transpile         | 1.76 ms                                                          | 1.83 ms: 1.04x slower                                            |
| pycparser                 | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                           |
| regex_effbot              | 3.40 ms                                                          | 3.56 ms: 1.05x slower                                            |
| deepcopy                  | 377 us                                                           | 395 us: 1.05x slower                                             |
| scimark_fft               | 312 ms                                                           | 328 ms: 1.05x slower                                             |
| async_tree_memoization_tg | 421 ms                                                           | 444 ms: 1.06x slower                                             |
| deepcopy_memo             | 37.3 us                                                          | 39.4 us: 1.06x slower                                            |
| scimark_monte_carlo       | 65.5 ms                                                          | 69.5 ms: 1.06x slower                                            |
| tomli_loads               | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                           |
| telco                     | 8.40 ms                                                          | 175 ms: 20.80x slower                                            |
| Geometric mean            | (ref)                                                            | 1.04x slower                                                     |

Benchmark hidden because not significant (22): bench_mp_pool, bench_thread_pool, async_tree_io_tg, asyncio_websockets, genshi_xml, logging_format, richards_super, async_tree_io, gunicorn, json, coverage, xml_etree_parse, xml_etree_iterparse, deltablue, tornado_http, aiohttp, create_gc_cycles, async_tree_none_tg, async_tree_memoization, pylint, async_tree_cpu_io_mixed_tg, nbody
Ignored benchmarks (1) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.99x