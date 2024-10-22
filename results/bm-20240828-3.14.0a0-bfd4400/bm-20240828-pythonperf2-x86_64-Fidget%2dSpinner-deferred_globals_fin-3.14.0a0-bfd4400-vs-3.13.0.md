# Results vs. 3.13.0

- fork: Fidget-Spinner
- ref: deferred_globals_fin
- machine: linux-x86_64
- commit hash: bfd4400
- commit date: 2024-08-28
- overall geometric mean: 1.03x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| html5lib       | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                                 |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 771 ms: 1.06x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 804 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                                  |
| async_generators           | 359 ms                                                       | 356 ms: 1.01x faster                                                                  |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| float          | 81.9 ms                                                      | 82.4 ms: 1.01x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                                  |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 25.4 ms: 1.03x faster                                                                 |
| regex_effbot   | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.30 sec: 1.05x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                                 |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                                  |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.01x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 84.6 ms: 1.01x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                                  |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.00x faster                                                                 |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| json_loads           | 24.0 us                                                      | 25.3 us: 1.06x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.3 ms: 1.05x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                                                 |
| mako            | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-pythonperf2-x86_64-Fidget%2dSpinner-deferred_globals_fin-3.14.0a0-bfd4400 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 29.4 us: 1.34x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 380 ms: 1.21x faster                                                                  |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.20x faster                                                                 |
| scimark_sor                | 126 ms                                                       | 107 ms: 1.17x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.9 ms: 1.16x faster                                                                 |
| async_tree_none_tg         | 340 ms                                                       | 300 ms: 1.13x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 332 ms: 1.12x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                                 |
| raytrace                   | 289 ms                                                       | 265 ms: 1.09x faster                                                                  |
| telco                      | 8.58 ms                                                      | 7.98 ms: 1.08x faster                                                                 |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                                  |
| richards_super             | 59.8 ms                                                      | 56.2 ms: 1.06x faster                                                                 |
| async_tree_io_tg           | 819 ms                                                       | 771 ms: 1.06x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 804 ms: 1.05x faster                                                                  |
| richards                   | 52.7 ms                                                      | 50.2 ms: 1.05x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 25.3 ms: 1.05x faster                                                                 |
| tomli_loads                | 2.41 sec                                                     | 2.30 sec: 1.05x faster                                                                |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 574 ms: 1.04x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 54.9 ms: 1.04x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                                                  |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                                  |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| logging_format             | 7.07 us                                                      | 6.81 us: 1.04x faster                                                                 |
| bench_thread_pool          | 901 us                                                       | 869 us: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.92 sec: 1.04x faster                                                                |
| logging_simple             | 6.40 us                                                      | 6.19 us: 1.03x faster                                                                 |
| scimark_lu                 | 97.8 ms                                                      | 94.8 ms: 1.03x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.1 ms: 1.03x faster                                                                 |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| regex_v8                   | 26.2 ms                                                      | 25.4 ms: 1.03x faster                                                                 |
| pyflate                    | 492 ms                                                       | 478 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.18 ms: 1.03x faster                                                                 |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                                  |
| crypto_pyaes               | 72.8 ms                                                      | 71.5 ms: 1.02x faster                                                                 |
| fannkuch                   | 365 ms                                                       | 358 ms: 1.02x faster                                                                  |
| mdp                        | 2.52 sec                                                     | 2.48 sec: 1.02x faster                                                                |
| spectral_norm              | 97.4 ms                                                      | 95.7 ms: 1.02x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                                  |
| unpickle_pure_python       | 214 us                                                       | 211 us: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                                  |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| sqlglot_optimize           | 59.7 ms                                                      | 58.9 ms: 1.01x faster                                                                 |
| mako                       | 10.4 ms                                                      | 10.3 ms: 1.01x faster                                                                 |
| xml_etree_generate         | 85.3 ms                                                      | 84.6 ms: 1.01x faster                                                                 |
| async_generators           | 359 ms                                                       | 356 ms: 1.01x faster                                                                  |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                                  |
| logging_silent             | 97.7 ns                                                      | 97.2 ns: 1.00x faster                                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.00x faster                                                                 |
| sympy_expand               | 505 ms                                                       | 503 ms: 1.00x faster                                                                  |
| chaos                      | 61.7 ms                                                      | 62.0 ms: 1.00x slower                                                                 |
| sympy_integrate            | 23.3 ms                                                      | 23.5 ms: 1.01x slower                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.43 ms: 1.01x slower                                                                 |
| float                      | 81.9 ms                                                      | 82.4 ms: 1.01x slower                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                                  |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                                 |
| go                         | 160 ms                                                       | 162 ms: 1.01x slower                                                                  |
| python_startup_no_site     | 8.94 ms                                                      | 9.03 ms: 1.01x slower                                                                 |
| django_template            | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| nqueens                    | 88.2 ms                                                      | 89.7 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 827 ms: 1.02x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                                  |
| regex_effbot               | 3.37 ms                                                      | 3.46 ms: 1.03x slower                                                                 |
| html5lib                   | 71.9 ms                                                      | 73.8 ms: 1.03x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.37 ms: 1.03x slower                                                                 |
| coverage                   | 81.1 ms                                                      | 83.6 ms: 1.03x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                                |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.03x slower                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.1 ms: 1.03x slower                                                                 |
| json_loads                 | 24.0 us                                                      | 25.3 us: 1.06x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                                |
| gc_traversal               | 4.11 ms                                                      | 4.45 ms: 1.08x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                          |

Benchmark hidden because not significant (10): thrift, sympy_str, asyncio_tcp_ssl, pidigits, pycparser, python_startup, typing_runtime_protocols, pylint, hexiom, bench_mp_pool
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x