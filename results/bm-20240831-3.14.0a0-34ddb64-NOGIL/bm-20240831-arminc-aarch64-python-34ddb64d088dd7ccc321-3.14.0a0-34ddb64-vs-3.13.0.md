# Results vs. 3.13.0

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.58x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 518 ms: 1.69x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.08 sec: 1.40x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| tornado_http   | 131 ms                                                   | 208 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 675 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 731 ms: 1.17x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.56 sec: 1.18x slower                                                  |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 869 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 673 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 570 ms: 1.22x slower                                                    |
| async_tree_none            | 493 ms                                                   | 606 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| async_generators           | 496 ms                                                   | 652 ms: 1.31x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 40.6 ms: 1.44x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 206 ms: 2.19x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                    | 1.75x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.46 ms: 1.09x faster                                                   |
| regex_dna      | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| regex_v8       | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                   | 257 ms: 2.00x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| json_loads           | 31.4 us                                                  | 38.6 us: 1.23x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 18.2 ms: 1.36x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 132 ms: 1.64x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.22 sec: 1.67x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 546 us: 2.14x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 773 us: 2.15x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.47x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.2 ms: 1.37x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.3 ms: 1.40x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.39x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 52.9 ms: 1.91x slower                                                   |
| django_template | 42.3 ms                                                  | 82.7 ms: 1.96x slower                                                   |
| mako            | 13.3 ms                                                  | 28.7 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.93x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.62 ms: 1.31x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.50 ms: 1.29x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.46 ms: 1.09x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 185 ms: 1.01x faster                                                    |
| regex_dna                  | 246 ms                                                   | 253 ms: 1.03x slower                                                    |
| bench_mp_pool              | 7.30 ms                                                  | 7.51 ms: 1.03x slower                                                   |
| asyncio_websockets         | 656 ms                                                   | 675 ms: 1.03x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| xml_etree_iterparse        | 147 ms                                                   | 156 ms: 1.07x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 731 ms: 1.17x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.56 sec: 1.18x slower                                                  |
| pathlib                    | 22.4 ms                                                  | 26.4 ms: 1.18x slower                                                   |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 869 ms: 1.18x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 673 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 570 ms: 1.22x slower                                                    |
| json_loads                 | 31.4 us                                                  | 38.6 us: 1.23x slower                                                   |
| async_tree_none            | 493 ms                                                   | 606 ms: 1.23x slower                                                    |
| json                       | 5.61 ms                                                  | 6.93 ms: 1.23x slower                                                   |
| deepcopy                   | 451 us                                                   | 557 us: 1.24x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.36 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.39 sec: 1.26x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.33 sec: 1.29x slower                                                  |
| scimark_fft                | 447 ms                                                   | 576 ms: 1.29x slower                                                    |
| telco                      | 9.73 ms                                                  | 12.8 ms: 1.31x slower                                                   |
| async_generators           | 496 ms                                                   | 652 ms: 1.31x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.94 ms: 1.36x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 18.2 ms: 1.36x slower                                                   |
| coverage                   | 98.5 ms                                                  | 135 ms: 1.37x slower                                                    |
| python_startup             | 13.3 ms                                                  | 18.2 ms: 1.37x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 12.3 ms: 1.40x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.08 sec: 1.40x slower                                                  |
| deepcopy_memo              | 51.0 us                                                  | 72.3 us: 1.42x slower                                                   |
| coroutines                 | 28.2 ms                                                  | 40.6 ms: 1.44x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 5.94 us: 1.46x slower                                                   |
| meteor_contest             | 113 ms                                                   | 168 ms: 1.48x slower                                                    |
| pylint                     | 343 ms                                                   | 514 ms: 1.50x slower                                                    |
| nqueens                    | 98.7 ms                                                  | 151 ms: 1.53x slower                                                    |
| generators                 | 37.8 ms                                                  | 58.4 ms: 1.54x slower                                                   |
| tornado_http               | 131 ms                                                   | 208 ms: 1.58x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.42 sec: 1.60x slower                                                  |
| pycparser                  | 1.26 sec                                                 | 2.03 sec: 1.61x slower                                                  |
| fannkuch                   | 452 ms                                                   | 736 ms: 1.63x slower                                                    |
| spectral_norm              | 141 ms                                                   | 231 ms: 1.64x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 132 ms: 1.64x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 34.8 ms: 1.66x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 2.13 ms: 1.67x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 4.22 sec: 1.67x slower                                                  |
| crypto_pyaes               | 82.7 ms                                                  | 139 ms: 1.68x slower                                                    |
| 2to3                       | 306 ms                                                   | 518 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 104 ms: 1.72x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 337 us: 1.76x slower                                                    |
| thrift                     | 946 us                                                   | 1.67 ms: 1.77x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 234 ms: 1.82x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 116 ms: 1.86x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.88x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.76 sec: 1.90x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 52.9 ms: 1.91x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.63 sec: 1.91x slower                                                  |
| sympy_str                  | 264 ms                                                   | 516 ms: 1.96x slower                                                    |
| django_template            | 42.3 ms                                                  | 82.7 ms: 1.96x slower                                                   |
| regex_compile              | 128 ms                                                   | 257 ms: 2.00x slower                                                    |
| comprehensions             | 20.4 us                                                  | 40.9 us: 2.00x slower                                                   |
| logging_format             | 7.83 us                                                  | 16.1 us: 2.05x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 174 ms: 2.07x slower                                                    |
| sympy_expand               | 455 ms                                                   | 959 ms: 2.11x slower                                                    |
| logging_simple             | 7.04 us                                                  | 14.9 us: 2.12x slower                                                   |
| logging_silent             | 135 ns                                                   | 287 ns: 2.12x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 546 us: 2.14x slower                                                    |
| scimark_sor                | 159 ms                                                   | 342 ms: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 773 us: 2.15x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.7 ms: 2.16x slower                                                   |
| richards                   | 53.5 ms                                                  | 117 ms: 2.18x slower                                                    |
| float                      | 94.4 ms                                                  | 206 ms: 2.19x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 317 ms: 2.21x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.8 ms: 2.22x slower                                                   |
| richards_super             | 60.3 ms                                                  | 138 ms: 2.28x slower                                                    |
| chaos                      | 68.8 ms                                                  | 159 ms: 2.31x slower                                                    |
| go                         | 163 ms                                                   | 389 ms: 2.39x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.27 ms: 2.47x slower                                                   |
| nbody                      | 114 ms                                                   | 281 ms: 2.47x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 353 ms: 2.54x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.65 ms: 2.64x slower                                                   |
| raytrace                   | 298 ms                                                   | 812 ms: 2.73x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.8 ms: 3.32x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.58x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (1) of results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: dulwich_log

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.17x