# Results vs. 3.10.4

- fork: mdboom
- ref: remove_redundant_typ
- machine: linux-aarch64
- commit hash: b0f5f3a
- commit date: 2024-09-23
- overall geometric mean: 1.32x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| tornado_http   | 178 ms                                                                | 124 ms: 1.44x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 419 ms: 2.27x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 553 ms: 2.05x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.01x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| float          | 135 ms                                                                | 93.3 ms: 1.44x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 79.3 ms: 1.25x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.54 us: 1.07x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.26 us: 1.00x slower                                                   |
| json_loads           | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                   |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 61.8 ms: 1.13x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 194 us: 3.40x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 419 ms: 2.27x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 553 ms: 2.05x faster                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.12 ms: 2.04x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.00x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 138 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                                    |
| richards_super           | 107 ms                                                                | 59.1 ms: 1.82x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 723 ms: 1.76x faster                                                    |
| chaos                    | 121 ms                                                                | 68.9 ms: 1.76x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.39 ms: 1.72x faster                                                   |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 561 ms: 1.68x faster                                                    |
| scimark_lu               | 227 ms                                                                | 136 ms: 1.67x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 81.4 ms: 1.65x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.63x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.0 us: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                   |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 83.6 ms: 1.53x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.19 sec: 1.50x faster                                                  |
| nbody                    | 166 ms                                                                | 111 ms: 1.49x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.47x faster                                                    |
| float                    | 135 ms                                                                | 93.3 ms: 1.44x faster                                                   |
| tornado_http             | 178 ms                                                                | 124 ms: 1.44x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                   |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.02 us: 1.39x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.22 sec: 1.39x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.65 us: 1.39x faster                                                   |
| pyflate                  | 795 ms                                                                | 580 ms: 1.37x faster                                                    |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                    |
| thrift                   | 1.26 ms                                                               | 932 us: 1.35x faster                                                    |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                    |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.2 ms: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 295 ms: 1.29x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.23 ms: 1.29x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.65 sec: 1.27x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 914 ms: 1.26x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 79.3 ms: 1.25x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.25x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 59.4 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.5 ms: 1.21x faster                                                   |
| fannkuch                 | 546 ms                                                                | 459 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.53 ms: 1.17x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.17x faster                                                  |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 61.8 ms: 1.13x faster                                                   |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.31 sec: 1.12x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| unpickle_list            | 6.99 us                                                               | 6.54 us: 1.07x faster                                                   |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                                   |
| sqlite_synth             | 4.12 us                                                               | 3.89 us: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.5 ms: 1.05x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 252 ms: 1.02x faster                                                    |
| pickle_list              | 5.24 us                                                               | 5.26 us: 1.00x slower                                                   |
| json_loads               | 30.9 us                                                               | 31.7 us: 1.02x slower                                                   |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 38.3 us: 1.09x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.96 ms: 1.17x slower                                                   |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.2 ms: 1.19x slower                                                   |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.09 ms: 1.23x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240923-3.14.0a0-b0f5f3a/bm-20240923-arminc-aarch64-mdboom-remove_redundant_typ-3.14.0a0-b0f5f3a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.13x