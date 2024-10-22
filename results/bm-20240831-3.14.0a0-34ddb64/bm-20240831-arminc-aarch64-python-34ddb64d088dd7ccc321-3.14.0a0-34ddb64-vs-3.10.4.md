# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-aarch64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                  |
| html5lib       | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 422 ms: 2.25x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.12 sec: 2.04x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 559 ms: 2.03x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| float          | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.41x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                   |
| regex_dna      | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 356 us: 1.49x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.43x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 422 ms: 2.25x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.00 ms: 2.08x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.12 sec: 2.04x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 559 ms: 2.03x faster                                                    |
| generators               | 68.1 ms                                                               | 35.0 ms: 1.95x faster                                                   |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                                    |
| raytrace                 | 573 ms                                                                | 301 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 60.7 ms: 1.77x faster                                                   |
| chaos                    | 121 ms                                                                | 68.6 ms: 1.77x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 726 ms: 1.75x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.72x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 551 ms: 1.71x faster                                                    |
| logging_silent           | 222 ns                                                                | 131 ns: 1.70x faster                                                    |
| richards                 | 91.7 ms                                                               | 54.3 ms: 1.69x faster                                                   |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 83.3 ms: 1.61x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.8 us: 1.60x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.5 ms: 1.55x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.13 ms: 1.53x faster                                                   |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.16 sec: 1.52x faster                                                  |
| deepcopy                 | 511 us                                                                | 337 us: 1.52x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 356 us: 1.49x faster                                                    |
| float                    | 135 ms                                                                | 92.7 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.43x faster                                                   |
| logging_simple           | 9.78 us                                                               | 6.91 us: 1.41x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.41x faster                                                    |
| pyflate                  | 795 ms                                                                | 567 ms: 1.40x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.64 us: 1.39x faster                                                   |
| tornado_http             | 178 ms                                                                | 129 ms: 1.38x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 63.7 ms: 1.36x faster                                                   |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 931 us: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.32x faster                                                    |
| coroutines               | 37.2 ms                                                               | 28.3 ms: 1.31x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.51 us: 1.31x faster                                                   |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.31x faster                                                    |
| 2to3                     | 381 ms                                                                | 294 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.4 ms: 1.29x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 915 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.7 ms: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.0 ms: 1.25x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.4 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.5 ms: 1.21x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.40 ms: 1.19x faster                                                   |
| nqueens                  | 117 ms                                                                | 99.9 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 465 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.0 ms: 1.16x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                  |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.2 ms: 1.07x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 150 ms: 1.04x faster                                                    |
| json                     | 5.88 ms                                                               | 5.70 ms: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 254 ms: 1.01x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                                   |
| async_generators         | 452 ms                                                                | 474 ms: 1.05x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.76 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.1 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 4.99 ms: 1.20x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.77 ms: 1.27x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.35x faster                                                            |

Benchmark hidden because not significant (2): pidigits, asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-arminc-aarch64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x