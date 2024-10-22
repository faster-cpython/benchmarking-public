# Results vs. 3.13.0

- fork: python
- ref: 52caaef6d01a94962576
- machine: linux-aarch64
- commit hash: 52caaef
- commit date: 2024-08-24
- overall geometric mean: 1.59x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.39x slower
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 521 ms: 1.70x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.04 sec: 1.39x slower                                                  |
| html5lib       | 64.3 ms                                                  | 122 ms: 1.90x slower                                                    |
| tornado_http   | 131 ms                                                   | 204 ms: 1.55x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 642 ms: 1.13x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 738 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 877 ms: 1.19x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 570 ms: 1.22x slower                                                    |
| async_tree_none            | 493 ms                                                   | 606 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.37 sec: 1.25x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| async_generators           | 496 ms                                                   | 665 ms: 1.34x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 41.3 ms: 1.46x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 209 ms: 2.21x slower                                                    |
| nbody          | 114 ms                                                   | 282 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                    | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| regex_v8       | 31.5 ms                                                  | 32.8 ms: 1.04x slower                                                   |
| regex_dna      | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| regex_compile  | 128 ms                                                   | 260 ms: 2.02x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                   | 160 ms: 1.09x slower                                                    |
| json_loads           | 31.4 us                                                  | 39.5 us: 1.26x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 18.3 ms: 1.37x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 131 ms: 1.64x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 548 us: 2.15x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 776 us: 2.16x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.48x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.0 ms: 1.35x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.37x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 105 ms: 1.75x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 53.4 ms: 1.93x slower                                                   |
| django_template | 42.3 ms                                                  | 84.2 ms: 1.99x slower                                                   |
| mako            | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240824-arminc-aarch64-python-52caaef6d01a94962576-3.14.0a0-52caaef |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.64 ms: 1.30x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.50 ms: 1.29x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 6.96 ms: 1.05x faster                                                   |
| xml_etree_parse            | 188 ms                                                   | 184 ms: 1.02x faster                                                    |
| asyncio_websockets         | 656 ms                                                   | 672 ms: 1.03x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 32.8 ms: 1.04x slower                                                   |
| regex_dna                  | 246 ms                                                   | 258 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 160 ms: 1.09x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.46 sec: 1.13x slower                                                  |
| asyncio_tcp                | 568 ms                                                   | 642 ms: 1.13x slower                                                    |
| async_tree_memoization     | 626 ms                                                   | 738 ms: 1.18x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 908 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 877 ms: 1.19x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.8 ms: 1.20x slower                                                   |
| async_tree_none_tg         | 467 ms                                                   | 570 ms: 1.22x slower                                                    |
| async_tree_none            | 493 ms                                                   | 606 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.37 sec: 1.25x slower                                                  |
| deepcopy                   | 451 us                                                   | 566 us: 1.25x slower                                                    |
| json_loads                 | 31.4 us                                                  | 39.5 us: 1.26x slower                                                   |
| json                       | 5.61 ms                                                  | 7.12 ms: 1.27x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| scimark_fft                | 447 ms                                                   | 576 ms: 1.29x slower                                                    |
| mdp                        | 3.36 sec                                                 | 4.34 sec: 1.29x slower                                                  |
| async_generators           | 496 ms                                                   | 665 ms: 1.34x slower                                                    |
| telco                      | 9.73 ms                                                  | 13.2 ms: 1.35x slower                                                   |
| python_startup             | 13.3 ms                                                  | 18.0 ms: 1.35x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 18.3 ms: 1.37x slower                                                   |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 9.03 ms: 1.37x slower                                                   |
| coverage                   | 98.5 ms                                                  | 136 ms: 1.38x slower                                                    |
| python_startup_no_site     | 8.75 ms                                                  | 12.1 ms: 1.38x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.04 sec: 1.39x slower                                                  |
| deepcopy_memo              | 51.0 us                                                  | 72.2 us: 1.42x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 41.3 ms: 1.46x slower                                                   |
| meteor_contest             | 113 ms                                                   | 167 ms: 1.47x slower                                                    |
| pylint                     | 343 ms                                                   | 509 ms: 1.48x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.08 us: 1.50x slower                                                   |
| generators                 | 37.8 ms                                                  | 57.4 ms: 1.52x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 153 ms: 1.55x slower                                                    |
| tornado_http               | 131 ms                                                   | 204 ms: 1.55x slower                                                    |
| pycparser                  | 1.26 sec                                                 | 2.03 sec: 1.60x slower                                                  |
| bpe_tokeniser              | 5.90 sec                                                 | 9.54 sec: 1.62x slower                                                  |
| xml_etree_process          | 80.1 ms                                                  | 131 ms: 1.64x slower                                                    |
| fannkuch                   | 452 ms                                                   | 740 ms: 1.64x slower                                                    |
| bench_thread_pool          | 1.28 ms                                                  | 2.10 ms: 1.65x slower                                                   |
| spectral_norm              | 141 ms                                                   | 233 ms: 1.65x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 34.7 ms: 1.66x slower                                                   |
| crypto_pyaes               | 82.7 ms                                                  | 137 ms: 1.66x slower                                                    |
| tomli_loads                | 2.53 sec                                                 | 4.20 sec: 1.66x slower                                                  |
| 2to3                       | 306 ms                                                   | 521 ms: 1.70x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 105 ms: 1.75x slower                                                    |
| thrift                     | 946 us                                                   | 1.66 ms: 1.75x slower                                                   |
| typing_runtime_protocols   | 192 us                                                   | 339 us: 1.77x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.01 sec: 1.82x slower                                                  |
| sqlglot_normalize          | 128 ms                                                   | 234 ms: 1.83x slower                                                    |
| sqlglot_optimize           | 62.4 ms                                                  | 117 ms: 1.87x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 122 ms: 1.90x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.78 sec: 1.92x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 53.4 ms: 1.93x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 3.66 sec: 1.93x slower                                                  |
| sympy_str                  | 264 ms                                                   | 514 ms: 1.95x slower                                                    |
| django_template            | 42.3 ms                                                  | 84.2 ms: 1.99x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.7 us: 1.99x slower                                                   |
| logging_format             | 7.83 us                                                  | 15.7 us: 2.00x slower                                                   |
| regex_compile              | 128 ms                                                   | 260 ms: 2.02x slower                                                    |
| logging_simple             | 7.04 us                                                  | 14.5 us: 2.05x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 174 ms: 2.07x slower                                                    |
| logging_silent             | 135 ns                                                   | 287 ns: 2.12x slower                                                    |
| sympy_expand               | 455 ms                                                   | 969 ms: 2.13x slower                                                    |
| scimark_sor                | 159 ms                                                   | 342 ms: 2.15x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 548 us: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 776 us: 2.16x slower                                                    |
| mako                       | 13.3 ms                                                  | 28.9 ms: 2.17x slower                                                   |
| richards                   | 53.5 ms                                                  | 118 ms: 2.20x slower                                                    |
| sympy_sum                  | 143 ms                                                   | 315 ms: 2.20x slower                                                    |
| float                      | 94.4 ms                                                  | 209 ms: 2.21x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.9 ms: 2.23x slower                                                   |
| richards_super             | 60.3 ms                                                  | 138 ms: 2.28x slower                                                    |
| chaos                      | 68.8 ms                                                  | 159 ms: 2.32x slower                                                    |
| nbody                      | 114 ms                                                   | 282 ms: 2.47x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.30 ms: 2.48x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 355 ms: 2.55x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.70 ms: 2.68x slower                                                   |
| go                         | 163 ms                                                   | 443 ms: 2.72x slower                                                    |
| raytrace                   | 298 ms                                                   | 817 ms: 2.74x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.8 ms: 3.34x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.59x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.49x
- 95% likely to have a slowdown of 1.45x
- 99% likely to have a slowdown of 1.39x

# Memory
- memory change: 1.18x