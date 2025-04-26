# Results vs. 3.10.4

- fork: python
- ref: ea8ec95cfadbf58a11ef
- machine: linux-aarch64
- commit hash: ea8ec95
- commit date: 2025-04-21
- overall geometric mean: 1.348x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.4 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 882 ms: 2.59x faster                                                     |
| async_tree_none         | 950 ms                                                                | 390 ms: 2.44x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 481 ms: 2.36x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.31x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.3 ms: 1.62x faster                                                    |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.32x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.73 ms: 1.14x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 29.0 ms: 1.11x faster                                                    |
| regex_dna      | 257 ms                                                                | 234 ms: 1.10x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.18x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 381 us: 1.39x faster                                                     |
| unpickle_pure_python | 366 us                                                                | 266 us: 1.38x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| json_loads           | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.19x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.22x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 882 ms: 2.59x faster                                                     |
| async_tree_none          | 950 ms                                                                | 390 ms: 2.44x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 481 ms: 2.36x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.96 ms: 2.26x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.68 sec: 2.20x faster                                                   |
| go                       | 264 ms                                                                | 132 ms: 2.00x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                     |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                                    |
| richards_super           | 107 ms                                                                | 58.6 ms: 1.83x faster                                                    |
| raytrace                 | 573 ms                                                                | 324 ms: 1.77x faster                                                     |
| chaos                    | 121 ms                                                                | 69.2 ms: 1.75x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.5 ms: 1.71x faster                                                    |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.67x faster                                                     |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 37.6 us: 1.64x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 82.5 ms: 1.62x faster                                                    |
| float                    | 135 ms                                                                | 83.3 ms: 1.62x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 79.8 ms: 1.60x faster                                                    |
| deepcopy                 | 511 us                                                                | 329 us: 1.55x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.5 us: 1.54x faster                                                    |
| pylint                   | 485 ms                                                                | 315 ms: 1.54x faster                                                     |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.28 ms: 1.50x faster                                                    |
| pyflate                  | 795 ms                                                                | 531 ms: 1.50x faster                                                     |
| spectral_norm            | 186 ms                                                                | 126 ms: 1.48x faster                                                     |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                     |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 51.9 ms: 1.41x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.01 us: 1.39x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 381 us: 1.39x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 62.4 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 266 us: 1.38x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.82 us: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.6 ms: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.27 sec: 1.33x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 26.5 ms: 1.33x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.51 us: 1.31x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.7 ms: 1.31x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 891 ms: 1.29x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.83 sec: 1.29x faster                                                   |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                     |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                    |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                    |
| sympy_str                | 329 ms                                                                | 271 ms: 1.21x faster                                                     |
| scimark_fft              | 500 ms                                                                | 414 ms: 1.21x faster                                                     |
| nqueens                  | 117 ms                                                                | 97.3 ms: 1.21x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 459 ms: 1.18x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 14.2 ms: 1.18x faster                                                    |
| fannkuch                 | 546 ms                                                                | 464 ms: 1.18x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 181 ms: 1.17x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 22.7 ms: 1.16x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.5 ms: 1.15x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.73 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.72 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 29.0 ms: 1.11x faster                                                    |
| regex_dna                | 257 ms                                                                | 234 ms: 1.10x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.86 us: 1.07x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 672 ms: 1.02x slower                                                     |
| json_loads               | 30.9 us                                                               | 34.5 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.59 ms: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 102 ms: 1.22x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.54 ms: 1.57x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.54 ms: 1.57x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 4.59 sec: 315.52x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (3): async_generators, pidigits, json
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250421-3.14.0a7+-ea8ec95/bm-20250421-arminc-aarch64-python-ea8ec95cfadbf58a11ef-3.14.0a7+-ea8ec95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.348x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.31x