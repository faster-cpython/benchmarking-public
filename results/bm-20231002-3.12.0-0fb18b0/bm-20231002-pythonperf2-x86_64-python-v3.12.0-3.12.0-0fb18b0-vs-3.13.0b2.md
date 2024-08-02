# Results vs. 3.13.0b2

- fork: python
- ref: v3.12.0
- machine: linux-x86_64
- commit hash: 0fb18b0
- commit date: 2023-10-02
- overall geometric mean: 1.00x faster
- HPT reliability: 70.35%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 291 ms                                                           | 285 ms: 1.02x faster                                         |
| chameleon      | 7.40 ms                                                          | 7.23 ms: 1.02x faster                                        |
| docutils       | 2.98 sec                                                         | 2.87 sec: 1.04x faster                                       |
| tornado_http   | 119 ms                                                           | 121 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                            | 1.02x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 604 ms                                                           | 696 ms: 1.15x slower                                         |
| async_tree_io_tg           | 900 ms                                                           | 1.05 sec: 1.17x slower                                       |
| async_tree_memoization     | 460 ms                                                           | 544 ms: 1.18x slower                                         |
| async_tree_io              | 873 ms                                                           | 1.04 sec: 1.19x slower                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 697 ms: 1.22x slower                                         |
| async_tree_none            | 365 ms                                                           | 452 ms: 1.24x slower                                         |
| async_tree_none_tg         | 340 ms                                                           | 431 ms: 1.27x slower                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 540 ms: 1.28x slower                                         |
| Geometric mean             | (ref)                                                            | 1.21x slower                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 80.2 ms                                                          | 76.6 ms: 1.05x faster                                        |
| pidigits       | 254 ms                                                           | 265 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                            | 1.00x slower                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_v8       | 26.0 ms                                                          | 23.6 ms: 1.10x faster                                        |
| regex_dna      | 249 ms                                                           | 239 ms: 1.05x faster                                         |
| regex_effbot   | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                        |
| Geometric mean | (ref)                                                            | 1.02x faster                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                       |
| unpickle_pure_python | 224 us                                                           | 210 us: 1.07x faster                                         |
| unpickle             | 15.7 us                                                          | 14.8 us: 1.06x faster                                        |
| json_dumps           | 10.8 ms                                                          | 10.2 ms: 1.05x faster                                        |
| json_loads           | 25.0 us                                                          | 24.4 us: 1.03x faster                                        |
| xml_etree_process    | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                        |
| pickle_dict          | 32.8 us                                                          | 32.5 us: 1.01x faster                                        |
| unpickle_list        | 4.70 us                                                          | 4.66 us: 1.01x faster                                        |
| pickle               | 10.6 us                                                          | 10.5 us: 1.01x faster                                        |
| xml_etree_generate   | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                        |
| pickle_pure_python   | 307 us                                                           | 318 us: 1.04x slower                                         |
| Geometric mean       | (ref)                                                            | 1.02x faster                                                 |

