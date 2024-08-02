# Results vs. 3.12.0

- fork: python
- ref: v3.13.0b2
- machine: linux-x86_64
- commit hash: 3a83b17
- commit date: 2024-06-05
- overall geometric mean: 1.01x slower
- HPT reliability: 57.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 305 ms: 1.07x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.48 ms: 1.04x slower                                            |
| tornado_http   | 121 ms                                                       | 123 ms: 1.01x slower                                             |
| Geometric mean | (ref)                                                        | 1.04x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 349 ms: 1.24x faster                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 441 ms: 1.22x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 454 ms: 1.20x faster                                             |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 891 ms: 1.18x faster                                             |
| async_tree_io              | 1.04 sec                                                     | 921 ms: 1.13x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 628 ms: 1.11x faster                                             |
| Geometric mean             | (ref)                                                        | 1.18x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| nbody          | 88.0 ms                                                      | 82.9 ms: 1.06x faster                                            |
| pidigits       | 265 ms                                                       | 250 ms: 1.06x faster                                             |
| float          | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                            |
| Geometric mean | (ref)                                                        | 1.05x faster                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| regex_effbot   | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                            |
| regex_dna      | 239 ms                                                       | 248 ms: 1.04x slower                                             |
| regex_v8       | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.9 us: 1.05x faster                                            |
| xml_etree_generate   | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                            |
| xml_etree_iterparse  | 103 ms                                                       | 99.3 ms: 1.04x faster                                            |
| tomli_loads          | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                           |
| pickle_pure_python   | 318 us                                                       | 310 us: 1.03x faster                                             |
| pickle_list          | 4.43 us                                                      | 4.35 us: 1.02x faster                                            |
| pickle               | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| unpickle_pure_python | 210 us                                                       | 211 us: 1.01x slower                                             |
| xml_etree_parse      | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| unpickle_list        | 4.66 us                                                      | 4.75 us: 1.02x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                            |
| unpickle             | 14.8 us                                                      | 15.6 us: 1.05x slower                                            |
| Geometric mean       | (ref)                                                        | 1.01x faster                                                     |

