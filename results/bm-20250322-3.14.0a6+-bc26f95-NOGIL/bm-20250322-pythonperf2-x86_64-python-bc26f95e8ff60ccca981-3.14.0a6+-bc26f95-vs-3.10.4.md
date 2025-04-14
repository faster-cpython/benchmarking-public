# Results vs. 3.10.4

- fork: python
- ref: bc26f95e8ff60ccca981
- machine: linux-x86_64
- commit hash: bc26f95
- commit date: 2025-03-22
- overall geometric mean: 1.202x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: 1.56x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 326 ms: 1.07x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                        |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 579 ms: 2.76x faster                                                         |
| async_tree_none         | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 337 ms: 2.43x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 507 ms: 1.85x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.36x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 76.8 ms: 1.45x faster                                                        |
| pidigits       | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| nbody          | 134 ms                                                       | 132 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 160 ms: 1.19x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 244 us: 1.28x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 88.1 ms: 1.25x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 370 us: 1.23x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| json_dumps           | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.5 ms: 1.09x faster                                                        |
| json_loads           | 30.3 us                                                      | 29.7 us: 1.02x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 96.3 ms: 1.04x slower                                                        |
| unpickle             | 13.5 us                                                      | 15.8 us: 1.17x slower                                                        |
| pickle_list          | 4.12 us                                                      | 4.85 us: 1.18x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.51 us: 1.18x slower                                                        |
| pickle_dict          | 29.5 us                                                      | 35.0 us: 1.19x slower                                                        |
| pickle               | 9.89 us                                                      | 12.0 us: 1.22x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 19.4 ms: 1.69x slower                                                        |
| python_startup_no_site | 7.33 ms                                                      | 13.8 ms: 1.88x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.78x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 45.5 ms: 1.10x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 30.5 ms: 1.03x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 63.8 ms: 1.01x slower                                                        |
| mako            | 14.7 ms                                                      | 17.7 ms: 1.21x slower                                                        |
| Geometric mean  | (ref)                                                        | 1.02x slower                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 579 ms: 2.76x faster                                                         |
| async_tree_none          | 692 ms                                                       | 278 ms: 2.49x faster                                                         |
| typing_runtime_protocols | 537 us                                                       | 217 us: 2.47x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 337 ms: 2.43x faster                                                         |
| generators               | 57.3 ms                                                      | 29.9 ms: 1.92x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.02 ms: 1.87x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 507 ms: 1.85x faster                                                         |
| asyncio_tcp              | 779 ms                                                       | 424 ms: 1.84x faster                                                         |
| go                       | 262 ms                                                       | 151 ms: 1.74x faster                                                         |
| logging_silent           | 167 ns                                                       | 101 ns: 1.66x faster                                                         |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.88 sec: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                         |
| gc_traversal             | 3.42 ms                                                      | 2.18 ms: 1.56x faster                                                        |
| chaos                    | 109 ms                                                       | 69.5 ms: 1.56x faster                                                        |
| pyflate                  | 733 ms                                                       | 489 ms: 1.50x faster                                                         |
| scimark_sor              | 180 ms                                                       | 121 ms: 1.49x faster                                                         |
| raytrace                 | 489 ms                                                       | 333 ms: 1.47x faster                                                         |
| float                    | 111 ms                                                       | 76.8 ms: 1.45x faster                                                        |
| deepcopy                 | 468 us                                                       | 328 us: 1.43x faster                                                         |
| coroutines               | 30.3 ms                                                      | 21.3 ms: 1.42x faster                                                        |
| richards_super           | 90.6 ms                                                      | 65.6 ms: 1.38x faster                                                        |
| spectral_norm            | 139 ms                                                       | 101 ms: 1.38x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 36.1 us: 1.38x faster                                                        |
| scimark_lu               | 167 ms                                                       | 122 ms: 1.37x faster                                                         |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.34x faster                                                       |
| richards                 | 75.1 ms                                                      | 57.0 ms: 1.32x faster                                                        |
| comprehensions           | 26.7 us                                                      | 20.5 us: 1.30x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 244 us: 1.28x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.39 ms: 1.27x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 64.5 ms: 1.26x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 85.4 ms: 1.26x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 95.0 ms: 1.26x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 88.1 ms: 1.25x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 370 us: 1.23x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                        |
| logging_simple           | 8.88 us                                                      | 7.31 us: 1.21x faster                                                        |
| thrift                   | 1.18 ms                                                      | 973 us: 1.21x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.42 sec: 1.21x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 134 ms: 1.19x faster                                                         |
| logging_format           | 9.64 us                                                      | 8.12 us: 1.19x faster                                                        |
| regex_compile            | 190 ms                                                       | 160 ms: 1.19x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.57 us: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.95 sec: 1.16x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 909 ms: 1.15x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.88 sec: 1.15x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.51 us: 1.14x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 20.6 ms: 1.10x faster                                                        |
| django_template          | 50.2 ms                                                      | 45.5 ms: 1.10x faster                                                        |
| sympy_sum                | 193 ms                                                       | 175 ms: 1.10x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 172 ms: 1.10x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 13.3 ms: 1.09x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 69.5 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 249 ms: 1.09x faster                                                         |
| mdp                      | 3.01 sec                                                     | 2.77 sec: 1.08x faster                                                       |
| 2to3                     | 350 ms                                                       | 326 ms: 1.07x faster                                                         |
| sympy_str                | 360 ms                                                       | 336 ms: 1.07x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.3 ms: 1.07x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 26.5 ms: 1.06x faster                                                        |
| sympy_expand             | 600 ms                                                       | 565 ms: 1.06x faster                                                         |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 375 ms: 1.04x faster                                                         |
| nqueens                  | 115 ms                                                       | 111 ms: 1.04x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 30.5 ms: 1.03x faster                                                        |
| json                     | 5.86 ms                                                      | 5.69 ms: 1.03x faster                                                        |
| scimark_fft              | 361 ms                                                       | 353 ms: 1.02x faster                                                         |
| json_loads               | 30.3 us                                                      | 29.7 us: 1.02x faster                                                        |
| fannkuch                 | 483 ms                                                       | 474 ms: 1.02x faster                                                         |
| nbody                    | 134 ms                                                       | 132 ms: 1.01x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 63.8 ms: 1.01x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.18 ms: 1.03x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 96.3 ms: 1.04x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 62.8 ns: 1.05x slower                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.62 ms: 1.11x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 1.95 ms: 1.11x slower                                                        |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                         |
| async_generators         | 421 ms                                                       | 480 ms: 1.14x slower                                                         |
| unpickle                 | 13.5 us                                                      | 15.8 us: 1.17x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.85 us: 1.18x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.51 us: 1.18x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 35.0 us: 1.19x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.7 ms: 1.21x slower                                                        |
| pickle                   | 9.89 us                                                      | 12.0 us: 1.22x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.45 ms: 1.27x slower                                                        |
| telco                    | 7.23 ms                                                      | 9.62 ms: 1.33x slower                                                        |
| python_startup           | 11.5 ms                                                      | 19.4 ms: 1.69x slower                                                        |
| coverage                 | 63.3 ms                                                      | 118 ms: 1.87x slower                                                         |
| python_startup_no_site   | 7.33 ms                                                      | 13.8 ms: 1.88x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 50.4 ms: 7.90x slower                                                        |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                 |
Ignored benchmarks (11) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250322-3.14.0a6+-bc26f95-NOGIL/bm-20250322-pythonperf2-x86_64-python-bc26f95e8ff60ccca981-3.14.0a6+-bc26f95.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.202x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.13x
- 95% likely to have a speedup of 1.10x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: 1.56x