# Results vs. 3.10.4

- fork: python
- ref: 33903c53dbdb768e1ef7
- machine: linux-aarch64
- commit hash: 33903c5
- commit date: 2024-07-01
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.22x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 358 ms: 1.06x faster                                                    |
| html5lib       | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 139 ms: 1.29x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.14x faster                                                            |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 582 ms: 1.95x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 735 ms: 1.73x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.6 ms: 1.50x faster                                                   |
| nbody          | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| regex_compile  | 177 ms                                                                | 174 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 398 us: 1.33x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 277 us: 1.32x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.16x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.93 ms: 1.30x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 81.7 ms: 1.17x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.08x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.47 ms: 2.00x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 582 ms: 1.95x faster                                                    |
| richards_super           | 107 ms                                                                | 60.5 ms: 1.77x faster                                                   |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                    |
| generators               | 68.1 ms                                                               | 39.3 ms: 1.73x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 735 ms: 1.73x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.40 ms: 1.73x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.5 ms: 1.71x faster                                                   |
| logging_silent           | 222 ns                                                                | 138 ns: 1.61x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.8 us: 1.59x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 87.0 ms: 1.54x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 614 ms: 1.54x faster                                                    |
| float                    | 135 ms                                                                | 89.6 ms: 1.50x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.50x faster                                                   |
| go                       | 264 ms                                                                | 179 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| comprehensions           | 33.1 us                                                               | 23.2 us: 1.43x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| nbody                    | 166 ms                                                                | 117 ms: 1.42x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 90.4 ms: 1.41x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.01 ms: 1.41x faster                                                   |
| scimark_sor              | 246 ms                                                                | 177 ms: 1.39x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.79 us: 1.36x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.20 us: 1.36x faster                                                   |
| deepcopy                 | 511 us                                                                | 376 us: 1.36x faster                                                    |
| chaos                    | 121 ms                                                                | 89.3 ms: 1.36x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 398 us: 1.33x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 277 us: 1.32x faster                                                    |
| thrift                   | 1.26 ms                                                               | 964 us: 1.31x faster                                                    |
| pyflate                  | 795 ms                                                                | 613 ms: 1.30x faster                                                    |
| tornado_http             | 178 ms                                                                | 139 ms: 1.29x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.35 sec: 1.26x faster                                                  |
| spectral_norm            | 186 ms                                                                | 148 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                   |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.24x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.23x faster                                                   |
| scimark_lu               | 227 ms                                                                | 185 ms: 1.23x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 70.9 ms: 1.22x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 9.00 ms: 1.21x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.0 ms: 1.20x faster                                                   |
| dask                     | 450 ms                                                                | 391 ms: 1.15x faster                                                    |
| pylint                   | 485 ms                                                                | 423 ms: 1.15x faster                                                    |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.86 ms: 1.11x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 141 ms: 1.11x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.11x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.21 us: 1.09x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 69.4 ms: 1.09x faster                                                   |
| scimark_fft              | 500 ms                                                                | 461 ms: 1.09x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| django_template          | 53.3 ms                                                               | 49.6 ms: 1.08x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.07x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.47 sec: 1.07x faster                                                  |
| 2to3                     | 381 ms                                                                | 358 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.6 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 34.2 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 71.5 ms: 1.03x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 1.12 sec: 1.02x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 2.32 sec: 1.02x faster                                                  |
| regex_compile            | 177 ms                                                                | 174 ms: 1.01x faster                                                    |
| sympy_expand             | 543 ms                                                                | 547 ms: 1.01x slower                                                    |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.4 us: 1.08x slower                                                   |
| async_generators         | 452 ms                                                                | 512 ms: 1.13x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 81.7 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 100 ms: 1.20x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 5.05 ms: 1.22x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.4 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.93 ms: 1.30x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (7): pidigits, docutils, nqueens, sympy_str, sympy_integrate, json, sympy_sum
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240701-3.14.0a0-33903c5-JIT/bm-20240701-arminc-aarch64-python-33903c53dbdb768e1ef7-3.14.0a0-33903c5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.22x