Benchmark hidden because not significant (3): pickle_list, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 13.2 ms                                                          | 11.6 ms: 1.14x faster                                        |
| python_startup_no_site | 8.85 ms                                                          | 8.64 ms: 1.02x faster                                        |
| Geometric mean         | (ref)                                                            | 1.08x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|-----------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 10.4 ms                                                          | 10.0 ms: 1.04x faster                                        |
| django_template | 39.0 ms                                                          | 38.2 ms: 1.02x faster                                        |
| Geometric mean  | (ref)                                                            | 1.03x faster                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 |
|----------------------------|:----------------------------------------------------------------:|:------------------------------------------------------------:|
| gc_traversal               | 4.69 ms                                                          | 3.48 ms: 1.35x faster                                        |
| create_gc_cycles           | 2.00 ms                                                          | 1.59 ms: 1.26x faster                                        |
| coverage                   | 83.5 ms                                                          | 66.7 ms: 1.25x faster                                        |
| telco                      | 8.40 ms                                                          | 6.96 ms: 1.21x faster                                        |
| richards_super             | 61.2 ms                                                          | 51.3 ms: 1.19x faster                                        |
| richards                   | 53.4 ms                                                          | 45.7 ms: 1.17x faster                                        |
| python_startup             | 13.2 ms                                                          | 11.6 ms: 1.14x faster                                        |
| typing_runtime_protocols   | 171 us                                                           | 152 us: 1.12x faster                                         |
| tomli_loads                | 2.40 sec                                                         | 2.16 sec: 1.11x faster                                       |
| go                         | 165 ms                                                           | 150 ms: 1.10x faster                                         |
| regex_v8                   | 26.0 ms                                                          | 23.6 ms: 1.10x faster                                        |
| pyflate                    | 482 ms                                                           | 439 ms: 1.10x faster                                         |
| scimark_sor                | 119 ms                                                           | 109 ms: 1.09x faster                                         |
| unpickle_pure_python       | 224 us                                                           | 210 us: 1.07x faster                                         |
| hexiom                     | 6.35 ms                                                          | 5.96 ms: 1.07x faster                                        |
| spectral_norm              | 97.3 ms                                                          | 91.6 ms: 1.06x faster                                        |
| unpickle                   | 15.7 us                                                          | 14.8 us: 1.06x faster                                        |
| json_dumps                 | 10.8 ms                                                          | 10.2 ms: 1.05x faster                                        |
| aiohttp                    | 1.07 ms                                                          | 1.02 ms: 1.05x faster                                        |
| float                      | 80.2 ms                                                          | 76.6 ms: 1.05x faster                                        |
| json                       | 5.35 ms                                                          | 5.12 ms: 1.05x faster                                        |
| regex_dna                  | 249 ms                                                           | 239 ms: 1.05x faster                                         |
| gunicorn                   | 1.04 ms                                                          | 1.00 ms: 1.04x faster                                        |
| deltablue                  | 3.37 ms                                                          | 3.24 ms: 1.04x faster                                        |
| docutils                   | 2.98 sec                                                         | 2.87 sec: 1.04x faster                                       |
| sqlglot_normalize          | 120 ms                                                           | 116 ms: 1.04x faster                                         |
| mako                       | 10.4 ms                                                          | 10.0 ms: 1.04x faster                                        |
| scimark_fft                | 312 ms                                                           | 301 ms: 1.04x faster                                         |
| sqlglot_optimize           | 59.5 ms                                                          | 57.5 ms: 1.04x faster                                        |
| sympy_expand               | 501 ms                                                           | 484 ms: 1.03x faster                                         |
| dulwich_log                | 67.3 ms                                                          | 65.4 ms: 1.03x faster                                        |
| json_loads                 | 25.0 us                                                          | 24.4 us: 1.03x faster                                        |
| python_startup_no_site     | 8.85 ms                                                          | 8.64 ms: 1.02x faster                                        |
| deepcopy                   | 377 us                                                           | 368 us: 1.02x faster                                         |
| chameleon                  | 7.40 ms                                                          | 7.23 ms: 1.02x faster                                        |
| xml_etree_process          | 59.7 ms                                                          | 58.4 ms: 1.02x faster                                        |
| 2to3                       | 291 ms                                                           | 285 ms: 1.02x faster                                         |
| django_template            | 39.0 ms                                                          | 38.2 ms: 1.02x faster                                        |
| asyncio_websockets         | 395 ms                                                           | 387 ms: 1.02x faster                                         |
| logging_silent             | 96.3 ns                                                          | 94.4 ns: 1.02x faster                                        |
| scimark_sparse_mat_mult    | 4.28 ms                                                          | 4.21 ms: 1.02x faster                                        |
| deepcopy_memo              | 37.3 us                                                          | 36.8 us: 1.01x faster                                        |
| pprint_safe_repr           | 818 ms                                                           | 807 ms: 1.01x faster                                         |
| sqlglot_parse              | 1.39 ms                                                          | 1.38 ms: 1.01x faster                                        |
| pickle_dict                | 32.8 us                                                          | 32.5 us: 1.01x faster                                        |
| unpickle_list              | 4.70 us                                                          | 4.66 us: 1.01x faster                                        |
| sqlite_synth               | 2.80 us                                                          | 2.77 us: 1.01x faster                                        |
| pickle                     | 10.6 us                                                          | 10.5 us: 1.01x faster                                        |
| fannkuch                   | 353 ms                                                           | 350 ms: 1.01x faster                                         |
| deepcopy_reduce            | 3.39 us                                                          | 3.37 us: 1.01x faster                                        |
| pprint_pformat             | 1.66 sec                                                         | 1.65 sec: 1.00x faster                                       |
| xml_etree_generate         | 85.7 ms                                                          | 86.1 ms: 1.00x slower                                        |
| asyncio_tcp_ssl            | 1.58 sec                                                         | 1.59 sec: 1.01x slower                                       |
| sqlglot_transpile          | 1.76 ms                                                          | 1.78 ms: 1.01x slower                                        |
| pycparser                  | 1.22 sec                                                         | 1.23 sec: 1.01x slower                                       |
| scimark_lu                 | 97.5 ms                                                          | 98.8 ms: 1.01x slower                                        |
| tornado_http               | 119 ms                                                           | 121 ms: 1.02x slower                                         |
| nqueens                    | 88.4 ms                                                          | 89.9 ms: 1.02x slower                                        |
| sympy_str                  | 295 ms                                                           | 302 ms: 1.03x slower                                         |
| sympy_integrate            | 23.2 ms                                                          | 23.9 ms: 1.03x slower                                        |
| pickle_pure_python         | 307 us                                                           | 318 us: 1.04x slower                                         |
| mdp                        | 2.46 sec                                                         | 2.57 sec: 1.04x slower                                       |
| pidigits                   | 254 ms                                                           | 265 ms: 1.04x slower                                         |
| bench_thread_pool          | 908 us                                                           | 950 us: 1.05x slower                                         |
| coroutines                 | 22.0 ms                                                          | 23.0 ms: 1.05x slower                                        |
| sympy_sum                  | 155 ms                                                           | 162 ms: 1.05x slower                                         |
| logging_simple             | 6.40 us                                                          | 6.71 us: 1.05x slower                                        |
| regex_effbot               | 3.40 ms                                                          | 3.57 ms: 1.05x slower                                        |
| logging_format             | 7.11 us                                                          | 7.48 us: 1.05x slower                                        |
| scimark_monte_carlo        | 65.5 ms                                                          | 69.0 ms: 1.05x slower                                        |
| chaos                      | 59.6 ms                                                          | 64.0 ms: 1.07x slower                                        |
| async_generators           | 363 ms                                                           | 390 ms: 1.08x slower                                         |
| mypy2                      | 764 ms                                                           | 830 ms: 1.09x slower                                         |
| crypto_pyaes               | 73.6 ms                                                          | 80.3 ms: 1.09x slower                                        |
| pathlib                    | 17.1 ms                                                          | 18.9 ms: 1.10x slower                                        |
| generators                 | 33.5 ms                                                          | 37.4 ms: 1.12x slower                                        |
| raytrace                   | 260 ms                                                           | 298 ms: 1.14x slower                                         |
| async_tree_cpu_io_mixed    | 604 ms                                                           | 696 ms: 1.15x slower                                         |
| async_tree_io_tg           | 900 ms                                                           | 1.05 sec: 1.17x slower                                       |
| async_tree_memoization     | 460 ms                                                           | 544 ms: 1.18x slower                                         |
| async_tree_io              | 873 ms                                                           | 1.04 sec: 1.19x slower                                       |
| async_tree_cpu_io_mixed_tg | 573 ms                                                           | 697 ms: 1.22x slower                                         |
| async_tree_none            | 365 ms                                                           | 452 ms: 1.24x slower                                         |
| async_tree_none_tg         | 340 ms                                                           | 431 ms: 1.27x slower                                         |
| async_tree_memoization_tg  | 421 ms                                                           | 540 ms: 1.28x slower                                         |
| comprehensions             | 17.0 us                                                          | 21.9 us: 1.29x slower                                        |
| Geometric mean             | (ref)                                                            | 1.00x faster                                                 |

Benchmark hidden because not significant (9): bench_mp_pool, pickle_list, regex_compile, meteor_contest, asyncio_tcp, xml_etree_parse, nbody, xml_etree_iterparse, dask
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence

# HPT report

- Reliability score: 70.35% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.09x