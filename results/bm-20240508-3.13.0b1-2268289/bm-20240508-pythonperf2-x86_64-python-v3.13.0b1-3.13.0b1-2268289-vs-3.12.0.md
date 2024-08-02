# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b1
- machine: linux-x86_64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.04x slower
- HPT reliability: 97.85%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 290 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                            |
| docutils       | 2.87 sec                                                     | 3.03 sec: 1.06x slower                                           |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                             |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 444 ms: 1.22x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 870 ms: 1.20x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 889 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.17x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 619 ms: 1.12x faster                                             |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 252 ms: 1.05x faster                                             |
| float          | 76.6 ms                                                      | 81.1 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                            |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                             |
| regex_compile  | 144 ms                                                       | 147 ms: 1.02x slower                                             |
| regex_v8       | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                            |
| Geometric mean | (ref)                                                        | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 31.2 us: 1.04x faster                                            |
| pickle               | 10.5 us                                                      | 10.4 us: 1.01x faster                                            |
| json_loads           | 24.4 us                                                      | 24.4 us: 1.00x slower                                            |
| pickle_list          | 4.43 us                                                      | 4.49 us: 1.01x slower                                            |
| unpickle_list        | 4.66 us                                                      | 4.75 us: 1.02x slower                                            |
| xml_etree_generate   | 86.1 ms                                                      | 88.9 ms: 1.03x slower                                            |
| xml_etree_process    | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                            |
| unpickle             | 14.8 us                                                      | 15.5 us: 1.05x slower                                            |
| unpickle_pure_python | 210 us                                                       | 222 us: 1.06x slower                                             |
| json_dumps           | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                           |
| Geometric mean       | (ref)                                                        | 1.03x slower                                                     |

