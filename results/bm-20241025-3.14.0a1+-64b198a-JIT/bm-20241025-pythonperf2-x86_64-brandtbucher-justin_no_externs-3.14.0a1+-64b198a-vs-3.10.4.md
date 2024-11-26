# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_no_externs
- machine: linux-x86_64
- commit hash: 64b198a
- commit date: 2024-10-25
- overall geometric mean: 1.261x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 318 ms: 1.10x faster                                                            |
| docutils       | 3.41 sec                                                     | 3.21 sec: 1.07x faster                                                          |
| html5lib       | 94.6 ms                                                      | 71.6 ms: 1.32x faster                                                           |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                            |
| Geometric mean | (ref)                                                        | 1.19x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 345 ms: 2.01x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 416 ms: 1.97x faster                                                            |
| async_tree_io           | 1.60 sec                                                     | 855 ms: 1.87x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 582 ms: 1.61x faster                                                            |
| Geometric mean          | (ref)                                                        | 1.86x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 86.1 ms: 1.56x faster                                                           |
| float          | 111 ms                                                       | 78.6 ms: 1.41x faster                                                           |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                           |
| regex_dna      | 261 ms                                                       | 256 ms: 1.02x faster                                                            |
| regex_effbot   | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                           |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 227 us: 1.37x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 349 us: 1.31x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 61.0 ms: 1.25x faster                                                           |
| json_loads           | 30.3 us                                                      | 24.7 us: 1.23x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                           |
| xml_etree_iterparse  | 110 ms                                                       | 100.0 ms: 1.11x faster                                                          |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.10x faster                                                            |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                           |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                                           |
| django_template | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 64.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                        | 1.16x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 186 us: 2.88x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.41 ms: 2.20x faster                                                           |
| async_tree_none          | 692 ms                                                       | 345 ms: 2.01x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 416 ms: 1.97x faster                                                            |
| async_tree_io            | 1.60 sec                                                     | 855 ms: 1.87x faster                                                            |
| richards_super           | 90.6 ms                                                      | 52.1 ms: 1.74x faster                                                           |
| scimark_lu               | 167 ms                                                       | 98.7 ms: 1.69x faster                                                           |
| go                       | 262 ms                                                       | 157 ms: 1.67x faster                                                            |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 30.3 us: 1.64x faster                                                           |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 582 ms: 1.61x faster                                                            |
| crypto_pyaes             | 119 ms                                                       | 75.1 ms: 1.59x faster                                                           |
| chaos                    | 109 ms                                                       | 68.6 ms: 1.58x faster                                                           |
| raytrace                 | 489 ms                                                       | 312 ms: 1.57x faster                                                            |
| nbody                    | 134 ms                                                       | 86.1 ms: 1.56x faster                                                           |
| richards                 | 75.1 ms                                                      | 49.2 ms: 1.53x faster                                                           |
| sqlglot_parse            | 2.24 ms                                                      | 1.47 ms: 1.52x faster                                                           |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.50x faster                                                            |
| pyflate                  | 733 ms                                                       | 494 ms: 1.48x faster                                                            |
| deepcopy                 | 468 us                                                       | 317 us: 1.48x faster                                                            |
| mako                     | 14.7 ms                                                      | 9.98 ms: 1.47x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 73.6 ms: 1.46x faster                                                           |
| spectral_norm            | 139 ms                                                       | 96.2 ms: 1.45x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                           |
| float                    | 111 ms                                                       | 78.6 ms: 1.41x faster                                                           |
| generators               | 57.3 ms                                                      | 40.6 ms: 1.41x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.95 ms: 1.37x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 227 us: 1.37x faster                                                            |
| logging_simple           | 8.88 us                                                      | 6.63 us: 1.34x faster                                                           |
| comprehensions           | 26.7 us                                                      | 19.9 us: 1.34x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.18 sec: 1.34x faster                                                          |
| pylint                   | 566 ms                                                       | 424 ms: 1.34x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                          |
| pathlib                  | 21.4 ms                                                      | 16.1 ms: 1.33x faster                                                           |
| html5lib                 | 94.6 ms                                                      | 71.6 ms: 1.32x faster                                                           |
| logging_format           | 9.64 us                                                      | 7.30 us: 1.32x faster                                                           |
| pickle_pure_python       | 455 us                                                       | 349 us: 1.31x faster                                                            |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                          |
| pprint_safe_repr         | 1.05 sec                                                     | 812 ms: 1.29x faster                                                            |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                            |
| dulwich_log              | 81.1 ms                                                      | 62.8 ms: 1.29x faster                                                           |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                            |
| thrift                   | 1.18 ms                                                      | 914 us: 1.29x faster                                                            |
| json_dumps               | 14.5 ms                                                      | 11.3 ms: 1.29x faster                                                           |
| fannkuch                 | 483 ms                                                       | 381 ms: 1.27x faster                                                            |
| deepcopy_reduce          | 4.01 us                                                      | 3.17 us: 1.27x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 7.51 ms: 1.25x faster                                                           |
| xml_etree_process        | 75.9 ms                                                      | 61.0 ms: 1.25x faster                                                           |
| json_loads               | 30.3 us                                                      | 24.7 us: 1.23x faster                                                           |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.5 ms: 1.23x faster                                                           |
| scimark_fft              | 361 ms                                                       | 299 ms: 1.21x faster                                                            |
| django_template          | 50.2 ms                                                      | 42.2 ms: 1.19x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                            |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.41 ms: 1.15x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.63 sec: 1.14x faster                                                          |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.13x faster                                                           |
| sqlalchemy_declarative   | 190 ms                                                       | 168 ms: 1.13x faster                                                            |
| xml_etree_generate       | 92.3 ms                                                      | 81.9 ms: 1.13x faster                                                           |
| sympy_expand             | 600 ms                                                       | 535 ms: 1.12x faster                                                            |
| sympy_str                | 360 ms                                                       | 322 ms: 1.12x faster                                                            |
| async_generators         | 421 ms                                                       | 380 ms: 1.11x faster                                                            |
| xml_etree_iterparse      | 110 ms                                                       | 100.0 ms: 1.11x faster                                                          |
| 2to3                     | 350 ms                                                       | 318 ms: 1.10x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.10x faster                                                            |
| sympy_sum                | 193 ms                                                       | 176 ms: 1.10x faster                                                            |
| nqueens                  | 115 ms                                                       | 106 ms: 1.08x faster                                                            |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                            |
| docutils                 | 3.41 sec                                                     | 3.21 sec: 1.07x faster                                                          |
| sqlglot_normalize        | 144 ms                                                       | 136 ms: 1.06x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 30.2 ms: 1.04x faster                                                           |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.03x faster                                                            |
| meteor_contest           | 138 ms                                                       | 135 ms: 1.02x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 27.6 ms: 1.02x faster                                                           |
| regex_dna                | 261 ms                                                       | 256 ms: 1.02x faster                                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 69.9 ms: 1.00x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 64.4 ms: 1.02x slower                                                           |
| telco                    | 7.23 ms                                                      | 7.99 ms: 1.11x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.66 ms: 1.19x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 9.05 ms: 1.24x slower                                                           |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                           |
| coverage                 | 63.3 ms                                                      | 83.5 ms: 1.32x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 5.51 ms: 1.61x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.64x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 1.70 sec: 266.26x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                                    |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241025-3.14.0a1+-64b198a-JIT/bm-20241025-pythonperf2-x86_64-brandtbucher-justin_no_externs-3.14.0a1+-64b198a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.261x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.33x