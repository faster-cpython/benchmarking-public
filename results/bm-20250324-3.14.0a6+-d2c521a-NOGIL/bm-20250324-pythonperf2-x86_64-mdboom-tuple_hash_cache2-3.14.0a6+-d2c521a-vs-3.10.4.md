# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: d2c521a
- commit date: 2025-03-24
- overall geometric mean: 1.214x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: 1.57x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 325 ms: 1.08x faster                                                      |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                    |
| html5lib       | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                     |
| Geometric mean | (ref)                                                        | 1.17x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 587 ms: 2.72x faster                                                      |
| async_tree_none         | 692 ms                                                       | 283 ms: 2.44x faster                                                      |
| async_tree_memoization  | 819 ms                                                       | 342 ms: 2.39x faster                                                      |
| async_tree_cpu_io_mixed | 936 ms                                                       | 511 ms: 1.83x faster                                                      |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 76.8 ms: 1.45x faster                                                     |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                      |
| nbody          | 134 ms                                                       | 131 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                        | 1.17x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 161 ms: 1.18x faster                                                      |
| regex_v8       | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                     |
| regex_dna      | 261 ms                                                       | 234 ms: 1.11x faster                                                      |
| Geometric mean | (ref)                                                        | 1.11x faster                                                              |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 247 us: 1.26x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 88.8 ms: 1.24x faster                                                     |
| pickle_pure_python   | 455 us                                                       | 372 us: 1.22x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 13.2 ms: 1.10x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 69.7 ms: 1.09x faster                                                     |
| json_loads           | 30.3 us                                                      | 29.1 us: 1.04x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 97.2 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                        | 1.14x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 19.5 ms: 1.69x slower                                                     |
| python_startup_no_site | 7.33 ms                                                      | 13.8 ms: 1.89x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.79x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.8 ms: 1.10x faster                                                     |
| genshi_text     | 31.4 ms                                                      | 30.4 ms: 1.03x faster                                                     |
| mako            | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                              |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 587 ms: 2.72x faster                                                      |
| typing_runtime_protocols | 537 us                                                       | 218 us: 2.46x faster                                                      |
| async_tree_none          | 692 ms                                                       | 283 ms: 2.44x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 342 ms: 2.39x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.57 sec: 1.92x faster                                                    |
| generators               | 57.3 ms                                                      | 30.3 ms: 1.89x faster                                                     |
| deltablue                | 7.50 ms                                                      | 4.04 ms: 1.86x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 511 ms: 1.83x faster                                                      |
| go                       | 262 ms                                                       | 151 ms: 1.74x faster                                                      |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                      |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                      |
| gc_traversal             | 3.42 ms                                                      | 2.12 ms: 1.61x faster                                                     |
| chaos                    | 109 ms                                                       | 69.8 ms: 1.56x faster                                                     |
| scimark_sor              | 180 ms                                                       | 121 ms: 1.49x faster                                                      |
| raytrace                 | 489 ms                                                       | 330 ms: 1.48x faster                                                      |
| pyflate                  | 733 ms                                                       | 497 ms: 1.47x faster                                                      |
| float                    | 111 ms                                                       | 76.8 ms: 1.45x faster                                                     |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                     |
| deepcopy                 | 468 us                                                       | 333 us: 1.41x faster                                                      |
| richards_super           | 90.6 ms                                                      | 65.7 ms: 1.38x faster                                                     |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.37x faster                                                      |
| scimark_lu               | 167 ms                                                       | 123 ms: 1.36x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 36.9 us: 1.35x faster                                                     |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                    |
| richards                 | 75.1 ms                                                      | 56.9 ms: 1.32x faster                                                     |
| comprehensions           | 26.7 us                                                      | 20.2 us: 1.32x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 73.4 ms: 1.29x faster                                                     |
| scimark_monte_carlo      | 107 ms                                                       | 83.8 ms: 1.28x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 247 us: 1.26x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 64.3 ms: 1.26x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 7.48 ms: 1.26x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 88.8 ms: 1.24x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 96.0 ms: 1.24x faster                                                     |
| logging_simple           | 8.88 us                                                      | 7.18 us: 1.24x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.22x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 372 us: 1.22x faster                                                      |
| logging_format           | 9.64 us                                                      | 7.95 us: 1.21x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.44 sec: 1.20x faster                                                    |
| regex_compile            | 190 ms                                                       | 161 ms: 1.18x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 23.1 ms: 1.17x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 900 ms: 1.17x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.85 sec: 1.17x faster                                                    |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                    |
| sqlite_synth             | 2.99 us                                                      | 2.59 us: 1.15x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 3.56 us: 1.13x faster                                                     |
| regex_dna                | 261 ms                                                       | 234 ms: 1.11x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 13.2 ms: 1.10x faster                                                     |
| sqlalchemy_declarative   | 190 ms                                                       | 172 ms: 1.10x faster                                                      |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                      |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.6 ms: 1.10x faster                                                     |
| django_template          | 50.2 ms                                                      | 45.8 ms: 1.10x faster                                                     |
| xml_etree_process        | 75.9 ms                                                      | 69.7 ms: 1.09x faster                                                     |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                      |
| 2to3                     | 350 ms                                                       | 325 ms: 1.08x faster                                                      |
| sympy_str                | 360 ms                                                       | 336 ms: 1.07x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 26.5 ms: 1.06x faster                                                     |
| sympy_expand             | 600 ms                                                       | 566 ms: 1.06x faster                                                      |
| json_loads               | 30.3 us                                                      | 29.1 us: 1.04x faster                                                     |
| json                     | 5.86 ms                                                      | 5.64 ms: 1.04x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 30.4 ms: 1.03x faster                                                     |
| nqueens                  | 115 ms                                                       | 111 ms: 1.03x faster                                                      |
| scimark_fft              | 361 ms                                                       | 352 ms: 1.03x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 381 ms: 1.02x faster                                                      |
| nbody                    | 134 ms                                                       | 131 ms: 1.02x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 97.2 ms: 1.05x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 1.90 ms: 1.08x slower                                                     |
| async_generators         | 421 ms                                                       | 465 ms: 1.11x slower                                                      |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.78 ms: 1.14x slower                                                     |
| mako                     | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 1.44 ms: 1.26x slower                                                     |
| telco                    | 7.23 ms                                                      | 9.46 ms: 1.31x slower                                                     |
| python_startup           | 11.5 ms                                                      | 19.5 ms: 1.69x slower                                                     |
| coverage                 | 63.3 ms                                                      | 116 ms: 1.84x slower                                                      |
| python_startup_no_site   | 7.33 ms                                                      | 13.8 ms: 1.89x slower                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 50.4 ms: 7.91x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.18x faster                                                              |

Benchmark hidden because not significant (3): fannkuch, regex_effbot, genshi_xml
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250324-3.14.0a6+-d2c521a-NOGIL/bm-20250324-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-d2c521a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.214x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.14x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: 1.57x