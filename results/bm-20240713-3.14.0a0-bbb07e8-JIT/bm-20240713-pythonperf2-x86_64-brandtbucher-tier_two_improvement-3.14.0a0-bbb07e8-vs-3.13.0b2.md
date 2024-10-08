# Results vs. 3.13.0b2

- fork: brandtbucher
- ref: tier_two_improvement
- machine: linux-x86_64
- commit hash: bbb07e8
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 88.43%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                              |
| docutils       | 2.98 sec                                                         | 3.08 sec: 1.03x slower                                                            |
| html5lib       | 74.7 ms                                                          | 70.4 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                      |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 776 ms: 1.16x faster                                                              |
| async_tree_memoization     | 460 ms                                                           | 407 ms: 1.13x faster                                                              |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                              |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                              |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                              |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                              |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 538 ms: 1.06x faster                                                              |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 581 ms: 1.04x faster                                                              |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 74.1 ms: 1.08x faster                                                             |
| nbody          | 87.8 ms                                                          | 83.7 ms: 1.05x faster                                                             |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 135 ms: 1.07x faster                                                              |
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                              |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                             |
| regex_effbot   | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                            |
| unpickle_pure_python | 224 us                                                           | 211 us: 1.06x faster                                                              |
| xml_etree_generate   | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                             |
| xml_etree_iterparse  | 103 ms                                                           | 99.4 ms: 1.03x faster                                                             |
| xml_etree_process    | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                             |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                              |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                             |
| pickle_pure_python   | 307 us                                                           | 315 us: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                             |
| python_startup_no_site | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                             |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                             |
| django_template | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                             |
| genshi_xml      | 58.1 ms                                                          | 61.9 ms: 1.07x slower                                                             |
| genshi_text     | 25.9 ms                                                          | 29.2 ms: 1.13x slower                                                             |
| Geometric mean  | (ref)                                                            | 1.03x slower                                                                      |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-brandtbucher-tier_two_improvement-3.14.0a0-bbb07e8 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 28.2 us: 1.32x faster                                                             |
| deepcopy                   | 377 us                                                           | 307 us: 1.23x faster                                                              |
| richards                   | 53.4 ms                                                          | 44.7 ms: 1.20x faster                                                             |
| spectral_norm              | 97.3 ms                                                          | 82.3 ms: 1.18x faster                                                             |
| richards_super             | 61.2 ms                                                          | 52.1 ms: 1.17x faster                                                             |
| async_tree_io_tg           | 900 ms                                                           | 776 ms: 1.16x faster                                                              |
| tomli_loads                | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                            |
| async_tree_memoization     | 460 ms                                                           | 407 ms: 1.13x faster                                                              |
| mako                       | 10.4 ms                                                          | 9.24 ms: 1.12x faster                                                             |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                              |
| deepcopy_reduce            | 3.39 us                                                          | 3.04 us: 1.11x faster                                                             |
| pyflate                    | 482 ms                                                           | 437 ms: 1.10x faster                                                              |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                              |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 3.92 ms: 1.09x faster                                                             |
| float                      | 80.2 ms                                                          | 74.1 ms: 1.08x faster                                                             |
| async_tree_none            | 365 ms                                                           | 338 ms: 1.08x faster                                                              |
| scimark_fft                | 312 ms                                                           | 290 ms: 1.08x faster                                                              |
| async_tree_io              | 873 ms                                                           | 813 ms: 1.07x faster                                                              |
| regex_compile              | 144 ms                                                           | 135 ms: 1.07x faster                                                              |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 538 ms: 1.06x faster                                                              |
| unpickle_pure_python       | 224 us                                                           | 211 us: 1.06x faster                                                              |
| html5lib                   | 74.7 ms                                                          | 70.4 ms: 1.06x faster                                                             |
| regex_dna                  | 249 ms                                                           | 235 ms: 1.06x faster                                                              |
| crypto_pyaes               | 73.6 ms                                                          | 69.7 ms: 1.06x faster                                                             |
| bpe_tokeniser              | 5.14 sec                                                         | 4.88 sec: 1.05x faster                                                            |
| pathlib                    | 17.1 ms                                                          | 16.3 ms: 1.05x faster                                                             |
| nbody                      | 87.8 ms                                                          | 83.7 ms: 1.05x faster                                                             |
| xml_etree_generate         | 85.7 ms                                                          | 81.8 ms: 1.05x faster                                                             |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 581 ms: 1.04x faster                                                              |
| create_gc_cycles           | 2.00 ms                                                          | 1.94 ms: 1.03x faster                                                             |
| telco                      | 8.40 ms                                                          | 8.14 ms: 1.03x faster                                                             |
| xml_etree_iterparse        | 103 ms                                                           | 99.4 ms: 1.03x faster                                                             |
| xml_etree_process          | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                             |
| dulwich_log                | 67.3 ms                                                          | 65.3 ms: 1.03x faster                                                             |
| coverage                   | 83.5 ms                                                          | 81.1 ms: 1.03x faster                                                             |
| fannkuch                   | 353 ms                                                           | 345 ms: 1.02x faster                                                              |
| pprint_safe_repr           | 818 ms                                                           | 800 ms: 1.02x faster                                                              |
| logging_format             | 7.11 us                                                          | 6.96 us: 1.02x faster                                                             |
| pprint_pformat             | 1.66 sec                                                         | 1.63 sec: 1.02x faster                                                            |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                             |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                              |
| asyncio_tcp                | 378 ms                                                           | 373 ms: 1.01x faster                                                              |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                              |
| logging_simple             | 6.40 us                                                          | 6.36 us: 1.01x faster                                                             |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.00x faster                                                              |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.7 ms: 1.00x slower                                                             |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                             |
| meteor_contest             | 128 ms                                                           | 130 ms: 1.01x slower                                                              |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                             |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.02x slower                                                             |
| json                       | 5.35 ms                                                          | 5.45 ms: 1.02x slower                                                             |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                            |
| pickle_pure_python         | 307 us                                                           | 315 us: 1.02x slower                                                              |
| regex_effbot               | 3.40 ms                                                          | 3.49 ms: 1.03x slower                                                             |
| python_startup_no_site     | 8.85 ms                                                          | 9.09 ms: 1.03x slower                                                             |
| thrift                     | 880 us                                                           | 906 us: 1.03x slower                                                              |
| sqlglot_transpile          | 1.76 ms                                                          | 1.82 ms: 1.03x slower                                                             |
| docutils                   | 2.98 sec                                                         | 3.08 sec: 1.03x slower                                                            |
| sympy_expand               | 501 ms                                                           | 519 ms: 1.04x slower                                                              |
| hexiom                     | 6.35 ms                                                          | 6.62 ms: 1.04x slower                                                             |
| sympy_str                  | 295 ms                                                           | 308 ms: 1.04x slower                                                              |
| django_template            | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                                             |
| sqlglot_optimize           | 59.5 ms                                                          | 62.4 ms: 1.05x slower                                                             |
| 2to3                       | 291 ms                                                           | 306 ms: 1.05x slower                                                              |
| async_generators           | 363 ms                                                           | 383 ms: 1.06x slower                                                              |
| mdp                        | 2.46 sec                                                         | 2.61 sec: 1.06x slower                                                            |
| sqlglot_normalize          | 120 ms                                                           | 128 ms: 1.06x slower                                                              |
| scimark_sor                | 119 ms                                                           | 126 ms: 1.06x slower                                                              |
| nqueens                    | 88.4 ms                                                          | 94.0 ms: 1.06x slower                                                             |
| genshi_xml                 | 58.1 ms                                                          | 61.9 ms: 1.07x slower                                                             |
| sympy_sum                  | 155 ms                                                           | 165 ms: 1.07x slower                                                              |
| typing_runtime_protocols   | 171 us                                                           | 182 us: 1.07x slower                                                              |
| generators                 | 33.5 ms                                                          | 36.0 ms: 1.07x slower                                                             |
| comprehensions             | 17.0 us                                                          | 18.3 us: 1.08x slower                                                             |
| deltablue                  | 3.37 ms                                                          | 3.64 ms: 1.08x slower                                                             |
| pylint                     | 339 ms                                                           | 368 ms: 1.08x slower                                                              |
| logging_silent             | 96.3 ns                                                          | 105 ns: 1.09x slower                                                              |
| chaos                      | 59.6 ms                                                          | 65.5 ms: 1.10x slower                                                             |
| sympy_integrate            | 23.2 ms                                                          | 25.5 ms: 1.10x slower                                                             |
| genshi_text                | 25.9 ms                                                          | 29.2 ms: 1.13x slower                                                             |
| raytrace                   | 260 ms                                                           | 295 ms: 1.13x slower                                                              |
| scimark_lu                 | 97.5 ms                                                          | 113 ms: 1.16x slower                                                              |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                      |

Benchmark hidden because not significant (9): bench_mp_pool, gc_traversal, asyncio_tcp_ssl, asyncio_websockets, json_loads, coroutines, dask, tornado_http, bench_thread_pool
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 88.43% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.06x