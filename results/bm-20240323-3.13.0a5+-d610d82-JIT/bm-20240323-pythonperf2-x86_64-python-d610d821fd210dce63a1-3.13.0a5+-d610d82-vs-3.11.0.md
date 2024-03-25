# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.04x faster
- HPT reliability: 78.75%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 302 ms: 1.05x slower                                                         |
| chameleon      | 7.92 ms                                                      | 7.29 ms: 1.09x faster                                                        |
| docutils       | 2.85 sec                                                     | 3.04 sec: 1.07x slower                                                       |
| html5lib       | 72.2 ms                                                      | 73.4 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 629 ms                                                       | 442 ms: 1.42x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 436 ms: 1.38x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 347 ms: 1.37x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 860 ms: 1.36x faster                                                         |
| async_tree_none            | 518 ms                                                       | 385 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 868 ms: 1.33x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 588 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 608 ms: 1.24x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 74.9 ms                                                      | 76.2 ms: 1.02x slower                                                        |
| pidigits       | 251 ms                                                       | 262 ms: 1.04x slower                                                         |
| nbody          | 92.9 ms                                                      | 100 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 145 ms: 1.08x faster                                                         |
| regex_effbot   | 3.34 ms                                                      | 3.47 ms: 1.04x slower                                                        |
| regex_v8       | 24.4 ms                                                      | 25.7 ms: 1.05x slower                                                        |
| regex_dna      | 227 ms                                                       | 249 ms: 1.10x slower                                                         |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                        |
| json_loads           | 28.9 us                                                      | 25.4 us: 1.14x faster                                                        |
| pickle_dict          | 32.3 us                                                      | 30.6 us: 1.06x faster                                                        |
| xml_etree_parse      | 155 ms                                                       | 147 ms: 1.05x faster                                                         |
| tomli_loads          | 2.25 sec                                                     | 2.14 sec: 1.05x faster                                                       |
| unpickle_pure_python | 238 us                                                       | 230 us: 1.04x faster                                                         |
| pickle_pure_python   | 316 us                                                       | 308 us: 1.03x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                       | 104 ms: 1.02x faster                                                         |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| xml_etree_generate   | 79.7 ms                                                      | 82.9 ms: 1.04x slower                                                        |
| xml_etree_process    | 55.9 ms                                                      | 58.6 ms: 1.05x slower                                                        |
| pickle_list          | 3.94 us                                                      | 4.49 us: 1.14x slower                                                        |
| unpickle             | 13.3 us                                                      | 15.1 us: 1.14x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 14.2 ms: 1.32x slower                                                        |
| python_startup_no_site | 7.73 ms                                                      | 12.5 ms: 1.61x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.46x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |
| django_template | 39.3 ms                                                      | 40.4 ms: 1.03x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 62.5 ms: 1.09x slower                                                        |
| genshi_text     | 25.5 ms                                                      | 29.2 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 121 us: 4.38x faster                                                         |
| asyncio_tcp                | 747 ms                                                       | 378 ms: 1.98x faster                                                         |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.93x faster                                                       |
| generators                 | 54.6 ms                                                      | 33.3 ms: 1.64x faster                                                        |
| pylint                     | 514 ms                                                       | 361 ms: 1.43x faster                                                         |
| async_tree_memoization     | 629 ms                                                       | 442 ms: 1.42x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 436 ms: 1.38x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 347 ms: 1.37x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 860 ms: 1.36x faster                                                         |
| async_tree_none            | 518 ms                                                       | 385 ms: 1.35x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 868 ms: 1.33x faster                                                         |
| comprehensions             | 25.1 us                                                      | 19.6 us: 1.28x faster                                                        |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 588 ms: 1.28x faster                                                         |
| json_dumps                 | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                        |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 608 ms: 1.24x faster                                                         |
| coroutines                 | 27.8 ms                                                      | 22.6 ms: 1.23x faster                                                        |
| sympy_sum                  | 186 ms                                                       | 161 ms: 1.15x faster                                                         |
| json_loads                 | 28.9 us                                                      | 25.4 us: 1.14x faster                                                        |
| sympy_str                  | 337 ms                                                       | 302 ms: 1.11x faster                                                         |
| richards_super             | 63.6 ms                                                      | 57.2 ms: 1.11x faster                                                        |
| chaos                      | 74.9 ms                                                      | 67.6 ms: 1.11x faster                                                        |
| mako                       | 11.0 ms                                                      | 10.0 ms: 1.10x faster                                                        |
| logging_simple             | 7.24 us                                                      | 6.64 us: 1.09x faster                                                        |
| chameleon                  | 7.92 ms                                                      | 7.29 ms: 1.09x faster                                                        |
| sympy_expand               | 553 ms                                                       | 512 ms: 1.08x faster                                                         |
| regex_compile              | 156 ms                                                       | 145 ms: 1.08x faster                                                         |
| sqlglot_parse              | 1.51 ms                                                      | 1.41 ms: 1.07x faster                                                        |
| mdp                        | 2.77 sec                                                     | 2.58 sec: 1.07x faster                                                       |
| deltablue                  | 3.97 ms                                                      | 3.70 ms: 1.07x faster                                                        |
| bench_thread_pool          | 1.00 ms                                                      | 936 us: 1.07x faster                                                         |
| thrift                     | 931 us                                                       | 878 us: 1.06x faster                                                         |
| crypto_pyaes               | 83.3 ms                                                      | 78.6 ms: 1.06x faster                                                        |
| pickle_dict                | 32.3 us                                                      | 30.6 us: 1.06x faster                                                        |
| xml_etree_parse            | 155 ms                                                       | 147 ms: 1.05x faster                                                         |
| sqlglot_transpile          | 1.91 ms                                                      | 1.82 ms: 1.05x faster                                                        |
| tomli_loads                | 2.25 sec                                                     | 2.14 sec: 1.05x faster                                                       |
| create_gc_cycles           | 1.58 ms                                                      | 1.50 ms: 1.05x faster                                                        |
| logging_format             | 7.71 us                                                      | 7.35 us: 1.05x faster                                                        |
| fannkuch                   | 416 ms                                                       | 398 ms: 1.04x faster                                                         |
| unpickle_pure_python       | 238 us                                                       | 230 us: 1.04x faster                                                         |
| json                       | 5.58 ms                                                      | 5.39 ms: 1.04x faster                                                        |
| logging_silent             | 100 ns                                                       | 96.9 ns: 1.04x faster                                                        |
| pycparser                  | 1.31 sec                                                     | 1.27 sec: 1.03x faster                                                       |
| deepcopy                   | 391 us                                                       | 380 us: 1.03x faster                                                         |
| sympy_integrate            | 25.8 ms                                                      | 25.1 ms: 1.03x faster                                                        |
| dask                       | 410 ms                                                       | 399 ms: 1.03x faster                                                         |
| pickle_pure_python         | 316 us                                                       | 308 us: 1.03x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                       | 104 ms: 1.02x faster                                                         |
| deepcopy_reduce            | 3.40 us                                                      | 3.36 us: 1.01x faster                                                        |
| nqueens                    | 103 ms                                                       | 102 ms: 1.01x faster                                                         |
| meteor_contest             | 131 ms                                                       | 130 ms: 1.00x faster                                                         |
| raytrace                   | 309 ms                                                       | 311 ms: 1.01x slower                                                         |
| dulwich_log                | 67.4 ms                                                      | 67.9 ms: 1.01x slower                                                        |
| sqlglot_normalize          | 122 ms                                                       | 123 ms: 1.01x slower                                                         |
| deepcopy_memo              | 37.5 us                                                      | 38.0 us: 1.01x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.01x slower                                                        |
| html5lib                   | 72.2 ms                                                      | 73.4 ms: 1.02x slower                                                        |
| scimark_lu                 | 114 ms                                                       | 116 ms: 1.02x slower                                                         |
| float                      | 74.9 ms                                                      | 76.2 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.14 ms: 1.02x slower                                                        |
| richards                   | 49.7 ms                                                      | 50.9 ms: 1.02x slower                                                        |
| django_template            | 39.3 ms                                                      | 40.4 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.67 sec                                                     | 1.71 sec: 1.03x slower                                                       |
| pickle                     | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| gc_traversal               | 4.15 ms                                                      | 4.30 ms: 1.04x slower                                                        |
| regex_effbot               | 3.34 ms                                                      | 3.47 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 805 ms                                                       | 837 ms: 1.04x slower                                                         |
| xml_etree_generate         | 79.7 ms                                                      | 82.9 ms: 1.04x slower                                                        |
| pidigits                   | 251 ms                                                       | 262 ms: 1.04x slower                                                         |
| xml_etree_process          | 55.9 ms                                                      | 58.6 ms: 1.05x slower                                                        |
| hexiom                     | 6.98 ms                                                      | 7.34 ms: 1.05x slower                                                        |
| regex_v8                   | 24.4 ms                                                      | 25.7 ms: 1.05x slower                                                        |
| 2to3                       | 287 ms                                                       | 302 ms: 1.05x slower                                                         |
| docutils                   | 2.85 sec                                                     | 3.04 sec: 1.07x slower                                                       |
| sqlglot_optimize           | 59.0 ms                                                      | 63.0 ms: 1.07x slower                                                        |
| mypy2                      | 762 ms                                                       | 818 ms: 1.07x slower                                                         |
| nbody                      | 92.9 ms                                                      | 100 ms: 1.08x slower                                                         |
| sqlite_synth               | 2.52 us                                                      | 2.72 us: 1.08x slower                                                        |
| scimark_monte_carlo        | 69.8 ms                                                      | 75.9 ms: 1.09x slower                                                        |
| go                         | 158 ms                                                       | 172 ms: 1.09x slower                                                         |
| genshi_xml                 | 57.1 ms                                                      | 62.5 ms: 1.09x slower                                                        |
| regex_dna                  | 227 ms                                                       | 249 ms: 1.10x slower                                                         |
| aiohttp                    | 986 us                                                       | 1.11 ms: 1.13x slower                                                        |
| gunicorn                   | 966 us                                                       | 1.09 ms: 1.13x slower                                                        |
| scimark_fft                | 281 ms                                                       | 318 ms: 1.13x slower                                                         |
| pickle_list                | 3.94 us                                                      | 4.49 us: 1.14x slower                                                        |
| unpickle                   | 13.3 us                                                      | 15.1 us: 1.14x slower                                                        |
| genshi_text                | 25.5 ms                                                      | 29.2 ms: 1.15x slower                                                        |
| pyflate                    | 449 ms                                                       | 523 ms: 1.16x slower                                                         |
| async_generators           | 322 ms                                                       | 383 ms: 1.19x slower                                                         |
| telco                      | 6.81 ms                                                      | 8.14 ms: 1.19x slower                                                        |
| coverage                   | 66.1 ms                                                      | 84.1 ms: 1.27x slower                                                        |
| python_startup             | 10.7 ms                                                      | 14.2 ms: 1.32x slower                                                        |
| scimark_sor                | 110 ms                                                       | 152 ms: 1.39x slower                                                         |
| unpack_sequence            | 45.7 ns                                                      | 73.6 ns: 1.61x slower                                                        |
| python_startup_no_site     | 7.73 ms                                                      | 12.5 ms: 1.61x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.04x faster                                                                 |

Benchmark hidden because not significant (5): tornado_http, spectral_norm, unpickle_list, asyncio_websockets, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 78.75% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.16x