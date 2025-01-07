# Results vs. 3.10.4

- fork: kumaraditya303
- ref: fast_state
- machine: linux-aarch64
- commit hash: 7de6e22
- commit date: 2025-01-07
- overall geometric mean: 1.308x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.24x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                 |
| html5lib       | 86.5 ms                                                               | 67.6 ms: 1.28x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 888 ms: 2.57x faster                                                   |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 495 ms: 2.29x faster                                                   |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 674 ms: 1.89x faster                                                   |
| Geometric mean          | (ref)                                                                 | 2.28x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 92.6 ms: 1.45x faster                                                  |
| nbody          | 166 ms                                                                | 122 ms: 1.36x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                   |
| regex_dna      | 257 ms                                                                | 251 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                           |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 265 us: 1.38x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 405 us: 1.31x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                   |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                           |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.88 ms: 1.29x slower                                                  |
| python_startup         | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.36x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                  |
| django_template | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                  |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.26x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 64.4 ms: 1.08x faster                                                  |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 207 us: 3.19x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 888 ms: 2.57x faster                                                   |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 495 ms: 2.29x faster                                                   |
| deltablue                | 8.94 ms                                                               | 3.98 ms: 2.25x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 674 ms: 1.89x faster                                                   |
| generators               | 68.1 ms                                                               | 37.1 ms: 1.84x faster                                                  |
| go                       | 264 ms                                                                | 146 ms: 1.81x faster                                                   |
| richards_super           | 107 ms                                                                | 60.1 ms: 1.78x faster                                                  |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                                  |
| raytrace                 | 573 ms                                                                | 326 ms: 1.76x faster                                                   |
| chaos                    | 121 ms                                                                | 71.8 ms: 1.69x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.46 ms: 1.65x faster                                                  |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                   |
| logging_silent           | 222 ns                                                                | 140 ns: 1.58x faster                                                   |
| pylint                   | 485 ms                                                                | 307 ms: 1.58x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 85.4 ms: 1.57x faster                                                  |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.85 ms: 1.54x faster                                                  |
| deepcopy                 | 511 us                                                                | 338 us: 1.51x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 41.1 us: 1.50x faster                                                  |
| comprehensions           | 33.1 us                                                               | 22.1 us: 1.50x faster                                                  |
| float                    | 135 ms                                                                | 92.6 ms: 1.45x faster                                                  |
| scimark_monte_carlo      | 128 ms                                                                | 88.0 ms: 1.45x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 7.52 ms: 1.45x faster                                                  |
| spectral_norm            | 186 ms                                                                | 133 ms: 1.41x faster                                                   |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 265 us: 1.38x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.14 us: 1.37x faster                                                  |
| nbody                    | 166 ms                                                                | 122 ms: 1.36x faster                                                   |
| sqlalchemy_declarative   | 197 ms                                                                | 145 ms: 1.36x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.93 us: 1.34x faster                                                  |
| pyflate                  | 795 ms                                                                | 595 ms: 1.34x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                  |
| django_template          | 53.3 ms                                                               | 40.5 ms: 1.32x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                 |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.7 ms: 1.31x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 405 us: 1.31x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.60 sec: 1.29x faster                                                 |
| html5lib                 | 86.5 ms                                                               | 67.6 ms: 1.28x faster                                                  |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.26x faster                                                  |
| thrift                   | 1.26 ms                                                               | 998 us: 1.26x faster                                                   |
| coroutines               | 37.2 ms                                                               | 29.5 ms: 1.26x faster                                                  |
| deepcopy_reduce          | 4.60 us                                                               | 3.69 us: 1.25x faster                                                  |
| 2to3                     | 381 ms                                                                | 306 ms: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 81.6 ms: 1.22x faster                                                  |
| sympy_str                | 329 ms                                                                | 270 ms: 1.22x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.8 ms: 1.22x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 14.0 ms: 1.19x faster                                                  |
| dulwich_log              | 73.5 ms                                                               | 61.6 ms: 1.19x faster                                                  |
| pprint_pformat           | 2.36 sec                                                              | 1.98 sec: 1.19x faster                                                 |
| pprint_safe_repr         | 1.15 sec                                                              | 966 ms: 1.19x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 63.6 ms: 1.19x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 22.2 ms: 1.19x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.17x faster                                                  |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.16x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.56 ms: 1.16x faster                                                  |
| docutils                 | 3.53 sec                                                              | 3.04 sec: 1.16x faster                                                 |
| sympy_expand             | 543 ms                                                                | 482 ms: 1.13x faster                                                   |
| fannkuch                 | 546 ms                                                                | 492 ms: 1.11x faster                                                   |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 64.4 ms: 1.08x faster                                                  |
| mdp                      | 3.70 sec                                                              | 3.43 sec: 1.08x faster                                                 |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                   |
| meteor_contest           | 126 ms                                                                | 118 ms: 1.07x faster                                                   |
| json                     | 5.88 ms                                                               | 5.62 ms: 1.04x faster                                                  |
| regex_dna                | 257 ms                                                                | 251 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 676 ms: 1.03x slower                                                   |
| async_generators         | 452 ms                                                                | 491 ms: 1.09x slower                                                   |
| mypy2                    | 936 ms                                                                | 1.06 sec: 1.13x slower                                                 |
| telco                    | 8.49 ms                                                               | 9.68 ms: 1.14x slower                                                  |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.88 ms: 1.29x slower                                                  |
| python_startup           | 11.2 ms                                                               | 16.1 ms: 1.44x slower                                                  |
| create_gc_cycles         | 2.26 ms                                                               | 3.68 ms: 1.63x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 6.99 ms: 1.68x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 5.70 sec: 391.96x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                           |

Benchmark hidden because not significant (5): regex_effbot, sqlite_synth, json_loads, pidigits, regex_v8
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250107-3.14.0a3+-7de6e22/bm-20250107-arminc-aarch64-kumaraditya303-fast_state-3.14.0a3+-7de6e22.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.308x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.30x