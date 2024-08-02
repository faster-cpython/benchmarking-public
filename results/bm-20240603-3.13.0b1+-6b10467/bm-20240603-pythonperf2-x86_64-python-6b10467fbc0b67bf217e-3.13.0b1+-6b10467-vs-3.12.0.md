# Results vs. 3.12.0

- fork: python
- ref: 6b10467fbc0b67bf217e
- machine: linux-x86_64
- commit hash: 6b10467
- commit date: 2024-06-03
- overall geometric mean: 1.00x slower
- HPT reliability: 86.16%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.49 ms: 1.04x slower                                                        |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| tornado_http   | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                                         |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 577 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.17x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 897 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 909 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.20x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| float          | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                        |
| regex_compile  | 144 ms                                                       | 143 ms: 1.00x faster                                                         |
| regex_dna      | 239 ms                                                       | 245 ms: 1.03x slower                                                         |
| regex_v8       | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|--------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_dict        | 32.5 us                                                      | 30.1 us: 1.08x faster                                                        |
| pickle_list        | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| pickle             | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| pickle_pure_python | 318 us                                                       | 314 us: 1.01x faster                                                         |
| xml_etree_generate | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                        |
| xml_etree_parse    | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| json_loads         | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| xml_etree_process  | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                        |
| unpickle_list      | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| unpickle           | 14.8 us                                                      | 15.4 us: 1.04x slower                                                        |
| json_dumps         | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| tomli_loads        | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| Geometric mean     | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (2): unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| mako            | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                                        |
| async_tree_memoization_tg  | 540 ms                                                       | 428 ms: 1.26x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 342 ms: 1.26x faster                                                         |
| async_tree_none            | 452 ms                                                       | 368 ms: 1.23x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 577 ms: 1.21x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 467 ms: 1.17x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 897 ms: 1.16x faster                                                         |
| async_tree_io_tg           | 1.05 sec                                                     | 909 ms: 1.16x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 612 ms: 1.14x faster                                                         |
| generators                 | 37.4 ms                                                      | 33.2 ms: 1.13x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.2 ms: 1.10x faster                                                        |
| crypto_pyaes               | 80.3 ms                                                      | 73.5 ms: 1.09x faster                                                        |
| raytrace                   | 298 ms                                                       | 276 ms: 1.08x faster                                                         |
| pickle_dict                | 32.5 us                                                      | 30.1 us: 1.08x faster                                                        |
| mypy2                      | 830 ms                                                       | 769 ms: 1.08x faster                                                         |
| async_generators           | 390 ms                                                       | 363 ms: 1.08x faster                                                         |
| bench_thread_pool          | 950 us                                                       | 898 us: 1.06x faster                                                         |
| logging_format             | 7.48 us                                                      | 7.09 us: 1.06x faster                                                        |
| sympy_sum                  | 162 ms                                                       | 154 ms: 1.05x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 21.9 ms: 1.05x faster                                                        |
| pidigits                   | 265 ms                                                       | 253 ms: 1.05x faster                                                         |
| chaos                      | 64.0 ms                                                      | 61.4 ms: 1.04x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.49 sec: 1.03x faster                                                       |
| pickle_list                | 4.43 us                                                      | 4.30 us: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                        |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.1 ms: 1.03x faster                                                        |
| tornado_http               | 121 ms                                                       | 118 ms: 1.03x faster                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                                        |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.02x faster                                                         |
| sympy_integrate            | 23.9 ms                                                      | 23.4 ms: 1.02x faster                                                        |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                                        |
| nqueens                    | 89.9 ms                                                      | 88.7 ms: 1.01x faster                                                        |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                         |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| xml_etree_generate         | 86.1 ms                                                      | 85.5 ms: 1.01x faster                                                        |
| regex_compile              | 144 ms                                                       | 143 ms: 1.00x faster                                                         |
| meteor_contest             | 128 ms                                                       | 129 ms: 1.00x slower                                                         |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.67 sec: 1.01x slower                                                       |
| json_loads                 | 24.4 us                                                      | 24.6 us: 1.01x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 95.8 ns: 1.02x slower                                                        |
| deepcopy_reduce            | 3.37 us                                                      | 3.43 us: 1.02x slower                                                        |
| pprint_safe_repr           | 807 ms                                                       | 823 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                        |
| python_startup_no_site     | 8.64 ms                                                      | 8.82 ms: 1.02x slower                                                        |
| sqlite_synth               | 2.77 us                                                      | 2.84 us: 1.02x slower                                                        |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                                         |
| deepcopy                   | 368 us                                                       | 378 us: 1.02x slower                                                         |
| xml_etree_process          | 58.4 ms                                                      | 59.9 ms: 1.03x slower                                                        |
| json                       | 5.12 ms                                                      | 5.26 ms: 1.03x slower                                                        |
| regex_dna                  | 239 ms                                                       | 245 ms: 1.03x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.79 us: 1.03x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.33 ms: 1.03x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 67.3 ms: 1.03x slower                                                        |
| django_template            | 38.2 ms                                                      | 39.4 ms: 1.03x slower                                                        |
| scimark_fft                | 301 ms                                                       | 311 ms: 1.03x slower                                                         |
| deepcopy_memo              | 36.8 us                                                      | 38.0 us: 1.03x slower                                                        |
| mako                       | 10.0 ms                                                      | 10.3 ms: 1.03x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.49 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.38 ms                                                      | 1.43 ms: 1.04x slower                                                        |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                       |
| sympy_expand               | 484 ms                                                       | 504 ms: 1.04x slower                                                         |
| float                      | 76.6 ms                                                      | 79.8 ms: 1.04x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.4 us: 1.04x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 59.9 ms: 1.04x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                                        |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.42 ms: 1.05x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.05 ms: 1.05x slower                                                        |
| fannkuch                   | 350 ms                                                       | 368 ms: 1.05x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 122 ms: 1.06x slower                                                         |
| go                         | 150 ms                                                       | 158 ms: 1.06x slower                                                         |
| spectral_norm              | 91.6 ms                                                      | 96.9 ms: 1.06x slower                                                        |
| hexiom                     | 5.96 ms                                                      | 6.31 ms: 1.06x slower                                                        |
| aiohttp                    | 1.02 ms                                                      | 1.08 ms: 1.06x slower                                                        |
| scimark_sor                | 109 ms                                                       | 118 ms: 1.08x slower                                                         |
| pyflate                    | 439 ms                                                       | 481 ms: 1.10x slower                                                         |
| regex_v8                   | 23.6 ms                                                      | 26.1 ms: 1.10x slower                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.39 sec: 1.11x slower                                                       |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.13x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 175 us: 1.15x slower                                                         |
| richards_super             | 51.3 ms                                                      | 59.8 ms: 1.16x slower                                                        |
| richards                   | 45.7 ms                                                      | 53.4 ms: 1.17x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.61 ms: 1.24x slower                                                        |
| coverage                   | 66.7 ms                                                      | 83.9 ms: 1.26x slower                                                        |
| gc_traversal               | 3.48 ms                                                      | 4.47 ms: 1.28x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 2.06 ms: 1.29x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (9): scimark_lu, bench_mp_pool, asyncio_websockets, asyncio_tcp, unpickle_pure_python, pycparser, dask, xml_etree_iterparse, nbody
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240603-3.13.0b1+-6b10467/bm-20240603-pythonperf2-x86_64-python-6b10467fbc0b67bf217e-3.13.0b1+-6b10467.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 86.16% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x