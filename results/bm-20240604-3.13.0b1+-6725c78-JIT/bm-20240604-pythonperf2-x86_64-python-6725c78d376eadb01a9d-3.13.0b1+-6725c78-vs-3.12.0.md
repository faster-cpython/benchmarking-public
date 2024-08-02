# Results vs. 3.12.0

- fork: python
- ref: 6725c78d376eadb01a9d
- machine: linux-x86_64
- commit hash: 6725c78
- commit date: 2024-06-04
- overall geometric mean: 1.01x slower
- HPT reliability: 63.22%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                                         |
| chameleon      | 7.23 ms                                                      | 7.60 ms: 1.05x slower                                                        |
| docutils       | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                       |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 844 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 438 ms: 1.23x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 351 ms: 1.23x faster                                                         |
| async_tree_memoization     | 544 ms                                                       | 451 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                         |
| async_tree_none            | 452 ms                                                       | 379 ms: 1.19x faster                                                         |
| async_tree_io              | 1.04 sec                                                     | 907 ms: 1.15x faster                                                         |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 633 ms: 1.10x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.19x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 81.9 ms: 1.07x faster                                                        |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                                         |
| float          | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| regex_dna      | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| regex_effbot   | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                        |
| regex_v8       | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| xml_etree_iterparse  | 103 ms                                                       | 100.0 ms: 1.03x faster                                                       |
| pickle_dict          | 32.5 us                                                      | 31.8 us: 1.02x faster                                                        |
| pickle_pure_python   | 318 us                                                       | 314 us: 1.01x faster                                                         |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| json_loads           | 24.4 us                                                      | 24.7 us: 1.02x slower                                                        |
| pickle_list          | 4.43 us                                                      | 4.56 us: 1.03x slower                                                        |
| unpickle_list        | 4.66 us                                                      | 4.81 us: 1.03x slower                                                        |
| json_dumps           | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                        |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.03x slower                                                         |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.05x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                        |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.02 ms: 1.11x faster                                                        |
| django_template | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 844 ms: 1.25x faster                                                         |
| async_tree_memoization_tg  | 540 ms                                                       | 438 ms: 1.23x faster                                                         |
| async_tree_none_tg         | 431 ms                                                       | 351 ms: 1.23x faster                                                         |
| comprehensions             | 21.9 us                                                      | 18.0 us: 1.22x faster                                                        |
| async_tree_memoization     | 544 ms                                                       | 451 ms: 1.21x faster                                                         |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 585 ms: 1.19x faster                                                         |
| async_tree_none            | 452 ms                                                       | 379 ms: 1.19x faster                                                         |
| crypto_pyaes               | 80.3 ms                                                      | 69.9 ms: 1.15x faster                                                        |
| async_tree_io              | 1.04 sec                                                     | 907 ms: 1.15x faster                                                         |
| spectral_norm              | 91.6 ms                                                      | 82.1 ms: 1.12x faster                                                        |
| mako                       | 10.0 ms                                                      | 9.02 ms: 1.11x faster                                                        |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 633 ms: 1.10x faster                                                         |
| generators                 | 37.4 ms                                                      | 34.2 ms: 1.10x faster                                                        |
| pathlib                    | 18.9 ms                                                      | 17.5 ms: 1.08x faster                                                        |
| nbody                      | 88.0 ms                                                      | 81.9 ms: 1.07x faster                                                        |
| logging_format             | 7.48 us                                                      | 7.06 us: 1.06x faster                                                        |
| xml_etree_generate         | 86.1 ms                                                      | 81.4 ms: 1.06x faster                                                        |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                                         |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.01 ms: 1.05x faster                                                        |
| scimark_fft                | 301 ms                                                       | 287 ms: 1.05x faster                                                         |
| fannkuch                   | 350 ms                                                       | 335 ms: 1.04x faster                                                         |
| regex_compile              | 144 ms                                                       | 138 ms: 1.04x faster                                                         |
| pprint_pformat             | 1.65 sec                                                     | 1.59 sec: 1.04x faster                                                       |
| raytrace                   | 298 ms                                                       | 287 ms: 1.04x faster                                                         |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                                        |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                                       |
| scimark_monte_carlo        | 69.0 ms                                                      | 66.7 ms: 1.03x faster                                                        |
| logging_simple             | 6.71 us                                                      | 6.52 us: 1.03x faster                                                        |
| pprint_safe_repr           | 807 ms                                                       | 784 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 103 ms                                                       | 100.0 ms: 1.03x faster                                                       |
| pickle_dict                | 32.5 us                                                      | 31.8 us: 1.02x faster                                                        |
| async_generators           | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| pickle_pure_python         | 318 us                                                       | 314 us: 1.01x faster                                                         |
| sqlite_synth               | 2.77 us                                                      | 2.74 us: 1.01x faster                                                        |
| deepcopy_memo              | 36.8 us                                                      | 36.5 us: 1.01x faster                                                        |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                                       |
| float                      | 76.6 ms                                                      | 76.2 ms: 1.01x faster                                                        |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                                       |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                                         |
| chaos                      | 64.0 ms                                                      | 64.7 ms: 1.01x slower                                                        |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                         |
| json_loads                 | 24.4 us                                                      | 24.7 us: 1.02x slower                                                        |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                                         |
| sqlglot_parse              | 1.38 ms                                                      | 1.40 ms: 1.02x slower                                                        |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                                         |
| regex_dna                  | 239 ms                                                       | 243 ms: 1.02x slower                                                         |
| sympy_str                  | 302 ms                                                       | 309 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.78 ms                                                      | 1.81 ms: 1.02x slower                                                        |
| dulwich_log                | 65.4 ms                                                      | 66.9 ms: 1.02x slower                                                        |
| richards_super             | 51.3 ms                                                      | 52.6 ms: 1.03x slower                                                        |
| pickle_list                | 4.43 us                                                      | 4.56 us: 1.03x slower                                                        |
| dask                       | 392 ms                                                       | 405 ms: 1.03x slower                                                         |
| unpickle_list              | 4.66 us                                                      | 4.81 us: 1.03x slower                                                        |
| json_dumps                 | 10.2 ms                                                      | 10.6 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.03x slower                                                         |
| regex_effbot               | 3.57 ms                                                      | 3.70 ms: 1.04x slower                                                        |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.05x slower                                                        |
| chameleon                  | 7.23 ms                                                      | 7.60 ms: 1.05x slower                                                        |
| regex_v8                   | 23.6 ms                                                      | 24.9 ms: 1.05x slower                                                        |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.05x slower                                                        |
| sympy_integrate            | 23.9 ms                                                      | 25.4 ms: 1.06x slower                                                        |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                         |
| pyflate                    | 439 ms                                                       | 468 ms: 1.07x slower                                                         |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                                         |
| deepcopy_reduce            | 3.37 us                                                      | 3.62 us: 1.07x slower                                                        |
| nqueens                    | 89.9 ms                                                      | 96.9 ms: 1.08x slower                                                        |
| docutils                   | 2.87 sec                                                     | 3.11 sec: 1.08x slower                                                       |
| django_template            | 38.2 ms                                                      | 41.3 ms: 1.08x slower                                                        |
| sympy_expand               | 484 ms                                                       | 525 ms: 1.09x slower                                                         |
| python_startup_no_site     | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                                        |
| sqlglot_optimize           | 57.5 ms                                                      | 62.9 ms: 1.09x slower                                                        |
| deepcopy                   | 368 us                                                       | 405 us: 1.10x slower                                                         |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                                         |
| sqlglot_normalize          | 116 ms                                                       | 129 ms: 1.11x slower                                                         |
| hexiom                     | 5.96 ms                                                      | 6.70 ms: 1.12x slower                                                        |
| gunicorn                   | 1.00 ms                                                      | 1.13 ms: 1.13x slower                                                        |
| scimark_lu                 | 98.8 ms                                                      | 113 ms: 1.14x slower                                                         |
| aiohttp                    | 1.02 ms                                                      | 1.17 ms: 1.15x slower                                                        |
| telco                      | 6.96 ms                                                      | 8.22 ms: 1.18x slower                                                        |
| deltablue                  | 3.24 ms                                                      | 3.84 ms: 1.19x slower                                                        |
| typing_runtime_protocols   | 152 us                                                       | 180 us: 1.19x slower                                                         |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                                        |
| coverage                   | 66.7 ms                                                      | 81.2 ms: 1.22x slower                                                        |
| create_gc_cycles           | 1.59 ms                                                      | 1.95 ms: 1.22x slower                                                        |
| scimark_sor                | 109 ms                                                       | 144 ms: 1.32x slower                                                         |
| gc_traversal               | 3.48 ms                                                      | 4.91 ms: 1.41x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (9): bench_thread_pool, richards, asyncio_websockets, pickle, asyncio_tcp, xml_etree_process, pycparser, bench_mp_pool, mypy2
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240604-3.13.0b1+-6725c78-JIT/bm-20240604-pythonperf2-x86_64-python-6725c78d376eadb01a9d-3.13.0b1+-6725c78.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 63.22% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.01x