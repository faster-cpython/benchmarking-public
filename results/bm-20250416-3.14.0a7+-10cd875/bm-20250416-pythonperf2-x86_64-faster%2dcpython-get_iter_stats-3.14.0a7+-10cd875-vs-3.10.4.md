# Results vs. 3.10.4

- fork: faster-cpython
- ref: get_iter_stats
- machine: linux-x86_64
- commit hash: 10cd875
- commit date: 2025-04-16
- overall geometric mean: 1.370x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 274 ms: 1.28x faster                                                             |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                           |
| html5lib       | 94.6 ms                                                      | 65.4 ms: 1.45x faster                                                            |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|-------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 629 ms: 2.54x faster                                                             |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                             |
| async_tree_none         | 692 ms                                                       | 284 ms: 2.44x faster                                                             |
| async_tree_cpu_io_mixed | 936 ms                                                       | 507 ms: 1.85x faster                                                             |
| Geometric mean          | (ref)                                                        | 2.31x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.2 ms: 1.65x faster                                                            |
| nbody          | 134 ms                                                       | 94.9 ms: 1.41x faster                                                            |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                             |
| Geometric mean | (ref)                                                        | 1.35x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                             |
| regex_v8       | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                            |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                             |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 210 us: 1.49x faster                                                             |
| tomli_loads          | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                             |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                             |
| json_loads           | 30.3 us                                                      | 26.6 us: 1.14x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 97.8 ms: 1.13x faster                                                            |
| xml_etree_generate   | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                            |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                            |
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                            |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                            |
| genshi_text     | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                            |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                            |
| genshi_xml      | 63.3 ms                                                      | 51.7 ms: 1.22x faster                                                            |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875 |
|--------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 166 us: 3.23x faster                                                             |
| async_tree_io            | 1.60 sec                                                     | 629 ms: 2.54x faster                                                             |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                             |
| async_tree_none          | 692 ms                                                       | 284 ms: 2.44x faster                                                             |
| deltablue                | 7.50 ms                                                      | 3.10 ms: 2.42x faster                                                            |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                           |
| go                       | 262 ms                                                       | 123 ms: 2.13x faster                                                             |
| generators               | 57.3 ms                                                      | 30.0 ms: 1.91x faster                                                            |
| chaos                    | 109 ms                                                       | 58.3 ms: 1.86x faster                                                            |
| logging_silent           | 167 ns                                                       | 90.5 ns: 1.85x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 507 ms: 1.85x faster                                                             |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                             |
| richards_super           | 90.6 ms                                                      | 50.6 ms: 1.79x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 27.8 us: 1.79x faster                                                            |
| scimark_monte_carlo      | 107 ms                                                       | 60.3 ms: 1.78x faster                                                            |
| pylint                   | 566 ms                                                       | 319 ms: 1.77x faster                                                             |
| scimark_lu               | 167 ms                                                       | 95.0 ms: 1.76x faster                                                            |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.75x faster                                                             |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                             |
| richards                 | 75.1 ms                                                      | 44.9 ms: 1.67x faster                                                            |
| pyflate                  | 733 ms                                                       | 440 ms: 1.67x faster                                                             |
| float                    | 111 ms                                                       | 67.2 ms: 1.65x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 6.03 ms: 1.56x faster                                                            |
| spectral_norm            | 139 ms                                                       | 89.4 ms: 1.56x faster                                                            |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.54x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 79.7 ms: 1.49x faster                                                            |
| unpickle_pure_python     | 312 us                                                       | 210 us: 1.49x faster                                                             |
| html5lib                 | 94.6 ms                                                      | 65.4 ms: 1.45x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.14 us: 1.45x faster                                                            |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                             |
| tomli_loads              | 2.92 sec                                                     | 2.04 sec: 1.43x faster                                                           |
| django_template          | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                            |
| nbody                    | 134 ms                                                       | 94.9 ms: 1.41x faster                                                            |
| logging_format           | 9.64 us                                                      | 6.87 us: 1.40x faster                                                            |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                            |
| coroutines               | 30.3 ms                                                      | 21.9 ms: 1.39x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.38x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 766 ms: 1.37x faster                                                             |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.35x faster                                                            |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                             |
| dulwich_log              | 81.1 ms                                                      | 61.0 ms: 1.33x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 148 ms: 1.29x faster                                                             |
| sympy_integrate          | 28.2 ms                                                      | 21.9 ms: 1.28x faster                                                            |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.28x faster                                                             |
| 2to3                     | 350 ms                                                       | 274 ms: 1.28x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                                            |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.9 ms: 1.27x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.26x faster                                                            |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                             |
| nqueens                  | 115 ms                                                       | 93.0 ms: 1.24x faster                                                            |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                             |
| genshi_xml               | 63.3 ms                                                      | 51.7 ms: 1.22x faster                                                            |
| scimark_fft              | 361 ms                                                       | 295 ms: 1.22x faster                                                             |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 955 us: 1.20x faster                                                             |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                             |
| json_loads               | 30.3 us                                                      | 26.6 us: 1.14x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 97.8 ms: 1.13x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.51 ms: 1.13x faster                                                            |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                             |
| regex_v8                 | 27.2 ms                                                      | 24.5 ms: 1.11x faster                                                            |
| xml_etree_generate       | 92.3 ms                                                      | 84.4 ms: 1.09x faster                                                            |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                             |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                             |
| json                     | 5.86 ms                                                      | 5.57 ms: 1.05x faster                                                            |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.04x faster                                                            |
| async_generators         | 421 ms                                                       | 413 ms: 1.02x faster                                                             |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                             |
| telco                    | 7.23 ms                                                      | 7.68 ms: 1.06x slower                                                            |
| coverage                 | 63.3 ms                                                      | 82.3 ms: 1.30x slower                                                            |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                            |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                            |
| create_gc_cycles         | 1.76 ms                                                      | 2.79 ms: 1.58x slower                                                            |
| gc_traversal             | 3.42 ms                                                      | 6.57 ms: 1.92x slower                                                            |
| bench_mp_pool            | 6.37 ms                                                      | 1.30 sec: 203.79x slower                                                         |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                     |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250416-3.14.0a7+-10cd875/bm-20250416-pythonperf2-x86_64-faster%2dcpython-get_iter_stats-3.14.0a7+-10cd875.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.370x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.29x