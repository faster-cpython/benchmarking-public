# Results vs. 3.10.4

- fork: faster-cpython
- ref: more_untracking
- machine: linux-x86_64
- commit hash: 1746ca4
- commit date: 2024-10-29
- overall geometric mean: 1.317x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                              |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                            |
| html5lib       | 94.6 ms                                                      | 71.7 ms: 1.32x faster                                                             |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                              |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 340 ms: 2.04x faster                                                              |
| async_tree_memoization  | 819 ms                                                       | 412 ms: 1.99x faster                                                              |
| async_tree_io           | 1.60 sec                                                     | 839 ms: 1.90x faster                                                              |
| async_tree_cpu_io_mixed | 936 ms                                                       | 578 ms: 1.62x faster                                                              |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.1 ms: 1.47x faster                                                             |
| float          | 111 ms                                                       | 83.1 ms: 1.34x faster                                                             |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                              |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                              |
| regex_dna      | 261 ms                                                       | 243 ms: 1.08x faster                                                              |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                             |
| regex_effbot   | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                             |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 215 us: 1.45x faster                                                              |
| pickle_pure_python   | 455 us                                                       | 328 us: 1.39x faster                                                              |
| xml_etree_process    | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                                             |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                             |
| json_loads           | 30.3 us                                                      | 24.4 us: 1.24x faster                                                             |
| tomli_loads          | 2.92 sec                                                     | 2.49 sec: 1.17x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                              |
| xml_etree_generate   | 92.3 ms                                                      | 86.0 ms: 1.07x faster                                                             |
| xml_etree_iterparse  | 110 ms                                                       | 104 ms: 1.06x faster                                                              |
| Geometric mean       | (ref)                                                        | 1.21x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.91 ms: 1.22x slower                                                             |
| python_startup         | 11.5 ms                                                      | 15.7 ms: 1.36x slower                                                             |
| Geometric mean         | (ref)                                                        | 1.29x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                             |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                             |
| django_template | 50.2 ms                                                      | 40.0 ms: 1.26x faster                                                             |
| genshi_xml      | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                             |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 173 us: 3.11x faster                                                              |
| deltablue                | 7.50 ms                                                      | 3.45 ms: 2.17x faster                                                             |
| async_tree_none          | 692 ms                                                       | 340 ms: 2.04x faster                                                              |
| async_tree_memoization   | 819 ms                                                       | 412 ms: 1.99x faster                                                              |
| generators               | 57.3 ms                                                      | 29.4 ms: 1.95x faster                                                             |
| go                       | 262 ms                                                       | 136 ms: 1.93x faster                                                              |
| async_tree_io            | 1.60 sec                                                     | 839 ms: 1.90x faster                                                              |
| raytrace                 | 489 ms                                                       | 282 ms: 1.74x faster                                                              |
| chaos                    | 109 ms                                                       | 62.7 ms: 1.73x faster                                                             |
| scimark_lu               | 167 ms                                                       | 96.5 ms: 1.73x faster                                                             |
| logging_silent           | 167 ns                                                       | 99.6 ns: 1.68x faster                                                             |
| scimark_monte_carlo      | 107 ms                                                       | 64.5 ms: 1.66x faster                                                             |
| deepcopy_memo            | 49.8 us                                                      | 30.4 us: 1.64x faster                                                             |
| richards_super           | 90.6 ms                                                      | 55.4 ms: 1.64x faster                                                             |
| pylint                   | 566 ms                                                       | 348 ms: 1.62x faster                                                              |
| crypto_pyaes             | 119 ms                                                       | 73.4 ms: 1.62x faster                                                             |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 578 ms: 1.62x faster                                                              |
| scimark_sor              | 180 ms                                                       | 113 ms: 1.59x faster                                                              |
| sqlglot_parse            | 2.24 ms                                                      | 1.43 ms: 1.56x faster                                                             |
| deepcopy                 | 468 us                                                       | 300 us: 1.56x faster                                                              |
| richards                 | 75.1 ms                                                      | 49.1 ms: 1.53x faster                                                             |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                                             |
| hexiom                   | 9.42 ms                                                      | 6.30 ms: 1.49x faster                                                             |
| pyflate                  | 733 ms                                                       | 492 ms: 1.49x faster                                                              |
| sqlglot_transpile        | 2.68 ms                                                      | 1.81 ms: 1.48x faster                                                             |
| nbody                    | 134 ms                                                       | 91.1 ms: 1.47x faster                                                             |
| unpickle_pure_python     | 312 us                                                       | 215 us: 1.45x faster                                                              |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                             |
| logging_simple           | 8.88 us                                                      | 6.35 us: 1.40x faster                                                             |
| spectral_norm            | 139 ms                                                       | 99.9 ms: 1.39x faster                                                             |
| pickle_pure_python       | 455 us                                                       | 328 us: 1.39x faster                                                              |
| logging_format           | 9.64 us                                                      | 7.03 us: 1.37x faster                                                             |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                              |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.37x faster                                                             |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                              |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.35x faster                                                              |
| thrift                   | 1.18 ms                                                      | 874 us: 1.34x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 2.99 us: 1.34x faster                                                             |
| float                    | 111 ms                                                       | 83.1 ms: 1.34x faster                                                             |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                             |
| pprint_safe_repr         | 1.05 sec                                                     | 791 ms: 1.33x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 71.7 ms: 1.32x faster                                                             |
| nqueens                  | 115 ms                                                       | 89.4 ms: 1.29x faster                                                             |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                                             |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                              |
| bench_thread_pool        | 1.14 ms                                                      | 905 us: 1.26x faster                                                              |
| django_template          | 50.2 ms                                                      | 40.0 ms: 1.26x faster                                                             |
| xml_etree_process        | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                                             |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                             |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                             |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                              |
| json_loads               | 30.3 us                                                      | 24.4 us: 1.24x faster                                                             |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                                              |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                                              |
| dulwich_log              | 81.1 ms                                                      | 66.8 ms: 1.21x faster                                                             |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                             |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                              |
| async_generators         | 421 ms                                                       | 352 ms: 1.19x faster                                                              |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 122 ms: 1.18x faster                                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.32 ms: 1.17x faster                                                             |
| genshi_xml               | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                             |
| tomli_loads              | 2.92 sec                                                     | 2.49 sec: 1.17x faster                                                            |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.17x faster                                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 60.1 ms: 1.17x faster                                                             |
| json                     | 5.86 ms                                                      | 5.13 ms: 1.14x faster                                                             |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                              |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                              |
| regex_dna                | 261 ms                                                       | 243 ms: 1.08x faster                                                              |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 86.0 ms: 1.07x faster                                                             |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                             |
| xml_etree_iterparse      | 110 ms                                                       | 104 ms: 1.06x faster                                                              |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                             |
| regex_effbot             | 3.09 ms                                                      | 3.56 ms: 1.15x slower                                                             |
| python_startup_no_site   | 7.33 ms                                                      | 8.91 ms: 1.22x slower                                                             |
| coverage                 | 63.3 ms                                                      | 83.8 ms: 1.32x slower                                                             |
| python_startup           | 11.5 ms                                                      | 15.7 ms: 1.36x slower                                                             |
| create_gc_cycles         | 1.76 ms                                                      | 2.73 ms: 1.55x slower                                                             |
| gc_traversal             | 3.42 ms                                                      | 5.52 ms: 1.62x slower                                                             |
| bench_mp_pool            | 6.37 ms                                                      | 1.47 sec: 230.96x slower                                                          |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                      |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (9) of results/bm-20241029-3.14.0a1+-1746ca4/bm-20241029-pythonperf2-x86_64-faster%2dcpython-more_untracking-3.14.0a1+-1746ca4.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, shortest_path, sphinx

- Geometric mean (including insignificant results): 1.317x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.26x