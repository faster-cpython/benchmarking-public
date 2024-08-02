# Results vs. 3.13.0b2

- fork: python
- ref: a2bec77d25b11f50362a
- machine: linux-x86_64
- commit hash: a2bec77
- commit date: 2024-07-13
- overall geometric mean: 1.01x faster
- HPT reliability: 69.48%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 306 ms: 1.05x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.10 sec: 1.04x slower                                                      |
| html5lib       | 74.7 ms                                                          | 70.8 ms: 1.05x faster                                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 805 ms: 1.12x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 414 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_none            | 365 ms                                                           | 340 ms: 1.07x faster                                                        |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 583 ms: 1.04x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.08x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.1 ms: 1.07x faster                                                       |
| nbody          | 87.8 ms                                                          | 82.6 ms: 1.06x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_v8       | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 82.5 ms: 1.04x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 217 us: 1.04x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.01x slower                                                        |
| json_dumps           | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.22 ms: 1.12x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 28.7 ms: 1.11x slower                                                       |
| django_template | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.7 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.05x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240713-pythonperf2-x86_64-python-a2bec77d25b11f50362a-3.14.0a0-a2bec77 |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.7 us: 1.35x faster                                                       |
| deepcopy                   | 377 us                                                           | 305 us: 1.24x faster                                                        |
| richards                   | 53.4 ms                                                          | 44.9 ms: 1.19x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 82.5 ms: 1.18x faster                                                       |
| richards_super             | 61.2 ms                                                          | 53.0 ms: 1.16x faster                                                       |
| tomli_loads                | 2.40 sec                                                         | 2.09 sec: 1.15x faster                                                      |
| mako                       | 10.4 ms                                                          | 9.22 ms: 1.12x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 805 ms: 1.12x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 3.05 us: 1.11x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 414 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 307 ms: 1.11x faster                                                        |
| pyflate                    | 482 ms                                                           | 445 ms: 1.08x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 390 ms: 1.08x faster                                                        |
| async_tree_none            | 365 ms                                                           | 340 ms: 1.07x faster                                                        |
| float                      | 80.2 ms                                                          | 75.1 ms: 1.07x faster                                                       |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| scimark_fft                | 312 ms                                                           | 293 ms: 1.06x faster                                                        |
| nbody                      | 87.8 ms                                                          | 82.6 ms: 1.06x faster                                                       |
| regex_dna                  | 249 ms                                                           | 235 ms: 1.06x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.44 ms: 1.06x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 70.8 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 545 ms: 1.05x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.0 ms: 1.05x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.3 ms: 1.05x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.09 ms: 1.05x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 70.3 ms: 1.05x faster                                                       |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.93 ms: 1.04x faster                                                       |
| coverage                   | 83.5 ms                                                          | 80.2 ms: 1.04x faster                                                       |
| xml_etree_generate         | 85.7 ms                                                          | 82.5 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 583 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                           | 217 us: 1.04x faster                                                        |
| dulwich_log                | 67.3 ms                                                          | 65.3 ms: 1.03x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 58.0 ms: 1.03x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 99.8 ms: 1.03x faster                                                       |
| pprint_safe_repr           | 818 ms                                                           | 796 ms: 1.03x faster                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.62 sec: 1.02x faster                                                      |
| scimark_monte_carlo        | 65.5 ms                                                          | 64.2 ms: 1.02x faster                                                       |
| fannkuch                   | 353 ms                                                           | 346 ms: 1.02x faster                                                        |
| regex_v8                   | 26.0 ms                                                          | 25.6 ms: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 164 ms: 1.01x faster                                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 5.12 sec: 1.00x faster                                                      |
| asyncio_tcp                | 378 ms                                                           | 380 ms: 1.01x slower                                                        |
| logging_simple             | 6.40 us                                                          | 6.47 us: 1.01x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.01x slower                                                        |
| tornado_http               | 119 ms                                                           | 121 ms: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| logging_format             | 7.11 us                                                          | 7.25 us: 1.02x slower                                                       |
| json_dumps                 | 10.8 ms                                                          | 11.0 ms: 1.02x slower                                                       |
| bench_thread_pool          | 908 us                                                           | 929 us: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| dask                       | 391 ms                                                           | 400 ms: 1.03x slower                                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 1.81 ms: 1.03x slower                                                       |
| mdp                        | 2.46 sec                                                         | 2.53 sec: 1.03x slower                                                      |
| pycparser                  | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                      |
| thrift                     | 880 us                                                           | 908 us: 1.03x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.51 ms: 1.03x slower                                                       |
| json                       | 5.35 ms                                                          | 5.54 ms: 1.04x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.10 sec: 1.04x slower                                                      |
| sympy_expand               | 501 ms                                                           | 521 ms: 1.04x slower                                                        |
| sympy_str                  | 295 ms                                                           | 308 ms: 1.04x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 6.66 ms: 1.05x slower                                                       |
| 2to3                       | 291 ms                                                           | 306 ms: 1.05x slower                                                        |
| generators                 | 33.5 ms                                                          | 35.3 ms: 1.05x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 164 ms: 1.06x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 63.2 ms: 1.06x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 102 ns: 1.06x slower                                                        |
| async_generators           | 363 ms                                                           | 386 ms: 1.06x slower                                                        |
| nqueens                    | 88.4 ms                                                          | 94.8 ms: 1.07x slower                                                       |
| comprehensions             | 17.0 us                                                          | 18.3 us: 1.08x slower                                                       |
| sqlglot_normalize          | 120 ms                                                           | 130 ms: 1.08x slower                                                        |
| deltablue                  | 3.37 ms                                                          | 3.66 ms: 1.09x slower                                                       |
| pylint                     | 339 ms                                                           | 372 ms: 1.10x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 25.5 ms: 1.10x slower                                                       |
| scimark_sor                | 119 ms                                                           | 131 ms: 1.10x slower                                                        |
| chaos                      | 59.6 ms                                                          | 66.0 ms: 1.11x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 28.7 ms: 1.11x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 189 us: 1.11x slower                                                        |
| django_template            | 39.0 ms                                                          | 43.3 ms: 1.11x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 64.7 ms: 1.12x slower                                                       |
| raytrace                   | 260 ms                                                           | 298 ms: 1.15x slower                                                        |
| scimark_lu                 | 97.5 ms                                                          | 114 ms: 1.17x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (5): bench_mp_pool, telco, xml_etree_parse, asyncio_websockets, asyncio_tcp_ssl
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 69.48% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x