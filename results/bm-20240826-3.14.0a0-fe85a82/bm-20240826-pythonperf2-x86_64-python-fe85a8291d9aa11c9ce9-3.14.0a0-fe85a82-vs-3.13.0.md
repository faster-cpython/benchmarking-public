# Results vs. 3.13.0

- fork: python
- ref: fe85a8291d9aa11c9ce9
- machine: linux-x86_64
- commit hash: fe85a82
- commit date: 2024-08-26
- overall geometric mean: 1.02x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 281 ms: 1.04x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.95 sec: 1.05x slower                                                      |
| html5lib       | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                       |
| tornado_http   | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| async_generators           | 359 ms                                                       | 363 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.5 ms: 1.03x faster                                                       |
| nbody          | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 27.1 ms: 1.04x slower                                                       |
| regex_dna      | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| xml_etree_process    | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                       |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                                        |
| unpickle_pure_python | 214 us                                                       | 213 us: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| json_loads           | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| genshi_xml      | 57.3 ms                                                      | 56.2 ms: 1.02x faster                                                       |
| django_template | 38.9 ms                                                      | 40.4 ms: 1.04x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240826-pythonperf2-x86_64-python-fe85a8291d9aa11c9ce9-3.14.0a0-fe85a82 |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 291 us: 1.37x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.8 us: 1.32x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.95 us: 1.20x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 392 ms: 1.18x faster                                                        |
| generators                 | 33.5 ms                                                      | 28.5 ms: 1.18x faster                                                       |
| async_tree_none            | 372 ms                                                       | 319 ms: 1.17x faster                                                        |
| scimark_sor                | 126 ms                                                       | 110 ms: 1.14x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 401 ms: 1.13x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 308 ms: 1.10x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.8 ms: 1.10x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 24.6 ms: 1.08x faster                                                       |
| richards_super             | 59.8 ms                                                      | 55.7 ms: 1.07x faster                                                       |
| raytrace                   | 289 ms                                                       | 272 ms: 1.06x faster                                                        |
| richards                   | 52.7 ms                                                      | 49.6 ms: 1.06x faster                                                       |
| async_tree_io              | 847 ms                                                       | 802 ms: 1.05x faster                                                        |
| bench_thread_pool          | 901 us                                                       | 856 us: 1.05x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 571 ms: 1.05x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 547 ms: 1.05x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.86 sec: 1.05x faster                                                      |
| pyflate                    | 492 ms                                                       | 471 ms: 1.04x faster                                                        |
| bench_mp_pool              | 4.65 ms                                                      | 4.48 ms: 1.04x faster                                                       |
| telco                      | 8.58 ms                                                      | 8.26 ms: 1.04x faster                                                       |
| thrift                     | 877 us                                                       | 846 us: 1.04x faster                                                        |
| 2to3                       | 291 ms                                                       | 281 ms: 1.04x faster                                                        |
| tornado_http               | 120 ms                                                       | 116 ms: 1.03x faster                                                        |
| scimark_lu                 | 97.8 ms                                                      | 94.7 ms: 1.03x faster                                                       |
| scimark_fft                | 314 ms                                                       | 304 ms: 1.03x faster                                                        |
| asyncio_tcp                | 380 ms                                                       | 369 ms: 1.03x faster                                                        |
| float                      | 81.9 ms                                                      | 79.5 ms: 1.03x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 795 ms: 1.03x faster                                                        |
| json_dumps                 | 11.0 ms                                                      | 10.6 ms: 1.03x faster                                                       |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.03x faster                                                      |
| fannkuch                   | 365 ms                                                       | 356 ms: 1.03x faster                                                        |
| nbody                      | 88.0 ms                                                      | 85.9 ms: 1.02x faster                                                       |
| regex_compile              | 144 ms                                                       | 141 ms: 1.02x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 170 us: 1.02x faster                                                        |
| sympy_sum                  | 154 ms                                                       | 150 ms: 1.02x faster                                                        |
| xml_etree_process          | 60.9 ms                                                      | 59.5 ms: 1.02x faster                                                       |
| sympy_str                  | 296 ms                                                       | 290 ms: 1.02x faster                                                        |
| genshi_xml                 | 57.3 ms                                                      | 56.2 ms: 1.02x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 22.9 ms: 1.02x faster                                                       |
| deltablue                  | 3.41 ms                                                      | 3.35 ms: 1.02x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.3 ms: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 812 ms                                                       | 804 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 59.2 ms: 1.01x faster                                                       |
| chaos                      | 61.7 ms                                                      | 61.2 ms: 1.01x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                                        |
| unpickle_pure_python       | 214 us                                                       | 213 us: 1.01x faster                                                        |
| xml_etree_generate         | 85.3 ms                                                      | 84.7 ms: 1.01x faster                                                       |
| hexiom                     | 6.33 ms                                                      | 6.29 ms: 1.01x faster                                                       |
| spectral_norm              | 97.4 ms                                                      | 96.7 ms: 1.01x faster                                                       |
| nqueens                    | 88.2 ms                                                      | 87.7 ms: 1.01x faster                                                       |
| pprint_pformat             | 1.65 sec                                                     | 1.64 sec: 1.00x faster                                                      |
| sympy_expand               | 505 ms                                                       | 502 ms: 1.00x faster                                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.57 sec: 1.00x faster                                                      |
| crypto_pyaes               | 72.8 ms                                                      | 73.0 ms: 1.00x slower                                                       |
| logging_simple             | 6.40 us                                                      | 6.44 us: 1.01x slower                                                       |
| python_startup_no_site     | 8.94 ms                                                      | 9.02 ms: 1.01x slower                                                       |
| coverage                   | 81.1 ms                                                      | 81.8 ms: 1.01x slower                                                       |
| async_generators           | 359 ms                                                       | 363 ms: 1.01x slower                                                        |
| html5lib                   | 71.9 ms                                                      | 72.7 ms: 1.01x slower                                                       |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.33 ms: 1.01x slower                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.7 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                                       |
| comprehensions             | 17.3 us                                                      | 17.5 us: 1.01x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 120 ms: 1.02x slower                                                        |
| json                       | 5.22 ms                                                      | 5.34 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 395 ms: 1.03x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.03x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 27.1 ms: 1.04x slower                                                       |
| django_template            | 38.9 ms                                                      | 40.4 ms: 1.04x slower                                                       |
| regex_dna                  | 244 ms                                                       | 254 ms: 1.04x slower                                                        |
| json_loads                 | 24.0 us                                                      | 25.1 us: 1.05x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.95 sec: 1.05x slower                                                      |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                                       |
| tomli_loads                | 2.41 sec                                                     | 2.58 sec: 1.07x slower                                                      |
| create_gc_cycles           | 1.76 ms                                                      | 1.89 ms: 1.08x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.43 ms: 1.08x slower                                                       |
| go                         | 160 ms                                                       | 179 ms: 1.12x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (9): mako, pidigits, mdp, python_startup, meteor_contest, logging_silent, logging_format, xml_etree_iterparse, pylint
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x