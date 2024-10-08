# Results vs. 3.10.4

- fork: python
- ref: 04eb5c8db1e24cabd0cb
- machine: linux-aarch64
- commit hash: 04eb5c8
- commit date: 2024-07-27
- overall geometric mean: 1.23x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.08x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                  |
| html5lib       | 86.5 ms                                                               | 71.0 ms: 1.22x faster                                                   |
| tornado_http   | 178 ms                                                                | 140 ms: 1.28x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 434 ms: 2.19x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 570 ms: 1.99x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 738 ms: 1.72x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.97x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.9 ms: 1.48x faster                                                   |
| nbody          | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                   |
| regex_dna      | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| regex_compile  | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 272 us: 1.34x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 82.0 ms: 1.21x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 146 ms: 1.07x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.92 ms: 1.29x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.23x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                                   |
| django_template | 53.3 ms                                                               | 50.7 ms: 1.05x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 35.0 ms: 1.01x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 82.9 ms: 1.19x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.07x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 209 us: 3.16x faster                                                    |
| async_tree_none          | 950 ms                                                                | 434 ms: 2.19x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.32 ms: 2.07x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 570 ms: 1.99x faster                                                    |
| generators               | 68.1 ms                                                               | 35.6 ms: 1.91x faster                                                   |
| richards_super           | 107 ms                                                                | 61.4 ms: 1.75x faster                                                   |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 8.38 ms: 1.74x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 738 ms: 1.72x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.8 ms: 1.70x faster                                                   |
| logging_silent           | 222 ns                                                                | 135 ns: 1.64x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 38.7 us: 1.60x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 617 ms: 1.53x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 88.4 ms: 1.52x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.60 ms: 1.51x faster                                                   |
| float                    | 135 ms                                                                | 90.9 ms: 1.48x faster                                                   |
| nbody                    | 166 ms                                                                | 112 ms: 1.48x faster                                                    |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.23 sec: 1.47x faster                                                  |
| go                       | 264 ms                                                                | 180 ms: 1.47x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 87.7 ms: 1.46x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.5 us: 1.41x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 2.03 ms: 1.40x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| chaos                    | 121 ms                                                                | 87.5 ms: 1.38x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.24 us: 1.35x faster                                                   |
| deepcopy                 | 511 us                                                                | 380 us: 1.34x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 272 us: 1.34x faster                                                    |
| pyflate                  | 795 ms                                                                | 593 ms: 1.34x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.96 us: 1.33x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.2 ms: 1.32x faster                                                   |
| spectral_norm            | 186 ms                                                                | 144 ms: 1.29x faster                                                    |
| thrift                   | 1.26 ms                                                               | 981 us: 1.28x faster                                                    |
| tornado_http             | 178 ms                                                                | 140 ms: 1.28x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| scimark_lu               | 227 ms                                                                | 181 ms: 1.26x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.22x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 71.0 ms: 1.22x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 82.0 ms: 1.21x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.41 sec: 1.20x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 9.16 ms: 1.19x faster                                                   |
| dask                     | 450 ms                                                                | 392 ms: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.0 ms: 1.14x faster                                                   |
| fannkuch                 | 546 ms                                                                | 479 ms: 1.14x faster                                                    |
| pylint                   | 485 ms                                                                | 428 ms: 1.13x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.77 ms: 1.13x faster                                                   |
| scimark_fft              | 500 ms                                                                | 456 ms: 1.10x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.20 us: 1.09x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.44 sec: 1.08x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 145 ms: 1.07x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 146 ms: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                   |
| 2to3                     | 381 ms                                                                | 359 ms: 1.06x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 71.2 ms: 1.06x faster                                                   |
| django_template          | 53.3 ms                                                               | 50.7 ms: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 249 ms: 1.03x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 35.0 ms: 1.01x faster                                                   |
| nqueens                  | 117 ms                                                                | 119 ms: 1.01x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.38 sec: 1.01x slower                                                  |
| regex_compile            | 177 ms                                                                | 180 ms: 1.02x slower                                                    |
| sympy_integrate          | 26.5 ms                                                               | 27.1 ms: 1.02x slower                                                   |
| docutils                 | 3.53 sec                                                              | 3.61 sec: 1.02x slower                                                  |
| sympy_str                | 329 ms                                                                | 339 ms: 1.03x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.33 ms: 1.03x slower                                                   |
| sympy_expand             | 543 ms                                                                | 571 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.6 us: 1.05x slower                                                   |
| sympy_sum                | 184 ms                                                                | 199 ms: 1.08x slower                                                    |
| async_generators         | 452 ms                                                                | 505 ms: 1.12x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                                   |
| genshi_xml               | 69.8 ms                                                               | 82.9 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.04 ms: 1.21x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.92 ms: 1.29x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (4): pidigits, json, pprint_safe_repr, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240727-3.14.0a0-04eb5c8-JIT/bm-20240727-arminc-aarch64-python-04eb5c8db1e24cabd0cb-3.14.0a0-04eb5c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.08x

# Memory
- memory change: 1.23x