# Results vs. 3.13.0

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 5e4c3d3
- commit date: 2024-08-16
- overall geometric mean: 1.02x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.03x faster                                                                  |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                                |
| html5lib       | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                                 |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.10x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                                  |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 804 ms: 1.02x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                                  |
| async_generators           | 359 ms                                                       | 355 ms: 1.01x faster                                                                  |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                                  |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                          |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.9 ms: 1.02x faster                                                                 |
| nbody          | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                                 |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                                 |
| regex_dna      | 244 ms                                                       | 254 ms: 1.04x slower                                                                  |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.27 sec: 1.06x faster                                                                |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| xml_etree_process    | 60.9 ms                                                      | 59.4 ms: 1.03x faster                                                                 |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.02x faster                                                                  |
| xml_etree_generate   | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                                                 |
| json_loads           | 24.0 us                                                      | 25.4 us: 1.06x slower                                                                 |
| unpickle_pure_python | 214 us                                                       | 231 us: 1.08x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x faster                                                                 |
| python_startup_no_site | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                                 |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                                 |
| genshi_xml      | 57.3 ms                                                      | 53.2 ms: 1.08x faster                                                                 |
| django_template | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| mako            | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                                                 |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                                  |
| deepcopy_memo              | 39.5 us                                                      | 29.2 us: 1.35x faster                                                                 |
| deepcopy_reduce            | 3.54 us                                                      | 2.96 us: 1.19x faster                                                                 |
| async_tree_memoization_tg  | 461 ms                                                       | 389 ms: 1.19x faster                                                                  |
| generators                 | 33.5 ms                                                      | 28.4 ms: 1.18x faster                                                                 |
| scimark_sor                | 126 ms                                                       | 110 ms: 1.14x faster                                                                  |
| async_tree_none_tg         | 340 ms                                                       | 307 ms: 1.11x faster                                                                  |
| async_tree_memoization     | 452 ms                                                       | 409 ms: 1.10x faster                                                                  |
| async_tree_none            | 372 ms                                                       | 338 ms: 1.10x faster                                                                  |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.10x faster                                                                 |
| genshi_text                | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                                 |
| genshi_xml                 | 57.3 ms                                                      | 53.2 ms: 1.08x faster                                                                 |
| telco                      | 8.58 ms                                                      | 8.00 ms: 1.07x faster                                                                 |
| richards_super             | 59.8 ms                                                      | 55.9 ms: 1.07x faster                                                                 |
| raytrace                   | 289 ms                                                       | 271 ms: 1.07x faster                                                                  |
| tomli_loads                | 2.41 sec                                                     | 2.27 sec: 1.06x faster                                                                |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                                  |
| richards                   | 52.7 ms                                                      | 50.1 ms: 1.05x faster                                                                 |
| bench_thread_pool          | 901 us                                                       | 862 us: 1.05x faster                                                                  |
| async_tree_io              | 847 ms                                                       | 816 ms: 1.04x faster                                                                  |
| scimark_lu                 | 97.8 ms                                                      | 94.4 ms: 1.04x faster                                                                 |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                                  |
| bpe_tokeniser              | 5.10 sec                                                     | 4.93 sec: 1.04x faster                                                                |
| 2to3                       | 291 ms                                                       | 281 ms: 1.03x faster                                                                  |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 580 ms: 1.03x faster                                                                  |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                                  |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                                |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.03x faster                                                                 |
| scimark_fft                | 314 ms                                                       | 306 ms: 1.03x faster                                                                  |
| logging_format             | 7.07 us                                                      | 6.89 us: 1.03x faster                                                                 |
| xml_etree_process          | 60.9 ms                                                      | 59.4 ms: 1.03x faster                                                                 |
| float                      | 81.9 ms                                                      | 79.9 ms: 1.02x faster                                                                 |
| nbody                      | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                                 |
| logging_simple             | 6.40 us                                                      | 6.26 us: 1.02x faster                                                                 |
| fannkuch                   | 365 ms                                                       | 357 ms: 1.02x faster                                                                  |
| async_tree_io_tg           | 819 ms                                                       | 804 ms: 1.02x faster                                                                  |
| coverage                   | 81.1 ms                                                      | 79.8 ms: 1.02x faster                                                                 |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.02x faster                                                                  |
| typing_runtime_protocols   | 174 us                                                       | 171 us: 1.02x faster                                                                  |
| deltablue                  | 3.41 ms                                                      | 3.36 ms: 1.02x faster                                                                 |
| pyflate                    | 492 ms                                                       | 484 ms: 1.02x faster                                                                  |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                                  |
| hexiom                     | 6.33 ms                                                      | 6.24 ms: 1.02x faster                                                                 |
| async_generators           | 359 ms                                                       | 355 ms: 1.01x faster                                                                  |
| comprehensions             | 17.3 us                                                      | 17.1 us: 1.01x faster                                                                 |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.25 ms: 1.01x faster                                                                 |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.4 ms: 1.01x faster                                                                 |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                                  |
| thrift                     | 877 us                                                       | 871 us: 1.01x faster                                                                  |
| chaos                      | 61.7 ms                                                      | 61.3 ms: 1.01x faster                                                                 |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.00x faster                                                                  |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x faster                                                                 |
| spectral_norm              | 97.4 ms                                                      | 97.6 ms: 1.00x slower                                                                 |
| xml_etree_generate         | 85.3 ms                                                      | 85.7 ms: 1.00x slower                                                                 |
| sqlglot_transpile          | 1.78 ms                                                      | 1.79 ms: 1.01x slower                                                                 |
| python_startup_no_site     | 8.94 ms                                                      | 9.00 ms: 1.01x slower                                                                 |
| sympy_sum                  | 154 ms                                                       | 155 ms: 1.01x slower                                                                  |
| html5lib                   | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                                 |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                                                  |
| django_template            | 38.9 ms                                                      | 39.3 ms: 1.01x slower                                                                 |
| mako                       | 10.4 ms                                                      | 10.6 ms: 1.01x slower                                                                 |
| pprint_safe_repr           | 812 ms                                                       | 824 ms: 1.02x slower                                                                  |
| coroutines                 | 21.6 ms                                                      | 22.0 ms: 1.02x slower                                                                 |
| sqlglot_parse              | 1.38 ms                                                      | 1.41 ms: 1.02x slower                                                                 |
| pprint_pformat             | 1.65 sec                                                     | 1.68 sec: 1.02x slower                                                                |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                                                  |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.03x slower                                                                 |
| json                       | 5.22 ms                                                      | 5.41 ms: 1.03x slower                                                                 |
| nqueens                    | 88.2 ms                                                      | 91.8 ms: 1.04x slower                                                                 |
| regex_dna                  | 244 ms                                                       | 254 ms: 1.04x slower                                                                  |
| json_loads                 | 24.0 us                                                      | 25.4 us: 1.06x slower                                                                 |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                                 |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                                |
| unpickle_pure_python       | 214 us                                                       | 231 us: 1.08x slower                                                                  |
| gc_traversal               | 4.11 ms                                                      | 4.49 ms: 1.09x slower                                                                 |
| create_gc_cycles           | 1.76 ms                                                      | 1.98 ms: 1.13x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                          |

Benchmark hidden because not significant (12): bench_mp_pool, pickle_pure_python, mdp, sympy_integrate, asyncio_tcp_ssl, sqlglot_optimize, crypto_pyaes, pidigits, logging_silent, pylint, go, xml_etree_iterparse
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x