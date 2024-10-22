# Results vs. 3.13.0

- fork: faster-cpython
- ref: fix_not_specialized_
- machine: linux-x86_64
- commit hash: 10855bc
- commit date: 2024-08-22
- overall geometric mean: 1.02x faster
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                                                |
| html5lib       | 71.9 ms                                                      | 72.8 ms: 1.01x slower                                                                 |
| tornado_http   | 120 ms                                                       | 117 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 797 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                                  |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.00x slower                                                                 |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                                  |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                                                 |
| nbody          | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                                  |
| regex_dna      | 244 ms                                                       | 240 ms: 1.01x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 26.1 ms: 1.00x faster                                                                 |
| regex_effbot   | 3.37 ms                                                      | 3.62 ms: 1.08x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.30 sec: 1.05x faster                                                                |
| xml_etree_process    | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                                 |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                                 |
| unpickle_pure_python | 214 us                                                       | 212 us: 1.01x faster                                                                  |
| pickle_pure_python   | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| xml_etree_iterparse  | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| json_loads           | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 55.5 ms: 1.03x faster                                                                 |
| genshi_text     | 26.6 ms                                                      | 25.8 ms: 1.03x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240822-pythonperf2-x86_64-faster%2dcpython-fix_not_specialized_-3.14.0a0-10855bc |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 287 us: 1.38x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 29.9 us: 1.32x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.94 us: 1.21x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 388 ms: 1.19x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.4 ms: 1.18x faster                                                                 |
| async_tree_none            | 372 ms                                                       | 318 ms: 1.17x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 398 ms: 1.13x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 55.1 ms: 1.08x faster                                                                 |
| raytrace                   | 289 ms                                                       | 267 ms: 1.08x faster                                                                  |
| richards                   | 52.7 ms                                                      | 49.0 ms: 1.08x faster                                                                 |
| telco                      | 8.58 ms                                                      | 7.98 ms: 1.08x faster                                                                 |
| async_tree_io              | 847 ms                                                       | 797 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 781 ms: 1.05x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.30 sec: 1.05x faster                                                                |
| bench_thread_pool          | 901 us                                                       | 862 us: 1.05x faster                                                                  |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                                  |
| pyflate                    | 492 ms                                                       | 471 ms: 1.04x faster                                                                  |
| coverage                   | 81.1 ms                                                      | 78.0 ms: 1.04x faster                                                                 |
| bpe_tokeniser              | 5.10 sec                                                     | 4.91 sec: 1.04x faster                                                                |
| scimark_lu                 | 97.8 ms                                                      | 94.7 ms: 1.03x faster                                                                 |
| asyncio_tcp                | 380 ms                                                       | 368 ms: 1.03x faster                                                                  |
| genshi_xml                 | 57.3 ms                                                      | 55.5 ms: 1.03x faster                                                                 |
| float                      | 81.9 ms                                                      | 79.3 ms: 1.03x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 305 ms: 1.03x faster                                                                  |
| genshi_text                | 26.6 ms                                                      | 25.8 ms: 1.03x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                                 |
| tornado_http               | 120 ms                                                       | 117 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.18 ms: 1.03x faster                                                                 |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 142 ms: 1.02x faster                                                                  |
| sqlglot_optimize           | 59.7 ms                                                      | 58.5 ms: 1.02x faster                                                                 |
| sympy_sum                  | 154 ms                                                       | 151 ms: 1.02x faster                                                                  |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                                 |
| sympy_str                  | 296 ms                                                       | 291 ms: 1.02x faster                                                                  |
| thrift                     | 877 us                                                       | 864 us: 1.01x faster                                                                  |
| regex_dna                  | 244 ms                                                       | 240 ms: 1.01x faster                                                                  |
| xml_etree_generate         | 85.3 ms                                                      | 84.2 ms: 1.01x faster                                                                 |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                                  |
| unpickle_pure_python       | 214 us                                                       | 212 us: 1.01x faster                                                                  |
| nbody                      | 88.0 ms                                                      | 86.9 ms: 1.01x faster                                                                 |
| chaos                      | 61.7 ms                                                      | 61.1 ms: 1.01x faster                                                                 |
| logging_format             | 7.07 us                                                      | 7.01 us: 1.01x faster                                                                 |
| logging_simple             | 6.40 us                                                      | 6.34 us: 1.01x faster                                                                 |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.01x faster                                                                  |
| regex_v8                   | 26.2 ms                                                      | 26.1 ms: 1.00x faster                                                                 |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                                |
| scimark_sor                | 126 ms                                                       | 126 ms: 1.00x slower                                                                  |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                                 |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                                                  |
| mdp                        | 2.52 sec                                                     | 2.53 sec: 1.00x slower                                                                |
| nqueens                    | 88.2 ms                                                      | 88.5 ms: 1.00x slower                                                                 |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.00x slower                                                                 |
| hexiom                     | 6.33 ms                                                      | 6.36 ms: 1.00x slower                                                                 |
| deltablue                  | 3.41 ms                                                      | 3.43 ms: 1.01x slower                                                                 |
| pickle_pure_python         | 318 us                                                       | 321 us: 1.01x slower                                                                  |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                                  |
| xml_etree_iterparse        | 100 ms                                                       | 101 ms: 1.01x slower                                                                  |
| logging_silent             | 97.7 ns                                                      | 98.5 ns: 1.01x slower                                                                 |
| python_startup_no_site     | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                                 |
| html5lib                   | 71.9 ms                                                      | 72.8 ms: 1.01x slower                                                                 |
| typing_runtime_protocols   | 174 us                                                       | 176 us: 1.01x slower                                                                  |
| scimark_monte_carlo        | 64.9 ms                                                      | 66.0 ms: 1.02x slower                                                                 |
| fannkuch                   | 365 ms                                                       | 371 ms: 1.02x slower                                                                  |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                                |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                                                  |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 827 ms: 1.02x slower                                                                  |
| json                       | 5.22 ms                                                      | 5.33 ms: 1.02x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                                  |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                                 |
| comprehensions             | 17.3 us                                                      | 17.8 us: 1.03x slower                                                                 |
| go                         | 160 ms                                                       | 166 ms: 1.04x slower                                                                  |
| json_loads                 | 24.0 us                                                      | 24.9 us: 1.04x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.94 sec: 1.05x slower                                                                |
| regex_effbot               | 3.37 ms                                                      | 3.62 ms: 1.08x slower                                                                 |
| gc_traversal               | 4.11 ms                                                      | 4.50 ms: 1.10x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (7): bench_mp_pool, mako, crypto_pyaes, spectral_norm, sqlglot_transpile, pylint, pycparser
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.86% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x