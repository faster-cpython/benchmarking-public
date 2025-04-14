# Results vs. 3.10.4

- fork: python
- ref: 470a0a68ebbbb4254f1a
- machine: linux-x86_64
- commit hash: 470a0a6
- commit date: 2025-01-22
- overall geometric mean: 1.352x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 622 ms: 2.57x faster                                                         |
| async_tree_none         | 692 ms                                                       | 274 ms: 2.52x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 507 ms: 1.85x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 70.5 ms: 1.58x faster                                                        |
| nbody          | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.10x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 62.0 ms: 1.22x faster                                                        |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 97.0 ms: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.6 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                        |
| mako            | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.8 ms: 1.16x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.03x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 622 ms: 2.57x faster                                                         |
| async_tree_none          | 692 ms                                                       | 274 ms: 2.52x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 341 ms: 2.40x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.29 ms: 2.28x faster                                                        |
| go                       | 262 ms                                                       | 128 ms: 2.05x faster                                                         |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 507 ms: 1.85x faster                                                         |
| pylint                   | 566 ms                                                       | 315 ms: 1.80x faster                                                         |
| chaos                    | 109 ms                                                       | 61.1 ms: 1.78x faster                                                        |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.3 ms: 1.77x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 61.6 ms: 1.75x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.5 ns: 1.73x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.31 ms: 1.70x faster                                                        |
| pyflate                  | 733 ms                                                       | 431 ms: 1.70x faster                                                         |
| richards_super           | 90.6 ms                                                      | 53.4 ms: 1.70x faster                                                        |
| deepcopy                 | 468 us                                                       | 283 us: 1.65x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.7 ms: 1.64x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                        |
| spectral_norm            | 139 ms                                                       | 85.4 ms: 1.63x faster                                                        |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                                         |
| sqlglot_transpile        | 2.68 ms                                                      | 1.69 ms: 1.59x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 75.4 ms: 1.58x faster                                                        |
| float                    | 111 ms                                                       | 70.5 ms: 1.58x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.98 ms: 1.58x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.2 ms: 1.43x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.07 sec: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 68.0 ms: 1.39x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.44 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.93 us: 1.37x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.58 sec: 1.36x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                         |
| thrift                   | 1.18 ms                                                      | 865 us: 1.36x faster                                                         |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 782 ms: 1.34x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                        |
| mako                     | 14.7 ms                                                      | 11.0 ms: 1.33x faster                                                        |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 144 ms: 1.31x faster                                                         |
| nqueens                  | 115 ms                                                       | 87.9 ms: 1.31x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.44 sec: 1.23x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 930 us: 1.23x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 62.0 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.22x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 67.2 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 58.3 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.19x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.8 ms: 1.16x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.44 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.0 ms: 1.14x faster                                                        |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                         |
| json                     | 5.86 ms                                                      | 5.31 ms: 1.10x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 83.6 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 398 ms: 1.06x faster                                                         |
| regex_dna                | 261 ms                                                       | 251 ms: 1.04x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.27 ms: 1.14x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.98 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.0 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.78 ms: 1.58x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.11 ms: 1.79x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.63 sec: 255.39x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250122-3.14.0a4+-470a0a6/bm-20250122-pythonperf2-x86_64-python-470a0a68ebbbb4254f1a-3.14.0a4+-470a0a6.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.352x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.27x