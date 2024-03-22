# Results vs. 3.11.0

- fork: python
- ref: dcaf33a41d5d220523d7
- machine: linux-x86_64
- commit hash: dcaf33a
- commit date: 2024-03-20
- overall geometric mean: 1.18x slower
- HPT reliability: 99.96%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                       | 332 ms: 1.16x slower                                                         |
| chameleon      | 7.92 ms                                                      | 7.21 ms: 1.10x faster                                                        |
| docutils       | 2.85 sec                                                     | 4.70 sec: 1.65x slower                                                       |
| html5lib       | 72.2 ms                                                      | 82.5 ms: 1.14x slower                                                        |
| tornado_http   | 124 ms                                                       | 128 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                        | 1.15x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 753 ms                                                       | 3.32 sec: 4.41x slower                                                       |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 3.44 sec: 4.58x slower                                                       |
| async_tree_none            | 518 ms                                                       | 2.74 sec: 5.30x slower                                                       |
| async_tree_memoization     | 629 ms                                                       | 3.44 sec: 5.47x slower                                                       |
| async_tree_memoization_tg  | 600 ms                                                       | 3.53 sec: 5.88x slower                                                       |
| async_tree_none_tg         | 474 ms                                                       | 2.88 sec: 6.06x slower                                                       |
| async_tree_io              | 1.17 sec                                                     | 9.75 sec: 8.32x slower                                                       |
| async_tree_io_tg           | 1.15 sec                                                     | 10.2 sec: 8.84x slower                                                       |
| Geometric mean             | (ref)                                                        | 5.93x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 251 ms                                                       | 261 ms: 1.04x slower                                                         |
| float          | 74.9 ms                                                      | 154 ms: 2.05x slower                                                         |
| Geometric mean | (ref)                                                        | 1.29x slower                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 156 ms                                                       | 146 ms: 1.07x faster                                                         |
| regex_v8       | 24.4 ms                                                      | 25.9 ms: 1.06x slower                                                        |
| regex_dna      | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| regex_effbot   | 3.34 ms                                                      | 3.57 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                      | 10.5 ms: 1.26x faster                                                        |
| json_loads           | 28.9 us                                                      | 24.8 us: 1.16x faster                                                        |
| tomli_loads          | 2.25 sec                                                     | 2.15 sec: 1.05x faster                                                       |
| unpickle_pure_python | 238 us                                                       | 229 us: 1.04x faster                                                         |
| unpickle_list        | 4.60 us                                                      | 4.64 us: 1.01x slower                                                        |
| pickle_pure_python   | 316 us                                                       | 319 us: 1.01x slower                                                         |
| pickle_dict          | 32.3 us                                                      | 33.0 us: 1.02x slower                                                        |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                        |
| pickle_list          | 3.94 us                                                      | 4.44 us: 1.13x slower                                                        |
| unpickle             | 13.3 us                                                      | 15.4 us: 1.16x slower                                                        |
| xml_etree_process    | 55.9 ms                                                      | 68.1 ms: 1.22x slower                                                        |
| xml_etree_generate   | 79.7 ms                                                      | 98.9 ms: 1.24x slower                                                        |
| xml_etree_parse      | 155 ms                                                       | 209 ms: 1.35x slower                                                         |
| xml_etree_iterparse  | 107 ms                                                       | 168 ms: 1.58x slower                                                         |
| Geometric mean       | (ref)                                                        | 1.08x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.7 ms                                                      | 14.5 ms: 1.35x slower                                                        |
| python_startup_no_site | 7.73 ms                                                      | 12.6 ms: 1.63x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.48x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.0 ms                                                      | 9.98 ms: 1.10x faster                                                        |
| django_template | 39.3 ms                                                      | 38.1 ms: 1.03x faster                                                        |
| genshi_text     | 25.5 ms                                                      | 29.5 ms: 1.16x slower                                                        |
| genshi_xml      | 57.1 ms                                                      | 66.9 ms: 1.17x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240320-pythonperf2-x86_64-python-dcaf33a41d5d220523d7-3.13.0a5+-dcaf33a |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 532 us                                                       | 115 us: 4.63x faster                                                         |
| asyncio_tcp                | 747 ms                                                       | 371 ms: 2.02x faster                                                         |
| asyncio_tcp_ssl            | 3.07 sec                                                     | 1.58 sec: 1.95x faster                                                       |
| generators                 | 54.6 ms                                                      | 33.3 ms: 1.64x faster                                                        |
| comprehensions             | 25.1 us                                                      | 19.1 us: 1.31x faster                                                        |
| json_dumps                 | 13.3 ms                                                      | 10.5 ms: 1.26x faster                                                        |
| coroutines                 | 27.8 ms                                                      | 22.8 ms: 1.22x faster                                                        |
| sympy_sum                  | 186 ms                                                       | 159 ms: 1.17x faster                                                         |
| json_loads                 | 28.9 us                                                      | 24.8 us: 1.16x faster                                                        |
| chaos                      | 74.9 ms                                                      | 66.7 ms: 1.12x faster                                                        |
| sympy_str                  | 337 ms                                                       | 300 ms: 1.12x faster                                                         |
| logging_simple             | 7.24 us                                                      | 6.52 us: 1.11x faster                                                        |
| richards_super             | 63.6 ms                                                      | 57.3 ms: 1.11x faster                                                        |
| mako                       | 11.0 ms                                                      | 9.98 ms: 1.10x faster                                                        |
| chameleon                  | 7.92 ms                                                      | 7.21 ms: 1.10x faster                                                        |
| thrift                     | 931 us                                                       | 859 us: 1.08x faster                                                         |
| sympy_expand               | 553 ms                                                       | 511 ms: 1.08x faster                                                         |
| logging_format             | 7.71 us                                                      | 7.16 us: 1.08x faster                                                        |
| crypto_pyaes               | 83.3 ms                                                      | 77.8 ms: 1.07x faster                                                        |
| bench_thread_pool          | 1.00 ms                                                      | 935 us: 1.07x faster                                                         |
| regex_compile              | 156 ms                                                       | 146 ms: 1.07x faster                                                         |
| sympy_integrate            | 25.8 ms                                                      | 24.3 ms: 1.06x faster                                                        |
| fannkuch                   | 416 ms                                                       | 396 ms: 1.05x faster                                                         |
| tomli_loads                | 2.25 sec                                                     | 2.15 sec: 1.05x faster                                                       |
| unpickle_pure_python       | 238 us                                                       | 229 us: 1.04x faster                                                         |
| json                       | 5.58 ms                                                      | 5.36 ms: 1.04x faster                                                        |
| mdp                        | 2.77 sec                                                     | 2.68 sec: 1.03x faster                                                       |
| django_template            | 39.3 ms                                                      | 38.1 ms: 1.03x faster                                                        |
| deepcopy                   | 391 us                                                       | 379 us: 1.03x faster                                                         |
| logging_silent             | 100 ns                                                       | 97.7 ns: 1.03x faster                                                        |
| nqueens                    | 103 ms                                                       | 100 ms: 1.02x faster                                                         |
| sqlglot_normalize          | 122 ms                                                       | 119 ms: 1.02x faster                                                         |
| deepcopy_memo              | 37.5 us                                                      | 36.9 us: 1.02x faster                                                        |
| spectral_norm              | 95.1 ms                                                      | 93.8 ms: 1.01x faster                                                        |
| asyncio_websockets         | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| meteor_contest             | 131 ms                                                       | 131 ms: 1.01x slower                                                         |
| unpickle_list              | 4.60 us                                                      | 4.64 us: 1.01x slower                                                        |
| pickle_pure_python         | 316 us                                                       | 319 us: 1.01x slower                                                         |
| scimark_lu                 | 114 ms                                                       | 115 ms: 1.01x slower                                                         |
| pathlib                    | 18.9 ms                                                      | 19.2 ms: 1.01x slower                                                        |
| deltablue                  | 3.97 ms                                                      | 4.02 ms: 1.01x slower                                                        |
| pprint_pformat             | 1.67 sec                                                     | 1.70 sec: 1.02x slower                                                       |
| pickle_dict                | 32.3 us                                                      | 33.0 us: 1.02x slower                                                        |
| dulwich_log                | 67.4 ms                                                      | 68.9 ms: 1.02x slower                                                        |
| tornado_http               | 124 ms                                                       | 128 ms: 1.03x slower                                                         |
| sqlglot_parse              | 1.51 ms                                                      | 1.55 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 805 ms                                                       | 830 ms: 1.03x slower                                                         |
| hexiom                     | 6.98 ms                                                      | 7.21 ms: 1.03x slower                                                        |
| richards                   | 49.7 ms                                                      | 51.5 ms: 1.04x slower                                                        |
| pidigits                   | 251 ms                                                       | 261 ms: 1.04x slower                                                         |
| sqlglot_transpile          | 1.91 ms                                                      | 2.02 ms: 1.06x slower                                                        |
| regex_v8                   | 24.4 ms                                                      | 25.9 ms: 1.06x slower                                                        |
| regex_dna                  | 227 ms                                                       | 241 ms: 1.06x slower                                                         |
| create_gc_cycles           | 1.58 ms                                                      | 1.68 ms: 1.06x slower                                                        |
| pickle                     | 9.89 us                                                      | 10.5 us: 1.06x slower                                                        |
| regex_effbot               | 3.34 ms                                                      | 3.57 ms: 1.07x slower                                                        |
| sqlite_synth               | 2.52 us                                                      | 2.71 us: 1.07x slower                                                        |
| scimark_sparse_mat_mult    | 4.06 ms                                                      | 4.37 ms: 1.08x slower                                                        |
| gc_traversal               | 4.15 ms                                                      | 4.47 ms: 1.08x slower                                                        |
| sqlglot_optimize           | 59.0 ms                                                      | 64.5 ms: 1.09x slower                                                        |
| scimark_monte_carlo        | 69.8 ms                                                      | 76.6 ms: 1.10x slower                                                        |
| go                         | 158 ms                                                       | 175 ms: 1.11x slower                                                         |
| pickle_list                | 3.94 us                                                      | 4.44 us: 1.13x slower                                                        |
| mypy2                      | 762 ms                                                       | 863 ms: 1.13x slower                                                         |
| pyflate                    | 449 ms                                                       | 513 ms: 1.14x slower                                                         |
| html5lib                   | 72.2 ms                                                      | 82.5 ms: 1.14x slower                                                        |
| scimark_fft                | 281 ms                                                       | 322 ms: 1.15x slower                                                         |
| genshi_text                | 25.5 ms                                                      | 29.5 ms: 1.16x slower                                                        |
| gunicorn                   | 966 us                                                       | 1.12 ms: 1.16x slower                                                        |
| 2to3                       | 287 ms                                                       | 332 ms: 1.16x slower                                                         |
| unpickle                   | 13.3 us                                                      | 15.4 us: 1.16x slower                                                        |
| aiohttp                    | 986 us                                                       | 1.15 ms: 1.17x slower                                                        |
| genshi_xml                 | 57.1 ms                                                      | 66.9 ms: 1.17x slower                                                        |
| telco                      | 6.81 ms                                                      | 8.07 ms: 1.18x slower                                                        |
| xml_etree_process          | 55.9 ms                                                      | 68.1 ms: 1.22x slower                                                        |
| coverage                   | 66.1 ms                                                      | 81.0 ms: 1.23x slower                                                        |
| pycparser                  | 1.31 sec                                                     | 1.60 sec: 1.23x slower                                                       |
| xml_etree_generate         | 79.7 ms                                                      | 98.9 ms: 1.24x slower                                                        |
| xml_etree_parse            | 155 ms                                                       | 209 ms: 1.35x slower                                                         |
| python_startup             | 10.7 ms                                                      | 14.5 ms: 1.35x slower                                                        |
| scimark_sor                | 110 ms                                                       | 153 ms: 1.39x slower                                                         |
| async_generators           | 322 ms                                                       | 474 ms: 1.48x slower                                                         |
| xml_etree_iterparse        | 107 ms                                                       | 168 ms: 1.58x slower                                                         |
| unpack_sequence            | 45.7 ns                                                      | 74.0 ns: 1.62x slower                                                        |
| python_startup_no_site     | 7.73 ms                                                      | 12.6 ms: 1.63x slower                                                        |
| pylint                     | 514 ms                                                       | 839 ms: 1.63x slower                                                         |
| docutils                   | 2.85 sec                                                     | 4.70 sec: 1.65x slower                                                       |
| dask                       | 410 ms                                                       | 711 ms: 1.74x slower                                                         |
| float                      | 74.9 ms                                                      | 154 ms: 2.05x slower                                                         |
| async_tree_cpu_io_mixed    | 753 ms                                                       | 3.32 sec: 4.41x slower                                                       |
| async_tree_cpu_io_mixed_tg | 750 ms                                                       | 3.44 sec: 4.58x slower                                                       |
| async_tree_none            | 518 ms                                                       | 2.74 sec: 5.30x slower                                                       |
| async_tree_memoization     | 629 ms                                                       | 3.44 sec: 5.47x slower                                                       |
| async_tree_memoization_tg  | 600 ms                                                       | 3.53 sec: 5.88x slower                                                       |
| async_tree_none_tg         | 474 ms                                                       | 2.88 sec: 6.06x slower                                                       |
| async_tree_io              | 1.17 sec                                                     | 9.75 sec: 8.32x slower                                                       |
| async_tree_io_tg           | 1.15 sec                                                     | 10.2 sec: 8.84x slower                                                       |
| Geometric mean             | (ref)                                                        | 1.18x slower                                                                 |

Benchmark hidden because not significant (4): deepcopy_reduce, raytrace, bench_mp_pool, nbody
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf2-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.96% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.02x
- 99% likely to have a slowdown of 1.02x


# Memory

- memory change: 1.13x