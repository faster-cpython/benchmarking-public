# Results vs. 3.13.0b2

- fork: colesbury
- ref: gh_100240_freelist
- machine: linux-x86_64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 286 ms: 1.02x faster                                                         |
| docutils       | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                                       |
| html5lib       | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                        |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 769 ms: 1.17x faster                                                         |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                         |
| async_tree_io              | 873 ms                                                           | 797 ms: 1.10x faster                                                         |
| async_tree_none            | 365 ms                                                           | 334 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 533 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                         |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 86.7 ms: 1.01x faster                                                        |
| pidigits       | 254 ms                                                           | 254 ms: 1.00x slower                                                         |
| float          | 80.2 ms                                                          | 81.8 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                         |
| regex_v8       | 26.0 ms                                                          | 25.1 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 212 us: 1.06x faster                                                         |
| xml_etree_generate   | 85.7 ms                                                          | 83.0 ms: 1.03x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| xml_etree_process    | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.45 sec: 1.02x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 320 us: 1.04x slower                                                         |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                        |
| python_startup_no_site | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                        |
| genshi_text    | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                        |
| mako           | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240717-pythonperf2-x86_64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------------------|:----------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 282 us: 1.34x faster                                                         |
| deepcopy_memo              | 37.3 us                                                          | 29.3 us: 1.27x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.87 us: 1.18x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 769 ms: 1.17x faster                                                         |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                         |
| scimark_sor                | 119 ms                                                           | 107 ms: 1.11x faster                                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                         |
| async_tree_io              | 873 ms                                                           | 797 ms: 1.10x faster                                                         |
| async_tree_none            | 365 ms                                                           | 334 ms: 1.09x faster                                                         |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 533 ms: 1.07x faster                                                         |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 212 us: 1.06x faster                                                         |
| telco                      | 8.40 ms                                                          | 7.94 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.87 sec: 1.05x faster                                                       |
| scimark_fft                | 312 ms                                                           | 296 ms: 1.05x faster                                                         |
| bench_thread_pool          | 908 us                                                           | 864 us: 1.05x faster                                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 576 ms: 1.05x faster                                                         |
| gc_traversal               | 4.69 ms                                                          | 4.47 ms: 1.05x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.11 ms: 1.04x faster                                                        |
| logging_format             | 7.11 us                                                          | 6.84 us: 1.04x faster                                                        |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                         |
| regex_v8                   | 26.0 ms                                                          | 25.1 ms: 1.04x faster                                                        |
| richards                   | 53.4 ms                                                          | 51.7 ms: 1.03x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 83.0 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| xml_etree_parse            | 144 ms                                                           | 140 ms: 1.03x faster                                                         |
| genshi_text                | 25.9 ms                                                          | 25.2 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 71.7 ms: 1.03x faster                                                        |
| meteor_contest             | 128 ms                                                           | 125 ms: 1.03x faster                                                         |
| richards_super             | 61.2 ms                                                          | 59.6 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 95.4 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                         |
| asyncio_websockets         | 395 ms                                                           | 388 ms: 1.02x faster                                                         |
| 2to3                       | 291 ms                                                           | 286 ms: 1.02x faster                                                         |
| pprint_safe_repr           | 818 ms                                                           | 805 ms: 1.02x faster                                                         |
| hexiom                     | 6.35 ms                                                          | 6.26 ms: 1.02x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.02x faster                                                         |
| xml_etree_process          | 59.7 ms                                                          | 58.9 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.7 ms: 1.01x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.32 us: 1.01x faster                                                        |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                                         |
| pyflate                    | 482 ms                                                           | 476 ms: 1.01x faster                                                         |
| nbody                      | 87.8 ms                                                          | 86.7 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.1 ms: 1.01x faster                                                        |
| typing_runtime_protocols   | 171 us                                                           | 169 us: 1.01x faster                                                         |
| html5lib                   | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                        |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                         |
| docutils                   | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                                       |
| dulwich_log                | 67.3 ms                                                          | 66.7 ms: 1.01x faster                                                        |
| async_generators           | 363 ms                                                           | 360 ms: 1.01x faster                                                         |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                         |
| go                         | 165 ms                                                           | 164 ms: 1.01x faster                                                         |
| coverage                   | 83.5 ms                                                          | 83.2 ms: 1.00x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 23.1 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                       |
| pidigits                   | 254 ms                                                           | 254 ms: 1.00x slower                                                         |
| comprehensions             | 17.0 us                                                          | 17.1 us: 1.01x slower                                                        |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                        |
| json                       | 5.35 ms                                                          | 5.42 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.8 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.6 ms: 1.02x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.45 sec: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                                       |
| chaos                      | 59.6 ms                                                          | 60.8 ms: 1.02x slower                                                        |
| float                      | 80.2 ms                                                          | 81.8 ms: 1.02x slower                                                        |
| fannkuch                   | 353 ms                                                           | 360 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.02x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.46 ms: 1.02x slower                                                        |
| raytrace                   | 260 ms                                                           | 267 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 99.6 ns: 1.03x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 320 us: 1.04x slower                                                         |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                 |

Benchmark hidden because not significant (9): bench_mp_pool, pylint, create_gc_cycles, coroutines, xml_etree_iterparse, thrift, sympy_expand, django_template, generators
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x