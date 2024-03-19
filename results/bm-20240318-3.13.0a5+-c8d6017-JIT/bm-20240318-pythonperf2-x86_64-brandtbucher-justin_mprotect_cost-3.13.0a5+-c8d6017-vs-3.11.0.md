# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.03x faster
- HPT reliability: 83.24%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.25x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 304 ms: 1.06x slower                                                               |
| chameleon      | 7.92 ms                                                      | 7.30 ms: 1.09x faster                                                              |
| docutils       | 2.85 sec                                                     | 2.93 sec: 1.03x slower                                                             |
| html5lib       | 72.2 ms                                                      | 73.8 ms: 1.02x slower                                                              |
| tornado_http   | 124 ms                                                       | 128 ms: 1.03x slower                                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none            | 518 ms                                                       | 436 ms: 1.19x faster                                                               |
| async_tree_memoization     | 629 ms                                                       | 548 ms: 1.15x faster                                                               |
| async_tree_none_tg         | 474 ms                                                       | 433 ms: 1.10x faster                                                               |
| async_tree_memoization_tg  | 600 ms                                                       | 553 ms: 1.09x faster                                                               |
| async_tree_io              | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                                             |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 702 ms: 1.07x faster                                                               |
| async_tree_io_tg           | 1.15 sec                                                     | 1.08 sec: 1.07x faster                                                             |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 705 ms: 1.06x faster                                                               |
| Geometric mean             | (ref)                                                        | 1.10x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| nbody          | 92.9 ms                                                      | 95.5 ms: 1.03x slower                                                              |
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                               |
| float          | 74.9 ms                                                      | 78.6 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                        | 1.04x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 146 ms: 1.07x faster                                                               |
| regex_v8       | 24.4 ms                                                      | 25.7 ms: 1.05x slower                                                              |
| regex_effbot   | 3.34 ms                                                      | 3.67 ms: 1.10x slower                                                              |
| regex_dna      | 227 ms                                                       | 252 ms: 1.11x slower                                                               |
| Geometric mean | (ref)                                                        | 1.05x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                              |
| json_loads           | 28.9 us                                                      | 24.6 us: 1.18x faster                                                              |
| xml_etree_parse      | 155 ms                                                       | 143 ms: 1.08x faster                                                               |
| pickle_dict          | 32.3 us                                                      | 30.4 us: 1.06x faster                                                              |
| xml_etree_iterparse  | 107 ms                                                       | 102 ms: 1.05x faster                                                               |
| tomli_loads          | 2.25 sec                                                     | 2.18 sec: 1.03x faster                                                             |
| unpickle_pure_python | 238 us                                                       | 232 us: 1.03x faster                                                               |
| pickle_pure_python   | 316 us                                                       | 309 us: 1.02x faster                                                               |
| pickle               | 9.89 us                                                      | 10.2 us: 1.03x slower                                                              |
| xml_etree_process    | 55.9 ms                                                      | 58.8 ms: 1.05x slower                                                              |
| xml_etree_generate   | 79.7 ms                                                      | 84.2 ms: 1.06x slower                                                              |
| unpickle             | 13.3 us                                                      | 14.8 us: 1.12x slower                                                              |
| pickle_list          | 3.94 us                                                      | 4.50 us: 1.14x slower                                                              |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                       |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 14.4 ms: 1.34x slower                                                              |
| python_startup_no_site | 7.73 ms                                                      | 12.8 ms: 1.66x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.49x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                              |
| django_template | 39.3 ms                                                      | 38.5 ms: 1.02x faster                                                              |
| genshi_xml      | 57.1 ms                                                      | 58.6 ms: 1.03x slower                                                              |
| genshi_text     | 25.5 ms                                                      | 27.9 ms: 1.09x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.00x faster                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-pythonperf2-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 121 us: 4.38x faster                                                               |
| asyncio_tcp                | 747 ms                                                       | 372 ms: 2.01x faster                                                               |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.94x faster                                                             |
| generators                 | 54.6 ms                                                      | 33.5 ms: 1.63x faster                                                              |
| pylint                     | 514 ms                                                       | 359 ms: 1.43x faster                                                               |
| comprehensions             | 25.1 us                                                      | 18.8 us: 1.33x faster                                                              |
| json_dumps                 | 13.3 ms                                                      | 10.6 ms: 1.25x faster                                                              |
| coroutines                 | 27.8 ms                                                      | 22.4 ms: 1.24x faster                                                              |
| gc_traversal               | 4.15 ms                                                      | 3.48 ms: 1.19x faster                                                              |
| async_tree_none            | 518 ms                                                       | 436 ms: 1.19x faster                                                               |
| json_loads                 | 28.9 us                                                      | 24.6 us: 1.18x faster                                                              |
| sympy_sum                  | 186 ms                                                       | 161 ms: 1.15x faster                                                               |
| async_tree_memoization     | 629 ms                                                       | 548 ms: 1.15x faster                                                               |
| richards_super             | 63.6 ms                                                      | 56.3 ms: 1.13x faster                                                              |
| chaos                      | 74.9 ms                                                      | 66.6 ms: 1.12x faster                                                              |
| mako                       | 11.0 ms                                                      | 9.92 ms: 1.11x faster                                                              |
| sympy_str                  | 337 ms                                                       | 305 ms: 1.11x faster                                                               |
| async_tree_none_tg         | 474 ms                                                       | 433 ms: 1.10x faster                                                               |
| fannkuch                   | 416 ms                                                       | 383 ms: 1.09x faster                                                               |
| chameleon                  | 7.92 ms                                                      | 7.30 ms: 1.09x faster                                                              |
| async_tree_memoization_tg  | 600 ms                                                       | 553 ms: 1.09x faster                                                               |
| async_tree_io              | 1.17 sec                                                     | 1.08 sec: 1.08x faster                                                             |
| xml_etree_parse            | 155 ms                                                       | 143 ms: 1.08x faster                                                               |
| sqlglot_parse              | 1.51 ms                                                      | 1.40 ms: 1.08x faster                                                              |
| mdp                        | 2.77 sec                                                     | 2.57 sec: 1.08x faster                                                             |
| crypto_pyaes               | 83.3 ms                                                      | 77.4 ms: 1.08x faster                                                              |
| sympy_expand               | 553 ms                                                       | 514 ms: 1.08x faster                                                               |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 702 ms: 1.07x faster                                                               |
| async_tree_io_tg           | 1.15 sec                                                     | 1.08 sec: 1.07x faster                                                             |
| logging_simple             | 7.24 us                                                      | 6.77 us: 1.07x faster                                                              |
| regex_compile              | 156 ms                                                       | 146 ms: 1.07x faster                                                               |
| pickle_dict                | 32.3 us                                                      | 30.4 us: 1.06x faster                                                              |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 705 ms: 1.06x faster                                                               |
| deepcopy                   | 391 us                                                       | 368 us: 1.06x faster                                                               |
| deltablue                  | 3.97 ms                                                      | 3.74 ms: 1.06x faster                                                              |
| thrift                     | 931 us                                                       | 879 us: 1.06x faster                                                               |
| xml_etree_iterparse        | 107 ms                                                       | 102 ms: 1.05x faster                                                               |
| sympy_integrate            | 25.8 ms                                                      | 24.7 ms: 1.05x faster                                                              |
| sqlglot_transpile          | 1.91 ms                                                      | 1.83 ms: 1.05x faster                                                              |
| deepcopy_reduce            | 3.40 us                                                      | 3.28 us: 1.04x faster                                                              |
| tomli_loads                | 2.25 sec                                                     | 2.18 sec: 1.03x faster                                                             |
| logging_silent             | 100 ns                                                       | 97.4 ns: 1.03x faster                                                              |
| unpickle_pure_python       | 238 us                                                       | 232 us: 1.03x faster                                                               |
| json                       | 5.58 ms                                                      | 5.45 ms: 1.02x faster                                                              |
| pickle_pure_python         | 316 us                                                       | 309 us: 1.02x faster                                                               |
| bench_thread_pool          | 1.00 ms                                                      | 979 us: 1.02x faster                                                               |
| logging_format             | 7.71 us                                                      | 7.55 us: 1.02x faster                                                              |
| django_template            | 39.3 ms                                                      | 38.5 ms: 1.02x faster                                                              |
| create_gc_cycles           | 1.58 ms                                                      | 1.55 ms: 1.02x faster                                                              |
| sqlglot_normalize          | 122 ms                                                       | 120 ms: 1.02x faster                                                               |
| spectral_norm              | 95.1 ms                                                      | 93.7 ms: 1.01x faster                                                              |
| nqueens                    | 103 ms                                                       | 101 ms: 1.01x faster                                                               |
| raytrace                   | 309 ms                                                       | 305 ms: 1.01x faster                                                               |
| deepcopy_memo              | 37.5 us                                                      | 37.1 us: 1.01x faster                                                              |
| asyncio_websockets         | 390 ms                                                       | 387 ms: 1.01x faster                                                               |
| meteor_contest             | 131 ms                                                       | 132 ms: 1.01x slower                                                               |
| richards                   | 49.7 ms                                                      | 50.4 ms: 1.01x slower                                                              |
| pprint_pformat             | 1.67 sec                                                     | 1.70 sec: 1.02x slower                                                             |
| html5lib                   | 72.2 ms                                                      | 73.8 ms: 1.02x slower                                                              |
| genshi_xml                 | 57.1 ms                                                      | 58.6 ms: 1.03x slower                                                              |
| nbody                      | 92.9 ms                                                      | 95.5 ms: 1.03x slower                                                              |
| pickle                     | 9.89 us                                                      | 10.2 us: 1.03x slower                                                              |
| pycparser                  | 1.31 sec                                                     | 1.35 sec: 1.03x slower                                                             |
| docutils                   | 2.85 sec                                                     | 2.93 sec: 1.03x slower                                                             |
| hexiom                     | 6.98 ms                                                      | 7.19 ms: 1.03x slower                                                              |
| tornado_http               | 124 ms                                                       | 128 ms: 1.03x slower                                                               |
| pathlib                    | 18.9 ms                                                      | 19.6 ms: 1.03x slower                                                              |
| pprint_safe_repr           | 805 ms                                                       | 833 ms: 1.03x slower                                                               |
| bench_mp_pool              | 4.70 ms                                                      | 4.87 ms: 1.04x slower                                                              |
| dulwich_log                | 67.4 ms                                                      | 69.9 ms: 1.04x slower                                                              |
| pidigits                   | 251 ms                                                       | 261 ms: 1.04x slower                                                               |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.25 ms: 1.05x slower                                                              |
| float                      | 74.9 ms                                                      | 78.6 ms: 1.05x slower                                                              |
| regex_v8                   | 24.4 ms                                                      | 25.7 ms: 1.05x slower                                                              |
| xml_etree_process          | 55.9 ms                                                      | 58.8 ms: 1.05x slower                                                              |
| xml_etree_generate         | 79.7 ms                                                      | 84.2 ms: 1.06x slower                                                              |
| 2to3                       | 287 ms                                                       | 304 ms: 1.06x slower                                                               |
| sqlglot_optimize           | 59.0 ms                                                      | 62.7 ms: 1.06x slower                                                              |
| sqlite_synth               | 2.52 us                                                      | 2.70 us: 1.07x slower                                                              |
| scimark_monte_carlo        | 69.8 ms                                                      | 75.1 ms: 1.08x slower                                                              |
| go                         | 158 ms                                                       | 172 ms: 1.09x slower                                                               |
| scimark_lu                 | 114 ms                                                       | 125 ms: 1.09x slower                                                               |
| genshi_text                | 25.5 ms                                                      | 27.9 ms: 1.09x slower                                                              |
| regex_effbot               | 3.34 ms                                                      | 3.67 ms: 1.10x slower                                                              |
| regex_dna                  | 227 ms                                                       | 252 ms: 1.11x slower                                                               |
| unpickle                   | 13.3 us                                                      | 14.8 us: 1.12x slower                                                              |
| gunicorn                   | 966 us                                                       | 1.08 ms: 1.12x slower                                                              |
| aiohttp                    | 986 us                                                       | 1.12 ms: 1.13x slower                                                              |
| scimark_fft                | 281 ms                                                       | 319 ms: 1.14x slower                                                               |
| pickle_list                | 3.94 us                                                      | 4.50 us: 1.14x slower                                                              |
| pyflate                    | 449 ms                                                       | 515 ms: 1.15x slower                                                               |
| telco                      | 6.81 ms                                                      | 8.12 ms: 1.19x slower                                                              |
| coverage                   | 66.1 ms                                                      | 79.0 ms: 1.20x slower                                                              |
| async_generators           | 322 ms                                                       | 388 ms: 1.21x slower                                                               |
| mypy2                      | 762 ms                                                       | 919 ms: 1.21x slower                                                               |
| python_startup             | 10.7 ms                                                      | 14.4 ms: 1.34x slower                                                              |
| unpack_sequence            | 45.7 ns                                                      | 62.6 ns: 1.37x slower                                                              |
| scimark_sor                | 110 ms                                                       | 152 ms: 1.38x slower                                                               |
| python_startup_no_site     | 7.73 ms                                                      | 12.8 ms: 1.66x slower                                                              |
| Geometric mean             | (ref)                                                        | 1.03x faster                                                                       |

Benchmark hidden because not significant (2): dask, unpickle_list
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 83.24% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.25x