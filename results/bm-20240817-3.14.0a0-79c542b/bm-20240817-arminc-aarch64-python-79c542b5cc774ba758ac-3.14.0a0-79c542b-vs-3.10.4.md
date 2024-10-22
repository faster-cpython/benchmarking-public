# Results vs. 3.10.4

- fork: python
- ref: 79c542b5cc774ba758ac
- machine: linux-aarch64
- commit hash: 79c542b
- commit date: 2024-08-17
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| tornado_http   | 178 ms                                                                | 121 ms: 1.47x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 438 ms: 2.17x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.08 sec: 2.11x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 549 ms: 2.06x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.02x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 93.1 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 356 us: 1.49x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                   |
| django_template | 53.3 ms                                                               | 42.9 ms: 1.24x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 201 us: 3.29x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.77 ms: 2.37x faster                                                   |
| async_tree_none          | 950 ms                                                                | 438 ms: 2.17x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.08 sec: 2.11x faster                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 7.00 ms: 2.08x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 549 ms: 2.06x faster                                                    |
| generators               | 68.1 ms                                                               | 34.4 ms: 1.98x faster                                                   |
| raytrace                 | 573 ms                                                                | 294 ms: 1.95x faster                                                    |
| richards_super           | 107 ms                                                                | 58.4 ms: 1.84x faster                                                   |
| chaos                    | 121 ms                                                                | 67.7 ms: 1.79x faster                                                   |
| richards                 | 91.7 ms                                                               | 51.9 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                    |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.70x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 37.5 us: 1.65x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 576 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.62x faster                                                   |
| scimark_sor              | 246 ms                                                                | 154 ms: 1.60x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 6.98 ms: 1.56x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 81.8 ms: 1.56x faster                                                   |
| deepcopy                 | 511 us                                                                | 330 us: 1.54x faster                                                    |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.49x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 356 us: 1.49x faster                                                    |
| tornado_http             | 178 ms                                                                | 121 ms: 1.47x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| float                    | 135 ms                                                                | 93.1 ms: 1.45x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.93 us: 1.41x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.38x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.69 us: 1.38x faster                                                   |
| pyflate                  | 795 ms                                                                | 577 ms: 1.38x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.40 us: 1.35x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| thrift                   | 1.26 ms                                                               | 957 us: 1.32x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.25 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                                   |
| sympy_sum                | 184 ms                                                                | 145 ms: 1.27x faster                                                    |
| 2to3                     | 381 ms                                                                | 302 ms: 1.26x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.1 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.24x faster                                                   |
| django_template          | 53.3 ms                                                               | 42.9 ms: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 61.8 ms: 1.22x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 942 ms: 1.22x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.37 ms: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.8 ms: 1.19x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 464 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.1 ms: 1.16x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.13 sec: 1.13x faster                                                  |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 189 ms: 1.12x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.10x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.38 sec: 1.09x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| json                     | 5.88 ms                                                               | 5.72 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 482 ms: 1.07x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 4.79 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.6 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240817-3.14.0a0-79c542b/bm-20240817-arminc-aarch64-python-79c542b5cc774ba758ac-3.14.0a0-79c542b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.15x