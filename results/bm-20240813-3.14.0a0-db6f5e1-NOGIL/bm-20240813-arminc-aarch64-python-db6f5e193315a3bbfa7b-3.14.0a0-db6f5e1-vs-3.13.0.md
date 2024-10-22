# Results vs. 3.13.0

- fork: python
- ref: db6f5e193315a3bbfa7b
- machine: linux-aarch64
- commit hash: db6f5e1
- commit date: 2024-08-13
- overall geometric mean: 1.59x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 306 ms                                                   | 517 ms: 1.69x slower                                                    |
| docutils       | 2.91 sec                                                 | 4.11 sec: 1.42x slower                                                  |
| html5lib       | 64.3 ms                                                  | 121 ms: 1.89x slower                                                    |
| tornado_http   | 131 ms                                                   | 208 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 656 ms                                                   | 675 ms: 1.03x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 872 ms: 1.18x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.59 sec: 1.19x slower                                                  |
| async_tree_memoization     | 626 ms                                                   | 746 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 917 ms: 1.20x slower                                                    |
| asyncio_tcp                | 568 ms                                                   | 684 ms: 1.21x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 565 ms: 1.21x slower                                                    |
| async_tree_none            | 493 ms                                                   | 608 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| async_generators           | 496 ms                                                   | 673 ms: 1.36x slower                                                    |
| coroutines                 | 28.2 ms                                                  | 40.0 ms: 1.42x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 94.4 ms                                                  | 212 ms: 2.24x slower                                                    |
| nbody          | 114 ms                                                   | 286 ms: 2.50x slower                                                    |
| Geometric mean | (ref)                                                    | 1.78x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.87 ms                                                  | 4.41 ms: 1.10x faster                                                   |
| regex_dna      | 246 ms                                                   | 249 ms: 1.01x slower                                                    |
| regex_v8       | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| regex_compile  | 128 ms                                                   | 258 ms: 2.01x slower                                                    |
| Geometric mean | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 147 ms                                                   | 159 ms: 1.09x slower                                                    |
| json_loads           | 31.4 us                                                  | 38.9 us: 1.24x slower                                                   |
| json_dumps           | 13.4 ms                                                  | 17.8 ms: 1.34x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.1 ms                                                  | 132 ms: 1.65x slower                                                    |
| tomli_loads          | 2.53 sec                                                 | 4.23 sec: 1.67x slower                                                  |
| unpickle_pure_python | 254 us                                                   | 543 us: 2.13x slower                                                    |
| pickle_pure_python   | 359 us                                                   | 782 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.48x slower                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                  | 18.1 ms: 1.37x slower                                                   |
| python_startup_no_site | 8.75 ms                                                  | 12.1 ms: 1.39x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.38x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.2 ms                                                  | 106 ms: 1.75x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 53.6 ms: 1.93x slower                                                   |
| django_template | 42.3 ms                                                  | 84.2 ms: 1.99x slower                                                   |
| mako            | 13.3 ms                                                  | 29.0 ms: 2.18x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.96x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240813-arminc-aarch64-python-db6f5e193315a3bbfa7b-3.14.0a0-db6f5e1 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 2.12 ms                                                  | 1.61 ms: 1.32x faster                                                   |
| gc_traversal               | 4.53 ms                                                  | 3.48 ms: 1.30x faster                                                   |
| regex_effbot               | 4.87 ms                                                  | 4.41 ms: 1.10x faster                                                   |
| bench_mp_pool              | 7.30 ms                                                  | 7.13 ms: 1.02x faster                                                   |
| regex_dna                  | 246 ms                                                   | 249 ms: 1.01x slower                                                    |
| asyncio_websockets         | 656 ms                                                   | 675 ms: 1.03x slower                                                    |
| regex_v8                   | 31.5 ms                                                  | 33.0 ms: 1.05x slower                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 695 ms: 1.07x slower                                                    |
| xml_etree_iterparse        | 147 ms                                                   | 159 ms: 1.09x slower                                                    |
| async_tree_cpu_io_mixed_tg | 736 ms                                                   | 872 ms: 1.18x slower                                                    |
| asyncio_tcp_ssl            | 2.18 sec                                                 | 2.59 sec: 1.19x slower                                                  |
| async_tree_memoization     | 626 ms                                                   | 746 ms: 1.19x slower                                                    |
| async_tree_cpu_io_mixed    | 764 ms                                                   | 917 ms: 1.20x slower                                                    |
| pathlib                    | 22.4 ms                                                  | 26.9 ms: 1.20x slower                                                   |
| asyncio_tcp                | 568 ms                                                   | 684 ms: 1.21x slower                                                    |
| async_tree_none_tg         | 467 ms                                                   | 565 ms: 1.21x slower                                                    |
| async_tree_none            | 493 ms                                                   | 608 ms: 1.23x slower                                                    |
| async_tree_io_tg           | 1.09 sec                                                 | 1.35 sec: 1.24x slower                                                  |
| json_loads                 | 31.4 us                                                  | 38.9 us: 1.24x slower                                                   |
| json                       | 5.61 ms                                                  | 7.00 ms: 1.25x slower                                                   |
| deepcopy                   | 451 us                                                   | 563 us: 1.25x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| mdp                        | 3.36 sec                                                 | 4.36 sec: 1.30x slower                                                  |
| scimark_fft                | 447 ms                                                   | 580 ms: 1.30x slower                                                    |
| telco                      | 9.73 ms                                                  | 12.9 ms: 1.33x slower                                                   |
| json_dumps                 | 13.4 ms                                                  | 17.8 ms: 1.34x slower                                                   |
| async_generators           | 496 ms                                                   | 673 ms: 1.36x slower                                                    |
| scimark_sparse_mat_mult    | 6.58 ms                                                  | 8.95 ms: 1.36x slower                                                   |
| python_startup             | 13.3 ms                                                  | 18.1 ms: 1.37x slower                                                   |
| python_startup_no_site     | 8.75 ms                                                  | 12.1 ms: 1.39x slower                                                   |
| coverage                   | 98.5 ms                                                  | 136 ms: 1.39x slower                                                    |
| deepcopy_memo              | 51.0 us                                                  | 72.2 us: 1.42x slower                                                   |
| docutils                   | 2.91 sec                                                 | 4.11 sec: 1.42x slower                                                  |
| coroutines                 | 28.2 ms                                                  | 40.0 ms: 1.42x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 162 ms: 1.43x slower                                                    |
| pylint                     | 343 ms                                                   | 510 ms: 1.49x slower                                                    |
| meteor_contest             | 113 ms                                                   | 169 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.08 us: 1.49x slower                                                   |
| generators                 | 37.8 ms                                                  | 57.1 ms: 1.51x slower                                                   |
| nqueens                    | 98.7 ms                                                  | 152 ms: 1.54x slower                                                    |
| tornado_http               | 131 ms                                                   | 208 ms: 1.58x slower                                                    |
| bpe_tokeniser              | 5.90 sec                                                 | 9.48 sec: 1.61x slower                                                  |
| pycparser                  | 1.26 sec                                                 | 2.05 sec: 1.62x slower                                                  |
| spectral_norm              | 141 ms                                                   | 233 ms: 1.65x slower                                                    |
| xml_etree_process          | 80.1 ms                                                  | 132 ms: 1.65x slower                                                    |
| crypto_pyaes               | 82.7 ms                                                  | 137 ms: 1.66x slower                                                    |
| fannkuch                   | 452 ms                                                   | 751 ms: 1.66x slower                                                    |
| sympy_integrate            | 21.0 ms                                                  | 35.0 ms: 1.67x slower                                                   |
| bench_thread_pool          | 1.28 ms                                                  | 2.13 ms: 1.67x slower                                                   |
| tomli_loads                | 2.53 sec                                                 | 4.23 sec: 1.67x slower                                                  |
| 2to3                       | 306 ms                                                   | 517 ms: 1.69x slower                                                    |
| genshi_xml                 | 60.2 ms                                                  | 106 ms: 1.75x slower                                                    |
| typing_runtime_protocols   | 192 us                                                   | 343 us: 1.79x slower                                                    |
| thrift                     | 946 us                                                   | 1.69 ms: 1.79x slower                                                   |
| sqlglot_normalize          | 128 ms                                                   | 235 ms: 1.83x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.84x slower                                                  |
| sqlglot_optimize           | 62.4 ms                                                  | 117 ms: 1.88x slower                                                    |
| html5lib                   | 64.3 ms                                                  | 121 ms: 1.89x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.78 sec: 1.92x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.66 sec: 1.93x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 53.6 ms: 1.93x slower                                                   |
| sympy_str                  | 264 ms                                                   | 521 ms: 1.97x slower                                                    |
| django_template            | 42.3 ms                                                  | 84.2 ms: 1.99x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.8 us: 2.00x slower                                                   |
| regex_compile              | 128 ms                                                   | 258 ms: 2.01x slower                                                    |
| logging_format             | 7.83 us                                                  | 16.1 us: 2.06x slower                                                   |
| scimark_monte_carlo        | 83.8 ms                                                  | 177 ms: 2.11x slower                                                    |
| logging_simple             | 7.04 us                                                  | 14.8 us: 2.11x slower                                                   |
| logging_silent             | 135 ns                                                   | 286 ns: 2.12x slower                                                    |
| sympy_expand               | 455 ms                                                   | 964 ms: 2.12x slower                                                    |
| unpickle_pure_python       | 254 us                                                   | 543 us: 2.13x slower                                                    |
| scimark_sor                | 159 ms                                                   | 339 ms: 2.13x slower                                                    |
| pickle_pure_python         | 359 us                                                   | 782 us: 2.18x slower                                                    |
| mako                       | 13.3 ms                                                  | 29.0 ms: 2.18x slower                                                   |
| sympy_sum                  | 143 ms                                                   | 317 ms: 2.21x slower                                                    |
| richards                   | 53.5 ms                                                  | 118 ms: 2.21x slower                                                    |
| hexiom                     | 7.13 ms                                                  | 15.8 ms: 2.21x slower                                                   |
| float                      | 94.4 ms                                                  | 212 ms: 2.24x slower                                                    |
| chaos                      | 68.8 ms                                                  | 159 ms: 2.31x slower                                                    |
| richards_super             | 60.3 ms                                                  | 139 ms: 2.31x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.27 ms: 2.47x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 347 ms: 2.49x slower                                                    |
| nbody                      | 114 ms                                                   | 286 ms: 2.50x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.71 ms: 2.69x slower                                                   |
| go                         | 163 ms                                                   | 445 ms: 2.74x slower                                                    |
| raytrace                   | 298 ms                                                   | 816 ms: 2.74x slower                                                    |
| deltablue                  | 3.85 ms                                                  | 12.7 ms: 3.29x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.59x slower                                                            |

Benchmark hidden because not significant (2): xml_etree_parse, pidigits
Ignored benchmarks (13) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.50x
- 95% likely to have a slowdown of 1.46x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.17x