# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 7c66906
- commit date: 2024-07-03
- overall geometric mean: 1.01x faster
- HPT reliability: 90.09%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 291 ms: 1.00x faster                                        |
| docutils       | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                      |
| html5lib       | 74.7 ms                                                          | 73.5 ms: 1.02x faster                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|---------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg          | 900 ms                                                           | 788 ms: 1.14x faster                                        |
| async_tree_memoization    | 460 ms                                                           | 411 ms: 1.12x faster                                        |
| async_tree_none_tg        | 340 ms                                                           | 308 ms: 1.11x faster                                        |
| async_tree_memoization_tg | 421 ms                                                           | 389 ms: 1.08x faster                                        |
| async_tree_none           | 365 ms                                                           | 339 ms: 1.08x faster                                        |
| async_tree_io             | 873 ms                                                           | 822 ms: 1.06x faster                                        |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 573 ms: 1.05x faster                                        |
| Geometric mean            | (ref)                                                            | 1.08x faster                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                        |
| regex_dna      | 249 ms                                                           | 246 ms: 1.01x faster                                        |
| regex_v8       | 26.0 ms                                                          | 26.3 ms: 1.01x slower                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 222 us: 1.01x faster                                        |
| xml_etree_generate   | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                       |
| xml_etree_parse      | 144 ms                                                           | 145 ms: 1.01x slower                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                       |
| xml_etree_process    | 59.7 ms                                                          | 60.5 ms: 1.01x slower                                       |
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                       |
| pickle_pure_python   | 307 us                                                           | 321 us: 1.04x slower                                        |
| Geometric mean       | (ref)                                                            | 1.01x slower                                                |

