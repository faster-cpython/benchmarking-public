# Results vs. 3.13.0

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-x86_64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.02x faster
- HPT reliability: 98.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 73.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 305 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 767 ms: 1.07x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 553 ms: 1.04x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 361 ms: 1.01x slower                                                        |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| float          | 81.9 ms                                                      | 81.3 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| xml_etree_generate   | 85.3 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| unpickle_pure_python | 214 us                                                       | 216 us: 1.01x slower                                                        |
| tomli_loads          | 2.41 sec                                                     | 2.44 sec: 1.01x slower                                                      |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (3): json_dumps, pickle_pure_python, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                       |
| genshi_text     | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                                       |
| django_template | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 288 us: 1.38x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.0 us: 1.36x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.92 us: 1.21x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.3 ms: 1.18x faster                                                       |
| scimark_sor                | 126 ms                                                       | 110 ms: 1.14x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none            | 372 ms                                                       | 333 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 305 ms: 1.11x faster                                                        |
| telco                      | 8.58 ms                                                      | 7.80 ms: 1.10x faster                                                       |
| pathlib                    | 17.4 ms                                                      | 16.0 ms: 1.09x faster                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.01 ms: 1.07x faster                                                       |
| scimark_fft                | 314 ms                                                       | 294 ms: 1.07x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 767 ms: 1.07x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 54.2 ms: 1.06x faster                                                       |
| raytrace                   | 289 ms                                                       | 273 ms: 1.06x faster                                                        |
| async_tree_io              | 847 ms                                                       | 813 ms: 1.04x faster                                                        |
| genshi_text                | 26.6 ms                                                      | 25.6 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 577 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 553 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.92 sec: 1.04x faster                                                      |
| nbody                      | 88.0 ms                                                      | 85.1 ms: 1.03x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 872 us: 1.03x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 58.9 ms: 1.03x faster                                                       |
| coverage                   | 81.1 ms                                                      | 78.7 ms: 1.03x faster                                                       |
| regex_dna                  | 244 ms                                                       | 237 ms: 1.03x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 94.9 ms: 1.03x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| logging_simple             | 6.40 us                                                      | 6.26 us: 1.02x faster                                                       |
| xml_etree_generate         | 85.3 ms                                                      | 83.8 ms: 1.02x faster                                                       |
| chaos                      | 61.7 ms                                                      | 60.6 ms: 1.02x faster                                                       |
| 2to3                       | 291 ms                                                       | 287 ms: 1.01x faster                                                        |
| regex_v8                   | 26.2 ms                                                      | 25.9 ms: 1.01x faster                                                       |
| richards_super             | 59.8 ms                                                      | 59.1 ms: 1.01x faster                                                       |
| typing_runtime_protocols   | 174 us                                                       | 172 us: 1.01x faster                                                        |
| logging_format             | 7.07 us                                                      | 7.00 us: 1.01x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 377 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.2 ms: 1.01x faster                                                       |
| sympy_expand               | 505 ms                                                       | 501 ms: 1.01x faster                                                        |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.01x faster                                                        |
| float                      | 81.9 ms                                                      | 81.3 ms: 1.01x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 97.3 ms: 1.00x faster                                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                                        |
| mdp                        | 2.52 sec                                                     | 2.52 sec: 1.00x faster                                                      |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.58 sec: 1.00x faster                                                      |
| sympy_integrate            | 23.3 ms                                                      | 23.5 ms: 1.01x slower                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.01x slower                                                      |
| async_generators           | 359 ms                                                       | 361 ms: 1.01x slower                                                        |
| thrift                     | 877 us                                                       | 882 us: 1.01x slower                                                        |
| python_startup             | 13.3 ms                                                      | 13.4 ms: 1.01x slower                                                       |
| deltablue                  | 3.41 ms                                                      | 3.43 ms: 1.01x slower                                                       |
| hexiom                     | 6.33 ms                                                      | 6.37 ms: 1.01x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 216 us: 1.01x slower                                                        |
| dulwich_log                | 65.5 ms                                                      | 66.0 ms: 1.01x slower                                                       |
| go                         | 160 ms                                                       | 162 ms: 1.01x slower                                                        |
| sympy_sum                  | 154 ms                                                       | 156 ms: 1.01x slower                                                        |
| pycparser                  | 1.26 sec                                                     | 1.27 sec: 1.01x slower                                                      |
| python_startup_no_site     | 8.94 ms                                                      | 9.07 ms: 1.01x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.44 sec: 1.01x slower                                                      |
| nqueens                    | 88.2 ms                                                      | 89.6 ms: 1.02x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                       |
| django_template            | 38.9 ms                                                      | 39.7 ms: 1.02x slower                                                       |
| coroutines                 | 21.6 ms                                                      | 22.1 ms: 1.02x slower                                                       |
| pyflate                    | 492 ms                                                       | 504 ms: 1.02x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 392 ms: 1.02x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 73.9 ms: 1.03x slower                                                       |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                                        |
| json                       | 5.22 ms                                                      | 5.41 ms: 1.03x slower                                                       |
| regex_effbot               | 3.37 ms                                                      | 3.50 ms: 1.04x slower                                                       |
| json_loads                 | 24.0 us                                                      | 25.0 us: 1.04x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.98 sec: 1.06x slower                                                      |
| scimark_monte_carlo        | 64.9 ms                                                      | 68.9 ms: 1.06x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.72 ms: 1.15x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (17): bench_mp_pool, tornado_http, json_dumps, richards, pickle_pure_python, xml_etree_parse, sqlglot_normalize, comprehensions, pidigits, mako, logging_silent, sqlglot_transpile, crypto_pyaes, pprint_safe_repr, fannkuch, dask, pylint
Ignored benchmarks (12) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 98.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x