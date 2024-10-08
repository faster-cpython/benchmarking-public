# Results vs. 3.13.0b2

- fork: faster-cpython
- ref: specialize_call_ex
- machine: linux-x86_64
- commit hash: 852115b
- commit date: 2024-08-19
- overall geometric mean: 1.02x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                                                |
| html5lib       | 74.7 ms                                                          | 75.4 ms: 1.01x slower                                                               |
| tornado_http   | 119 ms                                                           | 118 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                            | 1.00x faster                                                                        |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 764 ms: 1.18x faster                                                                |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                                |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.13x faster                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                                |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                                |
| async_tree_io              | 873 ms                                                           | 798 ms: 1.09x faster                                                                |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                                |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                                |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 85.4 ms: 1.03x faster                                                               |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                                |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 239 ms: 1.04x faster                                                                |
| regex_v8       | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                               |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                                |
| regex_effbot   | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                               |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.28 sec: 1.06x faster                                                              |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                                |
| json_dumps           | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                               |
| xml_etree_process    | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                               |
| xml_etree_generate   | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                               |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                                |
| pickle_pure_python   | 307 us                                                           | 317 us: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                               |
| python_startup_no_site | 8.85 ms                                                          | 9.03 ms: 1.02x slower                                                               |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                                               |
| django_template | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                               |
| Geometric mean  | (ref)                                                            | 1.01x faster                                                                        |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240819-pythonperf2-x86_64-faster%2dcpython-specialize_call_ex-3.14.0a0-852115b |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 284 us: 1.33x faster                                                                |
| deepcopy_memo              | 37.3 us                                                          | 29.6 us: 1.26x faster                                                               |
| deepcopy_reduce            | 3.39 us                                                          | 2.87 us: 1.18x faster                                                               |
| async_tree_io_tg           | 900 ms                                                           | 764 ms: 1.18x faster                                                                |
| generators                 | 33.5 ms                                                          | 29.1 ms: 1.15x faster                                                               |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                                |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.13x faster                                                                |
| async_tree_memoization_tg  | 421 ms                                                           | 382 ms: 1.10x faster                                                                |
| async_tree_none            | 365 ms                                                           | 333 ms: 1.10x faster                                                                |
| async_tree_io              | 873 ms                                                           | 798 ms: 1.09x faster                                                                |
| richards_super             | 61.2 ms                                                          | 57.1 ms: 1.07x faster                                                               |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                                |
| bench_mp_pool              | 4.91 ms                                                          | 4.61 ms: 1.06x faster                                                               |
| pathlib                    | 17.1 ms                                                          | 16.1 ms: 1.06x faster                                                               |
| richards                   | 53.4 ms                                                          | 50.6 ms: 1.06x faster                                                               |
| tomli_loads                | 2.40 sec                                                         | 2.28 sec: 1.06x faster                                                              |
| gc_traversal               | 4.69 ms                                                          | 4.44 ms: 1.05x faster                                                               |
| genshi_xml                 | 58.1 ms                                                          | 55.1 ms: 1.05x faster                                                               |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                                |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                                |
| telco                      | 8.40 ms                                                          | 8.01 ms: 1.05x faster                                                               |
| bench_thread_pool          | 908 us                                                           | 869 us: 1.05x faster                                                                |
| regex_dna                  | 249 ms                                                           | 239 ms: 1.04x faster                                                                |
| coverage                   | 83.5 ms                                                          | 80.3 ms: 1.04x faster                                                               |
| regex_v8                   | 26.0 ms                                                          | 25.2 ms: 1.03x faster                                                               |
| nbody                      | 87.8 ms                                                          | 85.4 ms: 1.03x faster                                                               |
| bpe_tokeniser              | 5.14 sec                                                         | 5.00 sec: 1.03x faster                                                              |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                                |
| meteor_contest             | 128 ms                                                           | 125 ms: 1.02x faster                                                                |
| scimark_sor                | 119 ms                                                           | 116 ms: 1.02x faster                                                                |
| json_dumps                 | 10.8 ms                                                          | 10.6 ms: 1.02x faster                                                               |
| hexiom                     | 6.35 ms                                                          | 6.23 ms: 1.02x faster                                                               |
| xml_etree_process          | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                               |
| spectral_norm              | 97.3 ms                                                          | 95.6 ms: 1.02x faster                                                               |
| xml_etree_generate         | 85.7 ms                                                          | 84.2 ms: 1.02x faster                                                               |
| scimark_lu                 | 97.5 ms                                                          | 95.8 ms: 1.02x faster                                                               |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                                |
| sqlglot_optimize           | 59.5 ms                                                          | 58.7 ms: 1.01x faster                                                               |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.7 ms: 1.01x faster                                                               |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                                |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                                |
| coroutines                 | 22.0 ms                                                          | 21.8 ms: 1.01x faster                                                               |
| tornado_http               | 119 ms                                                           | 118 ms: 1.01x faster                                                                |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.01x faster                                                                |
| 2to3                       | 291 ms                                                           | 289 ms: 1.01x faster                                                                |
| asyncio_tcp                | 378 ms                                                           | 376 ms: 1.01x faster                                                                |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                                |
| crypto_pyaes               | 73.6 ms                                                          | 73.3 ms: 1.00x faster                                                               |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                              |
| sympy_integrate            | 23.2 ms                                                          | 23.2 ms: 1.00x slower                                                               |
| sympy_sum                  | 155 ms                                                           | 155 ms: 1.00x slower                                                                |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.30 ms: 1.00x slower                                                               |
| sympy_expand               | 501 ms                                                           | 503 ms: 1.00x slower                                                                |
| sympy_str                  | 295 ms                                                           | 297 ms: 1.01x slower                                                                |
| thrift                     | 880 us                                                           | 888 us: 1.01x slower                                                                |
| html5lib                   | 74.7 ms                                                          | 75.4 ms: 1.01x slower                                                               |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                               |
| deltablue                  | 3.37 ms                                                          | 3.41 ms: 1.01x slower                                                               |
| raytrace                   | 260 ms                                                           | 263 ms: 1.01x slower                                                                |
| pprint_safe_repr           | 818 ms                                                           | 827 ms: 1.01x slower                                                                |
| logging_silent             | 96.3 ns                                                          | 97.4 ns: 1.01x slower                                                               |
| async_generators           | 363 ms                                                           | 368 ms: 1.02x slower                                                                |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.02x slower                                                                |
| django_template            | 39.0 ms                                                          | 39.6 ms: 1.02x slower                                                               |
| pprint_pformat             | 1.66 sec                                                         | 1.69 sec: 1.02x slower                                                              |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                               |
| comprehensions             | 17.0 us                                                          | 17.3 us: 1.02x slower                                                               |
| python_startup_no_site     | 8.85 ms                                                          | 9.03 ms: 1.02x slower                                                               |
| mdp                        | 2.46 sec                                                         | 2.51 sec: 1.02x slower                                                              |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                              |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                               |
| nqueens                    | 88.4 ms                                                          | 90.9 ms: 1.03x slower                                                               |
| pyflate                    | 482 ms                                                           | 496 ms: 1.03x slower                                                                |
| pickle_pure_python         | 307 us                                                           | 317 us: 1.03x slower                                                                |
| chaos                      | 59.6 ms                                                          | 61.8 ms: 1.04x slower                                                               |
| typing_runtime_protocols   | 171 us                                                           | 180 us: 1.05x slower                                                                |
| regex_effbot               | 3.40 ms                                                          | 3.66 ms: 1.08x slower                                                               |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                        |

Benchmark hidden because not significant (12): scimark_fft, genshi_text, create_gc_cycles, xml_etree_iterparse, logging_format, json_loads, float, docutils, json, logging_simple, mako, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x