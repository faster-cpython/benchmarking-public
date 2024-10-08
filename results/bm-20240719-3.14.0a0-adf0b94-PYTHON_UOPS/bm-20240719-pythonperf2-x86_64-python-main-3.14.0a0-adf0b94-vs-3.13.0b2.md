# Results vs. 3.13.0b2

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: adf0b94
- commit date: 2024-07-19
- overall geometric mean: 1.15x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 342 ms: 1.17x slower                                        |
| docutils       | 2.98 sec                                                         | 3.43 sec: 1.15x slower                                      |
| html5lib       | 74.7 ms                                                          | 83.0 ms: 1.11x slower                                       |
| tornado_http   | 119 ms                                                           | 127 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                            | 1.12x slower                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 826 ms: 1.09x faster                                        |
| async_tree_memoization     | 460 ms                                                           | 425 ms: 1.08x faster                                        |
| async_tree_none_tg         | 340 ms                                                           | 318 ms: 1.07x faster                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 399 ms: 1.05x faster                                        |
| async_tree_io              | 873 ms                                                           | 838 ms: 1.04x faster                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                        |
| async_tree_none            | 365 ms                                                           | 356 ms: 1.03x faster                                        |
| Geometric mean             | (ref)                                                            | 1.05x faster                                                |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 80.2 ms                                                          | 91.6 ms: 1.14x slower                                       |
| nbody          | 87.8 ms                                                          | 127 ms: 1.44x slower                                        |
| Geometric mean | (ref)                                                            | 1.18x slower                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 243 ms: 1.02x faster                                        |
| regex_v8       | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                       |
| regex_effbot   | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                       |
| regex_compile  | 144 ms                                                           | 213 ms: 1.48x slower                                        |
| Geometric mean | (ref)                                                            | 1.11x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| json_loads           | 25.0 us                                                          | 25.5 us: 1.02x slower                                       |
| json_dumps           | 10.8 ms                                                          | 11.4 ms: 1.06x slower                                       |
| xml_etree_iterparse  | 103 ms                                                           | 114 ms: 1.12x slower                                        |
| xml_etree_generate   | 85.7 ms                                                          | 97.8 ms: 1.14x slower                                       |
| xml_etree_process    | 59.7 ms                                                          | 68.7 ms: 1.15x slower                                       |
| tomli_loads          | 2.40 sec                                                         | 2.90 sec: 1.21x slower                                      |
| unpickle_pure_python | 224 us                                                           | 301 us: 1.34x slower                                        |
| pickle_pure_python   | 307 us                                                           | 427 us: 1.39x slower                                        |
| Geometric mean       | (ref)                                                            | 1.15x slower                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                       |
| python_startup_no_site | 8.85 ms                                                          | 9.14 ms: 1.03x slower                                       |
| Geometric mean         | (ref)                                                            | 1.02x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|-----------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                       |
| django_template | 39.0 ms                                                          | 46.3 ms: 1.19x slower                                       |
| genshi_text     | 25.9 ms                                                          | 32.8 ms: 1.27x slower                                       |
| mako            | 10.4 ms                                                          | 14.5 ms: 1.40x slower                                       |
| Geometric mean  | (ref)                                                            | 1.25x slower                                                |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240719-pythonperf2-x86_64-python-main-3.14.0a0-adf0b94 |
|----------------------------|:----------------------------------------------------------------:|:-----------------------------------------------------------:|
| generators                 | 33.5 ms                                                          | 30.2 ms: 1.11x faster                                       |
| async_tree_io_tg           | 900 ms                                                           | 826 ms: 1.09x faster                                        |
| async_tree_memoization     | 460 ms                                                           | 425 ms: 1.08x faster                                        |
| deepcopy                   | 377 us                                                           | 351 us: 1.07x faster                                        |
| async_tree_none_tg         | 340 ms                                                           | 318 ms: 1.07x faster                                        |
| async_tree_memoization_tg  | 421 ms                                                           | 399 ms: 1.05x faster                                        |
| coverage                   | 83.5 ms                                                          | 80.0 ms: 1.04x faster                                       |
| gc_traversal               | 4.69 ms                                                          | 4.49 ms: 1.04x faster                                       |
| async_tree_io              | 873 ms                                                           | 838 ms: 1.04x faster                                        |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 557 ms: 1.03x faster                                        |
| pathlib                    | 17.1 ms                                                          | 16.7 ms: 1.03x faster                                       |
| async_tree_none            | 365 ms                                                           | 356 ms: 1.03x faster                                        |
| regex_dna                  | 249 ms                                                           | 243 ms: 1.02x faster                                        |
| asyncio_websockets         | 395 ms                                                           | 391 ms: 1.01x faster                                        |
| regex_v8                   | 26.0 ms                                                          | 25.9 ms: 1.00x faster                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.61 sec: 1.02x slower                                      |
| python_startup             | 13.2 ms                                                          | 13.4 ms: 1.02x slower                                       |
| json_loads                 | 25.0 us                                                          | 25.5 us: 1.02x slower                                       |
| deepcopy_reduce            | 3.39 us                                                          | 3.47 us: 1.02x slower                                       |
| thrift                     | 880 us                                                           | 905 us: 1.03x slower                                        |
| logging_format             | 7.11 us                                                          | 7.33 us: 1.03x slower                                       |
| python_startup_no_site     | 8.85 ms                                                          | 9.14 ms: 1.03x slower                                       |
| asyncio_tcp                | 378 ms                                                           | 392 ms: 1.04x slower                                        |
| logging_simple             | 6.40 us                                                          | 6.65 us: 1.04x slower                                       |
| coroutines                 | 22.0 ms                                                          | 23.1 ms: 1.05x slower                                       |
| json_dumps                 | 10.8 ms                                                          | 11.4 ms: 1.06x slower                                       |
| tornado_http               | 119 ms                                                           | 127 ms: 1.06x slower                                        |
| richards_super             | 61.2 ms                                                          | 65.2 ms: 1.07x slower                                       |
| async_generators           | 363 ms                                                           | 388 ms: 1.07x slower                                        |
| regex_effbot               | 3.40 ms                                                          | 3.65 ms: 1.07x slower                                       |
| dask                       | 391 ms                                                           | 421 ms: 1.08x slower                                        |
| json                       | 5.35 ms                                                          | 5.78 ms: 1.08x slower                                       |
| richards                   | 53.4 ms                                                          | 57.9 ms: 1.08x slower                                       |
| bench_thread_pool          | 908 us                                                           | 987 us: 1.09x slower                                        |
| telco                      | 8.40 ms                                                          | 9.17 ms: 1.09x slower                                       |
| html5lib                   | 74.7 ms                                                          | 83.0 ms: 1.11x slower                                       |
| mdp                        | 2.46 sec                                                         | 2.74 sec: 1.11x slower                                      |
| xml_etree_iterparse        | 103 ms                                                           | 114 ms: 1.12x slower                                        |
| pylint                     | 339 ms                                                           | 383 ms: 1.13x slower                                        |
| meteor_contest             | 128 ms                                                           | 145 ms: 1.13x slower                                        |
| bpe_tokeniser              | 5.14 sec                                                         | 5.82 sec: 1.13x slower                                      |
| xml_etree_generate         | 85.7 ms                                                          | 97.8 ms: 1.14x slower                                       |
| float                      | 80.2 ms                                                          | 91.6 ms: 1.14x slower                                       |
| xml_etree_process          | 59.7 ms                                                          | 68.7 ms: 1.15x slower                                       |
| genshi_xml                 | 58.1 ms                                                          | 66.8 ms: 1.15x slower                                       |
| docutils                   | 2.98 sec                                                         | 3.43 sec: 1.15x slower                                      |
| dulwich_log                | 67.3 ms                                                          | 77.8 ms: 1.16x slower                                       |
| sqlglot_normalize          | 120 ms                                                           | 140 ms: 1.17x slower                                        |
| 2to3                       | 291 ms                                                           | 342 ms: 1.17x slower                                        |
| sqlglot_optimize           | 59.5 ms                                                          | 70.6 ms: 1.19x slower                                       |
| django_template            | 39.0 ms                                                          | 46.3 ms: 1.19x slower                                       |
| pycparser                  | 1.22 sec                                                         | 1.45 sec: 1.19x slower                                      |
| typing_runtime_protocols   | 171 us                                                           | 203 us: 1.19x slower                                        |
| tomli_loads                | 2.40 sec                                                         | 2.90 sec: 1.21x slower                                      |
| sympy_integrate            | 23.2 ms                                                          | 28.1 ms: 1.21x slower                                       |
| go                         | 165 ms                                                           | 202 ms: 1.22x slower                                        |
| sympy_sum                  | 155 ms                                                           | 190 ms: 1.23x slower                                        |
| raytrace                   | 260 ms                                                           | 322 ms: 1.24x slower                                        |
| sqlglot_transpile          | 1.76 ms                                                          | 2.19 ms: 1.24x slower                                       |
| sqlglot_parse              | 1.39 ms                                                          | 1.73 ms: 1.24x slower                                       |
| sympy_expand               | 501 ms                                                           | 628 ms: 1.25x slower                                        |
| sympy_str                  | 295 ms                                                           | 370 ms: 1.26x slower                                        |
| deltablue                  | 3.37 ms                                                          | 4.25 ms: 1.26x slower                                       |
| genshi_text                | 25.9 ms                                                          | 32.8 ms: 1.27x slower                                       |
| crypto_pyaes               | 73.6 ms                                                          | 93.4 ms: 1.27x slower                                       |
| pprint_safe_repr           | 818 ms                                                           | 1.04 sec: 1.27x slower                                      |
| pyflate                    | 482 ms                                                           | 616 ms: 1.28x slower                                        |
| pprint_pformat             | 1.66 sec                                                         | 2.13 sec: 1.28x slower                                      |
| nqueens                    | 88.4 ms                                                          | 114 ms: 1.29x slower                                        |
| chaos                      | 59.6 ms                                                          | 79.5 ms: 1.33x slower                                       |
| deepcopy_memo              | 37.3 us                                                          | 50.0 us: 1.34x slower                                       |
| unpickle_pure_python       | 224 us                                                           | 301 us: 1.34x slower                                        |
| scimark_sor                | 119 ms                                                           | 161 ms: 1.36x slower                                        |
| scimark_fft                | 312 ms                                                           | 433 ms: 1.39x slower                                        |
| pickle_pure_python         | 307 us                                                           | 427 us: 1.39x slower                                        |
| mako                       | 10.4 ms                                                          | 14.5 ms: 1.40x slower                                       |
| fannkuch                   | 353 ms                                                           | 500 ms: 1.42x slower                                        |
| nbody                      | 87.8 ms                                                          | 127 ms: 1.44x slower                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 94.4 ms: 1.44x slower                                       |
| scimark_lu                 | 97.5 ms                                                          | 144 ms: 1.47x slower                                        |
| regex_compile              | 144 ms                                                           | 213 ms: 1.48x slower                                        |
| spectral_norm              | 97.3 ms                                                          | 150 ms: 1.54x slower                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 6.81 ms: 1.59x slower                                       |
| comprehensions             | 17.0 us                                                          | 27.6 us: 1.62x slower                                       |
| logging_silent             | 96.3 ns                                                          | 157 ns: 1.63x slower                                        |
| hexiom                     | 6.35 ms                                                          | 10.5 ms: 1.65x slower                                       |
| Geometric mean             | (ref)                                                            | 1.15x slower                                                |

Benchmark hidden because not significant (5): bench_mp_pool, async_tree_cpu_io_mixed, pidigits, xml_etree_parse, create_gc_cycles
Ignored benchmarks (11) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.11x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.08x

# Memory
- memory change: 1.02x