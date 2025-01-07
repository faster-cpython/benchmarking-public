# Results vs. 3.10.4

- fork: kumaraditya303
- ref: future_iter
- machine: linux-aarch64
- commit hash: 82b905d
- commit date: 2025-01-05
- overall geometric mean: 1.311x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 308 ms: 1.24x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 875 ms: 2.61x faster                                                    |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 486 ms: 2.33x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 670 ms: 1.90x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 92.5 ms: 1.46x faster                                                   |
| nbody          | 166 ms                                                                | 126 ms: 1.32x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                    |
| regex_dna      | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 261 us: 1.40x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 393 us: 1.35x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| xml_etree_process    | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 140 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 115 ms: 1.07x faster                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                            |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.94 ms: 1.30x slower                                                   |
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.37x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                   |
| django_template | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 63.8 ms: 1.09x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.22x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 206 us: 3.22x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 875 ms: 2.61x faster                                                    |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 486 ms: 2.33x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.00 ms: 2.24x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 670 ms: 1.90x faster                                                    |
| generators               | 68.1 ms                                                               | 36.3 ms: 1.88x faster                                                   |
| go                       | 264 ms                                                                | 144 ms: 1.83x faster                                                    |
| raytrace                 | 573 ms                                                                | 322 ms: 1.78x faster                                                    |
| richards_super           | 107 ms                                                                | 61.1 ms: 1.76x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.6 ms: 1.71x faster                                                   |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| chaos                    | 121 ms                                                                | 72.6 ms: 1.67x faster                                                   |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                                    |
| scimark_sor              | 246 ms                                                                | 151 ms: 1.63x faster                                                    |
| logging_silent           | 222 ns                                                                | 137 ns: 1.62x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.80 ms: 1.58x faster                                                   |
| pylint                   | 485 ms                                                                | 308 ms: 1.58x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 85.4 ms: 1.57x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 41.3 us: 1.50x faster                                                   |
| comprehensions           | 33.1 us                                                               | 22.3 us: 1.48x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.39 ms: 1.48x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                                   |
| float                    | 135 ms                                                                | 92.5 ms: 1.46x faster                                                   |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.44x faster                                                    |
| deepcopy                 | 511 us                                                                | 356 us: 1.43x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 261 us: 1.40x faster                                                    |
| pyflate                  | 795 ms                                                                | 579 ms: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 393 us: 1.35x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.94 us: 1.34x faster                                                   |
| logging_simple           | 9.78 us                                                               | 7.35 us: 1.33x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.28 sec: 1.33x faster                                                  |
| sqlalchemy_declarative   | 197 ms                                                                | 149 ms: 1.32x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.6 ms: 1.32x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.4 ms: 1.32x faster                                                   |
| nbody                    | 166 ms                                                                | 126 ms: 1.32x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.6 ms: 1.32x faster                                                   |
| thrift                   | 1.26 ms                                                               | 972 us: 1.30x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.62 sec: 1.28x faster                                                  |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.27x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.0 ms: 1.27x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.72 us: 1.24x faster                                                   |
| 2to3                     | 381 ms                                                                | 308 ms: 1.24x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.22 ms: 1.23x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 81.3 ms: 1.22x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.8 ms: 1.21x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 22.1 ms: 1.20x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.97 sec: 1.20x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 29.4 ms: 1.20x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.33 ms: 1.20x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 962 ms: 1.19x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 62.3 ms: 1.18x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 132 ms: 1.18x faster                                                    |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 14.3 ms: 1.17x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 64.6 ms: 1.17x faster                                                   |
| scimark_fft              | 500 ms                                                                | 430 ms: 1.16x faster                                                    |
| sympy_str                | 329 ms                                                                | 286 ms: 1.15x faster                                                    |
| sympy_expand             | 543 ms                                                                | 478 ms: 1.14x faster                                                    |
| nqueens                  | 117 ms                                                                | 104 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 483 ms: 1.13x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 140 ms: 1.11x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 63.8 ms: 1.09x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.42 sec: 1.08x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 115 ms: 1.07x faster                                                    |
| json                     | 5.88 ms                                                               | 5.52 ms: 1.07x faster                                                   |
| regex_dna                | 257 ms                                                                | 245 ms: 1.05x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.05 us: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                    |
| async_generators         | 452 ms                                                                | 497 ms: 1.10x slower                                                    |
| mypy2                    | 936 ms                                                                | 1.05 sec: 1.12x slower                                                  |
| telco                    | 8.49 ms                                                               | 9.99 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 8.94 ms: 1.30x slower                                                   |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 3.60 ms: 1.59x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 6.69 ms: 1.61x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 4.57 sec: 314.14x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.20x faster                                                            |

Benchmark hidden because not significant (5): regex_effbot, meteor_contest, regex_v8, json_loads, pidigits
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250105-3.14.0a3+-82b905d/bm-20250105-arminc-aarch64-kumaraditya303-future_iter-3.14.0a3+-82b905d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.311x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x