Benchmark hidden because not significant (3): pickle_pure_python, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                            |
| python_startup         | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| Geometric mean         | (ref)                                                        | 1.07x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                            |
| mako            | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                            |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.1 us: 1.28x faster                                            |
| async_tree_none_tg         | 431 ms                                                       | 345 ms: 1.25x faster                                             |
| async_tree_none            | 452 ms                                                       | 371 ms: 1.22x faster                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 444 ms: 1.22x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 870 ms: 1.20x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 586 ms: 1.19x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 889 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.17x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 619 ms: 1.12x faster                                             |
| generators                 | 37.4 ms                                                      | 33.3 ms: 1.12x faster                                            |
| raytrace                   | 298 ms                                                       | 268 ms: 1.11x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 72.9 ms: 1.10x faster                                            |
| pathlib                    | 18.9 ms                                                      | 17.3 ms: 1.09x faster                                            |
| chaos                      | 64.0 ms                                                      | 59.4 ms: 1.08x faster                                            |
| coroutines                 | 23.0 ms                                                      | 21.5 ms: 1.07x faster                                            |
| mypy2                      | 830 ms                                                       | 780 ms: 1.06x faster                                             |
| async_generators           | 390 ms                                                       | 367 ms: 1.06x faster                                             |
| bench_thread_pool          | 950 us                                                       | 895 us: 1.06x faster                                             |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                            |
| pidigits                   | 265 ms                                                       | 252 ms: 1.05x faster                                             |
| pickle_dict                | 32.5 us                                                      | 31.2 us: 1.04x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.50 us: 1.03x faster                                            |
| sympy_sum                  | 162 ms                                                       | 157 ms: 1.03x faster                                             |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                           |
| pickle                     | 10.5 us                                                      | 10.4 us: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| sympy_integrate            | 23.9 ms                                                      | 23.8 ms: 1.01x faster                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.19 ms: 1.01x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                            |
| json_loads                 | 24.4 us                                                      | 24.4 us: 1.00x slower                                            |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                             |
| dask                       | 392 ms                                                       | 396 ms: 1.01x slower                                             |
| nqueens                    | 89.9 ms                                                      | 91.1 ms: 1.01x slower                                            |
| pickle_list                | 4.43 us                                                      | 4.49 us: 1.01x slower                                            |
| asyncio_websockets         | 387 ms                                                       | 393 ms: 1.01x slower                                             |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                             |
| 2to3                       | 285 ms                                                       | 290 ms: 1.02x slower                                             |
| unpickle_list              | 4.66 us                                                      | 4.75 us: 1.02x slower                                            |
| sqlite_synth               | 2.77 us                                                      | 2.83 us: 1.02x slower                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.69 sec: 1.02x slower                                           |
| scimark_lu                 | 98.8 ms                                                      | 101 ms: 1.02x slower                                             |
| logging_silent             | 94.4 ns                                                      | 96.6 ns: 1.02x slower                                            |
| regex_compile              | 144 ms                                                       | 147 ms: 1.02x slower                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.86 ms: 1.03x slower                                            |
| pprint_safe_repr           | 807 ms                                                       | 830 ms: 1.03x slower                                             |
| pycparser                  | 1.23 sec                                                     | 1.27 sec: 1.03x slower                                           |
| xml_etree_generate         | 86.1 ms                                                      | 88.9 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.83 ms: 1.03x slower                                            |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.48 us: 1.03x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 67.6 ms: 1.03x slower                                            |
| django_template            | 38.2 ms                                                      | 39.5 ms: 1.03x slower                                            |
| xml_etree_process          | 58.4 ms                                                      | 60.6 ms: 1.04x slower                                            |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                            |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.44 ms: 1.05x slower                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 60.1 ms: 1.05x slower                                            |
| json                       | 5.12 ms                                                      | 5.36 ms: 1.05x slower                                            |
| unpickle                   | 14.8 us                                                      | 15.5 us: 1.05x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.39 ms: 1.05x slower                                            |
| mako                       | 10.0 ms                                                      | 10.5 ms: 1.05x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 121 ms: 1.05x slower                                             |
| docutils                   | 2.87 sec                                                     | 3.03 sec: 1.06x slower                                           |
| float                      | 76.6 ms                                                      | 81.1 ms: 1.06x slower                                            |
| chameleon                  | 7.23 ms                                                      | 7.66 ms: 1.06x slower                                            |
| aiohttp                    | 1.02 ms                                                      | 1.08 ms: 1.06x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 222 us: 1.06x slower                                             |
| sympy_expand               | 484 ms                                                       | 514 ms: 1.06x slower                                             |
| spectral_norm              | 91.6 ms                                                      | 97.5 ms: 1.06x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 10.9 ms: 1.07x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.37 ms: 1.07x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 39.4 us: 1.07x slower                                            |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                             |
| deepcopy                   | 368 us                                                       | 395 us: 1.07x slower                                             |
| scimark_sor                | 109 ms                                                       | 117 ms: 1.07x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 25.6 ms: 1.08x slower                                            |
| scimark_fft                | 301 ms                                                       | 328 ms: 1.09x slower                                             |
| pyflate                    | 439 ms                                                       | 480 ms: 1.10x slower                                             |
| python_startup             | 11.6 ms                                                      | 12.9 ms: 1.11x slower                                            |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                             |
| richards                   | 45.7 ms                                                      | 54.0 ms: 1.18x slower                                            |
| richards_super             | 51.3 ms                                                      | 61.0 ms: 1.19x slower                                            |
| tomli_loads                | 2.16 sec                                                     | 2.58 sec: 1.19x slower                                           |
| coverage                   | 66.7 ms                                                      | 83.7 ms: 1.25x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.02 ms: 1.27x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 4.66 ms: 1.34x slower                                            |
| telco                      | 6.96 ms                                                      | 175 ms: 25.08x slower                                            |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (8): tornado_http, pickle_pure_python, sympy_str, xml_etree_iterparse, xml_etree_parse, bench_mp_pool, scimark_monte_carlo, nbody
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-pythonperf2-x86_64-python-v3.13.0b1-3.13.0b1-2268289.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 97.85% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x