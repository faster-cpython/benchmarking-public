# Results vs. 3.13.0b2

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-x86_64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.01x faster
- HPT reliability: 74.95%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 314 ms: 1.08x slower                                                        |
| docutils       | 2.98 sec                                                         | 3.28 sec: 1.10x slower                                                      |
| html5lib       | 74.7 ms                                                          | 72.4 ms: 1.03x faster                                                       |
| tornado_http   | 119 ms                                                           | 122 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 773 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 321 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.12x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 412 ms: 1.11x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 384 ms: 1.10x faster                                                        |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 560 ms: 1.08x faster                                                        |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                        |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                       |
| nbody          | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                       |
| pidigits       | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| regex_v8       | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| regex_dna      | 249 ms                                                           | 261 ms: 1.05x slower                                                        |
| regex_effbot   | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                            | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.12 sec: 1.14x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                          | 77.7 ms: 1.10x faster                                                       |
| xml_etree_process    | 59.7 ms                                                          | 55.3 ms: 1.08x faster                                                       |
| unpickle_pure_python | 224 us                                                           | 213 us: 1.05x faster                                                        |
| xml_etree_iterparse  | 103 ms                                                           | 98.0 ms: 1.05x faster                                                       |
| json_dumps           | 10.8 ms                                                          | 10.4 ms: 1.03x faster                                                       |
| xml_etree_parse      | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| pickle_pure_python   | 307 us                                                           | 319 us: 1.04x slower                                                        |
| Geometric mean       | (ref)                                                            | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 9.16 ms: 1.13x faster                                                       |
| django_template | 39.0 ms                                                          | 42.1 ms: 1.08x slower                                                       |
| genshi_xml      | 58.1 ms                                                          | 64.5 ms: 1.11x slower                                                       |
| genshi_text     | 25.9 ms                                                          | 30.3 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                            | 1.06x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240817-pythonperf2-x86_64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:----------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 37.3 us                                                          | 27.2 us: 1.37x faster                                                       |
| deepcopy                   | 377 us                                                           | 301 us: 1.25x faster                                                        |
| richards                   | 53.4 ms                                                          | 43.8 ms: 1.22x faster                                                       |
| richards_super             | 61.2 ms                                                          | 50.7 ms: 1.21x faster                                                       |
| spectral_norm              | 97.3 ms                                                          | 82.1 ms: 1.19x faster                                                       |
| scimark_sor                | 119 ms                                                           | 101 ms: 1.17x faster                                                        |
| deepcopy_reduce            | 3.39 us                                                          | 2.91 us: 1.17x faster                                                       |
| async_tree_io_tg           | 900 ms                                                           | 773 ms: 1.16x faster                                                        |
| async_tree_none            | 365 ms                                                           | 321 ms: 1.14x faster                                                        |
| tomli_loads                | 2.40 sec                                                         | 2.12 sec: 1.14x faster                                                      |
| mako                       | 10.4 ms                                                          | 9.16 ms: 1.13x faster                                                       |
| async_tree_none_tg         | 340 ms                                                           | 303 ms: 1.12x faster                                                        |
| async_tree_memoization     | 460 ms                                                           | 412 ms: 1.11x faster                                                        |
| xml_etree_generate         | 85.7 ms                                                          | 77.7 ms: 1.10x faster                                                       |
| scimark_fft                | 312 ms                                                           | 285 ms: 1.10x faster                                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 384 ms: 1.10x faster                                                        |
| deltablue                  | 3.37 ms                                                          | 3.11 ms: 1.08x faster                                                       |
| xml_etree_process          | 59.7 ms                                                          | 55.3 ms: 1.08x faster                                                       |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 560 ms: 1.08x faster                                                        |
| pathlib                    | 17.1 ms                                                          | 15.9 ms: 1.08x faster                                                       |
| gc_traversal               | 4.69 ms                                                          | 4.37 ms: 1.07x faster                                                       |
| coverage                   | 83.5 ms                                                          | 78.0 ms: 1.07x faster                                                       |
| telco                      | 8.40 ms                                                          | 7.85 ms: 1.07x faster                                                       |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.00 ms: 1.07x faster                                                       |
| float                      | 80.2 ms                                                          | 75.0 ms: 1.07x faster                                                       |
| async_tree_io              | 873 ms                                                           | 819 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 537 ms: 1.07x faster                                                        |
| crypto_pyaes               | 73.6 ms                                                          | 69.2 ms: 1.06x faster                                                       |
| bpe_tokeniser              | 5.14 sec                                                         | 4.87 sec: 1.06x faster                                                      |
| nbody                      | 87.8 ms                                                          | 83.3 ms: 1.05x faster                                                       |
| unpickle_pure_python       | 224 us                                                           | 213 us: 1.05x faster                                                        |
| xml_etree_iterparse        | 103 ms                                                           | 98.0 ms: 1.05x faster                                                       |
| create_gc_cycles           | 2.00 ms                                                          | 1.93 ms: 1.04x faster                                                       |
| json_dumps                 | 10.8 ms                                                          | 10.4 ms: 1.03x faster                                                       |
| html5lib                   | 74.7 ms                                                          | 72.4 ms: 1.03x faster                                                       |
| coroutines                 | 22.0 ms                                                          | 21.5 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.5 ms                                                          | 95.2 ms: 1.02x faster                                                       |
| xml_etree_parse            | 144 ms                                                           | 141 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 818 ms                                                           | 804 ms: 1.02x faster                                                        |
| pyflate                    | 482 ms                                                           | 475 ms: 1.01x faster                                                        |
| go                         | 165 ms                                                           | 163 ms: 1.01x faster                                                        |
| pidigits                   | 254 ms                                                           | 250 ms: 1.01x faster                                                        |
| json                       | 5.35 ms                                                          | 5.31 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.58 sec: 1.00x slower                                                      |
| logging_format             | 7.11 us                                                          | 7.16 us: 1.01x slower                                                       |
| regex_compile              | 144 ms                                                           | 145 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.68 sec: 1.01x slower                                                      |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                                       |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.01x slower                                                       |
| logging_simple             | 6.40 us                                                          | 6.49 us: 1.01x slower                                                       |
| fannkuch                   | 353 ms                                                           | 360 ms: 1.02x slower                                                        |
| thrift                     | 880 us                                                           | 898 us: 1.02x slower                                                        |
| pycparser                  | 1.22 sec                                                         | 1.25 sec: 1.02x slower                                                      |
| meteor_contest             | 128 ms                                                           | 131 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.85 ms                                                          | 9.06 ms: 1.02x slower                                                       |
| tornado_http               | 119 ms                                                           | 122 ms: 1.03x slower                                                        |
| logging_silent             | 96.3 ns                                                          | 99.5 ns: 1.03x slower                                                       |
| regex_v8                   | 26.0 ms                                                          | 26.9 ms: 1.03x slower                                                       |
| pickle_pure_python         | 307 us                                                           | 319 us: 1.04x slower                                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 68.4 ms: 1.04x slower                                                       |
| regex_dna                  | 249 ms                                                           | 261 ms: 1.05x slower                                                        |
| mdp                        | 2.46 sec                                                         | 2.58 sec: 1.05x slower                                                      |
| async_generators           | 363 ms                                                           | 382 ms: 1.05x slower                                                        |
| sqlglot_parse              | 1.39 ms                                                          | 1.48 ms: 1.06x slower                                                       |
| sympy_expand               | 501 ms                                                           | 535 ms: 1.07x slower                                                        |
| sympy_str                  | 295 ms                                                           | 315 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 120 ms                                                           | 129 ms: 1.07x slower                                                        |
| 2to3                       | 291 ms                                                           | 314 ms: 1.08x slower                                                        |
| comprehensions             | 17.0 us                                                          | 18.3 us: 1.08x slower                                                       |
| regex_effbot               | 3.40 ms                                                          | 3.67 ms: 1.08x slower                                                       |
| django_template            | 39.0 ms                                                          | 42.1 ms: 1.08x slower                                                       |
| raytrace                   | 260 ms                                                           | 283 ms: 1.09x slower                                                        |
| hexiom                     | 6.35 ms                                                          | 6.95 ms: 1.09x slower                                                       |
| docutils                   | 2.98 sec                                                         | 3.28 sec: 1.10x slower                                                      |
| typing_runtime_protocols   | 171 us                                                           | 188 us: 1.10x slower                                                        |
| chaos                      | 59.6 ms                                                          | 65.9 ms: 1.11x slower                                                       |
| sqlglot_optimize           | 59.5 ms                                                          | 65.9 ms: 1.11x slower                                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.96 ms: 1.11x slower                                                       |
| sympy_sum                  | 155 ms                                                           | 172 ms: 1.11x slower                                                        |
| genshi_xml                 | 58.1 ms                                                          | 64.5 ms: 1.11x slower                                                       |
| nqueens                    | 88.4 ms                                                          | 99.0 ms: 1.12x slower                                                       |
| generators                 | 33.5 ms                                                          | 37.8 ms: 1.13x slower                                                       |
| sympy_integrate            | 23.2 ms                                                          | 26.7 ms: 1.15x slower                                                       |
| genshi_text                | 25.9 ms                                                          | 30.3 ms: 1.17x slower                                                       |
| pylint                     | 339 ms                                                           | 405 ms: 1.19x slower                                                        |
| Geometric mean             | (ref)                                                            | 1.01x faster                                                                |

Benchmark hidden because not significant (4): bench_mp_pool, asyncio_tcp, asyncio_websockets, bench_thread_pool
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 74.95% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x