# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 6a85f95
- commit date: 2025-08-13
- overall geometric mean: 1.341x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                              |
| html5lib       | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                               |
| Geometric mean | (ref)                                                        | 1.25x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 623 ms: 2.56x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 328 ms: 2.50x faster                                                                |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.44x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 61.7 ms: 1.80x faster                                                               |
| nbody          | 134 ms                                                       | 86.6 ms: 1.55x faster                                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| Geometric mean | (ref)                                                        | 1.44x faster                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                               |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 195 us: 1.60x faster                                                                |
| tomli_loads          | 2.92 sec                                                     | 1.91 sec: 1.53x faster                                                              |
| json_dumps           | 14.5 ms                                                      | 10.3 ms: 1.42x faster                                                               |
| xml_etree_process    | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                               |
| pickle_pure_python   | 455 us                                                       | 335 us: 1.36x faster                                                                |
| json_loads           | 30.3 us                                                      | 25.9 us: 1.17x faster                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 99.5 ms: 1.11x faster                                                               |
| Geometric mean       | (ref)                                                        | 1.30x faster                                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.5 ms: 1.34x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.73 ms: 1.51x faster                                                               |
| django_template | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                               |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                                |
| deltablue                | 7.50 ms                                                      | 2.86 ms: 2.62x faster                                                               |
| async_tree_io            | 1.60 sec                                                     | 623 ms: 2.56x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 328 ms: 2.50x faster                                                                |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.44x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.33x faster                                                              |
| richards_super           | 90.6 ms                                                      | 39.1 ms: 2.32x faster                                                               |
| richards                 | 75.1 ms                                                      | 33.6 ms: 2.24x faster                                                               |
| go                       | 262 ms                                                       | 122 ms: 2.14x faster                                                                |
| generators               | 57.3 ms                                                      | 30.2 ms: 1.90x faster                                                               |
| pyflate                  | 733 ms                                                       | 393 ms: 1.86x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                                |
| chaos                    | 109 ms                                                       | 58.5 ms: 1.86x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 27.6 us: 1.81x faster                                                               |
| float                    | 111 ms                                                       | 61.7 ms: 1.80x faster                                                               |
| logging_silent           | 167 ns                                                       | 93.0 ns: 1.80x faster                                                               |
| spectral_norm            | 139 ms                                                       | 78.0 ms: 1.78x faster                                                               |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                                |
| raytrace                 | 489 ms                                                       | 279 ms: 1.75x faster                                                                |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                                |
| scimark_lu               | 167 ms                                                       | 95.8 ms: 1.74x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 63.3 ms: 1.70x faster                                                               |
| deepcopy                 | 468 us                                                       | 276 us: 1.70x faster                                                                |
| unpickle_pure_python     | 312 us                                                       | 195 us: 1.60x faster                                                                |
| hexiom                   | 9.42 ms                                                      | 6.00 ms: 1.57x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 76.7 ms: 1.55x faster                                                               |
| nbody                    | 134 ms                                                       | 86.6 ms: 1.55x faster                                                               |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                               |
| tomli_loads              | 2.92 sec                                                     | 1.91 sec: 1.53x faster                                                              |
| mako                     | 14.7 ms                                                      | 9.73 ms: 1.51x faster                                                               |
| logging_simple           | 8.88 us                                                      | 6.02 us: 1.48x faster                                                               |
| pprint_pformat           | 2.15 sec                                                     | 1.48 sec: 1.45x faster                                                              |
| logging_format           | 9.64 us                                                      | 6.64 us: 1.45x faster                                                               |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.3 ms: 1.42x faster                                                               |
| pprint_safe_repr         | 1.05 sec                                                     | 739 ms: 1.42x faster                                                                |
| json_dumps               | 14.5 ms                                                      | 10.3 ms: 1.42x faster                                                               |
| thrift                   | 1.18 ms                                                      | 850 us: 1.38x faster                                                                |
| html5lib                 | 94.6 ms                                                      | 68.5 ms: 1.38x faster                                                               |
| xml_etree_process        | 75.9 ms                                                      | 55.2 ms: 1.38x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 59.4 ms: 1.36x faster                                                               |
| pickle_pure_python       | 455 us                                                       | 335 us: 1.36x faster                                                                |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                              |
| deepcopy_reduce          | 4.01 us                                                      | 2.98 us: 1.35x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.5 ms: 1.35x faster                                                               |
| fannkuch                 | 483 ms                                                       | 362 ms: 1.33x faster                                                                |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.27x faster                                                               |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                                |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                               |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                                |
| nqueens                  | 115 ms                                                       | 93.4 ms: 1.23x faster                                                               |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                                |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                                |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.18x faster                                                                |
| json_loads               | 30.3 us                                                      | 25.9 us: 1.17x faster                                                               |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                              |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.3 ms: 1.17x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 54.5 ms: 1.16x faster                                                               |
| meteor_contest           | 138 ms                                                       | 120 ms: 1.15x faster                                                                |
| xml_etree_generate       | 92.3 ms                                                      | 80.8 ms: 1.14x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 99.5 ms: 1.11x faster                                                               |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                                |
| json                     | 5.86 ms                                                      | 5.54 ms: 1.06x faster                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.95 ms: 1.03x faster                                                               |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                                |
| async_generators         | 421 ms                                                       | 448 ms: 1.06x slower                                                                |
| regex_effbot             | 3.09 ms                                                      | 3.71 ms: 1.20x slower                                                               |
| python_startup_no_site   | 7.33 ms                                                      | 8.86 ms: 1.21x slower                                                               |
| coverage                 | 63.3 ms                                                      | 83.8 ms: 1.32x slower                                                               |
| python_startup           | 11.5 ms                                                      | 15.5 ms: 1.34x slower                                                               |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.32 ms: 1.85x slower                                                               |
| telco                    | 7.23 ms                                                      | 160 ms: 22.19x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                        |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250813-3.15.0a0-6a85f95-JIT/bm-20250813-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-6a85f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.341x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.41x