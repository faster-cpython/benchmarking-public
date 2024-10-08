# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.01x slower
- HPT reliability: 90.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.89x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                            |
| docutils       | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                           |
| Geometric mean | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 434 ms: 1.04x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 434 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 551 ms: 1.02x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.02x slower                                           |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.04x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                            |
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| float          | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                            |
| Geometric mean | (ref)                                                        | 1.01x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                            |
| regex_compile  | 144 ms                                                       | 142 ms: 1.01x faster                                             |
| regex_dna      | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.3 us: 1.07x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.33 us: 1.02x faster                                            |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| xml_etree_generate   | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                            |
| xml_etree_process    | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                            |
| pickle_pure_python   | 318 us                                                       | 316 us: 1.01x faster                                             |
| unpickle_list        | 4.66 us                                                      | 4.68 us: 1.00x slower                                            |
| xml_etree_iterparse  | 103 ms                                                       | 105 ms: 1.02x slower                                             |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| unpickle_pure_python | 210 us                                                       | 217 us: 1.04x slower                                             |
| json_loads           | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                           |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.6 ms: 1.09x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.0 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                        | 1.18x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                            |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 16.5 us: 1.33x faster                                            |
| typing_runtime_protocols   | 152 us                                                       | 117 us: 1.30x faster                                             |
| raytrace                   | 298 ms                                                       | 262 ms: 1.14x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 71.3 ms: 1.13x faster                                            |
| generators                 | 37.4 ms                                                      | 34.1 ms: 1.10x faster                                            |
| async_generators           | 390 ms                                                       | 359 ms: 1.09x faster                                             |
| pickle_dict                | 32.5 us                                                      | 30.3 us: 1.07x faster                                            |
| sympy_sum                  | 162 ms                                                       | 153 ms: 1.06x faster                                             |
| chaos                      | 64.0 ms                                                      | 61.0 ms: 1.05x faster                                            |
| scimark_lu                 | 98.8 ms                                                      | 94.4 ms: 1.05x faster                                            |
| async_tree_none            | 452 ms                                                       | 434 ms: 1.04x faster                                             |
| logging_format             | 7.48 us                                                      | 7.21 us: 1.04x faster                                            |
| nbody                      | 88.0 ms                                                      | 84.8 ms: 1.04x faster                                            |
| sympy_str                  | 302 ms                                                       | 291 ms: 1.04x faster                                             |
| coroutines                 | 23.0 ms                                                      | 22.2 ms: 1.04x faster                                            |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                            |
| mdp                        | 2.57 sec                                                     | 2.50 sec: 1.03x faster                                           |
| scimark_monte_carlo        | 69.0 ms                                                      | 67.0 ms: 1.03x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.48 ms: 1.03x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.62 sec: 1.02x faster                                           |
| pickle_list                | 4.43 us                                                      | 4.33 us: 1.02x faster                                            |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| pprint_safe_repr           | 807 ms                                                       | 791 ms: 1.02x faster                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.12 ms: 1.02x faster                                            |
| meteor_contest             | 128 ms                                                       | 126 ms: 1.02x faster                                             |
| sqlite_synth               | 2.77 us                                                      | 2.73 us: 1.02x faster                                            |
| regex_compile              | 144 ms                                                       | 142 ms: 1.01x faster                                             |
| logging_simple             | 6.71 us                                                      | 6.63 us: 1.01x faster                                            |
| xml_etree_generate         | 86.1 ms                                                      | 85.1 ms: 1.01x faster                                            |
| nqueens                    | 89.9 ms                                                      | 88.8 ms: 1.01x faster                                            |
| xml_etree_process          | 58.4 ms                                                      | 57.7 ms: 1.01x faster                                            |
| pidigits                   | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                             |
| sqlglot_normalize          | 116 ms                                                       | 115 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.57 sec: 1.01x faster                                           |
| docutils                   | 2.87 sec                                                     | 2.84 sec: 1.01x faster                                           |
| pickle_pure_python         | 318 us                                                       | 316 us: 1.01x faster                                             |
| logging_silent             | 94.4 ns                                                      | 93.6 ns: 1.01x faster                                            |
| unpickle_list              | 4.66 us                                                      | 4.68 us: 1.00x slower                                            |
| pathlib                    | 18.9 ms                                                      | 19.0 ms: 1.01x slower                                            |
| django_template            | 38.2 ms                                                      | 38.4 ms: 1.01x slower                                            |
| async_tree_none_tg         | 431 ms                                                       | 434 ms: 1.01x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 92.5 ms: 1.01x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 37.2 us: 1.01x slower                                            |
| regex_dna                  | 239 ms                                                       | 241 ms: 1.01x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 705 ms: 1.01x slower                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.41 us: 1.01x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.80 ms: 1.01x slower                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 58.6 ms: 1.02x slower                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 551 ms: 1.02x slower                                             |
| xml_etree_iterparse        | 103 ms                                                       | 105 ms: 1.02x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.02x slower                                           |
| 2to3                       | 285 ms                                                       | 292 ms: 1.02x slower                                             |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.02x slower                                            |
| sympy_expand               | 484 ms                                                       | 496 ms: 1.02x slower                                             |
| chameleon                  | 7.23 ms                                                      | 7.42 ms: 1.03x slower                                            |
| float                      | 76.6 ms                                                      | 78.8 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| unpickle                   | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.04x slower                                           |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                            |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 217 us: 1.04x slower                                             |
| pycparser                  | 1.23 sec                                                     | 1.28 sec: 1.04x slower                                           |
| json_loads                 | 24.4 us                                                      | 25.3 us: 1.04x slower                                            |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                            |
| aiohttp                    | 1.02 ms                                                      | 1.06 ms: 1.04x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 69.0 ms: 1.05x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 3.76 ms: 1.08x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.44 ms: 1.08x slower                                            |
| python_startup             | 11.6 ms                                                      | 12.6 ms: 1.09x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| tomli_loads                | 2.16 sec                                                     | 2.38 sec: 1.10x slower                                           |
| deltablue                  | 3.24 ms                                                      | 3.59 ms: 1.11x slower                                            |
| fannkuch                   | 350 ms                                                       | 393 ms: 1.12x slower                                             |
| go                         | 150 ms                                                       | 170 ms: 1.14x slower                                             |
| pyflate                    | 439 ms                                                       | 506 ms: 1.15x slower                                             |
| telco                      | 6.96 ms                                                      | 8.16 ms: 1.17x slower                                            |
| richards_super             | 51.3 ms                                                      | 60.8 ms: 1.18x slower                                            |
| richards                   | 45.7 ms                                                      | 54.4 ms: 1.19x slower                                            |
| coverage                   | 66.7 ms                                                      | 82.9 ms: 1.24x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 11.0 ms: 1.28x slower                                            |
| scimark_sor                | 109 ms                                                       | 146 ms: 1.34x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (10): bench_mp_pool, asyncio_websockets, scimark_fft, deepcopy, async_tree_cpu_io_mixed, async_tree_memoization, tornado_http, bench_thread_pool, create_gc_cycles, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: dask, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240215-3.13.0a4-9d34f60/bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 90.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.89x