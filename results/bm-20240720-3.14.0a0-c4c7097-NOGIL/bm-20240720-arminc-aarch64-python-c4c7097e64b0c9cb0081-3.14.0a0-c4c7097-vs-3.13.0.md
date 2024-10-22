# Results vs. 3.13.0

- fork: python
- ref: c4c7097e64b0c9cb0081
- machine: linux-aarch64
- commit hash: c4c7097
- commit date: 2024-07-20
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 513 ms: 1.68x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.11 sec: 1.42x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| tornado_http   | 131 ms                                                   | 207 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 688 ms: 1.06x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 859 ms: 1.17x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 671 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 912 ms: 1.19x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 560 ms: 1.20x slower                                                    |
| async_tree_none            | 493 ms                                                   | 604 ms: 1.22x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 38.5 ms: 1.36x slower                                                   |
| async_generators           | 496 ms                                                   | 686 ms: 1.38x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 209 ms: 2.22x slower                                                    |
| nbody          | 114 ms                                                   | 290 ms: 2.54x slower                                                    |
| Geometric mean | (ref)                                                    | 1.78x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.43 ms: 1.10x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 32.6 ms: 1.03x slower                                                   |
| regex_dna      | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| regex_compile  | 128 ms                                                   | 254 ms: 1.98x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| json_loads           | 31.4 us                                                  | 38.8 us: 1.23x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.7 ms: 1.33x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 157 ms: 1.39x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 130 ms: 1.62x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 538 us: 2.12x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 773 us: 2.15x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 17.6 ms: 1.33x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 11.8 ms: 1.35x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.34x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 52.2 ms: 1.88x slower                                                   |
| django_template | 42.3 ms                                                  | 81.3 ms: 1.92x slower                                                   |
| mako            | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.92x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.60 ms: 1.33x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.45 ms: 1.31x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.23 ms: 1.17x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.43 ms: 1.10x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 182 ms: 1.03x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 32.6 ms: 1.03x slower                                                   |
| regex_dna                  | 246 ms                                                   | 256 ms: 1.04x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 688 ms: 1.06x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 859 ms: 1.17x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 739 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 671 ms: 1.18x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.6 ms: 1.19x slower                                                   |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 912 ms: 1.19x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 560 ms: 1.20x slower                                                    |
| deepcopy                   | 451 us                                                   | 553 us: 1.22x slower                                                    |
| async_tree_none            | 493 ms                                                   | 604 ms: 1.22x slower                                                    |
| json_loads                 | 31.4 us                                                  | 38.8 us: 1.23x slower                                                   |
| json                       | 5.61 ms                                                  | 6.97 ms: 1.24x slower                                                   |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| telco                      | 9.73 ms                                                  | 12.5 ms: 1.29x slower                                                   |
| mdp                        | 3.36 sec                                                 | 4.38 sec: 1.30x slower                                                  |
| json_dumps                 | 13.4 ms                                                  | 17.7 ms: 1.33x slower                                                   |
| python_startup             | 13.3 ms                                                  | 17.6 ms: 1.33x slower                                                   |
| coverage                   | 98.5 ms                                                  | 132 ms: 1.34x slower                                                    |
| scimark_fft                | 447 ms                                                   | 599 ms: 1.34x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 11.8 ms: 1.35x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.92 ms: 1.36x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 38.5 ms: 1.36x slower                                                   |
| async_generators           | 496 ms                                                   | 686 ms: 1.38x slower                                                    |
| xml_etree_generate         | 113 ms                                                   | 157 ms: 1.39x slower                                                    |
| docutils                   | 2.91 sec                                                 | 4.11 sec: 1.42x slower                                                  |
| deepcopy_memo              | 51.0 us                                                  | 72.8 us: 1.43x slower                                                   |
| pylint                     | 343 ms                                                   | 502 ms: 1.46x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 1.87 ms: 1.47x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.99 us: 1.47x slower                                                   |
| meteor_contest             | 113 ms                                                   | 172 ms: 1.51x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 149 ms: 1.51x slower                                                    |
| generators                 | 37.8 ms                                                  | 57.7 ms: 1.53x slower                                                   |
| tornado_http               | 131 ms                                                   | 207 ms: 1.58x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 130 ms: 1.62x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.57 sec: 1.62x slower                                                  |
| pycparser                  | 1.26 sec                                                 | 2.06 sec: 1.63x slower                                                  |
| fannkuch                   | 452 ms                                                   | 740 ms: 1.64x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| sympy_integrate            | 21.0 ms                                                  | 35.1 ms: 1.67x slower                                                   |
| 2to3                       | 306 ms                                                   | 513 ms: 1.68x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 140 ms: 1.69x slower                                                    |
| spectral_norm              | 141 ms                                                   | 239 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 332 us: 1.73x slower                                                    |
| thrift                     | 946 us                                                   | 1.65 ms: 1.75x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 231 ms: 1.80x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.01 sec: 1.82x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 117 ms: 1.88x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.74 sec: 1.88x slower                                                  |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 52.2 ms: 1.88x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.59 sec: 1.89x slower                                                  |
| django_template            | 42.3 ms                                                  | 81.3 ms: 1.92x slower                                                   |
| sympy_str                  | 264 ms                                                   | 520 ms: 1.97x slower                                                    |
| regex_compile              | 128 ms                                                   | 254 ms: 1.98x slower                                                    |
| comprehensions             | 20.4 us                                                  | 40.5 us: 1.99x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.7 us: 2.01x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 172 ms: 2.05x slower                                                    |
| logging_silent             | 135 ns                                                   | 281 ns: 2.08x slower                                                    |
| logging_simple             | 7.04 us                                                  | 14.7 us: 2.09x slower                                                   |
| sympy_expand               | 455 ms                                                   | 953 ms: 2.10x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 538 us: 2.12x slower                                                    |
| scimark_sor                | 159 ms                                                   | 341 ms: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 773 us: 2.15x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| richards                   | 53.5 ms                                                  | 117 ms: 2.18x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.6 ms: 2.18x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 317 ms: 2.21x slower                                                    |
| float                      | 94.4 ms                                                  | 209 ms: 2.22x slower                                                    |
| richards_super             | 60.3 ms                                                  | 137 ms: 2.27x slower                                                    |
| chaos                      | 68.8 ms                                                  | 161 ms: 2.33x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 348 ms: 2.50x slower                                                    |
| nbody                      | 114 ms                                                   | 290 ms: 2.54x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.41 ms: 2.54x slower                                                   |
| go                         | 163 ms                                                   | 446 ms: 2.74x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.83 ms: 2.77x slower                                                   |
| raytrace                   | 298 ms                                                   | 829 ms: 2.78x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.7 ms: 3.31x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240720-3.14.0a0-c4c7097-NOGIL/bm-20240720-arminc-aarch64-python-c4c7097e64b0c9cb0081-3.14.0a0-c4c7097.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.17x