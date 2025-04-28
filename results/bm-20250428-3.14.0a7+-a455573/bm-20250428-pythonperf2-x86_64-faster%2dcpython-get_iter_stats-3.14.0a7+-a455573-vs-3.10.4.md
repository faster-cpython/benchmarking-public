# Results vs. 3.10.4

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: a455573
- commit date: 2025-04-28
- overall geometric mean: 1.374x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 274 ms: 1.28x faster                                                             |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                           |
| html5lib       | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                            |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 625 ms: 2.56x faster                                                             |
| async_tree_memoization  | 819 ms                                                       | 321 ms: 2.55x faster                                                             |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.49x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 495 ms: 1.89x faster                                                             |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.4 ms: 1.65x faster                                                            |
| nbody          | 134 ms                                                       | 94.9 ms: 1.41x faster                                                            |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                             |
| regex_v8       | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                            |
| regex_dna      | 261 ms                                                       | 240 ms: 1.09x faster                                                             |
| regex_effbot   | 3.09 ms                                                      | 3.25 ms: 1.05x slower                                                            |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 207 us: 1.51x faster                                                             |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.40x faster                                                             |
| xml_etree_process    | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                            |
| json_loads           | 30.3 us                                                      | 25.9 us: 1.17x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 96.6 ms: 1.14x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.14x faster                                                             |
| xml_etree_generate   | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                            |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.41x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.5 ms: 1.45x faster                                                            |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                            |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                            |
| genshi_xml      | 63.3 ms                                                      | 52.1 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.22x faster                                                             |
| async_tree_io            | 1.60 sec                                                     | 625 ms: 2.56x faster                                                             |
| async_tree_memoization   | 819 ms                                                       | 321 ms: 2.55x faster                                                             |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.49x faster                                                             |
| deltablue                | 7.50 ms                                                      | 3.08 ms: 2.43x faster                                                            |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.37x faster                                                           |
| go                       | 262 ms                                                       | 122 ms: 2.14x faster                                                             |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 495 ms: 1.89x faster                                                             |
| logging_silent           | 167 ns                                                       | 90.2 ns: 1.85x faster                                                            |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                                            |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                             |
| deepcopy_memo            | 49.8 us                                                      | 27.5 us: 1.81x faster                                                            |
| richards_super           | 90.6 ms                                                      | 50.3 ms: 1.80x faster                                                            |
| pylint                   | 566 ms                                                       | 319 ms: 1.78x faster                                                             |
| scimark_monte_carlo      | 107 ms                                                       | 61.6 ms: 1.74x faster                                                            |
| scimark_lu               | 167 ms                                                       | 96.1 ms: 1.74x faster                                                            |
| deepcopy                 | 468 us                                                       | 270 us: 1.73x faster                                                             |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.71x faster                                                             |
| richards                 | 75.1 ms                                                      | 44.6 ms: 1.69x faster                                                            |
| pyflate                  | 733 ms                                                       | 439 ms: 1.67x faster                                                             |
| float                    | 111 ms                                                       | 67.4 ms: 1.65x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 5.94 ms: 1.59x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.1 us: 1.56x faster                                                            |
| spectral_norm            | 139 ms                                                       | 89.2 ms: 1.56x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 78.8 ms: 1.51x faster                                                            |
| logging_simple           | 8.88 us                                                      | 5.87 us: 1.51x faster                                                            |
| unpickle_pure_python     | 312 us                                                       | 207 us: 1.51x faster                                                             |
| logging_format           | 9.64 us                                                      | 6.51 us: 1.48x faster                                                            |
| django_template          | 50.2 ms                                                      | 34.5 ms: 1.45x faster                                                            |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                             |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 66.6 ms: 1.42x faster                                                            |
| nbody                    | 134 ms                                                       | 94.9 ms: 1.41x faster                                                            |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.40x faster                                                             |
| deepcopy_reduce          | 4.01 us                                                      | 2.86 us: 1.40x faster                                                            |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 770 ms: 1.36x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                            |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 61.1 ms: 1.33x faster                                                            |
| fannkuch                 | 483 ms                                                       | 364 ms: 1.33x faster                                                             |
| xml_etree_process        | 75.9 ms                                                      | 58.3 ms: 1.30x faster                                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 147 ms: 1.29x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.29x faster                                                            |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                             |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                            |
| 2to3                     | 350 ms                                                       | 274 ms: 1.28x faster                                                             |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                            |
| sympy_str                | 360 ms                                                       | 285 ms: 1.26x faster                                                             |
| nqueens                  | 115 ms                                                       | 92.5 ms: 1.24x faster                                                            |
| sympy_expand             | 600 ms                                                       | 485 ms: 1.24x faster                                                             |
| genshi_xml               | 63.3 ms                                                      | 52.1 ms: 1.22x faster                                                            |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                           |
| scimark_fft              | 361 ms                                                       | 304 ms: 1.19x faster                                                             |
| bench_thread_pool        | 1.14 ms                                                      | 968 us: 1.18x faster                                                             |
| json_loads               | 30.3 us                                                      | 25.9 us: 1.17x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 96.6 ms: 1.14x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.14x faster                                                             |
| meteor_contest           | 138 ms                                                       | 125 ms: 1.11x faster                                                             |
| xml_etree_generate       | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.63 ms: 1.10x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 24.9 ms: 1.09x faster                                                            |
| json                     | 5.86 ms                                                      | 5.38 ms: 1.09x faster                                                            |
| regex_dna                | 261 ms                                                       | 240 ms: 1.09x faster                                                             |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                             |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.04x faster                                                            |
| async_generators         | 421 ms                                                       | 409 ms: 1.03x faster                                                             |
| regex_effbot             | 3.09 ms                                                      | 3.25 ms: 1.05x slower                                                            |
| telco                    | 7.23 ms                                                      | 7.81 ms: 1.08x slower                                                            |
| coverage                 | 63.3 ms                                                      | 81.6 ms: 1.29x slower                                                            |
| python_startup           | 11.5 ms                                                      | 15.9 ms: 1.38x slower                                                            |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                            |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                            |
| bench_mp_pool            | 6.37 ms                                                      | 1.41 sec: 221.18x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250428-3.14.0a7+-a455573/bm-20250428-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-a455573.json: bpe_tokeniser, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.374x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x