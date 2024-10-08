# Results vs. 3.13.0b2

- fork: python
- ref: v3.13.0rc1
- machine: linux-x86_64
- commit hash: e4a3e78
- commit date: 2024-07-31
- overall geometric mean: 1.00x slower
- HPT reliability: 97.47%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                               |
| chameleon      | 7.40 ms                                                          | 7.33 ms: 1.01x faster                                              |
| html5lib       | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                              |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                            | 1.01x faster                                                       |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 911 ms: 1.01x slower                                               |
| async_tree_io             | 873 ms                                                           | 895 ms: 1.03x slower                                               |
| async_tree_memoization_tg | 421 ms                                                           | 440 ms: 1.05x slower                                               |
| Geometric mean            | (ref)                                                            | 1.02x slower                                                       |

Benchmark hidden because not significant (5): async_tree_none, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                               |
| nbody          | 87.8 ms                                                          | 92.0 ms: 1.05x slower                                              |
| Geometric mean | (ref)                                                            | 1.02x slower                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 245 ms: 1.02x faster                                               |
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                               |
| regex_effbot   | 3.40 ms                                                          | 3.39 ms: 1.00x faster                                              |
| regex_v8       | 26.0 ms                                                          | 26.4 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                            | 1.00x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.19 sec: 1.10x faster                                             |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                               |
| json_loads           | 25.0 us                                                          | 24.1 us: 1.04x faster                                              |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                               |
| xml_etree_generate   | 85.7 ms                                                          | 86.2 ms: 1.01x slower                                              |
| xml_etree_process    | 59.7 ms                                                          | 61.0 ms: 1.02x slower                                              |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                               |
| json_dumps           | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                              |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                       |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| python_startup_no_site | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                              |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                              |
| genshi_text     | 25.9 ms                                                          | 25.5 ms: 1.02x faster                                              |
| django_template | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                              |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                       |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240731-pythonperf2-x86_64-python-v3.13.0rc1-3.13.0rc1-e4a3e78 |
|---------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------------:|
| tomli_loads               | 2.40 sec                                                         | 2.19 sec: 1.10x faster                                             |
| genshi_xml                | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                              |
| richards_super            | 61.2 ms                                                          | 57.4 ms: 1.07x faster                                              |
| unpickle_pure_python      | 224 us                                                           | 213 us: 1.05x faster                                               |
| gc_traversal              | 4.69 ms                                                          | 4.45 ms: 1.05x faster                                              |
| richards                  | 53.4 ms                                                          | 50.9 ms: 1.05x faster                                              |
| dulwich_log               | 67.3 ms                                                          | 64.2 ms: 1.05x faster                                              |
| go                        | 165 ms                                                           | 158 ms: 1.05x faster                                               |
| coverage                  | 83.5 ms                                                          | 79.8 ms: 1.05x faster                                              |
| json_loads                | 25.0 us                                                          | 24.1 us: 1.04x faster                                              |
| coroutines                | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                              |
| json                      | 5.35 ms                                                          | 5.20 ms: 1.03x faster                                              |
| pyflate                   | 482 ms                                                           | 469 ms: 1.03x faster                                               |
| html5lib                  | 74.7 ms                                                          | 72.8 ms: 1.03x faster                                              |
| logging_format            | 7.11 us                                                          | 6.99 us: 1.02x faster                                              |
| genshi_text               | 25.9 ms                                                          | 25.5 ms: 1.02x faster                                              |
| regex_dna                 | 249 ms                                                           | 245 ms: 1.02x faster                                               |
| xml_etree_parse           | 144 ms                                                           | 141 ms: 1.02x faster                                               |
| asyncio_websockets        | 395 ms                                                           | 390 ms: 1.01x faster                                               |
| tornado_http              | 119 ms                                                           | 118 ms: 1.01x faster                                               |
| deltablue                 | 3.37 ms                                                          | 3.34 ms: 1.01x faster                                              |
| 2to3                      | 291 ms                                                           | 289 ms: 1.01x faster                                               |
| bpe_tokeniser             | 5.14 sec                                                         | 5.09 sec: 1.01x faster                                             |
| chameleon                 | 7.40 ms                                                          | 7.33 ms: 1.01x faster                                              |
| regex_compile             | 144 ms                                                           | 143 ms: 1.01x faster                                               |
| crypto_pyaes              | 73.6 ms                                                          | 73.1 ms: 1.01x faster                                              |
| regex_effbot              | 3.40 ms                                                          | 3.39 ms: 1.00x faster                                              |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                             |
| pidigits                  | 254 ms                                                           | 254 ms: 1.00x slower                                               |
| sqlglot_optimize          | 59.5 ms                                                          | 59.7 ms: 1.00x slower                                              |
| spectral_norm             | 97.3 ms                                                          | 97.6 ms: 1.00x slower                                              |
| pathlib                   | 17.1 ms                                                          | 17.2 ms: 1.00x slower                                              |
| xml_etree_generate        | 85.7 ms                                                          | 86.2 ms: 1.01x slower                                              |
| meteor_contest            | 128 ms                                                           | 129 ms: 1.01x slower                                               |
| sympy_sum                 | 155 ms                                                           | 156 ms: 1.01x slower                                               |
| hexiom                    | 6.35 ms                                                          | 6.40 ms: 1.01x slower                                              |
| python_startup            | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                              |
| chaos                     | 59.6 ms                                                          | 60.1 ms: 1.01x slower                                              |
| logging_simple            | 6.40 us                                                          | 6.46 us: 1.01x slower                                              |
| thrift                    | 880 us                                                           | 888 us: 1.01x slower                                               |
| django_template           | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                              |
| sympy_str                 | 295 ms                                                           | 298 ms: 1.01x slower                                               |
| sqlglot_normalize         | 120 ms                                                           | 121 ms: 1.01x slower                                               |
| fannkuch                  | 353 ms                                                           | 356 ms: 1.01x slower                                               |
| generators                | 33.5 ms                                                          | 33.9 ms: 1.01x slower                                              |
| sqlglot_parse             | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                              |
| async_tree_io_tg          | 900 ms                                                           | 911 ms: 1.01x slower                                               |
| sympy_integrate           | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                              |
| mdp                       | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                             |
| comprehensions            | 17.0 us                                                          | 17.2 us: 1.01x slower                                              |
| regex_v8                  | 26.0 ms                                                          | 26.4 ms: 1.01x slower                                              |
| sqlglot_transpile         | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                              |
| python_startup_no_site    | 8.85 ms                                                          | 8.98 ms: 1.01x slower                                              |
| sympy_expand              | 501 ms                                                           | 508 ms: 1.01x slower                                               |
| scimark_lu                | 97.5 ms                                                          | 99.0 ms: 1.02x slower                                              |
| pprint_pformat            | 1.66 sec                                                         | 1.69 sec: 1.02x slower                                             |
| pprint_safe_repr          | 818 ms                                                           | 831 ms: 1.02x slower                                               |
| logging_silent            | 96.3 ns                                                          | 97.9 ns: 1.02x slower                                              |
| typing_runtime_protocols  | 171 us                                                           | 174 us: 1.02x slower                                               |
| raytrace                  | 260 ms                                                           | 265 ms: 1.02x slower                                               |
| dask                      | 391 ms                                                           | 398 ms: 1.02x slower                                               |
| async_generators          | 363 ms                                                           | 370 ms: 1.02x slower                                               |
| xml_etree_process         | 59.7 ms                                                          | 61.0 ms: 1.02x slower                                              |
| deepcopy                  | 377 us                                                           | 385 us: 1.02x slower                                               |
| nqueens                   | 88.4 ms                                                          | 90.4 ms: 1.02x slower                                              |
| scimark_monte_carlo       | 65.5 ms                                                          | 67.0 ms: 1.02x slower                                              |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.38 ms: 1.02x slower                                              |
| async_tree_io             | 873 ms                                                           | 895 ms: 1.03x slower                                               |
| deepcopy_memo             | 37.3 us                                                          | 38.3 us: 1.03x slower                                              |
| pycparser                 | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                             |
| pickle_pure_python        | 307 us                                                           | 317 us: 1.03x slower                                               |
| deepcopy_reduce           | 3.39 us                                                          | 3.50 us: 1.03x slower                                              |
| json_dumps                | 10.8 ms                                                          | 11.2 ms: 1.04x slower                                              |
| async_tree_memoization_tg | 421 ms                                                           | 440 ms: 1.05x slower                                               |
| nbody                     | 87.8 ms                                                          | 92.0 ms: 1.05x slower                                              |
| scimark_sor               | 119 ms                                                           | 127 ms: 1.07x slower                                               |
| Geometric mean            | (ref)                                                            | 1.00x slower                                                       |

Benchmark hidden because not significant (17): bench_mp_pool, scimark_fft, asyncio_tcp, docutils, bench_thread_pool, float, create_gc_cycles, telco, xml_etree_iterparse, mypy2, async_tree_none, mako, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_none_tg, pylint
Ignored benchmarks (9) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 97.47% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x