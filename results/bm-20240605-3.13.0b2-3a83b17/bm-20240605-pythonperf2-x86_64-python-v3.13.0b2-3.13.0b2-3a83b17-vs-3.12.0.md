# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.00x slower
- HPT reliability: 70.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.93x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 291 ms: 1.02x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.40 ms: 1.02x slower                                            |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                           |
| tornado_http   | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 421 ms: 1.28x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 340 ms: 1.27x faster                                             |
| async_tree_none            | 452 ms                                                       | 365 ms: 1.24x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 573 ms: 1.22x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 873 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 460 ms: 1.18x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 900 ms: 1.17x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                             |
| Geometric mean             | (ref)                                                        | 1.21x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 254 ms: 1.04x faster                                             |
| float          | 76.6 ms                                                      | 80.2 ms: 1.05x slower                                            |
| Geometric mean | (ref)                                                        | 1.00x faster                                                     |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                            |
| regex_dna      | 239 ms                                                       | 249 ms: 1.05x slower                                             |
| regex_v8       | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 318 us                                                       | 307 us: 1.04x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 85.7 ms: 1.00x faster                                            |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| unpickle_list        | 4.66 us                                                      | 4.70 us: 1.01x slower                                            |
| pickle_dict          | 32.5 us                                                      | 32.8 us: 1.01x slower                                            |
| xml_etree_process    | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                            |
| json_loads           | 24.4 us                                                      | 25.0 us: 1.03x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                            |
| unpickle             | 14.8 us                                                      | 15.7 us: 1.06x slower                                            |
| unpickle_pure_python | 210 us                                                       | 224 us: 1.07x slower                                             |
| tomli_loads          | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                           |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                     |

