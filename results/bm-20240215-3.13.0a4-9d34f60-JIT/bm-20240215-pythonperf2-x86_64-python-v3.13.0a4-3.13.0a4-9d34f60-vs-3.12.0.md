# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a4
- machine: linux-x86_64
- commit hash: 9d34f60
- commit date: 2024-02-15
- overall geometric mean: 1.04x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 300 ms: 1.05x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.14 ms: 1.01x faster                                            |
| docutils       | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                           |
| tornado_http   | 121 ms                                                       | 126 ms: 1.04x slower                                             |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 434 ms: 1.04x faster                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 706 ms: 1.01x slower                                             |
| async_tree_memoization_tg  | 540 ms                                                       | 549 ms: 1.02x slower                                             |
| async_tree_none_tg         | 431 ms                                                       | 438 ms: 1.02x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.03x slower                                           |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.03x slower                                           |
| Geometric mean             | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): async_tree_memoization, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| float          | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                            |
| nbody          | 88.0 ms                                                      | 106 ms: 1.21x slower                                             |
| Geometric mean | (ref)                                                        | 1.08x slower                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                            |
| regex_compile  | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| regex_dna      | 239 ms                                                       | 244 ms: 1.02x slower                                             |
| regex_v8       | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| Geometric mean | (ref)                                                        | 1.02x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.6 us: 1.06x faster                                            |
| pickle_pure_python   | 318 us                                                       | 304 us: 1.05x faster                                             |
| xml_etree_generate   | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                            |
| pickle               | 10.5 us                                                      | 10.2 us: 1.03x faster                                            |
| xml_etree_process    | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.50 us: 1.02x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                            |
| xml_etree_parse      | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| unpickle             | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| json_loads           | 24.4 us                                                      | 25.6 us: 1.05x slower                                            |
| tomli_loads          | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                           |
| unpickle_pure_python | 210 us                                                       | 230 us: 1.10x slower                                             |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                     |

