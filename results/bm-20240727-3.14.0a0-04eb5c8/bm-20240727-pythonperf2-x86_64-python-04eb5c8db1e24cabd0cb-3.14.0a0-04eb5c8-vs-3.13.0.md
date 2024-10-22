# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.02x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 285 ms: 1.02x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.9 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 778 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 573 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| float          | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| pidigits       | 253 ms                                                       | 253 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 242 ms: 1.01x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.20 sec: 1.09x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 85.0 ms: 1.00x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 320 us: 1.01x slower                                                        |
| unpickle_pure_python | 214 us                                                       | 218 us: 1.02x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.7 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.1 ms: 1.06x faster                                                       |
| genshi_xml     | 57.3 ms                                                      | 56.6 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-pythonperf2-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.5 us: 1.29x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.91 us: 1.22x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.8 ms: 1.16x faster                                                       |
| async_tree_memoization     | 452 ms                                                       | 402 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.20 sec: 1.09x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 537 ms: 1.07x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.1 ms: 1.06x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.11 ms: 1.06x faster                                                       |
| raytrace                   | 289 ms                                                       | 274 ms: 1.06x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 778 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 573 ms: 1.05x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 861 us: 1.05x faster                                                        |
| richards_super             | 59.8 ms                                                      | 57.2 ms: 1.04x faster                                                       |
| scimark_sor                | 126 ms                                                       | 120 ms: 1.04x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.91 sec: 1.04x faster                                                      |
| scimark_fft                | 314 ms                                                       | 304 ms: 1.03x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.22 sec: 1.03x faster                                                      |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.87 us: 1.03x faster                                                       |
| pyflate                    | 492 ms                                                       | 479 ms: 1.03x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.22 us: 1.03x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.3 ms: 1.03x faster                                                       |
| richards                   | 52.7 ms                                                      | 51.4 ms: 1.03x faster                                                       |
| tornado_http               | 120 ms                                                       | 117 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.19 ms: 1.02x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 58.4 ms: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                       | 285 ms: 1.02x faster                                                        |
| go                         | 160 ms                                                       | 158 ms: 1.02x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.02x faster                                                        |
| fannkuch                   | 365 ms                                                       | 359 ms: 1.01x faster                                                        |
| nbody                      | 88.0 ms                                                      | 86.7 ms: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.49 sec: 1.01x faster                                                      |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.2 ms: 1.01x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 56.6 ms: 1.01x faster                                                       |
| sympy_str                  | 296 ms                                                       | 292 ms: 1.01x faster                                                        |
| thrift                     | 877 us                                                       | 866 us: 1.01x faster                                                        |
| float                      | 81.9 ms                                                      | 81.0 ms: 1.01x faster                                                       |
| logging_silent             | 97.7 ns                                                      | 96.6 ns: 1.01x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.1 ms: 1.01x faster                                                       |
| regex_dna                  | 244 ms                                                       | 242 ms: 1.01x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.9 ms: 1.01x faster                                                       |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                        |
| sympy_expand               | 505 ms                                                       | 502 ms: 1.00x faster                                                        |
| deltablue                  | 3.41 ms                                                      | 3.40 ms: 1.00x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 85.0 ms: 1.00x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| python_startup             | 13.3 ms                                                      | 13.3 ms: 1.00x slower                                                       |
| pidigits                   | 253 ms                                                       | 253 ms: 1.00x slower                                                        |
| pickle_pure_python         | 318 us                                                       | 320 us: 1.01x slower                                                        |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.01x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                                       |
| scimark_lu                 | 97.8 ms                                                      | 98.6 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.4 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.05 ms: 1.01x slower                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 73.7 ms: 1.01x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 72.9 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 218 us: 1.02x slower                                                        |
| chaos                      | 61.7 ms                                                      | 62.8 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| async_generators           | 359 ms                                                       | 367 ms: 1.02x slower                                                        |
| regex_v8                   | 26.2 ms                                                      | 26.8 ms: 1.02x slower                                                       |
| pprint_safe_repr           | 812 ms                                                       | 838 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.71 sec: 1.03x slower                                                      |
| json                       | 5.22 ms                                                      | 5.41 ms: 1.03x slower                                                       |
| coverage                   | 81.1 ms                                                      | 84.2 ms: 1.04x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| gc_traversal               | 4.11 ms                                                      | 4.35 ms: 1.06x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.9 ms: 1.06x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.7 us: 1.07x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (10): bench_mp_pool, django_template, nqueens, pylint, sqlglot_normalize, xml_etree_parse, mako, hexiom, dask, typing_runtime_protocols
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x