# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_plt
- machine: linux-x86_64
- commit hash: 9242976
- commit date: 2024-03-15
- overall geometric mean: 1.01x faster
- HPT reliability: 64.34%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 308 ms: 1.08x slower                                                     |
| chameleon      | 7.92 ms                                                      | 7.33 ms: 1.08x faster                                                    |
| docutils       | 2.85 sec                                                     | 2.96 sec: 1.04x slower                                                   |
| html5lib       | 72.2 ms                                                      | 74.7 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                        | 1.01x slower                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 518 ms                                                       | 438 ms: 1.18x faster                                                     |
| async_tree_memoization     | 629 ms                                                       | 550 ms: 1.14x faster                                                     |
| async_tree_none_tg         | 474 ms                                                       | 435 ms: 1.09x faster                                                     |
| async_tree_memoization_tg  | 600 ms                                                       | 557 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 701 ms: 1.07x faster                                                     |
| async_tree_io              | 1.17 sec                                                     | 1.09 sec: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 705 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 1.15 sec                                                     | 1.09 sec: 1.06x faster                                                   |
| Geometric mean             | (ref)                                                        | 1.09x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 262 ms: 1.04x slower                                                     |
| float          | 74.9 ms                                                      | 79.2 ms: 1.06x slower                                                    |
| nbody          | 92.9 ms                                                      | 103 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                        | 1.07x slower                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 152 ms: 1.03x faster                                                     |
| regex_dna      | 227 ms                                                       | 236 ms: 1.04x slower                                                     |
| regex_effbot   | 3.34 ms                                                      | 3.54 ms: 1.06x slower                                                    |
| regex_v8       | 24.4 ms                                                      | 25.9 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                        | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                    |
| json_loads           | 28.9 us                                                      | 25.0 us: 1.16x faster                                                    |
| xml_etree_parse      | 155 ms                                                       | 145 ms: 1.06x faster                                                     |
| xml_etree_iterparse  | 107 ms                                                       | 104 ms: 1.02x faster                                                     |
| unpickle_list        | 4.60 us                                                      | 4.57 us: 1.01x faster                                                    |
| pickle_dict          | 32.3 us                                                      | 32.5 us: 1.01x slower                                                    |
| unpickle_pure_python | 238 us                                                       | 241 us: 1.01x slower                                                     |
| tomli_loads          | 2.25 sec                                                     | 2.34 sec: 1.04x slower                                                   |
| xml_etree_process    | 55.9 ms                                                      | 58.9 ms: 1.05x slower                                                    |
| xml_etree_generate   | 79.7 ms                                                      | 85.5 ms: 1.07x slower                                                    |
| pickle               | 9.89 us                                                      | 10.7 us: 1.08x slower                                                    |
| pickle_list          | 3.94 us                                                      | 4.45 us: 1.13x slower                                                    |
| unpickle             | 13.3 us                                                      | 15.2 us: 1.14x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.00x slower                                                             |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 14.2 ms: 1.32x slower                                                    |
| python_startup_no_site | 7.73 ms                                                      | 12.6 ms: 1.63x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                    |
| django_template | 39.3 ms                                                      | 38.4 ms: 1.02x faster                                                    |
| genshi_xml      | 57.1 ms                                                      | 61.9 ms: 1.09x slower                                                    |
| genshi_text     | 25.5 ms                                                      | 28.5 ms: 1.12x slower                                                    |
| Geometric mean  | (ref)                                                        | 1.03x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240315-pythonperf2-x86_64-brandtbucher-justin_plt-3.13.0a5+-9242976 |
|----------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 120 us: 4.45x faster                                                     |
| asyncio_tcp                | 747 ms                                                       | 373 ms: 2.00x faster                                                     |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.94x faster                                                   |
| generators                 | 54.6 ms                                                      | 34.2 ms: 1.60x faster                                                    |
| pylint                     | 514 ms                                                       | 362 ms: 1.42x faster                                                     |
| comprehensions             | 25.1 us                                                      | 19.3 us: 1.30x faster                                                    |
| json_dumps                 | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                    |
| coroutines                 | 27.8 ms                                                      | 22.8 ms: 1.22x faster                                                    |
| async_tree_none            | 518 ms                                                       | 438 ms: 1.18x faster                                                     |
| json_loads                 | 28.9 us                                                      | 25.0 us: 1.16x faster                                                    |
| sympy_sum                  | 186 ms                                                       | 162 ms: 1.14x faster                                                     |
| async_tree_memoization     | 629 ms                                                       | 550 ms: 1.14x faster                                                     |
| sympy_str                  | 337 ms                                                       | 305 ms: 1.11x faster                                                     |
| richards_super             | 63.6 ms                                                      | 57.6 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 474 ms                                                       | 435 ms: 1.09x faster                                                     |
| logging_simple             | 7.24 us                                                      | 6.66 us: 1.09x faster                                                    |
| thrift                     | 931 us                                                       | 857 us: 1.09x faster                                                     |
| chameleon                  | 7.92 ms                                                      | 7.33 ms: 1.08x faster                                                    |
| async_tree_memoization_tg  | 600 ms                                                       | 557 ms: 1.08x faster                                                     |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 701 ms: 1.07x faster                                                     |
| async_tree_io              | 1.17 sec                                                     | 1.09 sec: 1.07x faster                                                   |
| chaos                      | 74.9 ms                                                      | 69.9 ms: 1.07x faster                                                    |
| mako                       | 11.0 ms                                                      | 10.3 ms: 1.07x faster                                                    |
| sympy_expand               | 553 ms                                                       | 517 ms: 1.07x faster                                                     |
| xml_etree_parse            | 155 ms                                                       | 145 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 705 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 1.15 sec                                                     | 1.09 sec: 1.06x faster                                                   |
| mdp                        | 2.77 sec                                                     | 2.61 sec: 1.06x faster                                                   |
| deltablue                  | 3.97 ms                                                      | 3.74 ms: 1.06x faster                                                    |
| logging_format             | 7.71 us                                                      | 7.28 us: 1.06x faster                                                    |
| gc_traversal               | 4.15 ms                                                      | 3.92 ms: 1.06x faster                                                    |
| crypto_pyaes               | 83.3 ms                                                      | 79.1 ms: 1.05x faster                                                    |
| sqlglot_parse              | 1.51 ms                                                      | 1.44 ms: 1.05x faster                                                    |
| json                       | 5.58 ms                                                      | 5.37 ms: 1.04x faster                                                    |
| deepcopy                   | 391 us                                                       | 378 us: 1.04x faster                                                     |
| logging_silent             | 100 ns                                                       | 97.5 ns: 1.03x faster                                                    |
| deepcopy_reduce            | 3.40 us                                                      | 3.30 us: 1.03x faster                                                    |
| regex_compile              | 156 ms                                                       | 152 ms: 1.03x faster                                                     |
| sympy_integrate            | 25.8 ms                                                      | 25.1 ms: 1.03x faster                                                    |
| xml_etree_iterparse        | 107 ms                                                       | 104 ms: 1.02x faster                                                     |
| django_template            | 39.3 ms                                                      | 38.4 ms: 1.02x faster                                                    |
| bench_thread_pool          | 1.00 ms                                                      | 979 us: 1.02x faster                                                     |
| sqlglot_transpile          | 1.91 ms                                                      | 1.88 ms: 1.02x faster                                                    |
| sqlglot_normalize          | 122 ms                                                       | 120 ms: 1.01x faster                                                     |
| raytrace                   | 309 ms                                                       | 306 ms: 1.01x faster                                                     |
| dask                       | 410 ms                                                       | 405 ms: 1.01x faster                                                     |
| asyncio_websockets         | 390 ms                                                       | 386 ms: 1.01x faster                                                     |
| unpickle_list              | 4.60 us                                                      | 4.57 us: 1.01x faster                                                    |
| pickle_dict                | 32.3 us                                                      | 32.5 us: 1.01x slower                                                    |
| unpickle_pure_python       | 238 us                                                       | 241 us: 1.01x slower                                                     |
| create_gc_cycles           | 1.58 ms                                                      | 1.60 ms: 1.02x slower                                                    |
| meteor_contest             | 131 ms                                                       | 133 ms: 1.02x slower                                                     |
| dulwich_log                | 67.4 ms                                                      | 68.8 ms: 1.02x slower                                                    |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.03x slower                                                    |
| html5lib                   | 72.2 ms                                                      | 74.7 ms: 1.03x slower                                                    |
| nqueens                    | 103 ms                                                       | 106 ms: 1.04x slower                                                     |
| richards                   | 49.7 ms                                                      | 51.5 ms: 1.04x slower                                                    |
| docutils                   | 2.85 sec                                                     | 2.96 sec: 1.04x slower                                                   |
| regex_dna                  | 227 ms                                                       | 236 ms: 1.04x slower                                                     |
| tomli_loads                | 2.25 sec                                                     | 2.34 sec: 1.04x slower                                                   |
| pycparser                  | 1.31 sec                                                     | 1.37 sec: 1.04x slower                                                   |
| pidigits                   | 251 ms                                                       | 262 ms: 1.04x slower                                                     |
| xml_etree_process          | 55.9 ms                                                      | 58.9 ms: 1.05x slower                                                    |
| float                      | 74.9 ms                                                      | 79.2 ms: 1.06x slower                                                    |
| spectral_norm              | 95.1 ms                                                      | 101 ms: 1.06x slower                                                     |
| regex_effbot               | 3.34 ms                                                      | 3.54 ms: 1.06x slower                                                    |
| regex_v8                   | 24.4 ms                                                      | 25.9 ms: 1.06x slower                                                    |
| xml_etree_generate         | 79.7 ms                                                      | 85.5 ms: 1.07x slower                                                    |
| 2to3                       | 287 ms                                                       | 308 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 59.0 ms                                                      | 63.4 ms: 1.08x slower                                                    |
| pickle                     | 9.89 us                                                      | 10.7 us: 1.08x slower                                                    |
| fannkuch                   | 416 ms                                                       | 448 ms: 1.08x slower                                                     |
| pprint_pformat             | 1.67 sec                                                     | 1.80 sec: 1.08x slower                                                   |
| sqlite_synth               | 2.52 us                                                      | 2.73 us: 1.08x slower                                                    |
| genshi_xml                 | 57.1 ms                                                      | 61.9 ms: 1.09x slower                                                    |
| pprint_safe_repr           | 805 ms                                                       | 883 ms: 1.10x slower                                                     |
| hexiom                     | 6.98 ms                                                      | 7.68 ms: 1.10x slower                                                    |
| go                         | 158 ms                                                       | 175 ms: 1.11x slower                                                     |
| nbody                      | 92.9 ms                                                      | 103 ms: 1.11x slower                                                     |
| genshi_text                | 25.5 ms                                                      | 28.5 ms: 1.12x slower                                                    |
| gunicorn                   | 966 us                                                       | 1.08 ms: 1.12x slower                                                    |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.56 ms: 1.12x slower                                                    |
| pickle_list                | 3.94 us                                                      | 4.45 us: 1.13x slower                                                    |
| aiohttp                    | 986 us                                                       | 1.11 ms: 1.13x slower                                                    |
| unpickle                   | 13.3 us                                                      | 15.2 us: 1.14x slower                                                    |
| scimark_monte_carlo        | 69.8 ms                                                      | 81.4 ms: 1.17x slower                                                    |
| scimark_lu                 | 114 ms                                                       | 134 ms: 1.18x slower                                                     |
| pyflate                    | 449 ms                                                       | 536 ms: 1.19x slower                                                     |
| mypy2                      | 762 ms                                                       | 922 ms: 1.21x slower                                                     |
| coverage                   | 66.1 ms                                                      | 80.0 ms: 1.21x slower                                                    |
| telco                      | 6.81 ms                                                      | 8.30 ms: 1.22x slower                                                    |
| async_generators           | 322 ms                                                       | 395 ms: 1.23x slower                                                     |
| scimark_fft                | 281 ms                                                       | 353 ms: 1.26x slower                                                     |
| python_startup             | 10.7 ms                                                      | 14.2 ms: 1.32x slower                                                    |
| scimark_sor                | 110 ms                                                       | 156 ms: 1.42x slower                                                     |
| python_startup_no_site     | 7.73 ms                                                      | 12.6 ms: 1.63x slower                                                    |
| unpack_sequence            | 45.7 ns                                                      | 80.1 ns: 1.75x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.01x faster                                                             |

Benchmark hidden because not significant (4): deepcopy_memo, pickle_pure_python, tornado_http, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 64.34% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.14x