# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0a1
- machine: linux-x86_64
- commit hash: ad056f0
- commit date: 2023-10-13
- overall geometric mean: 1.03x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 297 ms: 1.02x slower                                             |
| chameleon      | 7.40 ms                                                          | 7.78 ms: 1.05x slower                                            |
| docutils       | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                           |
| tornado_http   | 119 ms                                                           | 121 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 713 ms: 1.18x slower                                             |
| async_tree_none            | 365 ms                                                           | 439 ms: 1.20x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 557 ms: 1.21x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.11 sec: 1.23x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.09 sec: 1.25x slower                                           |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 727 ms: 1.27x slower                                             |
| async_tree_none_tg         | 340 ms                                                           | 447 ms: 1.31x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 571 ms: 1.36x slower                                             |
| Geometric mean             | (ref)                                                            | 1.25x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 81.5 ms: 1.02x slower                                            |
| pidigits       | 254 ms                                                           | 264 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                            | 1.02x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 241 ms: 1.04x faster                                             |
| regex_compile  | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| regex_effbot   | 3.40 ms                                                          | 3.55 ms: 1.04x slower                                            |
| Geometric mean | (ref)                                                            | 1.01x slower                                                     |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 14.3 us: 1.10x faster                                            |
| tomli_loads          | 2.40 sec                                                         | 2.24 sec: 1.07x faster                                           |
| pickle               | 10.6 us                                                          | 10.1 us: 1.05x faster                                            |
| json_loads           | 25.0 us                                                          | 24.3 us: 1.03x faster                                            |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                             |
| unpickle_list        | 4.70 us                                                          | 4.61 us: 1.02x faster                                            |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                            |
| xml_etree_generate   | 85.7 ms                                                          | 87.3 ms: 1.02x slower                                            |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                             |
| xml_etree_parse      | 144 ms                                                           | 152 ms: 1.06x slower                                             |
| xml_etree_iterparse  | 103 ms                                                           | 110 ms: 1.08x slower                                             |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                     |

Benchmark hidden because not significant (3): pickle_list, pickle_dict, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 12.6 ms: 1.04x faster                                            |
| python_startup_no_site | 8.85 ms                                                          | 8.70 ms: 1.02x faster                                            |
| Geometric mean         | (ref)                                                            | 1.03x faster                                                     |

