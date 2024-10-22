# Results vs. 3.13.0

- fork: python
- ref: e913d2c87f1ae4e7a4ae
- machine: linux-x86_64
- commit hash: e913d2c
- commit date: 2024-08-15
- overall geometric mean: 1.03x faster
- HPT reliability: 99.97%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 285 ms: 1.02x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 118 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 331 ms: 1.12x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 808 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| async_generators           | 359 ms                                                       | 352 ms: 1.02x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                        |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.26 sec: 1.06x faster                                                      |
| xml_etree_process    | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                        |
| json_loads           | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 25.1 ms: 1.06x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 55.3 ms: 1.04x faster                                                       |
| django_template | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240815-pythonperf2-x86_64-python-e913d2c87f1ae4e7a4ae-3.14.0a0-e913d2c |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 292 us: 1.36x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 30.3 us: 1.30x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 381 ms: 1.21x faster                                                        |
| deepcopy_reduce            | 3.54 us                                                      | 2.97 us: 1.19x faster                                                       |
| generators                 | 33.5 ms                                                      | 28.7 ms: 1.16x faster                                                       |
| scimark_sor                | 126 ms                                                       | 108 ms: 1.16x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 400 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 302 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 331 ms: 1.12x faster                                                        |
| raytrace                   | 289 ms                                                       | 265 ms: 1.09x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| telco                      | 8.58 ms                                                      | 7.90 ms: 1.09x faster                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.26 sec: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 541 ms: 1.06x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.1 ms: 1.06x faster                                                       |
| richards_super             | 59.8 ms                                                      | 56.7 ms: 1.05x faster                                                       |
| richards                   | 52.7 ms                                                      | 50.1 ms: 1.05x faster                                                       |
| scimark_fft                | 314 ms                                                       | 299 ms: 1.05x faster                                                        |
| async_tree_io              | 847 ms                                                       | 808 ms: 1.05x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 784 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 575 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.89 sec: 1.04x faster                                                      |
| regex_dna                  | 244 ms                                                       | 234 ms: 1.04x faster                                                        |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                                        |
| logging_format             | 7.07 us                                                      | 6.80 us: 1.04x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 94.1 ms: 1.04x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 55.3 ms: 1.04x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 870 us: 1.04x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.18 us: 1.03x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| bench_mp_pool              | 4.65 ms                                                      | 4.51 ms: 1.03x faster                                                       |
| regex_v8                   | 26.2 ms                                                      | 25.6 ms: 1.02x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.19 ms: 1.02x faster                                                       |
| json_dumps                 | 11.0 ms                                                      | 10.7 ms: 1.02x faster                                                       |
| coverage                   | 81.1 ms                                                      | 79.6 ms: 1.02x faster                                                       |
| async_generators           | 359 ms                                                       | 352 ms: 1.02x faster                                                        |
| 2to3                       | 291 ms                                                       | 285 ms: 1.02x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| thrift                     | 877 us                                                       | 863 us: 1.02x faster                                                        |
| pycparser                  | 1.26 sec                                                     | 1.24 sec: 1.02x faster                                                      |
| asyncio_tcp                | 380 ms                                                       | 374 ms: 1.01x faster                                                        |
| tornado_http               | 120 ms                                                       | 118 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.1 ms: 1.01x faster                                                       |
| sqlglot_optimize           | 59.7 ms                                                      | 59.0 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 499 ms: 1.01x faster                                                        |
| sympy_str                  | 296 ms                                                       | 293 ms: 1.01x faster                                                        |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 153 ms: 1.01x faster                                                        |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.00x faster                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.77 ms: 1.00x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.32 ms: 1.00x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.54 sec: 1.01x slower                                                      |
| html5lib                   | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.04 ms: 1.01x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.01x slower                                                       |
| go                         | 160 ms                                                       | 163 ms: 1.01x slower                                                        |
| django_template            | 38.9 ms                                                      | 39.5 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| nbody                      | 88.0 ms                                                      | 89.8 ms: 1.02x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 121 ms: 1.02x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| nqueens                    | 88.2 ms                                                      | 90.4 ms: 1.02x slower                                                       |
| fannkuch                   | 365 ms                                                       | 374 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.70 sec: 1.03x slower                                                      |
| pprint_safe_repr           | 812 ms                                                       | 839 ms: 1.03x slower                                                        |
| json                       | 5.22 ms                                                      | 5.41 ms: 1.03x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 67.4 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.2 us: 1.05x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| gc_traversal               | 4.11 ms                                                      | 4.40 ms: 1.07x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 1.98 ms: 1.12x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                |

Benchmark hidden because not significant (14): mako, chaos, deltablue, pyflate, python_startup, pidigits, pylint, asyncio_tcp_ssl, crypto_pyaes, xml_etree_iterparse, comprehensions, float, logging_silent, typing_runtime_protocols
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.97% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x