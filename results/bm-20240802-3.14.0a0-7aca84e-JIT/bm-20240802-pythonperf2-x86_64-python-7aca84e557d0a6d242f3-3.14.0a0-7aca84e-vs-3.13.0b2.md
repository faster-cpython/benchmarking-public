# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.01x faster
- HPT reliability: 64.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                      |
| html5lib       | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 771 ms: 1.17x faster                                                        |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 563 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 540 ms: 1.06x faster                                                        |
| async_tree_io              | 873 ms                                                           | 828 ms: 1.05x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 76.2 ms: 1.05x faster                                                       |
| pidigits       | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| regex_v8       | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| regex_dna      | 249 ms                                                           | 261 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.10 sec: 1.14x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 80.3 ms: 1.07x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 211 us: 1.06x faster                                                        |
| xml_etree_process    | 59.7 ms                                                          | 56.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                           | 97.2 ms: 1.06x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| json_dumps           | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| json_loads           | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 314 us: 1.02x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.10 ms: 1.03x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.12 ms: 1.14x faster                                                       |
| django_template | 39.0 ms                                                          | 41.5 ms: 1.07x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 62.0 ms: 1.07x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 28.2 ms: 1.09x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.02x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 29.1 us: 1.28x faster                                                       |
| deepcopy                   | 377 us                                                           | 311 us: 1.21x faster                                                        |
| spectral_norm              | 97.3 ms                                                          | 81.4 ms: 1.20x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 771 ms: 1.17x faster                                                        |
| richards                   | 53.4 ms                                                          | 46.6 ms: 1.15x faster                                                       |
| scimark_sor                | 119 ms                                                           | 104 ms: 1.14x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.10 sec: 1.14x faster                                                      |
| mako                       | 10.4 ms                                                          | 9.12 ms: 1.14x faster                                                       |
| async_tree_none            | 365 ms                                                           | 322 ms: 1.13x faster                                                        |
| richards_super             | 61.2 ms                                                          | 54.1 ms: 1.13x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 3.04 us: 1.12x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 413 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 306 ms: 1.11x faster                                                        |
| scimark_fft                | 312 ms                                                           | 285 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 388 ms: 1.08x faster                                                        |
| gc_traversal               | 4.69 ms                                                          | 4.34 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 563 ms: 1.07x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 80.3 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.82 sec: 1.07x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 211 us: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 540 ms: 1.06x faster                                                        |
| coverage                   | 83.5 ms                                                          | 78.8 ms: 1.06x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 56.5 ms: 1.06x faster                                                       |
| xml_etree_iterparse        | 103 ms                                                           | 97.2 ms: 1.06x faster                                                       |
| async_tree_io              | 873 ms                                                           | 828 ms: 1.05x faster                                                        |
| float                      | 80.2 ms                                                          | 76.2 ms: 1.05x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 71.1 ms: 1.05x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.3 ms: 1.05x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.92 ms: 1.04x faster                                                       |
| regex_compile              | 144 ms                                                           | 138 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.11 ms: 1.04x faster                                                       |
| pyflate                    | 482 ms                                                           | 463 ms: 1.04x faster                                                        |
| telco                      | 8.40 ms                                                          | 8.09 ms: 1.04x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 71.0 ms: 1.04x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 139 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                          | 6.29 us: 1.02x faster                                                       |
| pidigits                   | 254 ms                                                           | 251 ms: 1.01x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                                        |
| logging_format             | 7.11 us                                                          | 7.05 us: 1.01x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.7 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.00x faster                                                      |
| fannkuch                   | 353 ms                                                           | 355 ms: 1.01x slower                                                        |
| json                       | 5.35 ms                                                          | 5.42 ms: 1.01x slower                                                       |
| json_loads                 | 25.0 us                                                          | 25.4 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                                       |
| coroutines                 | 22.0 ms                                                          | 22.4 ms: 1.02x slower                                                       |
| go                         | 165 ms                                                           | 168 ms: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| pickle_pure_python         | 307 us                                                           | 314 us: 1.02x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.48 ms: 1.02x slower                                                       |
| thrift                     | 880 us                                                           | 902 us: 1.03x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.10 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.5 ms: 1.03x slower                                                       |
| sympy_expand               | 501 ms                                                           | 521 ms: 1.04x slower                                                        |
| regex_v8                   | 26.0 ms                                                          | 27.1 ms: 1.04x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 100 ns: 1.04x slower                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 62.2 ms: 1.04x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.84 ms: 1.05x slower                                                       |
| regex_dna                  | 249 ms                                                           | 261 ms: 1.05x slower                                                        |
| sympy_str                  | 295 ms                                                           | 310 ms: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.59 sec: 1.05x slower                                                      |
| docutils                   | 2.98 sec                                                         | 3.14 sec: 1.05x slower                                                      |
| 2to3                       | 291 ms                                                           | 308 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 128 ms: 1.06x slower                                                        |
| comprehensions             | 17.0 us                                                          | 18.0 us: 1.06x slower                                                       |
| async_generators           | 363 ms                                                           | 386 ms: 1.06x slower                                                        |
| django_template            | 39.0 ms                                                          | 41.5 ms: 1.07x slower                                                       |
| hexiom                     | 6.35 ms                                                          | 6.77 ms: 1.07x slower                                                       |
| genshi_xml                 | 58.1 ms                                                          | 62.0 ms: 1.07x slower                                                       |
| typing_runtime_protocols   | 171 us                                                           | 183 us: 1.07x slower                                                        |
| sympy_sum                  | 155 ms                                                           | 167 ms: 1.08x slower                                                        |
| generators                 | 33.5 ms                                                          | 36.2 ms: 1.08x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 28.2 ms: 1.09x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.74 ms: 1.11x slower                                                       |
| chaos                      | 59.6 ms                                                          | 66.0 ms: 1.11x slower                                                       |
| raytrace                   | 260 ms                                                           | 289 ms: 1.11x slower                                                        |
| sympy_integrate            | 23.2 ms                                                          | 25.9 ms: 1.12x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 99.3 ms: 1.12x slower                                                       |
| pylint                     | 339 ms                                                           | 387 ms: 1.14x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, pprint_safe_repr, asyncio_tcp, meteor_contest, asyncio_tcp_ssl, bench_thread_pool, scimark_lu, nbody, tornado_http, dask
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 64.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x