Benchmarks with tag 'template':
===============================

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 2.00 ms                                                          | 1.58 ms: 1.27x faster                                            |
| gc_traversal               | 4.69 ms                                                          | 3.95 ms: 1.19x faster                                            |
| typing_runtime_protocols   | 171 us                                                           | 155 us: 1.10x faster                                             |
| unpickle                   | 15.7 us                                                          | 14.3 us: 1.10x faster                                            |
| tomli_loads                | 2.40 sec                                                         | 2.24 sec: 1.07x faster                                           |
| spectral_norm              | 97.3 ms                                                          | 92.3 ms: 1.05x faster                                            |
| pickle                     | 10.6 us                                                          | 10.1 us: 1.05x faster                                            |
| json                       | 5.35 ms                                                          | 5.12 ms: 1.05x faster                                            |
| python_startup             | 13.2 ms                                                          | 12.6 ms: 1.04x faster                                            |
| docutils                   | 2.98 sec                                                         | 2.88 sec: 1.04x faster                                           |
| regex_dna                  | 249 ms                                                           | 241 ms: 1.04x faster                                             |
| sqlite_synth               | 2.80 us                                                          | 2.70 us: 1.03x faster                                            |
| sqlglot_normalize          | 120 ms                                                           | 117 ms: 1.03x faster                                             |
| asyncio_tcp                | 378 ms                                                           | 367 ms: 1.03x faster                                             |
| json_loads                 | 25.0 us                                                          | 24.3 us: 1.03x faster                                            |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                             |
| unpickle_list              | 4.70 us                                                          | 4.61 us: 1.02x faster                                            |
| telco                      | 8.40 ms                                                          | 8.25 ms: 1.02x faster                                            |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                            |
| python_startup_no_site     | 8.85 ms                                                          | 8.70 ms: 1.02x faster                                            |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                             |
| sympy_expand               | 501 ms                                                           | 494 ms: 1.01x faster                                             |
| sqlglot_optimize           | 59.5 ms                                                          | 58.8 ms: 1.01x faster                                            |
| richards_super             | 61.2 ms                                                          | 61.7 ms: 1.01x slower                                            |
| nqueens                    | 88.4 ms                                                          | 89.2 ms: 1.01x slower                                            |
| pprint_safe_repr           | 818 ms                                                           | 829 ms: 1.01x slower                                             |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.34 ms: 1.01x slower                                            |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                           |
| tornado_http               | 119 ms                                                           | 121 ms: 1.02x slower                                             |
| float                      | 80.2 ms                                                          | 81.5 ms: 1.02x slower                                            |
| xml_etree_generate         | 85.7 ms                                                          | 87.3 ms: 1.02x slower                                            |
| 2to3                       | 291 ms                                                           | 297 ms: 1.02x slower                                             |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                             |
| logging_silent             | 96.3 ns                                                          | 98.3 ns: 1.02x slower                                            |
| pickle_pure_python         | 307 us                                                           | 314 us: 1.02x slower                                             |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                            |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                           |
| dulwich_log                | 67.3 ms                                                          | 69.2 ms: 1.03x slower                                            |
| coroutines                 | 22.0 ms                                                          | 22.6 ms: 1.03x slower                                            |
| hexiom                     | 6.35 ms                                                          | 6.54 ms: 1.03x slower                                            |
| deepcopy_memo              | 37.3 us                                                          | 38.6 us: 1.03x slower                                            |
| richards                   | 53.4 ms                                                          | 55.4 ms: 1.04x slower                                            |
| sqlglot_transpile          | 1.76 ms                                                          | 1.83 ms: 1.04x slower                                            |
| sympy_sum                  | 155 ms                                                           | 161 ms: 1.04x slower                                             |
| sympy_str                  | 295 ms                                                           | 307 ms: 1.04x slower                                             |
| pidigits                   | 254 ms                                                           | 264 ms: 1.04x slower                                             |
| regex_compile              | 144 ms                                                           | 150 ms: 1.04x slower                                             |
| go                         | 165 ms                                                           | 172 ms: 1.04x slower                                             |
| regex_effbot               | 3.40 ms                                                          | 3.55 ms: 1.04x slower                                            |
| sympy_integrate            | 23.2 ms                                                          | 24.2 ms: 1.05x slower                                            |
| logging_format             | 7.11 us                                                          | 7.44 us: 1.05x slower                                            |
| chameleon                  | 7.40 ms                                                          | 7.78 ms: 1.05x slower                                            |
| chaos                      | 59.6 ms                                                          | 62.7 ms: 1.05x slower                                            |
| scimark_lu                 | 97.5 ms                                                          | 103 ms: 1.05x slower                                             |
| generators                 | 33.5 ms                                                          | 35.4 ms: 1.05x slower                                            |
| bench_thread_pool          | 908 us                                                           | 961 us: 1.06x slower                                             |
| raytrace                   | 260 ms                                                           | 276 ms: 1.06x slower                                             |
| xml_etree_parse            | 144 ms                                                           | 152 ms: 1.06x slower                                             |
| logging_simple             | 6.40 us                                                          | 6.79 us: 1.06x slower                                            |
| pyflate                    | 482 ms                                                           | 513 ms: 1.07x slower                                             |
| xml_etree_iterparse        | 103 ms                                                           | 110 ms: 1.08x slower                                             |
| deltablue                  | 3.37 ms                                                          | 3.66 ms: 1.08x slower                                            |
| scimark_monte_carlo        | 65.5 ms                                                          | 71.0 ms: 1.08x slower                                            |
| pycparser                  | 1.22 sec                                                         | 1.33 sec: 1.09x slower                                           |
| async_generators           | 363 ms                                                           | 399 ms: 1.10x slower                                             |
| fannkuch                   | 353 ms                                                           | 396 ms: 1.12x slower                                             |
| pathlib                    | 17.1 ms                                                          | 19.3 ms: 1.13x slower                                            |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 713 ms: 1.18x slower                                             |
| async_tree_none            | 365 ms                                                           | 439 ms: 1.20x slower                                             |
| async_tree_memoization     | 460 ms                                                           | 557 ms: 1.21x slower                                             |
| async_tree_io_tg           | 900 ms                                                           | 1.11 sec: 1.23x slower                                           |
| async_tree_io              | 873 ms                                                           | 1.09 sec: 1.25x slower                                           |
| scimark_sor                | 119 ms                                                           | 149 ms: 1.26x slower                                             |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 727 ms: 1.27x slower                                             |
| comprehensions             | 17.0 us                                                          | 21.5 us: 1.27x slower                                            |
| async_tree_none_tg         | 340 ms                                                           | 447 ms: 1.31x slower                                             |
| async_tree_memoization_tg  | 421 ms                                                           | 571 ms: 1.36x slower                                             |
| Geometric mean             | (ref)                                                            | 1.03x slower                                                     |

Benchmark hidden because not significant (13): bench_mp_pool, crypto_pyaes, nbody, mako, asyncio_tcp_ssl, deepcopy_reduce, coverage, pickle_list, pickle_dict, xml_etree_process, deepcopy, regex_v8, scimark_fft
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, bpe_tokeniser, dask, django_template, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, mypy2, pylint, thrift
Ignored benchmarks (1) of results/bm-20231013-3.13.0a1-ad056f0/bm-20231013-pythonperf2-x86_64-python-v3.13.0a1-3.13.0a1-ad056f0.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x

# Memory
- memory change: 0.94x