# Results vs. 3.13.0b2

- fork: bdraco
- ref: speed_up_async_sched
- machine: linux-x86_64
- commit hash: f78838c
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.01x faster                                                      |
| html5lib       | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 775 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 558 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 827 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 550 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.06x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| xml_etree_process    | 59.7 ms                                                          | 60.8 ms: 1.02x slower                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 87.4 ms: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 54.3 ms: 1.07x faster                                                       |
| genshi_text    | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-bdraco-speed_up_async_sched-3.14.0a0-f78838c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 285 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.0 us: 1.28x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.8 ms: 1.16x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 775 ms: 1.16x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.93 us: 1.16x faster                                                       |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.48 ms: 1.09x faster                                                       |
| richards_super             | 61.2 ms                                                          | 56.0 ms: 1.09x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 558 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 54.3 ms: 1.07x faster                                                       |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.06x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.3 ms: 1.06x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 859 us: 1.06x faster                                                        |
| async_tree_io              | 873 ms                                                           | 827 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.48 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.91 sec: 1.05x faster                                                      |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 550 ms: 1.04x faster                                                        |
| scimark_fft                | 312 ms                                                           | 300 ms: 1.04x faster                                                        |
| thrift                     | 880 us                                                           | 846 us: 1.04x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.9 ms: 1.04x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 366 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.3 ms: 1.03x faster                                                       |
| telco                      | 8.40 ms                                                          | 8.18 ms: 1.03x faster                                                       |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 73.1 ms: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.23 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 388 ms: 1.02x faster                                                        |
| pyflate                    | 482 ms                                                           | 474 ms: 1.02x faster                                                        |
| float                      | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.02x faster                                                      |
| pprint_safe_repr           | 818 ms                                                           | 807 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 59.0 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                        |
| scimark_sor                | 119 ms                                                           | 118 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.8 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.1 ms: 1.01x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.97 sec: 1.01x faster                                                      |
| sympy_expand               | 501 ms                                                           | 499 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.00x slower                                                      |
| json_dumps                 | 10.8 ms                                                          | 10.8 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.48 sec: 1.01x slower                                                      |
| json                       | 5.35 ms                                                          | 5.40 ms: 1.01x slower                                                       |
| logging_format             | 7.11 us                                                          | 7.19 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| async_generators           | 363 ms                                                           | 368 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.34 ms: 1.01x slower                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 74.6 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| xml_etree_process          | 59.7 ms                                                          | 60.8 ms: 1.02x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.52 us: 1.02x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.44 ms: 1.02x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 90.0 ms: 1.02x slower                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 87.4 ms: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| raytrace                   | 260 ms                                                           | 267 ms: 1.02x slower                                                        |
| chaos                      | 59.6 ms                                                          | 61.1 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| tomli_loads                | 2.40 sec                                                         | 2.56 sec: 1.07x slower                                                      |
| go                         | 165 ms                                                           | 181 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (11): scimark_lu, coverage, fannkuch, xml_etree_parse, django_template, json_loads, nbody, typing_runtime_protocols, mako, create_gc_cycles, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x