# Results vs. 3.13.0

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.00x faster
- HPT reliability: 63.18%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 291 ms                                                       | 285 ms: 1.02x faster                                         |
| chameleon      | 7.42 ms                                                      | 7.23 ms: 1.03x faster                                        |
| docutils       | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                       |
| tornado_http   | 120 ms                                                       | 121 ms: 1.01x slower                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| asyncio_tcp                | 380 ms                                                       | 378 ms: 1.01x faster                                         |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                       |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                         |
| coroutines                 | 21.6 ms                                                      | 23.0 ms: 1.06x slower                                        |
| async_generators           | 359 ms                                                       | 390 ms: 1.09x slower                                         |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 696 ms: 1.16x slower                                         |
| async_tree_memoization_tg  | 461 ms                                                       | 540 ms: 1.17x slower                                         |
| async_tree_memoization     | 452 ms                                                       | 544 ms: 1.20x slower                                         |
| async_tree_none            | 372 ms                                                       | 452 ms: 1.21x slower                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 697 ms: 1.21x slower                                         |
| async_tree_io              | 847 ms                                                       | 1.04 sec: 1.23x slower                                       |
| async_tree_none_tg         | 340 ms                                                       | 431 ms: 1.27x slower                                         |
| async_tree_io_tg           | 819 ms                                                       | 1.05 sec: 1.29x slower                                       |
| Geometric mean             | (ref)                                                        | 1.14x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 81.9 ms                                                      | 76.6 ms: 1.07x faster                                        |
| pidigits       | 253 ms                                                       | 265 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                        | 1.01x faster                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                        |
| regex_dna      | 244 ms                                                       | 239 ms: 1.02x faster                                         |
| regex_compile  | 144 ms                                                       | 144 ms: 1.00x faster                                         |
| regex_effbot   | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.41 sec                                                     | 2.16 sec: 1.11x faster                                       |
| json_dumps           | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                        |
| xml_etree_process    | 60.9 ms                                                      | 58.4 ms: 1.04x faster                                        |
| pickle_list          | 4.59 us                                                      | 4.43 us: 1.04x faster                                        |
| unpickle_pure_python | 214 us                                                       | 210 us: 1.02x faster                                         |
| unpickle             | 15.1 us                                                      | 14.8 us: 1.02x faster                                        |
| xml_etree_parse      | 145 ms                                                       | 144 ms: 1.01x faster                                         |
| unpickle_list        | 4.62 us                                                      | 4.66 us: 1.01x slower                                        |
| xml_etree_generate   | 85.3 ms                                                      | 86.1 ms: 1.01x slower                                        |
| pickle_dict          | 32.1 us                                                      | 32.5 us: 1.02x slower                                        |
| json_loads           | 24.0 us                                                      | 24.4 us: 1.02x slower                                        |
| xml_etree_iterparse  | 100 ms                                                       | 103 ms: 1.03x slower                                         |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                 |

