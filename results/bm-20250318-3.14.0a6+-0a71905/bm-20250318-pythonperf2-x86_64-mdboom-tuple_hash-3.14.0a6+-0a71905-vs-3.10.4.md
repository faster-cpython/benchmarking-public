# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash
- machine: linux-x86_64
- commit hash: 0a71905
- commit date: 2025-03-18
- overall geometric mean: 1.310x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.23x faster                                               |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                             |
| html5lib       | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                              |
| Geometric mean | (ref)                                                        | 1.25x faster                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 650 ms: 2.46x faster                                               |
| async_tree_none         | 692 ms                                                       | 291 ms: 2.38x faster                                               |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                               |
| async_tree_cpu_io_mixed | 936 ms                                                       | 522 ms: 1.79x faster                                               |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.5 ms: 1.53x faster                                              |
| nbody          | 134 ms                                                       | 101 ms: 1.32x faster                                               |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                               |
| Geometric mean | (ref)                                                        | 1.29x faster                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                               |
| regex_v8       | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                              |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                               |
| regex_effbot   | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                              |
| Geometric mean | (ref)                                                        | 1.13x faster                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 225 us: 1.39x faster                                               |
| tomli_loads          | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                             |
| pickle_pure_python   | 455 us                                                       | 338 us: 1.34x faster                                               |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                              |
| xml_etree_process    | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                              |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.17x faster                                               |
| json_loads           | 30.3 us                                                      | 26.1 us: 1.16x faster                                              |
| xml_etree_iterparse  | 110 ms                                                       | 98.9 ms: 1.12x faster                                              |
| xml_etree_generate   | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                              |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                              |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                              |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                              |
| genshi_text     | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                              |
| mako            | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                              |
| genshi_xml      | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                              |
| Geometric mean  | (ref)                                                        | 1.29x faster                                                       |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                               |
| async_tree_io            | 1.60 sec                                                     | 650 ms: 2.46x faster                                               |
| async_tree_none          | 692 ms                                                       | 291 ms: 2.38x faster                                               |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                               |
| deltablue                | 7.50 ms                                                      | 3.36 ms: 2.23x faster                                              |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.96x faster                                              |
| go                       | 262 ms                                                       | 134 ms: 1.95x faster                                               |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 522 ms: 1.79x faster                                               |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                               |
| logging_silent           | 167 ns                                                       | 95.1 ns: 1.76x faster                                              |
| deepcopy_memo            | 49.8 us                                                      | 29.5 us: 1.69x faster                                              |
| chaos                    | 109 ms                                                       | 65.2 ms: 1.67x faster                                              |
| scimark_lu               | 167 ms                                                       | 101 ms: 1.64x faster                                               |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                               |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.63x faster                                               |
| richards_super           | 90.6 ms                                                      | 55.8 ms: 1.63x faster                                              |
| scimark_monte_carlo      | 107 ms                                                       | 66.2 ms: 1.62x faster                                              |
| deepcopy                 | 468 us                                                       | 296 us: 1.58x faster                                               |
| pyflate                  | 733 ms                                                       | 464 ms: 1.58x faster                                               |
| spectral_norm            | 139 ms                                                       | 90.2 ms: 1.54x faster                                              |
| float                    | 111 ms                                                       | 72.5 ms: 1.53x faster                                              |
| richards                 | 75.1 ms                                                      | 49.5 ms: 1.52x faster                                              |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                              |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                              |
| hexiom                   | 9.42 ms                                                      | 6.51 ms: 1.45x faster                                              |
| crypto_pyaes             | 119 ms                                                       | 84.7 ms: 1.41x faster                                              |
| unpickle_pure_python     | 312 us                                                       | 225 us: 1.39x faster                                               |
| django_template          | 50.2 ms                                                      | 36.4 ms: 1.38x faster                                              |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                               |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                              |
| tomli_loads              | 2.92 sec                                                     | 2.14 sec: 1.36x faster                                             |
| html5lib                 | 94.6 ms                                                      | 70.2 ms: 1.35x faster                                              |
| pickle_pure_python       | 455 us                                                       | 338 us: 1.34x faster                                               |
| thrift                   | 1.18 ms                                                      | 875 us: 1.34x faster                                               |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                              |
| genshi_text              | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                              |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.32x faster                                              |
| nbody                    | 134 ms                                                       | 101 ms: 1.32x faster                                               |
| deepcopy_reduce          | 4.01 us                                                      | 3.08 us: 1.30x faster                                              |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                             |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                               |
| dulwich_log              | 81.1 ms                                                      | 62.8 ms: 1.29x faster                                              |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                             |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                              |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.0 ms: 1.26x faster                                              |
| pprint_safe_repr         | 1.05 sec                                                     | 835 ms: 1.26x faster                                               |
| xml_etree_process        | 75.9 ms                                                      | 60.5 ms: 1.26x faster                                              |
| sympy_sum                | 193 ms                                                       | 155 ms: 1.25x faster                                               |
| fannkuch                 | 483 ms                                                       | 388 ms: 1.24x faster                                               |
| pathlib                  | 21.4 ms                                                      | 17.2 ms: 1.24x faster                                              |
| 2to3                     | 350 ms                                                       | 286 ms: 1.23x faster                                               |
| sympy_str                | 360 ms                                                       | 297 ms: 1.21x faster                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                              |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                             |
| bench_thread_pool        | 1.14 ms                                                      | 952 us: 1.20x faster                                               |
| nqueens                  | 115 ms                                                       | 96.1 ms: 1.20x faster                                              |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                               |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                             |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.17x faster                                               |
| json_loads               | 30.3 us                                                      | 26.1 us: 1.16x faster                                              |
| scimark_fft              | 361 ms                                                       | 314 ms: 1.15x faster                                               |
| regex_v8                 | 27.2 ms                                                      | 23.9 ms: 1.14x faster                                              |
| genshi_xml               | 63.3 ms                                                      | 55.8 ms: 1.13x faster                                              |
| xml_etree_iterparse      | 110 ms                                                       | 98.9 ms: 1.12x faster                                              |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.09x faster                                               |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                              |
| xml_etree_generate       | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                              |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                               |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                               |
| sqlite_synth             | 2.99 us                                                      | 2.83 us: 1.06x faster                                              |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.85 ms: 1.05x faster                                              |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                               |
| regex_effbot             | 3.09 ms                                                      | 3.17 ms: 1.03x slower                                              |
| telco                    | 7.23 ms                                                      | 8.02 ms: 1.11x slower                                              |
| coverage                 | 63.3 ms                                                      | 80.6 ms: 1.27x slower                                              |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                              |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                              |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.59x slower                                              |
| gc_traversal             | 3.42 ms                                                      | 6.61 ms: 1.93x slower                                              |
| bench_mp_pool            | 6.37 ms                                                      | 1.22 sec: 192.05x slower                                           |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                       |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250318-3.14.0a6+-0a71905/bm-20250318-pythonperf2-x86_64-mdboom-tuple_hash-3.14.0a6+-0a71905.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.310x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.28x