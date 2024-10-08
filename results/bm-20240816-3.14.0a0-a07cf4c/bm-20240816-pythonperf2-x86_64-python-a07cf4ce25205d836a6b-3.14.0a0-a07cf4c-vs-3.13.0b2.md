# Results vs. 3.13.0b2

- fork: python
- ref: a07cf4ce25205d836a6b
- machine: linux-x86_64
- commit hash: a07cf4c
- commit date: 2024-08-16
- overall geometric mean: 1.02x faster
- HPT reliability: 99.87%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| html5lib       | 74.7 ms                                                          | 73.5 ms: 1.02x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 774 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| float          | 80.2 ms                                                          | 81.6 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.22 sec: 1.08x faster                                                      |
| xml_etree_iterparse  | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| unpickle_pure_python | 224 us                                                           | 220 us: 1.02x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_parse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.3 ms: 1.05x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| mako            | 10.4 ms                                                          | 10.2 ms: 1.01x faster                                                       |
| django_template | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 293 us: 1.29x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 30.3 us: 1.23x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.7 ms: 1.17x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 774 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 404 ms: 1.14x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.99 us: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 304 ms: 1.12x faster                                                        |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| richards_super             | 61.2 ms                                                          | 55.9 ms: 1.10x faster                                                       |
| scimark_sor                | 119 ms                                                           | 109 ms: 1.09x faster                                                        |
| richards                   | 53.4 ms                                                          | 49.3 ms: 1.08x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.22 sec: 1.08x faster                                                      |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 812 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.07x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.66 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 544 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                        |
| scimark_fft                | 312 ms                                                           | 297 ms: 1.05x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 55.3 ms: 1.05x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 866 us: 1.05x faster                                                        |
| regex_dna                  | 249 ms                                                           | 239 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 4.93 sec: 1.04x faster                                                      |
| telco                      | 8.40 ms                                                          | 8.07 ms: 1.04x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.85 us: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.13 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 94.1 ms: 1.04x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.3 ms: 1.03x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.95 ms: 1.03x faster                                                       |
| async_generators           | 363 ms                                                           | 353 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.24 us: 1.03x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 385 ms: 1.02x faster                                                        |
| regex_compile              | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 100 ms: 1.02x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 220 us: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| thrift                     | 880 us                                                           | 864 us: 1.02x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                       |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| 2to3                       | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 72.4 ms: 1.02x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 73.5 ms: 1.02x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.0 ms: 1.01x faster                                                       |
| mako                       | 10.4 ms                                                          | 10.2 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| hexiom                     | 6.35 ms                                                          | 6.30 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 252 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 164 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 23.3 ms: 1.00x slower                                                       |
| sympy_str                  | 295 ms                                                           | 296 ms: 1.01x slower                                                        |
| pyflate                    | 482 ms                                                           | 485 ms: 1.01x slower                                                        |
| sympy_expand               | 501 ms                                                           | 505 ms: 1.01x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.40 ms: 1.01x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 60.1 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| django_template            | 39.0 ms                                                          | 39.4 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.9 ms: 1.02x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 66.6 ms: 1.02x slower                                                       |
| float                      | 80.2 ms                                                          | 81.6 ms: 1.02x slower                                                       |
| fannkuch                   | 353 ms                                                           | 359 ms: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.02x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.42 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 123 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.05 ms: 1.02x slower                                                       |
| coverage                   | 83.5 ms                                                          | 85.5 ms: 1.02x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 818 ms                                                           | 841 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 176 us: 1.03x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                        |
| raytrace                   | 260 ms                                                           | 269 ms: 1.03x slower                                                        |
| comprehensions             | 17.0 us                                                          | 17.6 us: 1.04x slower                                                       |
| chaos                      | 59.6 ms                                                          | 62.0 ms: 1.04x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.73 sec: 1.04x slower                                                      |
| regex_effbot               | 3.40 ms                                                          | 3.64 ms: 1.07x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (10): xml_etree_parse, sympy_sum, docutils, gc_traversal, json_loads, asyncio_tcp_ssl, logging_silent, json, nbody, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.87% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x