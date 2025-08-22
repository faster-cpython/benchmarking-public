# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: dc660a2
- commit date: 2025-08-22
- overall geometric mean: 1.349x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.42x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.23x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                              |
| html5lib       | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                               |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.60x faster                                                                |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.52x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 497 ms: 1.88x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.37x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 59.8 ms: 1.86x faster                                                               |
| nbody          | 134 ms                                                       | 87.5 ms: 1.53x faster                                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.45x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                                |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                               |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 191 us: 1.63x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                              |
| json_dumps           | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 55.0 ms: 1.38x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 331 us: 1.37x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.7 us: 1.18x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                                |
| xml_etree_generate   | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                               |
| xml_etree_iterparse  | 110 ms                                                       | 95.6 ms: 1.16x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.32x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                               |
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.33x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.85 ms: 2.63x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.60x faster                                                                |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.52x faster                                                                |
| richards_super           | 90.6 ms                                                      | 37.8 ms: 2.39x faster                                                               |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.32x faster                                                              |
| richards                 | 75.1 ms                                                      | 32.7 ms: 2.30x faster                                                               |
| go                       | 262 ms                                                       | 121 ms: 2.17x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 497 ms: 1.88x faster                                                                |
| float                    | 111 ms                                                       | 59.8 ms: 1.86x faster                                                               |
| generators               | 57.3 ms                                                      | 31.0 ms: 1.85x faster                                                               |
| chaos                    | 109 ms                                                       | 59.7 ms: 1.82x faster                                                               |
| spectral_norm            | 139 ms                                                       | 76.7 ms: 1.81x faster                                                               |
| logging_silent           | 167 ns                                                       | 92.3 ns: 1.81x faster                                                               |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                                |
| raytrace                 | 489 ms                                                       | 277 ms: 1.76x faster                                                                |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                               |
| scimark_lu               | 167 ms                                                       | 95.1 ms: 1.75x faster                                                               |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                                |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 62.5 ms: 1.72x faster                                                               |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 191 us: 1.63x faster                                                                |
| hexiom                   | 9.42 ms                                                      | 5.93 ms: 1.59x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 76.3 ms: 1.56x faster                                                               |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.55x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                              |
| logging_simple           | 8.88 us                                                      | 5.77 us: 1.54x faster                                                               |
| nbody                    | 134 ms                                                       | 87.5 ms: 1.53x faster                                                               |
| logging_format           | 9.64 us                                                      | 6.31 us: 1.53x faster                                                               |
| mako                     | 14.7 ms                                                      | 10.1 ms: 1.45x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.45x faster                                                              |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 10.2 ms: 1.42x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 67.2 ms: 1.41x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 746 ms: 1.41x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.19 sec: 1.41x faster                                                              |
| dulwich_log              | 81.1 ms                                                      | 58.5 ms: 1.39x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 55.0 ms: 1.38x faster                                                               |
| thrift                   | 1.18 ms                                                      | 853 us: 1.38x faster                                                                |
| pickle_pure_python       | 455 us                                                       | 331 us: 1.37x faster                                                                |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.5 ms: 1.34x faster                                                               |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                                |
| deepcopy_reduce          | 4.01 us                                                      | 3.05 us: 1.31x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.28x faster                                                               |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.3 ms: 1.26x faster                                                               |
| nqueens                  | 115 ms                                                       | 92.7 ms: 1.24x faster                                                               |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                                |
| 2to3                     | 350 ms                                                       | 286 ms: 1.23x faster                                                                |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.21x faster                                                                |
| sympy_expand             | 600 ms                                                       | 503 ms: 1.19x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.7 us: 1.18x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                                |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 79.8 ms: 1.16x faster                                                               |
| xml_etree_iterparse      | 110 ms                                                       | 95.6 ms: 1.16x faster                                                               |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                               |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.15x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                               |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.98 ms: 1.02x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                |
| async_generators         | 421 ms                                                       | 436 ms: 1.04x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.59 ms: 1.16x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                               |
| coverage                 | 63.3 ms                                                      | 83.0 ms: 1.31x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.60x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.54 ms: 1.92x slower                                                               |
| telco                    | 7.23 ms                                                      | 159 ms: 22.04x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250822-3.15.0a0-dc660a2-JIT/bm-20250822-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-dc660a2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.349x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.33x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.42x