Benchmark hidden because not significant (3): xml_etree_iterparse, xml_etree_parse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 8.85 ms: 1.02x slower                                            |
| python_startup         | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                            |
| Geometric mean         | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                            |
| mako            | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| comprehensions             | 21.9 us                                                      | 17.0 us: 1.29x faster                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 421 ms: 1.28x faster                                             |
| async_tree_none_tg         | 431 ms                                                       | 340 ms: 1.27x faster                                             |
| async_tree_none            | 452 ms                                                       | 365 ms: 1.24x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 573 ms: 1.22x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 873 ms: 1.19x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 460 ms: 1.18x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 900 ms: 1.17x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 604 ms: 1.15x faster                                             |
| raytrace                   | 298 ms                                                       | 260 ms: 1.14x faster                                             |
| generators                 | 37.4 ms                                                      | 33.5 ms: 1.12x faster                                            |
| pathlib                    | 18.9 ms                                                      | 17.1 ms: 1.10x faster                                            |
| crypto_pyaes               | 80.3 ms                                                      | 73.6 ms: 1.09x faster                                            |
| mypy2                      | 830 ms                                                       | 764 ms: 1.09x faster                                             |
| async_generators           | 390 ms                                                       | 363 ms: 1.08x faster                                             |
| chaos                      | 64.0 ms                                                      | 59.6 ms: 1.07x faster                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.5 ms: 1.05x faster                                            |
| logging_format             | 7.48 us                                                      | 7.11 us: 1.05x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.40 ms: 1.05x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.40 us: 1.05x faster                                            |
| sympy_sum                  | 162 ms                                                       | 155 ms: 1.05x faster                                             |
| coroutines                 | 23.0 ms                                                      | 22.0 ms: 1.05x faster                                            |
| bench_thread_pool          | 950 us                                                       | 908 us: 1.05x faster                                             |
| pidigits                   | 265 ms                                                       | 254 ms: 1.04x faster                                             |
| mdp                        | 2.57 sec                                                     | 2.46 sec: 1.04x faster                                           |
| pickle_pure_python         | 318 us                                                       | 307 us: 1.04x faster                                             |
| sympy_integrate            | 23.9 ms                                                      | 23.2 ms: 1.03x faster                                            |
| sympy_str                  | 302 ms                                                       | 295 ms: 1.03x faster                                             |
| nqueens                    | 89.9 ms                                                      | 88.4 ms: 1.02x faster                                            |
| tornado_http               | 121 ms                                                       | 119 ms: 1.02x faster                                             |
| scimark_lu                 | 98.8 ms                                                      | 97.5 ms: 1.01x faster                                            |
| pycparser                  | 1.23 sec                                                     | 1.22 sec: 1.01x faster                                           |
| sqlglot_transpile          | 1.78 ms                                                      | 1.76 ms: 1.01x faster                                            |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| xml_etree_generate         | 86.1 ms                                                      | 85.7 ms: 1.00x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.66 sec: 1.00x slower                                           |
| deepcopy_reduce            | 3.37 us                                                      | 3.39 us: 1.01x slower                                            |
| fannkuch                   | 350 ms                                                       | 353 ms: 1.01x slower                                             |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                            |
| unpickle_list              | 4.66 us                                                      | 4.70 us: 1.01x slower                                            |
| pickle_dict                | 32.5 us                                                      | 32.8 us: 1.01x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| pprint_safe_repr           | 807 ms                                                       | 818 ms: 1.01x slower                                             |
| deepcopy_memo              | 36.8 us                                                      | 37.3 us: 1.01x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.28 ms: 1.02x slower                                            |
| logging_silent             | 94.4 ns                                                      | 96.3 ns: 1.02x slower                                            |
| asyncio_websockets         | 387 ms                                                       | 395 ms: 1.02x slower                                             |
| django_template            | 38.2 ms                                                      | 39.0 ms: 1.02x slower                                            |
| 2to3                       | 285 ms                                                       | 291 ms: 1.02x slower                                             |
| xml_etree_process          | 58.4 ms                                                      | 59.7 ms: 1.02x slower                                            |
| chameleon                  | 7.23 ms                                                      | 7.40 ms: 1.02x slower                                            |
| deepcopy                   | 368 us                                                       | 377 us: 1.02x slower                                             |
| python_startup_no_site     | 8.64 ms                                                      | 8.85 ms: 1.02x slower                                            |
| json_loads                 | 24.4 us                                                      | 25.0 us: 1.03x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 67.3 ms: 1.03x slower                                            |
| sympy_expand               | 484 ms                                                       | 501 ms: 1.03x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 59.5 ms: 1.04x slower                                            |
| scimark_fft                | 301 ms                                                       | 312 ms: 1.04x slower                                             |
| mako                       | 10.0 ms                                                      | 10.4 ms: 1.04x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 120 ms: 1.04x slower                                             |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                           |
| deltablue                  | 3.24 ms                                                      | 3.37 ms: 1.04x slower                                            |
| gunicorn                   | 1.00 ms                                                      | 1.04 ms: 1.04x slower                                            |
| regex_dna                  | 239 ms                                                       | 249 ms: 1.05x slower                                             |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.05x slower                                            |
| float                      | 76.6 ms                                                      | 80.2 ms: 1.05x slower                                            |
| aiohttp                    | 1.02 ms                                                      | 1.07 ms: 1.05x slower                                            |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.05x slower                                            |
| unpickle                   | 14.8 us                                                      | 15.7 us: 1.06x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 97.3 ms: 1.06x slower                                            |
| hexiom                     | 5.96 ms                                                      | 6.35 ms: 1.07x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 224 us: 1.07x slower                                             |
| scimark_sor                | 109 ms                                                       | 119 ms: 1.09x slower                                             |
| pyflate                    | 439 ms                                                       | 482 ms: 1.10x slower                                             |
| regex_v8                   | 23.6 ms                                                      | 26.0 ms: 1.10x slower                                            |
| go                         | 150 ms                                                       | 165 ms: 1.10x slower                                             |
| tomli_loads                | 2.16 sec                                                     | 2.40 sec: 1.11x slower                                           |
| typing_runtime_protocols   | 152 us                                                       | 171 us: 1.12x slower                                             |
| python_startup             | 11.6 ms                                                      | 13.2 ms: 1.14x slower                                            |
| richards                   | 45.7 ms                                                      | 53.4 ms: 1.17x slower                                            |
| richards_super             | 51.3 ms                                                      | 61.2 ms: 1.19x slower                                            |
| telco                      | 6.96 ms                                                      | 8.40 ms: 1.21x slower                                            |
| coverage                   | 66.7 ms                                                      | 83.5 ms: 1.25x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 2.00 ms: 1.26x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 4.69 ms: 1.35x slower                                            |
| Geometric mean             | (ref)                                                        | 1.00x slower                                                     |

Benchmark hidden because not significant (9): dask, xml_etree_iterparse, nbody, xml_etree_parse, asyncio_tcp, meteor_contest, regex_compile, pickle_list, bench_mp_pool
Ignored benchmarks (3) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 70.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.93x