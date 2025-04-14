# Results vs. 3.10.4

- fork: kumaraditya303
- ref: per_thread_tasks
- machine: linux-x86_64
- commit hash: 4014e70
- commit date: 2025-01-29
- overall geometric mean: 1.342x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.64x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                             |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                           |
| html5lib       | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 644 ms: 2.48x faster                                                             |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                             |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 516 ms: 1.82x faster                                                             |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.6 ms: 1.60x faster                                                            |
| nbody          | 134 ms                                                       | 89.4 ms: 1.50x faster                                                            |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                             |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.41x faster                                                             |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                            |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                             |
| regex_effbot   | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                             |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 322 us: 1.41x faster                                                             |
| xml_etree_process    | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 106 ms: 1.05x faster                                                             |
| json_loads           | 30.3 us                                                      | 37.8 us: 1.25x slower                                                            |
| Geometric mean       | (ref)                                                        | 1.21x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                            |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_text     | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                            |
| django_template | 50.2 ms                                                      | 36.8 ms: 1.36x faster                                                            |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                            |
| genshi_xml      | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.11x faster                                                             |
| async_tree_io            | 1.60 sec                                                     | 644 ms: 2.48x faster                                                             |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                             |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                             |
| deltablue                | 7.50 ms                                                      | 3.37 ms: 2.23x faster                                                            |
| go                       | 262 ms                                                       | 129 ms: 2.03x faster                                                             |
| generators               | 57.3 ms                                                      | 28.6 ms: 2.01x faster                                                            |
| chaos                    | 109 ms                                                       | 58.7 ms: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 516 ms: 1.82x faster                                                             |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                             |
| pylint                   | 566 ms                                                       | 317 ms: 1.79x faster                                                             |
| scimark_lu               | 167 ms                                                       | 95.4 ms: 1.75x faster                                                            |
| logging_silent           | 167 ns                                                       | 97.5 ns: 1.72x faster                                                            |
| pyflate                  | 733 ms                                                       | 429 ms: 1.71x faster                                                             |
| richards_super           | 90.6 ms                                                      | 53.1 ms: 1.71x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.68x faster                                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                                            |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                             |
| scimark_monte_carlo      | 107 ms                                                       | 64.9 ms: 1.66x faster                                                            |
| spectral_norm            | 139 ms                                                       | 84.0 ms: 1.66x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                                            |
| scimark_sor              | 180 ms                                                       | 112 ms: 1.61x faster                                                             |
| float                    | 111 ms                                                       | 69.6 ms: 1.60x faster                                                            |
| richards                 | 75.1 ms                                                      | 47.9 ms: 1.57x faster                                                            |
| sqlglot_transpile        | 2.68 ms                                                      | 1.72 ms: 1.56x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                            |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                             |
| nbody                    | 134 ms                                                       | 89.4 ms: 1.50x faster                                                            |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.09 us: 1.46x faster                                                            |
| logging_format           | 9.64 us                                                      | 6.77 us: 1.42x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 66.5 ms: 1.42x faster                                                            |
| regex_compile            | 190 ms                                                       | 134 ms: 1.41x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 322 us: 1.41x faster                                                             |
| thrift                   | 1.18 ms                                                      | 846 us: 1.39x faster                                                             |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 15.5 ms: 1.37x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 23.0 ms: 1.37x faster                                                            |
| django_template          | 50.2 ms                                                      | 36.8 ms: 1.36x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.35x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 786 ms: 1.34x faster                                                             |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                             |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                           |
| fannkuch                 | 483 ms                                                       | 368 ms: 1.31x faster                                                             |
| nqueens                  | 115 ms                                                       | 87.9 ms: 1.31x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 58.4 ms: 1.30x faster                                                            |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.5 ms: 1.30x faster                                                            |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                             |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                            |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                             |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                             |
| bench_thread_pool        | 1.14 ms                                                      | 921 us: 1.24x faster                                                             |
| mdp                      | 3.01 sec                                                     | 2.45 sec: 1.23x faster                                                           |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 57.7 ms: 1.22x faster                                                            |
| dulwich_log              | 81.1 ms                                                      | 66.8 ms: 1.22x faster                                                            |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                             |
| genshi_xml               | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                            |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                             |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.19x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                             |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                             |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                            |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                             |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                            |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.80 ms: 1.06x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 106 ms: 1.05x faster                                                             |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                             |
| async_generators         | 421 ms                                                       | 413 ms: 1.02x faster                                                             |
| regex_effbot             | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                                            |
| telco                    | 7.23 ms                                                      | 7.75 ms: 1.07x slower                                                            |
| json                     | 5.86 ms                                                      | 6.88 ms: 1.17x slower                                                            |
| python_startup_no_site   | 7.33 ms                                                      | 8.96 ms: 1.22x slower                                                            |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                            |
| json_loads               | 30.3 us                                                      | 37.8 us: 1.25x slower                                                            |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.60x slower                                                            |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                            |
| bench_mp_pool            | 6.37 ms                                                      | 929 ms: 145.79x slower                                                           |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-4014e70/bm-20250129-pythonperf2-x86_64-kumaraditya303-per_thread_tasks-3.14.0a4+-4014e70.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.342x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.64x