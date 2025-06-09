# Results vs. 3.10.4

- fork: python
- ref: v3.14.0b2
- machine: linux-aarch64
- commit hash: 12d3f88
- commit date: 2025-05-26
- overall geometric mean: 1.341x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 309 ms: 1.23x faster                                         |
| docutils       | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                       |
| html5lib       | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                        |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 883 ms: 2.59x faster                                         |
| async_tree_none         | 950 ms                                                                | 390 ms: 2.43x faster                                         |
| async_tree_memoization  | 1.13 sec                                                              | 467 ms: 2.42x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                         |
| Geometric mean          | (ref)                                                                 | 2.33x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 135 ms                                                                | 87.0 ms: 1.55x faster                                        |
| nbody          | 166 ms                                                                | 125 ms: 1.33x faster                                         |
| pidigits       | 235 ms                                                                | 241 ms: 1.02x slower                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                         |
| regex_v8       | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                        |
| regex_dna      | 257 ms                                                                | 233 ms: 1.10x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 3.88 ms: 1.09x faster                                        |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                       |
| unpickle_pure_python | 366 us                                                                | 268 us: 1.37x faster                                         |
| pickle_pure_python   | 529 us                                                                | 399 us: 1.33x faster                                         |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                        |
| xml_etree_process    | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 142 ms: 1.09x faster                                         |
| xml_etree_generate   | 123 ms                                                                | 114 ms: 1.07x faster                                         |
| json_loads           | 30.9 us                                                               | 35.9 us: 1.16x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                        |
| python_startup         | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.33x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                        |
| django_template | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.25x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 883 ms: 2.59x faster                                         |
| async_tree_none          | 950 ms                                                                | 390 ms: 2.43x faster                                         |
| async_tree_memoization   | 1.13 sec                                                              | 467 ms: 2.42x faster                                         |
| deltablue                | 8.94 ms                                                               | 3.84 ms: 2.33x faster                                        |
| mdp                      | 3.70 sec                                                              | 1.69 sec: 2.19x faster                                       |
| go                       | 264 ms                                                                | 131 ms: 2.02x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                         |
| generators               | 68.1 ms                                                               | 36.8 ms: 1.85x faster                                        |
| richards_super           | 107 ms                                                                | 59.0 ms: 1.82x faster                                        |
| richards                 | 91.7 ms                                                               | 52.3 ms: 1.75x faster                                        |
| chaos                    | 121 ms                                                                | 70.0 ms: 1.73x faster                                        |
| raytrace                 | 573 ms                                                                | 336 ms: 1.71x faster                                         |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                         |
| scimark_monte_carlo      | 128 ms                                                                | 79.4 ms: 1.61x faster                                        |
| crypto_pyaes             | 134 ms                                                                | 83.7 ms: 1.60x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 38.9 us: 1.59x faster                                        |
| pylint                   | 485 ms                                                                | 311 ms: 1.56x faster                                         |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                         |
| comprehensions           | 33.1 us                                                               | 21.3 us: 1.55x faster                                        |
| hexiom                   | 10.9 ms                                                               | 7.04 ms: 1.55x faster                                        |
| float                    | 135 ms                                                                | 87.0 ms: 1.55x faster                                        |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                         |
| pyflate                  | 795 ms                                                                | 535 ms: 1.49x faster                                         |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                         |
| spectral_norm            | 186 ms                                                                | 131 ms: 1.42x faster                                         |
| html5lib                 | 86.5 ms                                                               | 61.0 ms: 1.42x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 53.5 ms: 1.37x faster                                        |
| tomli_loads              | 3.36 sec                                                              | 2.45 sec: 1.37x faster                                       |
| unpickle_pure_python     | 366 us                                                                | 268 us: 1.37x faster                                         |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.36x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                       |
| django_template          | 53.3 ms                                                               | 39.9 ms: 1.34x faster                                        |
| pickle_pure_python       | 529 us                                                                | 399 us: 1.33x faster                                         |
| nbody                    | 166 ms                                                                | 125 ms: 1.33x faster                                         |
| sqlalchemy_declarative   | 197 ms                                                                | 150 ms: 1.31x faster                                         |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                        |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.27x faster                                        |
| deepcopy_reduce          | 4.60 us                                                               | 3.63 us: 1.27x faster                                        |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.26x faster                                       |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                        |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                        |
| logging_format           | 10.6 us                                                               | 8.47 us: 1.25x faster                                        |
| logging_simple           | 9.78 us                                                               | 7.81 us: 1.25x faster                                        |
| pprint_safe_repr         | 1.15 sec                                                              | 917 ms: 1.25x faster                                         |
| sympy_sum                | 184 ms                                                                | 148 ms: 1.24x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 80.4 ms: 1.24x faster                                        |
| 2to3                     | 381 ms                                                                | 309 ms: 1.23x faster                                         |
| coroutines               | 37.2 ms                                                               | 30.9 ms: 1.20x faster                                        |
| sympy_str                | 329 ms                                                                | 274 ms: 1.20x faster                                         |
| docutils                 | 3.53 sec                                                              | 2.97 sec: 1.19x faster                                       |
| nqueens                  | 117 ms                                                                | 99.1 ms: 1.19x faster                                        |
| fannkuch                 | 546 ms                                                                | 465 ms: 1.17x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                         |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                         |
| scimark_fft              | 500 ms                                                                | 433 ms: 1.16x faster                                         |
| regex_v8                 | 32.2 ms                                                               | 28.0 ms: 1.15x faster                                        |
| pathlib                  | 26.3 ms                                                               | 22.9 ms: 1.15x faster                                        |
| genshi_xml               | 69.8 ms                                                               | 61.4 ms: 1.14x faster                                        |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.11x faster                                         |
| regex_dna                | 257 ms                                                                | 233 ms: 1.10x faster                                         |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.93 ms: 1.10x faster                                        |
| regex_effbot             | 4.25 ms                                                               | 3.88 ms: 1.09x faster                                        |
| xml_etree_iterparse      | 156 ms                                                                | 142 ms: 1.09x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 114 ms: 1.07x faster                                         |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                        |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                         |
| json                     | 5.88 ms                                                               | 6.02 ms: 1.02x slower                                        |
| pidigits                 | 235 ms                                                                | 241 ms: 1.02x slower                                         |
| telco                    | 8.49 ms                                                               | 9.34 ms: 1.10x slower                                        |
| json_loads               | 30.9 us                                                               | 35.9 us: 1.16x slower                                        |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                         |
| python_startup_no_site   | 6.89 ms                                                               | 8.55 ms: 1.24x slower                                        |
| python_startup           | 11.2 ms                                                               | 15.9 ms: 1.42x slower                                        |
| gc_traversal             | 4.15 ms                                                               | 6.53 ms: 1.57x slower                                        |
| create_gc_cycles         | 2.26 ms                                                               | 3.66 ms: 1.62x slower                                        |
| logging_silent           | 222 ns                                                                | 633 ns: 2.85x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.30x faster                                                 |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250526-3.14.0b2-12d3f88/bm-20250526-arminc-aarch64-python-v3.14.0b2-3.14.0b2-12d3f88.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.341x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.34x