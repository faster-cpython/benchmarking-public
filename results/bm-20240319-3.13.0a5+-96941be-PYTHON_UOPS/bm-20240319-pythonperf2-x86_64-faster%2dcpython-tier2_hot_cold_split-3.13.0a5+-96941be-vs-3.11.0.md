# Results vs. 3.11.0

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 96941be
- commit date: 2024-03-19
- overall geometric mean: 1.07x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 333 ms: 1.16x slower                                                                   |
| chameleon      | 7.92 ms                                                      | 7.56 ms: 1.05x faster                                                                  |
| docutils       | 2.85 sec                                                     | 3.11 sec: 1.09x slower                                                                 |
| html5lib       | 72.2 ms                                                      | 79.8 ms: 1.11x slower                                                                  |
| tornado_http   | 124 ms                                                       | 131 ms: 1.05x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_none            | 518 ms                                                       | 452 ms: 1.15x faster                                                                   |
| async_tree_memoization     | 629 ms                                                       | 571 ms: 1.10x faster                                                                   |
| async_tree_memoization_tg  | 600 ms                                                       | 556 ms: 1.08x faster                                                                   |
| async_tree_none_tg         | 474 ms                                                       | 449 ms: 1.06x faster                                                                   |
| async_tree_io              | 1.17 sec                                                     | 1.12 sec: 1.05x faster                                                                 |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 720 ms: 1.05x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 719 ms: 1.04x faster                                                                   |
| async_tree_io_tg           | 1.15 sec                                                     | 1.11 sec: 1.04x faster                                                                 |
| Geometric mean             | (ref)                                                        | 1.07x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 264 ms: 1.05x slower                                                                   |
| float          | 74.9 ms                                                      | 102 ms: 1.37x slower                                                                   |
| nbody          | 92.9 ms                                                      | 143 ms: 1.54x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.30x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_dna      | 227 ms                                                       | 244 ms: 1.07x slower                                                                   |
| regex_v8       | 24.4 ms                                                      | 26.2 ms: 1.07x slower                                                                  |
| regex_effbot   | 3.34 ms                                                      | 3.63 ms: 1.09x slower                                                                  |
| regex_compile  | 156 ms                                                       | 215 ms: 1.38x slower                                                                   |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.9 ms: 1.21x faster                                                                  |
| json_loads           | 28.9 us                                                      | 25.0 us: 1.16x faster                                                                  |
| xml_etree_parse      | 155 ms                                                       | 148 ms: 1.05x faster                                                                   |
| pickle_dict          | 32.3 us                                                      | 33.0 us: 1.02x slower                                                                  |
| pickle_pure_python   | 316 us                                                       | 326 us: 1.03x slower                                                                   |
| unpickle_list        | 4.60 us                                                      | 4.74 us: 1.03x slower                                                                  |
| xml_etree_iterparse  | 107 ms                                                       | 114 ms: 1.07x slower                                                                   |
| unpickle             | 13.3 us                                                      | 14.8 us: 1.12x slower                                                                  |
| pickle               | 9.89 us                                                      | 11.1 us: 1.12x slower                                                                  |
| xml_etree_process    | 55.9 ms                                                      | 63.7 ms: 1.14x slower                                                                  |
| pickle_list          | 3.94 us                                                      | 4.50 us: 1.14x slower                                                                  |
| xml_etree_generate   | 79.7 ms                                                      | 92.3 ms: 1.16x slower                                                                  |
| unpickle_pure_python | 238 us                                                       | 305 us: 1.28x slower                                                                   |
| tomli_loads          | 2.25 sec                                                     | 2.97 sec: 1.32x slower                                                                 |
| Geometric mean       | (ref)                                                        | 1.07x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 12.8 ms: 1.19x slower                                                                  |
| python_startup_no_site | 7.73 ms                                                      | 11.2 ms: 1.45x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| django_template | 39.3 ms                                                      | 40.3 ms: 1.03x slower                                                                  |
| genshi_text     | 25.5 ms                                                      | 28.2 ms: 1.11x slower                                                                  |
| genshi_xml      | 57.1 ms                                                      | 64.3 ms: 1.13x slower                                                                  |
| mako            | 11.0 ms                                                      | 13.9 ms: 1.26x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.13x slower                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-pythonperf2-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-96941be |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 131 us: 4.05x faster                                                                   |
| asyncio_tcp                | 747 ms                                                       | 380 ms: 1.96x faster                                                                   |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.60 sec: 1.92x faster                                                                 |
| generators                 | 54.6 ms                                                      | 33.9 ms: 1.61x faster                                                                  |
| pylint                     | 514 ms                                                       | 374 ms: 1.37x faster                                                                   |
| coroutines                 | 27.8 ms                                                      | 22.6 ms: 1.23x faster                                                                  |
| json_dumps                 | 13.3 ms                                                      | 10.9 ms: 1.21x faster                                                                  |
| gc_traversal               | 4.15 ms                                                      | 3.54 ms: 1.17x faster                                                                  |
| json_loads                 | 28.9 us                                                      | 25.0 us: 1.16x faster                                                                  |
| async_tree_none            | 518 ms                                                       | 452 ms: 1.15x faster                                                                   |
| async_tree_memoization     | 629 ms                                                       | 571 ms: 1.10x faster                                                                   |
| async_tree_memoization_tg  | 600 ms                                                       | 556 ms: 1.08x faster                                                                   |
| logging_simple             | 7.24 us                                                      | 6.79 us: 1.07x faster                                                                  |
| thrift                     | 931 us                                                       | 880 us: 1.06x faster                                                                   |
| sympy_sum                  | 186 ms                                                       | 176 ms: 1.06x faster                                                                   |
| async_tree_none_tg         | 474 ms                                                       | 449 ms: 1.06x faster                                                                   |
| async_tree_io              | 1.17 sec                                                     | 1.12 sec: 1.05x faster                                                                 |
| chameleon                  | 7.92 ms                                                      | 7.56 ms: 1.05x faster                                                                  |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 720 ms: 1.05x faster                                                                   |
| xml_etree_parse            | 155 ms                                                       | 148 ms: 1.05x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 719 ms: 1.04x faster                                                                   |
| async_tree_io_tg           | 1.15 sec                                                     | 1.11 sec: 1.04x faster                                                                 |
| logging_format             | 7.71 us                                                      | 7.48 us: 1.03x faster                                                                  |
| mdp                        | 2.77 sec                                                     | 2.70 sec: 1.03x faster                                                                 |
| comprehensions             | 25.1 us                                                      | 24.5 us: 1.02x faster                                                                  |
| json                       | 5.58 ms                                                      | 5.45 ms: 1.02x faster                                                                  |
| sympy_integrate            | 25.8 ms                                                      | 25.6 ms: 1.01x faster                                                                  |
| sympy_str                  | 337 ms                                                       | 342 ms: 1.01x slower                                                                   |
| create_gc_cycles           | 1.58 ms                                                      | 1.60 ms: 1.01x slower                                                                  |
| dask                       | 410 ms                                                       | 416 ms: 1.02x slower                                                                   |
| pickle_dict                | 32.3 us                                                      | 33.0 us: 1.02x slower                                                                  |
| sqlglot_normalize          | 122 ms                                                       | 125 ms: 1.02x slower                                                                   |
| crypto_pyaes               | 83.3 ms                                                      | 85.4 ms: 1.03x slower                                                                  |
| django_template            | 39.3 ms                                                      | 40.3 ms: 1.03x slower                                                                  |
| pickle_pure_python         | 316 us                                                       | 326 us: 1.03x slower                                                                   |
| unpickle_list              | 4.60 us                                                      | 4.74 us: 1.03x slower                                                                  |
| deepcopy                   | 391 us                                                       | 404 us: 1.03x slower                                                                   |
| chaos                      | 74.9 ms                                                      | 77.5 ms: 1.03x slower                                                                  |
| deltablue                  | 3.97 ms                                                      | 4.14 ms: 1.04x slower                                                                  |
| deepcopy_reduce            | 3.40 us                                                      | 3.54 us: 1.04x slower                                                                  |
| pidigits                   | 251 ms                                                       | 264 ms: 1.05x slower                                                                   |
| tornado_http               | 124 ms                                                       | 131 ms: 1.05x slower                                                                   |
| sympy_expand               | 553 ms                                                       | 585 ms: 1.06x slower                                                                   |
| richards_super             | 63.6 ms                                                      | 67.5 ms: 1.06x slower                                                                  |
| pathlib                    | 18.9 ms                                                      | 20.2 ms: 1.07x slower                                                                  |
| xml_etree_iterparse        | 107 ms                                                       | 114 ms: 1.07x slower                                                                   |
| meteor_contest             | 131 ms                                                       | 139 ms: 1.07x slower                                                                   |
| sqlglot_parse              | 1.51 ms                                                      | 1.62 ms: 1.07x slower                                                                  |
| regex_dna                  | 227 ms                                                       | 244 ms: 1.07x slower                                                                   |
| regex_v8                   | 24.4 ms                                                      | 26.2 ms: 1.07x slower                                                                  |
| sqlglot_transpile          | 1.91 ms                                                      | 2.06 ms: 1.08x slower                                                                  |
| regex_effbot               | 3.34 ms                                                      | 3.63 ms: 1.09x slower                                                                  |
| bench_mp_pool              | 4.70 ms                                                      | 5.12 ms: 1.09x slower                                                                  |
| docutils                   | 2.85 sec                                                     | 3.11 sec: 1.09x slower                                                                 |
| html5lib                   | 72.2 ms                                                      | 79.8 ms: 1.11x slower                                                                  |
| genshi_text                | 25.5 ms                                                      | 28.2 ms: 1.11x slower                                                                  |
| sqlite_synth               | 2.52 us                                                      | 2.81 us: 1.11x slower                                                                  |
| unpickle                   | 13.3 us                                                      | 14.8 us: 1.12x slower                                                                  |
| nqueens                    | 103 ms                                                       | 115 ms: 1.12x slower                                                                   |
| pickle                     | 9.89 us                                                      | 11.1 us: 1.12x slower                                                                  |
| genshi_xml                 | 57.1 ms                                                      | 64.3 ms: 1.13x slower                                                                  |
| raytrace                   | 309 ms                                                       | 349 ms: 1.13x slower                                                                   |
| gunicorn                   | 966 us                                                       | 1.09 ms: 1.13x slower                                                                  |
| aiohttp                    | 986 us                                                       | 1.12 ms: 1.14x slower                                                                  |
| xml_etree_process          | 55.9 ms                                                      | 63.7 ms: 1.14x slower                                                                  |
| pickle_list                | 3.94 us                                                      | 4.50 us: 1.14x slower                                                                  |
| bench_thread_pool          | 1.00 ms                                                      | 1.15 ms: 1.15x slower                                                                  |
| pycparser                  | 1.31 sec                                                     | 1.51 sec: 1.15x slower                                                                 |
| xml_etree_generate         | 79.7 ms                                                      | 92.3 ms: 1.16x slower                                                                  |
| scimark_lu                 | 114 ms                                                       | 132 ms: 1.16x slower                                                                   |
| 2to3                       | 287 ms                                                       | 333 ms: 1.16x slower                                                                   |
| dulwich_log                | 67.4 ms                                                      | 78.4 ms: 1.16x slower                                                                  |
| sqlglot_optimize           | 59.0 ms                                                      | 69.5 ms: 1.18x slower                                                                  |
| python_startup             | 10.7 ms                                                      | 12.8 ms: 1.19x slower                                                                  |
| deepcopy_memo              | 37.5 us                                                      | 44.9 us: 1.20x slower                                                                  |
| pprint_pformat             | 1.67 sec                                                     | 2.02 sec: 1.21x slower                                                                 |
| pprint_safe_repr           | 805 ms                                                       | 981 ms: 1.22x slower                                                                   |
| richards                   | 49.7 ms                                                      | 61.2 ms: 1.23x slower                                                                  |
| async_generators           | 322 ms                                                       | 398 ms: 1.24x slower                                                                   |
| fannkuch                   | 416 ms                                                       | 519 ms: 1.25x slower                                                                   |
| mypy2                      | 762 ms                                                       | 960 ms: 1.26x slower                                                                   |
| mako                       | 11.0 ms                                                      | 13.9 ms: 1.26x slower                                                                  |
| telco                      | 6.81 ms                                                      | 8.67 ms: 1.27x slower                                                                  |
| unpickle_pure_python       | 238 us                                                       | 305 us: 1.28x slower                                                                   |
| go                         | 158 ms                                                       | 208 ms: 1.32x slower                                                                   |
| tomli_loads                | 2.25 sec                                                     | 2.97 sec: 1.32x slower                                                                 |
| coverage                   | 66.1 ms                                                      | 89.3 ms: 1.35x slower                                                                  |
| float                      | 74.9 ms                                                      | 102 ms: 1.37x slower                                                                   |
| scimark_monte_carlo        | 69.8 ms                                                      | 95.8 ms: 1.37x slower                                                                  |
| regex_compile              | 156 ms                                                       | 215 ms: 1.38x slower                                                                   |
| scimark_sor                | 110 ms                                                       | 159 ms: 1.45x slower                                                                   |
| python_startup_no_site     | 7.73 ms                                                      | 11.2 ms: 1.45x slower                                                                  |
| pyflate                    | 449 ms                                                       | 660 ms: 1.47x slower                                                                   |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 5.98 ms: 1.47x slower                                                                  |
| unpack_sequence            | 45.7 ns                                                      | 68.0 ns: 1.49x slower                                                                  |
| hexiom                     | 6.98 ms                                                      | 10.7 ms: 1.53x slower                                                                  |
| nbody                      | 92.9 ms                                                      | 143 ms: 1.54x slower                                                                   |
| scimark_fft                | 281 ms                                                       | 432 ms: 1.54x slower                                                                   |
| spectral_norm              | 95.1 ms                                                      | 147 ms: 1.55x slower                                                                   |
| Geometric mean             | (ref)                                                        | 1.07x slower                                                                           |

Benchmark hidden because not significant (2): asyncio_websockets, logging_silent
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x


# Memory

- memory change: 1.01x