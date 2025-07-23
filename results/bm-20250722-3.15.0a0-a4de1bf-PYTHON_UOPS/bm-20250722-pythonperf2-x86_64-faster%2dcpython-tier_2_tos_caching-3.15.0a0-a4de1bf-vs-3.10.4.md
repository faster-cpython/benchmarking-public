# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: a4de1bf
- commit date: 2025-07-22
- overall geometric mean: 1.108x faster
- HPT reliability: 99.92%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 328 ms: 1.07x faster                                                                |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                              |
| html5lib       | 94.6 ms                                                      | 83.6 ms: 1.13x faster                                                               |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 665 ms: 2.40x faster                                                                |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 358 ms: 2.29x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 528 ms: 1.77x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.18x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 102 ms: 1.09x faster                                                                |
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                                                |
| nbody          | 134 ms                                                       | 198 ms: 1.48x slower                                                                |
| Geometric mean | (ref)                                                        | 1.09x slower                                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 160 ms: 1.19x faster                                                                |
| regex_dna      | 261 ms                                                       | 226 ms: 1.15x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                               |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| json_loads           | 30.3 us                                                      | 26.2 us: 1.16x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                                |
| pickle_pure_python   | 455 us                                                       | 414 us: 1.10x faster                                                                |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.02x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 76.9 ms: 1.01x slower                                                               |
| xml_etree_generate   | 92.3 ms                                                      | 111 ms: 1.20x slower                                                                |
| unpickle_pure_python | 312 us                                                       | 383 us: 1.23x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                        |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.69 ms: 1.19x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.7 ms: 1.40x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 56.5 ms: 1.12x faster                                                               |
| mako            | 14.7 ms                                                      | 18.4 ms: 1.25x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.14x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 208 us: 2.58x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 665 ms: 2.40x faster                                                                |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 358 ms: 2.29x faster                                                                |
| mdp                      | 3.01 sec                                                     | 1.49 sec: 2.02x faster                                                              |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.92x faster                                                               |
| logging_silent           | 167 ns                                                       | 92.2 ns: 1.81x faster                                                               |
| deepcopy_memo            | 49.8 us                                                      | 27.7 us: 1.79x faster                                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 528 ms: 1.77x faster                                                                |
| scimark_lu               | 167 ms                                                       | 94.2 ms: 1.77x faster                                                               |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.77x faster                                                                |
| chaos                    | 109 ms                                                       | 63.2 ms: 1.72x faster                                                               |
| pylint                   | 566 ms                                                       | 333 ms: 1.70x faster                                                                |
| deepcopy                 | 468 us                                                       | 277 us: 1.69x faster                                                                |
| richards_super           | 90.6 ms                                                      | 59.4 ms: 1.53x faster                                                               |
| raytrace                 | 489 ms                                                       | 332 ms: 1.47x faster                                                                |
| logging_simple           | 8.88 us                                                      | 6.17 us: 1.44x faster                                                               |
| logging_format           | 9.64 us                                                      | 6.74 us: 1.43x faster                                                               |
| richards                 | 75.1 ms                                                      | 52.6 ms: 1.43x faster                                                               |
| thrift                   | 1.18 ms                                                      | 833 us: 1.41x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.7 ms: 1.40x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.2 ms: 1.36x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                               |
| deltablue                | 7.50 ms                                                      | 5.71 ms: 1.31x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 62.4 ms: 1.30x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                               |
| scimark_monte_carlo      | 107 ms                                                       | 89.0 ms: 1.21x faster                                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                               |
| regex_compile            | 190 ms                                                       | 160 ms: 1.19x faster                                                                |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.18x faster                                                                |
| json_loads               | 30.3 us                                                      | 26.2 us: 1.16x faster                                                               |
| pyflate                  | 733 ms                                                       | 633 ms: 1.16x faster                                                                |
| regex_dna                | 261 ms                                                       | 226 ms: 1.15x faster                                                                |
| go                       | 262 ms                                                       | 228 ms: 1.15x faster                                                                |
| regex_v8                 | 27.2 ms                                                      | 23.7 ms: 1.15x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 83.6 ms: 1.13x faster                                                               |
| sympy_str                | 360 ms                                                       | 318 ms: 1.13x faster                                                                |
| genshi_xml               | 63.3 ms                                                      | 56.5 ms: 1.12x faster                                                               |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                                |
| pycparser                | 1.67 sec                                                     | 1.51 sec: 1.11x faster                                                              |
| pickle_pure_python       | 455 us                                                       | 414 us: 1.10x faster                                                                |
| json                     | 5.86 ms                                                      | 5.36 ms: 1.09x faster                                                               |
| crypto_pyaes             | 119 ms                                                       | 109 ms: 1.09x faster                                                                |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                              |
| nqueens                  | 115 ms                                                       | 106 ms: 1.09x faster                                                                |
| float                    | 111 ms                                                       | 102 ms: 1.09x faster                                                                |
| sympy_expand             | 600 ms                                                       | 559 ms: 1.07x faster                                                                |
| 2to3                     | 350 ms                                                       | 328 ms: 1.07x faster                                                                |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                                                |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.02x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                                |
| xml_etree_process        | 75.9 ms                                                      | 76.9 ms: 1.01x slower                                                               |
| sqlite_synth             | 2.99 us                                                      | 3.04 us: 1.02x slower                                                               |
| pprint_pformat           | 2.15 sec                                                     | 2.32 sec: 1.08x slower                                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 1.14 sec: 1.09x slower                                                              |
| async_generators         | 421 ms                                                       | 459 ms: 1.09x slower                                                                |
| comprehensions           | 26.7 us                                                      | 29.2 us: 1.09x slower                                                               |
| hexiom                   | 9.42 ms                                                      | 10.7 ms: 1.13x slower                                                               |
| regex_effbot             | 3.09 ms                                                      | 3.60 ms: 1.17x slower                                                               |
| meteor_contest           | 138 ms                                                       | 162 ms: 1.17x slower                                                                |
| python_startup_no_site   | 7.33 ms                                                      | 8.69 ms: 1.19x slower                                                               |
| xml_etree_generate       | 92.3 ms                                                      | 111 ms: 1.20x slower                                                                |
| unpickle_pure_python     | 312 us                                                       | 383 us: 1.23x slower                                                                |
| spectral_norm            | 139 ms                                                       | 172 ms: 1.24x slower                                                                |
| mako                     | 14.7 ms                                                      | 18.4 ms: 1.25x slower                                                               |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                               |
| fannkuch                 | 483 ms                                                       | 622 ms: 1.29x slower                                                                |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.33x slower                                                               |
| scimark_fft              | 361 ms                                                       | 479 ms: 1.33x slower                                                                |
| nbody                    | 134 ms                                                       | 198 ms: 1.48x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.65x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 8.59 ms: 1.69x slower                                                               |
| gc_traversal             | 3.42 ms                                                      | 6.27 ms: 1.83x slower                                                               |
| telco                    | 7.23 ms                                                      | 159 ms: 21.96x slower                                                               |
| Geometric mean           | (ref)                                                        | 1.12x faster                                                                        |

Benchmark hidden because not significant (1): tomli_loads
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250722-3.15.0a0-a4de1bf-PYTHON_UOPS/bm-20250722-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-a4de1bf.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.92% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.38x