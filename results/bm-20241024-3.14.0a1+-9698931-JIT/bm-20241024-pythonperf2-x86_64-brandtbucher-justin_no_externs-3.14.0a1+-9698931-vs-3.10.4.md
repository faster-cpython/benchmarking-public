# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 9698931
- commit date: 2024-10-24
- overall geometric mean: 1.192x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 335 ms: 1.05x faster                                                            |
| docutils       | 3.41 sec                                                     | 3.25 sec: 1.05x faster                                                          |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                           |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                            |
| Geometric mean | (ref)                                                        | 1.16x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 358 ms: 1.93x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 430 ms: 1.90x faster                                                            |
| async_tree_io           | 1.60 sec                                                     | 868 ms: 1.84x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 598 ms: 1.56x faster                                                            |
| Geometric mean          | (ref)                                                        | 1.80x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 80.3 ms: 1.38x faster                                                           |
| nbody          | 134 ms                                                       | 101 ms: 1.32x faster                                                            |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                            |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 157 ms: 1.21x faster                                                            |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                           |
| regex_effbot   | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                           |
| Geometric mean | (ref)                                                        | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 236 us: 1.32x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                                          |
| json_dumps           | 14.5 ms                                                      | 11.8 ms: 1.23x faster                                                           |
| pickle_pure_python   | 455 us                                                       | 375 us: 1.21x faster                                                            |
| json_loads           | 30.3 us                                                      | 25.4 us: 1.19x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 64.8 ms: 1.17x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                            |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                            |
| xml_etree_generate   | 92.3 ms                                                      | 87.7 ms: 1.05x faster                                                           |
| Geometric mean       | (ref)                                                        | 1.18x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                           |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                           |
| django_template | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 32.6 ms: 1.04x slower                                                           |
| genshi_xml      | 63.3 ms                                                      | 68.3 ms: 1.08x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.10x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 200 us: 2.68x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.58 ms: 2.09x faster                                                           |
| async_tree_none          | 692 ms                                                       | 358 ms: 1.93x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 430 ms: 1.90x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 868 ms: 1.84x faster                                                            |
| scimark_lu               | 167 ms                                                       | 98.3 ms: 1.70x faster                                                           |
| logging_silent           | 167 ns                                                       | 104 ns: 1.61x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 598 ms: 1.56x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 32.3 us: 1.54x faster                                                           |
| raytrace                 | 489 ms                                                       | 335 ms: 1.46x faster                                                            |
| scimark_sor              | 180 ms                                                       | 124 ms: 1.46x faster                                                            |
| go                       | 262 ms                                                       | 181 ms: 1.44x faster                                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.56 ms: 1.44x faster                                                           |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                           |
| richards_super           | 90.6 ms                                                      | 64.3 ms: 1.41x faster                                                           |
| spectral_norm            | 139 ms                                                       | 100 ms: 1.39x faster                                                            |
| float                    | 111 ms                                                       | 80.3 ms: 1.38x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 86.7 ms: 1.37x faster                                                           |
| chaos                    | 109 ms                                                       | 80.3 ms: 1.35x faster                                                           |
| deepcopy                 | 468 us                                                       | 350 us: 1.34x faster                                                            |
| pyflate                  | 733 ms                                                       | 548 ms: 1.34x faster                                                            |
| nbody                    | 134 ms                                                       | 101 ms: 1.32x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.72 us: 1.32x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 236 us: 1.32x faster                                                            |
| logging_format           | 9.64 us                                                      | 7.31 us: 1.32x faster                                                           |
| pylint                   | 566 ms                                                       | 431 ms: 1.31x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 16.3 ms: 1.31x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 2.05 ms: 1.31x faster                                                           |
| generators               | 57.3 ms                                                      | 44.3 ms: 1.29x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                           |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                            |
| thrift                   | 1.18 ms                                                      | 925 us: 1.27x faster                                                            |
| tomli_loads              | 2.92 sec                                                     | 2.29 sec: 1.27x faster                                                          |
| dulwich_log              | 81.1 ms                                                      | 64.4 ms: 1.26x faster                                                           |
| richards                 | 75.1 ms                                                      | 60.1 ms: 1.25x faster                                                           |
| pycparser                | 1.67 sec                                                     | 1.36 sec: 1.23x faster                                                          |
| scimark_monte_carlo      | 107 ms                                                       | 87.4 ms: 1.23x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.8 ms: 1.23x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.7 ms: 1.22x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 375 us: 1.21x faster                                                            |
| regex_compile            | 190 ms                                                       | 157 ms: 1.21x faster                                                            |
| json_loads               | 30.3 us                                                      | 25.4 us: 1.19x faster                                                           |
| comprehensions           | 26.7 us                                                      | 22.7 us: 1.18x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 64.8 ms: 1.17x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 984 us: 1.16x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.47 us: 1.15x faster                                                           |
| django_template          | 50.2 ms                                                      | 44.4 ms: 1.13x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.67 sec: 1.12x faster                                                          |
| scimark_fft              | 361 ms                                                       | 324 ms: 1.12x faster                                                            |
| sqlalchemy_declarative   | 190 ms                                                       | 170 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                            |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                           |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                            |
| sympy_expand             | 600 ms                                                       | 549 ms: 1.09x faster                                                            |
| pprint_safe_repr         | 1.05 sec                                                     | 967 ms: 1.08x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.99 sec: 1.08x faster                                                          |
| async_generators         | 421 ms                                                       | 390 ms: 1.08x faster                                                            |
| sympy_str                | 360 ms                                                       | 334 ms: 1.08x faster                                                            |
| sympy_sum                | 193 ms                                                       | 179 ms: 1.08x faster                                                            |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                            |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                            |
| hexiom                   | 9.42 ms                                                      | 8.92 ms: 1.06x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.81 ms: 1.06x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 87.7 ms: 1.05x faster                                                           |
| docutils                 | 3.41 sec                                                     | 3.25 sec: 1.05x faster                                                          |
| fannkuch                 | 483 ms                                                       | 461 ms: 1.05x faster                                                            |
| 2to3                     | 350 ms                                                       | 335 ms: 1.05x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 26.3 ms: 1.03x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 143 ms: 1.01x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 28.4 ms: 1.01x slower                                                           |
| genshi_text              | 31.4 ms                                                      | 32.6 ms: 1.04x slower                                                           |
| sqlglot_optimize         | 70.1 ms                                                      | 73.9 ms: 1.05x slower                                                           |
| nqueens                  | 115 ms                                                       | 121 ms: 1.06x slower                                                            |
| meteor_contest           | 138 ms                                                       | 148 ms: 1.07x slower                                                            |
| genshi_xml               | 63.3 ms                                                      | 68.3 ms: 1.08x slower                                                           |
| telco                    | 7.23 ms                                                      | 8.37 ms: 1.16x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.65 ms: 1.18x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 9.01 ms: 1.23x slower                                                           |
| coverage                 | 63.3 ms                                                      | 80.8 ms: 1.28x slower                                                           |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 5.36 ms: 1.57x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.64x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 2.20 sec: 345.02x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.11x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241024-3.14.0a1+-9698931-JIT/bm-20241024-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-9698931.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.192x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.34x