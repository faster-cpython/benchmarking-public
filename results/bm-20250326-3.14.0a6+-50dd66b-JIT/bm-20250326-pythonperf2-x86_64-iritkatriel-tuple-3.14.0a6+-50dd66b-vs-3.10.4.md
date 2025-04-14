# Results vs. 3.10.4

- fork: iritkatriel
- ref: tuple
- machine: linux-x86_64
- commit hash: 50dd66b
- commit date: 2025-03-26
- overall geometric mean: 1.321x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 293 ms: 1.19x faster                                               |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                             |
| html5lib       | 94.6 ms                                                      | 69.5 ms: 1.36x faster                                              |
| Geometric mean | (ref)                                                        | 1.23x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 640 ms: 2.50x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 339 ms: 2.42x faster                                               |
| async_tree_none         | 692 ms                                                       | 295 ms: 2.35x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 518 ms: 1.81x faster                                               |
| Geometric mean          | (ref)                                                        | 2.25x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.8 ms: 1.74x faster                                              |
| nbody          | 134 ms                                                       | 94.7 ms: 1.42x faster                                              |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                               |
| Geometric mean | (ref)                                                        | 1.38x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                               |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                              |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                              |
| Geometric mean | (ref)                                                        | 1.14x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.44x faster                                               |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                             |
| pickle_pure_python   | 455 us                                                       | 345 us: 1.32x faster                                               |
| xml_etree_process    | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                              |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                              |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                               |
| json_loads           | 30.3 us                                                      | 26.0 us: 1.17x faster                                              |
| xml_etree_iterparse  | 110 ms                                                       | 95.7 ms: 1.15x faster                                              |
| xml_etree_generate   | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                              |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                              |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                              |
| django_template | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                              |
| genshi_text     | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                              |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.98x faster                                               |
| async_tree_io            | 1.60 sec                                                     | 640 ms: 2.50x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.06 ms: 2.45x faster                                              |
| async_tree_memoization   | 819 ms                                                       | 339 ms: 2.42x faster                                               |
| async_tree_none          | 692 ms                                                       | 295 ms: 2.35x faster                                               |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                              |
| richards_super           | 90.6 ms                                                      | 47.3 ms: 1.92x faster                                              |
| richards                 | 75.1 ms                                                      | 40.7 ms: 1.85x faster                                              |
| go                       | 262 ms                                                       | 144 ms: 1.82x faster                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 518 ms: 1.81x faster                                               |
| logging_silent           | 167 ns                                                       | 93.8 ns: 1.78x faster                                              |
| deepcopy_memo            | 49.8 us                                                      | 28.5 us: 1.75x faster                                              |
| float                    | 111 ms                                                       | 63.8 ms: 1.74x faster                                              |
| pylint                   | 566 ms                                                       | 327 ms: 1.73x faster                                               |
| pyflate                  | 733 ms                                                       | 435 ms: 1.69x faster                                               |
| chaos                    | 109 ms                                                       | 64.4 ms: 1.69x faster                                              |
| scimark_lu               | 167 ms                                                       | 99.5 ms: 1.68x faster                                              |
| raytrace                 | 489 ms                                                       | 292 ms: 1.68x faster                                               |
| scimark_sor              | 180 ms                                                       | 109 ms: 1.65x faster                                               |
| spectral_norm            | 139 ms                                                       | 88.7 ms: 1.57x faster                                              |
| deepcopy                 | 468 us                                                       | 299 us: 1.56x faster                                               |
| scimark_monte_carlo      | 107 ms                                                       | 70.9 ms: 1.51x faster                                              |
| crypto_pyaes             | 119 ms                                                       | 82.3 ms: 1.45x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.44x faster                                               |
| nbody                    | 134 ms                                                       | 94.7 ms: 1.42x faster                                              |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.41x faster                                              |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                             |
| hexiom                   | 9.42 ms                                                      | 6.81 ms: 1.38x faster                                              |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                               |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                              |
| html5lib                 | 94.6 ms                                                      | 69.5 ms: 1.36x faster                                              |
| django_template          | 50.2 ms                                                      | 37.2 ms: 1.35x faster                                              |
| thrift                   | 1.18 ms                                                      | 872 us: 1.35x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                              |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.34x faster                                              |
| comprehensions           | 26.7 us                                                      | 20.1 us: 1.33x faster                                              |
| logging_format           | 9.64 us                                                      | 7.28 us: 1.32x faster                                              |
| pickle_pure_python       | 455 us                                                       | 345 us: 1.32x faster                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                             |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.32x faster                                             |
| xml_etree_process        | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 809 ms: 1.30x faster                                               |
| dulwich_log              | 81.1 ms                                                      | 62.9 ms: 1.29x faster                                              |
| genshi_text              | 31.4 ms                                                      | 24.6 ms: 1.28x faster                                              |
| sqlalchemy_declarative   | 190 ms                                                       | 149 ms: 1.28x faster                                               |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.27x faster                                              |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.2 ms: 1.25x faster                                              |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.24x faster                                               |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                              |
| nqueens                  | 115 ms                                                       | 93.9 ms: 1.22x faster                                              |
| fannkuch                 | 483 ms                                                       | 395 ms: 1.22x faster                                               |
| sympy_str                | 360 ms                                                       | 299 ms: 1.20x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.20x faster                                              |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                             |
| 2to3                     | 350 ms                                                       | 293 ms: 1.19x faster                                               |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                               |
| scimark_fft              | 361 ms                                                       | 310 ms: 1.17x faster                                               |
| json_loads               | 30.3 us                                                      | 26.0 us: 1.17x faster                                              |
| bench_thread_pool        | 1.14 ms                                                      | 984 us: 1.16x faster                                               |
| sympy_expand             | 600 ms                                                       | 519 ms: 1.16x faster                                               |
| xml_etree_iterparse      | 110 ms                                                       | 95.7 ms: 1.15x faster                                              |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.14x faster                                             |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                              |
| xml_etree_generate       | 92.3 ms                                                      | 82.4 ms: 1.12x faster                                              |
| json                     | 5.86 ms                                                      | 5.33 ms: 1.10x faster                                              |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                               |
| genshi_xml               | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                              |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                               |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                              |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                               |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                               |
| regex_effbot             | 3.09 ms                                                      | 3.11 ms: 1.01x slower                                              |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                               |
| telco                    | 7.23 ms                                                      | 7.89 ms: 1.09x slower                                              |
| coverage                 | 63.3 ms                                                      | 78.0 ms: 1.23x slower                                              |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.70 ms: 1.53x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 6.14 ms: 1.80x slower                                              |
| bench_mp_pool            | 6.37 ms                                                      | 713 ms: 111.81x slower                                             |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                       |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250326-3.14.0a6+-50dd66b-JIT/bm-20250326-pythonperf2-x86_64-iritkatriel-tuple-3.14.0a6+-50dd66b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.321x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.31x