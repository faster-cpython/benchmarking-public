# Results vs. 3.13.0b2

- fork: python
- ref: e38d0afe3548b856ccf0
- machine: linux-x86_64
- commit hash: e38d0af
- commit date: 2024-08-24
- overall geometric mean: 1.02x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                      |
| html5lib       | 74.7 ms                                                          | 75.1 ms: 1.01x slower                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 807 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| nbody          | 87.8 ms                                                          | 90.7 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| regex_compile  | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.0 ms: 1.00x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_generate   | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.54 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (3): xml_etree_process, json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| django_template | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240824-pythonperf2-x86_64-python-e38d0afe3548b856ccf0-3.14.0a0-e38d0af |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 290 us: 1.30x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.2 us: 1.28x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.6 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.93 us: 1.16x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| async_tree_none            | 365 ms                                                           | 323 ms: 1.13x faster                                                        |
| bench_mp_pool              | 4.91 ms                                                          | 4.41 ms: 1.11x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 310 ms: 1.10x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.6 ms: 1.10x faster                                                       |
| async_tree_io              | 873 ms                                                           | 807 ms: 1.08x faster                                                        |
| richards_super             | 61.2 ms                                                          | 56.8 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 852 us: 1.07x faster                                                        |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.07x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.5 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.87 sec: 1.05x faster                                                      |
| genshi_xml                 | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.7 ms: 1.05x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.48 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| scimark_fft                | 312 ms                                                           | 300 ms: 1.04x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| 2to3                       | 291 ms                                                           | 282 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 95.0 ms: 1.03x faster                                                       |
| scimark_sor                | 119 ms                                                           | 116 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.97 us: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.1 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 58.4 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.24 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| float                      | 80.2 ms                                                          | 78.9 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.02x faster                                                        |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 72.5 ms: 1.01x faster                                                       |
| logging_simple             | 6.40 us                                                          | 6.31 us: 1.01x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 808 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.2 ms: 1.01x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.23 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| regex_v8                   | 26.0 ms                                                          | 26.0 ms: 1.00x slower                                                       |
| html5lib                   | 74.7 ms                                                          | 75.1 ms: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| coverage                   | 83.5 ms                                                          | 84.2 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| json                       | 5.35 ms                                                          | 5.44 ms: 1.02x slower                                                       |
| async_generators           | 363 ms                                                           | 369 ms: 1.02x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 98.0 ns: 1.02x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 314 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 361 ms: 1.02x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.50 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.5 us: 1.03x slower                                                       |
| nbody                      | 87.8 ms                                                          | 90.7 ms: 1.03x slower                                                       |
| pyflate                    | 482 ms                                                           | 498 ms: 1.03x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 91.8 ms: 1.04x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.54 sec: 1.06x slower                                                      |
| django_template            | 39.0 ms                                                          | 41.3 ms: 1.06x slower                                                       |
| raytrace                   | 260 ms                                                           | 277 ms: 1.06x slower                                                        |
| go                         | 165 ms                                                           | 180 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (14): scimark_monte_carlo, mako, pprint_pformat, create_gc_cycles, thrift, telco, xml_etree_process, json_loads, sympy_expand, typing_runtime_protocols, deltablue, xml_etree_parse, pycparser, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x