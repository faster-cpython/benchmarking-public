# Results vs. 3.11.0

- fork: python
- ref: 8c094c3095feb4de2efe
- machine: linux-x86_64
- commit hash: 8c094c3
- commit date: 2024-03-13
- overall geometric mean: 1.02x faster
- HPT reliability: 70.90%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 307 ms: 1.07x slower                                                         |
| chameleon      | 7.92 ms                                                      | 7.41 ms: 1.07x faster                                                        |
| docutils       | 2.85 sec                                                     | 2.92 sec: 1.03x slower                                                       |
| html5lib       | 72.2 ms                                                      | 74.7 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 518 ms                                                       | 442 ms: 1.17x faster                                                         |
| async_tree_memoization     | 629 ms                                                       | 554 ms: 1.14x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 438 ms: 1.08x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 559 ms: 1.07x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 1.09 sec: 1.07x faster                                                       |
| async_tree_io_tg           | 1.15 sec                                                     | 1.09 sec: 1.06x faster                                                       |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 709 ms: 1.06x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 710 ms: 1.06x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                         |
| float          | 74.9 ms                                                      | 78.7 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 146 ms: 1.07x faster                                                         |
| regex_v8       | 24.4 ms                                                      | 25.5 ms: 1.04x slower                                                        |
| regex_effbot   | 3.34 ms                                                      | 3.56 ms: 1.06x slower                                                        |
| regex_dna      | 227 ms                                                       | 253 ms: 1.11x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                        |
| json_loads           | 28.9 us                                                      | 25.0 us: 1.16x faster                                                        |
| xml_etree_parse      | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| pickle_dict          | 32.3 us                                                      | 30.5 us: 1.06x faster                                                        |
| tomli_loads          | 2.25 sec                                                     | 2.14 sec: 1.05x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                       | 104 ms: 1.03x faster                                                         |
| pickle_pure_python   | 316 us                                                       | 310 us: 1.02x faster                                                         |
| unpickle_pure_python | 238 us                                                       | 234 us: 1.02x faster                                                         |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| xml_etree_process    | 55.9 ms                                                      | 58.8 ms: 1.05x slower                                                        |
| xml_etree_generate   | 79.7 ms                                                      | 86.0 ms: 1.08x slower                                                        |
| pickle_list          | 3.94 us                                                      | 4.30 us: 1.09x slower                                                        |
| unpickle             | 13.3 us                                                      | 14.9 us: 1.12x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 15.6 ms: 1.45x slower                                                        |
| python_startup_no_site | 7.73 ms                                                      | 14.1 ms: 1.82x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.62x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.0 ms                                                      | 9.75 ms: 1.13x faster                                                        |
| genshi_xml     | 57.1 ms                                                      | 60.6 ms: 1.06x slower                                                        |
| genshi_text    | 25.5 ms                                                      | 28.2 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240313-pythonperf2-x86_64-python-8c094c3095feb4de2efe-3.13.0a5+-8c094c3 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 117 us: 4.54x faster                                                         |
| asyncio_tcp                | 747 ms                                                       | 376 ms: 1.99x faster                                                         |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.94x faster                                                       |
| generators                 | 54.6 ms                                                      | 33.9 ms: 1.61x faster                                                        |
| pylint                     | 514 ms                                                       | 358 ms: 1.43x faster                                                         |
| comprehensions             | 25.1 us                                                      | 19.0 us: 1.32x faster                                                        |
| json_dumps                 | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                        |
| coroutines                 | 27.8 ms                                                      | 22.4 ms: 1.24x faster                                                        |
| async_tree_none            | 518 ms                                                       | 442 ms: 1.17x faster                                                         |
| json_loads                 | 28.9 us                                                      | 25.0 us: 1.16x faster                                                        |
| sympy_sum                  | 186 ms                                                       | 160 ms: 1.16x faster                                                         |
| async_tree_memoization     | 629 ms                                                       | 554 ms: 1.14x faster                                                         |
| richards_super             | 63.6 ms                                                      | 56.2 ms: 1.13x faster                                                        |
| mako                       | 11.0 ms                                                      | 9.75 ms: 1.13x faster                                                        |
| sympy_str                  | 337 ms                                                       | 302 ms: 1.11x faster                                                         |
| chaos                      | 74.9 ms                                                      | 67.6 ms: 1.11x faster                                                        |
| async_tree_none_tg         | 474 ms                                                       | 438 ms: 1.08x faster                                                         |
| sympy_expand               | 553 ms                                                       | 511 ms: 1.08x faster                                                         |
| thrift                     | 931 us                                                       | 862 us: 1.08x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 559 ms: 1.07x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 1.09 sec: 1.07x faster                                                       |
| logging_simple             | 7.24 us                                                      | 6.76 us: 1.07x faster                                                        |
| crypto_pyaes               | 83.3 ms                                                      | 77.8 ms: 1.07x faster                                                        |
| chameleon                  | 7.92 ms                                                      | 7.41 ms: 1.07x faster                                                        |
| regex_compile              | 156 ms                                                       | 146 ms: 1.07x faster                                                         |
| mdp                        | 2.77 sec                                                     | 2.60 sec: 1.07x faster                                                       |
| async_tree_io_tg           | 1.15 sec                                                     | 1.09 sec: 1.06x faster                                                       |
| xml_etree_parse            | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.51 ms                                                      | 1.43 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 709 ms: 1.06x faster                                                         |
| pickle_dict                | 32.3 us                                                      | 30.5 us: 1.06x faster                                                        |
| gc_traversal               | 4.15 ms                                                      | 3.92 ms: 1.06x faster                                                        |
| deepcopy                   | 391 us                                                       | 370 us: 1.06x faster                                                         |
| deltablue                  | 3.97 ms                                                      | 3.76 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 710 ms: 1.06x faster                                                         |
| fannkuch                   | 416 ms                                                       | 396 ms: 1.05x faster                                                         |
| tomli_loads                | 2.25 sec                                                     | 2.14 sec: 1.05x faster                                                       |
| sympy_integrate            | 25.8 ms                                                      | 24.6 ms: 1.05x faster                                                        |
| json                       | 5.58 ms                                                      | 5.41 ms: 1.03x faster                                                        |
| deepcopy_reduce            | 3.40 us                                                      | 3.29 us: 1.03x faster                                                        |
| sqlglot_transpile          | 1.91 ms                                                      | 1.85 ms: 1.03x faster                                                        |
| logging_format             | 7.71 us                                                      | 7.49 us: 1.03x faster                                                        |
| bench_thread_pool          | 1.00 ms                                                      | 972 us: 1.03x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                       | 104 ms: 1.03x faster                                                         |
| logging_silent             | 100 ns                                                       | 98.0 ns: 1.02x faster                                                        |
| pickle_pure_python         | 316 us                                                       | 310 us: 1.02x faster                                                         |
| unpickle_pure_python       | 238 us                                                       | 234 us: 1.02x faster                                                         |
| asyncio_websockets         | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| dask                       | 410 ms                                                       | 406 ms: 1.01x faster                                                         |
| spectral_norm              | 95.1 ms                                                      | 94.4 ms: 1.01x faster                                                        |
| meteor_contest             | 131 ms                                                       | 131 ms: 1.01x slower                                                         |
| raytrace                   | 309 ms                                                       | 312 ms: 1.01x slower                                                         |
| richards                   | 49.7 ms                                                      | 50.5 ms: 1.02x slower                                                        |
| dulwich_log                | 67.4 ms                                                      | 68.7 ms: 1.02x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.4 ms: 1.03x slower                                                        |
| docutils                   | 2.85 sec                                                     | 2.92 sec: 1.03x slower                                                       |
| pprint_pformat             | 1.67 sec                                                     | 1.72 sec: 1.03x slower                                                       |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.19 ms: 1.03x slower                                                        |
| html5lib                   | 72.2 ms                                                      | 74.7 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 805 ms                                                       | 836 ms: 1.04x slower                                                         |
| hexiom                     | 6.98 ms                                                      | 7.25 ms: 1.04x slower                                                        |
| pidigits                   | 251 ms                                                       | 261 ms: 1.04x slower                                                         |
| pickle                     | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| regex_v8                   | 24.4 ms                                                      | 25.5 ms: 1.04x slower                                                        |
| float                      | 74.9 ms                                                      | 78.7 ms: 1.05x slower                                                        |
| xml_etree_process          | 55.9 ms                                                      | 58.8 ms: 1.05x slower                                                        |
| sqlglot_normalize          | 122 ms                                                       | 128 ms: 1.05x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 60.6 ms: 1.06x slower                                                        |
| regex_effbot               | 3.34 ms                                                      | 3.56 ms: 1.06x slower                                                        |
| sqlite_synth               | 2.52 us                                                      | 2.69 us: 1.06x slower                                                        |
| 2to3                       | 287 ms                                                       | 307 ms: 1.07x slower                                                         |
| scimark_lu                 | 114 ms                                                       | 122 ms: 1.07x slower                                                         |
| sqlglot_optimize           | 59.0 ms                                                      | 63.3 ms: 1.07x slower                                                        |
| xml_etree_generate         | 79.7 ms                                                      | 86.0 ms: 1.08x slower                                                        |
| scimark_monte_carlo        | 69.8 ms                                                      | 76.2 ms: 1.09x slower                                                        |
| pickle_list                | 3.94 us                                                      | 4.30 us: 1.09x slower                                                        |
| go                         | 158 ms                                                       | 174 ms: 1.10x slower                                                         |
| genshi_text                | 25.5 ms                                                      | 28.2 ms: 1.11x slower                                                        |
| regex_dna                  | 227 ms                                                       | 253 ms: 1.11x slower                                                         |
| unpickle                   | 13.3 us                                                      | 14.9 us: 1.12x slower                                                        |
| gunicorn                   | 966 us                                                       | 1.09 ms: 1.13x slower                                                        |
| aiohttp                    | 986 us                                                       | 1.12 ms: 1.14x slower                                                        |
| scimark_fft                | 281 ms                                                       | 325 ms: 1.16x slower                                                         |
| pyflate                    | 449 ms                                                       | 524 ms: 1.17x slower                                                         |
| telco                      | 6.81 ms                                                      | 8.13 ms: 1.19x slower                                                        |
| async_generators           | 322 ms                                                       | 384 ms: 1.19x slower                                                         |
| mypy2                      | 762 ms                                                       | 915 ms: 1.20x slower                                                         |
| coverage                   | 66.1 ms                                                      | 80.3 ms: 1.21x slower                                                        |
| unpack_sequence            | 45.7 ns                                                      | 62.2 ns: 1.36x slower                                                        |
| scimark_sor                | 110 ms                                                       | 152 ms: 1.39x slower                                                         |
| python_startup             | 10.7 ms                                                      | 15.6 ms: 1.45x slower                                                        |
| bench_mp_pool              | 4.70 ms                                                      | 7.02 ms: 1.49x slower                                                        |
| python_startup_no_site     | 7.73 ms                                                      | 14.1 ms: 1.82x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (8): nqueens, unpickle_list, deepcopy_memo, pycparser, create_gc_cycles, django_template, tornado_http, nbody
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 70.90% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.25x