# Results vs. 3.13.0b2

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.03x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 287 ms: 1.01x faster                                                                  |
| docutils       | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                                |
| html5lib       | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                                 |
| tornado_http   | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                            | 1.01x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 900 ms                                                           | 771 ms: 1.17x faster                                                                  |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.13x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                                  |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                                  |
| Geometric mean             | (ref)                                                            | 1.11x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| pidigits       | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| float          | 80.2 ms                                                          | 82.4 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 249 ms                                                           | 234 ms: 1.07x faster                                                                  |
| regex_compile  | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| regex_v8       | 26.0 ms                                                          | 25.4 ms: 1.02x faster                                                                 |
| regex_effbot   | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                            | 1.03x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                           | 211 us: 1.06x faster                                                                  |
| tomli_loads          | 2.40 sec                                                         | 2.30 sec: 1.05x faster                                                                |
| xml_etree_generate   | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                                 |
| xml_etree_iterparse  | 103 ms                                                           | 101 ms: 1.01x faster                                                                  |
| xml_etree_process    | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                                 |
| json_loads           | 25.0 us                                                          | 25.3 us: 1.01x slower                                                                 |
| pickle_pure_python   | 307 us                                                           | 311 us: 1.01x slower                                                                  |
| json_dumps           | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                                 |
| Geometric mean       | (ref)                                                            | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                                 |
| python_startup_no_site | 8.85 ms                                                          | 9.03 ms: 1.02x slower                                                                 |
| Geometric mean         | (ref)                                                            | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                                                 |
| genshi_text     | 25.9 ms                                                          | 25.3 ms: 1.02x faster                                                                 |
| django_template | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                            | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:----------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 377 us                                                           | 292 us: 1.29x faster                                                                  |
| deepcopy_memo              | 37.3 us                                                          | 29.4 us: 1.27x faster                                                                 |
| async_tree_io_tg           | 900 ms                                                           | 771 ms: 1.17x faster                                                                  |
| generators                 | 33.5 ms                                                          | 28.9 ms: 1.16x faster                                                                 |
| async_tree_memoization     | 460 ms                                                           | 401 ms: 1.14x faster                                                                  |
| deepcopy_reduce            | 3.39 us                                                          | 2.96 us: 1.14x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                           | 300 ms: 1.13x faster                                                                  |
| scimark_sor                | 119 ms                                                           | 107 ms: 1.11x faster                                                                  |
| async_tree_memoization_tg  | 421 ms                                                           | 380 ms: 1.11x faster                                                                  |
| async_tree_none            | 365 ms                                                           | 332 ms: 1.10x faster                                                                  |
| richards_super             | 61.2 ms                                                          | 56.2 ms: 1.09x faster                                                                 |
| async_tree_io              | 873 ms                                                           | 804 ms: 1.09x faster                                                                  |
| pathlib                    | 17.1 ms                                                          | 16.0 ms: 1.07x faster                                                                 |
| regex_dna                  | 249 ms                                                           | 234 ms: 1.07x faster                                                                  |
| richards                   | 53.4 ms                                                          | 50.2 ms: 1.07x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 539 ms: 1.06x faster                                                                  |
| unpickle_pure_python       | 224 us                                                           | 211 us: 1.06x faster                                                                  |
| genshi_xml                 | 58.1 ms                                                          | 54.9 ms: 1.06x faster                                                                 |
| gc_traversal               | 4.69 ms                                                          | 4.45 ms: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 574 ms: 1.05x faster                                                                  |
| telco                      | 8.40 ms                                                          | 7.98 ms: 1.05x faster                                                                 |
| tomli_loads                | 2.40 sec                                                         | 2.30 sec: 1.05x faster                                                                |
| bench_thread_pool          | 908 us                                                           | 869 us: 1.05x faster                                                                  |
| logging_format             | 7.11 us                                                          | 6.81 us: 1.04x faster                                                                 |
| bpe_tokeniser              | 5.14 sec                                                         | 4.92 sec: 1.04x faster                                                                |
| regex_compile              | 144 ms                                                           | 139 ms: 1.04x faster                                                                  |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                                                  |
| logging_simple             | 6.40 us                                                          | 6.19 us: 1.03x faster                                                                 |
| crypto_pyaes               | 73.6 ms                                                          | 71.5 ms: 1.03x faster                                                                 |
| scimark_lu                 | 97.5 ms                                                          | 94.8 ms: 1.03x faster                                                                 |
| tornado_http               | 119 ms                                                           | 116 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.18 ms: 1.03x faster                                                                 |
| regex_v8                   | 26.0 ms                                                          | 25.4 ms: 1.02x faster                                                                 |
| genshi_text                | 25.9 ms                                                          | 25.3 ms: 1.02x faster                                                                 |
| go                         | 165 ms                                                           | 162 ms: 1.02x faster                                                                  |
| async_generators           | 363 ms                                                           | 356 ms: 1.02x faster                                                                  |
| spectral_norm              | 97.3 ms                                                          | 95.7 ms: 1.02x faster                                                                 |
| 2to3                       | 291 ms                                                           | 287 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.7 ms                                                          | 84.6 ms: 1.01x faster                                                                 |
| xml_etree_iterparse        | 103 ms                                                           | 101 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 395 ms                                                           | 390 ms: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                           | 127 ms: 1.01x faster                                                                  |
| xml_etree_process          | 59.7 ms                                                          | 59.1 ms: 1.01x faster                                                                 |
| coroutines                 | 22.0 ms                                                          | 21.7 ms: 1.01x faster                                                                 |
| html5lib                   | 74.7 ms                                                          | 73.8 ms: 1.01x faster                                                                 |
| sqlglot_optimize           | 59.5 ms                                                          | 58.9 ms: 1.01x faster                                                                 |
| asyncio_tcp                | 378 ms                                                           | 374 ms: 1.01x faster                                                                  |
| thrift                     | 880 us                                                           | 872 us: 1.01x faster                                                                  |
| pyflate                    | 482 ms                                                           | 478 ms: 1.01x faster                                                                  |
| sqlglot_normalize          | 120 ms                                                           | 120 ms: 1.01x faster                                                                  |
| pidigits                   | 254 ms                                                           | 253 ms: 1.00x faster                                                                  |
| docutils                   | 2.98 sec                                                         | 2.97 sec: 1.00x faster                                                                |
| sympy_str                  | 295 ms                                                           | 296 ms: 1.00x slower                                                                  |
| sympy_expand               | 501 ms                                                           | 503 ms: 1.00x slower                                                                  |
| django_template            | 39.0 ms                                                          | 39.3 ms: 1.01x slower                                                                 |
| mdp                        | 2.46 sec                                                         | 2.48 sec: 1.01x slower                                                                |
| python_startup             | 13.2 ms                                                          | 13.3 ms: 1.01x slower                                                                 |
| logging_silent             | 96.3 ns                                                          | 97.2 ns: 1.01x slower                                                                 |
| json_loads                 | 25.0 us                                                          | 25.3 us: 1.01x slower                                                                 |
| sympy_integrate            | 23.2 ms                                                          | 23.5 ms: 1.01x slower                                                                 |
| pprint_safe_repr           | 818 ms                                                           | 827 ms: 1.01x slower                                                                  |
| pickle_pure_python         | 307 us                                                           | 311 us: 1.01x slower                                                                  |
| json_dumps                 | 10.8 ms                                                          | 10.9 ms: 1.01x slower                                                                 |
| nqueens                    | 88.4 ms                                                          | 89.7 ms: 1.01x slower                                                                 |
| fannkuch                   | 353 ms                                                           | 358 ms: 1.02x slower                                                                  |
| deltablue                  | 3.37 ms                                                          | 3.43 ms: 1.02x slower                                                                 |
| regex_effbot               | 3.40 ms                                                          | 3.46 ms: 1.02x slower                                                                 |
| sqlglot_transpile          | 1.76 ms                                                          | 1.80 ms: 1.02x slower                                                                 |
| raytrace                   | 260 ms                                                           | 265 ms: 1.02x slower                                                                  |
| python_startup_no_site     | 8.85 ms                                                          | 9.03 ms: 1.02x slower                                                                 |
| typing_runtime_protocols   | 171 us                                                           | 174 us: 1.02x slower                                                                  |
| sqlglot_parse              | 1.39 ms                                                          | 1.43 ms: 1.02x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                          | 67.1 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.66 sec                                                         | 1.70 sec: 1.03x slower                                                                |
| comprehensions             | 17.0 us                                                          | 17.4 us: 1.03x slower                                                                 |
| float                      | 80.2 ms                                                          | 82.4 ms: 1.03x slower                                                                 |
| pycparser                  | 1.22 sec                                                         | 1.26 sec: 1.03x slower                                                                |
| chaos                      | 59.6 ms                                                          | 62.0 ms: 1.04x slower                                                                 |
| Geometric mean             | (ref)                                                            | 1.03x faster                                                                          |

Benchmark hidden because not significant (11): bench_mp_pool, nbody, create_gc_cycles, mako, hexiom, asyncio_tcp_ssl, sympy_sum, xml_etree_parse, coverage, json, pylint
Ignored benchmarks (13) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x