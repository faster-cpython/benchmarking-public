# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.01x faster
- HPT reliability: 72.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 308 ms: 1.06x slower                                                        |
| docutils       | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| html5lib       | 71.9 ms                                                      | 70.6 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 789 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 826 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 74.5 ms: 1.10x faster                                                       |
| nbody          | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                       |
| pidigits       | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.04x slower                                                       |
| regex_dna      | 244 ms                                                       | 259 ms: 1.06x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.10 sec: 1.15x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 82.3 ms: 1.04x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 97.8 ms: 1.02x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 211 us: 1.02x faster                                                        |
| json_dumps           | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| json_loads           | 24.0 us                                                      | 25.5 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 9.07 ms: 1.15x faster                                                       |
| django_template | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                                       |
| genshi_text     | 26.6 ms                                                      | 29.1 ms: 1.09x slower                                                       |
| genshi_xml      | 57.3 ms                                                      | 64.5 ms: 1.12x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy_memo              | 39.5 us                                                      | 28.8 us: 1.37x faster                                                       |
| deepcopy                   | 397 us                                                       | 308 us: 1.29x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 81.4 ms: 1.20x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 387 ms: 1.19x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.02 us: 1.17x faster                                                       |
| generators                 | 33.5 ms                                                      | 28.9 ms: 1.16x faster                                                       |
| richards                   | 52.7 ms                                                      | 45.5 ms: 1.16x faster                                                       |
| async_tree_none            | 372 ms                                                       | 323 ms: 1.15x faster                                                        |
| mako                       | 10.4 ms                                                      | 9.07 ms: 1.15x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.10 sec: 1.15x faster                                                      |
| richards_super             | 59.8 ms                                                      | 52.3 ms: 1.14x faster                                                       |
| pyflate                    | 492 ms                                                       | 433 ms: 1.14x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 306 ms: 1.11x faster                                                        |
| float                      | 81.9 ms                                                      | 74.5 ms: 1.10x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 413 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.2 ms: 1.07x faster                                                       |
| regex_compile              | 144 ms                                                       | 134 ms: 1.07x faster                                                        |
| scimark_fft                | 314 ms                                                       | 292 ms: 1.07x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.02 ms: 1.07x faster                                                       |
| bpe_tokeniser              | 5.10 sec                                                     | 4.82 sec: 1.06x faster                                                      |
| xml_etree_process          | 60.9 ms                                                      | 57.6 ms: 1.06x faster                                                       |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 544 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 568 ms: 1.06x faster                                                        |
| nbody                      | 88.0 ms                                                      | 84.0 ms: 1.05x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 69.9 ms: 1.04x faster                                                       |
| fannkuch                   | 365 ms                                                       | 351 ms: 1.04x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 789 ms: 1.04x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 82.3 ms: 1.04x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.16 ms: 1.03x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 141 ms: 1.03x faster                                                        |
| async_tree_io              | 847 ms                                                       | 826 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 97.8 ms: 1.02x faster                                                       |
| pprint_safe_repr           | 812 ms                                                       | 796 ms: 1.02x faster                                                        |
| html5lib                   | 71.9 ms                                                      | 70.6 ms: 1.02x faster                                                       |
| unpickle_pure_python       | 214 us                                                       | 211 us: 1.02x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.02x faster                                                      |
| json_dumps                 | 11.0 ms                                                      | 10.8 ms: 1.01x faster                                                       |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                        |
| pidigits                   | 253 ms                                                       | 250 ms: 1.01x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 376 ms: 1.01x faster                                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 64.3 ms: 1.01x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.35 us: 1.01x faster                                                       |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.00x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 21.7 ms: 1.01x slower                                                       |
| coverage                   | 81.1 ms                                                      | 81.9 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.06 ms: 1.01x slower                                                       |
| mdp                        | 2.52 sec                                                     | 2.57 sec: 1.02x slower                                                      |
| asyncio_websockets         | 382 ms                                                       | 391 ms: 1.02x slower                                                        |
| logging_silent             | 97.7 ns                                                      | 100 ns: 1.03x slower                                                        |
| thrift                     | 877 us                                                       | 903 us: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.84 ms: 1.03x slower                                                       |
| dask                       | 379 ms                                                       | 392 ms: 1.03x slower                                                        |
| go                         | 160 ms                                                       | 166 ms: 1.04x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.04x slower                                                       |
| sympy_expand               | 505 ms                                                       | 524 ms: 1.04x slower                                                        |
| raytrace                   | 289 ms                                                       | 300 ms: 1.04x slower                                                        |
| hexiom                     | 6.33 ms                                                      | 6.60 ms: 1.04x slower                                                       |
| sympy_str                  | 296 ms                                                       | 310 ms: 1.05x slower                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.87 ms: 1.05x slower                                                       |
| comprehensions             | 17.3 us                                                      | 18.2 us: 1.05x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.35 ms: 1.06x slower                                                       |
| 2to3                       | 291 ms                                                       | 308 ms: 1.06x slower                                                        |
| deltablue                  | 3.41 ms                                                      | 3.61 ms: 1.06x slower                                                       |
| regex_dna                  | 244 ms                                                       | 259 ms: 1.06x slower                                                        |
| json                       | 5.22 ms                                                      | 5.56 ms: 1.06x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.5 us: 1.06x slower                                                       |
| django_template            | 38.9 ms                                                      | 41.4 ms: 1.07x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.60 ms: 1.07x slower                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 63.8 ms: 1.07x slower                                                       |
| chaos                      | 61.7 ms                                                      | 66.0 ms: 1.07x slower                                                       |
| async_generators           | 359 ms                                                       | 387 ms: 1.08x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 166 ms: 1.08x slower                                                        |
| typing_runtime_protocols   | 174 us                                                       | 188 us: 1.08x slower                                                        |
| nqueens                    | 88.2 ms                                                      | 96.1 ms: 1.09x slower                                                       |
| genshi_text                | 26.6 ms                                                      | 29.1 ms: 1.09x slower                                                       |
| sympy_integrate            | 23.3 ms                                                      | 25.6 ms: 1.10x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.94 ms: 1.10x slower                                                       |
| pylint                     | 346 ms                                                       | 383 ms: 1.11x slower                                                        |
| sqlglot_normalize          | 118 ms                                                       | 131 ms: 1.11x slower                                                        |
| docutils                   | 2.81 sec                                                     | 3.15 sec: 1.12x slower                                                      |
| genshi_xml                 | 57.3 ms                                                      | 64.5 ms: 1.12x slower                                                       |
| scimark_sor                | 126 ms                                                       | 142 ms: 1.13x slower                                                        |
| scimark_lu                 | 97.8 ms                                                      | 113 ms: 1.16x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (6): logging_format, pprint_pformat, asyncio_tcp_ssl, bench_thread_pool, tornado_http, pickle_pure_python
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 72.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.08x