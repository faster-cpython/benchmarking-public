# Results vs. 3.12.0

- fork: python
- ref: v3.13.0
- machine: linux-x86_64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.00x slower
- HPT reliability: 56.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.92x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                         |
| chameleon      | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                        |
| docutils       | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| tornado_http   | 121 ms                                                       | 120 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                        | 1.00x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 819 ms: 1.29x faster                                         |
| async_tree_none_tg         | 431 ms                                                       | 340 ms: 1.27x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                         |
| async_tree_none            | 452 ms                                                       | 372 ms: 1.21x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 452 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 461 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 600 ms: 1.16x faster                                         |
| Geometric mean             | (ref)                                                        | 1.22x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                         |
| float          | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.37 ms: 1.06x faster                                        |
| regex_compile  | 144 ms                                                       | 144 ms: 1.00x slower                                         |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                         |
| regex_v8       | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| xml_etree_iterparse  | 103 ms                                                       | 100 ms: 1.03x faster                                         |
| json_loads           | 24.4 us                                                      | 24.0 us: 1.02x faster                                        |
| pickle_dict          | 32.5 us                                                      | 32.1 us: 1.02x faster                                        |
| xml_etree_generate   | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                        |
| unpickle_list        | 4.66 us                                                      | 4.62 us: 1.01x faster                                        |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                         |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                        |
| unpickle_pure_python | 210 us                                                       | 214 us: 1.02x slower                                         |
| pickle_list          | 4.43 us                                                      | 4.59 us: 1.04x slower                                        |
| xml_etree_process    | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                        |
| json_dumps           | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                        |
| tomli_loads          | 2.16 sec                                                     | 2.41 sec: 1.11x slower                                       |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                 |

