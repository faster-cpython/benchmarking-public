# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash_cache2
- machine: linux-x86_64
- commit hash: a31e8be
- commit date: 2025-03-20
- overall geometric mean: 1.323x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.29x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 288 ms: 1.22x faster                                                      |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                    |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                     |
| Geometric mean | (ref)                                                        | 1.24x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 660 ms: 2.42x faster                                                      |
| async_tree_none         | 692 ms                                                       | 299 ms: 2.31x faster                                                      |
| async_tree_memoization  | 819 ms                                                       | 359 ms: 2.28x faster                                                      |
| async_tree_cpu_io_mixed | 936 ms                                                       | 528 ms: 1.77x faster                                                      |
| Geometric mean          | (ref)                                                        | 2.18x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.9 ms: 1.55x faster                                                     |
| nbody          | 134 ms                                                       | 103 ms: 1.31x faster                                                      |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                      |
| Geometric mean | (ref)                                                        | 1.29x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 137 ms: 1.39x faster                                                      |
| regex_v8       | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                     |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                      |
| regex_effbot   | 3.09 ms                                                      | 3.01 ms: 1.03x faster                                                     |
| Geometric mean | (ref)                                                        | 1.16x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 224 us: 1.39x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 61.4 ms: 1.24x faster                                                     |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                      |
| json_loads           | 30.3 us                                                      | 26.3 us: 1.15x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 98.8 ms: 1.12x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                     |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                     |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.5 ms: 1.34x faster                                                     |
| mako            | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                     |
| genshi_text     | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                     |
| genshi_xml      | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                                     |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 176 us: 3.05x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 660 ms: 2.42x faster                                                      |
| async_tree_none          | 692 ms                                                       | 299 ms: 2.31x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 359 ms: 2.28x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.34 sec: 2.24x faster                                                    |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                     |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                     |
| go                       | 262 ms                                                       | 133 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 528 ms: 1.77x faster                                                      |
| logging_silent           | 167 ns                                                       | 94.9 ns: 1.76x faster                                                     |
| pylint                   | 566 ms                                                       | 323 ms: 1.75x faster                                                      |
| richards_super           | 90.6 ms                                                      | 53.4 ms: 1.70x faster                                                     |
| chaos                    | 109 ms                                                       | 65.9 ms: 1.65x faster                                                     |
| deepcopy_memo            | 49.8 us                                                      | 30.4 us: 1.64x faster                                                     |
| scimark_monte_carlo      | 107 ms                                                       | 65.6 ms: 1.64x faster                                                     |
| raytrace                 | 489 ms                                                       | 301 ms: 1.63x faster                                                      |
| deepcopy                 | 468 us                                                       | 289 us: 1.62x faster                                                      |
| scimark_lu               | 167 ms                                                       | 103 ms: 1.62x faster                                                      |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                                      |
| richards                 | 75.1 ms                                                      | 47.2 ms: 1.59x faster                                                     |
| pyflate                  | 733 ms                                                       | 464 ms: 1.58x faster                                                      |
| float                    | 111 ms                                                       | 71.9 ms: 1.55x faster                                                     |
| spectral_norm            | 139 ms                                                       | 91.6 ms: 1.52x faster                                                     |
| comprehensions           | 26.7 us                                                      | 17.9 us: 1.49x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 81.5 ms: 1.46x faster                                                     |
| hexiom                   | 9.42 ms                                                      | 6.45 ms: 1.46x faster                                                     |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 224 us: 1.39x faster                                                      |
| regex_compile            | 190 ms                                                       | 137 ms: 1.39x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.56 us: 1.35x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                     |
| django_template          | 50.2 ms                                                      | 37.5 ms: 1.34x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 3.00 us: 1.34x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                      |
| tomli_loads              | 2.92 sec                                                     | 2.19 sec: 1.33x faster                                                    |
| logging_format           | 9.64 us                                                      | 7.31 us: 1.32x faster                                                     |
| mako                     | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                     |
| nbody                    | 134 ms                                                       | 103 ms: 1.31x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                    |
| sqlalchemy_declarative   | 190 ms                                                       | 148 ms: 1.29x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 63.2 ms: 1.28x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                    |
| genshi_text              | 31.4 ms                                                      | 25.0 ms: 1.26x faster                                                     |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 838 ms: 1.25x faster                                                      |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.3 ms: 1.24x faster                                                     |
| fannkuch                 | 483 ms                                                       | 388 ms: 1.24x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 61.4 ms: 1.24x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                     |
| 2to3                     | 350 ms                                                       | 288 ms: 1.22x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 954 us: 1.20x faster                                                      |
| nqueens                  | 115 ms                                                       | 96.7 ms: 1.19x faster                                                     |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                    |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                      |
| json_loads               | 30.3 us                                                      | 26.3 us: 1.15x faster                                                     |
| genshi_xml               | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                                     |
| regex_v8                 | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 98.8 ms: 1.12x faster                                                     |
| scimark_fft              | 361 ms                                                       | 324 ms: 1.12x faster                                                      |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.72 ms: 1.07x faster                                                     |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                      |
| json                     | 5.86 ms                                                      | 5.50 ms: 1.07x faster                                                     |
| xml_etree_generate       | 92.3 ms                                                      | 86.7 ms: 1.06x faster                                                     |
| meteor_contest           | 138 ms                                                       | 130 ms: 1.06x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.05x faster                                                     |
| regex_effbot             | 3.09 ms                                                      | 3.01 ms: 1.03x faster                                                     |
| async_generators         | 421 ms                                                       | 424 ms: 1.01x slower                                                      |
| telco                    | 7.23 ms                                                      | 7.94 ms: 1.10x slower                                                     |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                     |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.43x slower                                                     |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.61x slower                                                     |
| gc_traversal             | 3.42 ms                                                      | 6.38 ms: 1.87x slower                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 1.07 sec: 168.30x slower                                                  |
| Geometric mean           | (ref)                                                        | 1.24x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (24) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250320-3.14.0a6+-a31e8be/bm-20250320-pythonperf2-x86_64-mdboom-tuple_hash_cache2-3.14.0a6+-a31e8be.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.323x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.29x