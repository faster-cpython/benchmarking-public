# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.08x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 291 ms: 1.01x slower                                                         |
| chameleon      | 7.92 ms                                                      | 7.36 ms: 1.08x faster                                                        |
| docutils       | 2.85 sec                                                     | 2.96 sec: 1.04x slower                                                       |
| html5lib       | 72.2 ms                                                      | 75.5 ms: 1.05x slower                                                        |
| tornado_http   | 124 ms                                                       | 121 ms: 1.03x faster                                                         |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 629 ms                                                       | 438 ms: 1.44x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 431 ms: 1.39x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 343 ms: 1.38x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 851 ms: 1.38x faster                                                         |
| async_tree_none            | 518 ms                                                       | 379 ms: 1.36x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 859 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 586 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 601 ms: 1.25x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                      | 86.8 ms: 1.07x faster                                                        |
| pidigits       | 251 ms                                                       | 262 ms: 1.04x slower                                                         |
| float          | 74.9 ms                                                      | 78.2 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 144 ms: 1.09x faster                                                         |
| regex_dna      | 227 ms                                                       | 233 ms: 1.02x slower                                                         |
| regex_v8       | 24.4 ms                                                      | 25.6 ms: 1.05x slower                                                        |
| regex_effbot   | 3.34 ms                                                      | 3.70 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                        | 1.02x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.5 ms: 1.26x faster                                                        |
| json_loads           | 28.9 us                                                      | 25.2 us: 1.15x faster                                                        |
| unpickle_pure_python | 238 us                                                       | 223 us: 1.07x faster                                                         |
| pickle_dict          | 32.3 us                                                      | 30.9 us: 1.05x faster                                                        |
| xml_etree_parse      | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| pickle_pure_python   | 316 us                                                       | 307 us: 1.03x faster                                                         |
| unpickle_list        | 4.60 us                                                      | 4.47 us: 1.03x faster                                                        |
| tomli_loads          | 2.25 sec                                                     | 2.21 sec: 1.02x faster                                                       |
| xml_etree_iterparse  | 107 ms                                                       | 105 ms: 1.02x faster                                                         |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| xml_etree_generate   | 79.7 ms                                                      | 82.0 ms: 1.03x slower                                                        |
| xml_etree_process    | 55.9 ms                                                      | 57.8 ms: 1.03x slower                                                        |
| unpickle             | 13.3 us                                                      | 14.6 us: 1.10x slower                                                        |
| pickle_list          | 3.94 us                                                      | 4.37 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 12.7 ms: 1.18x slower                                                        |
| python_startup_no_site | 7.73 ms                                                      | 11.0 ms: 1.42x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| genshi_xml      | 57.1 ms                                                      | 54.0 ms: 1.06x faster                                                        |
| genshi_text     | 25.5 ms                                                      | 25.2 ms: 1.01x faster                                                        |
| django_template | 39.3 ms                                                      | 40.9 ms: 1.04x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.03x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 113 us: 4.72x faster                                                         |
| asyncio_tcp                | 747 ms                                                       | 371 ms: 2.01x faster                                                         |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.94x faster                                                       |
| generators                 | 54.6 ms                                                      | 33.5 ms: 1.63x faster                                                        |
| comprehensions             | 25.1 us                                                      | 16.7 us: 1.50x faster                                                        |
| pylint                     | 514 ms                                                       | 347 ms: 1.48x faster                                                         |
| async_tree_memoization     | 629 ms                                                       | 438 ms: 1.44x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 431 ms: 1.39x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 343 ms: 1.38x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 851 ms: 1.38x faster                                                         |
| async_tree_none            | 518 ms                                                       | 379 ms: 1.36x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 859 ms: 1.34x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 586 ms: 1.28x faster                                                         |
| json_dumps                 | 13.3 ms                                                      | 10.5 ms: 1.26x faster                                                        |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 601 ms: 1.25x faster                                                         |
| chaos                      | 74.9 ms                                                      | 60.9 ms: 1.23x faster                                                        |
| coroutines                 | 27.8 ms                                                      | 22.7 ms: 1.23x faster                                                        |
| sympy_sum                  | 186 ms                                                       | 152 ms: 1.22x faster                                                         |
| scimark_lu                 | 114 ms                                                       | 94.4 ms: 1.21x faster                                                        |
| nqueens                    | 103 ms                                                       | 87.5 ms: 1.17x faster                                                        |
| crypto_pyaes               | 83.3 ms                                                      | 71.2 ms: 1.17x faster                                                        |
| raytrace                   | 309 ms                                                       | 265 ms: 1.17x faster                                                         |
| sympy_str                  | 337 ms                                                       | 290 ms: 1.16x faster                                                         |
| json_loads                 | 28.9 us                                                      | 25.2 us: 1.15x faster                                                        |
| deltablue                  | 3.97 ms                                                      | 3.52 ms: 1.13x faster                                                        |
| sympy_integrate            | 25.8 ms                                                      | 23.1 ms: 1.12x faster                                                        |
| sympy_expand               | 553 ms                                                       | 496 ms: 1.12x faster                                                         |
| mdp                        | 2.77 sec                                                     | 2.49 sec: 1.11x faster                                                       |
| bench_thread_pool          | 1.00 ms                                                      | 902 us: 1.11x faster                                                         |
| logging_simple             | 7.24 us                                                      | 6.58 us: 1.10x faster                                                        |
| sqlglot_parse              | 1.51 ms                                                      | 1.38 ms: 1.10x faster                                                        |
| hexiom                     | 6.98 ms                                                      | 6.35 ms: 1.10x faster                                                        |
| regex_compile              | 156 ms                                                       | 144 ms: 1.09x faster                                                         |
| sqlglot_transpile          | 1.91 ms                                                      | 1.76 ms: 1.08x faster                                                        |
| mako                       | 11.0 ms                                                      | 10.2 ms: 1.08x faster                                                        |
| fannkuch                   | 416 ms                                                       | 385 ms: 1.08x faster                                                         |
| chameleon                  | 7.92 ms                                                      | 7.36 ms: 1.08x faster                                                        |
| thrift                     | 931 us                                                       | 868 us: 1.07x faster                                                         |
| nbody                      | 92.9 ms                                                      | 86.8 ms: 1.07x faster                                                        |
| unpickle_pure_python       | 238 us                                                       | 223 us: 1.07x faster                                                         |
| deepcopy                   | 391 us                                                       | 368 us: 1.06x faster                                                         |
| scimark_monte_carlo        | 69.8 ms                                                      | 66.0 ms: 1.06x faster                                                        |
| genshi_xml                 | 57.1 ms                                                      | 54.0 ms: 1.06x faster                                                        |
| richards_super             | 63.6 ms                                                      | 60.4 ms: 1.05x faster                                                        |
| logging_format             | 7.71 us                                                      | 7.35 us: 1.05x faster                                                        |
| pickle_dict                | 32.3 us                                                      | 30.9 us: 1.05x faster                                                        |
| dask                       | 410 ms                                                       | 392 ms: 1.04x faster                                                         |
| pycparser                  | 1.31 sec                                                     | 1.26 sec: 1.04x faster                                                       |
| logging_silent             | 100 ns                                                       | 96.2 ns: 1.04x faster                                                        |
| create_gc_cycles           | 1.58 ms                                                      | 1.52 ms: 1.04x faster                                                        |
| deepcopy_memo              | 37.5 us                                                      | 36.3 us: 1.03x faster                                                        |
| sqlglot_normalize          | 122 ms                                                       | 118 ms: 1.03x faster                                                         |
| json                       | 5.58 ms                                                      | 5.40 ms: 1.03x faster                                                        |
| xml_etree_parse            | 155 ms                                                       | 150 ms: 1.03x faster                                                         |
| pprint_pformat             | 1.67 sec                                                     | 1.61 sec: 1.03x faster                                                       |
| spectral_norm              | 95.1 ms                                                      | 92.2 ms: 1.03x faster                                                        |
| pickle_pure_python         | 316 us                                                       | 307 us: 1.03x faster                                                         |
| unpickle_list              | 4.60 us                                                      | 4.47 us: 1.03x faster                                                        |
| tornado_http               | 124 ms                                                       | 121 ms: 1.03x faster                                                         |
| deepcopy_reduce            | 3.40 us                                                      | 3.30 us: 1.03x faster                                                        |
| pprint_safe_repr           | 805 ms                                                       | 789 ms: 1.02x faster                                                         |
| tomli_loads                | 2.25 sec                                                     | 2.21 sec: 1.02x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                       | 105 ms: 1.02x faster                                                         |
| meteor_contest             | 131 ms                                                       | 129 ms: 1.01x faster                                                         |
| asyncio_websockets         | 390 ms                                                       | 385 ms: 1.01x faster                                                         |
| genshi_text                | 25.5 ms                                                      | 25.2 ms: 1.01x faster                                                        |
| sqlglot_optimize           | 59.0 ms                                                      | 59.2 ms: 1.00x slower                                                        |
| dulwich_log                | 67.4 ms                                                      | 68.0 ms: 1.01x slower                                                        |
| pathlib                    | 18.9 ms                                                      | 19.1 ms: 1.01x slower                                                        |
| mypy2                      | 762 ms                                                       | 771 ms: 1.01x slower                                                         |
| 2to3                       | 287 ms                                                       | 291 ms: 1.01x slower                                                         |
| regex_dna                  | 227 ms                                                       | 233 ms: 1.02x slower                                                         |
| pickle                     | 9.89 us                                                      | 10.2 us: 1.03x slower                                                        |
| xml_etree_generate         | 79.7 ms                                                      | 82.0 ms: 1.03x slower                                                        |
| xml_etree_process          | 55.9 ms                                                      | 57.8 ms: 1.03x slower                                                        |
| gc_traversal               | 4.15 ms                                                      | 4.30 ms: 1.04x slower                                                        |
| docutils                   | 2.85 sec                                                     | 2.96 sec: 1.04x slower                                                       |
| django_template            | 39.3 ms                                                      | 40.9 ms: 1.04x slower                                                        |
| pidigits                   | 251 ms                                                       | 262 ms: 1.04x slower                                                         |
| float                      | 74.9 ms                                                      | 78.2 ms: 1.04x slower                                                        |
| html5lib                   | 72.2 ms                                                      | 75.5 ms: 1.05x slower                                                        |
| regex_v8                   | 24.4 ms                                                      | 25.6 ms: 1.05x slower                                                        |
| scimark_fft                | 281 ms                                                       | 296 ms: 1.06x slower                                                         |
| unpack_sequence            | 45.7 ns                                                      | 48.2 ns: 1.06x slower                                                        |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.32 ms: 1.06x slower                                                        |
| gunicorn                   | 966 us                                                       | 1.04 ms: 1.07x slower                                                        |
| aiohttp                    | 986 us                                                       | 1.07 ms: 1.08x slower                                                        |
| sqlite_synth               | 2.52 us                                                      | 2.74 us: 1.09x slower                                                        |
| richards                   | 49.7 ms                                                      | 54.4 ms: 1.09x slower                                                        |
| go                         | 158 ms                                                       | 173 ms: 1.10x slower                                                         |
| async_generators           | 322 ms                                                       | 354 ms: 1.10x slower                                                         |
| unpickle                   | 13.3 us                                                      | 14.6 us: 1.10x slower                                                        |
| regex_effbot               | 3.34 ms                                                      | 3.70 ms: 1.11x slower                                                        |
| pickle_list                | 3.94 us                                                      | 4.37 us: 1.11x slower                                                        |
| telco                      | 6.81 ms                                                      | 7.91 ms: 1.16x slower                                                        |
| pyflate                    | 449 ms                                                       | 525 ms: 1.17x slower                                                         |
| python_startup             | 10.7 ms                                                      | 12.7 ms: 1.18x slower                                                        |
| coverage                   | 66.1 ms                                                      | 79.9 ms: 1.21x slower                                                        |
| scimark_sor                | 110 ms                                                       | 140 ms: 1.27x slower                                                         |
| python_startup_no_site     | 7.73 ms                                                      | 11.0 ms: 1.42x slower                                                        |
| Geometric mean             | (ref)                                                        | 1.08x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.01x