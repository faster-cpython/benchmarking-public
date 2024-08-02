# Results vs. 3.13.0b2

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.02x faster
- HPT reliability: 99.37%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| docutils       | 2.98 sec                                                         | 3.00 sec: 1.00x slower                                                      |
| html5lib       | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                       |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 769 ms: 1.17x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                        |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 799 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 535 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| float          | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| nbody          | 87.8 ms                                                          | 90.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                            | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| regex_dna      | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.28 sec: 1.05x faster                                                      |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| xml_etree_parse      | 144 ms                                                           | 143 ms: 1.00x faster                                                        |
| pickle_pure_python   | 307 us                                                           | 312 us: 1.02x slower                                                        |
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                                       |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_generate, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.0 ms: 1.08x faster                                                       |
| genshi_text     | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| django_template | 39.0 ms                                                          | 38.6 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 286 us: 1.32x faster                                                        |
| deepcopy_memo              | 37.3 us                                                          | 29.9 us: 1.25x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 769 ms: 1.17x faster                                                        |
| generators                 | 33.5 ms                                                          | 28.7 ms: 1.17x faster                                                       |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.16x faster                                                       |
| async_tree_memoization     | 460 ms                                                           | 399 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.14x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 379 ms: 1.11x faster                                                        |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                        |
| scimark_sor                | 119 ms                                                           | 108 ms: 1.10x faster                                                        |
| async_tree_io              | 873 ms                                                           | 799 ms: 1.09x faster                                                        |
| genshi_xml                 | 58.1 ms                                                          | 54.0 ms: 1.08x faster                                                       |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                       |
| richards_super             | 61.2 ms                                                          | 57.2 ms: 1.07x faster                                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 535 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 572 ms: 1.06x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.28 sec: 1.05x faster                                                      |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                        |
| telco                      | 8.40 ms                                                          | 7.98 ms: 1.05x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.90 sec: 1.05x faster                                                      |
| bench_thread_pool          | 908 us                                                           | 870 us: 1.04x faster                                                        |
| richards                   | 53.4 ms                                                          | 51.2 ms: 1.04x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 93.5 ms: 1.04x faster                                                       |
| scimark_fft                | 312 ms                                                           | 302 ms: 1.03x faster                                                        |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                        |
| asyncio_websockets         | 395 ms                                                           | 386 ms: 1.02x faster                                                        |
| sqlglot_normalize          | 120 ms                                                           | 118 ms: 1.02x faster                                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 58.3 ms: 1.02x faster                                                       |
| genshi_text                | 25.9 ms                                                          | 25.4 ms: 1.02x faster                                                       |
| dask                       | 391 ms                                                           | 383 ms: 1.02x faster                                                        |
| 2to3                       | 291 ms                                                           | 287 ms: 1.02x faster                                                        |
| logging_format             | 7.11 us                                                          | 7.02 us: 1.01x faster                                                       |
| hexiom                     | 6.35 ms                                                          | 6.27 ms: 1.01x faster                                                       |
| crypto_pyaes               | 73.6 ms                                                          | 72.6 ms: 1.01x faster                                                       |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.23 ms: 1.01x faster                                                       |
| django_template            | 39.0 ms                                                          | 38.6 ms: 1.01x faster                                                       |
| thrift                     | 880 us                                                           | 871 us: 1.01x faster                                                        |
| coroutines                 | 22.0 ms                                                          | 21.8 ms: 1.01x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 96.4 ms: 1.01x faster                                                       |
| async_generators           | 363 ms                                                           | 359 ms: 1.01x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 102 ms: 1.01x faster                                                        |
| html5lib                   | 74.7 ms                                                          | 74.1 ms: 1.01x faster                                                       |
| sympy_sum                  | 155 ms                                                           | 154 ms: 1.01x faster                                                        |
| regex_compile              | 144 ms                                                           | 143 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 252 ms: 1.00x faster                                                        |
| xml_etree_parse            | 144 ms                                                           | 143 ms: 1.00x faster                                                        |
| meteor_contest             | 128 ms                                                           | 128 ms: 1.00x faster                                                        |
| sympy_str                  | 295 ms                                                           | 296 ms: 1.00x slower                                                        |
| docutils                   | 2.98 sec                                                         | 3.00 sec: 1.00x slower                                                      |
| sympy_integrate            | 23.2 ms                                                          | 23.3 ms: 1.01x slower                                                       |
| float                      | 80.2 ms                                                          | 81.0 ms: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.47 us: 1.01x slower                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.74 ms: 1.01x slower                                                       |
| sympy_expand               | 501 ms                                                           | 507 ms: 1.01x slower                                                        |
| json                       | 5.35 ms                                                          | 5.42 ms: 1.01x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 89.4 ms: 1.01x slower                                                       |
| pycparser                  | 1.22 sec                                                         | 1.24 sec: 1.01x slower                                                      |
| sqlglot_parse              | 1.39 ms                                                          | 1.41 ms: 1.02x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.79 ms: 1.02x slower                                                       |
| logging_silent             | 96.3 ns                                                          | 97.8 ns: 1.02x slower                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 2.04 ms: 1.02x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 312 us: 1.02x slower                                                        |
| regex_dna                  | 249 ms                                                           | 254 ms: 1.02x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.50 sec: 1.02x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 174 us: 1.02x slower                                                        |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                                       |
| pyflate                    | 482 ms                                                           | 492 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.04 ms: 1.02x slower                                                       |
| deltablue                  | 3.37 ms                                                          | 3.45 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 818 ms                                                           | 837 ms: 1.02x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.2 ms: 1.03x slower                                                       |
| chaos                      | 59.6 ms                                                          | 61.1 ms: 1.03x slower                                                       |
| comprehensions             | 17.0 us                                                          | 17.5 us: 1.03x slower                                                       |
| nbody                      | 87.8 ms                                                          | 90.6 ms: 1.03x slower                                                       |
| pprint_pformat             | 1.66 sec                                                         | 1.71 sec: 1.03x slower                                                      |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| coverage                   | 83.5 ms                                                          | 87.3 ms: 1.05x slower                                                       |
| fannkuch                   | 353 ms                                                           | 370 ms: 1.05x slower                                                        |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                                       |
| raytrace                   | 260 ms                                                           | 276 ms: 1.06x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.02x faster                                                                |

Benchmark hidden because not significant (8): bench_mp_pool, asyncio_tcp, xml_etree_process, xml_etree_generate, json_dumps, asyncio_tcp_ssl, mako, pylint
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.37% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x