Benchmark hidden because not significant (2): pickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                      | 11.6 ms: 1.15x faster                                        |
| python_startup_no_site | 8.94 ms                                                      | 8.64 ms: 1.04x faster                                        |
| Geometric mean         | (ref)                                                        | 1.09x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 10.4 ms                                                      | 10.0 ms: 1.04x faster                                        |
| django_template | 38.9 ms                                                      | 38.2 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| mypy2                      | 1.05 sec                                                     | 830 ms: 1.26x faster                                         |
| telco                      | 8.58 ms                                                      | 6.96 ms: 1.23x faster                                        |
| coverage                   | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                        |
| gc_traversal               | 4.11 ms                                                      | 3.48 ms: 1.18x faster                                        |
| richards_super             | 59.8 ms                                                      | 51.3 ms: 1.16x faster                                        |
| scimark_sor                | 126 ms                                                       | 109 ms: 1.15x faster                                         |
| richards                   | 52.7 ms                                                      | 45.7 ms: 1.15x faster                                        |
| typing_runtime_protocols   | 174 us                                                       | 152 us: 1.15x faster                                         |
| python_startup             | 13.3 ms                                                      | 11.6 ms: 1.15x faster                                        |
| pyflate                    | 492 ms                                                       | 439 ms: 1.12x faster                                         |
| tomli_loads                | 2.41 sec                                                     | 2.16 sec: 1.11x faster                                       |
| regex_v8                   | 26.2 ms                                                      | 23.6 ms: 1.11x faster                                        |
| create_gc_cycles           | 1.76 ms                                                      | 1.59 ms: 1.11x faster                                        |
| deepcopy                   | 397 us                                                       | 368 us: 1.08x faster                                         |
| deepcopy_memo              | 39.5 us                                                      | 36.8 us: 1.07x faster                                        |
| go                         | 160 ms                                                       | 150 ms: 1.07x faster                                         |
| json_dumps                 | 11.0 ms                                                      | 10.2 ms: 1.07x faster                                        |
| float                      | 81.9 ms                                                      | 76.6 ms: 1.07x faster                                        |
| unpack_sequence            | 56.8 ns                                                      | 53.2 ns: 1.07x faster                                        |
| hexiom                     | 6.33 ms                                                      | 5.96 ms: 1.06x faster                                        |
| spectral_norm              | 97.4 ms                                                      | 91.6 ms: 1.06x faster                                        |
| deltablue                  | 3.41 ms                                                      | 3.24 ms: 1.05x faster                                        |
| deepcopy_reduce            | 3.54 us                                                      | 3.37 us: 1.05x faster                                        |
| aiohttp                    | 1.07 ms                                                      | 1.02 ms: 1.05x faster                                        |
| scimark_fft                | 314 ms                                                       | 301 ms: 1.04x faster                                         |
| sympy_expand               | 505 ms                                                       | 484 ms: 1.04x faster                                         |
| xml_etree_process          | 60.9 ms                                                      | 58.4 ms: 1.04x faster                                        |
| fannkuch                   | 365 ms                                                       | 350 ms: 1.04x faster                                         |
| mako                       | 10.4 ms                                                      | 10.0 ms: 1.04x faster                                        |
| sqlglot_optimize           | 59.7 ms                                                      | 57.5 ms: 1.04x faster                                        |
| gunicorn                   | 1.04 ms                                                      | 1.00 ms: 1.04x faster                                        |
| python_startup_no_site     | 8.94 ms                                                      | 8.64 ms: 1.04x faster                                        |
| pickle_list                | 4.59 us                                                      | 4.43 us: 1.04x faster                                        |
| logging_silent             | 97.7 ns                                                      | 94.4 ns: 1.03x faster                                        |
| chameleon                  | 7.42 ms                                                      | 7.23 ms: 1.03x faster                                        |
| sqlglot_normalize          | 118 ms                                                       | 116 ms: 1.02x faster                                         |
| unpickle_pure_python       | 214 us                                                       | 210 us: 1.02x faster                                         |
| unpickle                   | 15.1 us                                                      | 14.8 us: 1.02x faster                                        |
| regex_dna                  | 244 ms                                                       | 239 ms: 1.02x faster                                         |
| json                       | 5.22 ms                                                      | 5.12 ms: 1.02x faster                                        |
| 2to3                       | 291 ms                                                       | 285 ms: 1.02x faster                                         |
| scimark_sparse_mat_mult    | 4.29 ms                                                      | 4.21 ms: 1.02x faster                                        |
| pycparser                  | 1.26 sec                                                     | 1.23 sec: 1.02x faster                                       |
| django_template            | 38.9 ms                                                      | 38.2 ms: 1.02x faster                                        |
| xml_etree_parse            | 145 ms                                                       | 144 ms: 1.01x faster                                         |
| pprint_safe_repr           | 812 ms                                                       | 807 ms: 1.01x faster                                         |
| asyncio_tcp                | 380 ms                                                       | 378 ms: 1.01x faster                                         |
| regex_compile              | 144 ms                                                       | 144 ms: 1.00x faster                                         |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x faster                                         |
| asyncio_tcp_ssl            | 1.58 sec                                                     | 1.59 sec: 1.00x slower                                       |
| unpickle_list              | 4.62 us                                                      | 4.66 us: 1.01x slower                                        |
| xml_etree_generate         | 85.3 ms                                                      | 86.1 ms: 1.01x slower                                        |
| scimark_lu                 | 97.8 ms                                                      | 98.8 ms: 1.01x slower                                        |
| asyncio_websockets         | 382 ms                                                       | 387 ms: 1.01x slower                                         |
| tornado_http               | 120 ms                                                       | 121 ms: 1.01x slower                                         |
| pickle_dict                | 32.1 us                                                      | 32.5 us: 1.02x slower                                        |
| json_loads                 | 24.0 us                                                      | 24.4 us: 1.02x slower                                        |
| mdp                        | 2.52 sec                                                     | 2.57 sec: 1.02x slower                                       |
| nqueens                    | 88.2 ms                                                      | 89.9 ms: 1.02x slower                                        |
| docutils                   | 2.81 sec                                                     | 2.87 sec: 1.02x slower                                       |
| sympy_str                  | 296 ms                                                       | 302 ms: 1.02x slower                                         |
| sympy_integrate            | 23.3 ms                                                      | 23.9 ms: 1.03x slower                                        |
| xml_etree_iterparse        | 100 ms                                                       | 103 ms: 1.03x slower                                         |
| raytrace                   | 289 ms                                                       | 298 ms: 1.03x slower                                         |
| dask                       | 379 ms                                                       | 392 ms: 1.03x slower                                         |
| chaos                      | 61.7 ms                                                      | 64.0 ms: 1.04x slower                                        |
| pidigits                   | 253 ms                                                       | 265 ms: 1.05x slower                                         |
| logging_simple             | 6.40 us                                                      | 6.71 us: 1.05x slower                                        |
| bench_thread_pool          | 901 us                                                       | 950 us: 1.05x slower                                         |
| sympy_sum                  | 154 ms                                                       | 162 ms: 1.05x slower                                         |
| logging_format             | 7.07 us                                                      | 7.48 us: 1.06x slower                                        |
| regex_effbot               | 3.37 ms                                                      | 3.57 ms: 1.06x slower                                        |
| scimark_monte_carlo        | 64.9 ms                                                      | 69.0 ms: 1.06x slower                                        |
| coroutines                 | 21.6 ms                                                      | 23.0 ms: 1.06x slower                                        |
| pathlib                    | 17.4 ms                                                      | 18.9 ms: 1.08x slower                                        |
| async_generators           | 359 ms                                                       | 390 ms: 1.09x slower                                         |
| crypto_pyaes               | 72.8 ms                                                      | 80.3 ms: 1.10x slower                                        |
| generators                 | 33.5 ms                                                      | 37.4 ms: 1.12x slower                                        |
| async_tree_cpu_io_mixed    | 600 ms                                                       | 696 ms: 1.16x slower                                         |
| async_tree_memoization_tg  | 461 ms                                                       | 540 ms: 1.17x slower                                         |
| async_tree_memoization     | 452 ms                                                       | 544 ms: 1.20x slower                                         |
| async_tree_none            | 372 ms                                                       | 452 ms: 1.21x slower                                         |
| async_tree_cpu_io_mixed_tg | 574 ms                                                       | 697 ms: 1.21x slower                                         |
| async_tree_io              | 847 ms                                                       | 1.04 sec: 1.23x slower                                       |
| async_tree_none_tg         | 340 ms                                                       | 431 ms: 1.27x slower                                         |
| comprehensions             | 17.3 us                                                      | 21.9 us: 1.27x slower                                        |
| async_tree_io_tg           | 819 ms                                                       | 1.05 sec: 1.29x slower                                       |
| Geometric mean             | (ref)                                                        | 1.00x faster                                                 |

Benchmark hidden because not significant (9): sqlite_synth, sqlglot_transpile, sqlglot_parse, dulwich_log, pickle, pickle_pure_python, nbody, pprint_pformat, bench_mp_pool
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative

# HPT report

- Reliability score: 63.18% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.10x