Benchmark hidden because not significant (2): unpickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.1 ms: 1.29x slower                                            |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.0 ms                                                      | 11.8 ms: 1.18x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240215-pythonperf2-x86_64-python-v3.13.0a4-3.13.0a4-9d34f60 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 117 us: 1.29x faster                                             |
| unpack_sequence            | 53.2 ns                                                      | 46.9 ns: 1.13x faster                                            |
| comprehensions             | 21.9 us                                                      | 19.3 us: 1.13x faster                                            |
| generators                 | 37.4 ms                                                      | 34.0 ms: 1.10x faster                                            |
| raytrace                   | 298 ms                                                       | 274 ms: 1.09x faster                                             |
| pickle_dict                | 32.5 us                                                      | 30.6 us: 1.06x faster                                            |
| async_generators           | 390 ms                                                       | 371 ms: 1.05x faster                                             |
| pickle_pure_python         | 318 us                                                       | 304 us: 1.05x faster                                             |
| async_tree_none            | 452 ms                                                       | 434 ms: 1.04x faster                                             |
| logging_format             | 7.48 us                                                      | 7.20 us: 1.04x faster                                            |
| coroutines                 | 23.0 ms                                                      | 22.3 ms: 1.03x faster                                            |
| xml_etree_generate         | 86.1 ms                                                      | 83.4 ms: 1.03x faster                                            |
| logging_simple             | 6.71 us                                                      | 6.51 us: 1.03x faster                                            |
| create_gc_cycles           | 1.59 ms                                                      | 1.55 ms: 1.03x faster                                            |
| pickle                     | 10.5 us                                                      | 10.2 us: 1.03x faster                                            |
| sympy_sum                  | 162 ms                                                       | 158 ms: 1.03x faster                                             |
| mdp                        | 2.57 sec                                                     | 2.53 sec: 1.02x faster                                           |
| sympy_str                  | 302 ms                                                       | 298 ms: 1.02x faster                                             |
| xml_etree_process          | 58.4 ms                                                      | 57.6 ms: 1.01x faster                                            |
| crypto_pyaes               | 80.3 ms                                                      | 79.3 ms: 1.01x faster                                            |
| chameleon                  | 7.23 ms                                                      | 7.14 ms: 1.01x faster                                            |
| regex_effbot               | 3.57 ms                                                      | 3.53 ms: 1.01x faster                                            |
| deepcopy_reduce            | 3.37 us                                                      | 3.33 us: 1.01x faster                                            |
| pidigits                   | 265 ms                                                       | 262 ms: 1.01x faster                                             |
| asyncio_tcp                | 378 ms                                                       | 374 ms: 1.01x faster                                             |
| asyncio_tcp_ssl            | 1.59 sec                                                     | 1.58 sec: 1.01x faster                                           |
| sympy_integrate            | 23.9 ms                                                      | 23.9 ms: 1.00x faster                                            |
| docutils                   | 2.87 sec                                                     | 2.88 sec: 1.00x slower                                           |
| deepcopy                   | 368 us                                                       | 370 us: 1.01x slower                                             |
| regex_compile              | 144 ms                                                       | 145 ms: 1.01x slower                                             |
| sqlglot_normalize          | 116 ms                                                       | 117 ms: 1.01x slower                                             |
| sqlglot_parse              | 1.38 ms                                                      | 1.39 ms: 1.01x slower                                            |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 706 ms: 1.01x slower                                             |
| pathlib                    | 18.9 ms                                                      | 19.1 ms: 1.01x slower                                            |
| async_tree_memoization_tg  | 540 ms                                                       | 549 ms: 1.02x slower                                             |
| async_tree_none_tg         | 431 ms                                                       | 438 ms: 1.02x slower                                             |
| pickle_list                | 4.43 us                                                      | 4.50 us: 1.02x slower                                            |
| meteor_contest             | 128 ms                                                       | 130 ms: 1.02x slower                                             |
| regex_dna                  | 239 ms                                                       | 244 ms: 1.02x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.82 ms: 1.02x slower                                            |
| pprint_safe_repr           | 807 ms                                                       | 826 ms: 1.02x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.08 sec: 1.03x slower                                           |
| json_dumps                 | 10.2 ms                                                      | 10.5 ms: 1.03x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 148 ms: 1.03x slower                                             |
| unpickle                   | 14.8 us                                                      | 15.3 us: 1.03x slower                                            |
| async_tree_io              | 1.04 sec                                                     | 1.08 sec: 1.03x slower                                           |
| logging_silent             | 94.4 ns                                                      | 97.7 ns: 1.03x slower                                            |
| sympy_expand               | 484 ms                                                       | 502 ms: 1.04x slower                                             |
| tornado_http               | 121 ms                                                       | 126 ms: 1.04x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.72 sec: 1.04x slower                                           |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.04x slower                                            |
| json_loads                 | 24.4 us                                                      | 25.6 us: 1.05x slower                                            |
| 2to3                       | 285 ms                                                       | 300 ms: 1.05x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 60.4 ms: 1.05x slower                                            |
| float                      | 76.6 ms                                                      | 80.7 ms: 1.05x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 25.0 ms: 1.06x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 69.1 ms: 1.06x slower                                            |
| nqueens                    | 89.9 ms                                                      | 95.4 ms: 1.06x slower                                            |
| tomli_loads                | 2.16 sec                                                     | 2.31 sec: 1.07x slower                                           |
| pycparser                  | 1.23 sec                                                     | 1.33 sec: 1.08x slower                                           |
| chaos                      | 64.0 ms                                                      | 69.4 ms: 1.09x slower                                            |
| python_startup             | 11.6 ms                                                      | 12.7 ms: 1.09x slower                                            |
| unpickle_pure_python       | 210 us                                                       | 230 us: 1.10x slower                                             |
| go                         | 150 ms                                                       | 167 ms: 1.12x slower                                             |
| richards_super             | 51.3 ms                                                      | 57.6 ms: 1.12x slower                                            |
| richards                   | 45.7 ms                                                      | 51.7 ms: 1.13x slower                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 78.5 ms: 1.14x slower                                            |
| deltablue                  | 3.24 ms                                                      | 3.69 ms: 1.14x slower                                            |
| telco                      | 6.96 ms                                                      | 8.12 ms: 1.17x slower                                            |
| fannkuch                   | 350 ms                                                       | 409 ms: 1.17x slower                                             |
| mako                       | 10.0 ms                                                      | 11.8 ms: 1.18x slower                                            |
| scimark_fft                | 301 ms                                                       | 357 ms: 1.19x slower                                             |
| nbody                      | 88.0 ms                                                      | 106 ms: 1.21x slower                                             |
| pyflate                    | 439 ms                                                       | 529 ms: 1.21x slower                                             |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.23 ms: 1.24x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 115 ms: 1.25x slower                                             |
| coverage                   | 66.7 ms                                                      | 84.4 ms: 1.27x slower                                            |
| hexiom                     | 5.96 ms                                                      | 7.63 ms: 1.28x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 11.1 ms: 1.29x slower                                            |
| scimark_sor                | 109 ms                                                       | 143 ms: 1.31x slower                                             |
| dask                       | 392 ms                                                       | 584 ms: 1.49x slower                                             |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                     |

Benchmark hidden because not significant (12): sqlite_synth, gc_traversal, asyncio_websockets, unpickle_list, deepcopy_memo, scimark_lu, xml_etree_iterparse, async_tree_memoization, async_tree_cpu_io_mixed, bench_thread_pool, bench_mp_pool, mypy2
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x


# Memory

- memory change: 0.91x