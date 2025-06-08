# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-aarch64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.041x slower
- HPT reliability: 99.06%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.44 sec: 1.03x faster                                                  |
| html5lib       | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 979 ms: 2.33x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 509 ms: 2.23x faster                                                    |
| async_tree_none         | 950 ms                                                                | 433 ms: 2.19x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 805 ms: 1.58x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.06x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 135 ms                                                                | 97.2 ms: 1.39x faster                                                   |
| nbody          | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| pidigits       | 235 ms                                                                | 281 ms: 1.19x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.12x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 152 ms: 1.16x faster                                                    |
| regex_dna      | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| regex_effbot   | 4.25 ms                                                               | 4.03 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.10x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.86 sec: 1.17x faster                                                  |
| unpickle_pure_python | 366 us                                                                | 321 us: 1.14x faster                                                    |
| pickle_pure_python   | 529 us                                                                | 471 us: 1.12x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| xml_etree_process    | 99.5 ms                                                               | 106 ms: 1.06x slower                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 168 ms: 1.08x slower                                                    |
| xml_etree_parse      | 212 ms                                                                | 230 ms: 1.09x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 43.3 us: 1.23x slower                                                   |
| json_loads           | 30.9 us                                                               | 38.6 us: 1.25x slower                                                   |
| unpickle             | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| xml_etree_generate   | 123 ms                                                                | 160 ms: 1.30x slower                                                    |
| pickle_list          | 5.24 us                                                               | 7.19 us: 1.37x slower                                                   |
| pickle               | 12.5 us                                                               | 19.7 us: 1.58x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.12x slower                                                            |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.58 ms: 1.39x slower                                                   |
| python_startup         | 11.2 ms                                                               | 16.9 ms: 1.51x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.45x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 17.4 ms: 1.09x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                   |
| django_template | 53.3 ms                                                               | 52.6 ms: 1.01x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 74.3 ms: 1.06x slower                                                   |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 259 us: 2.55x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 979 ms: 2.33x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 509 ms: 2.23x faster                                                    |
| async_tree_none          | 950 ms                                                                | 433 ms: 2.19x faster                                                    |
| deltablue                | 8.94 ms                                                               | 4.50 ms: 1.99x faster                                                   |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.98 sec: 1.87x faster                                                  |
| generators               | 68.1 ms                                                               | 40.3 ms: 1.69x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 581 ms: 1.63x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 805 ms: 1.58x faster                                                    |
| richards_super           | 107 ms                                                                | 71.8 ms: 1.49x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.26 sec: 1.45x faster                                                  |
| richards                 | 91.7 ms                                                               | 63.5 ms: 1.44x faster                                                   |
| chaos                    | 121 ms                                                                | 83.9 ms: 1.44x faster                                                   |
| comprehensions           | 33.1 us                                                               | 23.0 us: 1.44x faster                                                   |
| raytrace                 | 573 ms                                                                | 400 ms: 1.43x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 44.0 us: 1.40x faster                                                   |
| scimark_sor              | 246 ms                                                                | 176 ms: 1.40x faster                                                    |
| float                    | 135 ms                                                                | 97.2 ms: 1.39x faster                                                   |
| pyflate                  | 795 ms                                                                | 584 ms: 1.36x faster                                                    |
| pylint                   | 485 ms                                                                | 373 ms: 1.30x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 98.2 ms: 1.30x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 103 ms: 1.30x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 8.40 ms: 1.30x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 67.4 ms: 1.28x faster                                                   |
| deepcopy                 | 511 us                                                                | 405 us: 1.26x faster                                                    |
| scimark_lu               | 227 ms                                                                | 188 ms: 1.21x faster                                                    |
| nbody                    | 166 ms                                                                | 138 ms: 1.20x faster                                                    |
| spectral_norm            | 186 ms                                                                | 156 ms: 1.20x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 62.0 ms: 1.19x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.86 sec: 1.17x faster                                                  |
| regex_compile            | 177 ms                                                                | 152 ms: 1.16x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                                  |
| unpickle_pure_python     | 366 us                                                                | 321 us: 1.14x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 471 us: 1.12x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 23.6 ms: 1.12x faster                                                   |
| regex_dna                | 257 ms                                                                | 231 ms: 1.11x faster                                                    |
| coroutines               | 37.2 ms                                                               | 34.0 ms: 1.09x faster                                                   |
| mako                     | 18.9 ms                                                               | 17.4 ms: 1.09x faster                                                   |
| 2to3                     | 381 ms                                                                | 352 ms: 1.08x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.1 ms: 1.07x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.49 ms: 1.07x faster                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.03 ms: 1.06x faster                                                   |
| logging_simple           | 9.78 us                                                               | 9.33 us: 1.05x faster                                                   |
| logging_format           | 10.6 us                                                               | 10.2 us: 1.04x faster                                                   |
| genshi_text              | 35.2 ms                                                               | 33.9 ms: 1.04x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.44 sec: 1.03x faster                                                  |
| django_template          | 53.3 ms                                                               | 52.6 ms: 1.01x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 664 ms: 1.01x slower                                                    |
| pathlib                  | 26.3 ms                                                               | 26.6 ms: 1.01x slower                                                   |
| meteor_contest           | 126 ms                                                                | 128 ms: 1.01x slower                                                    |
| json_dumps               | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                   |
| xml_etree_process        | 99.5 ms                                                               | 106 ms: 1.06x slower                                                    |
| nqueens                  | 117 ms                                                                | 125 ms: 1.06x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 74.3 ms: 1.06x slower                                                   |
| sympy_expand             | 543 ms                                                                | 585 ms: 1.08x slower                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 168 ms: 1.08x slower                                                    |
| xml_etree_parse          | 212 ms                                                                | 230 ms: 1.09x slower                                                    |
| fannkuch                 | 546 ms                                                                | 593 ms: 1.09x slower                                                    |
| pprint_pformat           | 2.36 sec                                                              | 2.64 sec: 1.12x slower                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 1.30 sec: 1.13x slower                                                  |
| async_generators         | 452 ms                                                                | 519 ms: 1.15x slower                                                    |
| json                     | 5.88 ms                                                               | 7.02 ms: 1.19x slower                                                   |
| pidigits                 | 235 ms                                                                | 281 ms: 1.19x slower                                                    |
| sqlite_synth             | 4.12 us                                                               | 4.92 us: 1.20x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 43.3 us: 1.23x slower                                                   |
| json_loads               | 30.9 us                                                               | 38.6 us: 1.25x slower                                                   |
| unpickle                 | 17.5 us                                                               | 22.5 us: 1.29x slower                                                   |
| xml_etree_generate       | 123 ms                                                                | 160 ms: 1.30x slower                                                    |
| pickle_list              | 5.24 us                                                               | 7.19 us: 1.37x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 9.58 ms: 1.39x slower                                                   |
| python_startup           | 11.2 ms                                                               | 16.9 ms: 1.51x slower                                                   |
| telco                    | 8.49 ms                                                               | 13.4 ms: 1.57x slower                                                   |
| pickle                   | 12.5 us                                                               | 19.7 us: 1.58x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 4.05 ms: 1.79x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 7.47 ms: 1.80x slower                                                   |
| logging_silent           | 222 ns                                                                | 929 ns: 4.19x slower                                                    |
| coverage                 | 83.6 ms                                                               | 695 ms: 8.31x slower                                                    |
| thrift                   | 1.26 ms                                                               | 196 ms: 155.92x slower                                                  |
| bench_mp_pool            | 14.5 ms                                                               | 6.68 sec: 459.95x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.08x slower                                                            |

Benchmark hidden because not significant (6): sympy_sum, unpickle_list, scimark_fft, sympy_str, deepcopy_reduce, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-arminc-aarch64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.06% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.38x