Benchmark hidden because not significant (2): json_loads, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                            |
| python_startup         | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                            |
| Geometric mean         | (ref)                                                        | 1.14x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                            |
| django_template | 38.2 ms                                                      | 41.4 ms: 1.09x slower                                            |
| Geometric mean  | (ref)                                                        | 1.01x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none_tg         | 431 ms                                                       | 349 ms: 1.24x faster                                             |
| comprehensions             | 21.9 us                                                      | 17.8 us: 1.23x faster                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 441 ms: 1.22x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 582 ms: 1.20x faster                                             |
| async_tree_memoization     | 544 ms                                                       | 454 ms: 1.20x faster                                             |
| async_tree_none            | 452 ms                                                       | 380 ms: 1.19x faster                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 891 ms: 1.18x faster                                             |
| crypto_pyaes               | 80.3 ms                                                      | 70.6 ms: 1.14x faster                                            |
| async_tree_io              | 1.04 sec                                                     | 921 ms: 1.13x faster                                             |
| spectral_norm              | 91.6 ms                                                      | 82.3 ms: 1.11x faster                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 628 ms: 1.11x faster                                             |
| mako                       | 10.0 ms                                                      | 9.10 ms: 1.10x faster                                            |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                            |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.08x faster                                            |
| nbody                      | 88.0 ms                                                      | 82.9 ms: 1.06x faster                                            |
| pidigits                   | 265 ms                                                       | 250 ms: 1.06x faster                                             |
| fannkuch                   | 350 ms                                                       | 331 ms: 1.06x faster                                             |
| pickle_dict                | 32.5 us                                                      | 30.9 us: 1.05x faster                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 3.99 ms: 1.05x faster                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 65.9 ms: 1.05x faster                                            |
| xml_etree_generate         | 86.1 ms                                                      | 82.4 ms: 1.05x faster                                            |
| logging_format             | 7.48 us                                                      | 7.17 us: 1.04x faster                                            |
| regex_compile              | 144 ms                                                       | 139 ms: 1.04x faster                                             |
| xml_etree_iterparse        | 103 ms                                                       | 99.3 ms: 1.04x faster                                            |
| tomli_loads                | 2.16 sec                                                     | 2.09 sec: 1.03x faster                                           |
| float                      | 76.6 ms                                                      | 74.2 ms: 1.03x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                            |
| scimark_fft                | 301 ms                                                       | 292 ms: 1.03x faster                                             |
| pickle_pure_python         | 318 us                                                       | 310 us: 1.03x faster                                             |
| pprint_safe_repr           | 807 ms                                                       | 792 ms: 1.02x faster                                             |
| pickle_list                | 4.43 us                                                      | 4.35 us: 1.02x faster                                            |
| pprint_pformat             | 1.65 sec                                                     | 1.63 sec: 1.02x faster                                           |
| logging_simple             | 6.71 us                                                      | 6.61 us: 1.01x faster                                            |
| mdp                        | 2.57 sec                                                     | 2.55 sec: 1.01x faster                                           |
| raytrace                   | 298 ms                                                       | 297 ms: 1.00x faster                                             |
| async_generators           | 390 ms                                                       | 389 ms: 1.00x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.00x faster                                           |
| regex_effbot               | 3.57 ms                                                      | 3.56 ms: 1.00x faster                                            |
| pickle                     | 10.5 us                                                      | 10.6 us: 1.01x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 211 us: 1.01x slower                                             |
| chaos                      | 64.0 ms                                                      | 64.4 ms: 1.01x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 37.2 us: 1.01x slower                                            |
| asyncio_websockets         | 387 ms                                                       | 391 ms: 1.01x slower                                             |
| asyncio_tcp                | 378 ms                                                       | 382 ms: 1.01x slower                                             |
| tornado_http               | 121 ms                                                       | 123 ms: 1.01x slower                                             |
| dulwich_log                | 65.4 ms                                                      | 66.2 ms: 1.01x slower                                            |
| pycparser                  | 1.23 sec                                                     | 1.25 sec: 1.01x slower                                           |
| richards                   | 45.7 ms                                                      | 46.5 ms: 1.02x slower                                            |
| sympy_sum                  | 162 ms                                                       | 165 ms: 1.02x slower                                             |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                             |
| unpickle_list              | 4.66 us                                                      | 4.75 us: 1.02x slower                                            |
| pyflate                    | 439 ms                                                       | 449 ms: 1.02x slower                                             |
| sympy_str                  | 302 ms                                                       | 310 ms: 1.03x slower                                             |
| richards_super             | 51.3 ms                                                      | 52.8 ms: 1.03x slower                                            |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.03x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.42 ms: 1.03x slower                                            |
| chameleon                  | 7.23 ms                                                      | 7.48 ms: 1.04x slower                                            |
| json                       | 5.12 ms                                                      | 5.30 ms: 1.04x slower                                            |
| dask                       | 392 ms                                                       | 408 ms: 1.04x slower                                             |
| regex_dna                  | 239 ms                                                       | 248 ms: 1.04x slower                                             |
| json_dumps                 | 10.2 ms                                                      | 10.7 ms: 1.04x slower                                            |
| unpickle                   | 14.8 us                                                      | 15.6 us: 1.05x slower                                            |
| sympy_integrate            | 23.9 ms                                                      | 25.4 ms: 1.06x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 25.2 ms: 1.07x slower                                            |
| 2to3                       | 285 ms                                                       | 305 ms: 1.07x slower                                             |
| nqueens                    | 89.9 ms                                                      | 97.2 ms: 1.08x slower                                            |
| django_template            | 38.2 ms                                                      | 41.4 ms: 1.09x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 9.44 ms: 1.09x slower                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.68 us: 1.09x slower                                            |
| sqlglot_optimize           | 57.5 ms                                                      | 62.9 ms: 1.09x slower                                            |
| sympy_expand               | 484 ms                                                       | 532 ms: 1.10x slower                                             |
| sqlglot_normalize          | 116 ms                                                       | 127 ms: 1.10x slower                                             |
| go                         | 150 ms                                                       | 166 ms: 1.11x slower                                             |
| deepcopy                   | 368 us                                                       | 410 us: 1.11x slower                                             |
| hexiom                     | 5.96 ms                                                      | 6.65 ms: 1.12x slower                                            |
| gunicorn                   | 1.00 ms                                                      | 1.15 ms: 1.15x slower                                            |
| scimark_lu                 | 98.8 ms                                                      | 114 ms: 1.15x slower                                             |
| aiohttp                    | 1.02 ms                                                      | 1.17 ms: 1.15x slower                                            |
| telco                      | 6.96 ms                                                      | 8.05 ms: 1.16x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.81 ms: 1.18x slower                                            |
| python_startup             | 11.6 ms                                                      | 13.8 ms: 1.19x slower                                            |
| typing_runtime_protocols   | 152 us                                                       | 184 us: 1.21x slower                                             |
| coverage                   | 66.7 ms                                                      | 80.7 ms: 1.21x slower                                            |
| create_gc_cycles           | 1.59 ms                                                      | 1.94 ms: 1.22x slower                                            |
| gc_traversal               | 3.48 ms                                                      | 4.49 ms: 1.29x slower                                            |
| logging_silent             | 94.4 ns                                                      | 123 ns: 1.31x slower                                             |
| scimark_sor                | 109 ms                                                       | 144 ms: 1.32x slower                                             |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (5): bench_thread_pool, json_loads, xml_etree_process, bench_mp_pool, mypy2
Ignored benchmarks (4) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: docutils, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17-JIT/bm-20240605-pythonperf2-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: bpe_tokeniser, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 57.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x