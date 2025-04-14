# Results vs. 3.10.4

- fork: python
- ref: 7bb1e1a23634bae81bf7
- machine: linux-x86_64
- commit hash: 7bb1e1a
- commit date: 2025-04-06
- overall geometric mean: 1.365x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 275 ms: 1.28x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.86 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                         |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.43x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 509 ms: 1.84x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| nbody          | 134 ms                                                       | 93.9 ms: 1.43x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| regex_dna      | 261 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.03 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 332 us: 1.37x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.5 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 84.3 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                        |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.13x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                         |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.43x faster                                                         |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.25 ms: 2.31x faster                                                        |
| go                       | 262 ms                                                       | 124 ms: 2.11x faster                                                         |
| generators               | 57.3 ms                                                      | 28.1 ms: 2.04x faster                                                        |
| chaos                    | 109 ms                                                       | 58.5 ms: 1.86x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 509 ms: 1.84x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 59.4 ms: 1.81x faster                                                        |
| logging_silent           | 167 ns                                                       | 92.9 ns: 1.80x faster                                                        |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.78x faster                                                        |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                         |
| pyflate                  | 733 ms                                                       | 422 ms: 1.74x faster                                                         |
| richards_super           | 90.6 ms                                                      | 52.4 ms: 1.73x faster                                                        |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                         |
| scimark_lu               | 167 ms                                                       | 97.8 ms: 1.71x faster                                                        |
| deepcopy                 | 468 us                                                       | 281 us: 1.67x faster                                                         |
| richards                 | 75.1 ms                                                      | 46.1 ms: 1.63x faster                                                        |
| float                    | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| spectral_norm            | 139 ms                                                       | 87.3 ms: 1.59x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.54x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.16 ms: 1.53x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 79.1 ms: 1.51x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.13 us: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                        |
| nbody                    | 134 ms                                                       | 93.9 ms: 1.43x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.81 us: 1.42x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.8 ms: 1.40x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 332 us: 1.37x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.35x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 779 ms: 1.35x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.8 ms: 1.32x faster                                                        |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 62.4 ms: 1.30x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                        |
| 2to3                     | 350 ms                                                       | 275 ms: 1.28x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 59.6 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.2 ms: 1.27x faster                                                        |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                         |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.25x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.3 ms: 1.23x faster                                                        |
| sympy_expand             | 600 ms                                                       | 488 ms: 1.23x faster                                                         |
| nqueens                  | 115 ms                                                       | 93.7 ms: 1.23x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.8 ms: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.86 sec: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 135 ms: 1.18x faster                                                         |
| bench_thread_pool        | 1.14 ms                                                      | 968 us: 1.18x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.5 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.7 us: 1.14x faster                                                        |
| regex_dna                | 261 ms                                                       | 232 ms: 1.12x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 84.3 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| json                     | 5.86 ms                                                      | 5.50 ms: 1.07x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.77 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 411 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.03 ms: 1.02x faster                                                        |
| telco                    | 7.23 ms                                                      | 7.85 ms: 1.09x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.39 ms: 1.87x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.19 sec: 187.16x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250406-3.14.0a6+-7bb1e1a/bm-20250406-pythonperf2-x86_64-python-7bb1e1a23634bae81bf7-3.14.0a6+-7bb1e1a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.29x