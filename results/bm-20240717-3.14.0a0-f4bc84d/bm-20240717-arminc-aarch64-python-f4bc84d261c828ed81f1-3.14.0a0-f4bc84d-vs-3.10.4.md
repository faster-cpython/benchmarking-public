# Results vs. 3.10.4

- fork: python
- ref: f4bc84d261c828ed81f1
- machine: linux-aarch64
- commit hash: f4bc84d
- commit date: 2024-07-17
- overall geometric mean: 1.33x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 301 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                  |
| html5lib       | 86.5 ms                                                               | 68.0 ms: 1.27x faster                                                   |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 439 ms: 2.16x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 551 ms: 2.06x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 729 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.02x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| float          | 135 ms                                                                | 93.1 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.36x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 357 us: 1.48x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| django_template | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.31x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.87 ms: 2.31x faster                                                   |
| async_tree_none          | 950 ms                                                                | 439 ms: 2.16x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.07 sec: 2.14x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 551 ms: 2.06x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.08 ms: 2.05x faster                                                   |
| raytrace                 | 573 ms                                                                | 300 ms: 1.91x faster                                                    |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                                   |
| richards_super           | 107 ms                                                                | 60.3 ms: 1.78x faster                                                   |
| chaos                    | 121 ms                                                                | 68.4 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 729 ms: 1.74x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.8 ms: 1.71x faster                                                   |
| logging_silent           | 222 ns                                                                | 135 ns: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| go                       | 264 ms                                                                | 161 ms: 1.64x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 579 ms: 1.63x faster                                                    |
| comprehensions           | 33.1 us                                                               | 20.5 us: 1.61x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 39.3 us: 1.57x faster                                                   |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.5 ms: 1.55x faster                                                   |
| scimark_sor              | 246 ms                                                                | 160 ms: 1.54x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 357 us: 1.48x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.22 sec: 1.48x faster                                                  |
| nbody                    | 166 ms                                                                | 114 ms: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 93.1 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| pylint                   | 485 ms                                                                | 339 ms: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.6 ms: 1.39x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                                    |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.36x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.87 us: 1.35x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.42 us: 1.35x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.28 us: 1.34x faster                                                   |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.56 sec: 1.31x faster                                                  |
| thrift                   | 1.26 ms                                                               | 970 us: 1.30x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 68.0 ms: 1.27x faster                                                   |
| 2to3                     | 381 ms                                                                | 301 ms: 1.26x faster                                                    |
| sympy_sum                | 184 ms                                                                | 146 ms: 1.26x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.4 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.2 ms: 1.25x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.5 ms: 1.23x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.92 sec: 1.23x faster                                                  |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 28.8 ms: 1.22x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 81.4 ms: 1.22x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 939 ms: 1.22x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.6 ms: 1.22x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.6 ms: 1.20x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 130 ms: 1.20x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.2 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 470 ms: 1.16x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.06 sec: 1.15x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.67 ms: 1.14x faster                                                   |
| meteor_contest           | 126 ms                                                                | 111 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.3 ms: 1.12x faster                                                   |
| scimark_fft              | 500 ms                                                                | 448 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 147 ms: 1.06x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.8 ms: 1.04x faster                                                   |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                                   |
| json_loads               | 30.9 us                                                               | 33.1 us: 1.07x slower                                                   |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.91 ms: 1.16x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.2 ms: 1.19x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.07 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.90 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.33x faster                                                            |

Benchmark hidden because not significant (3): json, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240717-3.14.0a0-f4bc84d/bm-20240717-arminc-aarch64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x