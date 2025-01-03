# Results vs. 3.10.4

- fork: eendebakpt
- ref: iter_freelists
- machine: linux-aarch64
- commit hash: 05f479c
- commit date: 2025-01-02
- overall geometric mean: 1.319x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                 |
| html5lib       | 86.5 ms                                                               | 67.1 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 873 ms: 2.62x faster                                                   |
| async_tree_none         | 950 ms                                                                | 383 ms: 2.48x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 486 ms: 2.33x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 671 ms: 1.89x faster                                                   |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.6 ms: 1.49x faster                                                  |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 128 ms: 1.38x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                  |
| regex_dna      | 257 ms                                                                | 248 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                   |
| json_dumps           | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.91 ms: 1.29x slower                                                  |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                  |
| mako            | 18.9 ms                                                               | 14.5 ms: 1.30x faster                                                  |
| genshi_text     | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 63.8 ms: 1.09x faster                                                  |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 202 us: 3.27x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 873 ms: 2.62x faster                                                   |
| async_tree_none          | 950 ms                                                                | 383 ms: 2.48x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 486 ms: 2.33x faster                                                   |
| deltablue                | 8.94 ms                                                               | 3.95 ms: 2.27x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 671 ms: 1.89x faster                                                   |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                                  |
| go                       | 264 ms                                                                | 146 ms: 1.81x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                                  |
| richards_super           | 107 ms                                                                | 61.6 ms: 1.74x faster                                                  |
| raytrace                 | 573 ms                                                                | 330 ms: 1.74x faster                                                   |
| chaos                    | 121 ms                                                                | 72.4 ms: 1.67x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.45 ms: 1.66x faster                                                  |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 84.6 ms: 1.58x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 1.81 ms: 1.57x faster                                                  |
| comprehensions           | 33.1 us                                                               | 21.1 us: 1.57x faster                                                  |
| logging_silent           | 222 ns                                                                | 142 ns: 1.56x faster                                                   |
| pylint                   | 485 ms                                                                | 312 ms: 1.56x faster                                                   |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 85.9 ms: 1.49x faster                                                  |
| float                    | 135 ms                                                                | 90.6 ms: 1.49x faster                                                  |
| deepcopy_memo            | 61.7 us                                                               | 41.5 us: 1.49x faster                                                  |
| deepcopy                 | 511 us                                                                | 345 us: 1.48x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.45 ms: 1.47x faster                                                  |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.44x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                   |
| regex_compile            | 177 ms                                                                | 128 ms: 1.38x faster                                                   |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                   |
| pyflate                  | 795 ms                                                                | 590 ms: 1.35x faster                                                   |
| thrift                   | 1.26 ms                                                               | 938 us: 1.34x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.93 us: 1.34x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.37 us: 1.33x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                 |
| sqlalchemy_declarative   | 197 ms                                                                | 151 ms: 1.31x faster                                                   |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.30x faster                                                  |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                 |
| mako                     | 18.9 ms                                                               | 14.5 ms: 1.30x faster                                                  |
| html5lib                 | 86.5 ms                                                               | 67.1 ms: 1.29x faster                                                  |
| coroutines               | 37.2 ms                                                               | 29.1 ms: 1.28x faster                                                  |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.27x faster                                                   |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.3 ms: 1.26x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 3.65 us: 1.26x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 124 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 28.0 ms: 1.26x faster                                                  |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                   |
| sympy_str                | 329 ms                                                                | 262 ms: 1.25x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.5 ms: 1.24x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 61.2 ms: 1.23x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 60.4 ms: 1.22x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 21.9 ms: 1.20x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.45 ms: 1.18x faster                                                  |
| scimark_fft              | 500 ms                                                                | 423 ms: 1.18x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 972 ms: 1.18x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.00 sec: 1.18x faster                                                 |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                 |
| sympy_expand             | 543 ms                                                                | 462 ms: 1.17x faster                                                   |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                   |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.7 ms: 1.13x faster                                                  |
| genshi_xml               | 69.8 ms                                                               | 63.8 ms: 1.09x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.40 sec: 1.09x faster                                                 |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.05x faster                                                  |
| regex_dna                | 257 ms                                                                | 248 ms: 1.04x faster                                                   |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                                  |
| async_generators         | 452 ms                                                                | 496 ms: 1.10x slower                                                   |
| mypy2                    | 936 ms                                                                | 1.05 sec: 1.13x slower                                                 |
| telco                    | 8.49 ms                                                               | 9.70 ms: 1.14x slower                                                  |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.91 ms: 1.29x slower                                                  |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 3.53 ms: 1.56x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 7.03 ms: 1.69x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 5.00 sec: 343.75x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                           |

Benchmark hidden because not significant (5): sqlite_synth, json, regex_v8, pidigits, asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250102-3.14.0a3+-05f479c/bm-20250102-arminc-aarch64-eendebakpt-iter_freelists-3.14.0a3+-05f479c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.319x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x