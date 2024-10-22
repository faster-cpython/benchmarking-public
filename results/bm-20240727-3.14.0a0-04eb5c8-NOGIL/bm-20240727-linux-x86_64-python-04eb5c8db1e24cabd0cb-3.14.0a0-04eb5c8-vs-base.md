# Results vs. base

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-x86_64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.47x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                                                          | 394 ms: 1.49x slower                                                                                                  |
| docutils       | 2.74 sec                                                                                                        | 3.35 sec: 1.22x slower                                                                                                |
| html5lib       | 65.6 ms                                                                                                         | 97.3 ms: 1.48x slower                                                                                                 |
| tornado_http   | 90.9 ms                                                                                                         | 136 ms: 1.49x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.42x slower                                                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| async_tree_io_tg           | 860 ms                                                                                                          | 845 ms: 1.02x faster                                                                                                  |
| asyncio_websockets         | 560 ms                                                                                                          | 554 ms: 1.01x faster                                                                                                  |
| async_tree_cpu_io_mixed_tg | 530 ms                                                                                                          | 597 ms: 1.13x slower                                                                                                  |
| async_tree_none_tg         | 299 ms                                                                                                          | 346 ms: 1.16x slower                                                                                                  |
| async_tree_memoization_tg  | 391 ms                                                                                                          | 453 ms: 1.16x slower                                                                                                  |
| asyncio_tcp                | 487 ms                                                                                                          | 567 ms: 1.16x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                        | 2.08 sec: 1.16x slower                                                                                                |
| async_tree_cpu_io_mixed    | 562 ms                                                                                                          | 662 ms: 1.18x slower                                                                                                  |
| async_tree_memoization     | 409 ms                                                                                                          | 510 ms: 1.25x slower                                                                                                  |
| async_tree_none            | 323 ms                                                                                                          | 406 ms: 1.26x slower                                                                                                  |
| async_generators           | 437 ms                                                                                                          | 565 ms: 1.29x slower                                                                                                  |
| coroutines                 | 22.6 ms                                                                                                         | 31.2 ms: 1.38x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                           | 1.16x slower                                                                                                          |

Benchmark hidden because not significant (1): async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                                                          | 184 ms: 1.02x faster                                                                                                  |
| float          | 78.1 ms                                                                                                         | 142 ms: 1.81x slower                                                                                                  |
| nbody          | 89.0 ms                                                                                                         | 217 ms: 2.44x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.63x slower                                                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 3.67 ms                                                                                                         | 3.56 ms: 1.03x faster                                                                                                 |
| regex_dna      | 226 ms                                                                                                          | 221 ms: 1.02x faster                                                                                                  |
| regex_v8       | 24.6 ms                                                                                                         | 26.8 ms: 1.09x slower                                                                                                 |
| regex_compile  | 131 ms                                                                                                          | 217 ms: 1.66x slower                                                                                                  |
| Geometric mean | (ref)                                                                                                           | 1.14x slower                                                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| xml_etree_parse      | 154 ms                                                                                                          | 142 ms: 1.08x faster                                                                                                  |
| xml_etree_iterparse  | 105 ms                                                                                                          | 111 ms: 1.06x slower                                                                                                  |
| json_loads           | 27.6 us                                                                                                         | 32.2 us: 1.17x slower                                                                                                 |
| xml_etree_generate   | 87.0 ms                                                                                                         | 111 ms: 1.27x slower                                                                                                  |
| json_dumps           | 10.4 ms                                                                                                         | 13.4 ms: 1.29x slower                                                                                                 |
| xml_etree_process    | 60.2 ms                                                                                                         | 89.5 ms: 1.49x slower                                                                                                 |
| tomli_loads          | 2.03 sec                                                                                                        | 3.22 sec: 1.58x slower                                                                                                |
| pickle_pure_python   | 306 us                                                                                                          | 571 us: 1.86x slower                                                                                                  |
| unpickle_pure_python | 212 us                                                                                                          | 399 us: 1.88x slower                                                                                                  |
| Geometric mean       | (ref)                                                                                                           | 1.36x slower                                                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 10.5 ms                                                                                                         | 13.4 ms: 1.27x slower                                                                                                 |
| python_startup_no_site | 7.10 ms                                                                                                         | 9.08 ms: 1.28x slower                                                                                                 |
| Geometric mean         | (ref)                                                                                                           | 1.28x slower                                                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|-----------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 52.4 ms                                                                                                         | 83.9 ms: 1.60x slower                                                                                                 |
| genshi_text     | 23.7 ms                                                                                                         | 40.2 ms: 1.70x slower                                                                                                 |
| django_template | 34.5 ms                                                                                                         | 60.9 ms: 1.77x slower                                                                                                 |
| mako            | 11.0 ms                                                                                                         | 21.1 ms: 1.91x slower                                                                                                 |
| Geometric mean  | (ref)                                                                                                           | 1.74x slower                                                                                                          |

