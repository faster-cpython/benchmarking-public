# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.02x faster
- HPT reliability: 99.83%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| docutils       | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                      |
| html5lib       | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 776 ms: 1.16x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 383 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 811 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| float          | 80.2 ms                                                          | 80.6 ms: 1.00x slower                                                       |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.25 sec: 1.07x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 216 us: 1.04x faster                                                        |
| xml_etree_generate   | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| json_loads           | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 104 ms: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                           | 146 ms: 1.02x slower                                                        |
| pickle_pure_python   | 307 us                                                           | 325 us: 1.06x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.00x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| django_template | 39.0 ms                                                          | 38.3 ms: 1.02x faster                                                       |
| mako            | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 284 us: 1.33x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.8 us: 1.25x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 776 ms: 1.16x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.93 us: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 403 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.13x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 383 ms: 1.10x faster                                                        |
| async_tree_none            | 365 ms                                                           | 335 ms: 1.09x faster                                                        |
| async_tree_io              | 873 ms                                                           | 811 ms: 1.08x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.25 sec: 1.07x faster                                                      |
| coverage                   | 83.5 ms                                                          | 78.4 ms: 1.06x faster                                                       |
| genshi_xml                 | 58.1 ms                                                          | 54.6 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 16.2 ms: 1.06x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.46 ms: 1.05x faster                                                       |
| richards_super             | 61.2 ms                                                          | 58.5 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 579 ms: 1.04x faster                                                        |
| bench_thread_pool          | 908 us                                                           | 873 us: 1.04x faster                                                        |
| regex_dna                  | 249 ms                                                           | 240 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 216 us: 1.04x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.2 ms: 1.04x faster                                                       |
| richards                   | 53.4 ms                                                          | 51.5 ms: 1.04x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.0 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                           | 140 ms: 1.03x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 71.7 ms: 1.03x faster                                                       |
| tornado_http               | 119 ms                                                           | 117 ms: 1.02x faster                                                        |
| meteor_contest             | 128 ms                                                           | 126 ms: 1.02x faster                                                        |
| django_template            | 39.0 ms                                                          | 38.3 ms: 1.02x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 5.05 sec: 1.02x faster                                                      |
| telco                      | 8.40 ms                                                          | 8.25 ms: 1.02x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 95.8 ms: 1.02x faster                                                       |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 66.2 ms: 1.02x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.27 ms: 1.01x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                       |
| dask                       | 391 ms                                                           | 386 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.9 ms: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 153 ms: 1.01x faster                                                        |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                        |
| sympy_expand               | 501 ms                                                           | 496 ms: 1.01x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 74.0 ms: 1.01x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 59.2 ms: 1.01x faster                                                       |
| logging_format             | 7.11 us                                                          | 7.05 us: 1.01x faster                                                       |
| sympy_str                  | 295 ms                                                           | 292 ms: 1.01x faster                                                        |
| 2to3                       | 291 ms                                                           | 289 ms: 1.01x faster                                                        |
| docutils                   | 2.98 sec                                                         | 2.96 sec: 1.01x faster                                                      |
| nqueens                    | 88.4 ms                                                          | 87.7 ms: 1.01x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 812 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.2 ms                                                          | 23.0 ms: 1.01x faster                                                       |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x faster                                                      |
| float                      | 80.2 ms                                                          | 80.6 ms: 1.00x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.2 ms: 1.01x slower                                                       |
| go                         | 165 ms                                                           | 166 ms: 1.01x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.1 us: 1.01x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                       |
| scimark_lu                 | 97.5 ms                                                          | 98.4 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| async_generators           | 363 ms                                                           | 367 ms: 1.01x slower                                                        |
| mako                       | 10.4 ms                                                          | 10.5 ms: 1.01x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.49 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 104 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                           | 146 ms: 1.02x slower                                                        |
| pyflate                    | 482 ms                                                           | 490 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.01 ms: 1.02x slower                                                       |
| json                       | 5.35 ms                                                          | 5.47 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.38 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 98.8 ns: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.4 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.5 ms: 1.03x slower                                                       |
| raytrace                   | 260 ms                                                           | 269 ms: 1.03x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.50 ms: 1.04x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.52 ms: 1.04x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.27 sec: 1.04x slower                                                      |
| fannkuch                   | 353 ms                                                           | 368 ms: 1.04x slower                                                        |
| pickle_pure_python         | 307 us                                                           | 325 us: 1.06x slower                                                        |
| scimark_sor                | 119 ms                                                           | 131 ms: 1.10x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (11): bench_mp_pool, pylint, asyncio_websockets, create_gc_cycles, logging_simple, generators, pprint_pformat, thrift, typing_runtime_protocols, nbody, scimark_fft
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.83% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x