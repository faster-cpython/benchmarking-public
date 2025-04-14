# Results vs. 3.10.4

- fork: mdboom
- ref: tuple_hash_cache
- machine: linux-x86_64
- commit hash: bd82b00
- commit date: 2025-03-19
- overall geometric mean: 1.309x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 289 ms: 1.21x faster                                                     |
| docutils       | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                   |
| html5lib       | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                    |
| Geometric mean | (ref)                                                        | 1.24x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 649 ms: 2.46x faster                                                     |
| async_tree_none         | 692 ms                                                       | 300 ms: 2.31x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 357 ms: 2.30x faster                                                     |
| async_tree_cpu_io_mixed | 936 ms                                                       | 529 ms: 1.77x faster                                                     |
| Geometric mean          | (ref)                                                        | 2.19x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.7 ms: 1.55x faster                                                    |
| nbody          | 134 ms                                                       | 104 ms: 1.28x faster                                                     |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                        | 1.28x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 138 ms: 1.38x faster                                                     |
| regex_v8       | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                    |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                     |
| regex_effbot   | 3.09 ms                                                      | 3.23 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                        | 1.12x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 222 us: 1.40x faster                                                     |
| tomli_loads          | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                                   |
| pickle_pure_python   | 455 us                                                       | 346 us: 1.32x faster                                                     |
| xml_etree_process    | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                                    |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                    |
| xml_etree_parse      | 160 ms                                                       | 137 ms: 1.17x faster                                                     |
| json_loads           | 30.3 us                                                      | 26.6 us: 1.14x faster                                                    |
| xml_etree_iterparse  | 110 ms                                                       | 100 ms: 1.10x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                    |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                    |
| python_startup_no_site | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.43x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 37.9 ms: 1.33x faster                                                    |
| mako            | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.24x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.04x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 649 ms: 2.46x faster                                                     |
| async_tree_none          | 692 ms                                                       | 300 ms: 2.31x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 357 ms: 2.30x faster                                                     |
| mdp                      | 3.01 sec                                                     | 1.36 sec: 2.21x faster                                                   |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                    |
| generators               | 57.3 ms                                                      | 29.0 ms: 1.98x faster                                                    |
| go                       | 262 ms                                                       | 135 ms: 1.95x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 529 ms: 1.77x faster                                                     |
| logging_silent           | 167 ns                                                       | 95.4 ns: 1.75x faster                                                    |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                     |
| deepcopy_memo            | 49.8 us                                                      | 29.4 us: 1.69x faster                                                    |
| richards_super           | 90.6 ms                                                      | 53.6 ms: 1.69x faster                                                    |
| scimark_lu               | 167 ms                                                       | 100 ms: 1.66x faster                                                     |
| raytrace                 | 489 ms                                                       | 298 ms: 1.64x faster                                                     |
| chaos                    | 109 ms                                                       | 67.1 ms: 1.62x faster                                                    |
| scimark_sor              | 180 ms                                                       | 111 ms: 1.62x faster                                                     |
| pyflate                  | 733 ms                                                       | 461 ms: 1.59x faster                                                     |
| deepcopy                 | 468 us                                                       | 297 us: 1.58x faster                                                     |
| richards                 | 75.1 ms                                                      | 47.7 ms: 1.57x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 68.9 ms: 1.56x faster                                                    |
| float                    | 111 ms                                                       | 71.7 ms: 1.55x faster                                                    |
| spectral_norm            | 139 ms                                                       | 90.9 ms: 1.53x faster                                                    |
| comprehensions           | 26.7 us                                                      | 17.8 us: 1.50x faster                                                    |
| hexiom                   | 9.42 ms                                                      | 6.48 ms: 1.45x faster                                                    |
| crypto_pyaes             | 119 ms                                                       | 82.4 ms: 1.45x faster                                                    |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                    |
| unpickle_pure_python     | 312 us                                                       | 222 us: 1.40x faster                                                     |
| regex_compile            | 190 ms                                                       | 138 ms: 1.38x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 69.9 ms: 1.35x faster                                                    |
| tomli_loads              | 2.92 sec                                                     | 2.17 sec: 1.34x faster                                                   |
| deepcopy_reduce          | 4.01 us                                                      | 3.02 us: 1.33x faster                                                    |
| django_template          | 50.2 ms                                                      | 37.9 ms: 1.33x faster                                                    |
| pickle_pure_python       | 455 us                                                       | 346 us: 1.32x faster                                                     |
| logging_format           | 9.64 us                                                      | 7.34 us: 1.31x faster                                                    |
| logging_simple           | 8.88 us                                                      | 6.76 us: 1.31x faster                                                    |
| thrift                   | 1.18 ms                                                      | 897 us: 1.31x faster                                                     |
| mako                     | 14.7 ms                                                      | 11.2 ms: 1.31x faster                                                    |
| dulwich_log              | 81.1 ms                                                      | 63.0 ms: 1.29x faster                                                    |
| pycparser                | 1.67 sec                                                     | 1.30 sec: 1.29x faster                                                   |
| nbody                    | 134 ms                                                       | 104 ms: 1.28x faster                                                     |
| pprint_pformat           | 2.15 sec                                                     | 1.69 sec: 1.27x faster                                                   |
| sqlalchemy_declarative   | 190 ms                                                       | 149 ms: 1.27x faster                                                     |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                    |
| fannkuch                 | 483 ms                                                       | 382 ms: 1.26x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 836 ms: 1.26x faster                                                     |
| xml_etree_process        | 75.9 ms                                                      | 60.6 ms: 1.25x faster                                                    |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.24x faster                                                    |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.5 ms: 1.23x faster                                                    |
| sympy_sum                | 193 ms                                                       | 157 ms: 1.23x faster                                                     |
| 2to3                     | 350 ms                                                       | 289 ms: 1.21x faster                                                     |
| sympy_str                | 360 ms                                                       | 301 ms: 1.20x faster                                                     |
| nqueens                  | 115 ms                                                       | 96.1 ms: 1.20x faster                                                    |
| sympy_integrate          | 28.2 ms                                                      | 23.6 ms: 1.19x faster                                                    |
| bench_thread_pool        | 1.14 ms                                                      | 968 us: 1.18x faster                                                     |
| sympy_expand             | 600 ms                                                       | 512 ms: 1.17x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 137 ms: 1.17x faster                                                     |
| docutils                 | 3.41 sec                                                     | 2.94 sec: 1.16x faster                                                   |
| json_loads               | 30.3 us                                                      | 26.6 us: 1.14x faster                                                    |
| regex_v8                 | 27.2 ms                                                      | 24.0 ms: 1.13x faster                                                    |
| scimark_fft              | 361 ms                                                       | 325 ms: 1.11x faster                                                     |
| xml_etree_iterparse      | 110 ms                                                       | 100 ms: 1.10x faster                                                     |
| genshi_xml               | 63.3 ms                                                      | 58.3 ms: 1.09x faster                                                    |
| xml_etree_generate       | 92.3 ms                                                      | 85.1 ms: 1.08x faster                                                    |
| meteor_contest           | 138 ms                                                       | 129 ms: 1.08x faster                                                     |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                     |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                     |
| sqlite_synth             | 2.99 us                                                      | 2.82 us: 1.06x faster                                                    |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.84 ms: 1.05x faster                                                    |
| json                     | 5.86 ms                                                      | 5.59 ms: 1.05x faster                                                    |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                     |
| async_generators         | 421 ms                                                       | 432 ms: 1.03x slower                                                     |
| regex_effbot             | 3.09 ms                                                      | 3.23 ms: 1.05x slower                                                    |
| telco                    | 7.23 ms                                                      | 8.22 ms: 1.14x slower                                                    |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                    |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 10.5 ms: 1.44x slower                                                    |
| create_gc_cycles         | 1.76 ms                                                      | 2.83 ms: 1.60x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 6.39 ms: 1.87x slower                                                    |
| bench_mp_pool            | 6.37 ms                                                      | 1.58 sec: 247.80x slower                                                 |
| Geometric mean           | (ref)                                                        | 1.22x faster                                                             |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250319-3.14.0a6+-bd82b00/bm-20250319-pythonperf2-x86_64-mdboom-tuple_hash_cache-3.14.0a6+-bd82b00.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.309x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x