All benchmarks:
===============

| Benchmark                  | results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json | results/bm-20240727-3.14.0a0-04eb5c8-NOGIL/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json |
|----------------------------|:---------------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 3.75 ms                                                                                                         | 2.89 ms: 1.29x faster                                                                                                 |
| create_gc_cycles           | 1.74 ms                                                                                                         | 1.37 ms: 1.27x faster                                                                                                 |
| xml_etree_parse            | 154 ms                                                                                                          | 142 ms: 1.08x faster                                                                                                  |
| regex_effbot               | 3.67 ms                                                                                                         | 3.56 ms: 1.03x faster                                                                                                 |
| regex_dna                  | 226 ms                                                                                                          | 221 ms: 1.02x faster                                                                                                  |
| async_tree_io_tg           | 860 ms                                                                                                          | 845 ms: 1.02x faster                                                                                                  |
| pidigits                   | 187 ms                                                                                                          | 184 ms: 1.02x faster                                                                                                  |
| asyncio_websockets         | 560 ms                                                                                                          | 554 ms: 1.01x faster                                                                                                  |
| bench_mp_pool              | 24.0 ms                                                                                                         | 23.9 ms: 1.00x faster                                                                                                 |
| xml_etree_iterparse        | 105 ms                                                                                                          | 111 ms: 1.06x slower                                                                                                  |
| regex_v8                   | 24.6 ms                                                                                                         | 26.8 ms: 1.09x slower                                                                                                 |
| async_tree_cpu_io_mixed_tg | 530 ms                                                                                                          | 597 ms: 1.13x slower                                                                                                  |
| async_tree_none_tg         | 299 ms                                                                                                          | 346 ms: 1.16x slower                                                                                                  |
| async_tree_memoization_tg  | 391 ms                                                                                                          | 453 ms: 1.16x slower                                                                                                  |
| json                       | 5.17 ms                                                                                                         | 5.99 ms: 1.16x slower                                                                                                 |
| asyncio_tcp                | 487 ms                                                                                                          | 567 ms: 1.16x slower                                                                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                                                                                        | 2.08 sec: 1.16x slower                                                                                                |
| json_loads                 | 27.6 us                                                                                                         | 32.2 us: 1.17x slower                                                                                                 |
| async_tree_cpu_io_mixed    | 562 ms                                                                                                          | 662 ms: 1.18x slower                                                                                                  |
| pathlib                    | 15.7 ms                                                                                                         | 19.2 ms: 1.22x slower                                                                                                 |
| docutils                   | 2.74 sec                                                                                                        | 3.35 sec: 1.22x slower                                                                                                |
| telco                      | 8.10 ms                                                                                                         | 10.0 ms: 1.24x slower                                                                                                 |
| pylint                     | 318 ms                                                                                                          | 394 ms: 1.24x slower                                                                                                  |
| async_tree_memoization     | 409 ms                                                                                                          | 510 ms: 1.25x slower                                                                                                  |
| async_tree_none            | 323 ms                                                                                                          | 406 ms: 1.26x slower                                                                                                  |
| python_startup             | 10.5 ms                                                                                                         | 13.4 ms: 1.27x slower                                                                                                 |
| xml_etree_generate         | 87.0 ms                                                                                                         | 111 ms: 1.27x slower                                                                                                  |
| python_startup_no_site     | 7.10 ms                                                                                                         | 9.08 ms: 1.28x slower                                                                                                 |
| json_dumps                 | 10.4 ms                                                                                                         | 13.4 ms: 1.29x slower                                                                                                 |
| coverage                   | 85.4 ms                                                                                                         | 110 ms: 1.29x slower                                                                                                  |
| async_generators           | 437 ms                                                                                                          | 565 ms: 1.29x slower                                                                                                  |
| generators                 | 28.5 ms                                                                                                         | 38.0 ms: 1.33x slower                                                                                                 |
| mdp                        | 2.52 sec                                                                                                        | 3.37 sec: 1.34x slower                                                                                                |
| scimark_fft                | 351 ms                                                                                                          | 475 ms: 1.35x slower                                                                                                  |
| bpe_tokeniser              | 4.86 sec                                                                                                        | 6.61 sec: 1.36x slower                                                                                                |
| meteor_contest             | 108 ms                                                                                                          | 148 ms: 1.37x slower                                                                                                  |
| coroutines                 | 22.6 ms                                                                                                         | 31.2 ms: 1.38x slower                                                                                                 |
| scimark_sparse_mat_mult    | 4.62 ms                                                                                                         | 6.63 ms: 1.43x slower                                                                                                 |
| pycparser                  | 1.13 sec                                                                                                        | 1.64 sec: 1.44x slower                                                                                                |
| sympy_integrate            | 19.8 ms                                                                                                         | 28.7 ms: 1.45x slower                                                                                                 |
| html5lib                   | 65.6 ms                                                                                                         | 97.3 ms: 1.48x slower                                                                                                 |
| xml_etree_process          | 60.2 ms                                                                                                         | 89.5 ms: 1.49x slower                                                                                                 |
| 2to3                       | 264 ms                                                                                                          | 394 ms: 1.49x slower                                                                                                  |
| tornado_http               | 90.9 ms                                                                                                         | 136 ms: 1.49x slower                                                                                                  |
| nqueens                    | 79.8 ms                                                                                                         | 119 ms: 1.50x slower                                                                                                  |
| fannkuch                   | 405 ms                                                                                                          | 608 ms: 1.50x slower                                                                                                  |
| crypto_pyaes               | 73.6 ms                                                                                                         | 112 ms: 1.52x slower                                                                                                  |
| typing_runtime_protocols   | 166 us                                                                                                          | 254 us: 1.53x slower                                                                                                  |
| sympy_str                  | 274 ms                                                                                                          | 424 ms: 1.55x slower                                                                                                  |
| tomli_loads                | 2.03 sec                                                                                                        | 3.22 sec: 1.58x slower                                                                                                |
| deepcopy                   | 267 us                                                                                                          | 423 us: 1.58x slower                                                                                                  |
| genshi_xml                 | 52.4 ms                                                                                                         | 83.9 ms: 1.60x slower                                                                                                 |
| deepcopy_reduce            | 2.76 us                                                                                                         | 4.42 us: 1.60x slower                                                                                                 |
| thrift                     | 777 us                                                                                                          | 1.25 ms: 1.61x slower                                                                                                 |
| sympy_expand               | 464 ms                                                                                                          | 753 ms: 1.62x slower                                                                                                  |
| spectral_norm              | 113 ms                                                                                                          | 186 ms: 1.64x slower                                                                                                  |
| pyflate                    | 470 ms                                                                                                          | 777 ms: 1.65x slower                                                                                                  |
| regex_compile              | 131 ms                                                                                                          | 217 ms: 1.66x slower                                                                                                  |
| sqlglot_normalize          | 106 ms                                                                                                          | 177 ms: 1.66x slower                                                                                                  |
| sqlglot_optimize           | 53.2 ms                                                                                                         | 88.8 ms: 1.67x slower                                                                                                 |
| sympy_sum                  | 152 ms                                                                                                          | 254 ms: 1.67x slower                                                                                                  |
| genshi_text                | 23.7 ms                                                                                                         | 40.2 ms: 1.70x slower                                                                                                 |
| richards                   | 45.9 ms                                                                                                         | 78.0 ms: 1.70x slower                                                                                                 |
| comprehensions             | 16.6 us                                                                                                         | 28.7 us: 1.73x slower                                                                                                 |
| pprint_safe_repr           | 748 ms                                                                                                          | 1.32 sec: 1.76x slower                                                                                                |
| django_template            | 34.5 ms                                                                                                         | 60.9 ms: 1.77x slower                                                                                                 |
| pprint_pformat             | 1.54 sec                                                                                                        | 2.72 sec: 1.77x slower                                                                                                |
| logging_silent             | 104 ns                                                                                                          | 185 ns: 1.78x slower                                                                                                  |
| deepcopy_memo              | 29.4 us                                                                                                         | 52.3 us: 1.78x slower                                                                                                 |
| scimark_monte_carlo        | 68.6 ms                                                                                                         | 124 ms: 1.80x slower                                                                                                  |
| float                      | 78.1 ms                                                                                                         | 142 ms: 1.81x slower                                                                                                  |
| richards_super             | 51.8 ms                                                                                                         | 94.6 ms: 1.82x slower                                                                                                 |
| pickle_pure_python         | 306 us                                                                                                          | 571 us: 1.86x slower                                                                                                  |
| unpickle_pure_python       | 212 us                                                                                                          | 399 us: 1.88x slower                                                                                                  |
| mako                       | 11.0 ms                                                                                                         | 21.1 ms: 1.91x slower                                                                                                 |
| hexiom                     | 6.22 ms                                                                                                         | 12.0 ms: 1.94x slower                                                                                                 |
| logging_simple             | 5.49 us                                                                                                         | 10.7 us: 1.94x slower                                                                                                 |
| logging_format             | 6.17 us                                                                                                         | 12.0 us: 1.94x slower                                                                                                 |
| sqlglot_transpile          | 1.58 ms                                                                                                         | 3.20 ms: 2.03x slower                                                                                                 |
| chaos                      | 59.3 ms                                                                                                         | 124 ms: 2.10x slower                                                                                                  |
| scimark_sor                | 126 ms                                                                                                          | 264 ms: 2.10x slower                                                                                                  |
| sqlglot_parse              | 1.27 ms                                                                                                         | 2.71 ms: 2.14x slower                                                                                                 |
| scimark_lu                 | 113 ms                                                                                                          | 245 ms: 2.17x slower                                                                                                  |
| go                         | 139 ms                                                                                                          | 307 ms: 2.20x slower                                                                                                  |
| raytrace                   | 261 ms                                                                                                          | 593 ms: 2.27x slower                                                                                                  |
| nbody                      | 89.0 ms                                                                                                         | 217 ms: 2.44x slower                                                                                                  |
| deltablue                  | 3.24 ms                                                                                                         | 8.28 ms: 2.56x slower                                                                                                 |
| bench_thread_pool          | 789 us                                                                                                          | 3.03 ms: 3.84x slower                                                                                                 |
| Geometric mean             | (ref)                                                                                                           | 1.47x slower                                                                                                          |

Benchmark hidden because not significant (1): async_tree_io
Ignored benchmarks (1) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-linux-x86_64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: dask

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.37x
- 95% likely to have a slowdown of 1.36x
- 99% likely to have a slowdown of 1.33x

# Memory
- memory change: 1.14x