# Results vs. base

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.61x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.44x slower
- Memory change: 1.16x

Benchmarks with tag 'apps':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| 2to3           | 294 ms                                                                                                            | 518 ms: 1.76x slower                                                                                                    |
| docutils       | 3.04 sec                                                                                                          | 4.08 sec: 1.34x slower                                                                                                  |
| html5lib       | 63.7 ms                                                                                                           | 121 ms: 1.90x slower                                                                                                    |
| tornado_http   | 129 ms                                                                                                            | 208 ms: 1.61x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.64x slower                                                                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| asyncio_websockets         | 658 ms                                                                                                            | 675 ms: 1.03x slower                                                                                                    |
| async_tree_io_tg           | 1.16 sec                                                                                                          | 1.36 sec: 1.17x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.56 sec: 1.19x slower                                                                                                  |
| async_tree_cpu_io_mixed_tg | 722 ms                                                                                                            | 869 ms: 1.20x slower                                                                                                    |
| asyncio_tcp                | 551 ms                                                                                                            | 673 ms: 1.22x slower                                                                                                    |
| async_tree_io              | 1.12 sec                                                                                                          | 1.39 sec: 1.24x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                                                                            | 908 ms: 1.25x slower                                                                                                    |
| async_tree_memoization_tg  | 544 ms                                                                                                            | 695 ms: 1.28x slower                                                                                                    |
| async_tree_memoization     | 559 ms                                                                                                            | 731 ms: 1.31x slower                                                                                                    |
| async_tree_none_tg         | 416 ms                                                                                                            | 570 ms: 1.37x slower                                                                                                    |
| async_generators           | 474 ms                                                                                                            | 652 ms: 1.37x slower                                                                                                    |
| coroutines                 | 28.3 ms                                                                                                           | 40.6 ms: 1.43x slower                                                                                                   |
| async_tree_none            | 422 ms                                                                                                            | 606 ms: 1.44x slower                                                                                                    |
| Geometric mean             | (ref)                                                                                                             | 1.26x slower                                                                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| float          | 92.7 ms                                                                                                           | 206 ms: 2.23x slower                                                                                                    |
| nbody          | 109 ms                                                                                                            | 281 ms: 2.59x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.79x slower                                                                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                                                                           | 4.46 ms: 1.10x faster                                                                                                   |
| regex_v8       | 30.2 ms                                                                                                           | 33.0 ms: 1.09x slower                                                                                                   |
| regex_compile  | 126 ms                                                                                                            | 257 ms: 2.05x slower                                                                                                    |
| Geometric mean | (ref)                                                                                                             | 1.19x slower                                                                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                                                            | 156 ms: 1.04x slower                                                                                                    |
| json_loads           | 32.5 us                                                                                                           | 38.6 us: 1.19x slower                                                                                                   |
| json_dumps           | 13.4 ms                                                                                                           | 18.2 ms: 1.36x slower                                                                                                   |
| xml_etree_generate   | 113 ms                                                                                                            | 163 ms: 1.44x slower                                                                                                    |
| tomli_loads          | 2.62 sec                                                                                                          | 4.22 sec: 1.61x slower                                                                                                  |
| xml_etree_process    | 79.1 ms                                                                                                           | 132 ms: 1.66x slower                                                                                                    |
| unpickle_pure_python | 254 us                                                                                                            | 546 us: 2.15x slower                                                                                                    |
| pickle_pure_python   | 356 us                                                                                                            | 773 us: 2.17x slower                                                                                                    |
| Geometric mean       | (ref)                                                                                                             | 1.46x slower                                                                                                            |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                                                           | 18.2 ms: 1.40x slower                                                                                                   |
| python_startup_no_site | 8.77 ms                                                                                                           | 12.3 ms: 1.40x slower                                                                                                   |
| Geometric mean         | (ref)                                                                                                             | 1.40x slower                                                                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|-----------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| genshi_xml      | 60.0 ms                                                                                                           | 104 ms: 1.73x slower                                                                                                    |
| genshi_text     | 27.5 ms                                                                                                           | 52.9 ms: 1.93x slower                                                                                                   |
| django_template | 41.4 ms                                                                                                           | 82.7 ms: 2.00x slower                                                                                                   |
| mako            | 13.3 ms                                                                                                           | 28.7 ms: 2.17x slower                                                                                                   |
| Geometric mean  | (ref)                                                                                                             | 1.95x slower                                                                                                            |

All benchmarks:
===============

