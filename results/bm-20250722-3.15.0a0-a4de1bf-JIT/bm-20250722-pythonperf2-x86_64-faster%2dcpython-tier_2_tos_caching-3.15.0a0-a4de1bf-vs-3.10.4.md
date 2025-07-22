# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.332x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 285 ms: 1.23x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                              |
| html5lib       | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 623 ms: 2.57x faster                                                                |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 327 ms: 2.50x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 61.7 ms: 1.80x faster                                                               |
| nbody          | 134 ms                                                       | 84.4 ms: 1.59x faster                                                               |
| pidigits       | 271 ms                                                       | 256 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.45x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                               |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 199 us: 1.57x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                              |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                               |
| json_dumps           | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                               |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 140 ms: 1.14x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 97.9 ms: 1.13x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.29x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.72 ms: 1.19x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                               |
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 623 ms: 2.57x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.93 ms: 2.56x faster                                                               |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 327 ms: 2.50x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.32x faster                                                              |
| richards_super           | 90.6 ms                                                      | 41.6 ms: 2.18x faster                                                               |
| richards                 | 75.1 ms                                                      | 35.4 ms: 2.12x faster                                                               |
| go                       | 262 ms                                                       | 124 ms: 2.11x faster                                                                |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                                |
| chaos                    | 109 ms                                                       | 59.1 ms: 1.84x faster                                                               |
| float                    | 111 ms                                                       | 61.7 ms: 1.80x faster                                                               |
| logging_silent           | 167 ns                                                       | 93.4 ns: 1.79x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                                               |
| pyflate                  | 733 ms                                                       | 417 ms: 1.76x faster                                                                |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                                |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                                |
| scimark_lu               | 167 ms                                                       | 96.6 ms: 1.73x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 62.4 ms: 1.72x faster                                                               |
| spectral_norm            | 139 ms                                                       | 80.9 ms: 1.72x faster                                                               |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                                |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                                |
| nbody                    | 134 ms                                                       | 84.4 ms: 1.59x faster                                                               |
| unpickle_pure_python     | 312 us                                                       | 199 us: 1.57x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 77.2 ms: 1.54x faster                                                               |
| hexiom                   | 9.42 ms                                                      | 6.18 ms: 1.52x faster                                                               |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.52x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.94 sec: 1.50x faster                                                              |
| logging_simple           | 8.88 us                                                      | 6.12 us: 1.45x faster                                                               |
| logging_format           | 9.64 us                                                      | 6.69 us: 1.44x faster                                                               |
| django_template          | 50.2 ms                                                      | 35.0 ms: 1.44x faster                                                               |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                               |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| pprint_pformat           | 2.15 sec                                                     | 1.52 sec: 1.42x faster                                                              |
| html5lib                 | 94.6 ms                                                      | 67.0 ms: 1.41x faster                                                               |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 753 ms: 1.39x faster                                                                |
| dulwich_log              | 81.1 ms                                                      | 58.3 ms: 1.39x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                              |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 56.4 ms: 1.35x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.1 ms: 1.31x faster                                                               |
| fannkuch                 | 483 ms                                                       | 372 ms: 1.30x faster                                                                |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                               |
| sympy_str                | 360 ms                                                       | 289 ms: 1.24x faster                                                                |
| 2to3                     | 350 ms                                                       | 285 ms: 1.23x faster                                                                |
| nqueens                  | 115 ms                                                       | 94.4 ms: 1.22x faster                                                               |
| sympy_expand             | 600 ms                                                       | 493 ms: 1.22x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                               |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                              |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                               |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 80.2 ms: 1.15x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 140 ms: 1.14x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                               |
| meteor_contest           | 138 ms                                                       | 122 ms: 1.14x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 97.9 ms: 1.13x faster                                                               |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                               |
| pidigits                 | 271 ms                                                       | 256 ms: 1.06x faster                                                                |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                |
| async_generators         | 421 ms                                                       | 443 ms: 1.05x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.72 ms: 1.19x slower                                                               |
| coverage                 | 63.3 ms                                                      | 77.9 ms: 1.23x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.91 ms: 1.65x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.58 ms: 1.93x slower                                                               |
| telco                    | 7.23 ms                                                      | 163 ms: 22.55x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                        |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250722-3.15.0a0-a4de1bf-JIT/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.332x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x