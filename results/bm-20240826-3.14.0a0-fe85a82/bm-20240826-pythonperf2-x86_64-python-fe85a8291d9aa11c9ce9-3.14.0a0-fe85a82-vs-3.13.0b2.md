# Results vs. 3.13.0b2

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-x86_64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                                      |
| html5lib       | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 547 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.9 ms: 1.02x faster                                                       |
| float          | 80.2 ms                                                          | 79.5 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_dna      | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 213 us: 1.06x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.5 ms: 1.00x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 316 us: 1.03x slower                                                        |
| tomli_loads          | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| genshi_xml      | 58.1 ms                                                          | 56.2 ms: 1.03x faster                                                       |
| django_template | 39.0 ms                                                          | 40.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 291 us: 1.30x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.8 us: 1.25x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.5 ms: 1.18x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.95 us: 1.15x faster                                                       |
| async_tree_none            | 365 ms                                                           | 319 ms: 1.15x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.15x faster                                                        |
| async_tree_io_tg           | 900 ms                                                           | 795 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 308 ms: 1.10x faster                                                        |
| richards_super             | 61.2 ms                                                          | 55.7 ms: 1.10x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.48 ms: 1.10x faster                                                       |
| async_tree_io              | 873 ms                                                           | 802 ms: 1.09x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.8 ms: 1.08x faster                                                       |
| scimark_sor                | 119 ms                                                           | 110 ms: 1.08x faster                                                        |
| richards                   | 53.4 ms                                                          | 49.6 ms: 1.08x faster                                                       |
| async_tree_memoization_tg  | 421 ms                                                           | 392 ms: 1.07x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 856 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 571 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.43 ms: 1.06x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.89 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.86 sec: 1.06x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.06x faster                                                        |
| genshi_text                | 25.9 ms                                                          | 24.6 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 547 ms: 1.05x faster                                                        |
| thrift                     | 880 us                                                           | 846 us: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                           | 281 ms: 1.04x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 56.2 ms: 1.03x faster                                                       |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| sympy_sum                  | 155 ms                                                           | 150 ms: 1.03x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 94.7 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.7 ms: 1.03x faster                                                       |
| scimark_fft                | 312 ms                                                           | 304 ms: 1.03x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 369 ms: 1.02x faster                                                        |
| nbody                      | 87.8 ms                                                          | 85.9 ms: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| pyflate                    | 482 ms                                                           | 471 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| coverage                   | 83.5 ms                                                          | 81.8 ms: 1.02x faster                                                       |
| sympy_str                  | 295 ms                                                           | 290 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 804 ms: 1.02x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.26 ms: 1.02x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.01x faster                                                       |
| sympy_integrate            | 23.2 ms                                                          | 22.9 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.64 sec: 1.01x faster                                                      |
| hexiom                     | 6.35 ms                                                          | 6.29 ms: 1.01x faster                                                       |
| docutils                   | 2.98 sec                                                         | 2.95 sec: 1.01x faster                                                      |
| float                      | 80.2 ms                                                          | 79.5 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 73.0 ms: 1.01x faster                                                       |
| nqueens                    | 88.4 ms                                                          | 87.7 ms: 1.01x faster                                                       |
| deltablue                  | 3.37 ms                                                          | 3.35 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.7 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| xml_etree_process          | 59.7 ms                                                          | 59.5 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.57 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x slower                                                        |
| sympy_expand               | 501 ms                                                           | 502 ms: 1.00x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 65.7 ms: 1.00x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.44 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 356 ms: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.33 ms: 1.01x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.9 ns: 1.02x slower                                                       |
| regex_dna                  | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.02 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.52 sec: 1.02x slower                                                      |
| chaos                      | 59.6 ms                                                          | 61.2 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 316 us: 1.03x slower                                                        |
| comprehensions             | 17.0 us                                                          | 17.5 us: 1.03x slower                                                       |
| django_template            | 39.0 ms                                                          | 40.4 ms: 1.04x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| raytrace                   | 260 ms                                                           | 272 ms: 1.04x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.58 sec: 1.07x slower                                                      |
| go                         | 165 ms                                                           | 179 ms: 1.09x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (11): typing_runtime_protocols, xml_etree_parse, logging_format, json, asyncio_websockets, async_generators, mako, sqlglot_normalize, json_loads, pycparser, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x