| Benchmark                  | results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json | results/bm-20240831-3.14.0a0-34ddb64-NOGIL/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json |
|----------------------------|:-----------------------------------------------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------------------------------------------:|
| gc_traversal               | 4.99 ms                                                                                                           | 3.50 ms: 1.42x faster                                                                                                   |
| create_gc_cycles           | 2.29 ms                                                                                                           | 1.62 ms: 1.42x faster                                                                                                   |
| regex_effbot               | 4.89 ms                                                                                                           | 4.46 ms: 1.10x faster                                                                                                   |
| asyncio_websockets         | 658 ms                                                                                                            | 675 ms: 1.03x slower                                                                                                    |
| xml_etree_iterparse        | 150 ms                                                                                                            | 156 ms: 1.04x slower                                                                                                    |
| bench_mp_pool              | 7.00 ms                                                                                                           | 7.51 ms: 1.07x slower                                                                                                   |
| regex_v8                   | 30.2 ms                                                                                                           | 33.0 ms: 1.09x slower                                                                                                   |
| async_tree_io_tg           | 1.16 sec                                                                                                          | 1.36 sec: 1.17x slower                                                                                                  |
| asyncio_tcp_ssl            | 2.16 sec                                                                                                          | 2.56 sec: 1.19x slower                                                                                                  |
| json_loads                 | 32.5 us                                                                                                           | 38.6 us: 1.19x slower                                                                                                   |
| async_tree_cpu_io_mixed_tg | 722 ms                                                                                                            | 869 ms: 1.20x slower                                                                                                    |
| json                       | 5.70 ms                                                                                                           | 6.93 ms: 1.22x slower                                                                                                   |
| asyncio_tcp                | 551 ms                                                                                                            | 673 ms: 1.22x slower                                                                                                    |
| async_tree_io              | 1.12 sec                                                                                                          | 1.39 sec: 1.24x slower                                                                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                                                                            | 908 ms: 1.25x slower                                                                                                    |
| pathlib                    | 21.0 ms                                                                                                           | 26.4 ms: 1.25x slower                                                                                                   |
| async_tree_memoization_tg  | 544 ms                                                                                                            | 695 ms: 1.28x slower                                                                                                    |
| mdp                        | 3.35 sec                                                                                                          | 4.33 sec: 1.29x slower                                                                                                  |
| async_tree_memoization     | 559 ms                                                                                                            | 731 ms: 1.31x slower                                                                                                    |
| telco                      | 9.76 ms                                                                                                           | 12.8 ms: 1.31x slower                                                                                                   |
| scimark_fft                | 439 ms                                                                                                            | 576 ms: 1.31x slower                                                                                                    |
| docutils                   | 3.04 sec                                                                                                          | 4.08 sec: 1.34x slower                                                                                                  |
| coverage                   | 99.1 ms                                                                                                           | 135 ms: 1.36x slower                                                                                                    |
| json_dumps                 | 13.4 ms                                                                                                           | 18.2 ms: 1.36x slower                                                                                                   |
| async_tree_none_tg         | 416 ms                                                                                                            | 570 ms: 1.37x slower                                                                                                    |
| async_generators           | 474 ms                                                                                                            | 652 ms: 1.37x slower                                                                                                    |
| python_startup             | 13.0 ms                                                                                                           | 18.2 ms: 1.40x slower                                                                                                   |
| scimark_sparse_mat_mult    | 6.40 ms                                                                                                           | 8.94 ms: 1.40x slower                                                                                                   |
| python_startup_no_site     | 8.77 ms                                                                                                           | 12.3 ms: 1.40x slower                                                                                                   |
| pylint                     | 359 ms                                                                                                            | 514 ms: 1.43x slower                                                                                                    |
| coroutines                 | 28.3 ms                                                                                                           | 40.6 ms: 1.43x slower                                                                                                   |
| async_tree_none            | 422 ms                                                                                                            | 606 ms: 1.44x slower                                                                                                    |
| xml_etree_generate         | 113 ms                                                                                                            | 163 ms: 1.44x slower                                                                                                    |
| meteor_contest             | 112 ms                                                                                                            | 168 ms: 1.51x slower                                                                                                    |
| nqueens                    | 99.9 ms                                                                                                           | 151 ms: 1.51x slower                                                                                                    |
| fannkuch                   | 465 ms                                                                                                            | 736 ms: 1.59x slower                                                                                                    |
| bpe_tokeniser              | 5.87 sec                                                                                                          | 9.42 sec: 1.60x slower                                                                                                  |
| tornado_http               | 129 ms                                                                                                            | 208 ms: 1.61x slower                                                                                                    |
| tomli_loads                | 2.62 sec                                                                                                          | 4.22 sec: 1.61x slower                                                                                                  |
| spectral_norm              | 141 ms                                                                                                            | 231 ms: 1.64x slower                                                                                                    |
| dulwich_log                | 58.7 ms                                                                                                           | 97.1 ms: 1.65x slower                                                                                                   |
| deepcopy                   | 337 us                                                                                                            | 557 us: 1.66x slower                                                                                                    |
| xml_etree_process          | 79.1 ms                                                                                                           | 132 ms: 1.66x slower                                                                                                    |
| crypto_pyaes               | 83.3 ms                                                                                                           | 139 ms: 1.66x slower                                                                                                    |
| generators                 | 35.0 ms                                                                                                           | 58.4 ms: 1.67x slower                                                                                                   |
| pycparser                  | 1.21 sec                                                                                                          | 2.03 sec: 1.67x slower                                                                                                  |
| sympy_integrate            | 20.6 ms                                                                                                           | 34.8 ms: 1.69x slower                                                                                                   |
| deepcopy_reduce            | 3.51 us                                                                                                           | 5.94 us: 1.69x slower                                                                                                   |
| bench_thread_pool          | 1.24 ms                                                                                                           | 2.13 ms: 1.72x slower                                                                                                   |
| genshi_xml                 | 60.0 ms                                                                                                           | 104 ms: 1.73x slower                                                                                                    |
| typing_runtime_protocols   | 193 us                                                                                                            | 337 us: 1.75x slower                                                                                                    |
| 2to3                       | 294 ms                                                                                                            | 518 ms: 1.76x slower                                                                                                    |
| thrift                     | 931 us                                                                                                            | 1.67 ms: 1.80x slower                                                                                                   |
| pyflate                    | 567 ms                                                                                                            | 1.02 sec: 1.81x slower                                                                                                  |
| sqlglot_normalize          | 127 ms                                                                                                            | 234 ms: 1.84x slower                                                                                                    |
| sqlglot_optimize           | 62.5 ms                                                                                                           | 116 ms: 1.85x slower                                                                                                    |
| deepcopy_memo              | 38.2 us                                                                                                           | 72.3 us: 1.89x slower                                                                                                   |
| html5lib                   | 63.7 ms                                                                                                           | 121 ms: 1.90x slower                                                                                                    |
| pprint_pformat             | 1.90 sec                                                                                                          | 3.63 sec: 1.91x slower                                                                                                  |
| pprint_safe_repr           | 915 ms                                                                                                            | 1.76 sec: 1.92x slower                                                                                                  |
| genshi_text                | 27.5 ms                                                                                                           | 52.9 ms: 1.93x slower                                                                                                   |
| sympy_str                  | 264 ms                                                                                                            | 516 ms: 1.95x slower                                                                                                    |
| comprehensions             | 20.8 us                                                                                                           | 40.9 us: 1.97x slower                                                                                                   |
| django_template            | 41.4 ms                                                                                                           | 82.7 ms: 2.00x slower                                                                                                   |
| regex_compile              | 126 ms                                                                                                            | 257 ms: 2.05x slower                                                                                                    |
| sympy_expand               | 462 ms                                                                                                            | 959 ms: 2.08x slower                                                                                                    |
| logging_format             | 7.64 us                                                                                                           | 16.1 us: 2.10x slower                                                                                                   |
| scimark_monte_carlo        | 82.5 ms                                                                                                           | 174 ms: 2.11x slower                                                                                                    |
| richards                   | 54.3 ms                                                                                                           | 117 ms: 2.15x slower                                                                                                    |
| unpickle_pure_python       | 254 us                                                                                                            | 546 us: 2.15x slower                                                                                                    |
| logging_simple             | 6.91 us                                                                                                           | 14.9 us: 2.16x slower                                                                                                   |
| mako                       | 13.3 ms                                                                                                           | 28.7 ms: 2.17x slower                                                                                                   |
| pickle_pure_python         | 356 us                                                                                                            | 773 us: 2.17x slower                                                                                                    |
| scimark_sor                | 157 ms                                                                                                            | 342 ms: 2.18x slower                                                                                                    |
| logging_silent             | 131 ns                                                                                                            | 287 ns: 2.19x slower                                                                                                    |
| hexiom                     | 7.13 ms                                                                                                           | 15.8 ms: 2.22x slower                                                                                                   |
| float                      | 92.7 ms                                                                                                           | 206 ms: 2.23x slower                                                                                                    |
| sympy_sum                  | 141 ms                                                                                                            | 317 ms: 2.25x slower                                                                                                    |
| richards_super             | 60.7 ms                                                                                                           | 138 ms: 2.27x slower                                                                                                    |
| chaos                      | 68.6 ms                                                                                                           | 159 ms: 2.32x slower                                                                                                    |
| sqlglot_transpile          | 1.73 ms                                                                                                           | 4.27 ms: 2.46x slower                                                                                                   |
| nbody                      | 109 ms                                                                                                            | 281 ms: 2.59x slower                                                                                                    |
| sqlglot_parse              | 1.40 ms                                                                                                           | 3.65 ms: 2.60x slower                                                                                                   |
| scimark_lu                 | 135 ms                                                                                                            | 353 ms: 2.61x slower                                                                                                    |
| raytrace                   | 301 ms                                                                                                            | 812 ms: 2.70x slower                                                                                                    |
| go                         | 138 ms                                                                                                            | 389 ms: 2.83x slower                                                                                                    |
| deltablue                  | 3.92 ms                                                                                                           | 12.8 ms: 3.26x slower                                                                                                   |
| Geometric mean             | (ref)                                                                                                             | 1.61x slower                                                                                                            |

Benchmark hidden because not significant (3): xml_etree_parse, regex_dna, pidigits

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.53x
- 95% likely to have a slowdown of 1.49x
- 99% likely to have a slowdown of 1.44x

# Memory
- memory change: 1.16x