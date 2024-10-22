# Results vs. 3.13.0

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 516 ms: 1.69x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.15 sec: 1.43x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.89x slower                                                    |
| tornado_http   | 131 ms                                                   | 200 ms: 1.52x slower                                                    |
| Geometric mean | (ref)                                                    | 1.62x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 696 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 660 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 871 ms: 1.18x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 566 ms: 1.21x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 767 ms: 1.23x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 942 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| async_tree_none            | 493 ms                                                   | 631 ms: 1.28x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 39.0 ms: 1.38x slower                                                   |
| async_generators           | 496 ms                                                   | 692 ms: 1.40x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 207 ms: 2.20x slower                                                    |
| nbody          | 114 ms                                                   | 285 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                    | 1.77x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.41 ms: 1.10x faster                                                   |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| regex_v8       | 31.5 ms                                                  | 32.8 ms: 1.04x slower                                                   |
| regex_compile  | 128 ms                                                   | 256 ms: 1.99x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 177 ms: 1.06x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 155 ms: 1.06x slower                                                    |
| json_loads           | 31.4 us                                                  | 39.1 us: 1.24x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.9 ms: 1.34x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 130 ms: 1.63x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.19 sec: 1.66x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 550 us: 2.16x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 781 us: 2.17x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 17.6 ms: 1.32x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 11.7 ms: 1.34x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.33x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 105 ms: 1.74x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 52.8 ms: 1.91x slower                                                   |
| django_template | 42.3 ms                                                  | 82.3 ms: 1.95x slower                                                   |
| mako            | 13.3 ms                                                  | 29.1 ms: 2.18x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.94x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.60 ms: 1.33x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.45 ms: 1.31x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.14 ms: 1.19x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.41 ms: 1.10x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 177 ms: 1.06x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 32.8 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 155 ms: 1.06x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 696 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| pathlib                    | 22.4 ms                                                  | 26.0 ms: 1.16x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 660 ms: 1.16x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 871 ms: 1.18x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 566 ms: 1.21x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 767 ms: 1.23x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 942 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| json                       | 5.61 ms                                                  | 6.96 ms: 1.24x slower                                                   |
| json_loads                 | 31.4 us                                                  | 39.1 us: 1.24x slower                                                   |
| deepcopy                   | 451 us                                                   | 566 us: 1.25x slower                                                    |
| telco                      | 9.73 ms                                                  | 12.4 ms: 1.27x slower                                                   |
| async_tree_none            | 493 ms                                                   | 631 ms: 1.28x slower                                                    |
| mdp                        | 3.36 sec                                                 | 4.33 sec: 1.29x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.44 sec: 1.30x slower                                                  |
| python_startup             | 13.3 ms                                                  | 17.6 ms: 1.32x slower                                                   |
| scimark_fft                | 447 ms                                                   | 593 ms: 1.33x slower                                                    |
| json_dumps                 | 13.4 ms                                                  | 17.9 ms: 1.34x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 11.7 ms: 1.34x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.82 ms: 1.34x slower                                                   |
| coverage                   | 98.5 ms                                                  | 135 ms: 1.37x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 39.0 ms: 1.38x slower                                                   |
| async_generators           | 496 ms                                                   | 692 ms: 1.40x slower                                                    |
| deepcopy_memo              | 51.0 us                                                  | 71.9 us: 1.41x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.15 sec: 1.43x slower                                                  |
| xml_etree_generate         | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.87 ms: 1.46x slower                                                   |
| pylint                     | 343 ms                                                   | 508 ms: 1.48x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.07 us: 1.49x slower                                                   |
| generators                 | 37.8 ms                                                  | 57.0 ms: 1.51x slower                                                   |
| meteor_contest             | 113 ms                                                   | 173 ms: 1.52x slower                                                    |
| tornado_http               | 131 ms                                                   | 200 ms: 1.52x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 152 ms: 1.54x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.52 sec: 1.61x slower                                                  |
| xml_etree_process          | 80.1 ms                                                  | 130 ms: 1.63x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 2.06 sec: 1.63x slower                                                  |
| spectral_norm              | 141 ms                                                   | 233 ms: 1.65x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.19 sec: 1.66x slower                                                  |
| sympy_integrate            | 21.0 ms                                                  | 34.9 ms: 1.67x slower                                                   |
| fannkuch                   | 452 ms                                                   | 758 ms: 1.68x slower                                                    |
| 2to3                       | 306 ms                                                   | 516 ms: 1.69x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 141 ms: 1.71x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 334 us: 1.74x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 105 ms: 1.74x slower                                                    |
| thrift                     | 946 us                                                   | 1.69 ms: 1.79x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 231 ms: 1.80x slower                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 114 ms: 1.84x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.89x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 52.8 ms: 1.91x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.77 sec: 1.91x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.64 sec: 1.92x slower                                                  |
| django_template            | 42.3 ms                                                  | 82.3 ms: 1.95x slower                                                   |
| sympy_str                  | 264 ms                                                   | 514 ms: 1.95x slower                                                    |
| regex_compile              | 128 ms                                                   | 256 ms: 1.99x slower                                                    |
| logging_format             | 7.83 us                                                  | 15.8 us: 2.02x slower                                                   |
| comprehensions             | 20.4 us                                                  | 41.3 us: 2.02x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.7 us: 2.09x slower                                                   |
| sympy_expand               | 455 ms                                                   | 951 ms: 2.09x slower                                                    |
| logging_silent             | 135 ns                                                   | 285 ns: 2.11x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 179 ms: 2.14x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 550 us: 2.16x slower                                                    |
| scimark_sor                | 159 ms                                                   | 345 ms: 2.17x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 781 us: 2.17x slower                                                    |
| mako                       | 13.3 ms                                                  | 29.1 ms: 2.18x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 313 ms: 2.18x slower                                                    |
| float                      | 94.4 ms                                                  | 207 ms: 2.20x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.8 ms: 2.21x slower                                                   |
| richards                   | 53.5 ms                                                  | 121 ms: 2.26x slower                                                    |
| richards_super             | 60.3 ms                                                  | 139 ms: 2.30x slower                                                    |
| chaos                      | 68.8 ms                                                  | 162 ms: 2.35x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 343 ms: 2.46x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.29 ms: 2.48x slower                                                   |
| nbody                      | 114 ms                                                   | 285 ms: 2.50x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.70 ms: 2.68x slower                                                   |
| go                         | 163 ms                                                   | 448 ms: 2.76x slower                                                    |
| raytrace                   | 298 ms                                                   | 826 ms: 2.77x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.8 ms: 3.34x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.58x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.17x