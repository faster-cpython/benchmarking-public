# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.03x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| html5lib       | 74.7 ms                                                          | 73.6 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 772 ms: 1.17x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                        |
| async_tree_io              | 873 ms                                                           | 800 ms: 1.09x faster                                                        |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 87.8 ms                                                          | 86.3 ms: 1.02x faster                                                       |
| float          | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                                       |
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.27 sec: 1.06x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 214 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 58.1 ms                                                          | 55.0 ms: 1.06x faster                                                       |
| genshi_text    | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 285 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.3 us: 1.27x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.86 us: 1.18x faster                                                       |
| generators                 | 33.5 ms                                                          | 28.4 ms: 1.18x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 772 ms: 1.17x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 302 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                        |
| richards_super             | 61.2 ms                                                          | 55.4 ms: 1.11x faster                                                       |
| async_tree_io              | 873 ms                                                           | 800 ms: 1.09x faster                                                        |
| async_tree_none            | 365 ms                                                           | 336 ms: 1.09x faster                                                        |
| richards                   | 53.4 ms                                                          | 49.4 ms: 1.08x faster                                                       |
| scimark_sor                | 119 ms                                                           | 110 ms: 1.08x faster                                                        |
| coverage                   | 83.5 ms                                                          | 77.8 ms: 1.07x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.27 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 541 ms: 1.06x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 55.0 ms: 1.06x faster                                                       |
| telco                      | 8.40 ms                                                          | 7.98 ms: 1.05x faster                                                       |
| bench_mp_pool              | 4.91 ms                                                          | 4.67 ms: 1.05x faster                                                       |
| bench_thread_pool          | 908 us                                                           | 865 us: 1.05x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 214 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 577 ms: 1.05x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.48 ms: 1.05x faster                                                       |
| scimark_fft                | 312 ms                                                           | 299 ms: 1.04x faster                                                        |
| go                         | 165 ms                                                           | 158 ms: 1.04x faster                                                        |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                        |
| scimark_lu                 | 97.5 ms                                                          | 94.1 ms: 1.04x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                       |
| logging_format             | 7.11 us                                                          | 6.92 us: 1.03x faster                                                       |
| 2to3                       | 291 ms                                                           | 284 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 5.01 sec: 1.03x faster                                                      |
| logging_simple             | 6.40 us                                                          | 6.25 us: 1.02x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 58.4 ms: 1.02x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.02x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.97 ms: 1.02x faster                                                       |
| deltablue                  | 3.37 ms                                                          | 3.31 ms: 1.02x faster                                                       |
| nbody                      | 87.8 ms                                                          | 86.3 ms: 1.02x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.7 ms: 1.02x faster                                                       |
| asyncio_tcp                | 378 ms                                                           | 372 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 73.6 ms: 1.01x faster                                                       |
| asyncio_websockets         | 395 ms                                                           | 389 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.22 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.7 ms: 1.01x faster                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.9 ms: 1.01x faster                                                       |
| json                       | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 154 ms: 1.01x faster                                                        |
| sympy_expand               | 501 ms                                                           | 497 ms: 1.01x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| pycparser                  | 1.22 sec                                                         | 1.21 sec: 1.01x faster                                                      |
| pyflate                    | 482 ms                                                           | 478 ms: 1.01x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 96.6 ms: 1.01x faster                                                       |
| float                      | 80.2 ms                                                          | 79.6 ms: 1.01x faster                                                       |
| regex_v8                   | 26.0 ms                                                          | 25.8 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 73.1 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 814 ms: 1.00x faster                                                        |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.2 us: 1.01x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 357 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                      |
| comprehensions             | 17.0 us                                                          | 17.2 us: 1.01x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.01x slower                                                        |
| typing_runtime_protocols   | 171 us                                                           | 174 us: 1.02x slower                                                        |
| chaos                      | 59.6 ms                                                          | 61.0 ms: 1.02x slower                                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 90.9 ms: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 269 ms: 1.03x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.59 ms: 1.06x slower                                                       |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (10): thrift, sympy_integrate, docutils, django_template, sympy_str, logging_silent, hexiom, async_generators, mako, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x