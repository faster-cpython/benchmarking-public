# Results vs. 3.13.0

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-x86_64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.02x faster
- HPT reliability: 99.80%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 289 ms: 1.01x faster                                                        |
| docutils       | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| html5lib       | 71.9 ms                                                      | 73.4 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| async_tree_io_tg           | 819 ms                                                       | 766 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                        |
| async_tree_io              | 847 ms                                                       | 796 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                        |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                                        |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.06x faster                                                                |

Benchmark hidden because not significant (1): asyncio_tcp_ssl

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 79.9 ms: 1.03x faster                                                       |
| nbody          | 88.0 ms                                                      | 90.9 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| regex_dna      | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| regex_v8       | 26.2 ms                                                      | 26.3 ms: 1.00x slower                                                       |
| regex_effbot   | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| xml_etree_process    | 60.9 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| pickle_pure_python   | 318 us                                                       | 313 us: 1.02x faster                                                        |
| xml_etree_parse      | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| xml_etree_generate   | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| json_dumps           | 11.0 ms                                                      | 11.0 ms: 1.00x slower                                                       |
| tomli_loads          | 2.41 sec                                                     | 2.43 sec: 1.01x slower                                                      |
| unpickle_pure_python | 214 us                                                       | 224 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| json_loads           | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| python_startup_no_site | 8.94 ms                                                      | 9.11 ms: 1.02x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.02x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text    | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                       |
| genshi_xml     | 57.3 ms                                                      | 56.0 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240717-pythonperf2-x86_64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| deepcopy                   | 397 us                                                       | 283 us: 1.40x faster                                                        |
| deepcopy_memo              | 39.5 us                                                      | 29.3 us: 1.35x faster                                                       |
| deepcopy_reduce            | 3.54 us                                                      | 2.89 us: 1.23x faster                                                       |
| async_tree_memoization_tg  | 461 ms                                                       | 382 ms: 1.21x faster                                                        |
| scimark_sor                | 126 ms                                                       | 110 ms: 1.14x faster                                                        |
| async_tree_memoization     | 452 ms                                                       | 403 ms: 1.12x faster                                                        |
| async_tree_none_tg         | 340 ms                                                       | 303 ms: 1.12x faster                                                        |
| async_tree_none            | 372 ms                                                       | 336 ms: 1.11x faster                                                        |
| pathlib                    | 17.4 ms                                                      | 15.9 ms: 1.09x faster                                                       |
| async_tree_io_tg           | 819 ms                                                       | 766 ms: 1.07x faster                                                        |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 539 ms: 1.07x faster                                                        |
| async_tree_io              | 847 ms                                                       | 796 ms: 1.06x faster                                                        |
| raytrace                   | 289 ms                                                       | 272 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.04 ms: 1.06x faster                                                       |
| genshi_text                | 26.6 ms                                                      | 25.2 ms: 1.06x faster                                                       |
| pyflate                    | 492 ms                                                       | 468 ms: 1.05x faster                                                        |
| telco                      | 8.58 ms                                                      | 8.27 ms: 1.04x faster                                                       |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 578 ms: 1.04x faster                                                        |
| scimark_fft                | 314 ms                                                       | 303 ms: 1.04x faster                                                        |
| meteor_contest             | 128 ms                                                       | 124 ms: 1.04x faster                                                        |
| bpe_tokeniser              | 5.10 sec                                                     | 4.93 sec: 1.03x faster                                                      |
| richards_super             | 59.8 ms                                                      | 57.9 ms: 1.03x faster                                                       |
| bench_thread_pool          | 901 us                                                       | 875 us: 1.03x faster                                                        |
| typing_runtime_protocols   | 174 us                                                       | 169 us: 1.03x faster                                                        |
| go                         | 160 ms                                                       | 156 ms: 1.03x faster                                                        |
| regex_compile              | 144 ms                                                       | 140 ms: 1.03x faster                                                        |
| float                      | 81.9 ms                                                      | 79.9 ms: 1.03x faster                                                       |
| coroutines                 | 21.6 ms                                                      | 21.1 ms: 1.03x faster                                                       |
| richards                   | 52.7 ms                                                      | 51.5 ms: 1.02x faster                                                       |
| genshi_xml                 | 57.3 ms                                                      | 56.0 ms: 1.02x faster                                                       |
| asyncio_tcp                | 380 ms                                                       | 373 ms: 1.02x faster                                                        |
| hexiom                     | 6.33 ms                                                      | 6.21 ms: 1.02x faster                                                       |
| xml_etree_process          | 60.9 ms                                                      | 59.8 ms: 1.02x faster                                                       |
| scimark_lu                 | 97.8 ms                                                      | 96.1 ms: 1.02x faster                                                       |
| comprehensions             | 17.3 us                                                      | 17.0 us: 1.02x faster                                                       |
| logging_format             | 7.07 us                                                      | 6.96 us: 1.02x faster                                                       |
| crypto_pyaes               | 72.8 ms                                                      | 71.6 ms: 1.02x faster                                                       |
| pickle_pure_python         | 318 us                                                       | 313 us: 1.02x faster                                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 58.8 ms: 1.02x faster                                                       |
| logging_simple             | 6.40 us                                                      | 6.31 us: 1.01x faster                                                       |
| xml_etree_parse            | 145 ms                                                       | 143 ms: 1.01x faster                                                        |
| regex_dna                  | 244 ms                                                       | 241 ms: 1.01x faster                                                        |
| spectral_norm              | 97.4 ms                                                      | 96.4 ms: 1.01x faster                                                       |
| mdp                        | 2.52 sec                                                     | 2.50 sec: 1.01x faster                                                      |
| xml_etree_generate         | 85.3 ms                                                      | 84.5 ms: 1.01x faster                                                       |
| coverage                   | 81.1 ms                                                      | 80.6 ms: 1.01x faster                                                       |
| 2to3                       | 291 ms                                                       | 289 ms: 1.01x faster                                                        |
| sympy_str                  | 296 ms                                                       | 294 ms: 1.01x faster                                                        |
| chaos                      | 61.7 ms                                                      | 61.4 ms: 1.00x faster                                                       |
| sympy_integrate            | 23.3 ms                                                      | 23.2 ms: 1.00x faster                                                       |
| scimark_monte_carlo        | 64.9 ms                                                      | 65.0 ms: 1.00x slower                                                       |
| json_dumps                 | 11.0 ms                                                      | 11.0 ms: 1.00x slower                                                       |
| regex_v8                   | 26.2 ms                                                      | 26.3 ms: 1.00x slower                                                       |
| sqlglot_normalize          | 118 ms                                                       | 119 ms: 1.00x slower                                                        |
| pprint_safe_repr           | 812 ms                                                       | 817 ms: 1.01x slower                                                        |
| async_generators           | 359 ms                                                       | 362 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                      |
| tomli_loads                | 2.41 sec                                                     | 2.43 sec: 1.01x slower                                                      |
| python_startup             | 13.3 ms                                                      | 13.5 ms: 1.01x slower                                                       |
| generators                 | 33.5 ms                                                      | 33.9 ms: 1.01x slower                                                       |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.01x slower                                                       |
| sympy_sum                  | 154 ms                                                       | 156 ms: 1.01x slower                                                        |
| python_startup_no_site     | 8.94 ms                                                      | 9.11 ms: 1.02x slower                                                       |
| html5lib                   | 71.9 ms                                                      | 73.4 ms: 1.02x slower                                                       |
| asyncio_websockets         | 382 ms                                                       | 390 ms: 1.02x slower                                                        |
| thrift                     | 877 us                                                       | 900 us: 1.03x slower                                                        |
| json                       | 5.22 ms                                                      | 5.38 ms: 1.03x slower                                                       |
| nbody                      | 88.0 ms                                                      | 90.9 ms: 1.03x slower                                                       |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                       |
| dulwich_log                | 65.5 ms                                                      | 68.2 ms: 1.04x slower                                                       |
| unpickle_pure_python       | 214 us                                                       | 224 us: 1.04x slower                                                        |
| xml_etree_iterparse        | 100 ms                                                       | 105 ms: 1.05x slower                                                        |
| regex_effbot               | 3.37 ms                                                      | 3.56 ms: 1.06x slower                                                       |
| docutils                   | 2.81 sec                                                     | 2.97 sec: 1.06x slower                                                      |
| json_loads                 | 24.0 us                                                      | 25.4 us: 1.06x slower                                                       |
| gc_traversal               | 4.11 ms                                                      | 4.48 ms: 1.09x slower                                                       |
| create_gc_cycles           | 1.76 ms                                                      | 2.00 ms: 1.14x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                |

Benchmark hidden because not significant (13): pylint, tornado_http, pycparser, asyncio_tcp_ssl, nqueens, deltablue, sympy_expand, django_template, pidigits, fannkuch, logging_silent, bench_mp_pool, mako
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 99.80% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x