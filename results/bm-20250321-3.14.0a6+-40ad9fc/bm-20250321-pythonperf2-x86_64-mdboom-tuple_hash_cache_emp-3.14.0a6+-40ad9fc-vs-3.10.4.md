# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash_cache_emp
- machine: linux-x86_64
- commit hash: 40ad9fc
- commit date: 2025-03-21
- overall geometric mean: 1.320x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none         | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 354 ms: 2.32x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 525 ms: 1.78x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.21x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.1 ms: 1.54x faster                                                        |
| nbody          | 134 ms                                                       | 105 ms: 1.27x faster                                                         |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 222 us: 1.40x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 340 us: 1.34x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.20 sec: 1.32x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 61.5 ms: 1.23x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| json_loads           | 30.3 us                                                      | 26.2 us: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.7 ms: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.23x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 36.6 ms: 1.37x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                        |
| mako            | 14.7 ms                                                      | 11.4 ms: 1.29x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.13x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 642 ms: 2.49x faster                                                         |
| async_tree_none          | 692 ms                                                       | 297 ms: 2.33x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 354 ms: 2.32x faster                                                         |
| mdp                      | 3.01 sec                                                     | 1.31 sec: 2.29x faster                                                       |
| deltablue                | 7.50 ms                                                      | 3.40 ms: 2.20x faster                                                        |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                        |
| go                       | 262 ms                                                       | 132 ms: 1.99x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 525 ms: 1.78x faster                                                         |
| logging_silent           | 167 ns                                                       | 94.1 ns: 1.78x faster                                                        |
| pylint                   | 566 ms                                                       | 320 ms: 1.77x faster                                                         |
| richards_super           | 90.6 ms                                                      | 53.5 ms: 1.69x faster                                                        |
| chaos                    | 109 ms                                                       | 64.2 ms: 1.69x faster                                                        |
| scimark_lu               | 167 ms                                                       | 99.3 ms: 1.68x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.68x faster                                                        |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                                         |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                         |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 68.8 ms: 1.56x faster                                                        |
| pyflate                  | 733 ms                                                       | 471 ms: 1.56x faster                                                         |
| richards                 | 75.1 ms                                                      | 48.3 ms: 1.55x faster                                                        |
| float                    | 111 ms                                                       | 72.1 ms: 1.54x faster                                                        |
| spectral_norm            | 139 ms                                                       | 90.3 ms: 1.54x faster                                                        |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.51 ms: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 84.2 ms: 1.41x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.40x faster                                                         |
| django_template          | 50.2 ms                                                      | 36.6 ms: 1.37x faster                                                        |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.59 us: 1.35x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 340 us: 1.34x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                        |
| logging_format           | 9.64 us                                                      | 7.26 us: 1.33x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.7 ms: 1.33x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.20 sec: 1.32x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 146 ms: 1.30x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 63.0 ms: 1.29x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                       |
| mako                     | 14.7 ms                                                      | 11.4 ms: 1.29x faster                                                        |
| nbody                    | 134 ms                                                       | 105 ms: 1.27x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 825 ms: 1.27x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.5 ms: 1.26x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.1 ms: 1.26x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                        |
| fannkuch                 | 483 ms                                                       | 388 ms: 1.24x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 61.5 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                         |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                        |
| nqueens                  | 115 ms                                                       | 96.7 ms: 1.19x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 961 us: 1.19x faster                                                         |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.2 us: 1.16x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.9 ms: 1.15x faster                                                        |
| scimark_fft              | 361 ms                                                       | 316 ms: 1.14x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 97.7 ms: 1.13x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 24.4 ms: 1.11x faster                                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                         |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.69 ms: 1.08x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 415 ms: 1.02x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.12 ms: 1.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 8.19 ms: 1.13x slower                                                        |
| coverage                 | 63.3 ms                                                      | 82.4 ms: 1.30x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.4 ms: 1.42x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.43x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.61 ms: 1.94x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.65 sec: 259.12x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250321-3.14.0a6+-40ad9fc/bm-20250321-pythonperf2-x86_64-mdboom-tuple_hash_cache_emp-3.14.0a6+-40ad9fc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.320x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x