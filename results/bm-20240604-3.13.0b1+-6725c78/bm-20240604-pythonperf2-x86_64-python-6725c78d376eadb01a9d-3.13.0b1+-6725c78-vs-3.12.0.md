# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.00x slower
- HPT reliability: 78.97%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.00 sec: 1.04x slower                                                       |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 430 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.24x faster                                                         |
| async_tree_none            | 452 ms                                                       | 372 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 882 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                        |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.8 us: 1.06x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                                         |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                                         |
| xml_etree_generate   | 86.1 ms                                                      | 86.8 ms: 1.01x slower                                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| unpickle_list        | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.4 ms: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                        |
| unpickle             | 14.8 us                                                      | 15.8 us: 1.07x slower                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (3): pickle_list, json_loads, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 430 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 346 ms: 1.24x faster                                                         |
| async_tree_none            | 452 ms                                                       | 372 ms: 1.22x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 882 ms: 1.18x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 906 ms: 1.16x faster                                                         |
| generators                 | 37.4 ms                                                      | 32.7 ms: 1.15x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 615 ms: 1.13x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 73.4 ms: 1.09x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                        |
| mypy2                      | 830 ms                                                       | 767 ms: 1.08x faster                                                         |
| raytrace                   | 298 ms                                                       | 277 ms: 1.08x faster                                                         |
| async_generators           | 390 ms                                                       | 363 ms: 1.07x faster                                                         |
| logging_format             | 7.48 us                                                      | 6.99 us: 1.07x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.31 us: 1.06x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.9 ms: 1.06x faster                                                        |
| bench_thread_pool          | 950 us                                                       | 898 us: 1.06x faster                                                         |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 30.8 us: 1.06x faster                                                        |
| chaos                      | 64.0 ms                                                      | 60.7 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.04x faster                                                       |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                                        |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                                         |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                                         |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| pycparser                  | 1.23 sec                                                     | 1.21 sec: 1.02x faster                                                       |
| nqueens                    | 89.9 ms                                                      | 88.9 ms: 1.01x faster                                                        |
| meteor_contest             | 128 ms                                                       | 127 ms: 1.01x faster                                                         |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 86.8 ms: 1.01x slower                                                        |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.42 us: 1.01x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.27 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.83 ms: 1.02x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 825 ms: 1.02x slower                                                         |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 37.6 us: 1.02x slower                                                        |
| fannkuch                   | 350 ms                                                       | 358 ms: 1.02x slower                                                         |
| dulwich_log                | 65.4 ms                                                      | 67.0 ms: 1.03x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 96.8 ns: 1.03x slower                                                        |
| regex_effbot               | 3.57 ms                                                      | 3.67 ms: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                                        |
| unpickle_list              | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.85 us: 1.03x slower                                                        |
| sqlglot_normalize          | 116 ms                                                       | 119 ms: 1.03x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.4 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.29 ms: 1.03x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                                        |
| deepcopy                   | 368 us                                                       | 382 us: 1.04x slower                                                         |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                                         |
| scimark_fft                | 301 ms                                                       | 313 ms: 1.04x slower                                                         |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                                        |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                         |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.00 sec: 1.04x slower                                                       |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.05x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                                        |
| float                      | 76.6 ms                                                      | 81.0 ms: 1.06x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.8 us: 1.07x slower                                                        |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 98.6 ms: 1.08x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.44 ms: 1.08x slower                                                        |
| pyflate                    | 439 ms                                                       | 478 ms: 1.09x slower                                                         |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                                         |
| tomli_loads                | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                                       |
| regex_v8                   | 23.6 ms                                                      | 26.5 ms: 1.12x slower                                                        |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                                         |
| richards                   | 45.7 ms                                                      | 53.1 ms: 1.16x slower                                                        |
| richards_super             | 51.3 ms                                                      | 59.8 ms: 1.17x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.41 ms: 1.21x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.01 ms: 1.26x slower                                                        |
| coverage                   | 66.7 ms                                                      | 85.3 ms: 1.28x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.51 ms: 1.30x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (11): scimark_lu, pickle_list, json_loads, regex_compile, django_template, dask, asyncio_websockets, sqlglot_transpile, xml_etree_iterparse, nbody, bench_mp_pool
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 78.97% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x