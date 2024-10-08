# Results vs. 3.10.4

- fork: mdboom
- ref: simplify_richcompare
- machine: linux-aarch64
- commit hash: c9a5962
- commit date: 2024-08-29
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                   |
| tornado_http   | 178 ms                                                                | 128 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 426 ms: 2.23x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 553 ms: 2.05x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| float          | 135 ms                                                                | 93.4 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.5 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 190 us: 3.47x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.29x faster                                                   |
| async_tree_none          | 950 ms                                                                | 426 ms: 2.23x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.09 ms: 2.05x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 553 ms: 2.05x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                    |
| raytrace                 | 573 ms                                                                | 304 ms: 1.89x faster                                                    |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 68.6 ms: 1.76x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.72x faster                                                   |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 566 ms: 1.67x faster                                                    |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.7 us: 1.60x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.6 ms: 1.57x faster                                                   |
| scimark_sor              | 246 ms                                                                | 158 ms: 1.56x faster                                                    |
| deepcopy                 | 511 us                                                                | 330 us: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.10 ms: 1.54x faster                                                   |
| nbody                    | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| float                    | 135 ms                                                                | 93.4 ms: 1.44x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.5 ms: 1.40x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                                  |
| tornado_http             | 178 ms                                                                | 128 ms: 1.39x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.64 us: 1.39x faster                                                   |
| pyflate                  | 795 ms                                                                | 581 ms: 1.37x faster                                                    |
| thrift                   | 1.26 ms                                                               | 930 us: 1.35x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.1 ms: 1.33x faster                                                   |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.32x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.7 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.64 sec: 1.27x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 1.85 sec: 1.27x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 904 ms: 1.27x faster                                                    |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.5 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 61.4 ms: 1.23x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.39 ms: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 455 ms: 1.19x faster                                                    |
| nqueens                  | 117 ms                                                                | 99.5 ms: 1.18x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| fannkuch                 | 546 ms                                                                | 475 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 441 ms: 1.13x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                  |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| json_loads               | 30.9 us                                                               | 32.4 us: 1.05x slower                                                   |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.85 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 98.1 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.97 ms: 1.17x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.79 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.35x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-c9a5962/bm-20240829-arminc-aarch64-mdboom-simplify_richcompare-3.14.0a0-c9a5962.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.14x