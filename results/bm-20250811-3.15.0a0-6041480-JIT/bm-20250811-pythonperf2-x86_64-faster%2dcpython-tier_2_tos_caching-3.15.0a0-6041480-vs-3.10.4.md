# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6041480
- commit date: 2025-08-11
- overall geometric mean: 1.340x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                              |
| html5lib       | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 619 ms: 2.58x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 329 ms: 2.49x faster                                                                |
| async_tree_none         | 692 ms                                                       | 280 ms: 2.47x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 501 ms: 1.87x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 60.5 ms: 1.84x faster                                                               |
| nbody          | 134 ms                                                       | 86.4 ms: 1.55x faster                                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.45x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                                |
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.69 ms: 1.19x slower                                                               |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 199 us: 1.57x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                              |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.37x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 79.5 ms: 1.16x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 98.2 ms: 1.13x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.31x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                               |
| django_template | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.86 ms: 2.62x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 619 ms: 2.58x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 329 ms: 2.49x faster                                                                |
| async_tree_none          | 692 ms                                                       | 280 ms: 2.47x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.30 sec: 2.31x faster                                                              |
| richards_super           | 90.6 ms                                                      | 39.8 ms: 2.28x faster                                                               |
| richards                 | 75.1 ms                                                      | 34.3 ms: 2.19x faster                                                               |
| go                       | 262 ms                                                       | 122 ms: 2.14x faster                                                                |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 501 ms: 1.87x faster                                                                |
| chaos                    | 109 ms                                                       | 58.9 ms: 1.84x faster                                                               |
| float                    | 111 ms                                                       | 60.5 ms: 1.84x faster                                                               |
| logging_silent           | 167 ns                                                       | 91.5 ns: 1.83x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.80x faster                                                               |
| pyflate                  | 733 ms                                                       | 414 ms: 1.77x faster                                                                |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                                |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                                |
| scimark_lu               | 167 ms                                                       | 95.3 ms: 1.75x faster                                                               |
| spectral_norm            | 139 ms                                                       | 80.6 ms: 1.73x faster                                                               |
| raytrace                 | 489 ms                                                       | 283 ms: 1.73x faster                                                                |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 64.4 ms: 1.67x faster                                                               |
| unpickle_pure_python     | 312 us                                                       | 199 us: 1.57x faster                                                                |
| nbody                    | 134 ms                                                       | 86.4 ms: 1.55x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 77.3 ms: 1.54x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 6.12 ms: 1.54x faster                                                               |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.92 sec: 1.52x faster                                                              |
| mako                     | 14.7 ms                                                      | 9.87 ms: 1.49x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.04 us: 1.47x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.44x faster                                                              |
| logging_format           | 9.64 us                                                      | 6.70 us: 1.44x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.43x faster                                                               |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 742 ms: 1.41x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 67.3 ms: 1.41x faster                                                               |
| thrift                   | 1.18 ms                                                      | 844 us: 1.39x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.37x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 59.8 ms: 1.36x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.97 us: 1.35x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                              |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.32x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 16.5 ms: 1.29x faster                                                               |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                               |
| nqueens                  | 115 ms                                                       | 92.2 ms: 1.25x faster                                                               |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| sympy_expand             | 600 ms                                                       | 497 ms: 1.21x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 79.5 ms: 1.16x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                               |
| regex_dna                | 261 ms                                                       | 226 ms: 1.16x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.5 ms: 1.16x faster                                                               |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 98.2 ms: 1.13x faster                                                               |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                |
| async_generators         | 421 ms                                                       | 442 ms: 1.05x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.69 ms: 1.19x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.81 ms: 1.20x slower                                                               |
| coverage                 | 63.3 ms                                                      | 78.9 ms: 1.25x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.4 ms: 1.34x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                                               |
| telco                    | 7.23 ms                                                      | 161 ms: 22.21x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                        |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250811-3.15.0a0-6041480-JIT/bm-20250811-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6041480.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.340x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.41x