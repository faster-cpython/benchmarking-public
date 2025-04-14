# Results vs. 3.10.4

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: 8ca3f7d
- commit date: 2025-03-13
- overall geometric mean: 1.250x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 309 ms: 1.13x faster                                                                   |
| docutils       | 3.41 sec                                                     | 3.05 sec: 1.12x faster                                                                 |
| html5lib       | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                                  |
| Geometric mean | (ref)                                                        | 1.18x faster                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 665 ms: 2.40x faster                                                                   |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                                   |
| async_tree_memoization  | 819 ms                                                       | 377 ms: 2.18x faster                                                                   |
| async_tree_cpu_io_mixed | 936 ms                                                       | 541 ms: 1.73x faster                                                                   |
| Geometric mean          | (ref)                                                        | 2.14x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 76.5 ms: 1.45x faster                                                                  |
| nbody          | 134 ms                                                       | 119 ms: 1.13x faster                                                                   |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                   |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 148 ms: 1.29x faster                                                                   |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                                  |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                                   |
| regex_effbot   | 3.09 ms                                                      | 3.10 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 222 us: 1.41x faster                                                                   |
| pickle_pure_python   | 455 us                                                       | 345 us: 1.32x faster                                                                   |
| xml_etree_process    | 75.9 ms                                                      | 61.7 ms: 1.23x faster                                                                  |
| tomli_loads          | 2.92 sec                                                     | 2.41 sec: 1.21x faster                                                                 |
| json_dumps           | 14.5 ms                                                      | 12.2 ms: 1.19x faster                                                                  |
| xml_etree_parse      | 160 ms                                                       | 139 ms: 1.15x faster                                                                   |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.07x faster                                                                   |
| json_loads           | 30.3 us                                                      | 29.1 us: 1.04x faster                                                                  |
| xml_etree_generate   | 92.3 ms                                                      | 89.2 ms: 1.03x faster                                                                  |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                                  |
| python_startup_no_site | 7.33 ms                                                      | 10.6 ms: 1.44x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.44x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                                  |
| django_template | 50.2 ms                                                      | 39.2 ms: 1.28x faster                                                                  |
| genshi_text     | 31.4 ms                                                      | 26.9 ms: 1.17x faster                                                                  |
| genshi_xml      | 63.3 ms                                                      | 60.3 ms: 1.05x faster                                                                  |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 205 us: 2.62x faster                                                                   |
| async_tree_io            | 1.60 sec                                                     | 665 ms: 2.40x faster                                                                   |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                                   |
| async_tree_memoization   | 819 ms                                                       | 377 ms: 2.18x faster                                                                   |
| deltablue                | 7.50 ms                                                      | 3.58 ms: 2.10x faster                                                                  |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                                  |
| go                       | 262 ms                                                       | 137 ms: 1.91x faster                                                                   |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 541 ms: 1.73x faster                                                                   |
| pylint                   | 566 ms                                                       | 336 ms: 1.68x faster                                                                   |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.67x faster                                                                  |
| richards_super           | 90.6 ms                                                      | 54.7 ms: 1.66x faster                                                                  |
| scimark_lu               | 167 ms                                                       | 103 ms: 1.62x faster                                                                   |
| logging_silent           | 167 ns                                                       | 107 ns: 1.56x faster                                                                   |
| richards                 | 75.1 ms                                                      | 48.3 ms: 1.56x faster                                                                  |
| scimark_monte_carlo      | 107 ms                                                       | 70.3 ms: 1.53x faster                                                                  |
| deepcopy                 | 468 us                                                       | 306 us: 1.53x faster                                                                   |
| chaos                    | 109 ms                                                       | 71.1 ms: 1.53x faster                                                                  |
| raytrace                 | 489 ms                                                       | 324 ms: 1.51x faster                                                                   |
| hexiom                   | 9.42 ms                                                      | 6.40 ms: 1.47x faster                                                                  |
| scimark_sor              | 180 ms                                                       | 123 ms: 1.46x faster                                                                   |
| pyflate                  | 733 ms                                                       | 502 ms: 1.46x faster                                                                   |
| float                    | 111 ms                                                       | 76.5 ms: 1.45x faster                                                                  |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                                  |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.41x faster                                                                   |
| comprehensions           | 26.7 us                                                      | 19.1 us: 1.40x faster                                                                  |
| crypto_pyaes             | 119 ms                                                       | 85.9 ms: 1.39x faster                                                                  |
| spectral_norm            | 139 ms                                                       | 104 ms: 1.34x faster                                                                   |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                                                  |
| pickle_pure_python       | 455 us                                                       | 345 us: 1.32x faster                                                                   |
| html5lib                 | 94.6 ms                                                      | 72.1 ms: 1.31x faster                                                                  |
| regex_compile            | 190 ms                                                       | 148 ms: 1.29x faster                                                                   |
| django_template          | 50.2 ms                                                      | 39.2 ms: 1.28x faster                                                                  |
| logging_simple           | 8.88 us                                                      | 7.00 us: 1.27x faster                                                                  |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                                                 |
| logging_format           | 9.64 us                                                      | 7.66 us: 1.26x faster                                                                  |
| thrift                   | 1.18 ms                                                      | 940 us: 1.25x faster                                                                   |
| pprint_pformat           | 2.15 sec                                                     | 1.72 sec: 1.25x faster                                                                 |
| dulwich_log              | 81.1 ms                                                      | 65.1 ms: 1.25x faster                                                                  |
| pprint_safe_repr         | 1.05 sec                                                     | 848 ms: 1.24x faster                                                                   |
| xml_etree_process        | 75.9 ms                                                      | 61.7 ms: 1.23x faster                                                                  |
| sqlalchemy_declarative   | 190 ms                                                       | 155 ms: 1.23x faster                                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 3.29 us: 1.22x faster                                                                  |
| tomli_loads              | 2.92 sec                                                     | 2.41 sec: 1.21x faster                                                                 |
| json_dumps               | 14.5 ms                                                      | 12.2 ms: 1.19x faster                                                                  |
| pathlib                  | 21.4 ms                                                      | 17.9 ms: 1.19x faster                                                                  |
| genshi_text              | 31.4 ms                                                      | 26.9 ms: 1.17x faster                                                                  |
| sqlalchemy_imperative    | 22.7 ms                                                      | 19.5 ms: 1.17x faster                                                                  |
| sympy_sum                | 193 ms                                                       | 166 ms: 1.16x faster                                                                   |
| mdp                      | 3.01 sec                                                     | 2.61 sec: 1.15x faster                                                                 |
| xml_etree_parse          | 160 ms                                                       | 139 ms: 1.15x faster                                                                   |
| sympy_integrate          | 28.2 ms                                                      | 24.6 ms: 1.15x faster                                                                  |
| bench_thread_pool        | 1.14 ms                                                      | 1.00 ms: 1.14x faster                                                                  |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                                  |
| 2to3                     | 350 ms                                                       | 309 ms: 1.13x faster                                                                   |
| nbody                    | 134 ms                                                       | 119 ms: 1.13x faster                                                                   |
| docutils                 | 3.41 sec                                                     | 3.05 sec: 1.12x faster                                                                 |
| sympy_str                | 360 ms                                                       | 324 ms: 1.11x faster                                                                   |
| nqueens                  | 115 ms                                                       | 104 ms: 1.11x faster                                                                   |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                                   |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.07x faster                                                                   |
| fannkuch                 | 483 ms                                                       | 453 ms: 1.07x faster                                                                   |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                                   |
| scimark_fft              | 361 ms                                                       | 340 ms: 1.06x faster                                                                   |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                   |
| sympy_expand             | 600 ms                                                       | 566 ms: 1.06x faster                                                                   |
| genshi_xml               | 63.3 ms                                                      | 60.3 ms: 1.05x faster                                                                  |
| json_loads               | 30.3 us                                                      | 29.1 us: 1.04x faster                                                                  |
| xml_etree_generate       | 92.3 ms                                                      | 89.2 ms: 1.03x faster                                                                  |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.99 ms: 1.02x faster                                                                  |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                                   |
| json                     | 5.86 ms                                                      | 5.81 ms: 1.01x faster                                                                  |
| regex_effbot             | 3.09 ms                                                      | 3.10 ms: 1.01x slower                                                                  |
| telco                    | 7.23 ms                                                      | 8.39 ms: 1.16x slower                                                                  |
| async_generators         | 421 ms                                                       | 491 ms: 1.17x slower                                                                   |
| coverage                 | 63.3 ms                                                      | 80.7 ms: 1.28x slower                                                                  |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                                  |
| python_startup_no_site   | 7.33 ms                                                      | 10.6 ms: 1.44x slower                                                                  |
| create_gc_cycles         | 1.76 ms                                                      | 2.73 ms: 1.55x slower                                                                  |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                                  |
| bench_mp_pool            | 6.37 ms                                                      | 1.57 sec: 246.52x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.17x faster                                                                           |

Benchmark hidden because not significant (1): sqlite_synth
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250313-3.14.0a5+-8ca3f7d/bm-20250313-pythonperf2-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-8ca3f7d.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.250x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.28x