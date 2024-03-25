# Results vs. 3.11.0

- fork: python
- ref: d610d821fd210dce63a1
- machine: linux-x86_64
- commit hash: d610d82
- commit date: 2024-03-23
- overall geometric mean: 1.04x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 320 ms: 1.12x slower                                                         |
| chameleon      | 7.92 ms                                                      | 7.82 ms: 1.01x faster                                                        |
| docutils       | 2.85 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| html5lib       | 72.2 ms                                                      | 77.2 ms: 1.07x slower                                                        |
| tornado_http   | 124 ms                                                       | 127 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization     | 629 ms                                                       | 453 ms: 1.39x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 448 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 356 ms: 1.33x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 886 ms: 1.32x faster                                                         |
| async_tree_none            | 518 ms                                                       | 395 ms: 1.31x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 888 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 600 ms: 1.25x faster                                                         |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 617 ms: 1.22x faster                                                         |
| Geometric mean             | (ref)                                                        | 1.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 265 ms: 1.05x slower                                                         |
| float          | 74.9 ms                                                      | 101 ms: 1.35x slower                                                         |
| nbody          | 92.9 ms                                                      | 130 ms: 1.40x slower                                                         |
| Geometric mean | (ref)                                                        | 1.26x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                      | 25.8 ms: 1.06x slower                                                        |
| regex_dna      | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| regex_effbot   | 3.34 ms                                                      | 3.61 ms: 1.08x slower                                                        |
| regex_compile  | 156 ms                                                       | 204 ms: 1.31x slower                                                         |
| Geometric mean | (ref)                                                        | 1.12x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.7 ms: 1.24x faster                                                        |
| json_loads           | 28.9 us                                                      | 25.2 us: 1.15x faster                                                        |
| xml_etree_parse      | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| pickle_dict          | 32.3 us                                                      | 31.2 us: 1.03x faster                                                        |
| unpickle_list        | 4.60 us                                                      | 4.67 us: 1.02x slower                                                        |
| pickle               | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 107 ms                                                       | 115 ms: 1.08x slower                                                         |
| xml_etree_process    | 55.9 ms                                                      | 62.4 ms: 1.12x slower                                                        |
| pickle_list          | 3.94 us                                                      | 4.41 us: 1.12x slower                                                        |
| xml_etree_generate   | 79.7 ms                                                      | 90.3 ms: 1.13x slower                                                        |
| unpickle             | 13.3 us                                                      | 15.1 us: 1.14x slower                                                        |
| unpickle_pure_python | 238 us                                                       | 303 us: 1.27x slower                                                         |
| tomli_loads          | 2.25 sec                                                     | 2.90 sec: 1.29x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.05x slower                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 12.8 ms: 1.20x slower                                                        |
| python_startup_no_site | 7.73 ms                                                      | 11.1 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 39.3 ms                                                      | 42.2 ms: 1.07x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 62.1 ms: 1.09x slower                                                        |
| genshi_text     | 25.5 ms                                                      | 29.6 ms: 1.16x slower                                                        |
| mako            | 11.0 ms                                                      | 14.5 ms: 1.32x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.16x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240323-pythonperf2-x86_64-python-d610d821fd210dce63a1-3.13.0a5+-d610d82 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 129 us: 4.14x faster                                                         |
| asyncio_tcp                | 747 ms                                                       | 373 ms: 2.00x faster                                                         |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.59 sec: 1.92x faster                                                       |
| generators                 | 54.6 ms                                                      | 33.6 ms: 1.63x faster                                                        |
| pylint                     | 514 ms                                                       | 369 ms: 1.39x faster                                                         |
| async_tree_memoization     | 629 ms                                                       | 453 ms: 1.39x faster                                                         |
| async_tree_memoization_tg  | 600 ms                                                       | 448 ms: 1.34x faster                                                         |
| async_tree_none_tg         | 474 ms                                                       | 356 ms: 1.33x faster                                                         |
| async_tree_io              | 1.17 sec                                                     | 886 ms: 1.32x faster                                                         |
| async_tree_none            | 518 ms                                                       | 395 ms: 1.31x faster                                                         |
| async_tree_io_tg           | 1.15 sec                                                     | 888 ms: 1.30x faster                                                         |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 600 ms: 1.25x faster                                                         |
| json_dumps                 | 13.3 ms                                                      | 10.7 ms: 1.24x faster                                                        |
| coroutines                 | 27.8 ms                                                      | 22.5 ms: 1.24x faster                                                        |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 617 ms: 1.22x faster                                                         |
| json_loads                 | 28.9 us                                                      | 25.2 us: 1.15x faster                                                        |
| thrift                     | 931 us                                                       | 864 us: 1.08x faster                                                         |
| logging_simple             | 7.24 us                                                      | 6.76 us: 1.07x faster                                                        |
| xml_etree_parse            | 155 ms                                                       | 146 ms: 1.06x faster                                                         |
| sympy_sum                  | 186 ms                                                       | 176 ms: 1.05x faster                                                         |
| json                       | 5.58 ms                                                      | 5.31 ms: 1.05x faster                                                        |
| mdp                        | 2.77 sec                                                     | 2.66 sec: 1.04x faster                                                       |
| logging_format             | 7.71 us                                                      | 7.39 us: 1.04x faster                                                        |
| bench_thread_pool          | 1.00 ms                                                      | 962 us: 1.04x faster                                                         |
| pickle_dict                | 32.3 us                                                      | 31.2 us: 1.03x faster                                                        |
| chameleon                  | 7.92 ms                                                      | 7.82 ms: 1.01x faster                                                        |
| deepcopy_reduce            | 3.40 us                                                      | 3.42 us: 1.01x slower                                                        |
| sympy_str                  | 337 ms                                                       | 340 ms: 1.01x slower                                                         |
| logging_silent             | 100 ns                                                       | 101 ns: 1.01x slower                                                         |
| sympy_integrate            | 25.8 ms                                                      | 26.1 ms: 1.01x slower                                                        |
| deepcopy                   | 391 us                                                       | 396 us: 1.01x slower                                                         |
| unpickle_list              | 4.60 us                                                      | 4.67 us: 1.02x slower                                                        |
| richards_super             | 63.6 ms                                                      | 64.8 ms: 1.02x slower                                                        |
| tornado_http               | 124 ms                                                       | 127 ms: 1.02x slower                                                         |
| sqlglot_transpile          | 1.91 ms                                                      | 1.96 ms: 1.02x slower                                                        |
| sqlglot_parse              | 1.51 ms                                                      | 1.55 ms: 1.03x slower                                                        |
| sympy_expand               | 553 ms                                                       | 568 ms: 1.03x slower                                                         |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.04x slower                                                        |
| pycparser                  | 1.31 sec                                                     | 1.36 sec: 1.04x slower                                                       |
| chaos                      | 74.9 ms                                                      | 77.9 ms: 1.04x slower                                                        |
| comprehensions             | 25.1 us                                                      | 26.1 us: 1.04x slower                                                        |
| pickle                     | 9.89 us                                                      | 10.3 us: 1.04x slower                                                        |
| sqlglot_normalize          | 122 ms                                                       | 128 ms: 1.05x slower                                                         |
| pidigits                   | 251 ms                                                       | 265 ms: 1.05x slower                                                         |
| regex_v8                   | 24.4 ms                                                      | 25.8 ms: 1.06x slower                                                        |
| regex_dna                  | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| html5lib                   | 72.2 ms                                                      | 77.2 ms: 1.07x slower                                                        |
| django_template            | 39.3 ms                                                      | 42.2 ms: 1.07x slower                                                        |
| xml_etree_iterparse        | 107 ms                                                       | 115 ms: 1.08x slower                                                         |
| regex_effbot               | 3.34 ms                                                      | 3.61 ms: 1.08x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 62.1 ms: 1.09x slower                                                        |
| meteor_contest             | 131 ms                                                       | 143 ms: 1.09x slower                                                         |
| gc_traversal               | 4.15 ms                                                      | 4.59 ms: 1.11x slower                                                        |
| crypto_pyaes               | 83.3 ms                                                      | 92.2 ms: 1.11x slower                                                        |
| mypy2                      | 762 ms                                                       | 844 ms: 1.11x slower                                                         |
| sqlite_synth               | 2.52 us                                                      | 2.81 us: 1.11x slower                                                        |
| xml_etree_process          | 55.9 ms                                                      | 62.4 ms: 1.12x slower                                                        |
| 2to3                       | 287 ms                                                       | 320 ms: 1.12x slower                                                         |
| pickle_list                | 3.94 us                                                      | 4.41 us: 1.12x slower                                                        |
| docutils                   | 2.85 sec                                                     | 3.20 sec: 1.12x slower                                                       |
| sqlglot_optimize           | 59.0 ms                                                      | 66.3 ms: 1.12x slower                                                        |
| dulwich_log                | 67.4 ms                                                      | 75.8 ms: 1.12x slower                                                        |
| gunicorn                   | 966 us                                                       | 1.09 ms: 1.13x slower                                                        |
| deepcopy_memo              | 37.5 us                                                      | 42.5 us: 1.13x slower                                                        |
| xml_etree_generate         | 79.7 ms                                                      | 90.3 ms: 1.13x slower                                                        |
| unpickle                   | 13.3 us                                                      | 15.1 us: 1.14x slower                                                        |
| aiohttp                    | 986 us                                                       | 1.12 ms: 1.14x slower                                                        |
| raytrace                   | 309 ms                                                       | 355 ms: 1.15x slower                                                         |
| genshi_text                | 25.5 ms                                                      | 29.6 ms: 1.16x slower                                                        |
| nqueens                    | 103 ms                                                       | 120 ms: 1.17x slower                                                         |
| richards                   | 49.7 ms                                                      | 58.3 ms: 1.17x slower                                                        |
| python_startup             | 10.7 ms                                                      | 12.8 ms: 1.20x slower                                                        |
| scimark_lu                 | 114 ms                                                       | 137 ms: 1.20x slower                                                         |
| pprint_pformat             | 1.67 sec                                                     | 2.01 sec: 1.21x slower                                                       |
| async_generators           | 322 ms                                                       | 390 ms: 1.21x slower                                                         |
| coverage                   | 66.1 ms                                                      | 80.5 ms: 1.22x slower                                                        |
| pprint_safe_repr           | 805 ms                                                       | 980 ms: 1.22x slower                                                         |
| telco                      | 6.81 ms                                                      | 8.49 ms: 1.25x slower                                                        |
| go                         | 158 ms                                                       | 199 ms: 1.26x slower                                                         |
| unpickle_pure_python       | 238 us                                                       | 303 us: 1.27x slower                                                         |
| fannkuch                   | 416 ms                                                       | 532 ms: 1.28x slower                                                         |
| tomli_loads                | 2.25 sec                                                     | 2.90 sec: 1.29x slower                                                       |
| regex_compile              | 156 ms                                                       | 204 ms: 1.31x slower                                                         |
| mako                       | 11.0 ms                                                      | 14.5 ms: 1.32x slower                                                        |
| float                      | 74.9 ms                                                      | 101 ms: 1.35x slower                                                         |
| nbody                      | 92.9 ms                                                      | 130 ms: 1.40x slower                                                         |
| python_startup_no_site     | 7.73 ms                                                      | 11.1 ms: 1.43x slower                                                        |
| scimark_monte_carlo        | 69.8 ms                                                      | 102 ms: 1.46x slower                                                         |
| pyflate                    | 449 ms                                                       | 655 ms: 1.46x slower                                                         |
| scimark_sor                | 110 ms                                                       | 162 ms: 1.48x slower                                                         |
| hexiom                     | 6.98 ms                                                      | 10.4 ms: 1.49x slower                                                        |
| unpack_sequence            | 45.7 ns                                                      | 68.7 ns: 1.50x slower                                                        |
| scimark_fft                | 281 ms                                                       | 444 ms: 1.58x slower                                                         |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 6.61 ms: 1.63x slower                                                        |
| spectral_norm              | 95.1 ms                                                      | 160 ms: 1.69x slower                                                         |
| Geometric mean             | (ref)                                                        | 1.04x slower                                                                 |

Benchmark hidden because not significant (6): pickle_pure_python, dask, deltablue, asyncio_websockets, create_gc_cycles, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.02x