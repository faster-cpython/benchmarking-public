# Results vs. 3.12.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: 74c8568
- commit date: 2024-03-27
- overall geometric mean: 1.05x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 267 ms: 1.03x faster                                         |
| chameleon      | 7.41 ms                                                | 6.82 ms: 1.09x faster                                        |
| tornado_http   | 103 ms                                                 | 94.8 ms: 1.08x faster                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                         |
| async_tree_memoization     | 578 ms                                                 | 440 ms: 1.31x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 445 ms: 1.29x faster                                         |
| async_tree_io              | 1.16 sec                                               | 915 ms: 1.26x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 577 ms: 1.26x faster                                         |
| async_tree_none            | 472 ms                                                 | 381 ms: 1.24x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                         |
| Geometric mean             | (ref)                                                  | 1.28x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 84.7 ms                                                | 76.6 ms: 1.11x faster                                        |
| nbody          | 97.0 ms                                                | 88.3 ms: 1.10x faster                                        |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 133 ms: 1.12x faster                                         |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.06x slower                                        |
| regex_dna      | 212 ms                                                 | 230 ms: 1.09x slower                                         |
| regex_v8       | 23.1 ms                                                | 26.0 ms: 1.13x slower                                        |
| Geometric mean | (ref)                                                  | 1.04x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 324 us                                                 | 297 us: 1.09x faster                                         |
| unpickle_pure_python | 230 us                                                 | 215 us: 1.07x faster                                         |
| tomli_loads          | 2.33 sec                                               | 2.20 sec: 1.06x faster                                       |
| xml_etree_generate   | 89.2 ms                                                | 85.8 ms: 1.04x faster                                        |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                        |
| unpickle_list        | 5.29 us                                                | 5.26 us: 1.00x faster                                        |
| pickle_dict          | 35.5 us                                                | 35.6 us: 1.00x slower                                        |
| json_loads           | 28.5 us                                                | 28.6 us: 1.00x slower                                        |
| json_dumps           | 10.4 ms                                                | 10.4 ms: 1.01x slower                                        |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                         |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                        |
| unpickle             | 15.9 us                                                | 16.7 us: 1.05x slower                                        |
| pickle_list          | 5.08 us                                                | 5.40 us: 1.06x slower                                        |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 10.6 ms: 1.11x slower                                        |
| python_startup_no_site | 6.94 ms                                                | 9.00 ms: 1.30x slower                                        |
| Geometric mean         | (ref)                                                  | 1.20x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                        |
| django_template | 34.6 ms                                                | 34.8 ms: 1.01x slower                                        |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 111 us: 1.42x faster                                         |
| async_tree_none_tg         | 450 ms                                                 | 338 ms: 1.33x faster                                         |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                        |
| async_tree_memoization     | 578 ms                                                 | 440 ms: 1.31x faster                                         |
| async_tree_io_tg           | 1.18 sec                                               | 914 ms: 1.29x faster                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 445 ms: 1.29x faster                                         |
| async_tree_io              | 1.16 sec                                               | 915 ms: 1.26x faster                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 577 ms: 1.26x faster                                         |
| async_tree_none            | 472 ms                                                 | 381 ms: 1.24x faster                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                         |
| unpack_sequence            | 54.0 ns                                                | 44.4 ns: 1.21x faster                                        |
| raytrace                   | 312 ms                                                 | 263 ms: 1.19x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.26 ms: 1.14x faster                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                        |
| mypy2                      | 830 ms                                                 | 733 ms: 1.13x faster                                         |
| chaos                      | 67.0 ms                                                | 59.7 ms: 1.12x faster                                        |
| crypto_pyaes               | 81.9 ms                                                | 73.1 ms: 1.12x faster                                        |
| regex_compile              | 148 ms                                                 | 133 ms: 1.12x faster                                         |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                        |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.11x faster                                         |
| float                      | 84.7 ms                                                | 76.6 ms: 1.11x faster                                        |
| deepcopy_memo              | 40.7 us                                                | 37.0 us: 1.10x faster                                        |
| sympy_str                  | 300 ms                                                 | 272 ms: 1.10x faster                                         |
| logging_simple             | 6.46 us                                                | 5.87 us: 1.10x faster                                        |
| nbody                      | 97.0 ms                                                | 88.3 ms: 1.10x faster                                        |
| logging_format             | 7.23 us                                                | 6.59 us: 1.10x faster                                        |
| pickle_pure_python         | 324 us                                                 | 297 us: 1.09x faster                                         |
| chameleon                  | 7.41 ms                                                | 6.82 ms: 1.09x faster                                        |
| tornado_http               | 103 ms                                                 | 94.8 ms: 1.08x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 3.10 us: 1.08x faster                                        |
| unpickle_pure_python       | 230 us                                                 | 215 us: 1.07x faster                                         |
| deepcopy                   | 371 us                                                 | 347 us: 1.07x faster                                         |
| sympy_integrate            | 21.4 ms                                                | 20.0 ms: 1.07x faster                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.58 ms: 1.07x faster                                        |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                         |
| fannkuch                   | 417 ms                                                 | 391 ms: 1.07x faster                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                        |
| tomli_loads                | 2.33 sec                                               | 2.20 sec: 1.06x faster                                       |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                        |
| scimark_sor                | 129 ms                                                 | 122 ms: 1.06x faster                                         |
| logging_silent             | 104 ns                                                 | 98.9 ns: 1.06x faster                                        |
| async_generators           | 463 ms                                                 | 441 ms: 1.05x faster                                         |
| pprint_safe_repr           | 776 ms                                                 | 740 ms: 1.05x faster                                         |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                         |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                       |
| pathlib                    | 19.3 ms                                                | 18.5 ms: 1.04x faster                                        |
| pyflate                    | 482 ms                                                 | 464 ms: 1.04x faster                                         |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 85.8 ms: 1.04x faster                                        |
| sympy_expand               | 478 ms                                                 | 461 ms: 1.04x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                        |
| nqueens                    | 83.3 ms                                                | 80.5 ms: 1.03x faster                                        |
| meteor_contest             | 112 ms                                                 | 109 ms: 1.03x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                        |
| 2to3                       | 274 ms                                                 | 267 ms: 1.03x faster                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.95 ms: 1.02x faster                                        |
| bench_thread_pool          | 842 us                                                 | 825 us: 1.02x faster                                         |
| dulwich_log                | 68.5 ms                                                | 67.3 ms: 1.02x faster                                        |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.01x faster                                         |
| dask                       | 372 ms                                                 | 367 ms: 1.01x faster                                         |
| richards                   | 45.8 ms                                                | 45.4 ms: 1.01x faster                                        |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                        |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| richards_super             | 51.5 ms                                                | 51.2 ms: 1.01x faster                                        |
| unpickle_list              | 5.29 us                                                | 5.26 us: 1.00x faster                                        |
| pickle_dict                | 35.5 us                                                | 35.6 us: 1.00x slower                                        |
| json_loads                 | 28.5 us                                                | 28.6 us: 1.00x slower                                        |
| django_template            | 34.6 ms                                                | 34.8 ms: 1.01x slower                                        |
| json_dumps                 | 10.4 ms                                                | 10.4 ms: 1.01x slower                                        |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                         |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                         |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                        |
| json                       | 5.26 ms                                                | 5.37 ms: 1.02x slower                                        |
| asyncio_tcp                | 491 ms                                                 | 501 ms: 1.02x slower                                         |
| aiohttp                    | 1.15 ms                                                | 1.18 ms: 1.03x slower                                        |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                       |
| gunicorn                   | 1.24 ms                                                | 1.28 ms: 1.03x slower                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                       |
| asyncio_websockets         | 551 ms                                                 | 569 ms: 1.03x slower                                         |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                        |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                       |
| unpickle                   | 15.9 us                                                | 16.7 us: 1.05x slower                                        |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.06x slower                                        |
| gc_traversal               | 3.79 ms                                                | 4.01 ms: 1.06x slower                                        |
| pickle_list                | 5.08 us                                                | 5.40 us: 1.06x slower                                        |
| regex_dna                  | 212 ms                                                 | 230 ms: 1.09x slower                                         |
| python_startup             | 9.55 ms                                                | 10.6 ms: 1.11x slower                                        |
| regex_v8                   | 23.1 ms                                                | 26.0 ms: 1.13x slower                                        |
| create_gc_cycles           | 1.48 ms                                                | 1.68 ms: 1.14x slower                                        |
| telco                      | 7.10 ms                                                | 8.59 ms: 1.21x slower                                        |
| python_startup_no_site     | 6.94 ms                                                | 9.00 ms: 1.30x slower                                        |
| coverage                   | 72.7 ms                                                | 97.2 ms: 1.34x slower                                        |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                 |

Benchmark hidden because not significant (4): xml_etree_iterparse, sqlglot_optimize, docutils, go
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240327-3.13.0a5+-74c8568/bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 0.95x