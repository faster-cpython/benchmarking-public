# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.26x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                                  |
| html5lib       | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.13 sec: 2.03x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 563 ms: 2.01x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 730 ms: 1.74x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.98x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 92.0 ms: 1.46x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.37x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 251 us: 1.46x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.21x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| django_template | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 197 us: 3.36x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                                   |
| async_tree_none          | 950 ms                                                                | 444 ms: 2.14x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.15 ms: 2.03x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.13 sec: 2.03x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 563 ms: 2.01x faster                                                    |
| raytrace                 | 573 ms                                                                | 296 ms: 1.93x faster                                                    |
| generators               | 68.1 ms                                                               | 35.3 ms: 1.93x faster                                                   |
| richards_super           | 107 ms                                                                | 58.7 ms: 1.83x faster                                                   |
| chaos                    | 121 ms                                                                | 67.5 ms: 1.79x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 730 ms: 1.74x faster                                                    |
| logging_silent           | 222 ns                                                                | 129 ns: 1.72x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.71x faster                                                   |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                   |
| go                       | 264 ms                                                                | 162 ms: 1.63x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 580 ms: 1.63x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.79 ms: 1.59x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.0 ms: 1.56x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.15 ms: 1.53x faster                                                   |
| deepcopy                 | 511 us                                                                | 335 us: 1.53x faster                                                    |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                                    |
| float                    | 135 ms                                                                | 92.0 ms: 1.46x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.46x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 251 us: 1.46x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.97 us: 1.40x faster                                                   |
| tornado_http             | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.67 us: 1.38x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| regex_compile            | 177 ms                                                                | 128 ms: 1.37x faster                                                    |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                                    |
| pylint                   | 485 ms                                                                | 356 ms: 1.36x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.43 us: 1.34x faster                                                   |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.32x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 66.4 ms: 1.30x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.30x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                                   |
| thrift                   | 1.26 ms                                                               | 977 us: 1.29x faster                                                    |
| django_template          | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                   |
| 2to3                     | 381 ms                                                                | 304 ms: 1.26x faster                                                    |
| sympy_sum                | 184 ms                                                                | 147 ms: 1.25x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.2 ms: 1.24x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.3 ms: 1.24x faster                                                   |
| dask                     | 450 ms                                                                | 364 ms: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.22x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.95 sec: 1.21x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 952 ms: 1.21x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.37 ms: 1.20x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.5 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 463 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 476 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 438 ms: 1.14x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.2 ms: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.11 sec: 1.13x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 188 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                                   |
| json                     | 5.88 ms                                                               | 5.74 ms: 1.02x faster                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| json_loads               | 30.9 us                                                               | 32.8 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 493 ms: 1.09x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.82 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.4 ms: 1.17x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.95 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.2 ms: 1.18x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.89 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.34x faster                                                            |

Benchmark hidden because not significant (3): regex_dna, pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.15x