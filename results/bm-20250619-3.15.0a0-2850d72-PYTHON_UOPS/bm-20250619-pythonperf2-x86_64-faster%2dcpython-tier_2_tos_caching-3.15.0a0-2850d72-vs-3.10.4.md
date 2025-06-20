# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.113x faster
- HPT reliability: 99.64%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 333 ms: 1.05x faster                                                                |
| docutils       | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                              |
| html5lib       | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                               |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 675 ms: 2.37x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 361 ms: 2.27x faster                                                                |
| async_tree_none         | 692 ms                                                       | 312 ms: 2.22x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 536 ms: 1.75x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.14x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 259 ms: 1.05x faster                                                                |
| float          | 111 ms                                                       | 113 ms: 1.02x slower                                                                |
| nbody          | 134 ms                                                       | 218 ms: 1.62x slower                                                                |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 220 ms: 1.19x faster                                                                |
| regex_compile  | 190 ms                                                       | 164 ms: 1.16x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                               |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| json_loads           | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 147 ms: 1.09x faster                                                                |
| pickle_pure_python   | 455 us                                                       | 429 us: 1.06x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 113 ms: 1.02x slower                                                                |
| xml_etree_process    | 75.9 ms                                                      | 82.4 ms: 1.09x slower                                                               |
| tomli_loads          | 2.92 sec                                                     | 3.17 sec: 1.09x slower                                                              |
| xml_etree_generate   | 92.3 ms                                                      | 119 ms: 1.29x slower                                                                |
| unpickle_pure_python | 312 us                                                       | 428 us: 1.37x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.02x slower                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.7 ms: 1.37x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 57.2 ms: 1.11x faster                                                               |
| mako            | 14.7 ms                                                      | 20.8 ms: 1.42x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.09x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 214 us: 2.51x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 675 ms: 2.37x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 361 ms: 2.27x faster                                                                |
| async_tree_none          | 692 ms                                                       | 312 ms: 2.22x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.52 sec: 1.98x faster                                                              |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                               |
| scimark_lu               | 167 ms                                                       | 92.9 ms: 1.80x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 28.1 us: 1.77x faster                                                               |
| scimark_sor              | 180 ms                                                       | 103 ms: 1.76x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 536 ms: 1.75x faster                                                                |
| chaos                    | 109 ms                                                       | 63.4 ms: 1.71x faster                                                               |
| pylint                   | 566 ms                                                       | 337 ms: 1.68x faster                                                                |
| deepcopy                 | 468 us                                                       | 279 us: 1.68x faster                                                                |
| raytrace                 | 489 ms                                                       | 343 ms: 1.43x faster                                                                |
| thrift                   | 1.18 ms                                                      | 828 us: 1.42x faster                                                                |
| richards_super           | 90.6 ms                                                      | 64.7 ms: 1.40x faster                                                               |
| django_template          | 50.2 ms                                                      | 36.7 ms: 1.37x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                               |
| logging_format           | 9.64 us                                                      | 7.11 us: 1.36x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.34x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 70.8 ms: 1.34x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                               |
| richards                 | 75.1 ms                                                      | 57.5 ms: 1.31x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 62.9 ms: 1.29x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                               |
| json_loads               | 30.3 us                                                      | 25.3 us: 1.20x faster                                                               |
| regex_dna                | 261 ms                                                       | 220 ms: 1.19x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 23.7 ms: 1.19x faster                                                               |
| deltablue                | 7.50 ms                                                      | 6.35 ms: 1.18x faster                                                               |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                                |
| regex_compile            | 190 ms                                                       | 164 ms: 1.16x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 95.0 ms: 1.13x faster                                                               |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 57.2 ms: 1.11x faster                                                               |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                               |
| pyflate                  | 733 ms                                                       | 671 ms: 1.09x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 147 ms: 1.09x faster                                                                |
| docutils                 | 3.41 sec                                                     | 3.17 sec: 1.08x faster                                                              |
| pycparser                | 1.67 sec                                                     | 1.56 sec: 1.07x faster                                                              |
| nqueens                  | 115 ms                                                       | 107 ms: 1.07x faster                                                                |
| sympy_expand             | 600 ms                                                       | 562 ms: 1.07x faster                                                                |
| go                       | 262 ms                                                       | 246 ms: 1.06x faster                                                                |
| pickle_pure_python       | 455 us                                                       | 429 us: 1.06x faster                                                                |
| 2to3                     | 350 ms                                                       | 333 ms: 1.05x faster                                                                |
| pidigits                 | 271 ms                                                       | 259 ms: 1.05x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 118 ms: 1.01x faster                                                                |
| float                    | 111 ms                                                       | 113 ms: 1.02x slower                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 113 ms: 1.02x slower                                                                |
| sqlite_synth             | 2.99 us                                                      | 3.06 us: 1.02x slower                                                               |
| xml_etree_process        | 75.9 ms                                                      | 82.4 ms: 1.09x slower                                                               |
| tomli_loads              | 2.92 sec                                                     | 3.17 sec: 1.09x slower                                                              |
| async_generators         | 421 ms                                                       | 462 ms: 1.10x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.83 ms: 1.21x slower                                                               |
| comprehensions           | 26.7 us                                                      | 32.4 us: 1.21x slower                                                               |
| meteor_contest           | 138 ms                                                       | 169 ms: 1.22x slower                                                                |
| coverage                 | 63.3 ms                                                      | 77.8 ms: 1.23x slower                                                               |
| hexiom                   | 9.42 ms                                                      | 11.7 ms: 1.24x slower                                                               |
| pprint_pformat           | 2.15 sec                                                     | 2.69 sec: 1.25x slower                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 1.33 sec: 1.26x slower                                                              |
| xml_etree_generate       | 92.3 ms                                                      | 119 ms: 1.29x slower                                                                |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| telco                    | 7.23 ms                                                      | 9.73 ms: 1.35x slower                                                               |
| spectral_norm            | 139 ms                                                       | 189 ms: 1.36x slower                                                                |
| unpickle_pure_python     | 312 us                                                       | 428 us: 1.37x slower                                                                |
| mako                     | 14.7 ms                                                      | 20.8 ms: 1.42x slower                                                               |
| scimark_fft              | 361 ms                                                       | 513 ms: 1.42x slower                                                                |
| fannkuch                 | 483 ms                                                       | 690 ms: 1.43x slower                                                                |
| nbody                    | 134 ms                                                       | 218 ms: 1.62x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 9.49 ms: 1.87x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.72 ms: 1.97x slower                                                               |
| logging_silent           | 167 ns                                                       | 504 ns: 3.01x slower                                                                |
| Geometric mean           | (ref)                                                        | 1.10x faster                                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-2850d72-PYTHON_UOPS/bm-20250619-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 99.64% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.37x