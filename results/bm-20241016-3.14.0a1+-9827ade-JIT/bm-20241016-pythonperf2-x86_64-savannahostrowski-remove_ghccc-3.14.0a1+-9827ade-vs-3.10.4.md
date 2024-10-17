# Results vs. 3.10.4

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.19x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 314 ms: 1.11x faster                                                            |
| docutils       | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                          |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                           |
| tornado_http   | 157 ms                                                       | 121 ms: 1.29x faster                                                            |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 335 ms: 2.06x faster                                                            |
| async_tree_memoization  | 819 ms                                                       | 413 ms: 1.99x faster                                                            |
| async_tree_io           | 1.60 sec                                                     | 854 ms: 1.87x faster                                                            |
| async_tree_cpu_io_mixed | 936 ms                                                       | 582 ms: 1.61x faster                                                            |
| Geometric mean          | (ref)                                                        | 1.87x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 83.5 ms: 1.61x faster                                                           |
| float          | 111 ms                                                       | 79.4 ms: 1.40x faster                                                           |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                            |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 148 ms: 1.28x faster                                                            |
| regex_dna      | 261 ms                                                       | 232 ms: 1.13x faster                                                            |
| regex_v8       | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                           |
| regex_effbot   | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                           |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 219 us: 1.42x faster                                                            |
| tomli_loads          | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                          |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                            |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                           |
| xml_etree_process    | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                           |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                           |
| xml_etree_generate   | 92.3 ms                                                      | 82.0 ms: 1.12x faster                                                           |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                            |
| unpickle_list        | 4.65 us                                                      | 4.76 us: 1.02x slower                                                           |
| pickle               | 9.89 us                                                      | 10.8 us: 1.09x slower                                                           |
| unpickle             | 13.5 us                                                      | 15.0 us: 1.11x slower                                                           |
| pickle_list          | 4.12 us                                                      | 4.64 us: 1.13x slower                                                           |
| pickle_dict          | 29.5 us                                                      | 33.3 us: 1.13x slower                                                           |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                           |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                           |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.44 ms: 1.56x faster                                                           |
| django_template | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                                           |
| genshi_text     | 31.4 ms                                                      | 27.9 ms: 1.13x faster                                                           |
| genshi_xml      | 63.3 ms                                                      | 61.8 ms: 1.02x faster                                                           |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 180 us: 2.99x faster                                                            |
| deltablue                | 7.50 ms                                                      | 3.30 ms: 2.27x faster                                                           |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                            |
| async_tree_none          | 692 ms                                                       | 335 ms: 2.06x faster                                                            |
| async_tree_memoization   | 819 ms                                                       | 413 ms: 1.99x faster                                                            |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                          |
| async_tree_io            | 1.60 sec                                                     | 854 ms: 1.87x faster                                                            |
| logging_silent           | 167 ns                                                       | 92.1 ns: 1.82x faster                                                           |
| richards_super           | 90.6 ms                                                      | 51.4 ms: 1.76x faster                                                           |
| scimark_lu               | 167 ms                                                       | 97.1 ms: 1.72x faster                                                           |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                            |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                            |
| deepcopy_memo            | 49.8 us                                                      | 29.6 us: 1.68x faster                                                           |
| crypto_pyaes             | 119 ms                                                       | 71.1 ms: 1.68x faster                                                           |
| richards                 | 75.1 ms                                                      | 45.5 ms: 1.65x faster                                                           |
| chaos                    | 109 ms                                                       | 66.4 ms: 1.63x faster                                                           |
| pyflate                  | 733 ms                                                       | 452 ms: 1.62x faster                                                            |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 582 ms: 1.61x faster                                                            |
| nbody                    | 134 ms                                                       | 83.5 ms: 1.61x faster                                                           |
| mako                     | 14.7 ms                                                      | 9.44 ms: 1.56x faster                                                           |
| scimark_monte_carlo      | 107 ms                                                       | 70.2 ms: 1.53x faster                                                           |
| raytrace                 | 489 ms                                                       | 324 ms: 1.51x faster                                                            |
| generators               | 57.3 ms                                                      | 38.1 ms: 1.50x faster                                                           |
| spectral_norm            | 139 ms                                                       | 92.5 ms: 1.50x faster                                                           |
| deepcopy                 | 468 us                                                       | 313 us: 1.50x faster                                                            |
| sqlglot_parse            | 2.24 ms                                                      | 1.51 ms: 1.48x faster                                                           |
| comprehensions           | 26.7 us                                                      | 18.6 us: 1.44x faster                                                           |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.42x faster                                                            |
| float                    | 111 ms                                                       | 79.4 ms: 1.40x faster                                                           |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                           |
| tomli_loads              | 2.92 sec                                                     | 2.11 sec: 1.38x faster                                                          |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                            |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                           |
| sqlglot_transpile        | 2.68 ms                                                      | 1.99 ms: 1.35x faster                                                           |
| logging_simple           | 8.88 us                                                      | 6.59 us: 1.35x faster                                                           |
| logging_format           | 9.64 us                                                      | 7.22 us: 1.34x faster                                                           |
| pylint                   | 566 ms                                                       | 424 ms: 1.33x faster                                                            |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                           |
| hexiom                   | 9.42 ms                                                      | 7.06 ms: 1.33x faster                                                           |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                           |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.32x faster                                                           |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                            |
| thrift                   | 1.18 ms                                                      | 894 us: 1.32x faster                                                            |
| xml_etree_process        | 75.9 ms                                                      | 57.8 ms: 1.31x faster                                                           |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.30x faster                                                          |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                            |
| tornado_http             | 157 ms                                                       | 121 ms: 1.29x faster                                                            |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                          |
| regex_compile            | 190 ms                                                       | 148 ms: 1.28x faster                                                            |
| scimark_fft              | 361 ms                                                       | 288 ms: 1.26x faster                                                            |
| dulwich_log              | 81.1 ms                                                      | 64.6 ms: 1.26x faster                                                           |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                           |
| bench_thread_pool        | 1.14 ms                                                      | 958 us: 1.19x faster                                                            |
| django_template          | 50.2 ms                                                      | 43.3 ms: 1.16x faster                                                           |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.38 ms: 1.16x faster                                                           |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.15x faster                                                          |
| json                     | 5.86 ms                                                      | 5.16 ms: 1.14x faster                                                           |
| sympy_str                | 360 ms                                                       | 319 ms: 1.13x faster                                                            |
| regex_dna                | 261 ms                                                       | 232 ms: 1.13x faster                                                            |
| nqueens                  | 115 ms                                                       | 102 ms: 1.13x faster                                                            |
| genshi_text              | 31.4 ms                                                      | 27.9 ms: 1.13x faster                                                           |
| xml_etree_generate       | 92.3 ms                                                      | 82.0 ms: 1.12x faster                                                           |
| sympy_expand             | 600 ms                                                       | 534 ms: 1.12x faster                                                            |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                            |
| 2to3                     | 350 ms                                                       | 314 ms: 1.11x faster                                                            |
| sympy_sum                | 193 ms                                                       | 174 ms: 1.11x faster                                                            |
| sqlite_synth             | 2.99 us                                                      | 2.71 us: 1.10x faster                                                           |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                            |
| sqlglot_normalize        | 144 ms                                                       | 132 ms: 1.09x faster                                                            |
| async_generators         | 421 ms                                                       | 386 ms: 1.09x faster                                                            |
| regex_v8                 | 27.2 ms                                                      | 25.0 ms: 1.09x faster                                                           |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                            |
| docutils                 | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                          |
| meteor_contest           | 138 ms                                                       | 133 ms: 1.04x faster                                                            |
| sympy_integrate          | 28.2 ms                                                      | 27.2 ms: 1.04x faster                                                           |
| genshi_xml               | 63.3 ms                                                      | 61.8 ms: 1.02x faster                                                           |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                            |
| sqlglot_optimize         | 70.1 ms                                                      | 69.5 ms: 1.01x faster                                                           |
| unpickle_list            | 4.65 us                                                      | 4.76 us: 1.02x slower                                                           |
| telco                    | 7.23 ms                                                      | 7.78 ms: 1.08x slower                                                           |
| pickle                   | 9.89 us                                                      | 10.8 us: 1.09x slower                                                           |
| unpickle                 | 13.5 us                                                      | 15.0 us: 1.11x slower                                                           |
| regex_effbot             | 3.09 ms                                                      | 3.47 ms: 1.12x slower                                                           |
| pickle_list              | 4.12 us                                                      | 4.64 us: 1.13x slower                                                           |
| pickle_dict              | 29.5 us                                                      | 33.3 us: 1.13x slower                                                           |
| python_startup_no_site   | 7.33 ms                                                      | 8.99 ms: 1.23x slower                                                           |
| coverage                 | 63.3 ms                                                      | 79.8 ms: 1.26x slower                                                           |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.30x slower                                                           |
| unpack_sequence          | 59.9 ns                                                      | 88.4 ns: 1.47x slower                                                           |
| gc_traversal             | 3.42 ms                                                      | 5.48 ms: 1.61x slower                                                           |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                           |
| bench_mp_pool            | 6.37 ms                                                      | 1.98 sec: 310.67x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                                    |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-pythonperf2-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.34x