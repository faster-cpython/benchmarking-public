
# Results vs. 3.12.0

- fork: python
- ref: v3.13.0a3
- machine: linux-x86_64
- commit hash: f009305
- commit date: 2024-01-17
- overall geometric mean: 1.10x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 0.88x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 308 ms: 1.08x slower                                             |
| chameleon      | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                            |
| docutils       | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                           |
| tornado_http   | 121 ms                                                       | 123 ms: 1.02x slower                                             |
| Geometric mean | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none            | 452 ms                                                       | 446 ms: 1.01x faster                                             |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 710 ms: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 713 ms: 1.02x slower                                             |
| async_tree_none_tg         | 431 ms                                                       | 442 ms: 1.03x slower                                             |
| async_tree_memoization     | 544 ms                                                       | 558 ms: 1.03x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                           |
| async_tree_io              | 1.04 sec                                                     | 1.10 sec: 1.05x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 570 ms: 1.05x slower                                             |
| Geometric mean             | (ref)                                                        | 1.03x slower                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 103 ms: 1.34x slower                                             |
| nbody          | 88.0 ms                                                      | 125 ms: 1.42x slower                                             |
| Geometric mean | (ref)                                                        | 1.24x slower                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                            |
| regex_dna      | 239 ms                                                       | 240 ms: 1.01x slower                                             |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                            |
| regex_compile  | 144 ms                                                       | 170 ms: 1.18x slower                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_dict          | 32.5 us                                                      | 30.7 us: 1.06x faster                                            |
| pickle_list          | 4.43 us                                                      | 4.32 us: 1.03x faster                                            |
| pickle_pure_python   | 318 us                                                       | 311 us: 1.02x faster                                             |
| pickle               | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| xml_etree_parse      | 144 ms                                                       | 146 ms: 1.01x slower                                             |
| unpickle             | 14.8 us                                                      | 15.1 us: 1.02x slower                                            |
| unpickle_list        | 4.66 us                                                      | 4.74 us: 1.02x slower                                            |
| json_loads           | 24.4 us                                                      | 25.1 us: 1.03x slower                                            |
| xml_etree_generate   | 86.1 ms                                                      | 90.9 ms: 1.06x slower                                            |
| json_dumps           | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                            |
| xml_etree_process    | 58.4 ms                                                      | 62.3 ms: 1.07x slower                                            |
| xml_etree_iterparse  | 103 ms                                                       | 117 ms: 1.14x slower                                             |
| unpickle_pure_python | 210 us                                                       | 245 us: 1.17x slower                                             |
| tomli_loads          | 2.16 sec                                                     | 2.82 sec: 1.31x slower                                           |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.6 ms                                                      | 12.5 ms: 1.08x slower                                            |
| python_startup_no_site | 8.64 ms                                                      | 11.0 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                        | 1.17x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|-----------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako      | 10.0 ms                                                      | 14.8 ms: 1.48x slower                                            |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240117-pythonperf2-x86_64-python-v3.13.0a3-3.13.0a3-f009305 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols   | 152 us                                                       | 124 us: 1.22x faster                                             |
| unpack_sequence            | 53.2 ns                                                      | 44.2 ns: 1.20x faster                                            |
| generators                 | 37.4 ms                                                      | 34.3 ms: 1.09x faster                                            |
| pickle_dict                | 32.5 us                                                      | 30.7 us: 1.06x faster                                            |
| async_generators           | 390 ms                                                       | 372 ms: 1.05x faster                                             |
| regex_effbot               | 3.57 ms                                                      | 3.43 ms: 1.04x faster                                            |
| pickle_list                | 4.43 us                                                      | 4.32 us: 1.03x faster                                            |
| pickle_pure_python         | 318 us                                                       | 311 us: 1.02x faster                                             |
| coroutines                 | 23.0 ms                                                      | 22.5 ms: 1.02x faster                                            |
| pickle                     | 10.5 us                                                      | 10.3 us: 1.02x faster                                            |
| logging_format             | 7.48 us                                                      | 7.38 us: 1.01x faster                                            |
| async_tree_none            | 452 ms                                                       | 446 ms: 1.01x faster                                             |
| asyncio_tcp                | 378 ms                                                       | 375 ms: 1.01x faster                                             |
| regex_dna                  | 239 ms                                                       | 240 ms: 1.01x slower                                             |
| deepcopy_reduce            | 3.37 us                                                      | 3.41 us: 1.01x slower                                            |
| sqlite_synth               | 2.77 us                                                      | 2.80 us: 1.01x slower                                            |
| pathlib                    | 18.9 ms                                                      | 19.1 ms: 1.01x slower                                            |
| xml_etree_parse            | 144 ms                                                       | 146 ms: 1.01x slower                                             |
| unpickle                   | 14.8 us                                                      | 15.1 us: 1.02x slower                                            |
| tornado_http               | 121 ms                                                       | 123 ms: 1.02x slower                                             |
| unpickle_list              | 4.66 us                                                      | 4.74 us: 1.02x slower                                            |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 710 ms: 1.02x slower                                             |
| bench_thread_pool          | 950 us                                                       | 969 us: 1.02x slower                                             |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 713 ms: 1.02x slower                                             |
| raytrace                   | 298 ms                                                       | 305 ms: 1.02x slower                                             |
| docutils                   | 2.87 sec                                                     | 2.94 sec: 1.02x slower                                           |
| logging_simple             | 6.71 us                                                      | 6.88 us: 1.02x slower                                            |
| async_tree_none_tg         | 431 ms                                                       | 442 ms: 1.03x slower                                             |
| async_tree_memoization     | 544 ms                                                       | 558 ms: 1.03x slower                                             |
| sympy_sum                  | 162 ms                                                       | 166 ms: 1.03x slower                                             |
| mdp                        | 2.57 sec                                                     | 2.64 sec: 1.03x slower                                           |
| json_loads                 | 24.4 us                                                      | 25.1 us: 1.03x slower                                            |
| deepcopy                   | 368 us                                                       | 379 us: 1.03x slower                                             |
| async_tree_io_tg           | 1.05 sec                                                     | 1.09 sec: 1.03x slower                                           |
| sympy_integrate            | 23.9 ms                                                      | 24.8 ms: 1.04x slower                                            |
| dask                       | 392 ms                                                       | 407 ms: 1.04x slower                                             |
| json                       | 5.12 ms                                                      | 5.35 ms: 1.05x slower                                            |
| logging_silent             | 94.4 ns                                                      | 98.9 ns: 1.05x slower                                            |
| async_tree_io              | 1.04 sec                                                     | 1.10 sec: 1.05x slower                                           |
| async_tree_memoization_tg  | 540 ms                                                       | 570 ms: 1.05x slower                                             |
| sqlglot_transpile          | 1.78 ms                                                      | 1.87 ms: 1.05x slower                                            |
| xml_etree_generate         | 86.1 ms                                                      | 90.9 ms: 1.06x slower                                            |
| sqlglot_parse              | 1.38 ms                                                      | 1.45 ms: 1.06x slower                                            |
| scimark_lu                 | 98.8 ms                                                      | 104 ms: 1.06x slower                                             |
| json_dumps                 | 10.2 ms                                                      | 10.8 ms: 1.06x slower                                            |
| sympy_str                  | 302 ms                                                       | 322 ms: 1.07x slower                                             |
| xml_etree_process          | 58.4 ms                                                      | 62.3 ms: 1.07x slower                                            |
| sqlglot_normalize          | 116 ms                                                       | 124 ms: 1.07x slower                                             |
| gc_traversal               | 3.48 ms                                                      | 3.74 ms: 1.08x slower                                            |
| mypy2                      | 830 ms                                                       | 893 ms: 1.08x slower                                             |
| crypto_pyaes               | 80.3 ms                                                      | 86.6 ms: 1.08x slower                                            |
| python_startup             | 11.6 ms                                                      | 12.5 ms: 1.08x slower                                            |
| 2to3                       | 285 ms                                                       | 308 ms: 1.08x slower                                             |
| meteor_contest             | 128 ms                                                       | 139 ms: 1.08x slower                                             |
| chameleon                  | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                            |
| deepcopy_memo              | 36.8 us                                                      | 40.3 us: 1.10x slower                                            |
| dulwich_log                | 65.4 ms                                                      | 72.1 ms: 1.10x slower                                            |
| pycparser                  | 1.23 sec                                                     | 1.36 sec: 1.10x slower                                           |
| sympy_expand               | 484 ms                                                       | 534 ms: 1.10x slower                                             |
| sqlglot_optimize           | 57.5 ms                                                      | 63.6 ms: 1.11x slower                                            |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                            |
| xml_etree_iterparse        | 103 ms                                                       | 117 ms: 1.14x slower                                             |
| comprehensions             | 21.9 us                                                      | 25.0 us: 1.14x slower                                            |
| pprint_safe_repr           | 807 ms                                                       | 921 ms: 1.14x slower                                             |
| pprint_pformat             | 1.65 sec                                                     | 1.90 sec: 1.15x slower                                           |
| unpickle_pure_python       | 210 us                                                       | 245 us: 1.17x slower                                             |
| richards_super             | 51.3 ms                                                      | 60.0 ms: 1.17x slower                                            |
| regex_compile              | 144 ms                                                       | 170 ms: 1.18x slower                                             |
| telco                      | 6.96 ms                                                      | 8.28 ms: 1.19x slower                                            |
| richards                   | 45.7 ms                                                      | 54.5 ms: 1.19x slower                                            |
| nqueens                    | 89.9 ms                                                      | 108 ms: 1.20x slower                                             |
| go                         | 150 ms                                                       | 180 ms: 1.20x slower                                             |
| chaos                      | 64.0 ms                                                      | 77.4 ms: 1.21x slower                                            |
| coverage                   | 66.7 ms                                                      | 81.8 ms: 1.23x slower                                            |
| python_startup_no_site     | 8.64 ms                                                      | 11.0 ms: 1.28x slower                                            |
| scimark_monte_carlo        | 69.0 ms                                                      | 88.7 ms: 1.29x slower                                            |
| tomli_loads                | 2.16 sec                                                     | 2.82 sec: 1.31x slower                                           |
| pyflate                    | 439 ms                                                       | 582 ms: 1.33x slower                                             |
| float                      | 76.6 ms                                                      | 103 ms: 1.34x slower                                             |
| scimark_sor                | 109 ms                                                       | 147 ms: 1.35x slower                                             |
| fannkuch                   | 350 ms                                                       | 481 ms: 1.37x slower                                             |
| nbody                      | 88.0 ms                                                      | 125 ms: 1.42x slower                                             |
| scimark_fft                | 301 ms                                                       | 429 ms: 1.42x slower                                             |
| mako                       | 10.0 ms                                                      | 14.8 ms: 1.48x slower                                            |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 6.49 ms: 1.54x slower                                            |
| hexiom                     | 5.96 ms                                                      | 9.82 ms: 1.65x slower                                            |
| deltablue                  | 3.24 ms                                                      | 5.40 ms: 1.67x slower                                            |
| spectral_norm              | 91.6 ms                                                      | 161 ms: 1.76x slower                                             |
| Geometric mean             | (ref)                                                        | 1.10x slower                                                     |

Benchmark hidden because not significant (5): bench_mp_pool, asyncio_tcp_ssl, pidigits, create_gc_cycles, asyncio_websockets
Ignored benchmarks (5) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, django_template, gunicorn, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.05x
- 99% likely to have a slowdown of 1.04x


# Memory

- memory change: 0.88x