# Results vs. 3.13.0b2

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.57x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.35x slower
- Memory change: 1.17x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 305 ms                                                       | 518 ms: 1.70x slower                                                    |
| docutils       | 3.10 sec                                                     | 4.08 sec: 1.32x slower                                                  |
| html5lib       | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| tornado_http   | 128 ms                                                       | 208 ms: 1.63x slower                                                    |
| Geometric mean | (ref)                                                        | 1.61x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| async_tree_memoization     | 645 ms                                                       | 731 ms: 1.13x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 869 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 908 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| async_tree_none_tg         | 476 ms                                                       | 570 ms: 1.20x slower                                                    |
| async_tree_none            | 492 ms                                                       | 606 ms: 1.23x slower                                                    |
| Geometric mean             | (ref)                                                        | 1.15x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                      | 206 ms: 2.26x slower                                                    |
| nbody          | 114 ms                                                       | 281 ms: 2.47x slower                                                    |
| Geometric mean | (ref)                                                        | 1.77x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.98 ms                                                      | 4.46 ms: 1.12x faster                                                   |
| regex_dna      | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| regex_v8       | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| regex_compile  | 128 ms                                                       | 257 ms: 2.01x slower                                                    |
| Geometric mean | (ref)                                                        | 1.17x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 191 ms                                                       | 185 ms: 1.03x faster                                                    |
| xml_etree_iterparse  | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| json_loads           | 32.1 us                                                      | 38.6 us: 1.20x slower                                                   |
| json_dumps           | 13.1 ms                                                      | 18.2 ms: 1.39x slower                                                   |
| xml_etree_generate   | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| xml_etree_process    | 80.8 ms                                                      | 132 ms: 1.63x slower                                                    |
| tomli_loads          | 2.57 sec                                                     | 4.22 sec: 1.64x slower                                                  |
| pickle_pure_python   | 359 us                                                       | 773 us: 2.16x slower                                                    |
| unpickle_pure_python | 251 us                                                       | 546 us: 2.17x slower                                                    |
| Geometric mean       | (ref)                                                        | 1.46x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                      | 18.2 ms: 1.40x slower                                                   |
| python_startup_no_site | 8.60 ms                                                      | 12.3 ms: 1.43x slower                                                   |
| Geometric mean         | (ref)                                                        | 1.41x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.4 ms                                                      | 52.9 ms: 1.93x slower                                                   |
| django_template | 42.3 ms                                                      | 82.7 ms: 1.95x slower                                                   |
| mako            | 13.2 ms                                                      | 28.7 ms: 2.19x slower                                                   |
| Geometric mean  | (ref)                                                        | 1.94x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| gc_traversal               | 5.17 ms                                                      | 3.50 ms: 1.48x faster                                                   |
| create_gc_cycles           | 2.33 ms                                                      | 1.62 ms: 1.44x faster                                                   |
| regex_effbot               | 4.98 ms                                                      | 4.46 ms: 1.12x faster                                                   |
| xml_etree_parse            | 191 ms                                                       | 185 ms: 1.03x faster                                                    |
| regex_dna                  | 259 ms                                                       | 253 ms: 1.02x faster                                                    |
| asyncio_websockets         | 657 ms                                                       | 675 ms: 1.03x slower                                                    |
| regex_v8                   | 31.1 ms                                                      | 33.0 ms: 1.06x slower                                                   |
| async_tree_io_tg           | 1.27 sec                                                     | 1.36 sec: 1.07x slower                                                  |
| xml_etree_iterparse        | 147 ms                                                       | 156 ms: 1.07x slower                                                    |
| bench_mp_pool              | 7.03 ms                                                      | 7.51 ms: 1.07x slower                                                   |
| async_tree_memoization     | 645 ms                                                       | 731 ms: 1.13x slower                                                    |
| async_tree_io              | 1.22 sec                                                     | 1.39 sec: 1.14x slower                                                  |
| async_tree_cpu_io_mixed_tg | 763 ms                                                       | 869 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 791 ms                                                       | 908 ms: 1.15x slower                                                    |
| async_tree_memoization_tg  | 604 ms                                                       | 695 ms: 1.15x slower                                                    |
| asyncio_tcp                | 584 ms                                                       | 673 ms: 1.15x slower                                                    |
| pathlib                    | 22.8 ms                                                      | 26.4 ms: 1.16x slower                                                   |
| asyncio_tcp_ssl            | 2.21 sec                                                     | 2.56 sec: 1.16x slower                                                  |
| async_tree_none_tg         | 476 ms                                                       | 570 ms: 1.20x slower                                                    |
| json_loads                 | 32.1 us                                                      | 38.6 us: 1.20x slower                                                   |
| json                       | 5.64 ms                                                      | 6.93 ms: 1.23x slower                                                   |
| async_tree_none            | 492 ms                                                       | 606 ms: 1.23x slower                                                    |
| deepcopy                   | 448 us                                                       | 557 us: 1.24x slower                                                    |
| telco                      | 10.0 ms                                                      | 12.8 ms: 1.28x slower                                                   |
| scimark_fft                | 445 ms                                                       | 576 ms: 1.29x slower                                                    |
| mdp                        | 3.33 sec                                                     | 4.33 sec: 1.30x slower                                                  |
| docutils                   | 3.10 sec                                                     | 4.08 sec: 1.32x slower                                                  |
| async_generators           | 488 ms                                                       | 652 ms: 1.34x slower                                                    |
| scimark_sparse_mat_mult    | 6.55 ms                                                      | 8.94 ms: 1.36x slower                                                   |
| coverage                   | 98.4 ms                                                      | 135 ms: 1.37x slower                                                    |
| json_dumps                 | 13.1 ms                                                      | 18.2 ms: 1.39x slower                                                   |
| coroutines                 | 29.0 ms                                                      | 40.6 ms: 1.40x slower                                                   |
| python_startup             | 13.0 ms                                                      | 18.2 ms: 1.40x slower                                                   |
| deepcopy_memo              | 50.8 us                                                      | 72.3 us: 1.42x slower                                                   |
| python_startup_no_site     | 8.60 ms                                                      | 12.3 ms: 1.43x slower                                                   |
| xml_etree_generate         | 114 ms                                                       | 163 ms: 1.43x slower                                                    |
| deepcopy_reduce            | 4.04 us                                                      | 5.94 us: 1.47x slower                                                   |
| meteor_contest             | 113 ms                                                       | 168 ms: 1.48x slower                                                    |
| pylint                     | 337 ms                                                       | 514 ms: 1.53x slower                                                    |
| nqueens                    | 98.9 ms                                                      | 151 ms: 1.53x slower                                                    |
| generators                 | 37.1 ms                                                      | 58.4 ms: 1.57x slower                                                   |
| bpe_tokeniser              | 5.83 sec                                                     | 9.42 sec: 1.62x slower                                                  |
| tornado_http               | 128 ms                                                       | 208 ms: 1.63x slower                                                    |
| xml_etree_process          | 80.8 ms                                                      | 132 ms: 1.63x slower                                                    |
| fannkuch                   | 451 ms                                                       | 736 ms: 1.63x slower                                                    |
| spectral_norm              | 141 ms                                                       | 231 ms: 1.64x slower                                                    |
| tomli_loads                | 2.57 sec                                                     | 4.22 sec: 1.64x slower                                                  |
| dulwich_log                | 58.5 ms                                                      | 97.1 ms: 1.66x slower                                                   |
| pycparser                  | 1.22 sec                                                     | 2.03 sec: 1.66x slower                                                  |
| sympy_integrate            | 20.9 ms                                                      | 34.8 ms: 1.67x slower                                                   |
| crypto_pyaes               | 82.0 ms                                                      | 139 ms: 1.69x slower                                                    |
| bench_thread_pool          | 1.26 ms                                                      | 2.13 ms: 1.70x slower                                                   |
| 2to3                       | 305 ms                                                       | 518 ms: 1.70x slower                                                    |
| genshi_xml                 | 60.4 ms                                                      | 104 ms: 1.72x slower                                                    |
| thrift                     | 962 us                                                       | 1.67 ms: 1.74x slower                                                   |
| typing_runtime_protocols   | 193 us                                                       | 337 us: 1.74x slower                                                    |
| sqlglot_normalize          | 129 ms                                                       | 234 ms: 1.81x slower                                                    |
| html5lib                   | 66.1 ms                                                      | 121 ms: 1.83x slower                                                    |
| pyflate                    | 557 ms                                                       | 1.02 sec: 1.84x slower                                                  |
| sqlglot_optimize           | 62.6 ms                                                      | 116 ms: 1.85x slower                                                    |
| pprint_pformat             | 1.93 sec                                                     | 3.63 sec: 1.88x slower                                                  |
| pprint_safe_repr           | 933 ms                                                       | 1.76 sec: 1.88x slower                                                  |
| genshi_text                | 27.4 ms                                                      | 52.9 ms: 1.93x slower                                                   |
| sympy_str                  | 265 ms                                                       | 516 ms: 1.94x slower                                                    |
| django_template            | 42.3 ms                                                      | 82.7 ms: 1.95x slower                                                   |
| comprehensions             | 20.5 us                                                      | 40.9 us: 1.99x slower                                                   |
| regex_compile              | 128 ms                                                       | 257 ms: 2.01x slower                                                    |
| logging_format             | 7.82 us                                                      | 16.1 us: 2.05x slower                                                   |
| logging_simple             | 7.21 us                                                      | 14.9 us: 2.07x slower                                                   |
| richards                   | 55.9 ms                                                      | 117 ms: 2.09x slower                                                    |
| sympy_expand               | 457 ms                                                       | 959 ms: 2.10x slower                                                    |
| scimark_monte_carlo        | 82.3 ms                                                      | 174 ms: 2.11x slower                                                    |
| scimark_sor                | 159 ms                                                       | 342 ms: 2.15x slower                                                    |
| logging_silent             | 133 ns                                                       | 287 ns: 2.15x slower                                                    |
| pickle_pure_python         | 359 us                                                       | 773 us: 2.16x slower                                                    |
| unpickle_pure_python       | 251 us                                                       | 546 us: 2.17x slower                                                    |
| mako                       | 13.2 ms                                                      | 28.7 ms: 2.19x slower                                                   |
| richards_super             | 62.3 ms                                                      | 138 ms: 2.21x slower                                                    |
| sympy_sum                  | 144 ms                                                       | 317 ms: 2.21x slower                                                    |
| hexiom                     | 7.08 ms                                                      | 15.8 ms: 2.23x slower                                                   |
| float                      | 91.4 ms                                                      | 206 ms: 2.26x slower                                                    |
| chaos                      | 68.3 ms                                                      | 159 ms: 2.33x slower                                                    |
| go                         | 161 ms                                                       | 389 ms: 2.42x slower                                                    |
| nbody                      | 114 ms                                                       | 281 ms: 2.47x slower                                                    |
| sqlglot_transpile          | 1.71 ms                                                      | 4.27 ms: 2.50x slower                                                   |
| scimark_lu                 | 141 ms                                                       | 353 ms: 2.50x slower                                                    |
| sqlglot_parse              | 1.42 ms                                                      | 3.65 ms: 2.56x slower                                                   |
| raytrace                   | 297 ms                                                       | 812 ms: 2.74x slower                                                    |
| deltablue                  | 3.88 ms                                                      | 12.8 ms: 3.30x slower                                                   |
| Geometric mean             | (ref)                                                        | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (12) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-arminc-aarch64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpickle, unpickle_list

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.44x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.35x

# Memory
- memory change: 1.17x