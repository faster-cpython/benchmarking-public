# Results vs. 3.13.0

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.59x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.41x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 522 ms: 1.71x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.12 sec: 1.42x slower                                                  |
| html5lib       | 64.3 ms                                                  | 123 ms: 1.91x slower                                                    |
| tornado_http   | 131 ms                                                   | 209 ms: 1.59x slower                                                    |
| Geometric mean | (ref)                                                    | 1.65x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 868 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 672 ms: 1.18x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 743 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 917 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 571 ms: 1.22x slower                                                    |
| async_tree_none            | 493 ms                                                   | 612 ms: 1.24x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| async_generators           | 496 ms                                                   | 670 ms: 1.35x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 41.1 ms: 1.46x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 209 ms: 2.22x slower                                                    |
| nbody          | 114 ms                                                   | 285 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                    | 1.77x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| regex_dna      | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| regex_v8       | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                   | 258 ms: 2.01x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 180 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 159 ms: 1.09x slower                                                    |
| json_loads           | 31.4 us                                                  | 38.9 us: 1.24x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 18.2 ms: 1.36x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 131 ms: 1.64x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.28 sec: 1.69x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 546 us: 2.14x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 787 us: 2.19x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.48x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.1 ms: 1.36x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 109 ms: 1.81x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 55.1 ms: 1.99x slower                                                   |
| django_template | 42.3 ms                                                  | 84.1 ms: 1.99x slower                                                   |
| mako            | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.99x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.62 ms: 1.31x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.51 ms: 1.29x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 180 ms: 1.04x faster                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.16 ms: 1.02x faster                                                   |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.03x slower                                                    |
| regex_dna                  | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 159 ms: 1.09x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.47 sec: 1.13x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 868 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 672 ms: 1.18x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 743 ms: 1.19x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.6 ms: 1.19x slower                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 917 ms: 1.20x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 571 ms: 1.22x slower                                                    |
| json_loads                 | 31.4 us                                                  | 38.9 us: 1.24x slower                                                   |
| async_tree_none            | 493 ms                                                   | 612 ms: 1.24x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| deepcopy                   | 451 us                                                   | 564 us: 1.25x slower                                                    |
| json                       | 5.61 ms                                                  | 7.04 ms: 1.25x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.34 sec: 1.29x slower                                                  |
| scimark_fft                | 447 ms                                                   | 582 ms: 1.30x slower                                                    |
| telco                      | 9.73 ms                                                  | 13.1 ms: 1.34x slower                                                   |
| async_generators           | 496 ms                                                   | 670 ms: 1.35x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.96 ms: 1.36x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 18.2 ms: 1.36x slower                                                   |
| python_startup             | 13.3 ms                                                  | 18.1 ms: 1.36x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 12.2 ms: 1.39x slower                                                   |
| coverage                   | 98.5 ms                                                  | 138 ms: 1.40x slower                                                    |
| docutils                   | 2.91 sec                                                 | 4.12 sec: 1.42x slower                                                  |
| deepcopy_memo              | 51.0 us                                                  | 73.0 us: 1.43x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 41.1 ms: 1.46x slower                                                   |
| pylint                     | 343 ms                                                   | 509 ms: 1.48x slower                                                    |
| meteor_contest             | 113 ms                                                   | 168 ms: 1.48x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.10 us: 1.50x slower                                                   |
| generators                 | 37.8 ms                                                  | 57.2 ms: 1.51x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 152 ms: 1.54x slower                                                    |
| tornado_http               | 131 ms                                                   | 209 ms: 1.59x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.40 sec: 1.59x slower                                                  |
| pycparser                  | 1.26 sec                                                 | 2.06 sec: 1.63x slower                                                  |
| spectral_norm              | 141 ms                                                   | 231 ms: 1.64x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 131 ms: 1.64x slower                                                    |
| fannkuch                   | 452 ms                                                   | 746 ms: 1.65x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 2.11 ms: 1.66x slower                                                   |
| crypto_pyaes               | 82.7 ms                                                  | 139 ms: 1.68x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 35.2 ms: 1.68x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 4.28 sec: 1.69x slower                                                  |
| 2to3                       | 306 ms                                                   | 522 ms: 1.71x slower                                                    |
| thrift                     | 946 us                                                   | 1.67 ms: 1.76x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 344 us: 1.79x slower                                                    |
| sqlglot_normalize          | 128 ms                                                   | 232 ms: 1.81x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 109 ms: 1.81x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.01 sec: 1.82x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 117 ms: 1.88x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 123 ms: 1.91x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.78 sec: 1.92x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.66 sec: 1.93x slower                                                  |
| sympy_str                  | 264 ms                                                   | 523 ms: 1.98x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 55.1 ms: 1.99x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.6 us: 1.99x slower                                                   |
| django_template            | 42.3 ms                                                  | 84.1 ms: 1.99x slower                                                   |
| regex_compile              | 128 ms                                                   | 258 ms: 2.01x slower                                                    |
| comprehensions             | 20.4 us                                                  | 41.2 us: 2.02x slower                                                   |
| logging_simple             | 7.04 us                                                  | 14.5 us: 2.06x slower                                                   |
| sympy_expand               | 455 ms                                                   | 971 ms: 2.14x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 546 us: 2.14x slower                                                    |
| scimark_monte_carlo        | 83.8 ms                                                  | 180 ms: 2.15x slower                                                    |
| scimark_sor                | 159 ms                                                   | 342 ms: 2.15x slower                                                    |
| logging_silent             | 135 ns                                                   | 291 ns: 2.15x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| pickle_pure_python         | 359 us                                                   | 787 us: 2.19x slower                                                    |
| richards                   | 53.5 ms                                                  | 117 ms: 2.19x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.7 ms: 2.20x slower                                                   |
| float                      | 94.4 ms                                                  | 209 ms: 2.22x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 318 ms: 2.22x slower                                                    |
| chaos                      | 68.8 ms                                                  | 160 ms: 2.32x slower                                                    |
| richards_super             | 60.3 ms                                                  | 141 ms: 2.33x slower                                                    |
| nbody                      | 114 ms                                                   | 285 ms: 2.50x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 351 ms: 2.52x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.37 ms: 2.53x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.72 ms: 2.69x slower                                                   |
| go                         | 163 ms                                                   | 447 ms: 2.75x slower                                                    |
| raytrace                   | 298 ms                                                   | 820 ms: 2.75x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.7 ms: 3.30x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.59x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.41x

# Memory
- memory change: 1.16x