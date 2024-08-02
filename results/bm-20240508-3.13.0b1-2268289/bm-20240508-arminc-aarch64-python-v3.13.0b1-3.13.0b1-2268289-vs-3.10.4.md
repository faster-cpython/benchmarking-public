# Results vs. 3.10.4

- fork: python
- ref: v3.13.0b1
- machine: linux-aarch64
- commit hash: 2268289
- commit date: 2024-05-08
- overall geometric mean: 1.24x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                         |
| chameleon      | 10.8 ms                                                               | 9.23 ms: 1.18x faster                                        |
| docutils       | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                       |
| html5lib       | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                        |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                         |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 491 ms: 1.93x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 645 ms: 1.76x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 799 ms: 1.59x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.79x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.50x faster                                         |
| float          | 135 ms                                                                | 90.7 ms: 1.48x faster                                        |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                 |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                         |
| regex_v8       | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                        |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                        |
| Geometric mean | (ref)                                                                 | 1.05x faster                                                 |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 363 us: 1.46x faster                                         |
| unpickle_pure_python | 366 us                                                                | 255 us: 1.43x faster                                         |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                        |
| unpickle_list        | 6.99 us                                                               | 6.31 us: 1.11x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 199 ms: 1.06x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 118 ms: 1.04x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                         |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                        |
| pickle_dict          | 35.1 us                                                               | 38.0 us: 1.08x slower                                        |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                        |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.10x faster                                                 |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 8.49 ms: 1.23x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.18x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.25x faster                                        |
| django_template | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 61.7 ms: 1.13x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.25x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.90 ms: 2.29x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 7.04 ms: 2.06x faster                                        |
| async_tree_none          | 950 ms                                                                | 491 ms: 1.93x faster                                         |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.21 sec: 1.89x faster                                       |
| generators               | 68.1 ms                                                               | 37.3 ms: 1.82x faster                                        |
| chaos                    | 121 ms                                                                | 66.5 ms: 1.82x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 645 ms: 1.76x faster                                         |
| asyncio_tcp              | 944 ms                                                                | 545 ms: 1.73x faster                                         |
| richards_super           | 107 ms                                                                | 62.8 ms: 1.71x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.69x faster                                        |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                         |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                        |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                        |
| richards                 | 91.7 ms                                                               | 56.3 ms: 1.63x faster                                        |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                         |
| crypto_pyaes             | 134 ms                                                                | 82.4 ms: 1.63x faster                                        |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 799 ms: 1.59x faster                                         |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                         |
| hexiom                   | 10.9 ms                                                               | 7.07 ms: 1.54x faster                                        |
| scimark_monte_carlo      | 128 ms                                                                | 83.1 ms: 1.54x faster                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.17 sec: 1.51x faster                                       |
| nbody                    | 166 ms                                                                | 110 ms: 1.50x faster                                         |
| float                    | 135 ms                                                                | 90.7 ms: 1.48x faster                                        |
| pickle_pure_python       | 529 us                                                                | 363 us: 1.46x faster                                         |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                        |
| unpickle_pure_python     | 366 us                                                                | 255 us: 1.43x faster                                         |
| pylint                   | 485 ms                                                                | 344 ms: 1.41x faster                                         |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                       |
| logging_simple           | 9.78 us                                                               | 7.15 us: 1.37x faster                                        |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                         |
| logging_format           | 10.6 us                                                               | 7.78 us: 1.36x faster                                        |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                         |
| spectral_norm            | 186 ms                                                                | 139 ms: 1.34x faster                                         |
| pyflate                  | 795 ms                                                                | 595 ms: 1.34x faster                                         |
| thrift                   | 1.26 ms                                                               | 946 us: 1.33x faster                                         |
| html5lib                 | 86.5 ms                                                               | 66.6 ms: 1.30x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                       |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                         |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.25x faster                                        |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                        |
| django_template          | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                        |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                         |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                        |
| bench_thread_pool        | 1.59 ms                                                               | 1.28 ms: 1.24x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 21.4 ms: 1.24x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 59.5 ms: 1.23x faster                                        |
| pprint_pformat           | 2.36 sec                                                              | 1.94 sec: 1.22x faster                                       |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                         |
| mypy2                    | 936 ms                                                                | 771 ms: 1.21x faster                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 948 ms: 1.21x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 82.2 ms: 1.21x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                         |
| deepcopy_memo            | 61.7 us                                                               | 51.0 us: 1.21x faster                                        |
| gunicorn                 | 1.45 ms                                                               | 1.21 ms: 1.20x faster                                        |
| dask                     | 450 ms                                                                | 378 ms: 1.19x faster                                         |
| sqlglot_optimize         | 75.4 ms                                                               | 63.6 ms: 1.19x faster                                        |
| chameleon                | 10.8 ms                                                               | 9.23 ms: 1.18x faster                                        |
| fannkuch                 | 546 ms                                                                | 465 ms: 1.17x faster                                         |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.56 ms: 1.16x faster                                        |
| aiohttp                  | 1.39 ms                                                               | 1.20 ms: 1.16x faster                                        |
| sympy_expand             | 543 ms                                                                | 470 ms: 1.15x faster                                         |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                        |
| genshi_xml               | 69.8 ms                                                               | 61.7 ms: 1.13x faster                                        |
| docutils                 | 3.53 sec                                                              | 3.12 sec: 1.13x faster                                       |
| scimark_fft              | 500 ms                                                                | 442 ms: 1.13x faster                                         |
| deepcopy                 | 511 us                                                                | 453 us: 1.13x faster                                         |
| deepcopy_reduce          | 4.60 us                                                               | 4.09 us: 1.12x faster                                        |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                         |
| unpickle_list            | 6.99 us                                                               | 6.31 us: 1.11x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.34 sec: 1.11x faster                                       |
| xml_etree_parse          | 212 ms                                                                | 199 ms: 1.06x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                        |
| xml_etree_generate       | 123 ms                                                                | 118 ms: 1.04x faster                                         |
| json                     | 5.88 ms                                                               | 5.65 ms: 1.04x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 31.5 ms: 1.02x faster                                        |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                         |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 2.43 ms: 1.08x slower                                        |
| async_generators         | 452 ms                                                                | 488 ms: 1.08x slower                                         |
| pickle_dict              | 35.1 us                                                               | 38.0 us: 1.08x slower                                        |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                        |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                        |
| python_startup           | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                        |
| coverage                 | 83.6 ms                                                               | 98.6 ms: 1.18x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.22x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 8.49 ms: 1.23x slower                                        |
| telco                    | 8.49 ms                                                               | 167 ms: 19.73x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                 |

Benchmark hidden because not significant (4): regex_dna, flaskblogging, pidigits, pickle_list
Ignored benchmarks (2) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240508-3.13.0b1-2268289/bm-20240508-arminc-aarch64-python-v3.13.0b1-3.13.0b1-2268289.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: 1.13x