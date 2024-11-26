# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 5791853
- commit date: 2024-10-25
- overall geometric mean: 1.263x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 318 ms: 1.10x faster                                                            |
| docutils       | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                          |
| html5lib       | 94.6 ms                                                      | 71.2 ms: 1.33x faster                                                           |
| tornado_http   | 157 ms                                                       | 123 ms: 1.28x faster                                                            |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 344 ms: 2.01x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 415 ms: 1.97x faster                                                            |
| async_tree_io           | 1.60 sec                                                     | 845 ms: 1.89x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 579 ms: 1.62x faster                                                            |
| Geometric mean          | (ref)                                                        | 1.87x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.3 ms: 1.61x faster                                                           |
| float          | 111 ms                                                       | 79.4 ms: 1.40x faster                                                           |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 146 ms: 1.30x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                           |
| regex_dna      | 261 ms                                                       | 253 ms: 1.03x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                           |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 225 us: 1.39x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.35x faster                                                            |
| xml_etree_process    | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                           |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                           |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.23x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 81.2 ms: 1.14x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 99.8 ms: 1.11x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                           |
| python_startup         | 11.5 ms                                                      | 14.8 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                           |
| django_template | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 30.8 ms: 1.02x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 65.8 ms: 1.04x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.14x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 190 us: 2.82x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                                           |
| async_tree_none          | 692 ms                                                       | 344 ms: 2.01x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 415 ms: 1.97x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 845 ms: 1.89x faster                                                            |
| scimark_lu               | 167 ms                                                       | 97.0 ms: 1.72x faster                                                           |
| richards_super           | 90.6 ms                                                      | 54.3 ms: 1.67x faster                                                           |
| go                       | 262 ms                                                       | 159 ms: 1.64x faster                                                            |
| logging_silent           | 167 ns                                                       | 103 ns: 1.63x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 30.8 us: 1.62x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 579 ms: 1.62x faster                                                            |
| richards                 | 75.1 ms                                                      | 46.5 ms: 1.62x faster                                                           |
| nbody                    | 134 ms                                                       | 83.3 ms: 1.61x faster                                                           |
| chaos                    | 109 ms                                                       | 69.4 ms: 1.57x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                           |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                            |
| mako                     | 14.7 ms                                                      | 9.65 ms: 1.52x faster                                                           |
| raytrace                 | 489 ms                                                       | 324 ms: 1.51x faster                                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.50x faster                                                           |
| pyflate                  | 733 ms                                                       | 491 ms: 1.49x faster                                                            |
| scimark_monte_carlo      | 107 ms                                                       | 72.2 ms: 1.49x faster                                                           |
| spectral_norm            | 139 ms                                                       | 94.9 ms: 1.47x faster                                                           |
| deepcopy                 | 468 us                                                       | 320 us: 1.46x faster                                                            |
| generators               | 57.3 ms                                                      | 39.2 ms: 1.46x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                           |
| float                    | 111 ms                                                       | 79.4 ms: 1.40x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 225 us: 1.39x faster                                                            |
| comprehensions           | 26.7 us                                                      | 19.5 us: 1.37x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                                          |
| sqlglot_transpile        | 2.68 ms                                                      | 1.97 ms: 1.36x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.35x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 71.2 ms: 1.33x faster                                                           |
| pylint                   | 566 ms                                                       | 426 ms: 1.33x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.32x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 802 ms: 1.31x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.80 us: 1.30x faster                                                           |
| regex_compile            | 190 ms                                                       | 146 ms: 1.30x faster                                                            |
| logging_format           | 9.64 us                                                      | 7.44 us: 1.30x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 58.7 ms: 1.29x faster                                                           |
| dulwich_log              | 81.1 ms                                                      | 62.9 ms: 1.29x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.13 us: 1.28x faster                                                           |
| tornado_http             | 157 ms                                                       | 123 ms: 1.28x faster                                                            |
| thrift                   | 1.18 ms                                                      | 930 us: 1.26x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 7.46 ms: 1.26x faster                                                           |
| fannkuch                 | 483 ms                                                       | 389 ms: 1.24x faster                                                            |
| scimark_fft              | 361 ms                                                       | 292 ms: 1.24x faster                                                            |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.23x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.4 ms: 1.23x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.25 ms: 1.19x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 956 us: 1.19x faster                                                            |
| django_template          | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 81.2 ms: 1.14x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.13x faster                                                          |
| sympy_expand             | 600 ms                                                       | 532 ms: 1.13x faster                                                            |
| json                     | 5.86 ms                                                      | 5.21 ms: 1.12x faster                                                           |
| sqlalchemy_declarative   | 190 ms                                                       | 169 ms: 1.12x faster                                                            |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 99.8 ms: 1.11x faster                                                           |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                            |
| 2to3                     | 350 ms                                                       | 318 ms: 1.10x faster                                                            |
| async_generators         | 421 ms                                                       | 384 ms: 1.10x faster                                                            |
| nqueens                  | 115 ms                                                       | 106 ms: 1.09x faster                                                            |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 134 ms: 1.07x faster                                                            |
| docutils                 | 3.41 sec                                                     | 3.20 sec: 1.07x faster                                                          |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                           |
| regex_dna                | 261 ms                                                       | 253 ms: 1.03x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 27.4 ms: 1.03x faster                                                           |
| genshi_text              | 31.4 ms                                                      | 30.8 ms: 1.02x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                            |
| meteor_contest           | 138 ms                                                       | 137 ms: 1.01x faster                                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 69.6 ms: 1.01x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 65.8 ms: 1.04x slower                                                           |
| telco                    | 7.23 ms                                                      | 8.02 ms: 1.11x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.70 ms: 1.20x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                           |
| coverage                 | 63.3 ms                                                      | 78.1 ms: 1.23x slower                                                           |
| python_startup           | 11.5 ms                                                      | 14.8 ms: 1.29x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 5.53 ms: 1.62x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.89 ms: 1.64x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 1.90 sec: 298.49x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-5791853-JIT/bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-5791853.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.263x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.21x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: 1.33x