Benchmark hidden because not significant (2): tomli_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.2 ms: 1.00x slower                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                       |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.02x slower                                       |
| django_template | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                       |
| Geometric mean  | (ref)                                                            | 1.00x slower                                                |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240703-pythonperf2-x86_64-python-main-3.14.0a0-7c66906 |
|---------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| deepcopy                  | 377 us                                                           | 290 us: 1.30x faster                                        |
| deepcopy_memo             | 37.3 us                                                          | 29.5 us: 1.27x faster                                       |
| deepcopy_reduce           | 3.39 us                                                          | 2.93 us: 1.16x faster                                       |
| async_tree_io_tg          | 900 ms                                                           | 788 ms: 1.14x faster                                        |
| async_tree_memoization    | 460 ms                                                           | 411 ms: 1.12x faster                                        |
| async_tree_none_tg        | 340 ms                                                           | 308 ms: 1.11x faster                                        |
| pathlib                   | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                       |
| async_tree_memoization_tg | 421 ms                                                           | 389 ms: 1.08x faster                                        |
| async_tree_none           | 365 ms                                                           | 339 ms: 1.08x faster                                        |
| async_tree_io             | 873 ms                                                           | 822 ms: 1.06x faster                                        |
| gc_traversal              | 4.69 ms                                                          | 4.44 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed   | 604 ms                                                           | 573 ms: 1.05x faster                                        |
| genshi_xml                | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                       |
| richards_super            | 61.2 ms                                                          | 58.8 ms: 1.04x faster                                       |
| richards                  | 53.4 ms                                                          | 51.5 ms: 1.04x faster                                       |
| scimark_sor               | 119 ms                                                           | 115 ms: 1.03x faster                                        |
| bench_thread_pool         | 908 us                                                           | 879 us: 1.03x faster                                        |
| crypto_pyaes              | 73.6 ms                                                          | 71.3 ms: 1.03x faster                                       |
| go                        | 165 ms                                                           | 160 ms: 1.03x faster                                        |
| scimark_fft               | 312 ms                                                           | 303 ms: 1.03x faster                                        |
| asyncio_websockets        | 395 ms                                                           | 386 ms: 1.02x faster                                        |
| regex_compile             | 144 ms                                                           | 141 ms: 1.02x faster                                        |
| dask                      | 391 ms                                                           | 384 ms: 1.02x faster                                        |
| tornado_http              | 119 ms                                                           | 117 ms: 1.02x faster                                        |
| html5lib                  | 74.7 ms                                                          | 73.5 ms: 1.02x faster                                       |
| regex_dna                 | 249 ms                                                           | 246 ms: 1.01x faster                                        |
| docutils                  | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                      |
| spectral_norm             | 97.3 ms                                                          | 96.2 ms: 1.01x faster                                       |
| dulwich_log               | 67.3 ms                                                          | 66.6 ms: 1.01x faster                                       |
| meteor_contest            | 128 ms                                                           | 127 ms: 1.01x faster                                        |
| bpe_tokeniser             | 5.14 sec                                                         | 5.09 sec: 1.01x faster                                      |
| unpickle_pure_python      | 224 us                                                           | 222 us: 1.01x faster                                        |
| sqlglot_normalize         | 120 ms                                                           | 119 ms: 1.01x faster                                        |
| sympy_sum                 | 155 ms                                                           | 154 ms: 1.01x faster                                        |
| float                     | 80.2 ms                                                          | 79.8 ms: 1.00x faster                                       |
| sqlglot_optimize          | 59.5 ms                                                          | 59.3 ms: 1.00x faster                                       |
| pidigits                  | 254 ms                                                           | 253 ms: 1.00x faster                                        |
| asyncio_tcp_ssl           | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                      |
| 2to3                      | 291 ms                                                           | 291 ms: 1.00x faster                                        |
| python_startup            | 13.2 ms                                                          | 13.2 ms: 1.00x slower                                       |
| coverage                  | 83.5 ms                                                          | 83.8 ms: 1.00x slower                                       |
| xml_etree_generate        | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                       |
| sympy_integrate           | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                       |
| comprehensions            | 17.0 us                                                          | 17.1 us: 1.01x slower                                       |
| hexiom                    | 6.35 ms                                                          | 6.39 ms: 1.01x slower                                       |
| async_generators          | 363 ms                                                           | 366 ms: 1.01x slower                                        |
| sympy_expand              | 501 ms                                                           | 505 ms: 1.01x slower                                        |
| scimark_sparse_mat_mult   | 4.28 ms                                                          | 4.32 ms: 1.01x slower                                       |
| pycparser                 | 1.22 sec                                                         | 1.23 sec: 1.01x slower                                      |
| coroutines                | 22.0 ms                                                          | 22.2 ms: 1.01x slower                                       |
| regex_v8                  | 26.0 ms                                                          | 26.3 ms: 1.01x slower                                       |
| xml_etree_parse           | 144 ms                                                           | 145 ms: 1.01x slower                                        |
| generators                | 33.5 ms                                                          | 33.9 ms: 1.01x slower                                       |
| python_startup_no_site    | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                       |
| json_dumps                | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                       |
| xml_etree_process         | 59.7 ms                                                          | 60.5 ms: 1.01x slower                                       |
| pyflate                   | 482 ms                                                           | 488 ms: 1.01x slower                                        |
| pprint_safe_repr          | 818 ms                                                           | 828 ms: 1.01x slower                                        |
| pprint_pformat            | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                      |
| nqueens                   | 88.4 ms                                                          | 89.6 ms: 1.01x slower                                       |
| logging_simple            | 6.40 us                                                          | 6.49 us: 1.01x slower                                       |
| thrift                    | 880 us                                                           | 892 us: 1.01x slower                                        |
| mako                      | 10.4 ms                                                          | 10.5 ms: 1.02x slower                                       |
| json                      | 5.35 ms                                                          | 5.44 ms: 1.02x slower                                       |
| deltablue                 | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                       |
| sqlglot_transpile         | 1.76 ms                                                          | 1.79 ms: 1.02x slower                                       |
| json_loads                | 25.0 us                                                          | 25.5 us: 1.02x slower                                       |
| sqlglot_parse             | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                       |
| mdp                       | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                      |
| scimark_monte_carlo       | 65.5 ms                                                          | 67.2 ms: 1.03x slower                                       |
| raytrace                  | 260 ms                                                           | 268 ms: 1.03x slower                                        |
| typing_runtime_protocols  | 171 us                                                           | 176 us: 1.03x slower                                        |
| logging_silent            | 96.3 ns                                                          | 99.4 ns: 1.03x slower                                       |
| fannkuch                  | 353 ms                                                           | 365 ms: 1.03x slower                                        |
| chaos                     | 59.6 ms                                                          | 62.0 ms: 1.04x slower                                       |
| pickle_pure_python        | 307 us                                                           | 321 us: 1.04x slower                                        |
| django_template           | 39.0 ms                                                          | 40.8 ms: 1.05x slower                                       |
| Geometric mean            | (ref)                                                            | 1.01x faster                                                |

Benchmark hidden because not significant (14): bench_mp_pool, async_tree_cpu_io_mixed_tg, create_gc_cycles, telco, genshi_text, asyncio_tcp, scimark_lu, tomli_loads, sympy_str, regex_effbot, xml_etree_iterparse, logging_format, pylint, nbody
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 90.09% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x