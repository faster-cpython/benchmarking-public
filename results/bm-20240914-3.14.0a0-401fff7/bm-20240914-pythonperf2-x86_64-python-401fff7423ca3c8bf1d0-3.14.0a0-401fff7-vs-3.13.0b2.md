# Results vs. 3.13.0b2

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-x86_64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| html5lib       | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.8 ms: 1.02x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| float          | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 236 ms: 1.05x faster                                                        |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle             | 15.7 us                                                          | 15.0 us: 1.05x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| unpickle_list        | 4.70 us                                                          | 4.60 us: 1.02x faster                                                       |
| pickle               | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.5 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| pickle_dict          | 32.8 us                                                          | 33.5 us: 1.02x slower                                                       |
| pickle_list          | 4.44 us                                                          | 4.64 us: 1.04x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 322 us: 1.05x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.56 sec: 1.06x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                                       |
| genshi_text    | 25.9 ms                                                          | 24.3 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                            | 1.04x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.1 us: 1.28x faster                                                       |
| go                         | 165 ms                                                           | 137 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.17x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.9 ms: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 400 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 783 ms: 1.15x faster                                                        |
| async_tree_none            | 365 ms                                                           | 318 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 311 ms: 1.10x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.7 ms: 1.09x faster                                                       |
| async_tree_io              | 873 ms                                                           | 803 ms: 1.09x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 53.4 ms: 1.09x faster                                                       |
| richards_super             | 61.2 ms                                                          | 56.8 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.3 ms: 1.07x faster                                                       |
| scimark_fft                | 312 ms                                                           | 293 ms: 1.06x faster                                                        |
| richards                   | 53.4 ms                                                          | 50.5 ms: 1.06x faster                                                       |
| regex_dna                  | 249 ms                                                           | 236 ms: 1.05x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 863 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 575 ms: 1.05x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.91 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.09 ms: 1.05x faster                                                       |
| unpickle                   | 15.7 us                                                          | 15.0 us: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 549 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.03x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.97 sec: 1.03x faster                                                      |
| docutils                   | 2.98 sec                                                         | 2.90 sec: 1.03x faster                                                      |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| thrift                     | 880 us                                                           | 857 us: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 95.1 ms: 1.03x faster                                                       |
| nbody                      | 87.8 ms                                                          | 85.8 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| unpickle_list              | 4.70 us                                                          | 4.60 us: 1.02x faster                                                       |
| json                       | 5.35 ms                                                          | 5.25 ms: 1.02x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.98 us: 1.02x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 152 ms: 1.02x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 803 ms: 1.02x faster                                                        |
| pickle                     | 10.6 us                                                          | 10.4 us: 1.02x faster                                                       |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                        |
| sqlite_synth               | 2.80 us                                                          | 2.75 us: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.5 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 72.6 ms: 1.01x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 119 ms: 1.01x faster                                                        |
| async_generators           | 363 ms                                                           | 358 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.8 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.2 ms: 1.01x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                       |
| coverage                   | 83.5 ms                                                          | 82.7 ms: 1.01x faster                                                       |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                      |
| gc_traversal               | 4.69 ms                                                          | 4.65 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 375 ms: 1.01x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.35 us: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.01x faster                                                      |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                           | 129 ms: 1.00x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 88.7 ms: 1.00x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.47 sec: 1.00x slower                                                      |
| xml_etree_process          | 59.7 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| float                      | 80.2 ms                                                          | 80.7 ms: 1.01x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.40 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 8.95 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.45 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| pickle_dict                | 32.8 us                                                          | 33.5 us: 1.02x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 99.3 ns: 1.03x slower                                                       |
| scimark_sor                | 119 ms                                                           | 123 ms: 1.04x slower                                                        |
| fannkuch                   | 353 ms                                                           | 366 ms: 1.04x slower                                                        |
| raytrace                   | 260 ms                                                           | 270 ms: 1.04x slower                                                        |
| pyflate                    | 482 ms                                                           | 503 ms: 1.04x slower                                                        |
| chaos                      | 59.6 ms                                                          | 62.2 ms: 1.04x slower                                                       |
| pickle_list                | 4.44 us                                                          | 4.64 us: 1.04x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 322 us: 1.05x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.8 ms: 1.05x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.56 sec: 1.06x slower                                                      |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (9): bench_mp_pool, telco, dulwich_log, json_dumps, django_template, mako, hexiom, typing_runtime_protocols, pylint
Ignored benchmarks (6) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20240914-3.14.0a0-401fff7/bm-20240914-pythonperf2-x86_64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x