Benchmark hidden because not significant (2): pickle_pure_python, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                        |
| python_startup         | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                        |
| Geometric mean         | (ref)                                                        | 1.09x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                        |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 819 ms: 1.29x faster                                         |
| comprehensions             | 21.9 us                                                      | 17.3 us: 1.27x faster                                        |
| async_tree_none_tg         | 431 ms                                                       | 340 ms: 1.27x faster                                         |
| async_tree_io              | 1.04 sec                                                     | 847 ms: 1.23x faster                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 574 ms: 1.21x faster                                         |
| async_tree_none            | 452 ms                                                       | 372 ms: 1.21x faster                                         |
| async_tree_memoization     | 544 ms                                                       | 452 ms: 1.20x faster                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 461 ms: 1.17x faster                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 600 ms: 1.16x faster                                         |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                        |
| crypto_pyaes               | 80.3 ms                                                      | 72.8 ms: 1.10x faster                                        |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                         |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.08x faster                                        |
| coroutines                 | 23.0 ms                                                      | 21.6 ms: 1.06x faster                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 64.9 ms: 1.06x faster                                        |
| regex_effbot               | 3.57 ms                                                      | 3.37 ms: 1.06x faster                                        |
| logging_format             | 7.48 us                                                      | 7.07 us: 1.06x faster                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                         |
| bench_thread_pool          | 950 us                                                       | 901 us: 1.05x faster                                         |
| logging_simple             | 6.71 us                                                      | 6.40 us: 1.05x faster                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                         |
| chaos                      | 64.0 ms                                                      | 61.7 ms: 1.04x faster                                        |
| dask                       | 392 ms                                                       | 379 ms: 1.03x faster                                         |
| raytrace                   | 298 ms                                                       | 289 ms: 1.03x faster                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100 ms: 1.03x faster                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.3 ms: 1.03x faster                                        |
| sympy_str                  | 302 ms                                                       | 296 ms: 1.02x faster                                         |
| docutils                   | 2.87 sec                                                     | 2.81 sec: 1.02x faster                                       |
| nqueens                    | 89.9 ms                                                      | 88.2 ms: 1.02x faster                                        |
| mdp                        | 2.57 sec                                                     | 2.52 sec: 1.02x faster                                       |
| json_loads                 | 24.4 us                                                      | 24.0 us: 1.02x faster                                        |
| pickle_dict                | 32.5 us                                                      | 32.1 us: 1.02x faster                                        |
| tornado_http               | 121 ms                                                       | 120 ms: 1.01x faster                                         |
| asyncio_websockets         | 387 ms                                                       | 382 ms: 1.01x faster                                         |
| scimark_lu                 | 98.8 ms                                                      | 97.8 ms: 1.01x faster                                        |
| xml_etree_generate         | 86.1 ms                                                      | 85.3 ms: 1.01x faster                                        |
| unpickle_list              | 4.66 us                                                      | 4.62 us: 1.01x faster                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                       |
| meteor_contest             | 128 ms                                                       | 128 ms: 1.00x slower                                         |
| regex_compile              | 144 ms                                                       | 144 ms: 1.00x slower                                         |
| asyncio_tcp                | 378 ms                                                       | 380 ms: 1.01x slower                                         |
| pprint_safe_repr           | 807 ms                                                       | 812 ms: 1.01x slower                                         |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                         |
| django_template            | 38.2 ms                                                      | 38.9 ms: 1.02x slower                                        |
| pycparser                  | 1.23 sec                                                     | 1.26 sec: 1.02x slower                                       |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.29 ms: 1.02x slower                                        |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                         |
| json                       | 5.12 ms                                                      | 5.22 ms: 1.02x slower                                        |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                         |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                        |
| unpickle_pure_python       | 210 us                                                       | 214 us: 1.02x slower                                         |
| sqlglot_normalize          | 116 ms                                                       | 118 ms: 1.02x slower                                         |
| chameleon                  | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                        |
| logging_silent             | 94.4 ns                                                      | 97.7 ns: 1.03x slower                                        |
| pickle_list                | 4.43 us                                                      | 4.59 us: 1.04x slower                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.94 ms: 1.04x slower                                        |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.7 ms: 1.04x slower                                        |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                        |
| fannkuch                   | 350 ms                                                       | 365 ms: 1.04x slower                                         |
| xml_etree_process          | 58.4 ms                                                      | 60.9 ms: 1.04x slower                                        |
| sympy_expand               | 484 ms                                                       | 505 ms: 1.04x slower                                         |
| scimark_fft                | 301 ms                                                       | 314 ms: 1.04x slower                                         |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.54 us: 1.05x slower                                        |
| deltablue                  | 3.24 ms                                                      | 3.41 ms: 1.05x slower                                        |
| spectral_norm              | 91.6 ms                                                      | 97.4 ms: 1.06x slower                                        |
| hexiom                     | 5.96 ms                                                      | 6.33 ms: 1.06x slower                                        |
| unpack_sequence            | 53.2 ns                                                      | 56.8 ns: 1.07x slower                                        |
| float                      | 76.6 ms                                                      | 81.9 ms: 1.07x slower                                        |
| json_dumps                 | 10.2 ms                                                      | 11.0 ms: 1.07x slower                                        |
| go                         | 150 ms                                                       | 160 ms: 1.07x slower                                         |
| deepcopy_memo              | 36.8 us                                                      | 39.5 us: 1.07x slower                                        |
| deepcopy                   | 368 us                                                       | 397 us: 1.08x slower                                         |
| create_gc_cycles           | 1.59 ms                                                      | 1.76 ms: 1.11x slower                                        |
| regex_v8                   | 23.6 ms                                                      | 26.2 ms: 1.11x slower                                        |
| tomli_loads                | 2.16 sec                                                     | 2.41 sec: 1.11x slower                                       |
| pyflate                    | 439 ms                                                       | 492 ms: 1.12x slower                                         |
| python_startup             | 11.6 ms                                                      | 13.3 ms: 1.15x slower                                        |
| typing_runtime_protocols   | 152 us                                                       | 174 us: 1.15x slower                                         |
| richards                   | 45.7 ms                                                      | 52.7 ms: 1.15x slower                                        |
| scimark_sor                | 109 ms                                                       | 126 ms: 1.15x slower                                         |
| richards_super             | 51.3 ms                                                      | 59.8 ms: 1.16x slower                                        |
| gc_traversal               | 3.48 ms                                                      | 4.11 ms: 1.18x slower                                        |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                        |
| telco                      | 6.96 ms                                                      | 8.58 ms: 1.23x slower                                        |
| mypy2                      | 830 ms                                                       | 1.05 sec: 1.26x slower                                       |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                 |

Benchmark hidden because not significant (9): bench_mp_pool, pprint_pformat, nbody, pickle_pure_python, pickle, dulwich_log, sqlglot_parse, sqlglot_transpile, sqlite_synth
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf2-x86_64-python-v3.13.0-3.13.0-60403a5.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 56.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.92x